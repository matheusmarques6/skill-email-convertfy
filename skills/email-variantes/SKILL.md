---
name: email-variantes
description: Use ao pedir opções, versões ou alternativas de uma peca de e-mail, ou ao preparar um teste A/B. Gera exatamente 3 versões que divergem em um eixo nomeado (oferta, prova ou problema), nunca em redacao da mesma ideia, e monta um index.html que poe as três lado a lado para escolher. Use também quando a primeira versão não convenceu e ninguem sabe dizer por que. Não escolhe a vencedora e não faz QA (isso e email-qa).
---

# email-variantes

Três versões que **divergem de verdade**, e uma página para comparar.

O vício que esta skill existe para matar e P03: variacoes que são a mesma
ideia pintada de cor diferente. Três jeitos de escrever "10% OFF na
primeira compra" não são três variantes, são uma variante com três
redacoes, e um teste entre elas não ensina nada.

## A regra: um eixo nomeado por variante

Cada variante ataca o cliente por um **angulo diferente**. O eixo e
declarado antes de escrever, e aparece no comparativo.

| Eixo | A variante aposta que | O que muda na peca |
|---|---|---|
| **oferta** | O que decide e a condição comercial | Valor, código, prazo e mínimo na frente. Hero e a oferta |
| **prova** | O que decide e outra pessoa ter comprado | Avaliacao, nota, depoimento ou UGC na frente. Hero e a prova |
| **problema** | O que decide e o cliente se reconhecer | A dor específica na frente. Hero e o problema, a oferta desce |

As três respondem ao mesmo brief, com a mesma oferta real e o mesmo
produto. **O que muda e a ordem do argumento, não o fato.**

Não invente oferta diferente por variante: isso deixa de ser teste de
mensagem e vira teste de promocao, que e outra coisa e não e desta skill.

## Quando um eixo não serve

- Sem prova real no brief (avaliacao, nota, depoimento), **não gere a
  variante de prova**. Inventar prova e C02, que e B. Gere duas e diga
  por que a terceira não existe.
- Sem uma dor clara do nicho, a variante de problema vira pergunta
  retorica genérica, que e C15. Prefira duas boas a três, sendo uma ruim.
- Loja sem oferta no brief: só o eixo de problema e o de prova fazem
  sentido, e o pedido provavelmente e editorial, não campanha.

Duas variantes honestas valem mais que três com uma inventada.

## Ordem de trabalho

Igual a de toda a suite (P08), com um passo a mais no começo.

```
0. declarar os 3 eixos, em uma linha cada
1. intencao (var1)     -> a mesma para as tres
2. estrutura (var2)    -> pode divergir: o eixo muda a ordem das secoes
3. variantes do arsenal-> escolhe por secao, por eixo
4. copy por schema     -> so agora o texto
5. index.html          -> comparativo
6. lint nas tres       -> B em uma nao derruba as outras
```

O passo 2 e onde a divergência fica real. Se as três tiverem a mesma
estrutura, você provavelmente escreveu a mesma variante três vezes.

## Protocolo obrigatório

Segue `shared/protocolo-de-execucao.md`. Especificidades desta skill:

- **Ficha e brief (P01, P02).** Mesmo brief para as três. Sem oferta,
  produto e prazo, não gera.
- **Leitura do brief**, uma linha, mais a declaracao dos três eixos.
- **Gate de lint nas três**, separadamente. Variante com B não entra no
  comparativo: entra como "reprovada", com o ID, e o comparativo mostra
  as que passaram.
- **Só o artefato (C07).** O comparativo mostra o eixo e a peca. Não
  escreva "esta e a mais forte porque...". Quem escolhe e o humano.

## index.html do comparativo

Um arquivo, autocontido, aberto no navegador. Sem dependencia externa,
sem CDN, sem fonte remota.

Requisitos:

- As três pecas **lado a lado**, cada uma em um `iframe` com 600px de
  largura, que e a largura real do e-mail.
- Acima de cada uma: o **nome do eixo**, o assunto e o preheader, que são
  o que decide a abertura e não aparecem no corpo.
- Uma linha de dados por variante: contagem de palavras do corpo,
  número de CTAs e resultado do lint (`limpo`, `A: n`, `B: n`).
- Alternar dark mode nas três ao mesmo tempo, para comparar no mesmo
  estado.
- Sem vencedora marcada, sem estrela, sem "recomendada". A página compara,
  não opina.

Estrutura e o HTML de referência em `references/comparativo.md`.

## O que esta skill nunca faz

- Não gera variacao de redacao da mesma ideia (P03).
- Não escolhe a vencedora, e não marca recomendada.
- Não inventa oferta, prova ou dado para diferenciar (C02, C06).
- Não gera três a qualquer custo: duas honestas valem mais.
- Não faz QA. Peca escolhida vai para `email-qa` antes de enviar.


## Contrato de variante

O **contrato novo e o canonico**. Esta skill só gera no contrato novo.

Das 75 notas de variante do vault, 32 já estao no contrato novo e **43
estao no legado**. Quando o protocolo de seleção escolher uma legada,
converta antes de usar:

```bash
python3 scripts/adaptar_variante_legado.py <slug> --json
```

O adaptador carrega os campos compartilhados, deriva `profundidade` e
aposenta `momento`, `ativa` e os outros campos que sairam do contrato.

**`aliviador` não deriva de nada.** Vem de `shared/aliviador-legado.json`,
que e o registro das decisões humanas. Slug sem entrada la volta como
`[FALTA: decisao humana]` e o adaptador sai com exit code 1.

Variante legada com pendência **não pode ser usada para gerar**: peca a
decisão de `aliviador` ou escolha outra variante. Nunca preencha por
inferencia, nem copie o `aliviador` de uma variante parecida.

Ver `docs/vault/migracao-contrato.md`.

## Referências

| Arquivo | Quando |
|---|---|
| `references/comparativo.md` | Montar o `index.html` |
| `shared/vocabulario-arsenal.md` | Escolher variante de seção por eixo |
| `shared/protocolo-de-execucao.md` | O contrato de execução |
| `skills/email-copy/SKILL.md` | Escrever os campos de cada variante |
| `skills/email-design/SKILL.md` | Montar o HTML de cada variante |
