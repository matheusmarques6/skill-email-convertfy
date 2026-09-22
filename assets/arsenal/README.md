# assets/arsenal

Blocos HTML de e-mail prontos e validados, mais o manifesto que diz de onde
cada um veio.

A regra que organiza esta pasta cabe em uma linha:
**o vault é a fonte de verdade do HTML das variantes, e esta pasta não
guarda cópia dele.**

---

## 1. Quem é fonte de verdade

| Camada | O que é | Pode editar? |
|---|---|---|
| Banco (`email_component_variants`, Supabase) | O HTML que o pipeline renderiza de fato | Pelo admin, fora deste repo |
| `vault/componentes/_html/<slug>.html` | O HTML das variantes, **conferido por md5 contra o banco** (44 de 44 bateram em 31/08, ver `vault/componentes/_inventario.md`) | Não. O vault é somente leitura aqui, e é symlink fora do git |
| `vault/componentes/variantes/<secao>/<slug>.md` | O julgamento da variante: quando usar, copy, design system, direção fotográfica | Não |
| `assets/arsenal/` | O que **não** existe no vault: blocos de seção sem variante, fragmentos técnicos da casa, e o manifesto | Sim, é deste repo |

Consequência prática: se o bloco já tem variante no vault, ele **não** entra
aqui como arquivo. Entra como **linha no manifesto**, apontando para o
caminho no vault e carregando o md5 que prova que o arquivo não mudou.

Por que não copiar, já que seria mais cômodo:

1. O vault muda no Obsidian e sincroniza por Git. Uma cópia aqui nasce
   desatualizada e ninguém percebe, porque as duas renderizam.
2. O `variant_id` é o identificador estável. Cópia com nome diferente
   quebra o fio entre a peça montada e a telemetria.
3. `CLAUDE.md` proíbe gerar arquivo dentro do vault e proíbe tratar o vault
   como material de cópia. Espelhar o vault aqui é a mesma coisa pelo
   caminho inverso.

---

## 2. O que entra aqui

Três famílias, e só três.

### 2.1 `blocos/`: seção sem variante no vault

Hoje, `header` e `cta` têm **zero** variantes
(`vault/componentes/secoes/_header.md`, `_cta.md`), e as oito estruturas de
referência do welcome pedem `header`; duas pedem `cta`. É o buraco mais
citado do vault.

Um bloco aqui é **proposta**, não variante. Ele não vira variante por estar
nesta pasta: vira quando alguém o cadastra no banco e escreve a nota no
Obsidian. Enquanto isso, ele existe para o pipeline não cair em silêncio no
template global, e a lacuna correspondente continua aberta
(`vault/componentes/lacunas/header-sem-variante.md`,
`cta-sem-variante.md`).

Nomeação: `blocos/<secao>/<secao>-<n>-<slug>.html`, kebab-case ASCII, o
mesmo padrão do vault.

### 2.2 `fragmentos/`: peça técnica genérica da casa

Trechos que não são bloco de seção e não pertencem a variante nenhuma:
botão bulletproof com VML, bloco de preheader, tabela raiz de 600px,
`<head>` com os metas de dark mode, rodapé legal mínimo. São o que as
skills colam, e o que o `lint_email.py` usa como referência do certo.

Todo fragmento obedece às regras técnicas fixas: container de 600px,
tabelas com `role="presentation"`, estilos inline, botão bulletproof,
compatível com Outlook, seguro em dark mode.

### 2.3 `manifesto.json`: o índice de tudo

Uma entrada por bloco, seja ele do vault ou daqui. É o único arquivo que
enxerga as duas origens.

---

## 3. Formato do manifesto

`assets/arsenal/manifesto.json`, lista de objetos. Campos obrigatórios em
toda entrada:

```json
[
  {
    "slug": "reviews-1-depoimento-com-credencial",
    "secao": "reviews",
    "origem": "vault",
    "variant_id": "d48deaa4-6d8b-4a09-95fb-e512b676c8d8",
    "caminho": "vault/componentes/_html/reviews-1-depoimento-com-credencial.html",
    "md5": "aed53e92ad74e98385ab314f2e55d791",
    "md5_conferido_em": "2026-09-22",
    "nota_de_julgamento": "vault/componentes/variantes/reviews/reviews-1-depoimento-com-credencial.md",
    "schema_campos": 10,
    "validado": null,
    "observacao": "HTML conferido por md5 contra o banco em 31/08 (vault/componentes/_inventario.md)"
  },
  {
    "slug": "header-1-barra-de-logo",
    "secao": "header",
    "origem": "arsenal",
    "variant_id": null,
    "caminho": "assets/arsenal/blocos/header/header-1-barra-de-logo.html",
    "md5": "<md5 do arquivo local>",
    "md5_conferido_em": "2026-09-22",
    "nota_de_julgamento": null,
    "schema_campos": 3,
    "validado": "2026-09-22",
    "observacao": "Proposta. Fecha parcialmente a lacuna header-sem-variante; ainda não cadastrada no banco"
  }
]
```

| Campo | O que é | Regra |
|---|---|---|
| `slug` | nome do bloco, sem extensão | kebab-case ASCII, único no manifesto inteiro |
| `secao` | uma das oito | `header`, `hero`, `body`, `products`, `reviews`, `cta`, `offer`, `footer`. Nunca duas |
| `origem` | de onde o HTML vem | `vault` (o arquivo vive no vault), `arsenal` (vive aqui), `proposta` (ainda não é nenhum dos dois, o caminho aponta para um rascunho) |
| `variant_id` | o UUID do banco | obrigatório quando `origem: vault`; `null` quando não existe. Este é o identificador estável, não o slug |
| `caminho` | caminho relativo à raiz do repo | aponta para o vault ou para esta pasta. Nunca duplica conteúdo |
| `md5` | md5 do arquivo em `caminho` | é o que detecta divergência entre o que foi validado e o que está lá hoje |
| `md5_conferido_em` | data da última conferência | `AAAA-MM-DD` |
| `nota_de_julgamento` | caminho da nota de variante | `null` quando não há nota |
| `schema_campos` | número de campos preenchíveis | `0` significa não preenchível, e portanto não candidata (passo 3 do protocolo) |
| `validado` | data em que passou no `lint_email.py` | `null` enquanto não passou. `null` não é reprovação, é ausência de teste |
| `observacao` | uma linha de contexto | vazio quando não há o que dizer |

**Conferência de md5.** Uma entrada `origem: vault` não guarda cópia, então
o md5 é a única prova de que o arquivo validado é o arquivo de hoje:

```
md5sum $(python3 -c "import json;print(' '.join(e['caminho'] for e in json.load(open('assets/arsenal/manifesto.json'))))")
```

Divergência não é erro de manifesto: é aviso de que o vault mudou. O
procedimento é revalidar o bloco e atualizar `md5` e `md5_conferido_em`,
nunca reescrever o arquivo do vault.

---

## 4. Cobertura de hoje (22/09/2026)

- `vault/componentes/_html/` tem **44 arquivos**, um por variante do
  `_catalogo.md`.
- `vault/componentes/variantes/` tem **75 notas**. As 31 variantes da
  catalogação de 19/09 **não têm HTML no vault** e não estão no catálogo
  (`vault/componentes/_relatorio-catalogacao-2026-09-19.md`: o peso delas foi
  medido no HTML de produção, fora do vault). Para essas, a entrada do
  manifesto nasce com `origem: proposta`, `caminho: null` e a observação de
  que o HTML só existe no banco.
- `header` e `cta`: **zero** dos dois lados. É o que `blocos/` existe para
  atacar.
- Uma armadilha de nome: `body-8-cards-de-vidro-por-ocasiao` tem o HTML em
  `vault/componentes/_html/body-8-cards-vidro.html`, com o nome antigo (a
  nota foi renomeada em 19/09). O manifesto resolve pelo `caminho`, não
  presumindo que o arquivo se chama como o slug.

---

## 5. O que esta pasta não faz

- Não guarda peça montada. E-mail pronto de cliente não é arsenal.
- Não guarda variação de cor de marca. O arsenal é neutro: fundo branco,
  texto preto. Cor entra por ficha de marca (`marcas/<loja>.md`), em acento.
- Não decide escolha de bloco. Isso é
  `vault/componentes/_protocolo-de-selecao.md`, e a tradução do pedido
  falado para o slug é `shared/vocabulario-arsenal.md`.
- Não substitui o cadastro. Bloco validado aqui só vira variante de verdade
  quando entra no banco e ganha nota no Obsidian.
