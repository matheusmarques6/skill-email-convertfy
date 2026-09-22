# Super prompt: módulo Planejamento de Campanhas (mensal) + temporada BFCM 2026

Cole este arquivo inteiro no Claude Code, na raiz do repositório `admin-convertfy`, depois de copiar a pasta do pacote para `docs/planejamento-campanhas/` (seed, html, img, dados, obsidian, docs).

---

## 0. Papel e regras de trabalho

Você é o engenheiro responsável por construir, dentro do admin da Convertfy, o módulo que planeja, produz e acompanha o calendário de campanhas de e-mail de todas as lojas, todo mês. O primeiro uso é a temporada de outubro a dezembro de 2026 (10.10, 11.11, Black Friday, Cyber Monday e dezembro), mas nada pode ser específico da Black Friday: a Black é o primeiro **plano** do sistema.

Regras:

1. **Leia antes de escrever.** Antes de qualquer migration ou componente, leia: `src/types/campaign-central.ts`, `supabase/migrations/20260716_campaign_central.sql` e as migrations `2026*campaign*`, `src/lib/services/campaign-central/*` (em especial `suggestion-engine`, `suggestion-approval`, `production`, `board`, `campaign-store-email`, `copy-master`, `campaign-design-*`), `src/components/campaign-central/*`, `src/app/(app)/admin/campaigns/central/*`, `src/lib/ai/connectors/*`, `src/lib/ai/convertia/*`, `src/lib/routes.ts`, `src/components/layout/nav-config.ts`. Siga as convenções que já estão lá (services em `lib/services`, hooks SWR, `requireAuth` + `getUserOrgRole`, `successResponse`/`errorResponse`, logger, testes vitest ao lado do service, `loading.tsx` nas rotas, componentes shadcn, copy em pt-BR).
2. **Estenda, não duplique.** A Central de Campanhas já tem o fluxo mestre → loja: `campaign_suggestions` (campanha mestre com `targets`, `brief`, `copy_results` por loja, `pilot_store_ids`, pipeline de design) e `campaign_store_emails` (peça por loja). O planejamento gera `campaign_suggestions`. Não crie um segundo fluxo de produção.
3. **Nada de dado inventado na UI.** Todo número mostrado vem de tabela ou view. Se faltar dado, a UI mostra "sem dado" e o motivo.
4. **Server Components por padrão.** Use `"use client"` só onde há interação. Nada de waterfall de fetch no cliente (a auditoria do projeto já apontou isso).
5. **RLS em toda tabela nova**, com policy por `org_id` igual às tabelas da Central.
6. **Entregue por fases** (seção 9). Ao fim de cada fase: `pnpm typecheck`, `pnpm lint`, `pnpm test`, e um resumo do que mudou.
7. Antes de começar, avise que as tabelas `bkp_email_intents_20260917` e `bkp_dispositivo_20260917` estão sem RLS e pergunte se apaga ou habilita. Não altere sem resposta.

---

## 1. O que o sistema resolve

Hoje o calendário mensal é montado à mão, fica num documento, e ninguém sabe no dia 15 qual e-mail de qual loja está atrasado, nem se o modelo escolhido ainda vende. O módulo precisa:

1. **Planejar** o mês (ou a temporada) num calendário mestre, com cada envio justificado por dado.
2. **Explicar** cada envio: por que está ali, qual dado sustenta, qual e-mail validado serve de base, como produzir e o que melhorar.
3. **Distribuir** o plano para as lojas, aplicando nível da conta, lista pequena, idioma, mercado, trilha local e oferta.
4. **Acompanhar** a produção de cada envio em cada loja (copy, design, HTML, QA, agendado, enviado).
5. **Medir** o resultado de cada envio com o mesmo índice da pesquisa e realimentar o ranking dos modelos, que decide o plano do mês seguinte.
6. **Conversar** com a ConvertIA sobre tudo isso, inclusive pedir alterações com aprovação humana.

---

## 2. Princípio de decisão: 80 / 10 / 10

Regra do Bruno para qualquer plano:

