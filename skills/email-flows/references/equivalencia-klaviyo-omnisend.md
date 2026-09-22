# Equivalência Klaviyo ↔ Omnisend

Referência de tradução. O Omnisend é o ESP principal da Convertfy; o
Klaviyo é o secundário, então a coluna original fica, não é apagada.

Fonte do lado Omnisend: documentação oficial da API consultada pelo MCP em
22/09/2026 (tópicos `automations`, `automation_content`, `email_content`,
`segments`). Fonte do lado Klaviyo:
`vendor/email-campaign-skill/docs/flows/KLAVIYO-DYNAMIC-VARIABLES.md`,
MIT, reescrito.

**Regra de ouro:** onde a coluna Omnisend diz `TODO`, escreva `TODO` na
peça, com a variável Klaviyo entre parênteses. Nome inventado renderiza
vazio para a lista inteira.

---

## 1. Conceitos de arquitetura

| Klaviyo | Omnisend | Nota |
|---|---|---|
| Flow | Automation (workflow) | Nasce desabilitada; `isEnabled` é somente leitura |
| Flow trigger | `trigger.condition.event` mais `origin` | `origin` costuma ser `shopify` e o Omnisend resolve sozinho quando só há uma |
| Trigger filter | `trigger.condition.filterGroups` | A maioria dos eventos aceita no máximo um grupo. `subscribed to marketing` aceita até 10, com AND |
| Flow filter ("skip if true") | `exitConditions` | **Mais forte:** o Klaviyo pula a mensagem, o Omnisend remove o contato da automação |
| Flow entry filter por lista ou segmento | `trigger.audienceFilterGroup` | Não dispara, só decide quem entra |
| Time Delay | Bloco `delay`, modo `duration` | Unidades `m`, `h`, `d`, `w`, `M` |
| Delay until specific time | Bloco `delay`, modo `specificTime` | `time` em HH:MM, fuso da marca |
| Conditional Split | Bloco `split` com `filterGroup` | Filtros de evento, de contato ou de mensagem |
| A/B split dentro do flow | Bloco `abTesting` | Só `aBlocksPercentage` é editável por PATCH |
| Email action | `action.sendEmail` com `templateID` | |
| SMS action | `action.sendSms` | |
| Update profile property | `action.addTag` ou `action.removeTag` | O Omnisend não tem ação de escrever propriedade arbitrária no contato dentro do workflow. **TODO: confirmar** |
| Webhook action | `action.sendWebhook` | |
| **Smart Sending (janela de 16h)** | **Não existe equivalente idêntico** | Ver abaixo |
| Flow filter por compra desde a entrada | `exitConditions` com `placed order` | |
| Suppression / sunset | Segmento mais gatilho `entered segment` | |

### Smart Sending: a lacuna real

| Klaviyo | Omnisend mais próximo | O que não cobre |
|---|---|---|
| Smart Sending, 16h entre **qualquer** duas mensagens ao mesmo contato, flow ou campanha | `settings.frequencyLimiter`: `once` ou `interval` com duração em h, d ou w (máx. 8760h, 365d, 52 semanas) | Só controla **reentrada nesta automação**. Não olha outras automações nem campanhas |
| idem | `settings.overlapLimiter`: `currentlyIn` (pula se ativo em automações listadas) ou `recentlyIn` (pula se concluiu alguma nos últimos 1 a 7 dias, via `withinDays`) | Não cobre campanha manual. Auto-referência (listar o próprio ID) é rejeitada com 400 |

**Consequência operacional:** no Omnisend, evitar que um contato receba um
flow e uma campanha no mesmo dia é responsabilidade do calendário de
campanha, não da plataforma. Isso vira item de risco na auditoria.

---

## 2. Eventos de gatilho

Nomes reais, confirmados na documentação. Origem `shopify` salvo nota.

| Gatilho Klaviyo | Evento Omnisend | Confirmado? |
|---|---|---|
| Added to List | `subscribed to marketing` | Sim. Não usa `origin` |
| Viewed Product | `viewed product` | Sim |
| Added to Cart | `added product to cart` | Sim |
| Started Checkout | `started checkout` | Sim |
| Placed Order | `placed order` | Sim |
| Ordered Product | `ordered product` | Sim |
| (pagamento) | `paid for order` | Sim. Não tem equivalente direto nomeado no Klaviyo |
| Fulfilled Order | `order fulfilled` | Sim |
| Cancelled Order | `order canceled` | Sim |
| Refunded Order | `order refunded` | Sim |
| Birthday (data no perfil) | `birthday` | Sim. Formato de filtro próprio. Não pode ser condição de saída |
| Back in Stock | `product back in stock` | Sim. Shopify, BigCommerce e WooCommerce. Não aceita `filterGroups`. Não pode ser condição de saída |
| Segment entry | `entered segment`, com `origin: omnisend` e filtro de evento em `segment_id` | Sim |
| Date property (aniversário de compra, etc.) | TODO: não há gatilho de data arbitrária documentado além de `birthday` | Usar `entered segment` com segmento por `anniversaryIsInTheNext` |
| "X dias desde a última compra" (reposição) | TODO: não há gatilho de tempo-desde-evento documentado | Usar `entered segment` com segmento por `notInTheLast` |

