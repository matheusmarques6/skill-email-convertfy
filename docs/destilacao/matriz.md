# Matriz de destilação dos repos de e-mail

Rascunho do subagente C. Decide, arquivo por arquivo, o que sai de cada repo
de `vendor/` e entra nos rascunhos de skill.

**Nada é copiado.** "Aproveitar" nesta matriz significa *a ideia entra,
reescrita com nossas palavras e nossas regras*. Todo aproveitamento efetivo
está listado no fim, para virar crédito em `NOTICE.md`.

Precedência aplicada em cada linha:
**brief da loja > vault > CLAUDE.md > skill > vendor.**
Quando o vendor bate de frente com o CLAUDE.md, o vendor perde, sempre.

## Alerta de licença

`vendor/Ground-Retention-Skills` (Join-Ground-AI) **não declara licença**.
Sem licença não há permissão de uso ou derivação. Foi lido apenas para
entender o problema. **Nenhuma estrutura, lista ou fluxo dele entra nos
rascunhos.** Todas as linhas dele estão marcadas `descartar (sem licença
declarada)`.

Os demais repos desta matriz são MIT. MIT permite derivação com atribuição,
e mesmo assim a regra da casa vale: reescrito, nunca copiado.

## Legenda das decisões

| Decisão | Significa |
|---|---|
| `aproveitar` | A ideia entra quase como está, traduzida e adaptada |
| `reescrever` | O problema é real, a solução do vendor não serve: refazemos |
| `descartar` | Não entra, por licença, por conflito de regra ou por falta de evidência |

---

## 1. `vendor/email-marketing-bible` (CosmoBlk, MIT)

Arquivo único de 300 linhas. Linha por seção.

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| `SKILL.md` §0 Agent operating rules | reescrever | A ideia de portão humano antes de enviar é boa, a formulação é genérica | Nenhum | Alinha com P06 (revisor separado) |
| `SKILL.md` §1 Task router | descartar | Roteador de tarefas do próprio repo, sem uso aqui | Nenhum | Nenhum |
| `SKILL.md` §2 e §2b AI email automation / field notes | descartar | Notas de campo de outra operação, não verificáveis | Nenhum | Nenhum |
| `SKILL.md` §3 Pre-send checklist | aproveitar | Melhor checklist pré-envio dos 9 repos: autenticação, supressão, one-click, kill switch | Corrigir "subject ≤45 chars" para o nosso C40, que é alvo ≤40 e ideal ≤25, e declarar que o número vem de teste | Evidência REFINADA: assunto curto sim, limite exato por teste |
| `SKILL.md` §4 Anti-slop copy protocol | reescrever | A lista de vícios entra, a justificativa não | Nenhum na lista; a frase de abertura viola a honestidade epistêmica | **Conflito grave.** "Google filtra high-AI-similarity text harder" é **especulação sem evidência** segundo `evidencias-publicadas.md`. Ver bloco abaixo |
| `SKILL.md` §4 blacklist de palavras | aproveitar | Sobrepõe C20/C21; a nossa lista é pt-BR e mora em `shared/lexico/` | Nenhum | C21 CONFIRMADA (excesso de vocabulário quantificado) |
| `SKILL.md` §4 syntax fingerprints | aproveitar | "não é X, é Y", tríade, evasão do verbo ser, travessão: é C10, C11, C24, C01 | Nenhum | C10/C11 CONFIRMADAS, C01 REFINADA |
| `SKILL.md` §5 AI email design protocol, parte "dois leitores" | aproveitar | Resumidor do Gmail e do Apple lê texto vivo: sustenta D17 e C42 | Nenhum | CONFIRMADA (oferta em texto vivo + alt) |
| `SKILL.md` §5 "own one colour (30-60% of the surface)" | **descartar** | Manda a peça se apropriar de uma cor autoral em metade da superfície | **Viola CLAUDE.md layout.** Fundo branco, texto preto, sem paleta autoral; cor da marca só em acento, nunca como fundo de seção | Nenhum na pesquisa, o conflito é de regra da casa |
| `SKILL.md` §5 ban do gradiente roxo-azul e do banho bege | aproveitar | É exatamente D01 e D03 | Nenhum | D01/D03 confirmados por F8 |
| `SKILL.md` §5 dark mode ~#121212, nunca #000 nem logo #fff | aproveitar | É D19 | Nenhum | D19 |
| `SKILL.md` §5 seed strings, 12-20 direções, briefs ambiciosos, "reference: Graza, Aesop" | **descartar** | É um motor de autoria visual: produz peça impressionante, não peça indistinguível de produção | **Viola CLAUDE.md:** "o agente não escolhe paleta"; e o propósito do repo (escolher indistinguível sobre impressionante) | Nenhum na pesquisa; conflito de propósito |
| `SKILL.md` §5 critic loop (modelo separado, contexto limpo, nota /10, máx. 4 rodadas) | aproveitar | Vira P06 na prática | Nenhum | P06, evidência moderada |
| `SKILL.md` §6 tabela de métricas | aproveitar como **direcional** | Serve de calibração da auditoria | Nenhum | Rotular sempre "mercado americano, direcional, nunca promessa" |
| `SKILL.md` §7 core flow recipes | reescrever | A ordem de construção é útil; os nomes e gatilhos são de Klaviyo | Nenhum | Nenhum |
| `SKILL.md` §8 "buttons beat text links (+27%)", "one CTA beats several (+42%)", "under ~25 chars opens highest" | aproveitar só o **sentido**, descartar os números | Números agregados sem fonte primária no arquivo | Nenhum | "1 CTA principal" CONFIRMADA; os percentuais exatos são **folclore de mercado**: usar só como direção, nunca citar o número |
| `SKILL.md` §11 Deliverability triage (SPF, DKIM, DMARC, limiares de reclamação) | aproveitar | Base da skill de auditoria | Nenhum | Requisitos de remetente em massa: evidência **FORTE** |
| `SKILL.md` §11 "Raw un-personalised AI text is filtered harder" | **descartar** | Repetição da mesma especulação do §4 | Nenhum | **Sem evidência.** Ver bloco abaixo |
| `SKILL.md` §13 Compliance gates + tabela de regulação | aproveitar | CAN-SPAM, GDPR, CASL, Spam Act; falta o CDC art. 37 brasileiro | Nenhum | CONFIRMADA (estatutária) |
| `SKILL.md` §14 Cold email | descartar | Fora de escopo: e-commerce com lista opt-in | Nenhum | Nenhum |
| `SKILL.md` §15 Platform selection | descartar | Comparativo de ESP com divulgação de conflito de interesse do autor; nosso ESP já está decidido | Nenhum | Nenhum |
| `SKILL.md` §16 Email design decision table (arquétipos) | **descartar** | Manda "escolher um arquétipo e se comprometer" (punk, minimal-lux, lookbook) | **Viola CLAUDE.md layout.** Arquétipo é escolha autoral de estética; a peça neutra não escolhe | Nenhum |
| `SKILL.md` §17 Industry playbooks | descartar | Genérico demais para virar regra | Nenhum | Nenhum |
| `SKILL.md` Apêndice de benchmarks | aproveitar como **direcional** | Calibra o "está ruim?" da auditoria | Nenhum | Rotular: mercado americano, meados de 2026, direcional. Nunca promessa ao cliente |

