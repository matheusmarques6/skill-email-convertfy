# Oferta e condição

Detalhe da regra C46. Carregado sob demanda pela `email-copy`.

## A regra

Se há desconto, a copy carrega a condição completa:

**valor** mais **como aplicar** (código ou "aplicado no carrinho") mais
**prazo** (data real ou "por tempo limitado") mais **mínimo**, se houver.

Faltar qualquer parte obrigatória é achado de severidade A no
`lint_copy.py`.

## Por que a condição é uma regra de copy, não de rodapé

Três razões, em ordem de força.

1. **É o que marca grande faz.** No corpus de welcome, a L.L.Bean fecha
   com "One-time-use offer, exclusions apply." A frase de boas-vindas é
   igual à de todo mundo; o que diferencia é a condição clara.
2. **É a defesa contra urgência falsa (C06).** Escrever o prazo real força
   a pergunta "qual é o prazo?". Quando não há prazo, "por tempo limitado"
   é honesto justamente por não afirmar uma data.
3. **É proteção legal.** Oferta com condição escondida é publicidade
   enganosa pelo CDC art. 37. Evidência forte, estatutária.

## As quatro partes

### 1. Valor (obrigatório)

Formas aceitas: `15% OFF`, `R$ 30 OFF`, `frete grátis`, `leve 3 pague 2`.

Nunca: "desconto especial", "condição exclusiva", "preço que você nunca
viu". Superlativo vazio é C20; valor vago é o mesmo vício com outro
disfarce.

### 2. Como aplicar (obrigatório)

Duas formas, e só duas:

- **Código visível.** `BEMVINDO15`. No idioma da loja (C04).
- **A frase "aplicado no carrinho".** Quando a loja aplica o desconto
  automaticamente.

Se você não sabe qual das duas, pergunte. Não escolha por conta própria:
prometer um código que a loja não emitiu gera atendimento e desconfiança.

#### Atenção específica do Omnisend

No Omnisend, **o código de desconto não é texto de copy.** Um bloco
`discount` (ou `dynamicDiscount` em loja WooCommerce) emite um código único
por destinatário no momento do envio, e o placeholder na peça é
`XXXX-XXXX-XXXX`, substituído na hora.

Consequência para a copy:

- A copy escreve a **condição**: valor, prazo, mínimo.
- A copy **não escolhe o código**. O código nasce do bloco.
- Escrever "use o código BEMVINDO15" em bloco de texto cria um código que
  não existe na loja. O destinatário não consegue resgatar.
- A documentação do Omnisend é explícita sobre isso e trata a regra como
  válida para **qualquer** e-mail com oferta, não só automação: welcome,
  aniversário, winback, reativação, abandono que adoça a oferta.

Quando o brief da loja der um código fixo criado à mão no Shopify, aí sim
ele é texto. Confirme com o cliente qual dos dois caminhos a loja usa antes
de escrever.

### 3. Prazo (obrigatório)

Duas formas:

- **Data ou janela real.** "até domingo", "até 30/09", "nas próximas 48
  horas".
- **A frase "por tempo limitado".** Quando não existe prazo definido.

Nunca: "últimas unidades", "estoque acabando", "só hoje" sem que o brief
tenha dito isso. Urgência inventada é C06, severidade B, e a evidência de
que urgência falsa recorrente eleva reclamação e descadastro é moderada a
forte.

O bloco de desconto do Omnisend tem um campo `endsIn` em dias e um
componente opcional `discount_expiration_date`. Quando o brief dá prazo, ele
existe nos dois lugares: na copy e no bloco. Os dois precisam concordar.

### 4. Mínimo (condicional)

Só aparece se existir. Formas: "acima de R$ 100", "em compras a partir de
R$ 150", "válido para o primeiro pedido".

Não invente piso de pedido. Se o brief não deu, a oferta não tem mínimo.

## Formas completas aceitas

Em pt-BR:

- "15% OFF no primeiro pedido, aplicado no carrinho, até domingo."
- "R$ 30 OFF acima de R$ 150. Use BEMVINDO30 até 30/09."
- "Frete grátis por tempo limitado, em pedidos acima de R$ 199."
- "20% OFF em toda a coleção. Código aplicado no carrinho, por tempo
  limitado."

Em inglês, quando a loja é em inglês:

- "15% off your first order, applied at checkout, through Sunday."
- "$30 off orders over $150. Use WELCOME30 by Sep 30."

Observe: nenhuma delas tem travessão, adjetivo ou promessa de sentimento.
São quatro fatos numa frase.

## Formas que o lint reprova

| Copy | Problema |
|---|---|
| "Aproveite nosso desconto imperdível" | Sem valor, sem prazo, superlativo vazio (C20) |
| "15% OFF para você" | Sem como aplicar, sem prazo |
| "Use BEMVINDO15" | Sem valor, sem prazo |
| "30% OFF, últimas unidades" | Escassez sem dado de estoque (C06), sem como aplicar |
| "Oferta especial, corre que acaba" | Nada da condição existe |
| "15% OFF, só para você, seleto grupo" | Exclusividade genérica (C22) |
| "R$30 OFF — até domingo" | Travessão (C01), bloqueia |

## Quando o brief só deu metade

Ordem de ação:

1. **Pergunte uma vez, com as perguntas juntas.** "Qual o prazo do cupom e
   há valor mínimo?" Uma pergunta só, não três rodadas.
2. **Se não houver resposta a tempo,** escreva o que existe e marque o que
   falta: `[FALTA: prazo do cupom]`. O placeholder vai para a entrega e
   vira item de pendência.
3. **Nunca preencha com padrão plausível.** Um "válido por 7 dias" que
   ninguém confirmou é número inventado (C02), severidade B.

## Onde a condição fica na peça

- **Uma linha de texto vivo**, fora de imagem. Oferta só dentro da imagem é
  C42 e D17: o resumidor de IA não lê, o leitor de tela não lê, e o cliente
  com imagem bloqueada não lê.
- Perto do botão, não escondida no rodapé.
- O alt da imagem principal **também** carrega a oferta.
- Negrito só no valor e no código. Negrito pulverizado é C32.
