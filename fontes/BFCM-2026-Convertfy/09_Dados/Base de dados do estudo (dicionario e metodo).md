# Base de dados do estudo BFCM 2026

Esta aba guarda os dados brutos consultados no estudo: cada campanha, cada automação e cada agregado mensal das lojas analisadas, com a fonte, o método de cálculo e os limites de cada número. A aba principal interpreta; esta aba permite conferir e recalcular. Atualizada em 20/09/2026, com 101 envios de campanha e 18 fluxos de automação.

## B.1 Fontes consultadas

| Sigla | Fonte | O que forneceu | Acesso | Coleta |
| --- | --- | --- | --- | --- |
| OA-EM | Omnisend, conta Emyerre (emyerre.com) | 25 campanhas, 9 automações, pop-up, segmentos | Conector "Omnisend MCP" | 18/09/2026 |
| OA-BW | Omnisend, conta Blue Wolf (wolfbluestore.com) | 46 campanhas com assunto, pré-cabeçalho, conteúdo e resultado; 13 automações | Conector "Omnisend" | 18/09/2026 |
| OA-CR | Omnisend, conta Clube Rock (cluberock.com.br) | 55 campanhas com assunto, remetente, segmento e resultado; 9 automações | Conector "Omnisend" | 19/09/2026 |
| FG-BW | Figma, arquivos "CAMPANHAS - JULHO", "AGOSTO" e "SETEMBRO", linha da Blue Wolf | 36 e-mails em imagem, altura em pixels, estrutura de cada bloco | Conector Figma e prints enviadas | 18/09/2026 |
| FG-BF | Figma "BFCM Templates" e boards "PLANEJAMENTO" e "Emails Black Friday" | 177 wireframes do Max, planejamento do 11.11 de 2025, 21 e-mails de novembro de 2025 | Conector Figma e prints | 18/09/2026 |
| TT | Trendtrack | Calendários e criativos de marcas de referência | Conector Trendtrack | 18/09/2026 |
| WP | Wellcopy, "2026 Q4 Ecommerce Profit Playbook" | Números de demanda, custo de mídia e canais próprios (Shopify, NRF, Adobe, Klaviyo) | Material enviado | Antes de 18/09/2026 |
| C1 e C2 | Calls do Max no Skool (17/09 e 09/07/2026) | Prática de operador sobre ofertas, SMS e calendário | Transcrição | Antes de 18/09/2026 |

## B.2 Dicionário de campos e método

| Campo | Definição | Origem |
| --- | --- | --- |
| Envios | Mensagens enviadas pela campanha | Relatório da Omnisend, métrica "sent" |
| Abertura | Aberturas únicas ÷ envios | "openedUnique". Inflada pela proteção de privacidade da Apple. Usar como auxiliar |
| Clique | Cliques únicos ÷ envios | "clickedUnique" |
| Pedidos e receita | Pedidos e receita atribuídos pela Omnisend à campanha | "attributedOrders" e "attributedRevenue". A Omnisend atribui por clique e também por abertura, dentro da janela configurada na conta (ver B.9) |
| Por mil | Receita ÷ envios × 1.000, na moeda da loja | Calculado |
| Índice | Receita por mil da campanha ÷ receita por mil média da loja no trimestre | Calculado. Permite comparar lojas de tamanho e moeda diferentes. Índice 2 = o dobro da média daquela loja |
| Descad. | Descadastros únicos causados pelo envio | "unsubscribedUnique" |
| Spam | Reclamações de spam únicas | "markedAsSpamUnique" |
| Papel | Função do e-mail na sequência: antecipação, véspera, pico 7h, 11h ou 18h, ressaca, extensão, temática, gamificada, notificação, prova social, catálogo, lançamento, recorrente, semana 15% | Classificação manual pelo nome interno, assunto e design |
| Modelo | Texto puro ou imagem. Nos de imagem, a estrutura: A oferta na primeira tela, B convite com agenda, C aviso de sistema, outra | Classificação manual a partir do Figma e do conteúdo lido pela API (seção 21) |

Período: 17/06 a 17/09/2026 nas três contas. Ficaram fora da base: envios de teste com menos de 1.000 contatos, a reativação de 17/08 da Blue Wolf (analisada à parte na seção 18.3) e envios ainda em andamento na data da coleta (19/09 nas duas lojas).

## B.3 Blue Wolf: as 46 campanhas

Valores em dólar. Média da loja no trimestre: US$ 43,58 por mil envios. Assuntos e pré-cabeçalhos completos na seção 18.3 do estudo. Envios acima de 21 mil foram para o segmento ampliado.

