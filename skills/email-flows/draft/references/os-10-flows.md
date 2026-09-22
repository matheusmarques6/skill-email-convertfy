# Os 10 flows, especificados em Omnisend

Detalhe da `email-flows`. Cada flow traz: gatilho, escopo, filtro de
entrada, blocos, condições de saída, limitadores e a seção de conteúdo
obrigatória.

Origem `shopify` em todos, salvo nota. Os nomes de evento são os reais do
Omnisend. Onde o desenho depende de algo não confirmado, o item está
marcado `TODO` com a referência para
`equivalencia-klaviyo-omnisend.md` §5.

O orçamento de palavras de cada e-mail está em
`skills/email-copy/draft/references/orcamento-de-palavras.md`.

---

## 1. Welcome

**Camada:** entrada, por fonte de captação.
**Gatilho:** `subscribed to marketing`. Não usa `origin`.
**Filtro de entrada:** `trigger.audienceFilterGroup` por `tag` ou
`segmentID` da fonte. Um formulário por tag.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `duration`, 5 a 15 minutos. Existe para permitir `enrollExisting` e para não colidir com o e-mail transacional do formulário |
| 2 | `action.sendEmail` | E-mail 1: entrega o incentivo prometido |
| 3 | `delay` | `duration`, 2 dias |
| 4 | `split` | Filtro de mensagem `clickedEmail` no bloco 2 |
| 5 | `action.sendEmail` | E-mail 2: a loja em uma frase, mais os best-sellers |
| 6 | `delay` | `duration`, 2 dias |
| 7 | `action.sendEmail` | E-mail 3: prova social com números reais do brief |
| 8 | `delay` | `duration`, 3 dias |
| 9 | `action.sendEmail` | E-mail 4: lembrete do cupom, com o prazo |

**Conteúdo obrigatório:** nenhuma seção exigida. **Mas:** se o welcome
oferece desconto, a oferta vai num bloco `discount` com placeholder
`XXXX-XXXX-XXXX`, nunca em texto.

**Condições de saída:** `placed order`. O comprador sai do welcome e entra
no pós-compra.

**Limitadores:** `frequencyLimiter` em `once`. Ninguém entra duas vezes no
welcome da mesma fonte.

**Risco de vício a vigiar:** o repo de origem manda que o último e-mail
seja uma carta do fundador. **Não.** Carta de fundador por decreto é C05 e
C16. Se o brief pedir carta, vira exceção editorial declarada.

---

## 2. Carrinho abandonado

**Camada:** ciclo de vida, universal.
**Gatilho:** `added product to cart`.
**Padrão de abandono:** `trigger.inactivitySettings.duration` de 30 a 60
minutos. Cada novo evento de carrinho reinicia o relógio, que é
exatamente o comportamento desejado: só dispara quando a pessoa parou.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `immediate` (a espera já foi feita pelo `inactivitySettings`) |
| 2 | `action.sendEmail` | E-mail 1: lembrete, **sem desconto** |
| 3 | `delay` | `duration`, 24 horas |
| 4 | `action.sendEmail` | E-mail 2: objeções. Avaliação, frete, troca, garantia |
| 5 | `delay` | `duration`, 24 horas |
| 6 | `split` | Filtro de contato: primeira compra ou recompra |
| 7 | `action.sendEmail` | E-mail 3: incentivo, só se a margem permitir e só para primeira compra |

**Conteúdo obrigatório:** ao menos uma seção `product_cart_recovery` no
template do **primeiro** e-mail. Os itens abandonados do destinatário são
injetados no envio, até 12 blocos `product`.

**Condições de saída:** `started checkout` e `placed order`.

**Limitadores:**
`frequencyLimiter` em `interval`, tipicamente 7 dias, para não perseguir
quem abandona carrinho toda semana.
`overlapLimiter` em `currentlyIn`, listando checkout abandonado.

**Nota de copy:** teto de 60 palavras. A pessoa já quer o produto; lembrar
custa menos palavra que convencer.

**TODO aberto:** T4, o link de recuperação do carrinho como tag de texto.
Enquanto aberto, o link de volta ao carrinho vem do botão dentro da seção
`product_cart_recovery`.

---

## 3. Checkout abandonado