### O conflito mais grave deste repo

O §4 abre com: *copy crua de LLM é um passivo de entregabilidade porque o
Google filtra texto de alta similaridade com IA com mais força.*

`docs/pesquisa/evidencias-publicadas.md` classifica isso como
**especulação, sem evidência primária**, e é explícito: filtros agem sobre
reputação de IP e domínio, autenticação, engajamento e sinais spammy
clássicos, não sobre um detector de IA.

**Reposição correta, que deve entrar nos rascunhos no lugar dessa frase:**
o risco da copy homogênea é (a) engajamento baixo, (b) reclamação de spam,
que é o que de fato move o filtro, e (c) homogeneização entre lojas. O (c)
está **observado ao vivo**: 20 de 20 lojas Shopify não relacionadas na base
Trendtrack mandando o mesmo texto de boas-vindas quase idêntico. A regra
sobrevive inteira; só a justificativa muda, e passa a ser verdadeira.

---

## 2. `vendor/email-campaign-skill` (davidharttx, MIT)

Base da `skills/email-flows/`.

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| `docs/flows/FLOW-ARCHITECTURE.md` modelo de duas camadas (entrada por lista, ciclo de vida universal) | aproveitar | Melhor peça conceitual dos 9 repos: explica por que welcome é por fonte e carrinho é universal | Nenhum | Nenhum |
| `docs/flows/FLOW-ARCHITECTURE.md` ordem de prioridade de receita (10 flows) | aproveitar | Ordem de construção defensável | Nenhum | Nenhum |
| `docs/flows/FLOW-ARCHITECTURE.md` regras de interação, filtros de flow, saída por compra | aproveitar | Vira `exitConditions` e `audienceFilterGroup` no Omnisend | Nenhum | Nenhum |
| `docs/flows/FLOW-ARCHITECTURE.md` Smart Sending 16h | reescrever | Smart Sending é recurso nomeado do Klaviyo. No Omnisend o equivalente funcional é o **limitador de sobreposição** (`overlapLimiter`, modos `currentlyIn` e `recentlyIn`) e o **limitador de frequência** (`frequencyLimiter`) | Nenhum | Nenhum |
| `docs/flows/FLOW-ARCHITECTURE.md` "~70% dos carrinhos são abandonados", "recuperação de 5-15%" | aproveitar como direcional | Números de mercado sem fonte primária no arquivo | Nenhum | Marcar direcional; nunca prometer ao cliente |
| `docs/flows/KLAVIYO-DYNAMIC-VARIABLES.md` tabelas de variáveis | **reescrever inteiro** | Sintaxe Django do Klaviyo (`{{ event.ProductName }}`) não existe no Omnisend | **Conflito de ESP.** Nosso principal é Omnisend | Nenhum |
| `docs/flows/KLAVIYO-DYNAMIC-VARIABLES.md` disciplina de `default:` em toda merge tag | aproveitar | É C47 (personalização sem fallback) | Nenhum | C47 |
| `docs/flows/KLAVIYO-DYNAMIC-VARIABLES.md` exemplos de HTML | descartar | Botão com `border-radius` e cor autoral `#2d6a4f`; imagem de produto com `border-radius` | **Viola CLAUDE.md:** cor autoral sem brief. E `border-radius` em `<img>` é D18 (recurso que quebra) | D18 |
| `skill/flows/FLOW-SKILL.md` as 10 especificações de flow (gatilho, escopo, número de e-mails, timing) | aproveitar | É o esqueleto dos nossos 10 flows | Nenhum | Nenhum |
| `skill/flows/FLOW-SKILL.md` template HTML de referência | **descartar** | `background-color:#FAF7F2` (banho bege) no body, `border-radius:12px` no container, verde `#1A3D28` como cor de marca inventada, botão sem VML | **Viola CLAUDE.md** em três pontos: paleta autoral, fundo não branco, botão não bulletproof | **D03** (fundo creme/bege por padrão, peso 7 no slop-detect) |
| `skill/flows/FLOW-SKILL.md` "Trust bar com 3 sinais em todo e-mail" | reescrever | Faixa de 3 diferenciais é permitida, não obrigatória | Nenhum | **D08:** grade de cards idênticos é "revisar". Permitida como faixa curta, proibida como estrutura principal. Obrigatória em todo e-mail vira exatamente o vício |
| `skill/flows/FLOW-SKILL.md` "5 content pillars, todo flow toca ao menos 3" | reescrever | A ideia de não fazer só Produto+Venda é boa; a cota fixa de pilares produz e-mail de enchimento | Choca com o orçamento de palavras (C45) | C45 |
| `skill/flows/FLOW-SKILL.md` "ao menos 1 e-mail text-based por flow, com P.S. obrigatório e carta do fundador" | **descartar a obrigatoriedade** | Carta de fundador em todo flow é storytelling elaborado por decreto | **Viola CLAUDE.md copy:** proibido storytelling elaborado | **C05** (cena ou storytelling fabricado) e **C16** (abertura genérica). O e-mail de texto puro continua permitido quando o brief pedir |
| `skill/flows/FLOW-SKILL.md` naming convention `[PREFIX] \| Flow N -- Email` | aproveitar | Convenção de nome é útil em agência com 250+ lojas | Nenhum | Nenhum |
| `skill/flows/FLOW-SKILL.md` "Never use placeholder or fake image URLs" | aproveitar | É P02 (preencher lacuna com invenção) | Nenhum | P02 |
| `skill/flows/FLOW-SKILL.md` limitações da API do Klaviyo | descartar | Substituído pelas limitações reais do Omnisend, que são outras (o Omnisend **cria** automação pela API) | Nenhum | Nenhum |
| `docs/PILLARS.md`, `docs/SEGMENTATION.md`, `docs/TEXT-BASED-EMAILS.md`, `docs/FIGMA-MODULES.md` | descartar | Pilares e segmentação são de outro escopo; Figma modules é do design system deles | Nenhum | Nenhum |
| `examples/flows/*.md` | descartar como fonte de copy | Copy de exemplo em inglês com travessão e tríade | **C01** e **C11** | §2.3: exemplo contaminado ensina o vício. Não vira referência |
| `scripts/campaign_ideator.jsx` | descartar | Script de UI, sem uso | Nenhum | Nenhum |