| Data | Campanha | Papel | Modelo | Envios | Abertura | Clique | Pedidos | Receita US$ | Por mil | Índice | Descad. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17/06 | Semana Copa 2 | temática | imagem outra | 13.599 | 37,6% | 3,07% | 12 | 896,49 | 65,9 | 1,51 | 88 | 2 |
| 19/06 | Álbum de figurinha | gamificada | imagem outra | 13.681 | 36,4% | 1,60% | 6 | 513,06 | 37,5 | 0,86 | 43 | 3 |
| 26/06 | Social proof | prova social | imagem outra | 13.790 | 29,1% | 1,04% | 5 | 343,90 | 24,9 | 0,57 | 48 | 4 |
| 01/07 | Antecipação 7.7, 1, convite | antecipação | imagem B | 13.961 | 41,0% | 2,46% | 8 | 653,83 | 46,8 | 1,07 | 97 | 6 |
| 03/07 | Antecipação 7.7, 2, agenda | antecipação | imagem B | 13.937 | 44,3% | 1,90% | 14 | 1.171,42 | 84,1 | 1,93 | 97 | 7 |
| 06/07 | Antecipação 7.7, 3, acesso pendente | véspera | texto | 13.760 | 39,2% | 1,56% | 7 | 874,32 | 63,5 | 1,46 | 115 | 3 |
| 07/07 07h | 7.7, 1, cupom aprovado | pico 7h | texto | 13.698 | 40,2% | 1,47% | 6 | 336,88 | 24,6 | 0,56 | 91 | 3 |
| 07/07 11h | 7.7, 2, role até o fim | pico 11h | imagem outra | 13.679 | 33,1% | 1,27% | 12 | 737,68 | 53,9 | 1,24 | 70 | 3 |
| 07/07 18h | 7.7, 3, final call | pico 18h | imagem A | 13.629 | 38,8% | 3,06% | 14 | 1.435,34 | 105,3 | 2,42 | 94 | 1 |
| 15/07 | Favoritos do 7.7 | ressaca | imagem outra | 15.714 | 36,7% | 3,19% | 14 | 1.120,67 | 71,3 | 1,64 | 94 | 5 |
| 18/07 | Final da Copa | temática | imagem outra | 15.542 | 34,8% | 2,30% | 13 | 862,76 | 55,5 | 1,27 | 72 | 6 |
| 20/07 | Revele seu desconto | gamificada | imagem A | 15.575 | 35,8% | 1,66% | 18 | 1.066,14 | 68,5 | 1,57 | 99 | 5 |
| 22/07 | Jornal | notificação | imagem A | 15.606 | 35,3% | 2,04% | 15 | 1.122,53 | 71,9 | 1,65 | 100 | 4 |
| 24/07 | Ligação | notificação | imagem A | 15.437 | 34,5% | 1,69% | 11 | 755,69 | 49,0 | 1,12 | 69 | 6 |
| 25/07 | Reabertura | ressaca | texto | 15.472 | 36,7% | 1,23% | 8 | 775,77 | 50,1 | 1,15 | 84 | 6 |
| 27/07 | Segunda da sorte | gamificada | imagem outra | 15.521 | 34,6% | 1,82% | 3 | 267,44 | 17,2 | 0,40 | 84 | 3 |
| 29/07 | UGC social proof | prova social | imagem outra | 15.531 | 26,6% | 0,91% | 7 | 522,07 | 33,6 | 0,77 | 45 | 4 |
| 31/07 | Sexta premiada | gamificada | imagem outra | 15.584 | 33,4% | 1,58% | 9 | 781,91 | 50,2 | 1,15 | 66 | 1 |
| 03/08 | Esquenta 8.8, 1, warm-up | antecipação | imagem outra | 15.680 | 34,0% | 1,22% | 1 | 72,85 | 4,6 | 0,11 | 65 | 4 |
| 05/08 | Esquenta 8.8, 2, bom motivo | antecipação | imagem outra | 15.591 | 34,1% | 0,99% | 6 | 477,95 | 30,7 | 0,70 | 52 | 2 |
| 07/08 | Esquenta 8.8, 3, é amanhã | véspera | imagem outra | 15.643 | 34,1% | 1,32% | 10 | 718,08 | 45,9 | 1,05 | 59 | 3 |
| 08/08 07h | 8.8, 1, "Fwd" lista | pico 7h | texto | 15.676 | 39,0% | 1,19% | 7 | 503,65 | 32,1 | 0,74 | 87 | 3 |
| 08/08 11h | 8.8, 2, primeiros 100 | pico 11h | imagem A | 15.644 | 33,9% | 1,31% | 8 | 571,52 | 36,5 | 0,84 | 64 | 3 |
| 08/08 18h | 8.8, 3, status mudou | pico 18h | imagem A | 15.561 | 42,2% | 2,09% | 18 | 1.673,53 | 107,5 | 2,47 | 129 | 4 |
| 11/08 | Ressaca 8.8 | ressaca | imagem outra | 15.572 | 38,7% | 1,23% | 8 | 628,85 | 40,4 | 0,93 | 80 | 1 |
| 14/08 | Sextou | recorrente | imagem outra | 15.577 | 34,6% | 1,41% | 6 | 543,51 | 34,9 | 0,80 | 56 | 3 |
| 17/08 | Segunda turbo | gamificada | imagem outra | 15.725 | 33,8% | 1,50% | 6 | 950,45 | 60,4 | 1,39 | 55 | 0 |
| 19/08 | UGC Dia da Fotografia | prova social | imagem outra | 16.361 | 32,3% | 1,01% | 5 | 408,20 | 24,9 | 0,57 | 62 | 1 |
| 21/08 | Catálogo indecisão | catálogo | imagem outra | 16.394 | 34,1% | 1,89% | 5 | 394,69 | 24,1 | 0,55 | 71 | 5 |
| 24/08 | Semana 15%, 1, On & Off | semana 15% | imagem outra | 16.516 | 37,8% | 2,89% | 8 | 778,98 | 47,2 | 1,08 | 67 | 3 |
| 26/08 | Semana 15%, 2, Escolha o caminho | semana 15% | imagem outra | 16.519 | 37,4% | 0,97% | 3 | 208,26 | 12,6 | 0,29 | 65 | 0 |
| 28/08 | Semana 15%, 3, Notificação do futuro | notificação | imagem C | 16.577 | 37,0% | 3,61% | 9 | 648,22 | 39,1 | 0,90 | 85 | 2 |
| 31/08 | Catálogo fecha mês | catálogo | imagem outra | 16.620 | 36,2% | 2,91% | 8 | 815,25 | 49,1 | 1,13 | 77 | 0 |
| 03/09 | Esquenta 9.9, 1, "Fwd" | antecipação | texto | 21.733 | 29,3% | 0,83% | 4 | 482,21 | 22,2 | 0,51 | 84 | 6 |
| 05/09 | Esquenta 9.9, 2, prometi avisar | antecipação | imagem outra | 21.862 | 27,5% | 2,30% | 12 | 729,57 | 33,4 | 0,77 | 67 | 5 |
| 07/09 | Esquenta 9.9, 3, acesso garantido | antecipação | imagem outra | 22.042 | 26,0% | 2,21% | 3 | 287,37 | 13,0 | 0,30 | 68 | 2 |
| 08/09 | Esquenta 9.9, 4, agendado amanhã | véspera | imagem outra | 22.093 | 28,8% | 2,42% | 5 | 427,19 | 19,3 | 0,44 | 66 | 5 |
| 09/09 07h | 9.9, 1, cupom liberado | pico 7h | texto | 16.810 | 35,3% | 1,15% | 13 | 1.215,92 | 72,3 | 1,66 | 47 | 0 |
| 09/09 11h | 9.9, 2, acesso concedido | pico 11h | imagem A | 16.790 | 34,9% | 2,70% | 7 | 512,06 | 30,5 | 0,70 | 52 | 4 |
| 09/09 18h | 9.9, 3, status mudou | pico 18h | imagem A | 16.743 | 41,8% | 3,56% | 15 | 1.028,01 | 61,4 | 1,41 | 84 | 1 |
| 11/09 | Ressaca 9.9 | ressaca | imagem C | 16.771 | 34,6% | 3,20% | 14 | 1.303,30 | 77,7 | 1,78 | 49 | 1 |
| 14/09 | Antecipação VIP Day | véspera | imagem C | 16.818 | 33,5% | 1,54% | 5 | 440,74 | 26,2 | 0,60 | 60 | 0 |
| 15/09 07h | VIP Day, 1, selecionado | pico 7h | texto | 16.780 | 33,2% | 1,27% | 5 | 541,95 | 32,3 | 0,74 | 56 | 0 |
| 15/09 11h | VIP Day, 2, aprovado? | pico 11h | imagem outra | 16.766 | 31,7% | 1,14% | 6 | 846,58 | 50,5 | 1,16 | 40 | 3 |
| 15/09 18h | VIP Day, 3, prêmio reservado | pico 18h | imagem outra | 16.699 | 31,3% | 1,37% | 4 | 324,04 | 19,4 | 0,45 | 38 | 3 |
| 17/09 | VIP Week, 1 | extensão | imagem A | 16.762 | 29,5% | 1,24% | 6 | 567,49 | 33,9 | 0,78 | 32 | 1 |
| **Total** | 46 campanhas |  |  | 742.041 | 34,6% | 1,84% | 389 | 32.338 | 43,6 | 1,00 | 3.273 | 137 |

