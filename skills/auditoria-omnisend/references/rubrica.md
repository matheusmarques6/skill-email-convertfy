# Rubrica de auditoria: 100 pontos

Aprovada em `docs/decisoes.md`, D-007.

## A premissa, declarada

Esta rubrica **não e neutra**. Ela pontua o que a Convertfy consegue
mudar, na operacao que a Convertfy tem. Quem usar em outro contexto
precisa repontuar.

As três premissas que produziram esta distribuicao:

1. **Conformidade vale mais que oportunidade.** Autenticação, taxa de
   reclamação e one-click unsubscribe tem evidência forte e consequência
   binaria: ou a conta entrega, ou não entrega. Oportunidade de receita e
   estimativa. Por isso entregabilidade subiu.
2. **Captacao costuma ser de outro time.** Na carteira da Convertfy, o
   formulario e o popup em geral são da agencia de trafego ou do próprio
   cliente. Pontuar pesado algo que a auditoria não consegue destravar
   produz nota baixa que ninguem aciona. Por isso captacao caiu.
3. **A conta e comparada com ela mesma primeiro.** Benchmark de mercado
   entra como contexto, nunca como critério de pontuacao. Duas contas com
   a mesma nota podem ter números absolutos muito diferentes.

Se alguma das três não valer para o caso, a rubrica esta errada para
aquele caso e a nota não deve ser comparada com a de outras contas.

## Distribuicao

| Dimensao | Pontos | Origem | Delta |
|---|---|---|---|
| Automações e cobertura de ciclo de vida | 25 | 25 | 0 |
| Entregabilidade e conformidade | **20** | 15 | **+5** |
| Dados e medicao | 15 | 15 | 0 |
| Programa de campanha | 15 | 15 | 0 |
| Audiência e segmentação | 10 | 10 | 0 |
| Conteudo e experimentacao | 10 | 10 | 0 |
| Captacao | **5** | 10 | **-5** |
| **Total** | **100** | 100 | |

A soma fecha em 100 dos dois lados: os 5 pontos de captacao foram para
entregabilidade, não criados.

## Automações e cobertura (25)

| Critério | Pontos | Como medir |
|---|---|---|
| Os 4 flows de receita existem e estao ativos | 10 | `get_automations`, conferir status |
| Carrinho e checkout com link testado | 5 | Envio de teste, clique. Ver T4 e T5 |
| Timing do primeiro toque coerente | 4 | `trigger.inactivitySettings` |
| Condição de saída definida | 3 | `exitConditions` |
| Sobreposicao controlada | 3 | `overlapLimiter`. Campanha manual **não** entra nele |

Zero em "os 4 existem" trava a dimensao em 10, porque o resto mede
qualidade de algo que não esta rodando.

## Entregabilidade e conformidade (20)

As três primeiras são conformidade. Reprovam sozinhas e não ha nota
parcial: ou passa, ou não passa, ou não foi verificado.

| Critério | Pontos | Como medir |
|---|---|---|
| SPF, DKIM e DMARC em `pass` | 6 | `.eml`, cabeçalho **de cima**. Não obtenivel pelo MCP |
| Reclamação de spam abaixo de 0,1% | 6 | `markedAsSpamRate` como aproximacao; o número que decide vive no Postmaster Tools |
| One-click unsubscribe (RFC 8058) | 4 | `List-Unsubscribe-Post` no `.eml`. Link no corpo **não** conta |
| Bounce dentro do aceitavel | 2 | `post_analytics_reports` |
| Higiene de base, sem inativo antigo | 2 | `post_analytics_statistics` |

`dmarc=none` **não e pass**: e ausencia de politica. Registre como
pendência, nunca como aprovado.

Checagem sem evidência vale `nao verificavel` e **não pontua**. Não
pontuar não e o mesmo que zerar: diga na nota quantos pontos ficaram
fora de medicao.

## Dados e medicao (15)

| Critério | Pontos |
|---|---|
| UTM consistente entre campanha e automação | 5 |
| Receita atribuida batendo com o Shopify | 5 |
| Os dois relogios entendidos por quem le o relatorio | 3 |
| Eventos customizados em uso, quando fazem sentido | 2 |

"Os dois relogios": `post_analytics_reports` conta por data de envio,
`post_analytics_statistics` por data do evento. Relatorio que mistura os
dois produz número que não fecha, e o cliente perde a confiança no resto.

## Programa de campanha (15)

| Critério | Pontos |
|---|---|
| Frequência coerente com a base | 5 |
| Segmentação real, não envio para tudo | 4 |
| Calendario existindo | 3 |
| Reenvio para não abriu, feito com critério | 3 |

## Audiência e segmentação (10)

| Critério | Pontos |
|---|---|
| Segmentos de ciclo de vida existem | 4 |
| Supressao de inativo | 3 |
| Consentimento por canal correto | 3 |

## Conteudo e experimentacao (10)

| Critério | Pontos |
|---|---|
| A/B rodando, com métrica declarada | 4 |
| Peca passa no `lint_email.py` | 3 |
| Peca passa no `lint_copy.py` | 3 |

## Captacao (5)

| Critério | Pontos |
|---|---|
| Formulario existe e alimenta o welcome | 3 |
| Oferta de captacao coerente com a do welcome | 2 |

Pontuacao baixa aqui **não** significa que captacao importa pouco.
Significa que a auditoria em geral não tem alcance para mudar. Se o
cliente também contratar captacao, repontue e diga no relatorio que
repontuou.

## Como reportar a nota

```
NOTA: 68/100
Nao verificavel: 10 pontos (autenticacao e one-click, sem .eml)
Nota sobre o medido: 68 de 90
```

Sempre as duas. Nota sobre 100 escondendo 10 pontos não medidos e nota
inflada para baixo, e o cliente não sabe se o problema e a conta ou a
coleta.
