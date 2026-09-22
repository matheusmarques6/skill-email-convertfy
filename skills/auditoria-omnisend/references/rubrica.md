# Rubrica de auditoria: 100 pontos

Aprovada em `docs/decisoes.md`, D-007.

## A premissa, declarada

Esta rubrica **nao e neutra**. Ela pontua o que a Convertfy consegue
mudar, na operacao que a Convertfy tem. Quem usar em outro contexto
precisa repontuar.

As tres premissas que produziram esta distribuicao:

1. **Conformidade vale mais que oportunidade.** Autenticacao, taxa de
   reclamacao e one-click unsubscribe tem evidencia forte e consequencia
   binaria: ou a conta entrega, ou nao entrega. Oportunidade de receita e
   estimativa. Por isso entregabilidade subiu.
2. **Captacao costuma ser de outro time.** Na carteira da Convertfy, o
   formulario e o popup em geral sao da agencia de trafego ou do proprio
   cliente. Pontuar pesado algo que a auditoria nao consegue destravar
   produz nota baixa que ninguem aciona. Por isso captacao caiu.
3. **A conta e comparada com ela mesma primeiro.** Benchmark de mercado
   entra como contexto, nunca como criterio de pontuacao. Duas contas com
   a mesma nota podem ter numeros absolutos muito diferentes.

Se alguma das tres nao valer para o caso, a rubrica esta errada para
aquele caso e a nota nao deve ser comparada com a de outras contas.

## Distribuicao

| Dimensao | Pontos | Origem | Delta |
|---|---|---|---|
| Automacoes e cobertura de ciclo de vida | 25 | 25 | 0 |
| Entregabilidade e conformidade | **20** | 15 | **+5** |
| Dados e medicao | 15 | 15 | 0 |
| Programa de campanha | 15 | 15 | 0 |
| Audiencia e segmentacao | 10 | 10 | 0 |
| Conteudo e experimentacao | 10 | 10 | 0 |
| Captacao | **5** | 10 | **-5** |
| **Total** | **100** | 100 | |

A soma fecha em 100 dos dois lados: os 5 pontos de captacao foram para
entregabilidade, nao criados.

## Automacoes e cobertura (25)

| Criterio | Pontos | Como medir |
|---|---|---|
| Os 4 flows de receita existem e estao ativos | 10 | `get_automations`, conferir status |
| Carrinho e checkout com link testado | 5 | Envio de teste, clique. Ver T4 e T5 |
| Timing do primeiro toque coerente | 4 | `trigger.inactivitySettings` |
| Condicao de saida definida | 3 | `exitConditions` |
| Sobreposicao controlada | 3 | `overlapLimiter`. Campanha manual **nao** entra nele |

Zero em "os 4 existem" trava a dimensao em 10, porque o resto mede
qualidade de algo que nao esta rodando.

## Entregabilidade e conformidade (20)

As tres primeiras sao conformidade. Reprovam sozinhas e nao ha nota
parcial: ou passa, ou nao passa, ou nao foi verificado.

| Criterio | Pontos | Como medir |
|---|---|---|
| SPF, DKIM e DMARC em `pass` | 6 | `.eml`, cabecalho **de cima**. Nao obtenivel pelo MCP |
| Reclamacao de spam abaixo de 0,1% | 6 | `markedAsSpamRate` como aproximacao; o numero que decide vive no Postmaster Tools |
| One-click unsubscribe (RFC 8058) | 4 | `List-Unsubscribe-Post` no `.eml`. Link no corpo **nao** conta |
| Bounce dentro do aceitavel | 2 | `post_analytics_reports` |
| Higiene de base, sem inativo antigo | 2 | `post_analytics_statistics` |

`dmarc=none` **nao e pass**: e ausencia de politica. Registre como
pendencia, nunca como aprovado.

Checagem sem evidencia vale `nao verificavel` e **nao pontua**. Nao
pontuar nao e o mesmo que zerar: diga na nota quantos pontos ficaram
fora de medicao.

## Dados e medicao (15)

| Criterio | Pontos |
|---|---|
| UTM consistente entre campanha e automacao | 5 |
| Receita atribuida batendo com o Shopify | 5 |
| Os dois relogios entendidos por quem le o relatorio | 3 |
| Eventos customizados em uso, quando fazem sentido | 2 |

"Os dois relogios": `post_analytics_reports` conta por data de envio,
`post_analytics_statistics` por data do evento. Relatorio que mistura os
dois produz numero que nao fecha, e o cliente perde a confianca no resto.

## Programa de campanha (15)

| Criterio | Pontos |
|---|---|
| Frequencia coerente com a base | 5 |
| Segmentacao real, nao envio para tudo | 4 |
| Calendario existindo | 3 |
| Reenvio para nao abriu, feito com criterio | 3 |

## Audiencia e segmentacao (10)

| Criterio | Pontos |
|---|---|
| Segmentos de ciclo de vida existem | 4 |
| Supressao de inativo | 3 |
| Consentimento por canal correto | 3 |

## Conteudo e experimentacao (10)

| Criterio | Pontos |
|---|---|
| A/B rodando, com metrica declarada | 4 |
| Peca passa no `lint_email.py` | 3 |
| Peca passa no `lint_copy.py` | 3 |

## Captacao (5)

| Criterio | Pontos |
|---|---|
| Formulario existe e alimenta o welcome | 3 |
| Oferta de captacao coerente com a do welcome | 2 |

Pontuacao baixa aqui **nao** significa que captacao importa pouco.
Significa que a auditoria em geral nao tem alcance para mudar. Se o
cliente tambem contratar captacao, repontue e diga no relatorio que
repontuou.

## Como reportar a nota

```
NOTA: 68/100
Nao verificavel: 10 pontos (autenticacao e one-click, sem .eml)
Nota sobre o medido: 68 de 90
```

Sempre as duas. Nota sobre 100 escondendo 10 pontos nao medidos e nota
inflada para baixo, e o cliente nao sabe se o problema e a conta ou a
coleta.