- **Validado, no mínimo 80% dos envios:** modelo com mediana do índice ≥ 1 em pelo menos uma amostra da carteira, ou parte da sequência de pico validada.
- **Inspiração, até 10%:** prática externa que vem dando certo (Wellcopy, Max, Trendtrack) sem dado nosso.
- **Complemento, o restante:** envio operacional ou teste sem referência (reativação, 00h).

O sistema calcula a composição de cada plano em tempo real, mostra no topo do plano, bloqueia a aprovação abaixo de 80% validado e alerta acima de 10% em inspiração ou complemento. O nível de evidência de cada envio vem do status do modelo (seção 3.1), com override manual justificado.

---

## 3. Modelo de dados

Crie uma migration `supabase/migrations/2026MMDD_planejamento_campanhas.sql`. Nomes em português, seguindo `conteudo_*` e `transcricoes_*` do projeto. Ajuste tipos às convenções existentes.

### 3.1 Biblioteca de modelos

```
campanha_modelos
  id uuid pk, org_id uuid, key text unique por org,
  nome text, papel text check (antecipacao|soft|hard_pico|hard_fora),
  estrutura text check (A|B|C|D),
  status text check (validado|parcial|revisar|reserva|fora|teste),
  assuntos jsonb            -- {pt, en, fr, de, es}
  aliases_evento text[]     -- 4º campo do nome da campanha na Omnisend
  alias_hora text null      -- "07:00", "11:00", "18:00" para modelos de pico
  html_template_path text   -- ex. docs/planejamento-campanhas/html/A-status-mudou.html
  referencia jsonb          -- {imagens: [...], figma: "..."}
  copiar text, melhorar text,
  nota_vault text           -- path da nota em ai_knowledge_notes
  amostra_estudo jsonb      -- snapshot da amostra de 9 lojas (congelado)
  created_at, updated_at
```

Seed: `docs/planejamento-campanhas/seed/modelos.json` (29 modelos). As imagens de `docs/planejamento-campanhas/img/` sobem para o Storage (bucket novo `campanha-modelos`, público só para autenticados) e o path vai em `referencia.imagens`.

### 3.2 Índice vivo dos modelos

A tabela `omnisend_campaign_metrics` tem 16.867 linhas de 53 lojas, com **duplicatas por `period_label`** e, antes de meados de junho de 2026, linhas sem conversão. Por isso:

1. **View canônica** `v_campanhas_canonicas`: `distinct on (store_id, campaign_id)` ordenando por `conversion_value desc nulls last, recipients desc nulls last`, só e-mail, `recipients > 200`. Com o parse do nome no padrão `[DD/MM] - [HH:MM] - [SEGMENTO] - [N - EVENTO] - [IDIOMA]` em colunas `dia`, `hora`, `segmento`, `evento`, `idioma`.
2. **Função** `indice_modelos(p_inicio date, p_fim date, p_min_lojas int)`: para cada loja com ≥ 10 campanhas e receita > 0 no período, média = soma(receita) / soma(envios). Índice da campanha = (receita/envios) / média da loja. Agrega por modelo (via `aliases_evento` e `alias_hora`) e por evento bruto, com mediana (`percentile_cont(0.5)`), lojas acima de 1, pedidos, spam por mil e descadastro. Esta é a mesma conta que gerou `dados/ranking_46_lojas_2026-09-21.csv`: use o CSV como teste de regressão (as medianas precisam bater com tolerância de 0,02 para a janela 15/06 a 20/09/2026).
3. **Materialized view** `mv_indice_modelos_90d` atualizada por cron diário (`/api/cron/indice-modelos`, com `cron_locks`).
4. **Backfill.** Crie um job que, para campanhas com `conversions` nulo e mais de 7 dias, busca as métricas na API da Omnisend da loja e grava uma linha nova. Reaproveite o client de Omnisend que já existe no projeto. Isso é pré-requisito para o índice de meses anteriores a junho.

A UI nunca mostra média entre lojas sem a mediana ao lado.

### 3.3 Planos e envios mestre

