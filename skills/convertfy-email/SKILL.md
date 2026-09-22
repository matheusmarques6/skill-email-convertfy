---
name: convertfy-email
description: Ponto de entrada da suite de e-mail da Convertfy. Use ao pedir qualquer coisa de e-mail marketing de e-commerce sem nomear a skill: escrever uma campanha, montar um flow, gerar o HTML, revisar uma peca pronta, comparar versões, auditar uma conta Omnisend. Roteia para a skill certa, aplica as regras fixas da Convertfy (layout neutro, copy sem vício de IA, HTML compatível com Outlook e dark mode) e roda o gate de lint antes de qualquer entrega. Cobre Omnisend como ESP principal e Klaviyo como secundario, para as 250+ lojas Shopify da carteira.
version: 0.1.0
user-invocable: true
argument-hint: "[campanha|flow|transacional|editorial · copy|design|qa|revisor|variantes|auditoria] [loja]"
---

Esta e a porta de entrada. Ela decide **qual skill atende**, carrega o
contexto certo e garante que nada saia sem passar pelo gate.

O objetivo da suite inteira e um só: **a peca tem que parecer feita por
uma loja, não gerada por um assistente.** Entre "impressionante" e
"indistinguivel de uma peca real", escolha sempre a segunda.

## Setup, uma vez por sessao

1. Leia `CLAUDE.md`. Ele manda sobre qualquer heuristica que uma skill
   invente. Precedencia em caso de conflito:
   **brief da loja > vault > CLAUDE.md > skill > vendor.**
2. Leia `shared/protocolo-de-execucao.md`. E o contrato de execução de
   toda skill que produz peca.
3. Identifique a loja e leia `marcas/<cliente>.md` se existir.
4. Só então escolha a rota abaixo.

Não carregue tudo. Cada rota diz o que ler.

## Modos

O modo decide o orçamento de copy, o peso da oferta e o que o lint cobra.
Escolha pelo **papel do envio**, não pelo produto da loja.

| Modo | Quando | O que muda |
|---|---|---|
| **campanha** | Envio pontual para segmento: promocao, lancamento, data | Corpo até 80 palavras (C45). Oferta e prazo obrigatorios no texto vivo (C42, C46). Um CTA principal |
| **flow de recuperacao** | Automação disparada por comportamento: carrinho, checkout, navegacao, winback | Corpo até 60 palavras. O gatilho e a condição de saída importam mais que a copy. Nunca prometa estoque que não foi checado (C06) |
| **transacional** | Confirmação, envio, entrega, troca | Sem copy de venda no assunto. C03 e o risco central: campanha não pode se disfarcar de transacional, e transacional não vira vitrine |
| **editorial** | Carta, conteudo, novidade sem oferta | Único modo que dispensa o teto de palavras, e só quando o brief pede por escrito. Continua proibido storytelling fabricado (C05) |

Na dúvida entre campanha e editorial, e campanha. Editorial precisa de
pedido explícito no brief.

## Comandos

| Comando | Faz | Skill / reference |
|---|---|---|
| `copy [loja]` | Assunto, preheader, headline, corpo, CTA, alt | [skills/email-copy/SKILL.md](../email-copy/SKILL.md) |
| `assunto [loja]` | Só assunto e preheader | [email-copy/references/assunto-e-preheader.md](../email-copy/references/assunto-e-preheader.md) |
| `oferta [loja]` | Condição da oferta: valor, código, prazo, mínimo | [email-copy/references/oferta-e-condição.md](../email-copy/references/oferta-e-condição.md) |
| `design [peca]` | Monta o HTML: 600px, inline, bulletproof, dark mode | [skills/email-design/SKILL.md](../email-design/SKILL.md) |
| `darkmode [peca]` | Só o passe de dark mode | [email-design/references/dark-mode.md](../email-design/references/dark-mode.md) |
| `flow [tipo] [loja]` | Desenha a automação no Omnisend | [skills/email-flows/SKILL.md](../email-flows/SKILL.md) |
| `klaviyo [variavel]` | Equivalencia Klaviyo para Omnisend | [email-flows/references/equivalencia-klaviyo-omnisend.md](../email-flows/references/equivalencia-klaviyo-omnisend.md) |
| `qa [peca]` | Gate final: vai ou não vai | [skills/email-qa/SKILL.md](../email-qa/SKILL.md) |
| `eml [arquivo]` | Autenticação e one-click a partir do `.eml` | [email-qa/references/eml.md](../email-qa/references/eml.md) |
| `revisar [peca]` | Revisor separado, nota /10, lista de IDs | [skills/email-revisor/SKILL.md](../email-revisor/SKILL.md) |
| `variantes [peca]` | 3 versões divergindo em eixo nomeado | [skills/email-variantes/SKILL.md](../email-variantes/SKILL.md) |
| `calendario [loja] [mes]` | Planeja o mês: envios, papel, público, modelo | [skills/email-calendario/SKILL.md](../email-calendario/SKILL.md) |
| `sazonal [data] [loja]` | Escolhe o modelo validado do papel | [skills/email-campanhas-sazonais/SKILL.md](../email-campanhas-sazonais/SKILL.md) |
| `familia [papel]` | Familia de assunto do papel, com o dado | [email-copy/references/familias-de-assunto.md](../email-copy/references/familias-de-assunto.md) |
| `auditoria [loja]` | Audita a conta Omnisend inteira | [skills/auditoria-omnisend/SKILL.md](../auditoria-omnisend/SKILL.md) |
| `lint [peca]` | Só o gate, sem gerar nada | `scripts/lint_copy.py`, `scripts/lint_email.py` |

Pedido sem comando nomeado: escolha pela tabela de roteamento abaixo.

## Roteamento

