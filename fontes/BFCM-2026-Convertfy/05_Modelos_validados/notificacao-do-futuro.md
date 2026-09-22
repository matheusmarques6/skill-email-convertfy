---
tipo: modelo-de-email
autor: convertfy
fonte: "Estudo Base BFCM 2026, 9 lojas Omnisend, mai a set/2026; omnisend_campaign_metrics do admin, 46 lojas, 15/06 a 20/09/2026"
status: aprovado
assunto: notificacao-do-futuro
---

Notificação do futuro (pedido pendente). Estrutura C, papel hard fora. Situação na biblioteca: **Titular**.

# O dado

| Amostra | Mediana do índice | Lojas acima da média | Pedidos | Observação |
|---|---|---|---|---|
| 9 lojas (análise a fundo) | 1,43 | 6 de 9 | 105 |  |
| 46 lojas (carteira) | 1,67 | 24 de 39 | 252 | O melhor e-mail fora de pico da carteira |

Índice 1 é a média da própria loja. A mediana é o valor do meio entre as lojas que receberam o e-mail.

# Assunto testado

- Português: [Nome], falta você confirmar esse pedido...
- Inglês: [Nome], you still need to confirm your order...

# Como produzir

- **Copiar:** Caixa de aviso em fundo branco, "notificação que veio do futuro", resumo do pedido com o cupom e botão confirmar
- **Melhorar:** Oferta diferente da janela seguinte
- **Referência:** Blue Wolf 28/08 (agosto)
- **HTML:** modelo `C-notificacao.html` do pacote, ou o específico do modelo.
- **Nome na Omnisend:** o evento aparece como `3 - NOTIFICAÇÃO DO FUTURO`, `NOTIFICAÇÃO DO FUTURO`.

# Onde entra no Q4 2026

| Data | Hora | Papel no dia |
|---|---|---|
| 01/10 | 10:00 | Abre o mês com o e-mail de maior índice fora de pico |
| 16/11 | 10:00 | Notificação com brinde ou frete grátis, sem gastar a oferta da BF |
| 28/11 | 10:00 | Notificação com a oferta da BF |
| 15/12 | 10:00 | Prazo 1: pedido para chegar antes do Natal |
| 22/12 | 10:00 | O presente que chega em 1 minuto (vale-presente) |
| 30/12 | 10:00 | Notificação de 2027: o crédito que você esqueceu |

Voltar para [[mapa-do-calendario]] · [[ranking-de-modelos]]
