# Protocolo de execução

Contrato obrigatório de toda skill que **produz ou altera uma peca** de
e-mail: `email-copy`, `email-design`, `email-flows`, `email-qa` e
`auditoria-omnisend`. O roteador `convertfy-email` aplica este protocolo
antes de despachar.

Skill que precise divergir de qualquer item declara a divergência no
próprio SKILL.md, com o motivo. Divergência silenciosa e defeito.

---

## 1. Ficha da marca e brief (P01, P02)

Antes de gerar qualquer coisa:

1. Leia `marcas/<cliente>.md` se existir. Ela traz idioma, tom, tipografia
   principal, fonte secundaria, cor primaria, cor secundaria, uso de
   emoji, palavras proibidas e restrições legais do nicho.
2. O brief precisa trazer **oferta, produto e prazo**.

Sem ficha e sem esses três campos, **não gere**. Peca o que falta, em uma
pergunta só (ver item 4). Campo que falta vira `[FALTA: <campo>]`, nunca
invencao: número, estoque, prazo e depoimento inventados são C02 e C06,
ambos B.

Loja sem ficha ainda pode ser atendida se o brief cobrir os três campos.
Nesse caso registre na leitura do brief que a peca saiu sem ficha, porque
sem ficha o lint não consegue julgar C21, C22 e C31.

## 2. Regras anti-vício (C, D, P)

Sempre em vigor, sem exceção silenciosa:

| Arquivo | O que traz |
|---|---|
| `shared/anti-vicios-copy.md` | C01 a C47, com severidade, ruim e bom |
| `shared/anti-vicios-design.md` | D01 a D20, com status em e-mail |
| `shared/anti-vicios-processo.md` | P01 a P09 |
| `shared/calibracao.md` | o que **não** e vício, para não gerar falso positivo |
| `shared/padrao-de-qualidade.md` | o que a peça precisa **ter**, em perguntas de sim ou não |
| `shared/lexico/pt-br.txt`, `en.txt` | as listas de C20 a C26 |

Leia `calibracao.md` junto com as outras. Reprovar caixa alta em headline
curta, coluna única de 600px, número grande de oferta ou CTA repetido com
o mesmo destino e erro da skill, não da peca.

## 3. Gate de entrega: o lint decide

Antes de entregar, rode o que se aplicar:

```bash
python3 scripts/lint_copy.py --json <peca>.json
python3 scripts/lint_email.py --json <peca>.html
```

- **Qualquer violacao B: não entrega.** Corrija e rode de novo.
- Violacao A: corrija, salvo justificativa escrita na leitura do brief.
- Violacao M: julgamento, pode seguir.

Exit code 1 significa que existe B. O gate e o exit code, não a leitura
humana da saída. Regra dura e lint determinístico, nunca só instrução no
prompt: P05 existe porque travessão já escapou de prompt que o proibia.

## 4. Leitura do brief, e no máximo uma pergunta

Antes de gerar, escreva **uma linha** dizendo o que você entendeu do
brief: loja, tipo de e-mail, oferta, prazo e idioma.

```
Leitura: welcome 1 de 5, Loja X (pt-BR), 10% OFF com codigo BEMVINDO10,
valido 7 dias, sem minimo.
```

Se algo estiver ambíguo, faca **uma pergunta só**, juntando tudo que
falta. Não faca uma pergunta por campo e não gere enquanto a resposta não
vier, se o que falta for um dos três campos obrigatorios do item 1.

## 5. Entregue só o artefato (C07)

A saída e a peca. Sem comentario sobre a própria copy, sem "por que isso
funciona", sem explicar a escolha, sem oferecer variacoes que ninguem
pediu. C07 e B e o lint pega.

A leitura do brief do item 4 e a pergunta do item 4 não são comentario
sobre a copy: vem **antes** de gerar, e o artefato vem depois, separado.

## 6. Ordem de trabalho (P08)

Nunca escreva antes de decidir a estrutura:

```
intencao (var1)  ->  estrutura (var2)  ->  variantes do arsenal  ->  copy por schema
```

1. **Intencao** (`vault/intencoes/<flow>/<n>.md`): o que este toque faz,
   qual objecao ataca, papel de cada bloco.
2. **Estrutura** (`vault/estruturas/<flow>/`): a ordem das seções.
3. **Variantes** (`vault/componentes/variantes/<secao>/`, pelo passo a
   passo de `vault/componentes/_protocolo-de-selecao.md`): elimina antes
   de rankear.
4. **Copy por schema**: só agora o texto, campo a campo.

Pular da intencao direto para a copy e P08, e produz peca com estrutura
inventada. Zero candidata em uma seção não e erro: declare a lacuna, não
invente variante.

**Contrato de variante.** O contrato novo e o canonico e as skills só
geram nele. Das 75 notas, 43 estao no contrato legado: converta com
`scripts/adaptar_variante_legado.py` antes de usar. `aliviador` não
deriva e vem de `shared/aliviador-legado.json`; sem a decisão registrada,
a variante não pode ser usada. Ver `docs/vault/migracao-contrato.md`.

**Descompasso do catalogo:** `_catalogo.md` lista 44 slugs, a pasta tem
75 notas. O 44o não e variante: e `body-8-cards-vidro`, slug antigo de
uma nota renomeada. Enderece por `variant_id`, nunca por número.