**Camada:** ciclo de vida, universal.
**Gatilho:** `started checkout`.
**Padrão de abandono:** `inactivitySettings` de 30 minutos. Intenção mais
alta, espera mais curta.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `immediate` |
| 2 | `action.sendEmail` | E-mail 1: "algo deu errado?" mais link de retomada |
| 3 | `delay` | `duration`, 6 horas |
| 4 | `action.sendEmail` | E-mail 2: confiança. Pagamento seguro, prazo de entrega, política de troca |
| 5 | `delay` | `duration`, 18 horas |
| 6 | `action.sendEmail` | E-mail 3: última chamada, sem desconto novo |

**Conteúdo obrigatório:** seção `product_cart_recovery` no primeiro
e-mail.

**Condições de saída:** `placed order`.

**Limitadores:** `frequencyLimiter` em `interval` de 7 dias.
`overlapLimiter` em `currentlyIn` listando carrinho abandonado, para a
pessoa não receber os dois.

**Regra de oferta:** não descontar aqui. Quem chegou ao checkout já
aceitou o preço. Descontar treina a base a abandonar.

**TODO aberto:** T5. A origem `api` expõe `abandonedCheckoutURL`; para a
origem `shopify` isso não está confirmado. Confirmar por conta antes de
prometer um botão "retomar meu checkout" em texto.

---

## 4. Navegação abandonada

**Camada:** ciclo de vida, universal.
**Gatilho:** `viewed product`.
**Padrão de abandono:** `inactivitySettings` de 1 a 4 horas.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `immediate` |
| 2 | `action.sendEmail` | E-mail 1: cutucada leve com o produto visto |
| 3 | `delay` | `duration`, 24 horas |
| 4 | `action.sendEmail` | E-mail 2: prova social do produto, mais alternativas |

**Conteúdo obrigatório:** seção `product_cart_recovery` (a documentação a
usa também para abandono de navegação: os produtos vistos são injetados no
envio).

**Condições de saída:** `added product to cart`, `started checkout`,
`placed order`.

**Limitadores:** `frequencyLimiter` em `interval` de 3 a 7 dias. Sem isso,
quem navega muito recebe e-mail todo dia. `overlapLimiter` em
`currentlyIn` listando carrinho e checkout.

**Pré-requisito que quase sempre falta:** `viewed product` só existe se o
script de rastreamento do Omnisend estiver instalado na loja. Confirmar com
`post_event_metadata_query` antes de desenhar o flow. Prometer navegação
abandonada sem o evento é o erro mais comum de onboarding.

---

## 5. Pós-compra

**Camada:** ciclo de vida, universal.
**Gatilho:** `placed order` ou `paid for order`. Prefira `paid for order`
quando a loja tem pagamento por boleto ou pix, para não agradecer por um
pedido que não foi pago.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `immediate` |
| 2 | `action.sendEmail` | E-mail 1: agradecimento e o que esperar. **Sem venda** |
| 3 | `delay` | `duration`, 3 dias |
| 4 | `action.sendEmail` | E-mail 2: como usar, cuidados, dicas |
| 5 | `delay` | `duration`, 11 dias |
| 6 | `split` | Filtro de contato: primeira compra ou recompra |
| 7 | `action.sendEmail` | E-mail 3: cross-sell |

**Conteúdo obrigatório:**
- Se o e-mail 1 for confirmação de pedido de fato: blocos `orderSummary`,
  `orderProducts` e `orderTotal`, os três.
- Se houver e-mail de confirmação de envio (gatilho `order fulfilled`):
  os três acima **mais** `orderAddresses`.
- No e-mail de cross-sell: seção `product_recommender`, com
  `fallbackType` explícito. Ver a armadilha do plano Pro em
  `equivalencia-klaviyo-omnisend.md` §3.6.

**Condições de saída:** nenhuma obrigatória. Um novo `placed order`
reinicia o flow se o `frequencyLimiter` permitir.

**Limitadores:** `frequencyLimiter` em `interval` de 14 a 30 dias, para
quem compra duas vezes na mesma semana não receber dois "obrigado".

---

## 6. Nutrição

