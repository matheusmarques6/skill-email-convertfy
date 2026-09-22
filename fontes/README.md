# fontes/

Pacotes de origem que a suite cita. Diferente de `vendor/`, que e
referencia externa de terceiro: aqui e material da propria Convertfy.

| Pacote | O que e | Mapa |
|---|---|---|
| `BFCM-2026-Convertfy/` | Estrategia do Q4 2026, calendario, modelos validados, dados da carteira, design Blue Wolf | `docs/fontes/mapa-bfcm-2026.md` |

## O que entra no git

| Entra | Fica de fora |
|---|---|
| `.md` | `**/assets/` (180 imagens, 21 MB) |
| `.csv` | `*.pdf` (3 arquivos) |
| `.json` | `*.xlsx` (existe como `.csv` ao lado) |

O criterio e duplo: tamanho, e o binario ja existir em versao texto.
Quem clona sem os assets continua com toda a nota e todo o dado; perde
so a imagem de referencia.

As regras estao no `.gitignore` da raiz, em `fontes/**/`.

## Nivel na hierarquia

Os dados de desempenho daqui sao **nivel 2** do `CLAUDE.md`, atras so das
regras legais e eticas. Ganham do vault, do proprio CLAUDE.md e das
pesquisas publicadas.

Quando um dado daqui contradiz uma regra de nivel 4 a 7, a regra e
refinada com a condicao que o dado mostrou, e a mudanca fica registrada
em `docs/reconciliacao-regras-dados.md`.

## Regra de uso

Somente leitura, como o vault. Nada daqui e editado pela suite: o que a
suite produz vai para `skills/`, `shared/`, `docs/` ou `evals/`.

As skills citam o **resumo** em `docs/dados/`, nunca o CSV direto.