---

## 3. `vendor/skill-email-html-mjml` (framix-team, MIT)

Base técnica da `skills/email-design/`.

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| `SKILL.md` regra 2, largura 600px assumida | aproveitar | Bate com CLAUDE.md | Nenhum | Nenhum |
| `SKILL.md` regra 3, Outlook: `mj-font` com pilha de fallback, VML só em `mj-section` e `mj-hero` | aproveitar | Fato técnico verificável e caro de redescobrir | Nenhum | Nenhum |
| `SKILL.md` regra 4, Gmail: usar atributo de componente em vez de classe CSS | aproveitar | Reforça a regra de estilo inline do CLAUDE.md | Nenhum | Nenhum |
| `SKILL.md` regra 6, acessibilidade: `alt` obrigatório, contraste 4,5:1, sem texto assado em imagem | aproveitar | É D04, D17 e C42 | Nenhum | D04, D17 |
| `SKILL.md` regra 8, evitar `mj-accordion` e `mj-carousel` | aproveitar | Suporte ruim de cliente; é D18 | Nenhum | D18 |
| `SKILL.md` padrão de dark mode: `#121212` e não `#000000`, `#F1F1F1` e não `#FFFFFF` | aproveitar o `#121212`, **revisar** o `#F1F1F1` | `#121212` é D19 literal. O `#F1F1F1` no lugar de branco puro contraria o fundo branco da casa | **Atenção:** CLAUDE.md manda fundo branco. `#F1F1F1` entra, se entrar, só como decisão do vault, não da skill | D19 |
| `SKILL.md` dark mode por troca de logo (`.light-logo` / `.dark-logo` com media query) | reescrever | A técnica é válida mas depende de media query que vários clientes removem. Tratar como reforço, nunca como única defesa | Nenhum | D19 e §12 do QA skill |
| `SKILL.md` "102KB clip: sempre compilar com minify" | aproveitar, com o limite **a verificar** | O limite de clipping é citado em todo lugar e reconfirmado em lugar nenhum | Nenhum | `evidencias-publicadas.md` lista "limite exato de 102 KB" como item **a reconfirmar**. Escrever "~102 KB (a verificar)" |
| `SKILL.md` gotcha do `mj-include` desabilitado por padrão no MJML 5 | descartar | Só importa para quem compila MJML | Nenhum | Nenhum |
| `SKILL.md` gotcha do espaço em branco entre tags causar empilhamento | aproveitar | Armadilha real de renderização | Nenhum | Nenhum |
| `SKILL.md` bug do `vertical-align` (se uma coluna define, todas definem) | aproveitar | Armadilha real | Nenhum | Nenhum |
| `SKILL.md` "JS é bloqueado em todo cliente" | aproveitar | Fecha a porta para interatividade falsa | Nenhum | D18 |
| `SKILL.md` fluxo "entregar sempre `.mjml` + `.html`" | **descartar** | Adotar MJML seria adotar uma toolchain nova e um passo de compilação | Choca com o arsenal, que é HTML validado em `assets/arsenal/` | Nenhum. **Decisão para o dono do repo**, ver perguntas no relatório |
| `components/*.md`, `mjml-reference.md`, `compilation.md` | descartar | Referência de API do MJML; só serve se adotarmos MJML | Nenhum | Nenhum |
| `assets/examples/*.mjml` | descartar | "All copy, image URLs, and brands in these files are placeholders", e copy de placeholder é P04 | Nenhum | P04 |