## B.4 Clube Rock: as 55 campanhas

Valores em reais. Média da loja no trimestre: R$ 112,80 por mil envios. Envios acima de 52 mil foram para o segmento ampliado. "Henrique" indica e-mail de texto com remetente "Henrique da Clube Rock". \[Nome\] representa o primeiro nome do contato.

| Data | Campanha | Assunto | Papel | Envios | Abertura | Clique | Pedidos | Receita R$ | Por mil | Índice | Descad. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17/06 | Semana Copa 2 | 🟥 Cartão vermelho pra quem perder essas ofertas... | temática | 32.809 | 25,1% | 0,86% | 30 | 4.383,99 | 133,6 | 1,18 | 168 | 4 |
| 19/06 | Álbum de figurinha | ⚽ Faça o seu gol antes da Seleção | gamificada | 33.190 | 23,2% | 0,54% | 36 | 4.804,54 | 144,8 | 1,28 | 55 | 4 |
| 26/06 | Social proof | O que eles sabem que você ainda não? | prova social | 34.513 | 23,2% | 0,44% | 37 | 4.688,62 | 135,9 | 1,20 | 63 | 5 |
| 01/07 | Antecipação 7.7, convite | \[Nome\], chegou um convite pra você ✉️ | antecipação | 35.357 | 24,9% | 0,79% | 25 | 3.182,49 | 90,0 | 0,80 | 62 | 7 |
| 03/07 | Antecipação 7.7, agenda | \[Nome\], você já viu o que está vindo? 👀 | antecipação | 35.728 | 24,2% | 0,48% | 30 | 4.165,58 | 116,6 | 1,03 | 70 | 3 |
| 06/07 | Antecipação 7.7, acesso pendente | ⚠️ Seu acesso pra amanhã está pendente | véspera | 36.306 | 25,9% | 0,75% | 24 | 2.481,48 | 68,3 | 0,61 | 134 | 7 |
| 07/07 07h | 7.7, 1, cupom aprovado (Henrique) | Seu cupom foi aprovado ✅ | pico 7h | 36.496 | 34,5% | 2,07% | 89 | 14.510,69 | 397,6 | 3,52 | 118 | 8 |
| 07/07 11h | 7.7, 2, vá até o final | Vá até o final deste e-mail (tem surpresa) | pico 11h | 36.437 | 23,7% | 0,89% | 31 | 4.812,08 | 132,1 | 1,17 | 118 | 6 |
| 07/07 18h | 7.7, 3, última chamada | 🚨 \[ÚLTIMA CHAMADA\] Expira às 23h59 | pico 18h | 36.450 | 23,2% | 0,87% | 23 | 3.696,69 | 101,4 | 0,90 | 130 | 4 |
| 08/07 | Pós 7.7, obrigado (Henrique) | Obrigado... mas calma que ainda tem mais! 🤘 | ressaca | 36.557 | 28,5% | 0,00% | 31 | 4.589,21 | 125,5 | 1,11 | 197 | 7 |
| 10/07 | Antecipação Dia do Rock | Vem aí: 13.07, Dia Mundial do Rock 🤘 | antecipação | 53.979 | 16,4% | 0,41% | 33 | 4.489,78 | 83,2 | 0,74 | 131 | 4 |
| 13/07 07h | Dia do Rock, 1, 3 por R$ 169 (Henrique) | 3 camisetas por R$169 + FRETE GRÁTIS 🤘 | pico 7h | 37.609 | 25,8% | 0,96% | 49 | 8.272,40 | 220,0 | 1,95 | 195 | 8 |
| 13/07 11h | Dia do Rock, 2, R$ 56 a camiseta | R$56 a camiseta? Só HOJE no Dia do Rock 🤘 | pico 11h | 37.530 | 23,4% | 1,41% | 50 | 7.706,87 | 205,4 | 1,82 | 151 | 6 |
| 13/07 18h | Dia do Rock, 3, some à meia-noite | 🚨 \[Nome\], isso some à meia-noite (é sério) | pico 18h | 37.590 | 23,3% | 1,10% | 29 | 5.322,69 | 141,6 | 1,26 | 168 | 6 |
| 15/07 | Favoritos do Dia do Rock | \[Nome\], os favoritos do Dia Do Rock estão te esperando 👀 | ressaca | 37.195 | 24,9% | 1,25% | 30 | 3.750,71 | 100,8 | 0,89 | 174 | 4 |
| 18/07 | Final da Copa | \[Nome\], separei algo só pra clientes especiais 🏆 | temática | 37.545 | 25,4% | 1,46% | 22 | 2.536,88 | 67,6 | 0,60 | 176 | 6 |
| 20/07 | Revele seu desconto | (1) desconto escondido para \[nome\] neste e-mail 🤫 | gamificada | 37.818 | 24,9% | 1,48% | 39 | 5.194,80 | 137,4 | 1,22 | 176 | 9 |
| 22/07 | Jornal | \[Nome\], chegou a notícia que você não queria... | notificação | 38.356 | 25,8% | 1,31% | 48 | 7.633,32 | 199,0 | 1,76 | 186 | 3 |
| 24/07 | Ligação | \[Nome\], você recebeu uma ligação 📞 | notificação | 38.354 | 25,1% | 1,15% | 24 | 3.473,36 | 90,6 | 0,80 | 174 | 8 |
| 25/07 | Reabertura (Henrique) | Eu decidi reabrir tudo por mais um dia | ressaca | 41.069 | 26,8% | 0,63% | 33 | 4.325,29 | 105,3 | 0,93 | 277 | 6 |
| 27/07 | Segunda da sorte | Cuidado: esse e-mail contém sorte 🍀 | gamificada | 41.322 | 24,4% | 1,00% | 35 | 3.807,59 | 92,1 | 0,82 | 250 | 14 |
| 29/07 | UGC Dia dos Pais | O presente que todo pai queria ganhar | prova social | 41.659 | 23,2% | 0,38% | 39 | 7.520,85 | 180,5 | 1,60 | 245 | 8 |
| 31/07 | Sexta premiada | Você foi premiado hoje 🎁 | gamificada | 42.197 | 25,1% | 1,52% | 51 | 6.746,47 | 159,9 | 1,42 | 227 | 9 |
| 03/08 | Esquenta 8.8, 1 | Começou o Esquenta 8.8 🔥 | antecipação | 43.017 | 23,4% | 0,89% | 31 | 4.556,18 | 105,9 | 0,94 | 230 | 9 |
| 05/08 | Esquenta 8.8, 2 | Tem um bom motivo pra você abrir esse e-mail 👀 | antecipação | 42.993 | 24,1% | 0,87% | 32 | 5.406,06 | 125,7 | 1,11 | 193 | 11 |
| 07/08 | Esquenta 8.8, véspera | Amanhã é o 8.8. Você tá pronto? | véspera | 43.547 | 23,7% | 1,01% | 25 | 4.523,14 | 103,9 | 0,92 | 61 | 15 |
| 08/08 07h | 8.8, 1, "Enc" lista | Enc: consegui colocar seu nome nessa lista | pico 7h | 43.799 | 25,6% | 0,30% | 32 | 4.946,78 | 112,9 | 1,00 | 206 | 6 |
| 08/08 11h | 8.8, 2, 100 primeiros | Esse e-mail só vale pros 100 primeiros 🎁 | pico 11h | 43.857 | 22,6% | 0,86% | 35 | 6.806,99 | 155,2 | 1,38 | 198 | 7 |
| 08/08 18h | 8.8, 3, status mudou | 🚨 Seu status mudou agora | pico 18h | 43.713 | 36,5% | 1,24% | 95 | 12.070,19 | 276,1 | 2,45 | 229 | 10 |
| 11/08 | Ressaca 8.8 | Perdeu o 8.8? Ainda dá tempo... 👀 | ressaca | 44.346 | 22,9% | 0,90% | 24 | 2.932,66 | 66,1 | 0,59 | 174 | 8 |
| 14/08 | Coleção Ouro Nacional | Chegou a Coleção Ouro Nacional 🤘 | lançamento | 44.993 | 23,5% | 1,13% | 35 | 4.698,18 | 104,4 | 0,93 | 156 | 10 |
| 17/08 | Segunda turbo | Você está entre os 100 primeiros? | gamificada | 45.862 | 23,9% | 1,23% | 38 | 4.789,46 | 104,4 | 0,93 | 133 | 12 |
| 19/08 | UGC Dia da Fotografia | Faltou a sua aqui... | prova social | 46.151 | 24,4% | 0,58% | 34 | 4.614,58 | 100,0 | 0,89 | 150 | 10 |
| 21/08 | Catálogo indecisão | Ou você escolhe hoje, ou continua adiando… | catálogo | 46.588 | 22,4% | 0,48% | 27 | 3.500,19 | 75,1 | 0,67 | 123 | 8 |
| 22/08 | Antecipação Oversized (Henrique) | Amanhã, 10h: Oversized Clube Rock | lançamento | 46.873 | 24,9% | 0,00% | 16 | 4.225,63 | 90,2 | 0,80 | 140 | 4 |
| 23/08 | Lançamento Oversized R$ 99 | Chegou a Oversized por R$ 99,00 🤘 | lançamento | 47.050 | 22,7% | 0,69% | 21 | 3.243,01 | 68,9 | 0,61 | 136 | 8 |
| 24/08 | Semana 15%, On & Off | Ativei um desconto pra você ✅ | semana 15% | 47.204 | 23,3% | 0,96% | 40 | 5.649,83 | 119,7 | 1,06 | 163 | 14 |
| 26/08 | Semana 15%, Escolha o caminho | \[Nome\], escolha o seu caminho... | semana 15% | 47.596 | 23,4% | 0,44% | 31 | 3.495,80 | 73,4 | 0,65 | 156 | 5 |
| 28/08 | Notificação do futuro | \[Nome\], falta você confirmar esse pedido... | notificação | 48.094 | 24,0% | 1,09% | 52 | 7.738,40 | 160,9 | 1,43 | 132 | 7 |
| 31/08 | Catálogo fecha mês | Ignore este e-mail depois das 23h59 | catálogo | 48.588 | 23,9% | 0,95% | 22 | 2.902,36 | 59,7 | 0,53 | 135 | 10 |
| 01/09 | Estampa da turnê SOAD | SOAD: estampa exclusiva da tour 🤘 | lançamento | 48.711 | 23,0% | 0,32% | 15 | 3.063,94 | 62,9 | 0,56 | 121 | 6 |
| 02/09 | Rock in Rio, kit 3 por R$ 189 | Rock in Rio chegando... e seu kit? 🎸 | temática | 47.789 | 22,8% | 0,42% | 28 | 4.578,73 | 95,8 | 0,85 | 115 | 4 |
| 03/09 | Esquenta 9.9, 1, "Enc" | Enc: você não deveria saber disso | antecipação | 79.447 | 15,6% | 0,29% | 32 | 4.432,09 | 55,8 | 0,49 | 208 | 8 |
| 05/09 | Esquenta 9.9, 2 | Prometi te avisar antes, \[nome\] 👀 | antecipação | 80.215 | 15,3% | 0,44% | 31 | 4.965,74 | 61,9 | 0,55 | 168 | 9 |
| 07/09 | 7 de Setembro | Quanto vale LIBERDADE? 🇧🇷 | temática | 81.238 | 14,5% | 0,30% | 30 | 3.598,15 | 44,3 | 0,39 | 149 | 4 |
| 08/09 | Esquenta 9.9, véspera | \[Nome\], você tem um compromisso pra amanhã 📅 | véspera | 81.757 | 13,9% | 0,32% | 20 | 2.658,42 | 32,5 | 0,29 | 141 | 13 |
| 09/09 07h | 9.9, 1, cupom liberado | Seu cupom foi liberado ✅ | pico 7h | 49.421 | 23,4% | 0,81% | 67 | 10.667,80 | 215,9 | 1,91 | 103 | 2 |
| 09/09 11h | 9.9, 2, acesso liberado | 🔓 Seu acesso foi liberado (só hoje) | pico 11h | 49.464 | 21,8% | 0,63% | 47 | 8.151,46 | 164,8 | 1,46 | 118 | 4 |
| 09/09 18h | 9.9, 3, status mudou | 🚨 Seu status acaba de mudar | pico 18h | 49.320 | 30,2% | 1,14% | 94 | 12.494,68 | 253,3 | 2,25 | 145 | 3 |
| 11/09 | Ressaca 9.9 | Lamentamos informar que... | ressaca | 49.681 | 24,8% | 0,88% | 34 | 3.404,66 | 68,5 | 0,61 | 155 | 5 |
| 14/09 | Antecipação Dia do Cliente | Confirmado: você está na lista pra amanhã ✅ | véspera | 50.052 | 22,8% | 0,52% | 15 | 2.573,12 | 51,4 | 0,46 | 119 | 4 |
| 15/09 07h | Dia do Cliente, 1, escolhido | \[Nome\], você foi escolhido | pico 7h | 50.167 | 24,9% | 0,75% | 40 | 5.389,07 | 107,4 | 0,95 | 104 | 4 |
| 15/09 11h | Dia do Cliente, 2, aprovado? | Será que você foi aprovado? | pico 11h | 49.925 | 21,6% | 0,46% | 19 | 2.246,97 | 45,0 | 0,40 | 92 | 3 |
| 15/09 18h | Dia do Cliente, 3, prêmio | Prêmio reservado para \[nome\] 🎁 | pico 18h | 49.867 | 21,9% | 0,52% | 34 | 5.516,89 | 110,6 | 0,98 | 144 | 2 |
| 17/09 | Semana do Cliente, 1 | O Dia do Cliente virou SEMANA 👀 | extensão | 50.253 | 19,7% | 0,34% | 16 | 2.083,99 | 41,5 | 0,37 | 78 | 2 |
| **Total** | 55 campanhas |  |  | 2.517.644 | 23,0% | 0,75% | 1.950 | 284.022 | 112,8 | 1,00 | 8.320 | 373 |

