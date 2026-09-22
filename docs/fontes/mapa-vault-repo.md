# Mapa do vault-repo (All-for-Eficiencia)

Clone em `./vault-repo`, profundidade 1, **somente leitura**. Esta no
`.gitignore`: nunca recebe commit nem push daqui.

O symlink `./vault` aponta para `vault-repo/Admin Convertfy/Emails`.

| | |
|---|---|
| Commit clonado | `fc28a08` |
| Notas .md no total | 528 |
| Ignorados | `.obsidian/`, `.tools/`, `Sem titulo*`, `.canvas`, `.base` |

## Arvore e relevancia

| Pasta | Notas | Tipo de conhecimento | Relevancia | Observacao |
|---|---|---|---|---|
| `Admin Convertfy/Emails` | 279 | estrutura de e-mail, copy | **alta** | Ja e a fonte da suite. 279 notas: protocolo, 75 variantes, intencoes, estruturas, aprendizados |
| `Admin Convertfy/Conhecimento/Advisors` | 212 | copy, doutrina externa | **media** | 212 notas, todas do Max. Doutrina de copy e assunto. A ponte subject-line-e-preview ja e usada. O resto nao foi lido pela suite |
| `Admin Convertfy/Conhecimento/Referencias` | 11 | referencia de e-mail | **alta** | 11 notas, subpasta email/. Candidato direto a evals/referencias-reais |
| `Admin Convertfy/Conhecimento/Convertfy` | 7 | cliente, processo | **media** | 7 notas: mapa da agencia, estruturas, cliente ride-nation. Afeta e-mail so no contexto de conta |
| `Admin Convertfy/Conhecimento/Padrao Convertfy` | 6 | processo | **media** | 6 notas: modelos de nota (anti-exemplo, referencia, decisao-com-numero, pesquisa) e como escrever. E padrao de ESCRITA DE NOTA, nao regra de e-mail |
| `Admin Convertfy/Conhecimento/Pesquisas` | 1 | dados | **baixa** | 1 nota, so o mapa. A pesquisa real esta no pacote BFCM |
| `Admin Convertfy/Conhecimento/_inbox` | 1 | outro | **nenhuma** | 1 nota, so o leia-me. NAO CANONICO por instrucao |
| `Admin Convertfy/CONTEUDO BRUTO` | 3 | referencia de e-mail | **alta** | figma-best-performing-emails e ride-nation. Candidato a evals/referencias-reais com checagem de lint |
| `Admin Convertfy/Testes` | 1 | outro | **baixa** | 1 nota |
| `list-growth` | 1 | captacao | **media** | Formularios e captacao. NAO integrar agora: vira skill futura. Contem a pasta com wikilink no nome |

## O que a suite JA usa

Somente `Admin Convertfy/Emails`, pelo symlink `./vault`:

- `_protocolo-de-selecao.md`, `_julgamento.md`, `_catalogo.md`, `_PADRAO-DO-VAULT.md`
- `componentes/variantes/` (75 notas), `componentes/secoes/`, `componentes/eixos/`,
  `componentes/requisitos/`, `componentes/convivencia/`, `componentes/lacunas/`
- `intencoes/`, `estruturas/`, `aprendizados/`
- `componentes/doutrina/subject-line-e-preview.md`

Indice em `docs/indice-vault.md` (41 notas indexadas de intencoes,
estruturas e aprendizados).

## O que existe no vault-repo e a suite NAO usa

Ordenado por valor para a suite de e-mail.

| # | O que e | Onde | Por que importa | Esforco |
|---|---|---|---|---|
| 1 | **Referencias de e-mail** | `Conhecimento/Referencias/email/` | 11 notas de peca real catalogada. Entrada direta para `evals/referencias-reais/` | P |
| 2 | **figma-best-performing-emails** | `CONTEUDO BRUTO/figma-best-performing-emails/` | Pecas que performaram. Mesma checagem de lint da Fase 3.6 | M |
| 3 | **Doutrina do Max** | `Conhecimento/Advisors/Max/` (212 notas) | So `subject-line-e-preview` foi lido. Ha doutrina de copy, oferta e estrutura sem ponte para a suite | G |
| 4 | **Modelos de nota** | `Conhecimento/Padrao Convertfy/` | `modelo-decisao-com-numero` e `modelo-anti-exemplo` sao o formato certo para registrar eval e falso positivo | P |
| 5 | **Contexto da agencia** | `Conhecimento/Convertfy/` | `mapa-da-convertfy` e as estruturas de conta. Afeta `auditoria-omnisend` | P |
| 6 | **ride-nation** | `Conhecimento/Convertfy/ride-nation/`, `CONTEUDO BRUTO/ride-nation/` | Cliente real com material proprio. Candidato a `marcas/ride-nation.md` | M |
| 7 | **list-growth** | `list-growth/` | Captacao e formulario. **Nao integrar agora**, por instrucao. Vira skill futura | G |

## Defeito de sincronizacao registrado, nao corrigido

`vault-repo/list-growth/` tem uma pasta cujo nome contem wikilinks:

```
os-sete-testes-de-form]], [[list-growth
```

Parece nome de pasta gerado a partir de um wikilink quebrado na
sincronizacao do Obsidian. **Nao foi corrigido**: o vault e somente
leitura daqui. Corrigir no Obsidian.

## Regra de uso

`vault-repo/` e nivel 3 na hierarquia de fontes do `CLAUDE.md`. Nunca
editar, nunca copiar arquivo de la para ca, nunca versionar.
