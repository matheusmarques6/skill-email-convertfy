# Módulos de e-commerce: anatomia, medidas e HTML testado

Detalhe da `email-design`. É o "como construir bem" de cada peça de uma
loja: hero, oferta, botão, produto, grade, avaliação, garantias, texto de
pessoa, rodapé. Cada módulo traz a anatomia, as medidas, os erros que mais
aparecem e um HTML de referência.

## O que este arquivo é, e o que não é

**A estrutura continua vindo do vault.** Quem escolhe hero, body, products e
a ordem é o protocolo de seleção (`vault/componentes/_protocolo-de-selecao.md`).
Este arquivo não escolhe variante e não substitui uma.

Ele serve a três coisas:

1. **Julgar e consertar** o HTML de uma variante que saiu torta no render
   (hierarquia, espaço, botão, preço).
2. **Montar o bloco do arsenal** quando a seção não tem variante (`header`
   e `cta` têm zero hoje) ou quando a ficha da marca pede algo que nenhuma
   variante cobre. Bloco novo entra como **proposta**, com lacuna declarada,
   como os de `assets/arsenal/blocos/`.
3. **Preencher slot com critério**: quanto texto cabe no título, que
   proporção a foto precisa ter, onde vai o preço riscado.

## Como os trechos são verificados

Todo bloco marcado com ` ```html modulo=<slug> ` é extraído por
`scripts/vitrine_modulos.py`, montado na `casca-600` com valores de
exemplo e passado no `lint_email.py`. O teste
`scripts/tests/test_vitrine_modulos.py` falha se algum módulo gerar achado
de lint ou deixar slot sem valor. Para ver os três PNGs:

```bash
python3 scripts/vitrine_modulos.py --render
# abre evals/render/vitrine-modulos/{desktop-600,mobile-375,dark-600}.png
```

Mudou um trecho aqui, rode o teste. Trecho que não passa no lint não fica
neste arquivo.

## Convenções de todos os módulos

- Cada módulo é uma ou mais linhas `<tr>` para entrar no container de
  600px da `casca-600`.
- Slots em CAIXA_ALTA, como no arsenal. `COR_DO_BOTAO` é `#111111` no
  regime neutro e a `cor_primaria` da ficha quando `usa_cor_de_marca: true`.
- Pilha tipográfica de texto vivo: `Helvetica,Arial,sans-serif`. Fonte da
  marca entra na frente da pilha só quando a ficha nomeia (ver
  `tipografia.md`).
- Cores de texto do regime neutro: `#111111` (título), `#1A1A1A` (corpo),
  `#595959` (apoio, 7,0:1 no branco). Linha divisória `#E3E3E3`.
- `line-height` sempre em px e com `mso-line-height-rule:exactly` em título,
  porque o Outlook calcula a entrelinha de outro jeito e abre buraco.
- Título em `<h1>`/`<h2>` com `margin:0`: leitor de tela navega por título,
  e o `margin:0` impede o Outlook de somar margem própria.
- Espaço só da escala de `espaco-e-ritmo.md`: 8, 12, 16, 24, 32, 40, 48, 64.
- A classe `pad` é a da `casca-600`: no celular ela troca o respiro lateral
  por 16px.

---

## 1. Cabeçalho com logo

**Função:** dizer de quem é o e-mail em meio segundo e levar ao site.

**Medidas:** logo entre 120 e 160px de largura no desktop (o mesmo no
celular, ele não cresce). Altura do bloco: 64 a 88px. Exportar o PNG em 2x
(o dobro da largura exibida).

**Erros comuns:**
- Logo PNG transparente preto: some no dark mode (R18). Use versão com
  contorno, fundo sólido embutido, ou a troca de logo de `dark-mode.md`.
- Menu de navegação com 5 itens no topo: rouba a dobra do celular. Se a
  ficha pede navegação, no máximo 3 itens curtos, e só em e-mail de
  catálogo.
- Logo sem link: perde o clique de quem só quer ir ao site.

Slots: `URL_DO_SITE`, `URL_DO_LOGO`, `NOME_DA_MARCA`.

```html modulo=cabecalho-logo
<tr>
  <td align="center" style="padding:24px 24px 16px;background:#FFFFFF;">
    <a href="URL_DO_SITE" style="text-decoration:none;"><img src="URL_DO_LOGO" width="140" alt="NOME_DA_MARCA" style="display:block;width:140px;max-width:140px;height:auto;border:0;"></a>
  </td>
</tr>
```

Sem logo em imagem, o `header-1-wordmark-centralizado` do arsenal resolve
com texto vivo.

---

## 2. Hero com imagem e texto vivo (o padrão)

**Função:** fazer a pessoa entender o benefício e saber onde clicar sem
rolar. É a seção que carrega 75% do esforço (vault,
`doutrina/hero-quatro-itens-above-the-fold.md`): título claro, imagem
forte, proposta de valor clara e botão.

**Anatomia, de cima para baixo:**