**Sempre confirme na conta** com `post_event_metadata_query`. O documento
lista o que o Omnisend suporta; a conta lista o que a loja de fato
registra. `viewed product` só existe se o script de rastreamento estiver
instalado.

---

## 3. Variáveis dinâmicas: a tradução que não é um para um

**Esta é a parte mais importante desta referência.**

No Klaviyo, o dado do evento entra na peça como merge tag de texto:
`{{ event.ProductName }}`. **O Omnisend funciona diferente na
abandonagem:** os produtos são injetados por **seção de conteúdo**, não por
merge tag. A documentação é explícita: numa seção
`product_cart_recovery`, cada bloco `product` é um slot que a plataforma
preenche com um produto personalizado por destinatário no momento do envio.

Portanto:

- **Não procure o equivalente de `{{ event.ProductName }}`.** Na maior
  parte dos casos ele não é uma tag: é a seção certa no template.
- Os caminhos de propriedade da tabela abaixo estão documentados **para
  segmentação e para filtros de evento** (em `split` e `exitConditions`).
  Se eles funcionam também como merge tag dentro de um bloco de texto é
  **algo que a documentação consultada não afirma**. Está na lista de
  TODOs.

### 3.1 Perfil e sistema

| Klaviyo | Omnisend | Confirmado? |
|---|---|---|
| `{{ first_name }}` | `[[contact.first_name]]` | Sim |
| `{{ last_name }}` | TODO (Klaviyo: `{{ last_name }}`). Provável `[[contact.last_name]]`, **não confirmado** | Não |
| `{{ email }}` | TODO (Klaviyo: `{{ email }}`) | Não |
| `{{ city }}`, `{{ region }}`, `{{ country }}` | TODO (Klaviyo: `{{ city }}` etc.). Os campos existem como propriedade de contato em segmentação (`city`, `state`, `country`) | Não como tag |
| `{{ unsubscribe_url }}` | `[[unsubscribe_link]]` | Sim. **Obrigatório** no conteúdo |
| `{{ manage_preferences_url }}` | `[[preference_link]]` | Sim |
| `{{ browser_url }}` ("ver no navegador") | Seção de tipo `preheader` ou bloco `preheader`. Só em conteúdo de campanha | Sim, mas é seção, não tag |
| `{{ organization_name }}` | TODO (Klaviyo: `{{ organization_name }}`) | Não |
| `{{ first_name\|default:"there" }}` | **TODO: mecanismo de valor padrão não documentado** | Não. Ver §5 |

### 3.2 Navegação abandonada (`viewed product`, origem shopify)

| Klaviyo | Caminho de propriedade Omnisend | Serve para |
|---|---|---|
| `{{ event.ProductName }}` | `product.title` | Segmentação e filtro. Como tag: TODO |
| `{{ event.ProductURL }}` | `page.url` | idem |
| `{{ event.ProductImageURL }}` | TODO (Klaviyo: `{{ event.ProductImageURL }}`) | Usar seção `product_cart_recovery` |
| `{{ event.Price }}` | `product._price` | Segmentação e filtro. Como tag: TODO |
| `{{ event.Categories }}` | `product.categories.[].title` | idem |
| `{{ event.extra.ProductID }}` | `product.id` | idem |

### 3.3 Carrinho abandonado (`added product to cart`, origem shopify)

| Klaviyo | Caminho de propriedade Omnisend | Serve para |
|---|---|---|
| `{{ event.ProductName }}` | `added_item.product_title` | Segmentação e filtro. Como tag: TODO |
| `{{ event.ProductURL }}` | `added_item.product.product_url` | idem |
| `{{ event.Categories }}` | `added_item.product.collections.[].title` | idem |
| (tags do produto) | `added_item.product.tags` | idem |
| `{{ event.extra.CartTotal }}` | TODO (Klaviyo: `{{ event.extra.CartTotal }}`) | Não listado nas 7 propriedades principais de `added product to cart` no Shopify |
| `{{ event.extra.CartURL }}` | TODO (Klaviyo: `{{ event.extra.CartURL }}`) | O link de recuperação vem da seção `product_cart_recovery` |
| `{{ event.extra.CartItems }}` (laço) | **Seção `product_cart_recovery`**, até 12 blocos `product` | Não é laço: é seção |
| `{{ event.Quantity }}` | TODO (Klaviyo: `{{ event.Quantity }}`) | Não |