---

## 4. `vendor/email-html-qa-skill` (EmailBoutique, MIT)

Melhor repo da lista para o passo de QA. Entra quase inteiro, reescrito.

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| `SKILL.md` princípio "verificar mecânica, não suficiência" | aproveitar | Separa o que a skill pode afirmar do que é decisão jurídica do cliente | Nenhum | Nenhum |
| `SKILL.md` escala de severidade (Critical / High / Medium / Low) | aproveitar | Mapeia direto no nosso B / A / M | Nenhum | §5 da pesquisa |
| `SKILL.md` §1 dark mode: checar as duas metas de opt-in antes de qualquer coisa | aproveitar | Passo que nenhum outro repo tem: saber **se** dark mode está sendo mirado | Nenhum | D19 |
| `SKILL.md` §1 logo transparente que some em fundo escuro | aproveitar | Caso concreto de D19 que a pesquisa só menciona de passagem | Nenhum | D19 |
| `SKILL.md` §1 distinguir elemento fixo-escuro de elemento adaptativo, nunca misturar as técnicas | aproveitar | Precisão técnica rara | Nenhum | D19 |
| `SKILL.md` §5 alt intencional: descritivo quando carrega sentido, `alt=""` quando é decorativo, **nunca ausente** | aproveitar | Refina D17: o nosso D17 só fala de alt presente, e alt decorativo presente e descritivo é ruído em leitor de tela | Nenhum | **Refina D17** |
| `SKILL.md` §7 imagem grande não linkada vira lightbox do Gmail e rouba o clique | aproveitar | Armadilha real, não está em nenhuma pesquisa nossa | Nenhum | Item novo, candidato a D21 |
| `SKILL.md` §12 supressão de auto-link (telefone, data, endereço) com os três overrides separados | aproveitar | Caso clássico de rodapé quebrado; Gmail remove seletor de atributo encadeado | Nenhum | Item novo, candidato a D22 |
| `SKILL.md` §13 leitura de `Authentication-Results` e `List-Unsubscribe-Post` a partir de `.eml` recebido | aproveitar | É o único caminho concreto para checar SPF/DKIM/DMARC e RFC 8058 na prática | Nenhum | Evidência **FORTE** (requisitos de remetente em massa) |
| `SKILL.md` "diagnosticar primeiro, não alterar o código sem pedido" | aproveitar | Postura correta para revisão | Nenhum | P06 |
| `references/dark-mode-qa-matrix.md` grade superfície × cliente | aproveitar | Vira a nossa matriz de QA de dark mode | Nenhum | D19 |
| `scripts/lint_email_html.py` conjunto de checagens | aproveitar as **checagens**, não o código | O linter é de outro subagente (`scripts/lint_email.py`). A lista de checagens dele cobre tamanho, alt, `role=presentation`, link vazio, imagem não linkada, preheader ausente, logo transparente | Nenhum | §9.2 da pesquisa já prevê quase todas |
| `scripts/lint_email_headers.py` | aproveitar a ideia | Checagem de cabeçalho a partir do `.eml`: SPF, DKIM, DMARC, RFC 8058 | Nenhum | Conformidade, evidência forte |
| `SKILL.md` "out of scope: deliverability advice" | **divergir** | Eles se recusam a diagnosticar entregabilidade. A nossa `auditoria-omnisend` **precisa** diagnosticar | Nenhum | Divergência declarada, não conflito |

