---
tipo: modelo-de-email
autor: convertfy
fonte: "Estudo Base BFCM 2026, 9 lojas Omnisend, mai a set/2026; omnisend_campaign_metrics do admin, 46 lojas, 15/06 a 20/09/2026"
status: aprovado
assunto: cupom-liberado-7h
---

Cupom liberado (7h do pico). Estrutura D, papel hard pico. Situação na biblioteca: **Titular com ressalva**.

# O dado

| Amostra | Mediana do índice | Lojas acima da média | Pedidos | Observação |
|---|---|---|---|---|
| 9 lojas (análise a fundo) | 1,66 | 6 de 9 | 110 |  |
| 46 lojas (carteira) | 0,95 | 20 de 40 | 242 | 7.7: 0,86. 8.8: 0,89 (com Enc: no assunto) |

Índice 1 é a média da própria loja. A mediana é o valor do meio entre as lojas que receberam o e-mail.

# Assunto testado

- Português: Seu cupom foi liberado ✅
- Inglês: Your coupon has been released ✅

# Como produzir

- **Copiar:** Texto curto, cupom em negrito, um link
- **Melhorar:** Usar a versão do 9.9 (cupom liberado: 1,66 nas 9 lojas). A do 7.7 (cupom aprovado) ficou 0,70 sem pessoa no remetente. Sem Enc: ou Fwd: no assunto
- **Referência:** Clube Rock 7.7 07h (remetente Henrique). Blue Wolf 09/09 07h
- **HTML:** modelo `D-texto.html` do pacote, ou o específico do modelo.
- **Nome na Omnisend:** o evento aparece como `1 - 7.7`, `1 - 8.8`, `1 - 9.9`.

# Onde entra no Q4 2026

| Data | Hora | Papel no dia |
|---|---|---|
| 10/10 | 07:00 | Cupom liberado, texto com pessoa |
| 11/11 | 07:00 | Cupom liberado |
| 25/11 | 07:00 | A oferta do ano começou |
| 27/11 | 07:00 | Hoje é o dia |
| 29/11 | 10:00 | A Black termina hoje, texto |
| 30/11 | 07:00 | Cyber Monday com oferta nova |
| 20/12 | 10:00 | Segunda parcela do 13º, texto com pessoa |
| 23/12 | 10:00 | Vale-presente de última hora, texto com pessoa |
| 26/12 | 07:00 | Boxing Day |

Voltar para [[mapa-do-calendario]] · [[ranking-de-modelos]]
