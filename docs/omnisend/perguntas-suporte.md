# Perguntas prontas para o suporte do Omnisend

Para o que o teste em conta real nao responde, ou responde de forma
ambigua. Copie e cole.

Mande **uma pergunta por chamado**. Chamado com quatro perguntas volta
com uma resposta.

Antes de mandar: rode o teste de `roteiro-de-teste.md` primeiro. Resposta
de suporte sobre comportamento que voce nao observou e dificil de
interpretar.

---

## P1, sobre T1: valor padrao de merge tag

> Ola. Em automacao e campanha, uso `[[contact.first_name]]` no corpo do
> e-mail. Quando o contato nao tem primeiro nome preenchido, a tag
> resolve para vazio e a frase fica quebrada.
>
> Existe sintaxe de valor padrao (fallback) para merge tag de contato?
> Algo equivalente a `{{ first_name|default:"pessoa" }}`.
>
> Se existir, qual a sintaxe exata? Se nao existir, ha alguma forma
> recomendada de tratar contato sem nome, alem de segmentar por
> "tem primeiro nome" e montar duas versoes do e-mail?

## P2, sobre T3: propriedade de evento em bloco de texto

> Ola. Em uma automacao de carrinho abandonado (origem Shopify), quero
> citar o nome do produto em um **bloco de texto**, na headline, nao
> apenas dentro do bloco de produto.
>
> As propriedades do evento (por exemplo o nome do produto de
> `added product to cart`) podem ser usadas como merge tag em bloco de
> texto? Se sim, qual o caminho exato da propriedade?
>
> Se nao for possivel, o nome do produto so pode aparecer dentro do bloco
> de produto da automacao. Esta correto?

## P3, sobre T4 e T5: link de recuperacao na origem Shopify

> Ola. Tenho automacoes de carrinho abandonado e checkout abandonado em
> lojas integradas por **Shopify** (nao por API).
>
> A documentacao da origem `api` cita `abandonedCheckoutURL`. Para a
> origem **Shopify**, qual e a tag do link que devolve o cliente ao
> carrinho com os itens dentro, e qual e a do link que reabre o checkout
> com os itens e o e-mail preenchidos?
>
> Preciso das duas tags exatas, porque sao o CTA principal desses dois
> e-mails.

## P4: limitador entre automacao e campanha

> Ola. Entendi que `frequencyLimiter` controla reentrada na mesma
> automacao e `overlapLimiter` controla sobreposicao entre automacoes.
>
> Existe algum controle que impeca um contato de receber um e-mail de
> automacao e uma **campanha manual** no mesmo dia? Se nao existir, qual
> a pratica recomendada para evitar isso?

---

## Ao receber resposta

1. Registre em `verificado.md`, com a data e o texto da resposta.
2. Resposta de suporte **nao substitui teste**: se der para testar,
   teste e registre os dois. Suporte ja respondeu coisa que o
   comportamento da conta contradisse.
3. Se a resposta fechar o TODO, tire o `nao verificado` da skill e troque
   o fallback pela sintaxe real, no mesmo commit.