### 3.4 Checkout abandonado (`started checkout`, origem shopify)

| Klaviyo | Caminho de propriedade Omnisend | Serve para |
|---|---|---|
| `{{ event.extra.CheckoutURL }}` | Origem `api` expõe `abandonedCheckoutURL`. Para origem `shopify`, **TODO** (Klaviyo: `{{ event.extra.CheckoutURL }}`) | Confirmar por conta |
| `{{ event.extra.CartTotal }}` | `raw._subtotal_price` ou `raw._total_line_items_price` | Segmentação e filtro. Como tag: TODO |
| `{{ event.extra.CartItems }}` | `raw.line_items.[].title`, e **seção `product_cart_recovery`** para exibir | |
| `{{ event.extra.ShippingTotal }}` | TODO (Klaviyo: `{{ event.extra.ShippingTotal }}`) | Não |
| `{{ event.extra.DiscountCode }}` | TODO (Klaviyo: `{{ event.extra.DiscountCode }}`) | Não |

### 3.5 Pós-compra (`placed order` e `order fulfilled`, origem shopify)

| Klaviyo | Omnisend | Serve para |
|---|---|---|
| `{{ event.OrderId }}` | Bloco `orderSummary` no template | Bloco, não tag |
| `{{ event.Value }}` | `raw._total_price`, e bloco `orderTotal` para exibir | |
| `{{ event.ItemCount }}` | TODO (Klaviyo: `{{ event.ItemCount }}`) | Bloco `orderProducts` exibe a lista |
| `{{ event.DiscountCode }}` | `raw.discount_applications.[].code` (visto em `order canceled`). Para `placed order`: **TODO** | |
| `{{ event.Currency }}` | TODO (Klaviyo: `{{ event.Currency }}`) | |
| Laço `{% for item in ... %}` com `item.ProductName`, `item.Price`, `item.Quantity`, `item.SKU` | Blocos `orderProducts` e `orderTotal`, ou seção `dynamic_list` configurada por `dynamicList` nas `settings` da seção | Não é laço Django |
| (status de envio) | `fulfillment.shipment_status` | Segmentação e filtro |
| (endereço de entrega) | Bloco `orderAddresses` | Obrigatório em confirmação de envio |

### 3.6 Recomendação de produto

O Klaviyo resolve com bloco de catálogo. No Omnisend é uma seção
`product_recommender` com um objeto `productRecommender` configurando a
estratégia:

| Estratégia | O que faz | Plano |
|---|---|---|
| `newest` | Produtos adicionados mais recentemente | Todos |
| `popular` | Mais vendidos | Todos |
| `mostViewed` | Mais vistos entre todos os destinatários | Todos |
| `personalized` | Similares às compras anteriores do destinatário | Pro |
| `recentlyViewed` | Produtos que o destinatário viu | Pro |

Armadilha registrada na documentação: numa conta **sem** o recurso Pro, a
API aceita `personalized` e `recentlyViewed` **sem erro** e troca
silenciosamente pelo `fallbackType` no envio. Se o `fallbackType` também
for personalizado, cai em `newest`. **Sempre defina `fallbackType`
explicitamente**, e não prometa recomendação personalizada ao cliente sem
confirmar o plano da conta.

Filtros disponíveis na seção: `isOutOfStockIncluded`, `includeCategories`,
`excludeCategories`, `excludeProducts`, `purchaseExclusionDays`,
`recencyMonths`, `priceFrom`.

### 3.7 Desconto

| Klaviyo | Omnisend |
|---|---|
| Código estático escrito na copy, ou cupom dinâmico de catálogo | Bloco `discount` com `code: "XXXX-XXXX-XXXX"`, substituído por um código único por destinatário no envio |
| (WooCommerce) | Bloco `dynamicDiscount`. O `discount_button` passa de opcional a obrigatório |

Componentes por papel: `discount_code` (texto, obrigatório, exatamente
um, com o mesmo placeholder), `discount_button` (botão), e
`discount_expiration_date` (texto).

---

## 4. Segmentação: propriedades de contato úteis

