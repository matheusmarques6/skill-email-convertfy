# Checklist técnico de HTML de e-mail

Detalhe da `email-design`. Ordem de revisão, do mais grave para o menos.

## 1. Documento

- `<!DOCTYPE html>` presente.
- `lang` no `<html>`. Acessibilidade, e o leitor de tela escolhe a voz
  certa.
- `<meta charset="utf-8">`. Sem isso, acento e aspas viram mojibake na
  passagem design para código para ESP.
- Namespaces VML no `<html>`, para o botão bulletproof funcionar no
  Outlook.
- Bloco condicional MSO com `PixelsPerInch` 96.
- As duas metas de `color-scheme`. Ver `dark-mode.md`.
- `<meta name="format-detection" content="telephone=no,date=no,address=no,email=no">`.

Depois de mover a copy entre ferramentas, confira visualmente: aspas
curvas, acentos e emoji renderizando sem mojibake.

## 2. Estrutura

- Container de 600px. O lint marca qualquer valor diferente de 600 ou 598
  (a decisão entre os dois está pendente no arsenal).
- `role="presentation"` em **toda** tabela de layout. O lint conta quantas
  têm e quantas não têm.
- Aninhamento mínimo. Tabela dentro de tabela dentro de tabela é peso e
  risco.
- Sem tabela fantasma de Outlook por reflexo: só onde resolve um problema
  real.
- Coluna única, com as duas exceções (grade 2×2 e comparativo de 2
  colunas).

### Cards lado a lado com mesma altura

Regra de ouro, em dois passos:

1. **Cor de fundo no `<td>` externo**, nunca num `<div>` ou `<td>`
   interno. O `<td>` externo estica sozinho até a altura da coluna mais
   alta.
2. **Altura fixa em todas as imagens da mesma linha.** O mesmo
   `height:Npx; object-fit:cover;` em cada imagem de produto da linha.
   Nunca `height:auto` em imagens lado a lado.

Quando o texto é que define a altura numa divisão horizontal, use
`background-image` no `<td>` em vez de uma tag `<img>`, sempre com
`background-color` de fallback.

### Bug do vertical-align

Se **qualquer** coluna de uma seção define `vertical-align`, **todas** as
colunas daquela seção precisam definir explicitamente. Do contrário, o
alinhamento quebra de forma difícil de rastrear.

### Empilhamento no celular

Espaço em branco entre tags causa empilhamento indesejado, inclusive
dentro de grupos que não deveriam empilhar. A defesa que funciona é
`font-size:0px` no `<td>` pai.

## 3. Estilo

- **Tudo que importa é inline.** O `<style>` carrega media query e os
  overrides de auto-link, e nada mais.
- A peça precisa estar correta se o `<style>` for removido inteiro.
- Nunca dependa de media query para legibilidade crítica.
- Sem `!important` fora dos overrides de auto-link e dos overrides de
  dark mode.
- Cor de texto e cor de botão **explícitas**, sempre. Cor herdada é o que
  some na inversão forçada.

## 4. Botão

- Bulletproof: `<table>` envolvendo `<a>`, com bloco condicional VML para
  o Outlook.
- Altura de toque mínima de 44px, garantida por padding.
- `background-color` e `color` explícitos no botão e no texto.
- `text-decoration:none` explícito.
- O botão nunca é só imagem. Se for imagem, existe equivalente em texto
  vivo.
- Um destino principal. Repetir o botão duas ou três vezes com o mesmo
  destino é permitido e recomendado em peça longa.

## 5. Imagens

- `alt` decidido em cada imagem: descritivo quando carrega sentido, `""`
  quando é decorativa. Nunca ausente.
- O alt da imagem principal contém a oferta.
- `display:block` e `border:0`.
- `max-width:100%`.
- **Nada de `border-radius` em `<img>`.** Quebra no Outlook.
- Tamanho de export correto, 2× para retina, arquivo enxuto.
- **Linke a imagem hero e as imagens grandes.** Imagem grande sem link
  vira lightbox do Gmail, que abre a imagem no toque em vez de seguir o
  CTA. Logo, espaçador e ícone pequeno podem ficar sem link.
- Peso: teto de 200 KB por imagem, 800 KB no total.

## 6. Auto-link de telefone, data e endereço