**Camada:** entrada, por fonte de captação.
**Gatilho:** `subscribed to marketing`, com o mesmo filtro de audiência do
welcome.
**Público real:** quem terminou o welcome e não comprou.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `duration`, 14 dias. Deixa o welcome terminar |
| 2 | `action.sendEmail` | E-mail 1: o problema que o produto resolve |
| 3 | `delay` | `duration`, 2 dias |
| 4 | `action.sendEmail` | E-mail 2: prova social |
| 5 | `delay` | `duration`, 2 dias |
| 6 | `action.sendEmail` | E-mail 3: best-sellers |
| 7 | `delay` | `duration`, 3 dias |
| 8 | `action.sendEmail` | E-mail 4: última chamada, referenciando o cupom do welcome |

**Conteúdo obrigatório:** nenhum. Se houver oferta, bloco `discount`.

**Condições de saída:** `placed order`. Obrigatória: mandar nutrição para
quem comprou é o erro que mais gera reclamação.

**Limitadores:** `frequencyLimiter` em `once`.
`overlapLimiter` em `currentlyIn` listando o welcome da mesma fonte.

**Regra de oferta:** referenciar o cupom do welcome, **nunca empilhar um
segundo desconto**. Dois cupons vivos ao mesmo tempo treinam a base a
esperar.

**Risco de vício a vigiar:** o repo de origem manda "cobrir os 5 pilares de
conteúdo". Isso produz e-mail de enchimento para bater cota. O critério
correto é o inverso: **corte o e-mail que não tem nada novo para dizer.**
Quatro e-mails com fato batem seis com tema.

---

## 7. Winback

**Camada:** ciclo de vida, universal.
**Gatilho:** `entered segment`, com `origin: omnisend` e filtro de evento
em `segment_id`.

**O segmento:** contatos com `placed order` usando `notInTheLast` de 60 a
90 dias, e `subscriptionStatus` igual a `subscribed` no canal `email`.

Alternativa mais simples, que o Omnisend calcula sozinho: a propriedade
de contato `customerLifecycleStage` com valor `atRisk`, `aboutToLose` ou
`cantLose`. Verificar qual dos dois desenhos a loja prefere, porque o RFM
calculado é opaco para o cliente e a regra explícita é auditável.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `immediate` |
| 2 | `action.sendEmail` | E-mail 1: o que mudou na loja. **Sem desconto** |
| 3 | `delay` | `duration`, 5 dias |
| 4 | `action.sendEmail` | E-mail 2: incentivo |
| 5 | `delay` | `duration`, 5 dias |
| 6 | `action.sendEmail` | E-mail 3: última chamada com o incentivo maior |

**Conteúdo obrigatório:** nenhum. Bloco `discount` nos e-mails 2 e 3.

**Condições de saída:** `placed order`.

**Limitadores:** `frequencyLimiter` em `interval` de 180 dias.

**Nota de copy:** reconhecer o intervalo custa uma linha, não um
parágrafo. Nada de "sentimos sua falta" seguido de três frases sobre o que
a relação significa.

**TODO:** confirmar se `entered segment` com `enrollExisting` funciona
mais de uma vez. A documentação diz que só funciona na primeira habilitação
e que reabilitar com `enrollExisting=true` retorna
`409 enroll-existing-not-applicable`.

---

## 8. Reposição

**Camada:** ciclo de vida, universal. Só faz sentido para produto de
consumo (suplemento, cosmético, café, ração).

**Gatilho:** **TODO (T7).** Não há gatilho documentado de "N dias desde o
último pedido". O desenho recomendado enquanto isso não fecha:
`entered segment`, com um segmento de `ordered product` do SKU relevante
usando `notInTheLast` no ciclo de consumo do produto.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `immediate` |
| 2 | `action.sendEmail` | E-mail 1: hora de repor, recompra em um clique |
| 3 | `delay` | `duration`, 7 dias |
| 4 | `action.sendEmail` | E-mail 2: última chamada, com assinatura como alternativa |

**Conteúdo obrigatório:** seção `product_recommender` (a documentação
lista reposição como um dos tipos que a exige), com `fallbackType`
explícito e `purchaseExclusionDays` configurado para não recomendar o que
a pessoa acabou de comprar.

**Ciclos de consumo, direcionais:** suplemento 25 a 30 dias, cosmético 45
a 60, café ou chá 14 a 21, ração 21 a 30. **Confirme com o cliente.** O
ciclo verdadeiro está no histórico de recompra da loja, não numa tabela.

**Condições de saída:** `placed order`.

---

## 9. Sunset

