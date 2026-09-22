---
tipo: doutrina
autor: convertfy
fonte: "Estudo Base BFCM 2026, 9 lojas Omnisend, mai a set/2026"
status: aprovado
assunto: segmentacao-e-freios
---

Segmento pesa mais que o modelo. Na Donaris, engajados de 90 dias renderam R$ 92,5 por mil envios contra R$ 17,5 da lista toda. Na Brinque Mais, R$ 176,0 contra R$ 41,4. No pico da Brinque Mais, engajados fizeram 44 pedidos com 40 mil envios e a lista toda fez 24 com 99 mil.

# Camadas

| Camada | Definição |
|---|---|
| VIP | Tag de quem clicou em confirmar presença no convite do evento (ex.: VIP-1111) |
| E30 | Clicou nos últimos 30 dias ou comprou nos últimos 90 |
| E90 | Abriu ou clicou nos últimos 90 dias |
| E180 | Abriu ou clicou nos últimos 180 dias |
| LT | Inscritos, sem descadastrados, sem bounce e sem quem nunca abriu em 365 dias |
| NA_* | Recebeu o envio indicado e não abriu |
| CNC | Abriu ou clicou num envio do dia e não comprou |

# Nível da conta

| Nível | Critério | Lista toda no trimestre |
|---|---|---|
| A | Domínio com mais de 12 meses, spam histórico abaixo de 0,05%, lista estável | 2 |
| B | Domínio de 6 a 12 meses, ou spam entre 0,05% e 0,1% | 1 |
| C | Domínio com menos de 6 meses, base importada recente ou spam acima de 0,1% | 0 |
| LP | Lista abaixo de 3 mil contatos, qualquer nível | Só envios marcados lista_pequena=true |

# Freios

| Sinal | Ação |
|---|---|
| spam > 0,1% num envio | Próximo envio da conta desce um degrau de público |
| spam > 0,3% | Conta para de ampliar até o fim do plano. Só E90 |
| descadastro > 0,5% | Revisar assunto e frequência antes do próximo pico |
| bounce > 2% | Parar e limpar antes do próximo envio |
| queda no Postmaster | Pausar LT e reativação |
| aviso da Omnisend | Congelar volume e responder no mesmo dia |
| volume | Nenhum envio passa de 2x o tamanho do E90 da conta |

Métrica de decisão: clique, pedidos e receita por mil envios, e spam. Abertura é sinal auxiliar por causa do Apple Mail.

Ver [[sequencia-de-pico]] · [[mapa-do-calendario]]
