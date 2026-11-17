# Direção de imagem por slot

Detalhe da `email-design`. Fecha a lacuna 3 de `docs/lacunas-priorizadas.md`
("o hero é o que mais pesa, e a suíte não produz brief de imagem"). Para
cada slot de imagem: a proporção, o tamanho de exportação, o peso, o que
pode e o que não pode ter dentro, e um brief pronto para foto ou para
geração.

Fontes: estratégia de imagem do `taste-skill` (imagem real antes de
ilustração, nunca "screenshot falso" de div), requisitos fotográficos do
vault (`componentes/requisitos/`: `foto-estudio-fundo-claro`,
`foto-monocromatica`, `macro-de-produto`, `foto-com-pessoas`,
`foto-de-campanha-propria`), procedimento de upload do Max (vault,
`Conhecimento/Advisors/Max/design/upload-do-design.md`), a direção de arte
real da Blue Wolf (`fontes/BFCM-2026-Convertfy/07_Design_Blue_Wolf/`) e D15,
D17, D21, V02.

## As quatro regras que valem para toda imagem

1. **Foto real da loja primeiro.** Foto de produto do site, foto de
   campanha da marca, foto de cliente com permissão. Imagem gerada por IA só
   com aprovação no brief (D15), e nunca para o produto em si (a IA inventa
   detalhe do produto: costura, rótulo, cor).
2. **Nada essencial só dentro da imagem.** Oferta, código, prazo e preço
   existem em texto vivo (V02, D17). A imagem ilustra; o texto informa.
3. **Imagem grande sempre linkada** ao destino do bloco (D21): hero para o
   CTA, foto de produto para o produto. O lint avisa.
4. **Alt decidido:** descritivo e com a oferta quando a imagem carrega
   sentido; `alt=""` quando é decorativa. Nunca ausente.

## Tabela de slots

| Slot | Proporção | Exibe a | Exportar a (2x) | Peso máximo | Formato |
|---|---|---|---|---|---|
| Logo | livre, larga | 120 a 160px de largura | 240 a 320px | 20 KB | PNG (transparente só com prova de dark mode) |
| Hero, foto | **4:3** (padrão) ou 3:2 | 600 x 450 | 1200 x 900 | 200 KB | JPG qualidade 75 a 82 |
| Hero, foto vertical | 4:5 | 600 x 750 | 1200 x 1500 | 200 KB | JPG. **Empurra o botão para fora da dobra no celular**: só com hero sem texto acima |
| Hero de fundo com texto vivo | 600 x altura do bloco | 600 x 440 | 1200 x 880 | 200 KB | JPG, já escurecido no arquivo onde vai o texto |
| Produto em destaque | 1:1 ou 4:5 | 536 | 1072 | 150 KB | JPG |
| Produto em grade | **1:1, igual em todos** | 260 x 260 | 520 x 520 | 80 KB cada | JPG |
| Produto em linha | 1:1 | 176 x 176 | 352 x 352 | 40 KB | JPG |
| Faixa de largura total (lifestyle, banner de coleção) | 2:1 ou 3:1 | 600 x 300 | 1200 x 600 | 150 KB | JPG |
| GIF de produto ou contagem | livre | até 600 de largura | 1x ou 2x conforme o peso | **1 MB** | GIF (ver `movimento-e-gif.md`) |
| Ícone de garantia ou social | 1:1 | 24 a 32px | 48 a 64px | 5 KB | PNG |

Teto do e-mail inteiro: **800 KB de imagem** (`SKILL.md`, item 4). Uma peça
com hero, produto em destaque e grade de 4 já usa cerca de 670 KB nos tetos
acima: não sobra para GIF.

### Por que 2x

A tela do celular tem densidade de 2 a 3 pixels por ponto. Uma imagem
exportada no tamanho exato em que aparece (600px) fica borrada no iPhone.
Exportar no dobro e declarar a largura de exibição no HTML
(`width="600"` mais `style="width:100%;max-width:600px"`) resolve. O Max
exporta em 2x pelo mesmo motivo ("I like to export on 2x quality").

