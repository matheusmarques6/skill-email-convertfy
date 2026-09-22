---
tipo: especificacao
autor: convertfy
fonte: "Estudo Base BFCM 2026, 9 lojas Omnisend, mai a set/2026; omnisend_campaign_metrics do admin, 46 lojas, 15/06 a 20/09/2026"
status: aprovado
assunto: sequencia-de-pico
---

O molde de toda data dupla (6.6, 7.7, 10.10, 11.11) e de todo pico de temporada. É a parte mais validada da operação: o 18h com status mudou ficou acima da média em 8 de 9 lojas no 9.9 e em 25 de 33 no 8.8.

| Dia | Hora | E-mail | Público | Condição |
|---|---|---|---|---|
| D-6 | 10:00 | [[convite]] | E90 |  |
| D-3 | 10:00 | [[agenda]] | VIP+E30 |  |
| D-1 | 18:00 | amanhã às 7h | - |  |
| D+0 | 00:00 | [[acesso-liberado-00h]] | VIP | se T1 aprovado |
| D+0 | 07:00 | [[cupom-liberado-7h]] | E90 |  |
| D+0 | 11:00 | [[reenvio-11h]] | NA_07H |  |
| D+0 | 18:00 | [[status-mudou-18h]] | {"A": "E180", "B": "E180", "C": "E90"} |  |
| D+0 | 21:30 | [[ultima-chamada-2130]] | CNC |  |
| D+2 | 10:00 | [[ressaca]] | {"A": "E90", "B": "E90", "C": "E30"} | só com estoque real |

Esquenta de 3 ou 4 e-mails e véspera por e-mail estão fora: ficaram abaixo da média nas duas amostras.

Ver [[segmentacao-e-freios]] · [[mapa-do-calendario]]
