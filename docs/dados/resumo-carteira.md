# Resumo dos dados da carteira

Os números que as skills citam. **As skills citam este arquivo, nunca o
CSV.** Fonte primária em `fontes/BFCM-2026-Convertfy/09_Dados/`.

## O que é o índice

**Índice = receita por mil da campanha ÷ receita por mil média daquela
loja no trimestre.** Índice 1 é a média da própria loja, índice 2 é o
dobro. Serve para comparar lojas de tamanho e moeda diferentes.

Definição em `09_Dados/Base de dados do estudo (dicionario e metodo).md`,
seção B.2.

## Amostras

| Sigla | Amostra | Período | Volume |
|---|---|---|---|
| Ampla | 46 lojas da carteira | 15/06 a 20/09/2026 | `ranking_46_lojas_2026-09-21.csv` |
| Profunda | 9 lojas Omnisend | mai a set/2026 | `base_campanhas_525_9_lojas.csv` |
| Três lojas | Emyerre, Blue Wolf, Clube Rock | 17/06 a 17/09/2026 | 101 envios |
| Figma | Blue Wolf, jul a set | | 36 e-mails com altura em px |

**Quando as duas amostras discordam, vale a ampla.**

## Médias por loja

| Loja | Média do trimestre |
|---|---|
| Blue Wolf | US$ 43,58 por mil |

## Os números mais citados

### Campanhas que funcionaram

| Campanha | Índice | Detalhe |
|---|---|---|
| Notificação do futuro | **1,67** | 24 de 39 lojas, 3,61% de clique |
| Status mudou, 18h | **1,48** | 25 de 33 lojas. Assunto 2,13 |
| Figurinha | 1,35 | 14 de 24 |
| Última chamada 21h30 | 1,22 | US$ 105,3 por mil |
| Sexta premiada | 1,17 | US$ 50,2 por mil |
| Ligação | 1,17 | 15 de 28 |
| Reabertura | 1,15 | 17 de 28 |
| Favoritos | 1,12 | 3,19% de clique |
| Jornal | 1,10 | 1,62 nas 9 lojas |
| Cupom liberado, 07h | 0,95 na ampla | 1,66 nas 9 lojas |

### Assuntos, por receita

| Assunto | Índice |
|---|---|
| 🚨 Your status has just changed | **2,13** (5 de 5) |
| Your coupon has been approved ✅ | 1,86 |
| [Nome], have you seen what is coming? 👀 | 1,77 |
| 🟥 A red card for anyone who misses out | 1,65 |
| [Nome], the news you did not want to hear | 1,59 |
| [Nome], you still need to confirm | 1,52 |
| (1) hidden discount for [nome] 🤫 | 1,50 |
| your access is confirmed ✅ | 1,48 |
| [Nome], your invitation has arrived 🎟️ | 1,43 |
| **Fwd: ou Enc:** | **0,39 a 0,49** |

### O que falhou

| O que | Dado |
|---|---|
| Esquenta em tom de anúncio | **1 pedido** |
| Véspera como modelo | 0,10 na ampla |
| Extensão de oferta | 0,49 e 0,52 |
| Evento colado em outro | 0,38 a 0,50 |
| Promessa repetida na antecipação | 0,39 a 0,52 |
| Acesso pendente na véspera | 0,77 na Blue Wolf, 0,10 na ampla |
| E-mail longo demais | 4.136 px |

### Segmento pesa mais que modelo

| Loja | Engajados | Lista toda |
|---|---|---|
| Donaris | R$ 92,5 por mil | R$ 17,5 por mil |
| Brinque Mais | R$ 176,0 por mil | R$ 41,4 por mil |
| Segmento ampliado | US$ 22 por mil | contra US$ 55 antes |

### Antecipação

| Loja e data | Antecipação | Dia do pico |
|---|---|---|
| Blue Wolf 7.7 | US$ 2.700 | US$ 2.510 |
| 8.8 | 46% da receita do pico | |
| 9.9 | 70% da receita do pico | |
| Clube Rock | 43% a 61% | |

O pico faz o mesmo número de pedidos a cada data (32, 33, 35). **O que
muda o total é a antecipação e o pós.**

## Limites destes números

- Atribuição da Omnisend é por clique **e por abertura**, na janela
  configurada na conta. Não é atribuição de último clique.
- **Abertura é inflada** pela proteção de privacidade da Apple. Usar como
  sinal auxiliar, nunca como métrica de decisão.
- Ficaram fora da base: envios de teste abaixo de 1.000 contatos e
  envios em andamento na data da coleta.
- A amostra de 9 lojas é pequena para conclusão por loja. Serve para
  mediana, não para caso individual.