Vários clientes detectam telefone, data e endereço no rodapé e embrulham
em link azul próprio. Isso recolore o texto, troca a fonte e quebra o
layout.

Os três overrides ficam **separados**, porque o Gmail remove seletor de
atributo encadeado:

| Cliente | Seletor |
|---|---|
| Apple Mail e iOS | `a[x-apple-data-detectors]` com `color`, `text-decoration` e `font-*` todos em `inherit !important` |
| Gmail | `u + #body a { ... inherit !important }`, com `id="body"` no `<body>` |
| Samsung Mail | `#MessageViewBody a { ... inherit !important }` |

Mais a meta `format-detection` no `<head>`.

Depois de adicionar, **olhe o rodapé renderizado em cada cliente.** Esse
CSS é fácil de escrever e fácil de ser removido pelo cliente; verifique,
não assuma.

## 7. Preheader

- Presente.
- Não repete o assunto.
- Conteúdo oculto não vaza para o corpo visível nem aparece no dark mode.
- **Sem sequência de caracteres invisíveis** para empurrar o texto do
  corpo para fora do preview. É o que a Insider faz, e esconde exatamente
  o que o resumidor de IA e o leitor de tela leem.

## 8. Links

- Todo `href` é URL absoluta.
- Nenhum `href="#"`, nenhum `href=""`, nenhum placeholder.
- Toda merge tag dentro de `href` renderiza com o valor real no teste.
- Parâmetros UTM conforme a convenção da conta. No Omnisend, UTM é por
  bloco de envio, em `PUT /automations/{id}/blocks/{blockID}/utm`, com
  `source`, `medium` e `campaign` substituídos de forma atômica.

## 9. Conformidade, mecânica e não suficiência

Esta skill confirma que o elemento **especificado** está presente e
funciona. Ela não julga suficiência jurídica: isso é decisão do cliente e
do jurídico dele, e varia por país e por setor.

- Link de descadastro presente e **resolvendo**, nunca placeholder.
- No Omnisend, o conteúdo é rejeitado sem ao menos um bloco de texto ou
  HTML contendo `[[unsubscribe_link]]`.
- Bloco de identidade do remetente e endereço físico onde exigido.
- Cabeçalho `List-Unsubscribe`, verificado no `.eml` recebido, não no HTML
  pré-envio.
- Qualquer outro elemento de conformidade que o brief tenha especificado.

Sinalize o que **falta em relação ao que foi especificado**. Não avalie
suficiência estatutária.

## 10. Tamanho

- Alvo de trabalho: abaixo de 90 KB de HTML.
- Aviso: 90 KB.
- Bloqueio: ~102 KB, e o número é **aproximado e a verificar**.
- Se estourou: corte markup morto, corte aninhamento, minifique, e por
  último corte seção. Nunca corte o rodapé legal para caber.

## 11. Personalização

- Teste com **campo vazio**. O comportamento de fallback é dependente do
  banco do ESP e quebra em silêncio.
- No Omnisend, o mecanismo de valor padrão não está documentado e é o TODO
  T1. Enquanto isso, escreva a frase de modo que ela leia bem sem o nome.
- Envio de teste revisado numa caixa de entrada real, com dado real de
  merge. Preview de editor não conta.

## 12. Estados de bloco

Ideia que vem do `chappie/email-design` e que nenhuma pesquisa nossa
cobria: **o bloco pode sair vazio ou curto.**

- Bloco de produto numa seção dinâmica: o que acontece se o recomendador
  devolver 1 produto em vez de 3? E se devolver 0?
- Bloco de avaliação: e se não houver avaliação?
- Bloco de desconto: e se a loja não emitir o código?

Cada bloco de conteúdo dinâmico precisa de um estado definido para vazio.
O padrão da casa: **a seção não aparece**, em vez de aparecer com furo.
Bloco com furo é P04 na prática.

## 13. Provar em cliente real

- **Outlook Windows:** espaçamento, elemento sem `max-width`, buraco de
  imagem de fundo.
- **Outlook para Mac:** teste separado do Windows. Regressão de
  condicional MSO aparece só aqui.
- **Gmail:** `<style>` removido, botão colorido, clipping.
- **Apple Mail e iOS:** melhor suporte, mas confirme o comportamento de
  dark mode em que você está apostando.
- Guarde as provas de render.