| Elemento | Medida | Regra |
|---|---|---|
| Imagem | 600px de largura, proporção 4:3 (600x450) ou 1:1 (600x600) | Linkada (D21). Sem texto essencial dentro. O sujeito no terço de cima |
| Título | 30 a 36px, `line-height` +6px | Até 40 caracteres (D13). Duas linhas no desktop, três no celular, no máximo |
| Proposta de valor | 17 ou 18px, `line-height` 26px | Uma frase, até 20 palavras. Diz o valor, o prazo ou a condição |
| Botão | 52px de altura, 280 a 320px de largura | Um só no hero (D30). Na dobra do celular, que é 667px |

**A conta da primeira dobra no celular (375 x 667), medida no render:** a
imagem 4:3 vai de ponta a ponta e ocupa 375 x 281px; o título de 34px quebra
em 3 linhas (120px) com 32 de respiro; a proposta em 2 linhas (52px) com 12;
o botão de 52px com 24 acima. Somando o cabeçalho de 80px, **o botão termina
em cerca de 653px**. Cabe, sem folga. Com imagem 1:1 (375px de altura), o
botão cai para cerca de 747px, fora da dobra (R10): troque a proporção ou
corte o título para 2 linhas.

**Erros comuns:**
- Oferta só dentro da imagem (V02, bloqueia): o valor e o prazo precisam
  existir em texto vivo.
- Título genérico ("Novidades chegaram"): o título carrega o benefício ou o
  motivo de comprar agora.
- Pílula acima do título só para enfeitar (D07). Rótulo acima do título
  vale quando carrega prazo ou condição, e no máximo um a cada três seções.

Slots: `URL_DO_CTA`, `URL_DA_IMAGEM_HERO`, `ALT_DO_HERO`, `HEADLINE_DO_HERO`,
`PROPOSTA_DE_VALOR`, `COR_DO_BOTAO`, `TEXTO_DO_CTA`.

```html modulo=hero-imagem-e-texto-vivo
<tr>
  <td style="padding:0;background:#FFFFFF;">
    <a href="URL_DO_CTA" style="text-decoration:none;"><img src="URL_DA_IMAGEM_HERO" width="600" height="450" alt="ALT_DO_HERO" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a>
  </td>
</tr>
<tr>
  <td align="center" class="pad" style="padding:32px 40px 0;background:#FFFFFF;">
    <h1 style="margin:0;font-family:Helvetica,Arial,sans-serif;font-size:34px;line-height:40px;font-weight:bold;color:#111111;mso-line-height-rule:exactly;">HEADLINE_DO_HERO</h1>
    <p style="margin:12px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:17px;line-height:26px;color:#1A1A1A;mso-line-height-rule:exactly;">PROPOSTA_DE_VALOR</p>
  </td>
</tr>
<tr>
  <td align="center" style="padding:24px 24px 40px;background:#FFFFFF;">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="URL_DO_CTA" style="height:52px;v-text-anchor:middle;width:300px;" arcsize="6%" stroke="f" fillcolor="COR_DO_BOTAO"><w:anchorlock/><center style="color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;letter-spacing:1px;">TEXTO_DO_CTA</center></v:roundrect><![endif]-->
    <!--[if !mso]><!--><a href="URL_DO_CTA" style="display:inline-block;min-width:236px;background:COR_DO_BOTAO;color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;line-height:20px;letter-spacing:1px;text-align:center;text-decoration:none;padding:16px 32px;border-radius:3px;">TEXTO_DO_CTA</a><!--<![endif]-->
  </td>
</tr>
```

---

## 3. Hero com imagem de fundo e texto vivo por cima

**Quando:** só quando a ficha da marca traz direção de arte com foto de
campanha (o regime "marca" de `direcao-visual.md`), e a foto tem uma área
lisa para o texto. No regime neutro, use o módulo 2.

**Por que existe:** é o jeito de ter o visual de "texto sobre foto" sem
colocar o texto dentro da imagem. O texto continua vivo: resumidor de IA,
leitor de tela e imagem bloqueada leem a oferta.

**Medidas:** 600 x 420 a 480px. Área do texto com, no mínimo, 48px de
respiro. Cor de fundo sólida (`bgcolor`) igual ao tom dominante da foto,
porque é ela que aparece quando a imagem não carrega, e é contra ela que o
contraste é medido.

**Riscos que precisam ser aceitos por escrito:**
- O app do Gmail com conta que não é Google pode descartar a imagem de
  fundo. Sobra a cor sólida com o texto: legível, mas sem foto.
- O VML do Outlook não aceita `background-size:cover`: a foto precisa ser
  exportada exatamente em 600 x altura do bloco.
- Escurecer a foto por cima (overlay) não funciona com gradiente (D02,
  bloqueia). Escureça no arquivo da imagem.

Slots: `URL_DA_IMAGEM_DE_FUNDO`, `HEADLINE_DO_HERO`, `PROPOSTA_DE_VALOR`,
`URL_DO_CTA`, `TEXTO_DO_CTA`.