## B.5 Automações

**Blue Wolf, 17/06 a 18/09/2026, em dólar**

| Fluxo | Envios | Abertura | Clique | Pedidos | Receita | Por mil |
| --- | --- | --- | --- | --- | --- | --- |
| Welcome Series | 94.856 | 27,4% | 2,86% | 415 | 37.711 | 398 |
| Checkout abandonado | 40.838 | 29,6% | 4,57% | 317 | 30.315 | 742 |
| Rastreio de envio | 26.010 | 65,3% | 27,1% | 89 | 10.414 | 400 |
| Carrinho abandonado | 27.922 | 30,2% | 4,05% | 101 | 9.103 | 326 |
| Produto visto | 54.131 | 31,9% | 3,33% | 100 | 8.914 | 165 |
| Upsell | 17.366 | 50,2% | 6,35% | 76 | 6.322 | 364 |
| Em trânsito | 4.188 | 71,3% | 43,1% | 29 | 2.471 | 590 |
| Pedido entregue | 4.449 | 58,4% | 10,8% | 22 | 2.045 | 460 |
| Site abandonado | 3.647 | 39,1% | 4,85% | 15 | 1.110 | 304 |
| Em rota de entrega | 4.106 | 56,6% | 20,9% | 8 | 651 | 158 |
| Winback | 6.684 | 36,4% | 2,77% | 10 | 592 | 89 |
| Retirada e tentativa falhada | 279 | 71,7% | 44,1% | 1 | 152 |  |
| **Total** | 284.476 |  |  | 1.183 | 109.800 | 386 |

