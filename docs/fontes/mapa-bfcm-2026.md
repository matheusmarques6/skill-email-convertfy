# Mapa do pacote BFCM 2026

Extrato do Obsidian com a estrategia do Q4 2026, dados da carteira e
material validado. Em `fontes/BFCM-2026-Convertfy/`.

| | |
|---|---|
| Notas .md | 302 |
| Pastas | 15 |
| Versionado | `.md`, `.csv`, `.json` |
| Fora do git | `assets/`, `*.pdf`, `*.xlsx` (existem em versao texto ou CSV) |

## Pastas

| Pasta | .md | Outros | Tipos | O que tem | Para qual skill serve |
|---|---|---|---|---|---|
| `00_Indice` | 3 | 0 | 3.md | Mapa do pacote e indice geral | orientacao, nenhuma skill direta |
| `01_Estrategia` | 18 | 0 | 18.md | Estrategia do Q4, Campaign Booster, SMS e WhatsApp | email-calendario, auditoria-omnisend (booster e freios) |
| `02_Calendario_Q4` | 67 | 0 | 67.md | Calendario de out a dez com brief por envio | **email-calendario** (fonte principal) |
| `03_Referencias_validadas` | 66 | 0 | 66.md | Pecas validadas com dado | evals/referencias-reais, email-copy (tom e tamanho) |
| `04_Assuntos` | 18 | 0 | 18.md | 18 familias de assunto com dado de receita | **email-copy** references/familias-de-assunto.md |
| `05_Modelos_validados` | 37 | 0 | 37.md | 36 modelos de campanha com papel e ranking | **email-campanhas-sazonais** ou email-copy references |
| `06_Figma_copy_real` | 58 | 0 | 58.md | Copy real aprovada (Blue Wolf e master Brasil) | **evals/referencias-reais/** com lint |
| `07_Design_Blue_Wolf` | 15 | 8 | 15.md, 8.txt | Design system, paletas por momento, checklist | **marcas/blue-wolf.md** e email-qa |
| `08_Skill` | 1 | 0 | 1.md | SKILL de base de conhecimento BFCM | shared/ (principios) e roteador |
| `09_Dados` | 1 | 10 | 6.csv, 3.json, 1.xlsx, 1.md | CSV, JSON e dicionario do estudo | **docs/dados/** (as skills citam o resumo, nao o CSV) |
| `10_Documentos` | 3 | 3 | 3.pdf, 3.md | Estudo Base, Playbook Q4, Briefs Q4 | docs/dados/ e email-calendario |
| `11_Pacote_admin_e_modelos_HTML` | 2 | 22 | 16.html, 3.py, 3.json, 2.md | Modelos HTML e pacote do admin | email-design (estrutura), assets/arsenal |
| `12_Codigo_fonte` | 0 | 15 | 12.py, 1.html, 1.css, 1.json | Scripts py de analise | referencia, nao integra |
| `99_Versoes_anteriores` | 13 | 0 | 13.md | Versoes antigas das notas | nenhuma, historico |
| `assets` | 0 | 180 | 180.jpg | 180 imagens jpg | **gitignored**, nao versionado |

## Leitura obrigatoria feita

| Arquivo | O que trouxe |
|---|---|
| `08_Skill/SKILL - Base de conhecimento BFCM Convertfy.md` | Os 5 principios, 24 campanhas validadas com dado, o que nao funcionou, receita de antecipacao e de pico, familias de assunto, segmentacao e freios, design e copy |
| `00_Indice/00 BFCM 2026 - Mapa.md` | Indice do pacote |
| `05_Modelos_validados/principio-80-10-10.md` | 80% validado, ate 10% inspiracao, resto complemento. Plano Q4 fecha em 93/0/7 |
| `05_Modelos_validados/ranking-de-modelos.md` | Ranking por indice nas duas amostras (46 e 9 lojas), com situacao (titular, ressalva, reserva, fora) |
| `05_Modelos_validados/segmentacao-e-freios.md` | Camadas VIP/E30/E90/E180/LT, nivel de conta A/B/C/LP, tabela de freios |
| `05_Modelos_validados/regras-de-copy-de-campanha.md` | 10 regras duras e checklist de 14 itens antes de agendar |
| `09_Dados/Base de dados do estudo (dicionario e metodo).md` | Definicao de indice, por mil, papel e modelo. Fontes OA-EM, OA-BW, OA-CR, FG-BW, FG-BF, TT, WP |
| `10_Documentos/Estudo Base BFCM 2026 (texto).md` | O estudo completo |
| `10_Documentos/Playbook Q4 2026 (texto).md` | O playbook |
| `04_Assuntos/` (18 notas) | Uma familia por nota, com dado |
| `07_Design_Blue_Wolf/` (23 arquivos) | Design system, paletas por momento, checklist de aprovacao, 8 lotes |

## Duplicacao com o vault-repo

Verificado por comparacao de nome e de conteudo. Resultado em
`docs/fontes/duplicacao-bfcm-vault.md`.

## Regra de versionamento

`.md`, `.csv` e `.json` entram no git porque sao a fonte que as skills
citam. Ficam de fora, por tamanho e por existirem em versao texto:

```
fontes/**/assets/     180 imagens, 21 MB
fontes/**/*.pdf       3 arquivos
fontes/**/*.xlsx      1 arquivo (existe como .csv ao lado)
```

Quem clonar o repo sem o pacote continua com as notas e os dados. Perde
so a imagem de referencia.