```html modulo=hero-fundo-com-texto-vivo
<tr>
  <td background="URL_DA_IMAGEM_DE_FUNDO" bgcolor="#1A1A1A" width="600" height="440" valign="middle" style="background:#1A1A1A url('URL_DA_IMAGEM_DE_FUNDO') center top / cover no-repeat;">
    <!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:450pt;height:330pt;"><v:fill type="frame" src="URL_DA_IMAGEM_DE_FUNDO" color="#1A1A1A" /><v:textbox inset="0,0,0,0"><![endif]-->
    <div>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="center" class="pad" style="padding:64px 48px 64px;">
            <h1 style="margin:0;font-family:Helvetica,Arial,sans-serif;font-size:36px;line-height:42px;font-weight:bold;color:#FFFFFF;mso-line-height-rule:exactly;">HEADLINE_DO_HERO</h1>
            <p style="margin:12px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:17px;line-height:26px;color:#FFFFFF;mso-line-height-rule:exactly;">PROPOSTA_DE_VALOR</p>
            <div style="margin-top:24px;">
              <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="URL_DO_CTA" style="height:52px;v-text-anchor:middle;width:300px;" arcsize="6%" stroke="f" fillcolor="#FFFFFF"><w:anchorlock/><center style="color:#111111;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;letter-spacing:1px;">TEXTO_DO_CTA</center></v:roundrect><![endif]-->
              <!--[if !mso]><!--><a href="URL_DO_CTA" style="display:inline-block;min-width:236px;background:#FFFFFF;color:#111111;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;line-height:20px;letter-spacing:1px;text-align:center;text-decoration:none;padding:16px 32px;border-radius:3px;">TEXTO_DO_CTA</a><!--<![endif]-->
            </div>
          </td>
        </tr>
      </table>
    </div>
    <!--[if gte mso 9]></v:textbox></v:rect><![endif]-->
  </td>
</tr>
```

O botão é branco com texto escuro: sobre foto, um botão escuro some. No
Outlook ele sai do VML (fundo branco, texto `#111111`); nos outros, do link
com padding. Não use tabela aninhada para o botão aqui: a `casca-600` força
`width:100%` em toda tabela interna no celular, e o botão estica de ponta a
ponta.

---

## 4. Oferta com cupom

**Função:** responder em três segundos "quanto, como e até quando". A
carteira manda oferta, cupom, prazo e botão nos primeiros 500px em e-mail
de venda (R21).

**Anatomia:**

| Elemento | Medida | Regra |
|---|---|---|
| Rótulo | 13px, caixa alta, `letter-spacing` 2px | Opcional. Só se carregar informação ("SÓ ATÉ DOMINGO"). Nunca "OFERTA ESPECIAL" |
| Número | 56 a 72px, negrito, `line-height` 1,05 | Caixa alta e número gigante não são vício em e-mail (§8). Até 9 caracteres: "15% OFF", "R$ 50" |
| Condição | 16px | Mínimo de compra, coleção, frete. Uma linha |
| Cupom | código em 24px, negrito, espaçado | Texto vivo, selecionável. Nunca o código só na imagem |
| Prazo | 14px, cinza de apoio | Data e hora reais da ficha ou do brief (C06, V29). Sem prazo real, sem hora |

**Erros comuns:**
- Código do cupom em idioma diferente da loja (C04, bloqueia na copy).
- Caixa do cupom com fundo cinza escuro e texto cinza: some no dark mode.
  A borda tracejada em cor sólida sobrevive à inversão.
- Desconto automático e cupom na mesma peça. A ficha diz qual dos dois
  (`desconto_automatico`); o outro não aparece.

Slots: `ROTULO_DA_OFERTA`, `VALOR_DA_OFERTA`, `CONDICAO_DA_OFERTA`,
`CODIGO_DO_CUPOM`, `PRAZO_DA_OFERTA`.

```html modulo=oferta-cupom
<tr>
  <td align="center" class="pad" style="padding:40px 40px 0;background:#FFFFFF;">
    <p style="margin:0;font-family:Helvetica,Arial,sans-serif;font-size:13px;line-height:18px;font-weight:bold;letter-spacing:2px;color:#1A1A1A;">ROTULO_DA_OFERTA</p>
    <p style="margin:8px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:64px;line-height:68px;font-weight:bold;color:#111111;mso-line-height-rule:exactly;">VALOR_DA_OFERTA</p>
    <p style="margin:8px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:24px;color:#1A1A1A;">CONDICAO_DA_OFERTA</p>
  </td>
</tr>
<tr>
  <td align="center" style="padding:24px 24px 0;background:#FFFFFF;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td align="center" style="padding:16px 32px;border:2px dashed #111111;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;">
          <span style="display:block;font-size:12px;line-height:16px;letter-spacing:2px;color:#595959;">CUPOM</span>
          <span style="display:block;margin-top:4px;font-size:24px;line-height:30px;font-weight:bold;letter-spacing:3px;color:#111111;">CODIGO_DO_CUPOM</span>
        </td>
      </tr>
    </table>
  </td>
</tr>
<tr>
  <td align="center" style="padding:12px 24px 0;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:20px;color:#595959;">PRAZO_DA_OFERTA</td>
</tr>
```

---

## 5. Botão principal e link secundário

**Botão principal (o único com cor de ação):**
- 48 a 56px de altura, 280 a 320px de largura no desktop. É 75 a 85% da
  largura útil do celular, o que bate com a régua de "1,5 a 2 polegadas" do
  Max convertida em pixel (vault, `doutrina/botao-e-clique.md`).
