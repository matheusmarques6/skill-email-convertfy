---
name: email-flows
description: Use ao desenhar, revisar ou montar um flow de e-mail no Omnisend para uma loja Shopify: welcome, carrinho abandonado, checkout abandonado, navegação abandonada, pós-compra, nutrição, winback, sunset, reposição e pedido de avaliação. Cobre gatilho, atraso, filtro de entrada, condição de saída, limitador de sobreposição e qual bloco de conteúdo cada tipo de automação exige. Não escreve a copy (isso é email-copy) nem o HTML (isso é email-design).
---

# email-flows

Desenha os 10 flows de ciclo de vida de uma loja de e-commerce no
**Omnisend**, que é o ESP principal da Convertfy. O Klaviyo é o
secundário: a tabela de equivalência entre os dois está em
`references/equivalencia-klaviyo-omnisend.md` e é mantida, não apagada.

Divergências desta skill em relação ao CLAUDE.md: nenhuma.


## Protocolo obrigatorio

Esta skill segue `shared/protocolo-de-execucao.md` inteiro. Em resumo:

1. **Ficha e brief (P01, P02).** Le `marcas/<cliente>.md` quando existir.
   Sem ficha e sem brief com **oferta, produto e prazo**, nao gera: pede o
   que falta. Campo ausente vira `[FALTA: <campo>]`, nunca invencao.
2. **Anti-vicios.** Aplica `shared/anti-vicios-copy.md`,
   `anti-vicios-design.md`, `anti-vicios-processo.md` e, junto,
   `shared/calibracao.md`, para nao reprovar convencao legitima de e-mail.
3. **Gate de lint.** Roda `scripts/lint_copy.py` e `scripts/lint_email.py`
   antes de entregar. **Violacao B: nao entrega.** O gate e o exit code.
4. **Leitura do brief.** Antes de gerar, uma linha dizendo o que entendeu.
   Se estiver ambiguo, **uma pergunta so**, juntando tudo que falta.
5. **So o artefato (C07).** Sem comentario sobre a propria copy, sem
   explicar a escolha, sem variacao que ninguem pediu.
6. **Ordem de trabalho (P08).** intencao (var1) -> estrutura (var2) ->
   variantes do arsenal -> copy por schema. Nunca escreve antes de
   decidir a estrutura.

## Antes de tudo: a regra do TODO

Onde o equivalente exato em Omnisend não está confirmado na documentação
oficial, esta skill escreve `TODO` com a variável Klaviyo original entre
parênteses. **Nunca invente nome de variável Omnisend.** Um nome inventado
renderiza vazio em produção, para a lista inteira, e ninguém percebe até o
cliente reclamar.

Os TODOs abertos estão listados em
`references/equivalencia-klaviyo-omnisend.md`, na seção final.

## As duas camadas

Modelo herdado do `email-campaign-skill` e adaptado.

| Camada | Escopo | Flows |
|---|---|---|
| **Entrada** | Por fonte de captação | Welcome, Nutrição |
| **Ciclo de vida** | Universal, uma vez por loja | Navegação abandonada, Carrinho abandonado, Checkout abandonado, Pós-compra, Winback, Sunset, Reposição, Pedido de avaliação |

**Por que entrada é por fonte:** o incentivo prometido muda por ponto de
captura. Quem entrou por "10% no primeiro pedido" espera o cupom; quem
entrou por um guia espera o guia. A copy herda a promessa do ponto de
captura e pode quebrá-la sem saber que ela existe.

**Por que ciclo de vida é universal:** o gatilho é uma ação no site, não
uma lista. Duplicar flow de carrinho por fonte de captação cria colisão e
não melhora nada.

No Omnisend, a camada de entrada se resolve com o gatilho
`"subscribed to marketing"` mais `trigger.audienceFilterGroup` filtrando por
`tag` ou `segmentID`, ou com o gatilho `"entered segment"`. Detalhe em
`references/os-10-flows.md`.