**Camada:** ciclo de vida, universal.
**Gatilho:** `entered segment`.

**O segmento:** contatos sem `opened message` nem `clicked message` usando
`notInTheLast` de 120 a 180 dias, e `subscriptionStatus` igual a
`subscribed`.

**TODO:** confirmar os nomes exatos dos eventos de engajamento na conta
(a documentação de segmentos cita `"opened message"` como exemplo).
Verificar com `post_event_metadata_query`.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `immediate` |
| 2 | `action.sendEmail` | E-mail 1: "ainda quer receber?" com dois botões |
| 3 | `delay` | `duration`, 7 dias |
| 4 | `split` | Filtro de mensagem `clickedEmail` no bloco 2 |
| 5 | `action.sendEmail` | E-mail 2: última chamada com o descadastro em destaque |
| 6 | `action.addTag` | Tag `sunset-sem-resposta`, para suprimir por segmento |

**Teto de copy: 40 palavras.** Uma pergunta e dois botões.

**Condições de saída:** `placed order`.

**Por que este flow existe:** não é receita, é proteção. Lista
desengajada derruba a entregabilidade de todo o resto. O envio por camada
de engajamento é a alavanca de maior impacto documentada.

**Atenção:** o Omnisend não tem ação de suprimir contato dentro do
workflow. A tag no bloco 6 é o mecanismo: um segmento de exclusão lê a tag
e é aplicado em toda campanha. Isso **precisa** virar item de checklist do
calendário de campanha, senão o flow não faz nada.

---

## 10. Pedido de avaliação

**Camada:** ciclo de vida, universal.
**Gatilho:** `order fulfilled`.

| Bloco | Tipo | Configuração |
|---|---|---|
| 1 | `delay` | `duration`, 7 a 21 dias, conforme o produto |
| 2 | `action.sendEmail` | E-mail 1: pedido de avaliação, link direto para o formulário |
| 3 | `delay` | `duration`, 7 dias |
| 4 | `split` | Filtro de mensagem `clickedEmail` no bloco 2 |
| 5 | `action.sendEmail` | E-mail 2: lembrete curto |

**Teto de copy: 40 palavras.** Um pedido, um link.

**Timing por tipo de produto:** o produto precisa ter sido usado. Roupa
ou acessório: 7 dias depois da entrega. Suplemento ou cosmético: 14 a 21
dias. Eletrônico: 10 a 14.

Vale usar `fulfillment.shipment_status` num filtro de evento para só
disparar quando o status indicar entrega, e não apenas despacho.
**TODO:** confirmar os valores possíveis desse campo na conta.

**Condições de saída:** nenhuma obrigatória.

**Limitadores:** `frequencyLimiter` em `interval` de 60 dias, para quem
compra todo mês não receber um pedido de avaliação por mês.

---

## Matriz de colisão

O que acontece quando o contato está num flow e dispara outro.

| Está em | Dispara | O que acontece |
|---|---|---|
| Welcome | Navegação abandonada | Os dois rodam. Controlar com `overlapLimiter` |
| Welcome | Carrinho abandonado | Os dois rodam. O carrinho tem prioridade: listar o welcome no `overlapLimiter` do carrinho é o inverso do desejado, então prefira controlar pelo lado da navegação |
| Navegação abandonada | Carrinho abandonado | Navegação **sai**, por `exitConditions` em `added product to cart` |
| Carrinho abandonado | Checkout abandonado | Carrinho **sai**, por `exitConditions` em `started checkout` |
| Qualquer abandono | `placed order` | Todos **saem**. Pós-compra entra |
| Nutrição | `placed order` | Nutrição **sai**. Pós-compra entra |
| Winback | `placed order` | Winback **sai** |
| Pós-compra | Navegação abandonada | Os dois rodam. `overlapLimiter` em `currentlyIn` |
| Sunset | Qualquer engajamento | Sai pelo split do bloco 4 |

Princípio por trás: **intenção mais alta ganha.** Checkout acima de
carrinho, carrinho acima de navegação, compra acima de tudo.

## Regra de ouro dos descontos empilhados

Se o welcome oferece 15%, o carrinho abandonado **referencia o mesmo
cupom**, não cria um segundo. Dois cupons vivos ao mesmo tempo é o que
treina a base a nunca comprar a preço cheio, e é o que mais aparece em
auditoria de conta herdada.
