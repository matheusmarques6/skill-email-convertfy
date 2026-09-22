# Correções a fazer no vault

O vault e somente leitura deste repo. Este arquivo registra o que precisa
ser corrigido **no Obsidian**, com o motivo e o texto sugerido.

Nada aqui foi aplicado. Quem aplica e humano, no Obsidian.

---

## VC01. Title Case e emoji no assunto: escopo de idioma

**Nota:** `vault/componentes/doutrina/subject-line-e-preview.md`
**Regra em conflito:** C34 (Title Case em pt-BR), e tensao com C31 (emoji)
**Severidade:** baixa. O conflito e menor do que parecia.
**Decisão tomada:** C34 vale só para pt-BR. Loja de idioma ingles pode
usar Title Case no assunto. Emoji no assunto só se `marcas/<cliente>.md`
permitir.

### O que a doutrina já diz certo

A nota **não** prescreve Title Case em portugues. Ela transcreve o
framework do Max como regra de forma em ingles e fecha com
"Nunca traduzir". A seção "Sem tradução" e explícita:

> Title Case e emoji são regras de forma em ingles; o vault não tem campo
> de idioma nem de tom de assunto. Onde o `registro` da loja (`luxo`,
> `clinico-sobrio`) parecer vetar emoji, a decisão e da pesquisa da loja,
> que precede esta doutrina.

Ou seja: a doutrina já e escopada por idioma e já cede a pesquisa da loja
no caso do emoji. O relatorio inicial que registrou isto como colisao
direta com C34 estava forte demais.

### O que ainda precisa mudar

Duas frouxidoes, não um conflito:

1. **"Nunca traduzir" não diz o que fazer em loja pt-BR.** A instrução e
   sobre não traduzir os exemplos, e uma skill pode ler como permissao
   para aplicar Title Case em portugues. Falta a frase que fecha a porta.
2. **"a decisão e da pesquisa da loja" não nomeia onde a decisão mora.**
   Neste repo ela mora em `marcas/<cliente>.md`, campo `marca_usa_emoji`,
   e o padrão sem ficha e não permitir.

### Texto sugerido

Na seção "Sem tradução", acrescentar ao fim:

> Em loja de idioma portugues, Title Case no assunto não se aplica: use
> caixa de frase ou caixa alta total. Esta e a regra C34 da suite de
> skills, e ela vence esta doutrina em pt-BR. Em loja de idioma ingles a
> doutrina vale como esta.
>
> O emoji depende da ficha da loja. Sem autorizacao explícita na ficha, o
> padrão e zero emoji no assunto e zero no corpo.

### Estado na suite

Já implementado, e coberto por teste:

- `scripts/lint_copy.py`, `regra_c34`: devolve zero achados quando
  `idioma` não e `pt-br`.
- `scripts/lint_copy.py`, `regra_c31`: limite de 1 emoji no assunto só
  quando `marca_usa_emoji` e verdadeiro; sem ficha, o padrão e `false`.
- `shared/anti-vicios-copy.md`: escopo de C34 e gate de ficha de C31
  escritos por extenso.
- `scripts/tests/test_lint_copy.py`: três testes travam o comportamento.

O idioma vem da ficha, não do texto. Loja inglesa com uma frase em
portugues segue sendo loja inglesa.

---

## VC02. Eixos `aliviador` e `profundidade` não existem

**Notas:** as 32 de contrato novo, mais `vault/componentes/eixos/`
**Regra do próprio vault:** `_INDEX.md` diz "Todo valor tem nota; valor
sem nota e bug (validar com `python .tools/valida.py`)"
**Severidade:** alta. O contrato canonico depende de dois eixos sem nota.

O contrato novo, que passou a ser o canonico, usa `aliviador` e
`profundidade`. Nenhum dos dois tem pasta em `eixos/`. Os que existem são
`momento` (21 valores), `objecao` (11), `paleta` (8), `papel-na-peca` (6)
e `registro` (10).

E `momento`, o único dos três em questão que tem notas, e justamente o
que esta sendo aposentado.

### O que criar

`eixos/aliviador/` com os 6 valores observados:

| Valor | Casos nas 32 |
|---|---|
| `dado_de_adequacao` | 21 |
| `demonstracao_de_mecanismo` | 4 |
| `prova_de_terceiro` | 4 |
| `transparencia_de_politica` | 2 |
| `comparacao_de_categoria` | 1 |
| `prova_por_volume` | 1 |

`eixos/profundidade/` com os 4 valores observados: `afirmacao`,
`mecanismo`, `prova_de_terceiro`, `garantia`.

### O que decidir junto

`momento` era o filtro dos passos 4 a 6 do protocolo. O contrato novo não
declara substituto. Ou nomeia o que filtra agora, ou declara que a fase
de filtro deixou de existir e o protocolo passa a eliminar só por `exige`
e `convivencia`.

Detalhe em `docs/vault/migracao-contrato.md`.

---

## VC03. `_PADRAO-DO-VAULT` A4 descreve o contrato antigo

**Nota:** `vault/_PADRAO-DO-VAULT.md`, seção A4
**Severidade:** media

O padrão ainda descreve `ativa` e `momento` como contrato de variante. As
32 notas novas não tem nenhum dos dois. O validador do vault reprovaria
as 32 pelo motivo errado, e quem escrever nota nova seguindo o padrão vai
escrever no contrato aposentado.

Atualizar A4 para o contrato novo, e registrar que as 43 legadas
convivem por enquanto, convertidas por adaptador.

---

## VC04. `_catalogo.md` e `_html/` com slug antigo

**Severidade:** baixa, mas causa erro silencioso

`_catalogo.md` e `_html/` tem `body-8-cards-vidro`. A nota se chama
`body-8-cards-de-vidro-por-ocasiao`. Regerar o catalogo com
`.tools/gera_catalogo.py` e renomear o HTML.

Enquanto não for corrigido, quem cruzar catalogo com pasta por slug perde
essa variante e conta 44 onde ha 43.

Relacionado: `reviews-8` e usado por duas variantes distintas
(`reviews-8-tres-cards-com-nota` e `reviews-8-ugc-de-comunidade`).
Enderece por `variant_id`, nunca por número.

---

## VC05. 12 valores de `exige` sem nota de requisito

**Severidade:** alta, porque `exige` e gate de código

Valores sem nota em `componentes/requisitos/`, entre eles
`oferta-bogo-real`, `politica-real`, `review-com-nome`,
`N-produtos-com-link` e `nota-real`.

`exige` e o passo 4 do protocolo e e resolvido por código. Gate sem nota
e gate que não elimina: a variante passa o filtro que deveria barra-la.

Lista completa em `docs/pesquisa/vault-vicios.md`.

---

## VC06. Notas de seção atrasadas

**Severidade:** media

`_reviews.md` cobre 7 variantes; a pasta tem 10. A chave de desempate do
passo 9 fica incompleta: `qualidade-eficacia` passou de 3 para 5
candidatas e `adesao-social` de 1 para 2.

Atualizar as notas de seção das seções que receberam variante em 19/09.