---

## 5. `vendor/claude-marketing` (thatrebeccarae, MIT), skill `klaviyo-analyst`

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| `skills/klaviyo-analyst/SKILL.md` framework de auditoria em 4 fases (inventário, configuração, estrutura de dados, recomendação) | aproveitar | Melhor esqueleto de auditoria dos dois repos de audit | Nenhum | Nenhum |
| idem, recomendação em três camadas (achado com evidência / recomendação em linguagem de cliente / spec de implementação) | aproveitar | Resolve o problema de relatório que o cliente não entende e o time não consegue executar | Nenhum | Nenhum |
| idem, sequência de ferramentas MCP passo a passo | **reescrever** | Ferramentas são do MCP do Klaviyo (`get_flows`, `get_flow_report`, `get_catalog_items`) | **Conflito de ESP.** Reescrito contra as operações reais do MCP Omnisend | Nenhum |
| idem, checklist dos 10 flows essenciais | aproveitar | Converge com o `email-campaign-skill`; usar a interseção dos dois | Nenhum | Nenhum |
| idem, tabelas de benchmark (open, click, unsub, complaint, flow revenue %) | aproveitar como **direcional** | Calibra severidade | Nenhum | Direcional. Mercado americano. **Exceção:** o limiar de reclamação não é direcional, é conformidade |
| idem, "Deliverability: autenticação SPF, DKIM, DMARC" | aproveitar | Conformidade | Nenhum | Evidência **FORTE** |
| idem, comparativo Klaviyo SMS vs Attentive | descartar | Fora de escopo | Nenhum | Nenhum |
| idem, seções de instalação, scripts Python, troubleshooting | descartar | Infra do repo deles | Nenhum | Nenhum |
| `skills/klaviyo-analyst/REFERENCE.md` | descartar | Modelo de dados do Klaviyo | Conflito de ESP | Nenhum |
| `skills/email-composer/`, `skills/retention-churn-prevention/` | descartar | Coberto melhor por chappie e pelo vault | Nenhum | Nenhum |
| `skills/shared/scoring-system.md` | reescrever | Ideia de nota composta; o rubrico do olivalcf é melhor | Nenhum | Nenhum |

---