**Clube Rock, 17/06 a 19/09/2026, em reais**

| Fluxo | Envios | Abertura | Clique | Pedidos | Receita | Por mil |
| --- | --- | --- | --- | --- | --- | --- |
| Welcome Flow | 275.681 | 12,7% | 1,38% | 2.751 | 368.304 | 1.336 |
| Carrinho abandonado | 116.606 | 18,1% | 2,74% | 1.107 | 176.632 | 1.515 |
| Checkout abandonado | 142.574 | 16,0% | 0,71% | 1.002 | 148.715 | 1.043 |
| Produto visto | 108.273 | 13,5% | 1,07% | 262 | 33.784 | 312 |
| Rastreio criado | 56.779 | 50,2% | 23,2% | 175 | 24.273 | 427 |
| Pedido confirmado e separação | 81.991 | 51,7% | 4,04% | 137 | 17.807 | 217 |
| Upsell | 107.217 | 25,7% | 1,68% | 117 | 14.474 | 135 |
| Site abandonado | 11.727 | 17,9% | 1,84% | 62 | 9.332 | 796 |
| Winback | 53.860 | 14,0% | 0,68% | 54 | 7.158 | 133 |
| **Total** | 954.708 |  |  | 5.667 | 800.479 | 838 |

Leitura das duas tabelas. Na Clube Rock, a abertura do Welcome (12,7%) e do checkout abandonado (16,0%) é menos da metade da Blue Wolf (27,4% e 29,6%), e mesmo assim são os fluxos que mais faturam. Vale abrir mensagem por mensagem nos dois fluxos para ver onde a abertura cai, porque é o maior potencial de receita da conta. Na Blue Wolf, os quatro fluxos de logística somam US$ 15.580 (14% das automações); na Clube Rock, rastreio e pedido confirmado somam R$ 42.080 (5%).