| O que o usuario diz | Rota |
|---|---|
| "escreve um e-mail de X" | `copy`, depois `design`, depois `qa` |
| "monta o HTML disso" | `design`, depois `qa` |
| "cria o flow de carrinho" | `flow`, depois `copy` por toque, depois `design` |
| "isso aqui esta bom?" | `revisar` |
| "pode enviar?" | `qa` |
| "me da opções" | `variantes` |
| "monta o calendario de novembro" | `calendario` |
| "qual modelo usar no 11.11" | `sazonal` |
| "que assunto usar no pico das 18h" | `familia` |
| "por que a conta X caiu" | `auditoria` |
| "tira a cara de IA disso" | `revisar`, e só depois `copy` no que ele apontar |

Peca completa do zero e sempre a cadeia inteira:

```
calendario (se for plano)  ->  sazonal (se for data)  ->  copy  ->  design  ->  qa
flow (se for automacao)    ->  copy  ->  design  ->  qa
```

`revisar` e `variantes` são opcionais e entram entre `copy` e `design`.

**Campanha de data sazonal comeca em `calendario` ou `sazonal`**, nunca
em `copy`: o papel do envio decide o modelo, e o modelo decide a
estrutura. Pular para a copy produz peca sem papel, que e o defeito que a
carteira mediu como esquenta em tom de anuncio (1 pedido).

## O que vale em toda rota

Detalhe em `shared/protocolo-de-execucao.md`. O resumo que o roteador
cobra antes de despachar:

1. **Ficha e brief (P01, P02).** Sem `marcas/<cliente>.md` e sem brief
   com **oferta, produto e prazo**, não despache: peca o que falta.
2. **Uma linha de leitura do brief**, antes de gerar. Se ambíguo, **uma
   pergunta só**, juntando tudo.
3. **Anti-vícios sempre**: `shared/anti-vicios-copy.md`,
   `anti-vicios-design.md`, `anti-vicios-processo.md`, e
   `shared/calibracao.md` junto, para não reprovar convenção legitima.
4. **Gate de lint antes de entregar.** Violacao B não entrega.
5. **Só o artefato (C07).** Sem comentario sobre a própria copy.
6. **Ordem de trabalho (P08)**: intencao (var1), estrutura (var2),
   variantes do arsenal, copy por schema. Nesta ordem.

## As regras que nenhuma rota negocia

Vem do `CLAUDE.md`. Skill que precise divergir declara no próprio
SKILL.md, com motivo.

- Fundo branco, texto preto, **sem paleta autoral**. Cor da marca só
  quando o brief exigir, e em acento.
- Container 600px, tabelas `role="presentation"`, estilos inline, botao
  bulletproof com VML, compatível com Outlook, seguro para dark mode.
- Copy curta, genérica e realista. Sem storytelling elaborado.
- **Travessão proibido em qualquer copy.** E o primeiro item de toda eval.
- Em spec: "tipografia principal", fonte secundaria nomeada, "cor
  primaria", "cor secundaria".

## As 8 categorias de bloco

`header`, `hero`, `body`, `products`, `reviews`, `cta`, `offer`, `footer`.

Os mesmos nomes do vault. `header` e `cta` tem **zero variantes** hoje:
zero candidata não e erro, declare a lacuna e não invente variante.

## O que a suite nunca faz

- Não inventa número, estoque, prazo, depoimento ou avaliacao (C02, C06).
- Não edita o `vault/`. Ele e somente leitura daqui.
- Não copia nada de `vendor/`. O que reaproveitamos e reescrito, com
  credito em `NOTICE.md`.
- Não entrega peca com violacao B.
- Não explica a própria copy junto da entrega (C07).
- Não afirma que uma checagem passou sem evidência: marca
  `nao verificado`.


## Contrato de variante

O **contrato novo e o canonico**. Esta skill só gera no contrato novo.

Das 75 notas de variante do vault, 32 já estao no contrato novo e **43
estao no legado**. Quando o protocolo de seleção escolher uma legada,
converta antes de usar:

```bash
python3 scripts/adaptar_variante_legado.py <slug> --json
```

O adaptador carrega os campos compartilhados, deriva `profundidade` e
aposenta `momento`, `ativa` e os outros campos que sairam do contrato.

**`aliviador` não deriva de nada.** Vem de `shared/aliviador-legado.json`,
que e o registro das decisões humanas. Slug sem entrada la volta como
`[FALTA: decisao humana]` e o adaptador sai com exit code 1.

Variante legada com pendência **não pode ser usada para gerar**: peca a
decisão de `aliviador` ou escolha outra variante. Nunca preencha por
inferencia, nem copie o `aliviador` de uma variante parecida.

Ver `docs/vault/migracao-contrato.md`.

## Referências

| Arquivo | Quando |
|---|---|
| `shared/protocolo-de-execucao.md` | Sempre, antes de despachar |
| `shared/calibracao.md` | Antes de reprovar qualquer coisa |
| `shared/postura-revisao.md` | Ao acionar `revisar` |
| `docs/pesquisa/pesquisa-vicios-ia-email.md` | A origem dos IDs C, D e P |
| `docs/pesquisa/evidencias-publicadas.md` | A força da evidência de cada regra |
| `docs/pesquisa/a-verificar.md` | O que não pode ser citado como fato |
| `docs/indice-vault.md` | Achar a nota de intencao ou estrutura |
| `shared/vocabulario-arsenal.md` | Traduzir descrição vaga em slug de variante |
| `shared/principios-carteira.md` | 80/10/10 e os cinco principios da carteira |
| `shared/segmentacao-e-freios.md` | Camadas, nível de conta e freios |
| `docs/dados/resumo-carteira.md` | Os números que as skills citam |
| `docs/reconciliacao-regras-dados.md` | Regras em disputa, aguardando aprovação |