```
campanha_planos
  id, org_id, nome ("Outubro 2026", "Q4 2026 | BFCM"), tipo (mensal|temporada),
  inicio date, fim date,
  status (rascunho|aprovado|em_producao|encerrado),
  principio jsonb        -- {validado_min:80, inspiracao_max:10, complemento_max:10}
  composicao jsonb       -- calculada
  aprovado_por, aprovado_em, created_by, created_at, updated_at

campanha_plano_envios
  id, org_id, plano_id fk,
  data date, hora time, canal (email|sms|whatsapp|push),
  janela text            -- "10.10", "11.11", "bf", "cm", "dezembro", "outubro"
  modelo_key text fk logico para campanha_modelos.key (null para canais)
  estrutura text, objetivo text,
  assuntos jsonb         -- {pt, en, ...} (sobrescreve o do modelo)
  publico jsonb          -- {A:"E180", B:"E180", C:"E90"}; valores em regras.camadas
  lista_pequena boolean  -- entra no calendário de listas < 3 mil
  trilha text            -- todas | br | global | br_infantil | uk_eu | global_halloween | br_opcional ...
  teste_id text null     -- T1-madrugada etc.
  evidencia text check (validado|inspiracao|complemento) + evidencia_override_motivo text
  porque text, notas text,
  oferta_slot text       -- qual oferta da loja entra (ex. "oferta_1111")
  suggestion_id uuid null fk campaign_suggestions  -- preenchido na materialização
  ordem int, created_at, updated_at
```

Seed: `seed/plano_q4_2026.json` (68 envios de e-mail) e `seed/regras.json` (`canais_q4`: 21 mensagens de SMS, WhatsApp e push). O seed cria o plano "Q4 2026 | BFCM" com status `rascunho`.

### 3.4 Perfil da loja no plano

`client_stores` já tem `lista_total`, `lista_engajados_90`, `sms_consent_pct`, `timezone`, `language`, `country`, `countries`, `niche`, `frete_prazo`. Não duplique isso. Crie só o que é do plano:

```
campanha_plano_lojas
  id, org_id, plano_id, store_id,
  nivel text check (A|B|C)  + nivel_origem (auto|manual) + nivel_motivo text
  lista_pequena boolean     -- auto: lista_total < 3000
  remetente_pessoa text null  -- nome e cargo que assinam os textos
  canais jsonb              -- {sms:bool, whatsapp:bool, push:bool}
  ofertas jsonb             -- {oferta_1010:"...", oferta_1111:"...", oferta_bf:"...", ...}
  data_corte_natal date null
  trilhas text[]            -- ["br","br_infantil"] etc.
  incluida boolean default true
```

**Nível automático** (editável): A = primeira campanha da conta há mais de 12 meses e spam médio dos últimos 90 dias < 0,05%; B = 6 a 12 meses ou spam entre 0,05% e 0,1%; C = o resto, ou alerta ativo em `store_alerts`. Mostre o motivo.

### 3.5 Regras e segmentos

`seed/regras.json` vira a tabela `campanha_regras` (uma linha por org, jsonb versionado): camadas, níveis, freios, sequência de pico, meio de semana, regras de copy, padrão de nome, checklist, testes. Editável em `/admin/settings/campaign-central?tab=planejamento`.

### 3.6 Testes

```
campanha_testes
  id, org_id, plano_id, key ("T1-madrugada"), pergunta, desenho, metrica, decisao,
  prazo_leitura date, status (planejado|rodando|lido), resultado jsonb, lido_em
```

---

## 4. Materialização: do plano para as lojas

Ação "Distribuir para as lojas", por envio ou pelo plano inteiro, com prévia antes de gravar:

