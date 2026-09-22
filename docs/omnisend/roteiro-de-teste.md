# Roteiro de teste: fechar T1, T3, T4 e T5

Passo a passo para responder em conta real o que a documentacao e o MCP
nao respondem. Feito para **um envio por teste, so para um e-mail seed**.

Enquanto um item nao for testado, ele vale como `nao verificado` nas
skills, com o fallback seguro descrito em cada secao.

Registre cada resultado em `docs/omnisend/verificado.md`. Teste sem
registro nao fecha o item.

---

## Antes de comecar

**Conta.** Use uma loja de baixo volume, ou uma conta de sandbox. Nao
teste em loja com campanha ativa no mesmo dia: o `overlapLimiter` pode
segurar a automacao e voce vai achar que o teste falhou.

**E-mail seed.** Um endereco so, que voce controla, com caixa que voce
consegue abrir no desktop. Gmail ajuda, porque tem "Exibir original".

**Contato seed.** Crie um contato com **nome preenchido** e outro com
**nome vazio**. Os dois precisam estar inscritos em e-mail. T1 depende
dos dois.

**Regra de ouro.** Cada teste isola uma variavel. Se voce mudar o texto e
o gatilho na mesma rodada, o resultado nao responde nada.

---

## T1. Valor padrao para tag de contato vazia

**Pergunta.** Existe mecanismo de valor padrao quando `[[contact.first_name]]`
esta vazio? No Klaviyo seria `{{ first_name|default:"there" }}`.

**Por que importa.** C47 (personalizacao sem fallback) e severidade A. Sem
resposta, toda frase precisa funcionar sem o nome.

**Teste**

1. Crie uma campanha de rascunho, publico = apenas o e-mail seed.
2. No corpo, ponha as quatro formas na mesma peca, uma por linha:
   ```
   A: Oi [[contact.first_name]], tudo bem?
   B: Oi [[contact.first_name | default: "tudo bem"]], tudo bem?
   C: Oi [[contact.first_name|default:"pessoa"]], tudo bem?
   D: Oi [[contact.first_name ?? "pessoa"]], tudo bem?
   ```
3. Envie para o contato **com nome**. Guarde o print.
4. Envie para o contato **sem nome**. Guarde o print.

**Como ler**

| O que aparece na linha B, C ou D com nome vazio | Conclusao |
|---|---|
| A palavra do default | A sintaxe funciona. Registre qual |
| Vazio, e a frase fica "Oi , tudo bem?" | Nao ha default nessa sintaxe |
| O texto cru, com colchetes | A sintaxe nao e reconhecida |

**Fallback enquanto aberto.** A frase tem que ler bem com o campo vazio.
Prefira o nome no fim da frase, ou nao use nome. `Oi, tudo bem?` sem nome
e melhor que `Oi , tudo bem?`.

---

## T3. Propriedade de evento como merge tag em bloco de texto

**Pergunta.** Da para escrever "ainda pensando na Camiseta Pima?" em um
bloco de texto, ou o nome do produto so existe dentro do bloco de
produto?

**Por que importa.** Decide se a copy de carrinho abandonado pode citar o
produto na headline, que e o toque mais valioso da sequencia.

**Teste**

1. Crie uma automacao de carrinho abandonado (`product_cart_recovery`),
   com `inactivitySettings` curto: 15 minutos, se a conta permitir.
2. No e-mail, deixe o bloco de produto obrigatorio **e** adicione um
   bloco de texto com as variacoes:
   ```
   A: Ainda pensando na [[event.productName]]?
   B: Ainda pensando na [[event.product_name]]?
   C: Ainda pensando na [[event.extra.productName]]?
   D: Ainda pensando na [[trigger.productName]]?
   ```
3. Com o contato seed, adicione um produto ao carrinho na loja e
   abandone. Nao finalize.
4. Espere a automacao disparar. Guarde o print do e-mail recebido.

**Como ler**

