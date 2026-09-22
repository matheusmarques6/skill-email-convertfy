# Auditoria da fusão

Verificação item a item do que foi absorvido dos repos de referência.
Regra: afirmação sem evidência conta como NÃO FEITO.

Legenda: **FEITO** · **PARCIAL** · **NÃO FEITO** · **DESCARTADO**

---

## 1. davidharttx/email-campaign-skill

### 1a. Os 10 flows — FEITO

`skills/email-flows/references/os-10-flows.md`, um por cabeçalho `##`:

| # | Flow | Linha |
|---|---|---|
| 1 | Welcome | 17 |
| 2 | Carrinho abandonado | 52 |
| 3 | Checkout abandonado | 90 |
| 4 | Navegação abandonada | 124 |
| 5 | Pós-compra | 155 |
| 6 | Nutrição | 189 |
| 7 | Winback | 226 |
| 8 | Reposição | 266 |
| 9 | Sunset | 296 |
| 10 | Pedido de avaliação | 333 |

Mais a matriz de colisão (linha 363) e a regra dos descontos empilhados
(linha 382), que o original não tinha nessa forma.

### 1b. Equivalência Klaviyo → Omnisend — PARCIAL

`references/equivalencia-klaviyo-omnisend.md`, 117 linhas de tabela.

Confirmado no MCP e em uso: nomes de evento Shopify (`subscribed to
marketing`, `added product to cart`, `started checkout`, `placed order`,
`product back in stock`, `entered segment`), `trigger.inactivitySettings`,
`exitConditions`, `frequencyLimiter`, `overlapLimiter`, tags
`[[contact.first_name]]`, `[[unsubscribe_link]]`.

**Sem equivalente, marcados `nao verificado`:** T1 (valor padrão para tag
vazia), T3 (propriedade de evento como merge tag em texto), T4 (link de
recuperação de carrinho na origem `shopify`), T5 (link de retomada de
checkout). Mais T2 e T6 a T10 em prioridade menor. Fallback obrigatório
para cada um em `skills/email-flows/SKILL.md`, seção "Não verificado no
Omnisend". Roteiro para fechar: `docs/omnisend/roteiro-de-teste.md`.

### 1c. /campaign-calendar — NÃO FEITO

`ls skills/` devolve 8 skills e **nenhuma de calendário**. A lógica de
calendário mensal com brief por e-mail, segmentação e nota de design não
foi aproveitada.

Resolvido na Fase 3.4: `skills/email-calendario`.

### 1d. Descartado

| O que | Por quê |
|---|---|
| Template HTML com `#FAF7F2` de fundo, `border-radius:12px`, verde `#1A3D28`, botão sem VML | Viola o layout neutro do CLAUDE.md em três pontos, e o bege é D03 |
| Carta do fundador obrigatória com P.S. em todo flow | C05 e C16 institucionalizados |
| Trust bar de 3 sinais em todo e-mail | D08 virando estrutura obrigatória |
| Cota de "3 de 5 pilares" por flow | Produz e-mail de enchimento, estoura C45 |

---

## 2. framix-team/skill-email-html-mjml

### 2a. Decisão de não adotar — FEITO

`docs/decisoes.md:28`, D-002, com motivo e critério de revisitar.
Repetido em `skills/email-design/SKILL.md`.

### 2b. Conhecimento de compatibilidade — PARCIAL

| Item | Status | Onde |
|---|---|---|
| `role="presentation"` | FEITO | `email-design/SKILL.md`, `references/checklist-tecnico.md` |
| Estilos inline | FEITO | 3 arquivos de `email-design/` |
| Botão bulletproof com VML | FEITO | `SKILL.md` e `checklist-tecnico.md` |
| Condicionais MSO | FEITO | 2 arquivos |
| Dark mode, `color-scheme` | FEITO | 3 arquivos, mais `references/dark-mode.md` inteiro |
| Cores seguras em dark | FEITO | `dark-mode.md`, `#121212` em vez de `#000` |
| Largura travada em 600 | FEITO | `SKILL.md`, e `E_CONTAINER` no lint |
| `alt` | FEITO | 4 arquivos, mais D17 e Q03 |
| Contraste | FEITO | 3 arquivos, e `regra_contraste` no lint |
| **Imagens retina** | **PARCIAL** | Uma linha só: `checklist-tecnico.md:92`. Não há regra de export 2x nem checagem |
| **`lang`** | **PARCIAL** | Só dentro do exemplo de HTML em `SKILL.md:245`. Não é regra nem item de lint |

---

## 3. EmailBoutique-Digital-Inc/email-html-qa-skill

### 3a e 3b. Checagens — PARCIAL

| Checagem | Onde | Tipo |
|---|---|---|
| Outlook, Gmail, Apple | `email-qa` Q01 | manual |
| Dark mode forçado | `email-qa` Q02 | manual |
| Clipping acima de 102 KB | `lint_email.py` `E_TAMANHO` (B) | **lint** |
| Imagens e alt | D17 no lint, Q03 manual | os dois |
| Links e CTAs | `email-qa` Q04 | manual |
| Preheader | `lint_email.py` `E_PREHEADER` | **lint** |
| Fallback de personalização | C47 no lint, Q06 manual | os dois |
| SPF, DKIM, DMARC | `email-qa/references/eml.md` | manual, exige `.eml` |
| Unsubscribe one-click | `references/eml.md` | manual, exige `.eml` |
| Compliance (descadastro visível, endereço) | Q07 e Q08 | manual |
| **Responsivo** | **ausente** | grep por "responsiv" em `email-qa/` e `lint_email.py`: 0 |
| **Acessibilidade como bloco** | **ausente** | grep por "acessib": 0. Há alt e contraste soltos, sem a checagem de conjunto |