**Emyerre, 20/07 a 18/09/2026, em dólar:** automações somam US$ 5.103 (78% da receita de e-mail). Welcome, e-mail 1: US$ 1.827, 86% da receita do fluxo. Checkout abandonado, e-mail 1: US$ 1.281. Zero pedido nos e-mails 6 a 8 do welcome, 4 a 8 do checkout e nos 5 do produto visto. Detalhe na seção 17.6.

## B.6 Agregados por mês

| Loja | Mês | Campanhas | Envios | Abertura | Clique | Pedidos | Receita | Por mil | Índice | Descadastro por envio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Blue Wolf | Junho, desde 17/06 | 3 | 41.070 | 34,3% | 1,90% | 23 | US$ 1.753 | 42,7 | 0,98 | 0,44% |
| Blue Wolf | Julho | 15 | 222.646 | 36,2% | 1,87% | 159 | US$ 12.484 | 56,1 | 1,29 | 0,57% |
| Blue Wolf | Agosto | 15 | 239.656 | 36,0% | 1,71% | 108 | US$ 9.394 | 39,2 | 0,90 | 0,45% |
| Blue Wolf | Setembro, até 17/09 | 13 | 238.669 | 31,7% | 1,92% | 99 | US$ 8.706 | 36,5 | 0,84 | 0,31% |
| Clube Rock | Junho, desde 17/06 | 3 | 100.512 | 23,8% | 0,61% | 103 | R$ 13.877 | 138,1 | 1,22 | 0,28% |
| Clube Rock | Julho | 20 | 775.554 | 24,8% | 0,98% | 735 | R$ 108.219 | 139,5 | 1,24 | 0,43% |
| Clube Rock | Agosto | 17 | 774.271 | 24,4% | 0,80% | 590 | R$ 86.099 | 111,2 | 0,99 | 0,35% |
| Clube Rock | Setembro, até 17/09 | 15 | 867.307 | 20,2% | 0,51% | 522 | R$ 75.826 | 87,4 | 0,77 | 0,23% |
| Emyerre | 20/07 a 18/09 | 25 | lista de 1.096 contatos | 34% | 2,66% |  | US$ 1.479 |  |  |  |