O Omnisend expõe propriedades calculadas que o desenho de winback e de
sunset aproveita, e que dispensam construir a conta de dias na mão:

| Propriedade | Tipo | Uso |
|---|---|---|
| `customerLifecycleStage` | texto (RFM) | `champions`, `loyalists`, `cantLose`, `atRisk`, `highPotential`, `needNurturing`, `aboutToLose`, `recentCustomers` |
| `totalSpent` | número | VIP, faixa de gasto |
| `averageOrderValue` | número | Faixa de ticket |
| `dateAdded` | data | Idade na base |
| `subscriptionStatus` mais `channels` | status | `subscribed`, `unsubscribed`, `nonSubscribed` por canal |
| `tags` | lista | Fonte de captação |
| `birthday` | variádica | Gatilho `birthday` |

Operadores de período em filtro de evento: `inTheLast`, `notInTheLast`,
`anniversaryIsInTheNext` (com `value` e `unit` em days, weeks, months,
years), mais `equals`, `before`, `after`, `between` com data ISO.

`notInTheLast` é o operador que faz winback e sunset: "não tem
`placed order` nos últimos 90 dias".

Limites: 1.000 segmentos por marca, 10 grupos de regra por segmento, 9
filtros por condição.

---

## 5. TODOs abertos

Lista viva. Cada item precisa ser fechado no painel do Omnisend ou com o
suporte deles.

**Estado de T1, T3, T4 e T5: `nao verificado`.** Nenhum foi testado em
conta real. Enquanto estiverem assim, valem os fallbacks da seção
"Não verificado no Omnisend" do `SKILL.md`, e nenhum nome de variavel
pode ser inventado para fecha-los.

Para fechar: `docs/omnisend/roteiro-de-teste.md`. Registro em
`docs/omnisend/verificado.md`. Chamado pronto em
`docs/omnisend/perguntas-suporte.md`.

| # | Pergunta | Variável Klaviyo original | Impacto se ficar aberto |
|---|---|---|---|
| T1 | Existe mecanismo de valor padrão para tag de contato vazia? | `{{ first_name\|default:"there" }}` | Alto. C47 depende disso. Enquanto aberto, escrever frase que funciona sem o nome |
| T2 | Qual a sintaxe de tag para sobrenome, e-mail, cidade, estado, país? | `{{ last_name }}`, `{{ email }}`, `{{ city }}` | Médio |
| T3 | Propriedade de evento pode ser usada como merge tag em bloco de texto, ou só em filtro e segmento? | `{{ event.ProductName }}` | **Alto.** Define se dá para escrever "ainda pensando na Camiseta Pima?" ou se o nome do produto só aparece dentro do bloco de produto |
| T4 | Qual a tag do link de recuperação de carrinho na origem `shopify`? | `{{ event.extra.CartURL }}` | Alto para carrinho abandonado |
| T5 | Qual a tag do link de retomada de checkout na origem `shopify`? A origem `api` tem `abandonedCheckoutURL` | `{{ event.extra.CheckoutURL }}` | Alto para checkout abandonado |
| T6 | Qual a propriedade de total do carrinho em `added product to cart` na origem shopify? | `{{ event.extra.CartTotal }}` | Médio. Usado no split "carrinho acima de X" |
| T7 | Existe gatilho de "N dias desde o último pedido" sem passar por segmento? | (reposição no Klaviyo é gatilho de data) | Médio. Enquanto aberto, usar `entered segment` com `notInTheLast` |
| T8 | Existe ação de escrever propriedade de contato dentro do workflow, além de tag? | "Update profile property" | Baixo. `addTag` resolve a maioria dos casos |
| T9 | Qual o comportamento de `product_cart_recovery` quando o carrinho tem mais de 12 itens? | (Klaviyo itera a lista inteira) | Baixo |
| T10 | Qual o nome do evento e o caminho de propriedade em loja que não é Shopify na carteira? | | Baixo hoje, alto se entrar loja WooCommerce |

## 6. O que não traduzir

Coisas do Klaviyo que **não** devem ganhar equivalente porque o problema
não existe no Omnisend:

- **Limitações da API do Klaviyo** ("a API não cria flows"). O Omnisend
  cria automação por API: `post_automations`.
- **Naming convention ligada ao upload de template** (`POST /api/templates/`
  e depois atribuir na UI). No Omnisend, `post_email_templates` mais
  `templateID` no bloco `sendEmail`.
- **CDN do Klaviyo para imagem.** No Omnisend, `post_images` (por URL) ou
  `post_images_upload` (arquivo).
