---
name: email-qa
description: Use ao fazer QA de um e-mail pronto antes do envio: rodar os linters, conferir render em Outlook, Gmail e Apple Mail, checar dark mode, alt de imagem, contraste, tamanho do arquivo e clipping do Gmail, links e UTM, merge tag com fallback, e os itens de conformidade da peca (descadastro visivel, endereco fisico, idioma do cupom). Tambem ao receber um .eml e verificar autenticacao e one-click unsubscribe. Nao escreve copy (isso e email-copy), nao monta o HTML (isso e email-design) e nao audita a conta inteira (isso e auditoria-omnisend).
---

# email-qa

Ultimo portao antes do envio. Recebe uma peca pronta e responde uma coisa
so: **vai ou nao vai**.

Esta skill nao conserta a peca. Ela reprova com o ID e devolve para
`email-design` ou `email-copy`. Quem conserta e quem escreveu.

Divergencias desta skill em relacao ao CLAUDE.md: nenhuma.

## Protocolo obrigatorio

Esta skill segue `shared/protocolo-de-execucao.md` inteiro. Em resumo:

1. **Ficha e brief (P01, P02).** Le `marcas/<cliente>.md` quando existir.
   Sem ficha, C21, C22 e C31 ficam sem julgamento: registre isso no
   veredito em vez de aprovar por omissao. Para QA, o brief precisa
   trazer **oferta, produto e prazo** para que C02 e C46 sejam checaveis.
2. **Anti-vicios.** Aplica `shared/anti-vicios-copy.md`,
   `anti-vicios-design.md`, `anti-vicios-processo.md` e, junto,
   `shared/calibracao.md`. Nesta skill a calibracao pesa mais que nas
   outras: QA que reprova convencao legitima de e-mail gera retrabalho e
   perde a confianca do time.
3. **Gate de lint.** Roda `scripts/lint_copy.py` e `scripts/lint_email.py`.
   **Violacao B: reprova.** O gate e o exit code.
4. **Leitura do brief.** Uma linha dizendo o que entendeu. Se ambiguo,
   **uma pergunta so**.
5. **So o artefato (C07).** A saida e o veredito, no formato abaixo. Sem
   comentario sobre a copy alheia alem do ID e da correcao objetiva.
6. **Ordem de trabalho (P08).** QA entra depois da montagem, mas confere
   se a ordem foi seguida: peca cuja estrutura nao corresponde a nenhuma
   var2 do vault e achado de processo, nao de gosto.

## Ordem de execucao

Barato primeiro, caro depois. Parar no primeiro B economiza o resto.

```
1. lint_email.py   (HTML)        -> B aqui, reprova e para
2. lint_copy.py    (campos)      -> B aqui, reprova e para
3. checagem manual do que o lint nao ve
4. veredito
```

O lint nao substitui os passos 3. Ele cobre o que e deterministico; o
resto e leitura. Ver `references/checklist-manual.md`.

## O que o lint ja cobre

Nao repita a mao. `lint_email.py` entrega D18, D02, D17, D04, D05,
tamanho acima de 102 KB, container fora de 600, preheader ausente, CTA
so em imagem e placeholder repetido. `lint_copy.py` entrega C01 a C47.

Rode os dois e leia o JSON:

```bash
python3 scripts/lint_email.py --json peca.html
python3 scripts/lint_copy.py  --json peca.json
```

## O que o lint nao ve

Estes sao a razao de existir desta skill. Detalhe em
`references/checklist-manual.md` e `references/eml.md`.

| # | Checagem | Como | Severidade |
|---|---|---|---|
| Q01 | Render real em Outlook, Gmail e Apple Mail | Teste de caixa ou ferramenta de preview | B se quebrar estrutura |
| Q02 | Dark mode nos tres clientes, nao so no CSS | Captura lado a lado | B se sumir conteudo |
| Q03 | Alt **descritivo**, nao so presente | Leitura humana: o alt sozinho conta a oferta? | A |
| Q04 | Link aponta para onde diz | Clicar todos, inclusive o do logo | B se quebrado |
| Q05 | UTM presente e consistente | Comparar com a convencao da loja | A |
| Q06 | Merge tag com fallback, testada vazia | Preview com o campo vazio | B, e C47 |
| Q07 | Descadastro visivel e funcional | Achar no render, nao no codigo | B |
| Q08 | Endereco fisico do remetente | Exigencia legal de e-mail comercial | B |
| Q09 | Cupom no idioma da loja e valido no Shopify | Conferir no admin, nao presumir | B, e C04 |
| Q10 | Prazo da oferta bate com o cupom real | Comparar peca e admin | B, e C06 |
| Q11 | Peca acima da dobra faz sentido sem imagem | Desligar imagens | A |
| Q12 | Estrutura corresponde a uma var2 do vault | Comparar com `vault/estruturas/` | A, P08 |

Q07, Q08, Q09 e Q10 sao conformidade, nao gosto: reprovam sozinhos.

## Quando existe o .eml

Se voce conseguir o `.eml` de um envio de teste, ele resolve de uma vez o
que nenhuma outra fonte entrega: autenticacao e one-click unsubscribe.

- `Authentication-Results`: SPF, DKIM e DMARC, os tres com `pass`.
- `List-Unsubscribe` e `List-Unsubscribe-Post`: os dois presentes, o
  segundo com `List-Unsubscribe=One-Click` (RFC 8058).

Leia sempre o cabecalho **de cima**, que e o do servidor que recebeu. Os
de baixo podem ter sido forjados pela origem.

Procedimento de coleta por cliente em `references/eml.md`. Sem `.eml`,
marque como `nao verificado`, nunca como aprovado.

## Formato do veredito

A saida e isto, e nada alem disto.

```
VEREDITO: reprovado
Bloqueios (B): 2
  D18  HTML    position:absolute no bloco hero
  Q07  render  descadastro nao aparece no render, so no codigo
Corrigir (A): 1
  C41  copy    preheader repete o assunto (Jaccard 0,71)
Observacao (M): 0
Nao verificado: autenticacao e one-click, sem .eml
```

Aprovado tem a mesma forma, com `VEREDITO: aprovado` e as listas vazias.
Nunca escreva "aprovado com ressalva": ou os B estao zerados, ou reprova.

## O que esta skill nunca faz

- Nao conserta a peca. Reprova com ID e devolve.
- Nao aprova por omissao. O que nao foi verificado aparece como
  `nao verificado`, com o motivo.
- Nao afirma que uma checagem passou sem evidencia.
- Nao reprova convencao legitima de e-mail: caixa alta em headline curta,
  coluna unica de 600px, numero grande de oferta, CTA repetido com o
  mesmo destino. Ver `shared/calibracao.md`.
- Nao audita a conta. Cobertura de automacao, reputacao de dominio e
  saude da base sao de `auditoria-omnisend`.

## Referencias

| Arquivo | Quando |
|---|---|
| `references/checklist-manual.md` | Q01 a Q12, passo a passo |
| `references/eml.md` | Coletar e ler o `.eml` |
| `shared/calibracao.md` | Antes de reprovar qualquer coisa |
| `shared/anti-vicios-design.md` | Para o ID correto de um achado de design |
| `skills/email-design/SKILL.md` | Para devolver um achado de HTML |
| `skills/email-copy/SKILL.md` | Para devolver um achado de copy |