1. Para cada envio de e-mail, gera **uma** `campaign_suggestions` com `source = 'plano'` (acrescente o valor ao CHECK), `status = 'approved'`, `send_date`, título, `brief` (estrutura, tom e o que incluir, montados a partir do modelo e das regras de copy), `email_draft` inicial a partir do HTML do modelo e do assunto, e `targets` com as lojas elegíveis.
2. **Loja elegível:** incluída no plano, trilha compatível, e com `lista_pequena = false` ou envio marcado para lista pequena.
3. Em cada target, grave `publico_resolvido` (a camada do nível da loja) e `nome_campanha` no padrão `[DD/MM] - [HH:MM] - [CAMADA] - [N - EVENTO] - [IDIOMA]`. Acrescente coluna `send_time time` em `campaign_suggestions`, ou guarde em `targets[].send_time` se preferir não mexer na tabela. Justifique a escolha.
4. Grave `suggestion_id` no envio. Rodar de novo atualiza, não duplica.
5. Mudança posterior no envio mestre gera um diff e pergunta se propaga. Loja com ajuste manual fica marcada como "alterada na loja" e não é sobrescrita sem confirmação.
6. Daí para frente o fluxo é o que já existe: piloto, copy (n8n), design, cortes, `campaign_store_emails`, tarefas por papel.

---

## 5. Interface

Nova aba **Planejamento** em `/admin/campaigns/central`, antes de "Fluxo", ou rota própria `/admin/campaigns/planejamento`. Decida pelo que for mais simples de manter com o shell atual e justifique. Layout neutro, igual ao resto do admin.

### 5.1 Cabeçalho do plano

Seletor de plano, período, status, **barra de composição 80/10/10** com os três números, contagem de envios, lojas incluídas e botões: Aprovar (bloqueado abaixo de 80% validado), Distribuir para as lojas, Duplicar plano, Exportar para o Obsidian (seção 7).

### 5.2 Visão Calendário

Grade do mês com navegação entre os meses do plano. Cada dia mostra etiquetas: pico, meio de semana, teste, trilha local, canal de apoio. Filtros: mercado (BR, global, EUA, Reino Unido e Europa), nível (A, B, C, lista pequena), janela, papel, evidência, modelo. Hoje destacado. Clique no dia abre a linha do tempo.

### 5.3 Visão Dia (linha do tempo)

Eixo de 00h a 23h59 com três faixas: e-mail, SMS/WhatsApp, push. Cada envio é um bloco na hora certa com modelo, assunto e público. Mostra também D-6, D-3 e D+2 do pico quando o dia faz parte de uma sequência. Clique abre a ficha.

### 5.4 Ficha do envio (drawer)

Seções, nesta ordem:

1. **Resumo:** data, hora, canal, janela, objetivo, estrutura, evidência.
2. **Por que está aqui:** o texto de `porque`, mais o índice vivo do modelo (mediana e lojas acima de 1 nos últimos 90 dias) ao lado do snapshot do estudo. Se o índice vivo cair abaixo de 1, alerta "modelo perdeu força".
3. **Assuntos:** pt, en e demais idiomas, com três variações para reenvio.
4. **Público por nível:** tabela A, B, C e lista pequena, com a camada e o número estimado de contatos por loja (de `client_stores.lista_engajados_90` e afins).
5. **Referência:** imagem do e-mail validado, com zoom, e link do Figma.
6. **HTML proposto:** preview em iframe `srcdoc` e aba de código, com as variáveis preenchidas com uma loja de exemplo selecionável (logo, produtos de `store_top_products`, cupom e prazo fictícios marcados como exemplo).
7. **Como produzir:** copiar e melhorar, regras de copy e checklist.
8. **Produção:** status por loja (seção 5.5) em miniatura.
9. **Ações:** editar, pedir alteração à ConvertIA, distribuir, abrir no Fluxo.

### 5.5 Visão Produção

Matriz envio × loja. Célula = etapa atual (brief, copy, design, HTML, QA, agendado, enviado, resultado) lida das tabelas que já existem (`campaign_suggestions.copy_results`, `campaign_store_emails`, `campaign_generation_tasks`, `tasks`). Cor por atraso contra o prazo de produção da janela (`regras.prazos_producao`). Filtros por responsável e por etapa. Clique leva à tarefa.

### 5.6 Visão Biblioteca

Lista dos modelos com: nome, estrutura, status, mediana viva e do estudo, lojas acima de 1, pedidos, spam por mil, uso no plano atual. Detalhe com imagem, HTML e nota do vault. Ordenação padrão pela mediana viva. Botão "Promover" ou "Rebaixar" o status, com motivo, que registra histórico.