- Largura por `min-width` (236px) mais padding lateral (32px de cada lado),
  nunca `width` fixo com padding zero. A `casca-600` troca todo `width` de
  link por `auto` no celular (para não rolar na horizontal), e um botão com
  `width:300px; padding:16px 0` vira um retângulo do tamanho exato do texto,
  colado nas bordas. Achado no render desta vitrine.
- Texto de 15 a 16px, negrito, 1 a 3 palavras. **Nunca quebra em duas
  linhas.** Se quebra, o texto está longo, não o botão estreito.
- Centralizado. Mesmo texto e mesmo destino quando repetido: o §8 protege
  a repetição, e dois textos diferentes para a mesma ação ("Comprar
  agora", "Garantir o meu", "Quero") fazem a pessoa achar que são ações
  diferentes.
- Uma cor de botão na peça inteira (D29, o lint avisa).

**Link secundário (ação de apoio):**
- Texto sublinhado, 15 a 16px, negrito, cor do texto. Sem fundo.
- Usado para "Ver todos os produtos", "Ver a coleção", o fecho geral que o
  Max pede depois da vitrine (+25% de clique relatado, vault
  `secao-product`).
- Nunca com cor diferente do botão principal. Se precisa de mais peso,
  use o botão fantasma: fundo branco, borda de 2px na cor do texto.

Slots: `URL_DO_CTA`, `COR_DO_BOTAO`, `TEXTO_DO_CTA`, `URL_DA_COLECAO`,
`TEXTO_DO_LINK_SECUNDARIO`.

```html modulo=botao-e-link-secundario
<tr>
  <td align="center" style="padding:32px 24px 0;background:#FFFFFF;">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="URL_DO_CTA" style="height:52px;v-text-anchor:middle;width:300px;" arcsize="6%" stroke="f" fillcolor="COR_DO_BOTAO"><w:anchorlock/><center style="color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;letter-spacing:1px;">TEXTO_DO_CTA</center></v:roundrect><![endif]-->
    <!--[if !mso]><!--><a href="URL_DO_CTA" style="display:inline-block;min-width:236px;background:COR_DO_BOTAO;color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;line-height:20px;letter-spacing:1px;text-align:center;text-decoration:none;padding:16px 32px;border-radius:3px;">TEXTO_DO_CTA</a><!--<![endif]-->
  </td>
</tr>
<tr>
  <td align="center" style="padding:16px 24px 40px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:15px;line-height:22px;font-weight:bold;">
    <a href="URL_DA_COLECAO" style="color:#111111;text-decoration:underline;">TEXTO_DO_LINK_SECUNDARIO</a>
  </td>
</tr>
```

---

## 6. Produto em destaque (um produto só)

**Quando:** lançamento, volta ao estoque, produto do dia, carrinho
abandonado de um item. Um produto aprofundado vende mais que uma vitrine
rasa quando o e-mail tem um só motivo.

**Anatomia:** foto 1:1 ou 4:5 com 536px, nome (20 a 24px), preço, uma frase
de benefício, botão.

**Preço "de/por":**
- "Por" em negrito, 18px, cor do texto. É o número que a pessoa procura.
- "De" riscado, 15px, cinza de apoio `#595959`, **antes** do "por".
- Os dois em texto vivo, com a moeda da ficha: `R$ 149,90` (pt-BR),
  `$149.90` (en-US), `149,90 €` (de, fr, it, es).
- Preço "de" só se é o preço real anterior (C02). Desconto inventado
  é publicidade enganosa.

Slots: `URL_DO_PRODUTO`, `URL_FOTO_PRODUTO`, `ALT_DO_PRODUTO`,
`NOME_DO_PRODUTO`, `PRECO_DE`, `PRECO_POR`, `BENEFICIO_EM_UMA_FRASE`,
`COR_DO_BOTAO`, `TEXTO_DO_CTA_PRODUTO`.

```html modulo=produto-destaque
<tr>
  <td align="center" style="padding:40px 32px 0;background:#FFFFFF;">
    <a href="URL_DO_PRODUTO" style="text-decoration:none;"><img src="URL_FOTO_PRODUTO" width="536" height="536" alt="ALT_DO_PRODUTO" style="display:block;width:100%;max-width:536px;height:auto;border:0;"></a>
  </td>
</tr>
<tr>
  <td align="center" class="pad" style="padding:24px 40px 0;background:#FFFFFF;">
    <h2 style="margin:0;font-family:Helvetica,Arial,sans-serif;font-size:22px;line-height:28px;font-weight:bold;color:#111111;mso-line-height-rule:exactly;">NOME_DO_PRODUTO</h2>
    <p style="margin:8px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:18px;line-height:24px;color:#111111;"><span style="font-size:15px;color:#595959;text-decoration:line-through;">PRECO_DE</span>&nbsp;&nbsp;<strong>PRECO_POR</strong></p>
    <p style="margin:12px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:24px;color:#1A1A1A;">BENEFICIO_EM_UMA_FRASE</p>
  </td>
</tr>
<tr>
  <td align="center" style="padding:24px 24px 40px;background:#FFFFFF;">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="URL_DO_PRODUTO" style="height:52px;v-text-anchor:middle;width:300px;" arcsize="6%" stroke="f" fillcolor="COR_DO_BOTAO"><w:anchorlock/><center style="color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;letter-spacing:1px;">TEXTO_DO_CTA_PRODUTO</center></v:roundrect><![endif]-->
    <!--[if !mso]><!--><a href="URL_DO_PRODUTO" style="display:inline-block;min-width:236px;background:COR_DO_BOTAO;color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:bold;line-height:20px;letter-spacing:1px;text-align:center;text-decoration:none;padding:16px 32px;border-radius:3px;">TEXTO_DO_CTA_PRODUTO</a><!--<![endif]-->
  </td>
</tr>
```

---

## 7. Grade de produtos 2x2

**Quando:** coleção, mais vendidos, "os que esgotam primeiro", fecho de
campanha. É uma das duas exceções à coluna única (a outra é o comparativo
de duas colunas).

**Regras da grade:**
- **Exatamente o número de produtos que você tem.** Quatro produtos, 2x2.
  Seis, 2x3. Três produtos não viram 2x2 com um buraco: viram destaque + 2
  ou três linhas do módulo 8. Célula vazia é peça truncada.
- **Todas as fotos na mesma proporção, recortadas antes do upload.** O
  Gmail ignora `object-fit`, então a única forma garantida de cards com a
  mesma altura (D25, R20) é o arquivo já sair 1:1 (ou todos 4:5). Com o
  recorte garantido, `height:auto` é seguro; sem ele, fixe a altura.
- **CTA por produto.** O Max exige; o slide dele aceita título sublinhado
  (vault, `secao-product`). Aqui o padrão é o link "COMPRAR" sublinhado:
  quatro botões cheios competem com o principal e disparam o D29.
- **Fecho geral depois da grade:** "Ver todos" (módulo 5).
- Nome do produto com até 40 caracteres (duas linhas a 16px numa coluna de
  260px). Calha de 16px entre os cards (8 de cada lado), na escala. Mais que isso, encurte para o nome comercial.
- No celular, cada coluna vira linha inteira (técnica híbrida: `div`
  inline-block de 276px, sem depender de media query, que o Gmail pode
  descartar). A tabela condicional faz o Outlook respeitar as duas colunas.

Slots: `URL_PRODUTO_1` a `URL_PRODUTO_4`, `URL_FOTO_1` a `URL_FOTO_4`,
`ALT_PRODUTO_1` a `ALT_PRODUTO_4`, `NOME_PRODUTO_1` a `NOME_PRODUTO_4`,
`PRECO_DE_1` a `PRECO_DE_4`, `PRECO_POR_1` a `PRECO_POR_4`,
`TEXTO_DO_LINK_PRODUTO`.

O trecho mostra uma linha da grade (dois produtos). A segunda linha é a
mesma estrutura com os slots 3 e 4.

```html modulo=grade-2x2-linha
<tr>
  <td align="center" style="padding:32px 24px 0;background:#FFFFFF;font-size:0;">
    <!--[if mso]><table role="presentation" width="552" cellpadding="0" cellspacing="0" border="0"><tr><td width="276" valign="top"><![endif]-->
    <div style="display:inline-block;width:100%;max-width:276px;vertical-align:top;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="center" valign="top" style="padding:0 8px 32px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;">
            <a href="URL_PRODUTO_1" style="text-decoration:none;"><img src="URL_FOTO_1" width="260" height="260" alt="ALT_PRODUTO_1" style="display:block;width:100%;max-width:260px;height:auto;border:0;"></a>
            <p style="margin:16px 0 0;font-size:16px;line-height:22px;font-weight:bold;color:#111111;">NOME_PRODUTO_1</p>
            <p style="margin:8px 0 0;font-size:16px;line-height:22px;color:#111111;"><span style="font-size:14px;color:#595959;text-decoration:line-through;">PRECO_DE_1</span>&nbsp; <strong>PRECO_POR_1</strong></p>
            <p style="margin:12px 0 0;font-size:14px;line-height:20px;font-weight:bold;letter-spacing:1px;"><a href="URL_PRODUTO_1" style="color:#111111;text-decoration:underline;">TEXTO_DO_LINK_PRODUTO</a></p>
          </td>
        </tr>
      </table>
    </div>
    <!--[if mso]></td><td width="276" valign="top"><![endif]-->
    <div style="display:inline-block;width:100%;max-width:276px;vertical-align:top;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="center" valign="top" style="padding:0 8px 32px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;">
            <a href="URL_PRODUTO_2" style="text-decoration:none;"><img src="URL_FOTO_2" width="260" height="260" alt="ALT_PRODUTO_2" style="display:block;width:100%;max-width:260px;height:auto;border:0;"></a>
            <p style="margin:16px 0 0;font-size:16px;line-height:22px;font-weight:bold;color:#111111;">NOME_PRODUTO_2</p>
            <p style="margin:8px 0 0;font-size:16px;line-height:22px;color:#111111;"><span style="font-size:14px;color:#595959;text-decoration:line-through;">PRECO_DE_2</span>&nbsp; <strong>PRECO_POR_2</strong></p>
            <p style="margin:12px 0 0;font-size:14px;line-height:20px;font-weight:bold;letter-spacing:1px;"><a href="URL_PRODUTO_2" style="color:#111111;text-decoration:underline;">TEXTO_DO_LINK_PRODUTO</a></p>
          </td>
        </tr>
      </table>
    </div>
    <!--[if mso]></td></tr></table><![endif]-->
  </td>
</tr>
```

O `font-size:0` no `<td>` pai mata o espaço em branco entre as duas `div`,
que de outro modo empurra a segunda coluna para baixo no desktop
(`checklist-tecnico.md`, empilhamento). Por isso todo texto dentro declara
o próprio `font-size`.

---

## 8. Produto em linha (foto à esquerda, texto à direita)

**Quando:** item de carrinho abandonado, lista de 3 produtos, "o que tem
na caixa", comparação curta. Dá mais espaço para nome e argumento que a
grade.

**Medidas:** foto de 176px (1:1) numa coluna de 200px, coluna de texto de 352px, alinhada à
esquerda. No celular, empilha: foto em cima, texto embaixo, os dois à
esquerda.

**Regra do `vertical-align`:** se uma coluna declara, todas declaram
(`checklist-tecnico.md`). Aqui as duas declaram `middle`.

Slots: `URL_DO_PRODUTO`, `URL_FOTO_PRODUTO`, `ALT_DO_PRODUTO`,
`NOME_DO_PRODUTO`, `DETALHE_DO_PRODUTO`, `PRECO_POR`,
`TEXTO_DO_LINK_PRODUTO`.

```html modulo=produto-em-linha
<tr>
  <td align="left" style="padding:16px 24px;background:#FFFFFF;font-size:0;">
    <!--[if mso]><table role="presentation" width="552" cellpadding="0" cellspacing="0" border="0"><tr><td width="200" valign="middle"><![endif]-->
    <div style="display:inline-block;width:100%;max-width:200px;vertical-align:middle;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="left" valign="middle" style="padding:0 24px 0 0;">
            <a href="URL_DO_PRODUTO" style="text-decoration:none;"><img src="URL_FOTO_PRODUTO" width="176" height="176" alt="ALT_DO_PRODUTO" style="display:block;width:176px;max-width:100%;height:auto;border:0;"></a>
          </td>
        </tr>
      </table>
    </div>
    <!--[if mso]></td><td width="352" valign="middle"><![endif]-->
    <div style="display:inline-block;width:100%;max-width:352px;vertical-align:middle;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="left" valign="middle" style="padding:12px 0;font-family:Helvetica,Arial,sans-serif;">
            <p style="margin:0;font-size:17px;line-height:24px;font-weight:bold;color:#111111;">NOME_DO_PRODUTO</p>
            <p style="margin:8px 0 0;font-size:15px;line-height:22px;color:#1A1A1A;">DETALHE_DO_PRODUTO</p>
            <p style="margin:8px 0 0;font-size:16px;line-height:22px;font-weight:bold;color:#111111;">PRECO_POR</p>
            <p style="margin:12px 0 0;font-size:14px;line-height:20px;font-weight:bold;letter-spacing:1px;"><a href="URL_DO_PRODUTO" style="color:#111111;text-decoration:underline;">TEXTO_DO_LINK_PRODUTO</a></p>
          </td>
        </tr>
      </table>
    </div>
    <!--[if mso]></td></tr></table><![endif]-->
  </td>
</tr>
```

---

## 9. Avaliação real

**Função:** prova social que a pessoa acredita. Só existe com dado real da
loja (C02, `reviews_disponiveis: true` na ficha). Sem dado, o bloco **não
aparece** (D24): nunca um depoimento de exemplo.

**Anatomia:**
- Estrelas em texto (`&#9733;`, a estrela cheia), 20px, cor do texto ou da
  marca. Texto renderiza em todo cliente e sobrevive ao dark mode; estrela
  em imagem some com imagem bloqueada.
- A nota e o volume em texto ao lado ou embaixo: "4,8 de 5, 1.284
  avaliações". Estrela sem número é enfeite.
- O trecho: no máximo três linhas no desktop, entre aspas tipográficas
  (“ ”). Corte a avaliação; não reescreva. Palavra do cliente com erro de
  digitação fica (é o que prova que é real), salvo palavrão.
- Assinatura: primeiro nome e inicial do sobrenome, mais "Compra
  verificada" quando o app de avaliação marca. Nunca só o primeiro nome.
- Sem avatar de inicial em gradiente (D10). Foto real do cliente, foto do
  produto ou nenhuma imagem.

Slots: `NOTA_MEDIA`, `NUMERO_DE_AVALIACOES`, `TRECHO_DA_AVALIACAO`,
`NOME_DO_CLIENTE`, `SELO_DA_AVALIACAO`.

```html modulo=avaliacao
<tr>
  <td align="center" class="pad" style="padding:40px 48px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;">
    <p style="margin:0;font-size:20px;line-height:24px;letter-spacing:4px;color:#111111;">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
    <p style="margin:8px 0 0;font-size:14px;line-height:20px;color:#595959;">NOTA_MEDIA de 5, NUMERO_DE_AVALIACOES avaliações</p>
    <p style="margin:24px 0 0;font-size:18px;line-height:28px;color:#111111;">&ldquo;TRECHO_DA_AVALIACAO&rdquo;</p>
    <p style="margin:12px 0 0;font-size:14px;line-height:20px;font-weight:bold;color:#111111;">NOME_DO_CLIENTE <span style="font-weight:normal;color:#595959;">&middot; SELO_DA_AVALIACAO</span></p>
  </td>
</tr>
```

---

## 10. Faixa de garantias

**Função:** tirar a dúvida que trava a compra (frete, troca, pagamento)
sem virar seção de "diferenciais" com ícone (D08 permite faixa curta, não
estrutura principal).

**Regras:**
- Três itens, no máximo. Cada um com até 5 palavras e com o fato
  verificável da ficha (`prazo_de_entrega_declarado`,
  `politica_de_troca_publicada`). Sem o fato, o item sai.
- Uma linha por item, empilhado. A versão em três colunas com ícone de
  linha (a do rodapé da Blue Wolf) entra quando a ficha da marca já tem
  esse componente.
- Sem ícone de banco de imagem e sem emoji no lugar de ícone.

Slots: `GARANTIA_1`, `GARANTIA_2`, `GARANTIA_3`.

```html modulo=faixa-de-garantias
<tr>
  <td style="padding:0 40px;background:#FFFFFF;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td align="center" style="padding:24px 0;border-top:1px solid #E3E3E3;border-bottom:1px solid #E3E3E3;font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:26px;color:#1A1A1A;">
          GARANTIA_1<br>GARANTIA_2<br>GARANTIA_3
        </td>
      </tr>
    </table>
  </td>
</tr>
```

---

## 11. Texto de pessoa

**Quando:** os modelos titulares do ranking da carteira que não são
"desenho": texto de pessoa, fundador, gerente, conversa, cupom liberado às
7h (`fontes/BFCM-2026-Convertfy/05_Modelos_validados/`). O visual é a
ausência de visual: parece um e-mail escrito por alguém.

**Regras:**
- Alinhado à esquerda (texto corrido centralizado é R16).
- 16px, `line-height` 26px, largura de leitura de 500 a 520px (cerca de 65
  caracteres por linha).
- Sem imagem, sem botão cheio. A ação é um link sublinhado no meio do texto
  e, se o brief pede, repetido no P.S.
- Assinatura com nome e cargo de uma pessoa que existe (PQ6 do padrão de
  qualidade).
- Sem cabeçalho de marca grande. Se a ficha exige o logo, ele entra
  pequeno (100px) e à esquerda.

Slots: `SAUDACAO_COM_NOME`, `PARAGRAFO_1`, `PARAGRAFO_2`, `URL_DO_CTA`,
`LINK_DE_ACAO`, `NOME_DE_QUEM_ASSINA`, `CARGO_E_LOJA`.

```html modulo=texto-de-pessoa
<tr>
  <td align="left" class="pad" style="padding:40px 48px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:26px;color:#111111;text-align:left;">
    <p style="margin:0 0 16px;">SAUDACAO_COM_NOME</p>
    <p style="margin:0 0 16px;">PARAGRAFO_1</p>
    <p style="margin:0 0 16px;">PARAGRAFO_2 <a href="URL_DO_CTA" style="color:#111111;font-weight:bold;text-decoration:underline;">LINK_DE_ACAO</a></p>
    <p style="margin:24px 0 0;">NOME_DE_QUEM_ASSINA<br><span style="color:#595959;">CARGO_E_LOJA</span></p>
  </td>
</tr>
```

---

## 12. Divisória e espaçador

**Divisória:** só entre dois blocos da mesma natureza que precisam ser lidos
separados (dois produtos em linha, o fim da vitrine antes do rodapé). Entre
blocos de natureza diferente, quem separa é o espaço, não a linha. Mais de
duas divisórias na peça é R22 (densidade de enfeite).

**Espaçador:** linha vazia com altura fixa. Use quando o espaço não cabe no
padding de nenhum dos dois vizinhos (por exemplo, entre duas variantes do
vault, que não se editam). O `font-size:0` e o `line-height:0` impedem o
Outlook de esticar a linha até a altura de uma linha de texto.

Slots: nenhum. A altura do espaçador vem da escala (`espaco-e-ritmo.md`).

```html modulo=divisoria-e-espacador
<tr>
  <td style="padding:0 40px;background:#FFFFFF;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr><td style="height:1px;font-size:0;line-height:0;border-top:1px solid #E3E3E3;">&nbsp;</td></tr>
    </table>
  </td>
</tr>
<tr>
  <td height="32" style="height:32px;font-size:0;line-height:0;mso-line-height-rule:exactly;background:#FFFFFF;">&nbsp;</td>
</tr>
```

---

## 13. Contagem regressiva em GIF

**Só com prazo real** (C06, nível 1 do CLAUDE.md: nenhum dado revoga).
Contador que reinicia a cada abertura, ou que aponta para um prazo que não
existe, é proibido.

**Regras:**
- O GIF vem de um serviço de contagem com a data real do brief. O Outlook
  de desktop mostra só o primeiro quadro: o primeiro quadro precisa ser
  legível sozinho.
- O prazo também em texto vivo, embaixo, por extenso.
- Alt com o prazo: "A oferta termina domingo, 23h59".
- Largura de 400 a 520px, linkado ao CTA.
- Um por peça. Ver `movimento-e-gif.md`.

Slots: `URL_DO_CTA`, `URL_DO_GIF_DE_CONTAGEM`, `PRAZO_POR_EXTENSO`.

```html modulo=contagem-regressiva
<tr>
  <td align="center" style="padding:24px 24px 0;background:#FFFFFF;">
    <a href="URL_DO_CTA" style="text-decoration:none;"><img src="URL_DO_GIF_DE_CONTAGEM" width="440" height="110" alt="A oferta termina PRAZO_POR_EXTENSO" style="display:block;width:100%;max-width:440px;height:auto;border:0;"></a>
  </td>
</tr>
<tr>
  <td align="center" style="padding:8px 24px 0;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:20px;color:#595959;">A oferta termina PRAZO_POR_EXTENSO.</td>
</tr>
```

---

## 14. Rodapé com categorias

**Função:** o último lugar onde um clique perdido ainda acontece. O Max
chama de "huge lever": quem rolou tudo sem achar nada ainda clica numa
categoria (vault, `secao-footer`).

**Regras:**
- De 3 a 5 categorias reais da loja, em caixa alta curta, links de texto.
  Área de toque com padding (o link inteiro, não só a palavra).
- Igual em todos os e-mails da loja (universal).
- Depois das categorias, o `rodape-legal` do arsenal: descadastro visível e
  endereço físico. Isso é conformidade, não estilo.
- Social só se a loja tem perfil ativo, em texto ("Instagram") ou ícone
  PNG de 24px com alt. Nunca ícone SVG (D18).

Slots: `URL_CATEGORIA_1` a `URL_CATEGORIA_4`, `CATEGORIA_1` a `CATEGORIA_4`.

```html modulo=rodape-categorias
<tr>
  <td align="center" style="padding:32px 16px 16px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:20px;font-weight:bold;letter-spacing:1px;">
    <a href="URL_CATEGORIA_1" style="display:inline-block;padding:12px;color:#111111;text-decoration:none;">CATEGORIA_1</a>
    <a href="URL_CATEGORIA_2" style="display:inline-block;padding:12px;color:#111111;text-decoration:none;">CATEGORIA_2</a>
    <a href="URL_CATEGORIA_3" style="display:inline-block;padding:12px;color:#111111;text-decoration:none;">CATEGORIA_3</a>
    <a href="URL_CATEGORIA_4" style="display:inline-block;padding:12px;color:#111111;text-decoration:none;">CATEGORIA_4</a>
  </td>
</tr>
```

---

## Composição: como os módulos se somam numa peça

A ordem é do vault. As alturas abaixo foram **medidas** no render da
vitrine (`vitrine_modulos.py`, viewport de 640 e de 375), com a copy de
exemplo. Servem para não estourar o orçamento da carteira: 2.000 a 3.200px
no total, e 4.000px é o fracasso medido (R01, R02).

| Módulo | Desktop | Celular | Observação |
|---|---|---|---|
| Cabeçalho com logo | 80px | 80px | |
| Hero com imagem e texto vivo | 716px | 613px | 450 de imagem no desktop |
| Hero com fundo | 440px | 458px | Altura fixa; no celular cresce com o texto |
| Oferta com cupom | 304px | 328px | |
| Botão e link secundário | 162px | 162px | |
| Produto em destaque | 817px | 616px | Foto de 536px |
| Grade 2x2, uma linha (2 produtos) | 420px | 808px | A grade inteira: 840 no desktop, **1.616 no celular** |
| Produto em linha | 212px | 348px | Por produto |
| Avaliação | 240px | 240px | |
| Faixa de garantias | 128px | 128px | |
| Texto de pessoa | 318px | 370px | Depende da copy |
| Divisória e espaçador de 32 | 34px | 34px | |
| Contagem regressiva | 162px | 133px | |
| Rodapé com categorias | 88px | 128px | |
| Rodapé legal (arsenal) | 83px | 103px | |

**A conta que mais pega.** Cabeçalho (80) + hero (716) + oferta (304) +
grade completa (840) + avaliação (240) + garantias (128) + rodapés (171) =
**2.479px no desktop**, dentro do alvo. No celular a mesma peça dá cerca de
**3.236px**, no limite do alvo, porque a grade empilhada dobra de altura. Por isso:

- Grade de 6 produtos e produto em destaque na mesma peça passam do teto no
  celular. Escolha um.
- Com grade completa, o resto da peça tem que ser curto: um bloco de prova,
  não dois.
- O `render.py` mede a altura no desktop. O celular é sempre mais alto
  quando há colunas: some a diferença da grade antes de aprovar.