## Ordem de construção

Por prioridade de receita. Construa nesta ordem quando a loja é nova.

| # | Flow | Gatilho Omnisend | E-mails |
|---|---|---|---|
| 1 | Welcome | `subscribed to marketing` | 3 a 5 |
| 2 | Carrinho abandonado | `added product to cart` com `inactivitySettings` | 3 |
| 3 | Checkout abandonado | `started checkout` com `inactivitySettings` | 3 |
| 4 | Navegação abandonada | `viewed product` com `inactivitySettings` | 2 |
| 5 | Pós-compra | `placed order` ou `paid for order` | 4 a 5 |
| 6 | Nutrição | `subscribed to marketing` com atraso de 14 dias | 4 a 6 |
| 7 | Winback | `entered segment` (TODO: confirmar desenho do segmento) | 3 |
| 8 | Reposição | TODO: sem gatilho de tempo desde a compra documentado | 2 |
| 9 | Sunset | `entered segment` (TODO: confirmar desenho do segmento) | 2 |
| 10 | Pedido de avaliação | `order fulfilled` mais atraso | 1 a 2 |

Especificação completa de cada um, com blocos, atrasos, condições de saída
e bloco de conteúdo exigido: `references/os-10-flows.md`.

## O vocabulário do Omnisend

Traduzido do vocabulário Klaviyo do repo de origem.

### Blocos

Uma automação é uma lista ordenada de blocos. Quatro tipos:

| Tipo | Papel |
|---|---|
| `delay` | Espera. Modos: `duration` (quantidade mais unidade m/h/d/w/M), `immediate`, `specificTime` (hora do dia no fuso da marca). Todos aceitam `allowedWeekdays` |
| `action` | Faz algo: `sendEmail`, `sendSms`, `sendPush`, `sendWebhook`, `addTag`, `removeTag` |
| `split` | Ramifica por `filterGroup`, com filtros de evento, de contato ou de mensagem |
| `abTesting` | Divide por percentual entre dois caminhos |

Regras que mordem:

- **Um `delay` não pode ser o último bloco.**
- Blocos depois de um `split` rodam para os dois ramos: os ramos
  reconvergem.
- `sendEmail` e `sendSms` têm `isSkipAllowed` com padrão `true`: contato
  inelegível pula o bloco e segue. Em `sendPush`, o padrão na criação é
  `false`.

### Gatilho

`trigger.condition.event` recebe o nome do evento. Para loja Shopify, os
nomes reais são:

`subscribed to marketing` · `viewed product` · `added product to cart` ·
`started checkout` · `placed order` · `paid for order` · `ordered product`
· `order fulfilled` · `order canceled` · `order refunded` · `birthday` ·
`product back in stock` · `entered segment`

`origin` é `shopify` na maioria dos casos e o Omnisend resolve sozinho
quando o evento só existe em uma origem. `subscribed to marketing` não usa
`origin`. `birthday` e `product back in stock` também não.

**Sempre confirme o nome e as propriedades disponíveis na conta da loja**
com `post_event_metadata_query` antes de montar a automação. Evento que
nunca foi registrado naquela marca não serve de gatilho.

### O padrão de abandono

`trigger.inactivitySettings.duration` atrasa o início do workflow até o
contato ficar inativo (sem novo evento disparador) pelo período. Cada novo
disparo reinicia o relógio.

É exatamente o mecanismo de carrinho e checkout abandonado: 30 minutos
depois de `added product to cart` sem novo evento de carrinho. A
documentação do Omnisend nomeia esse uso.

### Filtro de entrada

`trigger.audienceFilterGroup` **não dispara nada**: só decide quem entra
quando o gatilho já disparou. Campos disponíveis: `segmentID`, `tag`,
`dateAdded`, `firstName`, `lastName`, `state`, `city`, `postalCode`,
`country`, `gender`.

### Condição de saída

`exitConditions` tira o contato da automação quando um evento acontece.
Várias condições são avaliadas com OR.