### 5.7 Visão Resultados e testes

Por envio já disparado: índice por loja e mediana, contra a expectativa do modelo. Por teste: grupos, métrica, leitura contra o critério de decisão, botão "Registrar leitura". Alerta quando um freio da seção de regras disparar (spam > 0,1%, descadastro > 0,5%, bounce > 2%) numa loja.

### 5.8 Checagem antes do envio

Para cada `campaign_store_emails` agendado, valide contra a Omnisend (quando houver credencial): endereço de resposta é da loja (nunca `bruno@convertfy.me`), remetente sem erro, idioma, horário igual ao nome da campanha e no fuso da loja, segmento compatível com o nível. Liste os problemas na ficha e na Produção.

---

## 6. Gerador do plano do mês

Botão "Gerar plano do mês" que monta um rascunho a partir de: datas duplas do mês (N.N), `commemorative_dates` por país das lojas, `regras.sequencia_de_pico` e `regras.meio_de_semana`.

1. Para cada data dupla e pico: aplica a sequência de pico (convite D-6, agenda D-3, SMS/push D-1, 00h se o T1 aprovou, 07h, 11h, 18h, 21h30, ressaca D+2).
2. Preenche os dias de meio de semana até o ritmo de 3 por semana para E90, escolhendo o modelo titular de maior mediana viva que não foi usado nos últimos 14 dias, respeitando as regras específicas (sexta premiada só às sextas, reabertura só depois de fechamento real).
3. Não põe dois eventos colados: nenhum pico a menos de 14 dias do anterior.
4. Marca a evidência e calcula a composição. Se ficar abaixo de 80% validado, troca os envios de inspiração ou complemento de menor prioridade por titulares até bater.
5. Escreve o `porque` de cada envio com o número usado ("Notificação do futuro: mediana 1,67 em 39 lojas, 24 acima da média").

O gerador é determinístico (sem LLM). A ConvertIA pode ser chamada depois para sugerir ajustes, sempre como proposta.

---

## 7. Vault do Obsidian

O vault `All-for-Eficiencia` já sincroniza com `ai_knowledge_notes` e `email_vault_docs`. O pacote traz `obsidian/Convertfy/calendario/` com 48 notas (mapa, princípio 80/10/10, ranking, sequência de pico, segmentação e freios, regras de copy, convenção de nome, 29 modelos, plano Q4 por janela, testes, lojas analisadas, fontes). Formato igual às notas de `Convertfy/estruturas`: frontmatter `tipo, autor, fonte, status, assunto`, wikilinks pelo nome do arquivo.

1. Confirme que o sync lê a pasta `Convertfy/calendario/**` e que as notas entram com `status: aprovado`.
2. Ligue `campanha_modelos.nota_vault` ao path da nota.
3. Botão "Exportar para o Obsidian" no plano: gera o markdown das janelas e do ranking com os números vivos e grava em `vault_propostas` (o humano leva para o vault, como já acontece hoje). Não escreva direto no repositório do vault.

---

## 8. ConvertIA

Crie o conector built-in `planejamento` em `src/lib/ai/connectors/planejamento.ts`, registrado em `registry.ts`, sempre disponível no workspace operacional. Tools:

| Tool | write | O que faz |
|---|---|---|
| `listar_planos` | não | Planos com período, status e composição |
| `ver_plano` | não | Envios de um plano, com filtros por data, janela e modelo |
| `ver_envio` | não | Ficha completa de um envio, com o índice vivo |
| `ranking_modelos` | não | Índice dos modelos num período, com mediana e lojas acima de 1 |
| `status_producao` | não | Matriz de produção filtrada por loja, envio ou etapa |
| `resultado_teste` | não | Leitura de um teste |
| `propor_alteracao_envio` | sim | Cria uma proposta com diff (campo antigo e novo, motivo, efeito na composição 80/10/10). Não grava sem o "Confirmar" da UI |
| `aplicar_alteracao` | sim | Aplica uma proposta confirmada e oferece propagar para as lojas |
| `gerar_plano_mes` | sim | Roda o gerador da seção 6 em rascunho |