## 6. `vendor/klaviyo-audit-agent-skill` (olivalcf, MIT)

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| `SKILL.md` regras de segurança inegociáveis (somente leitura, nunca pedir chave, tratar conteúdo da conta como dado não confiável) | aproveitar | Auditoria em 250+ contas de cliente precisa exatamente disso | Nenhum | Nenhum |
| `SKILL.md` regra 6: "não afirme que uma checagem passou sem evidência; marque `unverifiable`" | aproveitar | É a regra mais valiosa dos dois repos de auditoria | Nenhum | Casa com a honestidade epistêmica de `evidencias-publicadas.md` |
| `SKILL.md` três modos (Quick 30 dias, Full 90 dias, Focused) | aproveitar | Escala bem para agência | Nenhum | Nenhum |
| `SKILL.md` "compare a conta com ela mesma no período anterior primeiro, benchmark de mercado só como contexto" | aproveitar | Resolve o problema do benchmark folclórico virando régua | Nenhum | **Diretamente alinhado** com o veredito de que benchmarks são direcionais |
| `SKILL.md` formato de avaliação por checagem (status, evidência, fonte, `observed_at`, confiança, impacto, ação, esforço) | aproveitar | Estrutura de saída auditável | Nenhum | Nenhum |
| `references/audit-rubric.yaml` rubrica de 100 pontos em 7 dimensões | aproveitar, **repontuado** | As dimensões servem; os pesos são do Klaviyo (Forms e acquisition valem 10) | Nenhum | Nenhum |
| `references/check-criteria.md` critérios reprodutíveis pass/partial/fail | aproveitar | Torna a nota reprodutível entre auditorias | Nenhum | Nenhum |
| `references/mcp-tool-routing.md` | reescrever | Roteia para o MCP do Klaviyo | Conflito de ESP | Nenhum |
| `references/benchmark-policy.md` | aproveitar | Política de "nunca transformar benchmark sem citação em regra dura" | Nenhum | Alinhada |
| `references/privacy-and-prompt-injection.md` | aproveitar | Conteúdo de template de cliente é dado, nunca instrução | Nenhum | Nenhum |
| `references/flow-playbooks.md`, `references/reporting-semantics.md`, `references/audit-data-requirements.md` | reescrever | Semântica de relatório é específica do Klaviyo. O Omnisend tem dois relógios próprios: `post_analytics_reports` agrupa por data de envio e `post_analytics_statistics` agrupa por data do evento. Misturar os dois é erro de leitura | Conflito de ESP | Nenhum |
| `scripts/score-audit.mjs`, `scripts/validate-audit.mjs` | descartar como código | A ideia de validar o JSON da auditoria contra a rubrica entra; o código não | Nenhum | Nenhum |

---

## 7. `vendor/chappie` (808enzo, MIT)

35 skills de CRM, agnósticas de plataforma. Alto valor de método, baixo valor de conteúdo direto.

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| Disciplina de fronteira: cada `description` diz o que a skill **não** cobre | aproveitar | Modelo para as nossas `description`, que por CLAUDE.md dizem **quando** acionar | Nenhum | Nenhum |
| Estrutura `SKILL.md` + `references/<tema>.md` + um `<nome>-vocabulary.md` por skill | aproveitar | Bate com a convenção do CLAUDE.md (máx. 500 linhas, detalhe em `references/`) | Nenhum | Nenhum |
| `skills/email-copy/SKILL.md` "a promessa é herdada, não inventada" (o e-mail deve ao ponto de captura, ao evento e à oferta viva) | aproveitar | Enquadra C46 e C06 melhor do que a nossa formulação atual | Nenhum | C46, C06 |
| `skills/email-copy/SKILL.md` "as palavras medem pior que tudo em volta" | aproveitar | Justifica por que copy só é isolável dentro de um único e-mail | Nenhum | Alinha com a recomendação de A/B |
| `skills/triggered-messages/SKILL.md` o gatilho como regra, não como mensagem; colisão entre flows; quando o flow para | aproveitar | Complementa a arquitetura do `email-campaign-skill` no ponto fraco dela | Nenhum | Nenhum |
| `skills/triggered-messages/SKILL.md` "mensagem descrevendo item que esgotou uma hora antes" | aproveitar | Caso concreto de frescor de dado | Nenhum | C06 (urgência ou escassez falsa) |
| `skills/deliverability/SKILL.md` identidades de envio, alinhamento de DMARC, one-click, escada de aquecimento, quatro classes de endereço inalcançável | aproveitar | Cobre a auditoria melhor que os dois repos de audit juntos | Nenhum | Conformidade, evidência forte |
| `skills/email-design/SKILL.md` "o remetente olha a mensagem em lugar diferente de onde ela é lida" | aproveitar | Melhor formulação do problema de dark mode e de cliente de e-mail | Nenhum | D18, D19 |
| `skills/email-design/SKILL.md` estados de bloco na montagem (bloco de produto que pode sair curto ou vazio) | aproveitar | Nenhuma pesquisa nossa cobre isso; é P04 na prática | Nenhum | **Item novo**, liga em P04 |
| Demais 28 skills (RFM, loyalty, B2B, push, calendário promocional, etc.) | descartar por ora | Fora do escopo dos quatro rascunhos | Nenhum | Nenhum |