## B.7 Agregados por papel na sequência

| Papel | Blue Wolf: campanhas | Blue Wolf: índice | Clube Rock: campanhas | Clube Rock: índice |
| --- | --- | --- | --- | --- |
| Pico 18h | 4 | 1,63 | 5 | 1,60 |
| Pico 7h | 4 | 0,95 | 5 | 1,78 |
| Pico 11h | 4 | 0,97 | 5 | 1,21 |
| Ressaca e reabertura | 4 | 1,38 | 5 | 0,81 |
| Notificação | 3 | 1,22 | 3 | 1,34 |
| Temática | 2 | 1,39 | 4 | 0,67 |
| Gamificada | 5 | 1,08 | 5 | 1,12 |
| Antecipação | 7 | 0,71 | 7 | 0,75 |
| Véspera | 4 | 0,83 | 4 | 0,51 |
| Catálogo | 2 | 0,84 | 2 | 0,60 |
| Prova social | 3 | 0,64 | 3 | 1,22 |
| Semana 15% | 2 | 0,69 | 2 | 0,86 |
| Extensão | 1 | 0,78 | 1 | 0,37 |
| Lançamento | 0 |  | 4 | 0,72 |

## B.8 Arquivo da base

A base completa está guardada dentro deste documento como arquivo CSV (base\_campanhas\_convertfy\_padrao.csv, separador vírgula, ponto como decimal, UTF-8, 101 linhas). O gráfico abaixo lê o arquivo diretamente: cada ponto é um envio. Quando uma loja nova entra, o CSV é substituído por uma versão com as novas linhas e o gráfico passa a mostrá-las.

