---
tipo: especificacao
autor: convertfy
fonte: "Padrão das contas Omnisend da Convertfy"
status: aprovado
assunto: nome-de-campanha
---

Toda campanha na Omnisend segue o padrão `[DD/MM] - [HH:MM] - [SEGMENTO] - [N - EVENTO] - [IDIOMA]`. Exemplo: `[11/11] - [18:00] - [E180] - [3 - 11.11] - [BRASIL]`.

O nome é a chave que liga cada campanha da Omnisend ao modelo e ao plano. É por ele que o índice é calculado. O admin lê o quarto campo (evento) e liga à nota do modelo pelos aliases de cada modelo em [[ranking-de-modelos]].

Erro já encontrado: campanha com 18:00 no nome agendada para 11h (Brinque Mais, 7.7). O nome e o horário precisam bater.