---

## 8. `vendor/prescott-amelia-agents` (jayreis, MIT)

| Arquivo de origem | Decisão | Motivo | Conflito com regra da Convertfy | Conflito com as pesquisas |
|---|---|---|---|---|
| `amelia/references/anti_patterns.md` "nunca inventar preço, alegação, ingrediente ou nome de produto; use `[PRICE TBC]`" | aproveitar | É C02 e P02, com a solução prática do placeholder marcado | Nenhum | C02 (evidência **FORTE**: risco legal), P02 |
| idem, "prova social de enchimento sem citação e atribuição reais" | aproveitar | Fecha a lacuna do nosso `reviews` | Nenhum | C02, D09 |
| idem, "sem painel de fundo em gradiente atrás de texto" | aproveitar | D01, D02 | Nenhum | D01, D02 |
| idem, "caixa dentro de caixa dentro de caixa: um nível de card, no máximo" | aproveitar | É D11 literal | Nenhum | D11 |
| idem, "sem foto de banco de imagem de pessoa feliz segurando celular" | aproveitar | É D15 | Nenhum | D15 |
| idem, "no máximo dois tipos de letra" | aproveitar | Casa com a nomenclatura obrigatória: tipografia principal e fonte secundária | Nenhum | Nenhum |
| idem, "texto de corpo abaixo de 14px, rodapé abaixo de 11px: a seção está cheia demais, corte a copy em vez de encolher" | aproveitar | Ótima formulação: trata sintoma de layout como problema de copy | Nenhum | Nenhum |
| idem, "sem lorem ipsum, sem seção em branco" | aproveitar | P04 | Nenhum | P04 |
| `amelia/references/copy_voice_standards.md` "números e específicos batem adjetivos" | aproveitar | §4.3: especificidade é o humanizador mais barato | Nenhum | CONFIRMADA |
| idem, CTA com verbo, 2 a 4 palavras | aproveitar | C43, e bate com o corpus (shop, claim, explore dominam) | Nenhum | C43 |
| idem, **"Headlines: Title Case por padrão"** | **descartar em pt-BR** | Title Case em português é vício de tradução | **C34:** Title Case em pt-BR é proibido; usar caixa de frase ou caixa alta total | **C34** |
| idem, "CTAs: ALL CAPS por padrão" | aproveitar | Caixa alta em botão é convenção legítima de e-mail | Nenhum | **§8 da pesquisa:** caixa alta em rótulo e botão **não é vício** |
| idem, parágrafo de introdução com no máximo 2 frases | aproveitar | Converge com C45 | Nenhum | C45 |
| `amelia/references/email_html_rules.md` **"nenhuma tag `<!DOCTYPE>`, `<html>`, `<head>`, `<meta>`"** | **descartar** | Sem `<head>` não há `<meta name="color-scheme">`, não há `charset`, não há `lang` | **Viola CLAUDE.md:** "seguro para dark mode" fica impossível de declarar | **D19** e §1 do QA skill (as duas metas de opt-in) |
| idem, largura 600px, coluna única, exceção só para grade 2×2 e comparativo de 2 colunas | aproveitar | Bate com CLAUDE.md | Nenhum | §8 (coluna única é convenção, não vício) |
| idem, botão bulletproof com VML e altura mínima de toque de 44px | aproveitar | É exigência do CLAUDE.md, com o número de toque que faltava | Nenhum | Nenhum |
| idem, "trate o bloco `<style>` como melhor esforço: a peça tem que funcionar se ele for removido inteiro" | aproveitar | Formulação mais forte da regra de estilo inline do CLAUDE.md | Nenhum | Nenhum |
| idem, regra de cards de mesma altura (cor de fundo no `<td>` externo, altura fixa nas imagens da mesma linha) | aproveitar | Armadilha concreta de e-mail, não está em nenhuma pesquisa nossa | Nenhum | Item novo |
| idem, "uma mensagem, uma ação; repetir o botão 2 a 3 vezes com o mesmo destino" | aproveitar | É C44 com a permissão explícita de repetir | Nenhum | C44 e §8 |
| `prescott/tools/omnisend_client.py` | descartar como código, **aproveitar o sinal** | Confirma que outra agência opera Omnisend por API. Usa v3 e v5 direto; o nosso caminho é o MCP | Nenhum | Nenhum |
| `prescott/tools/klaviyo_client.py`, `flow_health_check.py` | descartar | Conflito de ESP e código | Nenhum | Nenhum |
| `prescott/sops/`, `prescott/pitch-decks/`, `prescott/playbooks/` | descartar | Operação comercial da agência deles | Nenhum | Nenhum |
| `examples/finished-email/rendered_email.html` | descartar como fonte | Peça pronta de outra marca; copiar seria copiar do vendor | Regra 2 do CLAUDE.md | Nenhum |