| Resultado | Conclusao |
|---|---|
| Uma das linhas traz o nome do produto | Propriedade de evento serve em texto. Registre a sintaxe |
| Todas vazias, e o bloco de produto preenchido | So dentro do bloco de produto |
| Texto cru com colchetes | Sintaxe nao reconhecida |

**Fallback enquanto aberto.** Nao cite o produto no texto. Deixe o bloco
de produto fazer esse trabalho e escreva a headline generica:
"Voce deixou algo para tras", nao "Voce deixou a Camiseta Pima".

---

## T4. Link de recuperacao de carrinho na origem `shopify`

**Pergunta.** Qual a tag do link que devolve o cliente ao carrinho, em
loja com origem `shopify`? A origem `api` expoe `abandonedCheckoutURL`; a
`shopify` nao esta documentada.

**Por que importa.** E o CTA do e-mail. Sem ele, o botao manda para a
home e a recuperacao vira navegacao.

**Teste**

1. Use a mesma automacao do T3, ou crie outra igual.
2. No CTA, teste uma por rodada (o link e uma so, nao da para empilhar):
   ```
   rodada 1: [[event.abandonedCheckoutURL]]
   rodada 2: [[event.extra.abandonedCheckoutURL]]
   rodada 3: [[event.cartRecoveryUrl]]
   rodada 4: [[event.extra.cartURL]]
   ```
   Alternativa mais rapida: ponha as quatro como **texto visivel** no
   corpo, em vez de href. Uma rodada so, e voce ve qual resolve.
3. Abandone um carrinho com o contato seed.
4. No e-mail recebido, veja qual variante virou URL de verdade.
5. **Clique.** Confirme que o carrinho vem com o item dentro, nao vazio.

**Como ler**

Resolver para uma URL nao basta. O criterio e o carrinho abrir **com o
item**. URL que abre a loja vazia conta como falha.

**Fallback enquanto aberto.** O link de recuperacao **sempre e testado
antes de enviar**, em envio de teste real, com clique e conferencia do
carrinho. Nenhum flow de carrinho vai ao ar sem esse clique. Na duvida,
aponte para a pagina da colecao do produto, que e pior em conversao mas
nunca leva a carrinho vazio.

---

## T5. Link de retomada de checkout na origem `shopify`

**Pergunta.** Mesma coisa do T4, para `started checkout` em vez de
`added product to cart`.

**Por que importa.** Checkout abandonado converte mais que carrinho. O
link errado desperdica o toque mais quente da base.

**Teste**

Igual ao T4, com duas diferencas:

1. O gatilho e `started checkout`.
2. Com o contato seed, va **ate a tela de pagamento** e saia sem pagar.
   Parar antes disso dispara `added product to cart`, nao
   `started checkout`, e o teste responde a pergunta errada.

Variantes a testar:
```
[[event.abandonedCheckoutURL]]
[[event.extra.abandonedCheckoutURL]]
[[event.checkoutURL]]
[[event.extra.checkoutUrl]]
```

**Como ler.** O criterio e o checkout reabrir **com os itens e o e-mail
ja preenchidos**. Reabrir vazio conta como falha.

**Fallback enquanto aberto.** Mesmo do T4: link sempre testado com
clique antes do envio.

---

## Ordem e custo

| Ordem | Item | Envios | Por que nesta ordem |
|---|---|---|---|
| 1 | T1 | 2 | Nao depende de automacao, e o mais barato |
| 2 | T3 | 1 | Ja monta a automacao de carrinho que o T4 reusa |
| 3 | T4 | 1 | Reusa a automacao do T3 |
| 4 | T5 | 1 | Precisa de checkout real, e o mais trabalhoso |

Cinco envios no total, todos para um e-mail seed.

## O que nao da para testar assim

Vira pergunta pronta para o suporte, em
`docs/omnisend/perguntas-suporte.md`. Nao tente inferir do
comportamento: ausencia de resultado em um teste nao prova ausencia de
recurso, prova que a sintaxe testada nao era a certa.