É o substituto direto do "flow filter: Has Placed Order since flow start"
do Klaviyo, e é **mais forte**: no Klaviyo o filtro só pula a mensagem, no
Omnisend a condição remove o contato.

Eventos de gatilho embutidos (`birthday`, `product back in stock`) **não
podem** ser condição de saída.

### Não existe "Smart Sending"

Smart Sending é recurso nomeado do Klaviyo (janela de 16h entre qualquer
duas mensagens ao mesmo contato). **O Omnisend não tem equivalente
idêntico.** O que ele tem:

| Recurso Omnisend | O que faz | O que não faz |
|---|---|---|
| `settings.frequencyLimiter` | `once` (uma vez por vida) ou `interval` (reentrada só depois de N horas, dias ou semanas) | Não olha outras automações nem campanhas |
| `settings.overlapLimiter` | `currentlyIn` (pula se o contato está ativo em automações listadas) ou `recentlyIn` (pula se concluiu alguma delas nos últimos 1 a 7 dias) | Não cobre campanha manual |

Consequência prática, que precisa estar no relatório ao cliente: **o
limite de frequência entre flow e campanha não é automático no Omnisend.**
Quem controla é o calendário de campanha. Listar isso como risco na
auditoria.

### Ciclo de vida da automação

- Automação nasce **desabilitada**. `isEnabled` é somente leitura.
- **Automação habilitada não pode ser alterada:** `PATCH` e
  `PUT /blocks` retornam `409`. Desabilite, altere, reabilite.
- `POST /automations/{id}/enable` com `enrollExisting` inscreve quem já
  qualifica. Para gatilho de evento, o workflow **precisa** começar com um
  bloco `delay`, senão retorna `409 enroll-existing-not-applicable`.
- `POST /automations/{id}/disable` com `contactsInWorkflow`: `keep`
  (quem está dentro continua) ou `exit` (sai todo mundo na hora).

## O conteúdo que cada tipo de automação exige

Esta é a parte que não existe no Klaviyo e que quebra o flow em silêncio
se for ignorada. A regra vale para o **primeiro e-mail** da automação, o
que carrega o conteúdo principal; os seguintes só levam a seção quando ela
cabe na mensagem.

| Tipo de automação | Seção ou blocos obrigatórios no template |
|---|---|
| Carrinho abandonado | Ao menos uma seção `product_cart_recovery` |
| Checkout abandonado | Ao menos uma seção `product_cart_recovery` |
| Navegação abandonada | Ao menos uma seção `product_cart_recovery` |
| Volta ao estoque | Ao menos uma seção `product_back_in_stock` |
| Confirmação de pedido | Blocos `orderSummary`, `orderProducts` e `orderTotal` |
| Confirmação de envio | Os três acima **mais** `orderAddresses` |
| Confirmação de cancelamento | `orderSummary`, `orderProducts`, `orderTotal` |
| Cross-sell, follow-up de pedido, reposição | Ao menos uma seção `product_recommender` |
| Welcome | Nenhuma seção obrigatória |

E, atravessando todos os tipos: **todo e-mail que oferece desconto carrega
o desconto num bloco `discount`**, não em texto. Ver abaixo.

## Desconto: o erro mais caro desta skill

Escrever "use o código BEMVINDO15" num bloco de texto **não cria código
nenhum na loja.** O destinatário tenta resgatar, falha, e o cliente fica
explicando.

O caminho correto:

- Bloco `discount`, com `discount.code` no placeholder `XXXX-XXXX-XXXX`.
  A loja substitui por um código único por destinatário no envio.
- Configurar `discountType`, `valuePercentage` ou `valueFixed`,
  `discountConditions`, `endsIn`, `link`.
- Componentes por papel: `discount_code` (texto, obrigatório, exatamente
  um), `discount_button` (opcional), `discount_expiration_date`
  (opcional). O texto do `discount_code` usa o **mesmo** placeholder.
