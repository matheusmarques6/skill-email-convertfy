# Biblioteca de modelos de campanha validados

Fonte: `fontes/BFCM-2026-Convertfy/05_Modelos_validados/` (36 notas) e
`ranking-de-modelos.md`, recalculado em 21/09/2026.

**Índice 1 = a receita por mil média da própria loja.**

Duas amostras: 46 lojas da carteira (ampla) e 9 lojas analisadas a fundo.
**Quando discordam, vale a ampla.**

## Situação de cada modelo

| Situação | O que significa | Uso no calendário |
|---|---|---|
| Titular | Índice acima de 1 na amostra ampla | Livre |
| Titular com ressalva | Ampla abaixo de 1, 9 lojas acima | Só com justificativa no brief |
| Teste | Sem dado ainda | Máximo 1 por plano |
| Reserva | Foi rebaixado | Só se nada do papel servir |
| Fora do calendário | Índice baixo nas duas | **Não usar** |

## Ranking

| Modelo | 46 lojas | 9 lojas | Situação |
|---|---|---|---|
| `notificacao-do-futuro` | 1,67 | 1,43 | Titular |
| `status-mudou-18h` | 1,48 | 1,90 | Titular |
| `figurinha` | 1,35 | 1,80 | Titular |
| `ultima-chamada-2130` | 1,22 | 1,46 | Teste |
| `sexta-premiada` | 1,17 | 1,22 | Titular |
| `ligacao` | 1,17 | 0,91 | Titular |
| `reabertura` | 1,15 | 1,11 | Titular |
| `favoritos` | 1,12 | - | Titular |
| `jornal` | 1,10 | 1,62 | Titular |
| `convite` | 0,98 | 1,55 | Titular com ressalva |
| `social-proof` | 0,98 | 1,20 | Titular com ressalva |
| `cupom-liberado-7h` | 0,95 | 1,66 | Titular com ressalva |
| `segunda-turbo` | 0,83 | 1,06 | Titular com ressalva |
| `catalogo-fecha-mes` | 0,79 | 1,13 | Titular com ressalva |
| `reenvio-11h` | 0,67 | 1,24 | Titular com ressalva |
| `ressaca` | 0,56 | 0,78 | Titular com ressalva |
| `extensao-lista-toda` | 0,52 | 0,50 | Fora do calendário |
| `agenda` | 0,37 | 1,21 | Em revisão |
| `conceito-sem-oferta` | 0,28 | 0,55 | Fora do calendário |
| `esquenta` | 0,27 | 0,50 | Fora do calendário |
| `vespera` | 0,10 | 0,55 | Fora do calendário |
| `acesso-liberado-00h` | - | - | Teste |
| `revele` | 0,00 | 1,22 | Reserva |
| `tema-do-momento` | 0,00 | 1,27 | Reserva |
| `guia-presentes` | - | - | Teste |
| `prazo-entrega` | - | - | Teste |
| `vale-presente` | - | - | Teste |
| `texto-pessoa` | - | - | Teste |
| `reativacao` | - | - | Teste |
| `on-off` | 0,00 | 0,99 | Titular com ressalva |

## Por papel na sequência

| Papel | Modelo titular | Dado |
|---|---|---|
| Antecipação 1 | `convite` | 1,55 nas 9 lojas, 0,98 na ampla (ressalva) |
| Antecipação 2 | `agenda` | 44,3% de abertura, 14 pedidos. **Em revisão**: 0,37 na ampla, só VIP e E30 |
| Antecipação 3 | `acesso-liberado-00h` | Teste |
| Véspera | `vespera` | **0,10 na ampla. Fora do calendário** |
| **Pico 07h** | `cupom-liberado-7h` | 1,66 nas 9 lojas, 0,95 na ampla (ressalva) |
| **Pico 11h** | `reenvio-11h` | 1,24 nas 9 lojas, 0,67 na ampla (ressalva) |
| **Pico 18h** | `status-mudou-18h` | **1,48 na ampla, 25 de 33 lojas. Titular** |
| Fechamento | `notificacao-do-futuro` | **1,67, o melhor da base. 24 de 39** |
| Último dia | `ligacao` | 1,17, promovido a titular |
| Dia seguinte | `reabertura` | 1,15 |
| D+2 pós-pico | Aviso de estoque, fundo branco | 14 pedidos, US$ 77,7 por mil |
| D+5 a D+8 | `favoritos` | 1,12, 3,19% de clique |
| Meio de semana | `jornal` | 1,10 na ampla, 1,62 nas 9 |
| Sexta | `sexta-premiada` | 1,17 |
| Início de semana | `segunda-turbo` | 0,83 (ressalva) |
| Gamificada | `figurinha` | 1,35 |

## O que não funcionou, não repetir

Da seção 3 do SKILL BFCM. Cada um com o número:

| O que | Dado |
|---|---|
| Esquenta em tom de anúncio ("The Warm-Up Has Begun") | **1 pedido.** Falava da marca e do evento, sem número nem prazo, com dois botões vagos |
| Assunto com `Fwd:` ou `Enc:` | 0,39 a 0,49 |
| Promessa repetida na antecipação ("na lista", "prometi", "garantido") | 0,39 a 0,52 |
| "Acesso pendente" na véspera | 0,77 na Blue Wolf, 0,10 na ampla |
| Segmento ampliado sem critério | Os 5,2 mil a mais não abriram. Por mil caiu de US$ 55 para US$ 22 |
| Evento colado em outro (VIP Day logo após o 9.9) | 0,38 a 0,50 |
| Extensão ("virou semana", "VIP Week") | 0,49 e 0,52 |
| Depoimento sem oferta | Abre, mas vende pouco |
| E-mail longo demais | O 11h do 9.9 tinha **4.136 px** |

## Quando não usar um modelo titular

- **`status-mudou-18h` fora das 18h do pico.** O assunto de mudança de
  estado é o de maior receita da base e queima se repetir.
- **`agenda` para lista toda.** 0,37 na ampla. Só VIP e E30.
- **Qualquer modelo duas vezes na mesma semana.** O ranking mede envio
  isolado, não repetição.
- **`vespera`, `esquenta`, `conceito-sem-oferta`, `extensao-lista-toda`:**
  fora do calendário nas duas amostras.

## Estrutura do dia de pico

| Envio | Modelo | Público |
|---|---|---|
| 00h | Acesso antecipado, tela desbloqueada | Engajados de 30 dias + quem cumpriu a tarefa |
| 07h | Texto de pessoa com o cupom | O mais largo, pelo nível da conta: A = lista ativa, B = E365, C = E180. Em duas levas |
| 11h | Relógio ou clube VIP, cupom no topo | E180 (C: E90) |
| 18h | Status mudou, com a surpresa | E90 |
| 20h30 | Notificação do futuro ou last call | Engajados de 30 dias que clicaram hoje |

Quem compra sai dos envios seguintes. Sem booster no dia: o 20h30 faz
esse papel. SMS 5 minutos depois do e-mail, no máximo 2 por pessoa no dia.
