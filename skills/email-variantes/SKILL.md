---
name: email-variantes
description: Use ao pedir opcoes, versoes ou alternativas de uma peca de e-mail, ou ao preparar um teste A/B. Gera exatamente 3 versoes que divergem em um eixo nomeado (oferta, prova ou problema), nunca em redacao da mesma ideia, e monta um index.html que poe as tres lado a lado para escolher. Use tambem quando a primeira versao nao convenceu e ninguem sabe dizer por que. Nao escolhe a vencedora e nao faz QA (isso e email-qa).
---

# email-variantes

Tres versoes que **divergem de verdade**, e uma pagina para comparar.

O vicio que esta skill existe para matar e P03: variacoes que sao a mesma
ideia pintada de cor diferente. Tres jeitos de escrever "10% OFF na
primeira compra" nao sao tres variantes, sao uma variante com tres
redacoes, e um teste entre elas nao ensina nada.

## A regra: um eixo nomeado por variante

Cada variante ataca o cliente por um **angulo diferente**. O eixo e
declarado antes de escrever, e aparece no comparativo.

| Eixo | A variante aposta que | O que muda na peca |
|---|---|---|
| **oferta** | O que decide e a condicao comercial | Valor, codigo, prazo e minimo na frente. Hero e a oferta |
| **prova** | O que decide e outra pessoa ter comprado | Avaliacao, nota, depoimento ou UGC na frente. Hero e a prova |
| **problema** | O que decide e o cliente se reconhecer | A dor especifica na frente. Hero e o problema, a oferta desce |

As tres respondem ao mesmo brief, com a mesma oferta real e o mesmo
produto. **O que muda e a ordem do argumento, nao o fato.**

Nao invente oferta diferente por variante: isso deixa de ser teste de
mensagem e vira teste de promocao, que e outra coisa e nao e desta skill.

## Quando um eixo nao serve

- Sem prova real no brief (avaliacao, nota, depoimento), **nao gere a
  variante de prova**. Inventar prova e C02, que e B. Gere duas e diga
  por que a terceira nao existe.
- Sem uma dor clara do nicho, a variante de problema vira pergunta
  retorica generica, que e C15. Prefira duas boas a tres, sendo uma ruim.
- Loja sem oferta no brief: so o eixo de problema e o de prova fazem
  sentido, e o pedido provavelmente e editorial, nao campanha.

Duas variantes honestas valem mais que tres com uma inventada.

## Ordem de trabalho

Igual a de toda a suite (P08), com um passo a mais no comeco.

```
0. declarar os 3 eixos, em uma linha cada
1. intencao (var1)     -> a mesma para as tres
2. estrutura (var2)    -> pode divergir: o eixo muda a ordem das secoes
3. variantes do arsenal-> escolhe por secao, por eixo
4. copy por schema     -> so agora o texto
5. index.html          -> comparativo
6. lint nas tres       -> B em uma nao derruba as outras
```

O passo 2 e onde a divergencia fica real. Se as tres tiverem a mesma
estrutura, voce provavelmente escreveu a mesma variante tres vezes.

## Protocolo obrigatorio

Segue `shared/protocolo-de-execucao.md`. Especificidades desta skill:

- **Ficha e brief (P01, P02).** Mesmo brief para as tres. Sem oferta,
  produto e prazo, nao gera.
- **Leitura do brief**, uma linha, mais a declaracao dos tres eixos.
- **Gate de lint nas tres**, separadamente. Variante com B nao entra no
  comparativo: entra como "reprovada", com o ID, e o comparativo mostra
  as que passaram.
- **So o artefato (C07).** O comparativo mostra o eixo e a peca. Nao
  escreva "esta e a mais forte porque...". Quem escolhe e o humano.

## index.html do comparativo

Um arquivo, autocontido, aberto no navegador. Sem dependencia externa,
sem CDN, sem fonte remota.

Requisitos:

- As tres pecas **lado a lado**, cada uma em um `iframe` com 600px de
  largura, que e a largura real do e-mail.
- Acima de cada uma: o **nome do eixo**, o assunto e o preheader, que sao
  o que decide a abertura e nao aparecem no corpo.
- Uma linha de dados por variante: contagem de palavras do corpo,
  numero de CTAs e resultado do lint (`limpo`, `A: n`, `B: n`).
- Alternar dark mode nas tres ao mesmo tempo, para comparar no mesmo
  estado.
- Sem vencedora marcada, sem estrela, sem "recomendada". A pagina compara,
  nao opina.

Estrutura e o HTML de referencia em `references/comparativo.md`.

## O que esta skill nunca faz

- Nao gera variacao de redacao da mesma ideia (P03).
- Nao escolhe a vencedora, e nao marca recomendada.
- Nao inventa oferta, prova ou dado para diferenciar (C02, C06).
- Nao gera tres a qualquer custo: duas honestas valem mais.
- Nao faz QA. Peca escolhida vai para `email-qa` antes de enviar.


## Contrato de variante

O **contrato novo e o canonico**. Esta skill so gera no contrato novo.

Das 75 notas de variante do vault, 32 ja estao no contrato novo e **43
estao no legado**. Quando o protocolo de selecao escolher uma legada,
converta antes de usar:

```bash
python3 scripts/adaptar_variante_legado.py <slug> --json
```

O adaptador carrega os campos compartilhados, deriva `profundidade` e
aposenta `momento`, `ativa` e os outros campos que sairam do contrato.

**`aliviador` nao deriva de nada.** Vem de `shared/aliviador-legado.json`,
que e o registro das decisoes humanas. Slug sem entrada la volta como
`[FALTA: decisao humana]` e o adaptador sai com exit code 1.

Variante legada com pendencia **nao pode ser usada para gerar**: peca a
decisao de `aliviador` ou escolha outra variante. Nunca preencha por
inferencia, nem copie o `aliviador` de uma variante parecida.

Ver `docs/vault/migracao-contrato.md`.

## Referencias

| Arquivo | Quando |
|---|---|
| `references/comparativo.md` | Montar o `index.html` |
| `shared/vocabulario-arsenal.md` | Escolher variante de secao por eixo |
| `shared/protocolo-de-execucao.md` | O contrato de execucao |
| `skills/email-copy/SKILL.md` | Escrever os campos de cada variante |
| `skills/email-design/SKILL.md` | Montar o HTML de cada variante |