---

## 9. `vendor/Ground-Retention-Skills` (Join-Ground-AI, SEM LICENÇA)

**Tudo descartado.** Sem licença não há permissão. Lido somente para
entender o problema; nada dele entra em rascunho, nem estrutura, nem lista,
nem fluxo, nem ordem de perguntas.

| Arquivo de origem | Decisão | Motivo |
|---|---|---|
| `skills/welcome-series-optimizer/SKILL.md` | descartar (sem licença declarada) | Sem licença não há permissão de uso ou derivação |
| `skills/personalization-engine/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/abandonment-flow-suite/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/flow-performance-reviewer/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/sms-strategy-compliance/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/flow-audit-gap-finder/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/flow-builder-drafter/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/deliverability-list-health/SKILL.md` | descartar (sem licença declarada) | idem. **Cuidado particular:** é o arquivo mais tentador da lista, porque cobre SPF, DKIM, DMARC e requisitos Gmail/Yahoo, que é exatamente o que a nossa auditoria precisa. A cobertura vem do `email-marketing-bible` (MIT), do `chappie/deliverability` (MIT) e da documentação oficial, não daqui |
| `skills/customer-journey-mapper/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/winback-churn-prevention/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/retention-dashboard-reporting/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/campaign-calendar-planner/SKILL.md` | descartar (sem licença declarada) | idem |
| `skills/segmentation-auditor-builder/SKILL.md` | descartar (sem licença declarada) | idem |
| `.claude-plugin/marketplace.json`, `README.md` | descartar (sem licença declarada) | idem |

Fatos de conformidade que aparecem nesse repo (SPF, DKIM, DMARC, limiar de
0,3% do Gmail) **não são propriedade dele**: são documentação pública de
plataforma, e entram nos nossos rascunhos citando a documentação oficial e
o `evidencias-publicadas.md`, nunca este repo.

---

## Números folclóricos: lista de quarentena

Números que circulam nestes repos sem fonte primária. Se algum aparecer em
rascunho, entra **sempre** com rótulo de direcional e origem declarada.
Nenhum vira promessa a cliente e nenhum vira limiar de aprovação.

| Número | Onde aparece | Status |
|---|---|---|
| "+45% com gorjeta" | `taste-skill`, research/laziness | **Folclore.** Fora das regras, por decisão já registrada na pesquisa (F10) |
| "botão supera link de texto em +27%" | `email-marketing-bible` §8 | Direcional. O sentido é confirmado, o número não |
| "1 CTA supera vários em +42%" | `email-marketing-bible` §8 | Direcional. "1 CTA principal" é CONFIRMADA; o percentual não |
| "assunto abaixo de ~25 caracteres abre mais" | `email-marketing-bible` §8 | Direcional. C40 é **REFINADA**: curto sim, limite exato por teste |
| "lowercase casual bate title-case em ~14%" | `email-marketing-bible` §8 | Direcional, sem fonte |
| "~70% dos carrinhos são abandonados" | `email-campaign-skill` | Direcional, mercado americano |
| "recuperação de carrinho 5-15%" / "~17%" | `email-campaign-skill`, `email-marketing-bible` | Direcional, mercado americano |
| "flows rendem ~30x campanhas por destinatário" | `email-marketing-bible` §7 | Direcional, sem fonte |
| "e-mail rende $36 a $42 por $1" | `email-marketing-bible` §6 | Direcional, número de mercado muito repetido e pouco auditado |
| Benchmarks por tipo (welcome 50-60% abertura, etc.) | `email-marketing-bible` apêndice | Direcional, **mercado americano, meados de 2026**. Serve para calibrar severidade de auditoria, nunca como meta contratual |
| "Estudo de Adrian Krebs, abr/2026" e repo `ravidsrk/slop-detect` | Citado em F8 da nossa própria pesquisa | **A verificar.** Não confirmado; não citar até confirmar |
| "clipping do Gmail em 102 KB" | Vários repos | **A verificar.** O limite é folclore bem estabelecido e nunca reconfirmado aqui. Escrever "~102 KB (a verificar)" |

Contraste: os três itens de conformidade que **não** são direcionais e
podem ser afirmados sem ressalva, porque têm evidência forte de
documentação de plataforma: autenticação SPF + DKIM + DMARC; reclamação de
spam abaixo de 0,3% como limite duro do Gmail, com 0,1% como meta prática;
e one-click unsubscribe (RFC 8058).