### 3c. Relatório por severidade — FEITO

`email-qa/SKILL.md`, seção "Formato do veredito": B, A, M e
`nao verificado`, com a regra de que não existe "aprovado com ressalva".

---

## 4. CosmoBlk/email-marketing-bible

### 4a. Seções que entraram

| Seção | Onde |
|---|---|
| §4 e §5 (anti-slop) | `shared/anti-vicios-copy.md`, `anti-vicios-design.md` |
| §8 (calibração) | `shared/calibracao.md` |
| Critic loop | `shared/postura-revisao.md`, teto de 4 rodadas |
| Entregabilidade | `skills/auditoria-omnisend/references/conformidade-remetente.md` |
| Benchmarks | Rotulados direcionais, do mercado americano |
| `#121212` no dark mode | `email-design/references/dark-mode.md` |

### 4b. "own a colour" NÃO entrou — CONFIRMADO

Grep por "own a colour", "own one colour" e "cor autoral" em `shared/` e
`skills/`: a única ocorrência é
`skills/email-variantes/references/comparativo.md:35`, e é **proibição**
("cor autoral aqui contamina a leitura"). O conceito não foi adotado.

### 4c. Ignorado

"Google filtra texto de alta similaridade com IA" (§4, repetido no §11):
descartado como especulação sem evidência primária, conforme
`docs/pesquisa/evidencias-publicadas.md`. Registrado em
`docs/destilacao/matriz.md` com a reposição correta.

---

## 5. Impeccable

| Item | Status | Evidência |
|---|---|---|
| a. Roteador + tabela de comandos | FEITO | `skills/convertfy-email/SKILL.md` |
| b. PRODUCT/DESIGN → ficha da loja | FEITO | `marcas/_template.md`, nomenclatura obrigatória |
| c. Modes | FEITO | campanha, flow de recuperação, transacional, editorial |
| d. craft-floor Verify/Refuse | FEITO | `shared/anti-vicios-*.md`, IDs C, D, P |
| e. critique com nota | **PARCIAL** | Nota /10 existe em `email-revisor`. **O snapshot NÃO é salvo**: grep por "snapshot" em `email-revisor/`: 0. Não há como comparar evolução entre rodadas |
| f. audit | FEITO | `skills/auditoria-omnisend` |
| g. detector automático | FEITO, cobertura maior | slop-detect tem 32 padrões; nosso lint tem 30 regras em `lint_copy.py` e 11 em `lint_email.py`, sobre 38 IDs C e 31 IDs D |
| h. polish, distill, clarify, typeset, layout | **NÃO FEITO** | Nenhum aparece no roteador. Só "layout" e por acaso |
| i. subagentes | **NÃO FEITO** | Nenhum equivalente de finish-reviewer, asset-producer, documenter |
| j. doctor | **NÃO FEITO** | Não há checagem de divergência entre skill, vault e arsenal |

---

## 6. Taste Skill

| Item | Status | Evidência |
|---|---|---|
| a. Leitura do brief + 1 pergunta | FEITO | `shared/protocolo-de-execucao.md`, item 4, 6 ocorrências |
| b. 3 dials de e-mail | **NÃO FEITO** | Nenhum dial de densidade, peso da oferta ou tom. Não há ligação com escolha de variante |
| c. output-skill anti-truncamento | PARCIAL | P04 existe em `anti-vicios-processo.md`; a parte detectável é `E_PLACEHOLDER` (B) no lint. Falta a contagem de entregáveis antes e depois |
| d. redesign, prioridade + "o que a IA esquece" | **NÃO FEITO** | Nenhum equivalente |
| e. imagegen, direção de imagem por slot | **NÃO FEITO** | Não há proporção nomeada nem prompt pronto por slot do arsenal |
| f. brandkit | FEITO | `marcas/_template.md` com tipografia principal, fonte secundária, cor primária e secundária |
| g. minimalist | FEITO | Layout neutro é a regra fixa do `CLAUDE.md` |

---

## 7. Emil Kowalski

| Item | Status | Evidência |
|---|---|---|
| a. prototype → email-variantes | FEITO | Eixo nomeado (oferta, prova, problema) e `index.html` em `references/comparativo.md` |
| b. animation-vocabulary → vocabulario-arsenal | FEITO | 7 ocorrências de "desempate". A regra entre as variantes de prova social está escrita, com TODO nomeado onde o vault não declara o critério |
| c. review-animations → postura | FEITO | `shared/postura-revisao.md` |
| d. improve-animations, PLAN-TEMPLATE → admin | **NÃO FEITO** | Grep por "PLAN-TEMPLATE" e "admin-convertfy": 0 |

---

## Resumo

| Bloco | FEITO | PARCIAL | NÃO FEITO |
|---|---|---|---|
| 1. davidharttx | 1 | 1 | 1 |
| 2. framix | 1 | 1 | 0 |
| 3. email-html-qa | 1 | 1 | 0 |
| 4. bible | 3 | 0 | 0 |
| 5. Impeccable | 6 | 1 | 3 |
| 6. Taste | 3 | 1 | 3 |
| 7. Emil | 3 | 0 | 1 |
| **Total** | **18** | **5** | **8** |