### Por que todas as fotos da grade na mesma proporção

O Gmail ignora `object-fit`. Se uma foto é 1:1 e a vizinha é 4:5, os cards
ficam com altura diferente e os preços desalinham (D25, R20). O único jeito
garantido é **recortar todas na mesma proporção antes do upload**, com o
produto centralizado e a mesma margem em volta.

## O que pode ter dentro da imagem

| Pode | Não pode |
|---|---|
| O produto, a pessoa, a cena | O preço, como única ocorrência |
| Um título de campanha em fonte da marca, **repetido em texto vivo ou no alt** | O código do cupom, como única ocorrência |
| Selo gráfico da marca (o 10/10 da Blue Wolf) | O botão (botão é HTML: E_CTA_IMAGEM, A) |
| Mockup de celular, convite, notificação, quando é o conceito da peça | Texto de corpo (parágrafo) |
| Texto grande o bastante para o celular (tabela em `tipografia.md`) | Texto de 16px desenhado a 600px: vira 9px no celular |

O mockup de celular, de convite ou de notificação (a Blue Wolf usa oito) é
legítimo **quando a ideia da peça é ele**. Não é o "screenshot falso feito
de div" que o `taste-skill` proíbe: é uma imagem desenhada, com o texto do
mockup repetido em texto vivo logo abaixo, quando carrega oferta.

## Direção fotográfica

O vault declara requisitos por variante (`exige:`). Antes de pedir foto,
leia o `exige` da variante escolhida. Os tipos:

| Requisito do vault | Como é | Quando funciona |
|---|---|---|
| `foto-estudio-fundo-claro` | Produto sozinho, fundo branco ou cinza muito claro, luz difusa, sombra suave | Grade, produto em destaque, carrinho. É o padrão de e-commerce e o que mais sobrevive em qualquer bloco |
| `foto-monocromatica` | Produto e fundo na mesma família de cor | Hero editorial, lançamento de cor nova |
| `macro-de-produto` | Detalhe: textura, costura, fecho, ingrediente | Bloco de mecanismo ("por que é diferente"), body |
| `foto-com-pessoas` | Produto em uso, pessoa real | Hero de coleção, prova social |
| `foto-de-campanha-propria` | A campanha que a marca já fotografou | Hero de data (Black Friday, Natal) |

### Para o hero, em especial

O hero é 75% do esforço (Max). A foto do hero:

- Tem **um assunto**. Produto ou pessoa usando o produto. Não uma mesa
  com sete objetos.
- Deixa o assunto no **terço de cima ou no centro**. Embaixo, a foto
  encolhe no celular e o assunto vira detalhe.
- Tem **área de respiro** se for receber texto por cima (módulo 3): um
  terço liso, sem detalhe, onde o texto senta.
- Conversa com a oferta. Hero de "20% em casacos" mostra casaco, não uma
  paisagem de inverno.

## Brief de imagem: o formato

Para cada slot que precisa de imagem nova, o agente entrega um brief neste
formato, junto da peça. É o que a pessoa da loja ou o designer usa para
fotografar, recortar ou gerar.

```
Slot: <hero | produto-destaque | grade-1..4 | faixa | ...>
Proporção e exportação: <4:3, 1200 x 900, JPG até 200 KB>
Assunto: <o produto X, na cor Y; ou: pessoa usando X em Z>
Fonte: <foto do site em <url> | foto da campanha <nome> | gerar>
Enquadramento: <produto centralizado, 15% de margem; assunto no terço de cima>
Fundo e luz: <fundo branco liso, luz difusa de cima | cena externa, fim de tarde>
Área livre: <terço de baixo liso para texto | nenhuma>
Não pode: <texto dentro, outros produtos, marca d'água, modelo diferente da cor do brief>
Alt: <texto do alt, com a oferta quando o slot carrega sentido>
```

### Quando a imagem vai ser gerada

Só com `aprovação de imagem gerada` no brief (D15). O prompt sai do brief
acima, com três travas que o modelo de imagem precisa receber:

1. **A foto real do produto como referência.** Sem referência, o modelo
   inventa o produto. O que se gera é o fundo, a cena, a luz, nunca o
   produto do zero.
2. **"Sem texto na imagem".** O texto entra em HTML.
3. **A proporção exata do slot.** Gerar 1:1 e cortar para 4:3 perde o
   enquadramento.

Modelo de prompt (adaptar à ferramenta):

```
Fotografia de produto para e-mail de e-commerce. Use a foto de referência
como o produto exato, sem alterar forma, cor, costura, rótulo ou logo.
Cena: <cena do brief>. Luz: <luz do brief>. Enquadramento: <enquadramento>,
proporção <4:3>, produto ocupando <60%> da área, <área livre> lisa.
Sem texto, sem letras, sem marca d'água, sem outros produtos.
Estilo: fotografia real, não ilustração, não 3D.
```

O material de prompts por lote da Blue Wolf
(`07_Design_Blue_Wolf/04_PROMPTS_POR_LOTE.md`) é o exemplo de como isso vira
rotina por campanha: um prompt mestre com a direção de arte, e um prompt
por lote que anexa as referências validadas.

### Checklist contra imagem genérica de IA (D15)

Reprove a imagem gerada que tiver qualquer um destes:

- [ ] Pessoa com pele de plástico, dentes perfeitos, mãos com dedos a mais
      ou a menos.
- [ ] Produto flutuando sobre fundo abstrato.
- [ ] Brilho, reflexo e partícula de "premium" que a marca não usa.
- [ ] Texto ou letras deformadas em algum canto.
- [ ] Produto diferente do real (cor, detalhe, logo).
- [ ] Iluminação de estúdio impossível numa cena externa.

## Imagem e dark mode

- JPG com fundo branco **vira um retângulo branco** no fundo escuro do dark
  mode. Em peça neutra (fundo branco) isso é invisível no claro e aceitável
  no escuro. Em peça de fundo escuro, a foto de estúdio branca vira um
  buraco: peça foto com o fundo da peça, ou PNG recortado com borda tratada.
- PNG transparente com elemento preto (logo, ícone) **some** no escuro
  (R18). Opções em `dark-mode.md`.
- Texto dentro de imagem não inverte junto com o texto vivo, e a peça fica
  com "dois registros" (R19). Mais um motivo para texto vivo.

## Quando o design vem do Figma em fatias

O método do Max é desenhar no Figma e subir o e-mail em fatias de imagem.
A casa é HTML-primeiro (texto, preço, cupom e botão vivos), e usa fatia de
imagem para o que é arte. Quando uma peça chega do Figma:

1. **Fatie por área de link.** Cada fatia com um destino só (regra do Max:
   "different slices for different areas of our email that are going to
   have different links").
2. **Nenhum texto cortado entre duas fatias** (Blue Wolf). O corte cai no
   espaço entre blocos.
3. **Altura de fatia até 800px** (o Max fala em "800ish"; 720 recomendado).
4. **Largura exata de 600 e exportação em 2x.**
5. **Comprima antes de subir.** O teto por imagem é 200 KB.
6. **O que é oferta, preço, cupom, prazo e botão sai da fatia e vira HTML**
   (os módulos 4, 5 e 6). Se o corte é automático (Figma para PNG), essa
   separação acontece antes do corte, não depois.
7. **Alt em toda fatia**, e a fatia do hero com a oferta no alt.

## Verificação

- [ ] Toda imagem tem proporção e tamanho da tabela de slots?
- [ ] As fotos da grade têm a mesma proporção?
- [ ] Toda imagem grande está linkada?
- [ ] Nenhuma informação de compra só dentro da imagem?
- [ ] Texto dentro de imagem respeita a tabela de `tipografia.md`?
- [ ] Peso total de imagem abaixo de 800 KB?
- [ ] Imagem gerada tem aprovação no brief e passou no checklist D15?
- [ ] No `dark-600.png`, nenhum retângulo branco ou logo sumido?
- [ ] O brief de imagem foi entregue para cada slot sem foto?