No system prompt da ConvertIA, quando o conector estiver ativo, acrescente: "Toda proposta de calendário respeita 80% validado, até 10% inspiração e o restante complemento. Cite o número do modelo que justifica cada envio. Nunca proponha esquenta de vários e-mails, véspera por e-mail ou extensão para a lista toda sem dado novo."

---

## 9. Fases e critérios de aceite

**Fase 1: dados e leitura**
- Migration com as tabelas da seção 3, RLS e seeds (modelos, plano Q4 2026, regras, testes, canais).
- `v_campanhas_canonicas`, `indice_modelos()`, `mv_indice_modelos_90d` e o teste de regressão contra o CSV de 46 lojas.
- Visões Calendário, Dia, Ficha e Biblioteca, só leitura.
- Aceite: o plano Q4 aparece com 68 envios de e-mail e 21 de canais; a composição mostra 93% validado e 7% complemento; a ficha de 11/11 às 18h mostra a imagem de referência, o HTML renderizado com uma loja real e o índice vivo do modelo.

**Fase 2: lojas e produção**
- `campanha_plano_lojas` com nível automático e motivo, edição manual, ofertas por janela.
- Distribuir para as lojas (seção 4) com prévia, idempotência e diff de propagação.
- Visão Produção e checagem antes do envio.
- Aceite: distribuir a janela 10.10 gera 9 `campaign_suggestions` com `source='plano'` (convite, agenda, os 5 disparos do dia 10, a ressaca e o Dia das Crianças das lojas BR infantis), `targets` corretos por nível e trilha, e rodar de novo não duplica.

**Fase 3: resultados, testes e ConvertIA**
- Visão Resultados e testes, cron do índice, backfill da Omnisend.
- Conector `planejamento` com as tools da seção 8 e o gate de confirmação.
- Aceite: pedir à ConvertIA "troca o e-mail de 14/10 por um modelo melhor" gera proposta com diff, número do modelo e composição recalculada, e só grava depois do Confirmar.

**Fase 4: mensal**
- Gerador do plano do mês, duplicar plano, exportar para o Obsidian.
- Aceite: gerar "Janeiro 2027" produz um rascunho com a sequência de pico no 1.1 (se aplicável pelas regras), meio de semana com titulares e composição ≥ 80% validado.

---

## 10. Arquivos do pacote

| Caminho | O que é |
|---|---|
| `seed/modelos.json` | 30 modelos com as duas amostras, assuntos, aliases, referência, copiar e melhorar |
| `seed/plano_q4_2026.json` | 68 envios de e-mail de 01/10 a 31/12/2026 |
| `seed/regras.json` | Princípio 80/10/10, camadas, níveis, freios, sequência de pico, meio de semana, copy, nome, checklist, testes, prazos e canais do Q4 |
| `html/*.html` | 15 modelos em layout neutro (fundo branco, texto preto), variáveis entre chaves duplas, e `index.html` com a galeria |
| `img/*.jpg` | Peças validadas da Blue Wolf (jul, ago, set), nomeadas por mês e dia |
| `dados/ranking_46_lojas_2026-09-21.csv` | Resultado da conta do índice em 46 lojas, para o teste de regressão |
| `dados/base_campanhas_convertfy.*` | Base de 525 campanhas de 9 lojas do estudo |
| `obsidian/Convertfy/calendario/` | 48 notas para o vault |
| `docs/` | Calendário Q4, Estudo Base e Playbook exportados em markdown |

Links dos documentos originais: Estudo Base https://claude.ai/code/artifact/e3da050a-9dbb-42dc-9b30-987f7cf02ad7 · Playbook https://claude.ai/code/artifact/7f25e035-cf35-4336-858b-a2cd0fdadc91 · Calendário Q4 https://claude.ai/code/artifact/d2398783-1e9c-4de4-b580-b98d5826f0d2

Comece pela leitura da seção 0, item 1, e me devolva o plano de implementação da Fase 1 com a lista de arquivos que vai criar e alterar antes de escrever código.