- **Loja WooCommerce usa `dynamicDiscount`**, não `discount`. Um bloco
  `discount` numa loja WooCommerce é ignorado no envio e o placeholder vai
  para o destinatário como se fosse o código. Como a Convertfy é Shopify,
  o caso normal é `discount`; confirme antes em loja que não seja Shopify.

A copy escreve a **condição** (valor, prazo, mínimo). O código nasce do
bloco. Ver `skills/email-copy/references/oferta-e-condicao.md`.

## Personalização

Tags conhecidas e documentadas:

| Tag | Uso |
|---|---|
| `[[contact.first_name]]` | Primeiro nome |
| `[[unsubscribe_link]]` | Descadastro. **Obrigatório:** o conteúdo é rejeitado sem ao menos um bloco de texto ou HTML contendo essa tag |
| `[[preference_link]]` | Centro de preferências |

**TODO aberto:** o mecanismo de valor padrão (`default`) para tag de
contato vazia não está documentado na referência consultada. No Klaviyo é
`{{ first_name|default:"there" }}`. Até confirmar, a regra desta skill é
escrever a frase de modo que ela leia bem com o campo vazio, e não
depender de fallback. Ver C47.

## Ordem de trabalho

1. **Ler o brief** em `marcas/<cliente>.md` e a intenção no vault.
2. **Confirmar os eventos da conta** com `post_event_metadata_query`. Não
   assuma que a loja registra `viewed product`: o script de rastreamento
   pode não estar instalado.
3. **Escolher o gatilho, a origem e o filtro de entrada.**
4. **Desenhar os blocos:** atraso, e-mail, split, atraso, e-mail.
5. **Escrever as condições de saída.** Toda automação de abandono sai em
   `placed order`. Nutrição e winback também.
6. **Definir os limitadores:** frequência e sobreposição.
7. **Montar o template** com a seção obrigatória do tipo, e com o bloco
   `discount` se houver oferta.
8. **Chamar `email-copy`** para os campos de texto e `email-design` para o
   HTML.
9. **Criar desabilitada, testar com `test-email`, habilitar.**

## Checklist por flow

- [ ] O evento de gatilho existe na conta (confirmado em
      `post_event_metadata_query`)
- [ ] O primeiro bloco é um `delay`, se a intenção é usar `enrollExisting`
- [ ] Nenhum `delay` é o último bloco
- [ ] `exitConditions` cobre `placed order` em toda automação de abandono
      e de nutrição
- [ ] O template do primeiro e-mail tem a seção obrigatória do tipo
- [ ] Toda oferta está em bloco `discount`, nunca em texto
- [ ] Existe `[[unsubscribe_link]]` no conteúdo
- [ ] `frequencyLimiter` definido, e a decisão está justificada
- [ ] `overlapLimiter` definido quando há flows que colidem
- [ ] Tags UTM definidas por bloco de envio
- [ ] Nenhum TODO de variável sobrou sem virar pergunta ao cliente
- [ ] A automação foi criada desabilitada e testada antes de habilitar

## Convenção de nome

`CVF | <Flow> <n> | <nome curto>`

Exemplos: `CVF | Welcome 1 | Cupom`, `CVF | Carrinho 2 | Prova social`,
`CVF | Winback 3 | Última chamada`.

Em agência com 250+ lojas, o nome é a única coisa que sobrevive à troca de
quem opera a conta.

## Referências

| Arquivo | Quando abrir |
|---|---|
| `references/os-10-flows.md` | Ao montar qualquer flow: gatilho, blocos, atrasos, saídas, conteúdo exigido |
| `references/equivalencia-klaviyo-omnisend.md` | Ao migrar de Klaviyo, ao traduzir uma variável, ou ao consultar os TODOs abertos |
| `skills/email-copy/SKILL.md` | Para os campos de texto |
| `skills/email-design/SKILL.md` | Para o HTML |
| `shared/anti-vicios-copy.md` | Sempre, antes de escrever copy |