Colunas, na ordem do arquivo: loja, mercado, idioma, moeda, mês, data do envio, campanha, papel, segmento ampliado, modelo, estrutura, altura em px, desconto, envios, aberturas, cliques, pedidos, receita (na moeda da loja), descadastros, spam, abertura %, clique %, clique em pedido %, receita por mil envios, índice e descadastro %.

[base_campanhas_convertfy_padrao.csv · 101 envios, Blue Wolf e Clube Rock, 17/06 a 17/09/2026](node/68a10fe9-6dfe)

Como ler: os pontos no alto à direita são os e-mails de assunto de status às 18h e o texto do fundador às 7h. A nuvem de pontos da Clube Rock abaixo de 17% de abertura são os envios para o segmento ampliado, todos com índice entre 0,29 e 0,74. Abrir mais não garante vender: há campanhas com 37% de abertura e índice 0,3.

## B.9 Limites dos dados

1. **Atribuição.** A Omnisend atribui pedido por clique e também por abertura. Na Clube Rock, dois e-mails sem link (08/07 e 22/08) têm zero clique e 31 e 16 pedidos. A receita atribuída a campanhas inclui compras que aconteceriam sem o e-mail. O índice compara bem campanhas da mesma loja. Não serve para dizer quanto o e-mail gerou de receita nova.
2. **Abertura.** Inflada pela proteção de privacidade da Apple e por filtros de segurança corporativos. É a métrica menos confiável da base.
3. **Janela de 3 meses.** Julho tem as datas mais fortes do período. O índice por mês não separa sazonalidade de fadiga.
4. **Uma execução por modelo e loja.** Cada modelo rodou uma vez em cada loja, sem grupo de controle. O cruzamento entre lojas (seção 25.1) é o que dá robustez.
5. **Emyerre.** Lista de 1.096 contatos, pequena demais para o índice por campanha. Entra só nos achados agregados.
6. **Receita total das lojas não coletada.** A participação do e-mail no faturamento só existe para a Emyerre (14,2%).
7. **Novembro de 2025 ausente.** As três contas foram criadas em 2026.
8. **Classificação manual.** Papel e estrutura foram atribuídos por leitura do nome, do assunto e do design. A estrutura só foi classificada na Blue Wolf, onde há imagens.
