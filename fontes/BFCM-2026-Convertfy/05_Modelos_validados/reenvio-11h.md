---
tipo: modelo-de-email
autor: convertfy
fonte: "Estudo Base BFCM 2026, 9 lojas Omnisend, mai a set/2026; omnisend_campaign_metrics do admin, 46 lojas, 15/06 a 20/09/2026"
status: aprovado
assunto: reenvio-11h
---

Reenvio das 11h (resgate pendente). Estrutura A, papel hard pico. Situação na biblioteca: **Titular com ressalva**.

# O dado

| Amostra | Mediana do índice | Lojas acima da média | Pedidos | Observação |
|---|---|---|---|---|
| 9 lojas (análise a fundo) | 1,24 | 5 de 9 | 80 |  |
| 46 lojas (carteira) | 0,67 | 15 de 40 | 160 | Foi para a lista toda. No calendário vai só para quem não abriu o 07h |

Índice 1 é a média da própria loja. A mediana é o valor do meio entre as lojas que receberam o e-mail.

# Assunto testado

- Português: ⚠️ (1) resgate pendente para [nome]
- Inglês: ⚠️ (1) pending reward for [nome]

# Como produzir

- **Copiar:** Corpo do 07h
- **Melhorar:** Só não abridores do 07h
- **Referência:** Blue Wolf 09/09 11h (setembro)
- **HTML:** modelo `A-status-mudou.html` do pacote, ou o específico do modelo.
- **Nome na Omnisend:** o evento aparece como `2 - 7.7`, `2 - 8.8`, `2 - 9.9`.

# Onde entra no Q4 2026

| Data | Hora | Papel no dia |
|---|---|---|
| 10/10 | 11:00 | Reenvio para quem não abriu o 07h |
| 11/11 | 11:00 | Reenvio para não abridores |
| 26/11 | 19:00 | Reenvio do 18h de 25/11 para não abridores |
| 27/11 | 11:00 | Para quem não abriu o 07h |
| 30/11 | 11:00 | Reenvio |

Voltar para [[mapa-do-calendario]] · [[ranking-de-modelos]]
