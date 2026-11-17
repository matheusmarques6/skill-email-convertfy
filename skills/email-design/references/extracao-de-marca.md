# Extração de marca: preencher a parte visual da ficha

Detalhe da `email-design`. A ficha da marca (`marcas/<cliente>.md`) é
pré-requisito de geração (P01). Este arquivo diz **de onde tirar** os
campos visuais (tipografia, cor, logo, foto, componentes) e como provar
cada um, sem preencher nada por inferência.

A regra do `_template.md` vale aqui inteira: **campo desconhecido fica
`null`. Um chute faz o gate mentir.**

## As fontes, em ordem de confiança

1. **Design system ou guia de marca enviado pelo cliente.** Vence tudo.
2. **E-mails já aprovados da própria loja** (Figma da Convertfy ou o que a
   loja enviou antes). É o que a lista já reconhece.
3. **O site da loja.** Bom para logo, cor e fonte; ruim para tom (site e
   e-mail falam diferente).
4. **Anúncios e Instagram da loja.** Só para confirmar foto e clima; nunca
   como fonte de cor.

O caso de referência é a Blue Wolf: tipografia e cores foram **contadas nos
frames** dos e-mails de agosto e setembro no Figma
(`07_Design_Blue_Wolf/02_DESIGN_SYSTEM_BLUE_WOLF.md`). A fonte mais usada
virou tipografia principal; a cor mais usada em título e botão virou cor
primária. É o método.

## Passo a passo

### 1. Tipografia

**Do Figma (e-mails aprovados):** liste os estilos de texto dos frames e
conte. A família que mais aparece em corpo, botão e preço é a
**tipografia principal**. A que aparece em título de seção é a **fonte
secundária**. As outras (display de evento, wordmark, apoio) entram na
prosa da ficha como "vive em imagem".

Com o conector do Figma: `get_variable_defs` traz as variáveis e estilos
definidos; `get_design_context` num frame traz as fontes usadas nele. Rode
em 3 a 5 e-mails, não em um.

**Do site:** inspecione o CSS do tema (Shopify: `font-family` do `body` e
dos títulos; variáveis `--font-body-family` e `--font-heading-family` nos
temas Dawn e derivados). Confirme que a fonte é a da marca, não a padrão do
tema.

**Na ficha:**
- `tipografia_principal` e `fonte_secundaria`: os nomes exatos.
- `tipografia_principal_fallback` e `fonte_secundaria_fallback`: pela
  tabela de pilhas de `tipografia.md` (geométrica cai em Century Gothic e
  Arial; serifa em Georgia).
- Na prosa: onde cada uma aparece, onde não aparece, e quais vivem só em
  imagem.

### 2. Cor

**Do Figma:** conte as cores de preenchimento de botão, de título e de
fundo de seção. Ignore cor de foto.

**Do site:** cor do botão de compra ("Adicionar ao carrinho") e do link.
O botão de compra do site é o melhor candidato a cor de ação no e-mail,
porque a lista já associa aquela cor a comprar.

**Antes de gravar, teste** (`cor-e-contraste.md`): com texto branco, a cor
do botão passa 4,5:1? Se não passa, registre na prosa qual texto vai sobre
ela (preto ou branco) e o contraste medido. A Blue Wolf é o exemplo: o azul
aço `#4588B9` da ficha não passa com branco em 16px; passa com preto.

**Na ficha:**
- `usa_cor_de_marca: true` **só se o cliente pediu** cor nos e-mails, ou se
  os e-mails aprovados já usam. Ter cor no site não basta: a casa é neutra
  por padrão.
- `cor_primaria`, `cor_secundaria` em hex.
- `acento_permitido_em`: onde a cor entra. Fundo de seção só se os e-mails
  aprovados usam.
- Paleta por momento: só se o cliente aprovou (é a exceção, não a regra).

### 3. Logo

- Pegue o arquivo vetorial ou PNG grande com o cliente. O logo do site
  (header) serve como provisório, se tiver pelo menos 280px de largura.
- Precisa de **duas versões**: para fundo claro e para fundo escuro. Se a
  loja só tem a escura, registre `[FALTA: logo para fundo escuro]` e use a
  solução de contorno de `dark-mode.md` até chegar.
- Largura de exibição na ficha (120 a 160px) e o arquivo em 2x.

### 4. Foto

- **Shopify expõe o catálogo público.** `https://<loja>/products.json` (30
  por página por padrão, até 250 com `?limit=250`, e `&page=2` para a
  seguinte) e
  `https://<loja>/products/<handle>.json` trazem, por produto: título,
  imagens em resolução máxima, variantes, `price` e `compare_at_price`.
- É a fonte certa para o slot de produto: foto real, preço real, preço
  "de" real (`compare_at_price`). Preço "de" sem `compare_at_price` não
  entra (C02).
- Registre na prosa o estilo da foto da loja: estúdio fundo claro, lifestyle,
  modelo, flat lay. É o que define que requisito do vault (`exige:`) a loja
  atende.
- Avaliações: o app de reviews da loja (Judge.me, Yotpo, Okendo, Loox) é a
  fonte de nota, volume e trechos. Preencha `reviews_disponiveis`,
  `review_com_nome` e `foto_do_depoente` a partir dele. Sem acesso, `null`.

### 5. Componentes que a loja repete

Dos e-mails aprovados, liste o que aparece em todos: cabeçalho, rodapé,
faixa de garantias, botão, caixa de cupom. A Blue Wolf tem doze
(`02_DESIGN_SYSTEM_BLUE_WOLF.md`, "Componentes"). Na ficha, cada um com uma
linha: o que é, onde aparece, e se é imagem ou HTML.

### 6. E-mails da própria loja e de concorrentes

O conector do Trendtrack lê e-mails enviados por lojas (`search_emails`,
`analyze_shop_emails`, `get_email_html`). Serve para duas coisas:

- **A própria loja**, quando ela já enviava e-mail antes da Convertfy: o
  que a lista já está acostumada a ver.
- **Concorrentes do nicho**: referência de estrutura e de oferta, nunca de
  cor ou de fonte. O que vem de concorrente não entra na ficha.

## O que nunca entra na ficha por inferência

- Cor "que combina com o nicho".
- Fonte "parecida com a do logo".
- `usa_cor_de_marca: true` porque o site é colorido.
- Número de avaliações, nota média, prazo de entrega, política de troca
  sem fonte verificável.
- Tom de voz deduzido do site. Tom vem de e-mail aprovado ou do cliente.

## Fecho: validar com o cliente

A ficha nasce com `status: rascunho`. Antes de virar `aprovada`:

1. Mande ao cliente uma peça de teste montada com a ficha (render dos três
   PNGs).
2. Pergunte só o que ficou `null` ou ambíguo. Uma mensagem, uma lista.
3. Registre `revisado_por` e a data. Palavra que o cliente reprovar vai para
   `palavras_proibidas`, com a data.

## Verificação

- [ ] Tipografia principal e fonte secundária com nome exato e fallback?
- [ ] Cada cor com hex, papel e contraste medido com o texto que vai sobre
      ela?
- [ ] `usa_cor_de_marca` justificado por pedido do cliente ou por e-mail
      aprovado?
- [ ] Logo em duas versões, ou a falta registrada?
- [ ] Estilo de foto e fonte do catálogo registrados?
- [ ] Todo campo sem fonte está `null`?
