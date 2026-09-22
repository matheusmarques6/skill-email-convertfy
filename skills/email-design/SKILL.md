---
name: email-design
description: Use ao montar, revisar ou fazer QA do HTML de um e-mail: estrutura de tabela, container de 600px, estilo inline, botão bulletproof com VML, compatibilidade com Outlook, comportamento em dark mode, alt de imagem, tamanho do arquivo e clipping do Gmail. Também ao decidir se um padrão visual é vício de IA ou convenção legítima de e-mail. Não escreve copy (isso é email-copy) nem escolhe a estrutura da peça (isso vem do vault).
---

# email-design

Produz e revisa o HTML de um e-mail de e-commerce que renderiza igual no
Outlook, no Gmail e no Apple Mail, sobrevive ao dark mode forçado, e não
tem cara de IA.

Esta skill **usa** as regras anti-vício de design, não as reescreve. A
lista está em `shared/anti-vicios-design.md`. A verificação
determinística é `scripts/lint_email.py`.

Divergências desta skill em relação ao CLAUDE.md: nenhuma.


## Protocolo obrigatório

Esta skill segue `shared/protocolo-de-execucao.md` inteiro. Em resumo:

1. **Ficha e brief (P01, P02).** Le `marcas/<cliente>.md` quando existir.
   Sem ficha e sem brief com **oferta, produto e prazo**, não gera: pede o
   que falta. Campo ausente vira `[FALTA: <campo>]`, nunca invencao.
2. **Anti-vícios.** Aplica `shared/anti-vicios-copy.md`,
   `anti-vicios-design.md`, `anti-vicios-processo.md` e, junto,
   `shared/calibracao.md`, para não reprovar convenção legitima de e-mail.
3. **Gate de lint.** Roda `scripts/lint_copy.py` e `scripts/lint_email.py`
   antes de entregar. **Violacao B: não entrega.** O gate e o exit code.
4. **Leitura do brief.** Antes de gerar, uma linha dizendo o que entendeu.
   Se estiver ambíguo, **uma pergunta só**, juntando tudo que falta.
5. **Só o artefato (C07).** Sem comentario sobre a própria copy, sem
   explicar a escolha, sem variacao que ninguem pediu.
6. **Ordem de trabalho (P08).** intencao (var1) -> estrutura (var2) ->
   variantes do arsenal -> copy por schema. Nunca escreve antes de
   decidir a estrutura.

## Contrato técnico, herdado do CLAUDE.md

Não negociável. Divergir exige declaração explícita.

| Regra | Valor |
|---|---|
| Container | 600px |
| Tabelas | `role="presentation"` em toda tabela de layout |
| Estilo | Inline. `<style>` é reforço, nunca fonte única |
| Botão | Bulletproof, com VML para Outlook |
| Motor de render | Compatível com Outlook (Word) |
| Dark mode | Seguro: nada some nem inverte errado |
| Fundo | Branco |
| Texto | Preto |
| Paleta | **Sem paleta autoral.** Cor da marca só quando o brief exigir, e só em acento |

Regra derivada, formulada melhor pelo `prescott-amelia-agents`:

> **Trate o bloco `<style>` como melhor esforço: a peça tem que funcionar
> se ele for removido inteiro.**

O Gmail remove `<style>` em vários contextos. Se a legibilidade depende de
uma media query, a peça já está quebrada para parte da base.

## A regra mais importante desta skill

Metade dos padrões de "cara de IA" catalogados para a web é **convenção
legítima de e-mail**. Importar lista de web sem filtro quebra o arsenal.

A pesquisa resolve isso com uma coluna de status. Use sempre essa coluna,
nunca a lista bruta.

**Não é vício em e-mail** (§8 da pesquisa, calibração):

- Layout centralizado e coluna única de 600px
- Caixa alta em headline curta, rótulo e botão
- Número grande de oferta ("15% OFF") como elemento visual
- Repetir o mesmo CTA, com o mesmo destino, ao longo da peça
- "Comprar agora", "Aproveitar", "Shop now" como texto de botão
- Frase pronta curta de boas-vindas, quando seguida da oferta
- Um parágrafo de 25 a 40 palavras no e-mail inteiro, quando é a única
  explicação do produto

Um revisor que reprova coluna única centralizada está aplicando régua de
landing page num e-mail. Corrija o revisor, não a peça.

Catálogo completo com a coluna de status:
`references/vicios-de-design.md`.

## Ordem de trabalho

1. **Ler o brief** em `marcas/<cliente>.md`: tipografia principal, fonte
   secundária, cor primária, cor secundária. Se o brief não deu cor, a
   peça fica neutra. O agente não escolhe paleta.
2. **Pegar a estrutura no vault.** As variantes vêm do protocolo de
   seleção em `vault/componentes/_protocolo-de-selecao.md`, nove passos,
   eliminando antes de rankear. Esta skill não inventa estrutura.
3. **Montar a partir de `assets/arsenal/`.** Bloco validado antes de
   bloco novo.
4. **Aplicar o checklist técnico** de `references/checklist-tecnico.md`.
5. **Rodar `scripts/lint_email.py`.**
6. **Fazer a prova de dark mode** com a matriz de
   `references/dark-mode.md`.
7. **Reportar por severidade, do mais grave para o menos.** Diagnosticar
   antes de alterar.

## Severidade

| Nível | Significa |
|---|---|
| **Bloqueia** | Quebra para parte grande da base, ou destrói a mensagem: texto invisível em dark mode, clipping do Gmail, CTA principal quebrado |
| **Alta** | Claramente errado num cliente comum: regressão de Outlook para Mac, logo invisível no escuro, contraste reprovado |
| **Média** | Perceptível, mas limitado |
| **Baixa** | Acabamento |

## Os seis itens que esta skill nunca deixa passar

### 1. Alt descritivo com a oferta, mais uma linha de texto vivo (D17)

Evidência **FORTE** e confirmada. Serve a quatro coisas de uma vez:
entregabilidade (razão texto sobre imagem), acessibilidade, dark mode, e o
resumidor de IA do Gmail e do Apple, que lê texto vivo.

Observação direta na base Trendtrack: preview de e-mail só imagem aparece
como OCR ilegível, do tipo "FCTSFEXTRAWSPGJ RTSWGHJLBSLKMSF". É
literalmente o que o resumidor e o leitor de tela enxergam.

A regra tem três partes:

- **Ao menos uma linha de texto vivo** com a oferta em HTML, fora de
  imagem. Com o valor, o percentual ou o código visível como texto.
- **Alt descritivo** em cada imagem que carrega sentido, e esse alt
  contém a oferta.
- **`alt=""` em imagem decorativa.** Refinamento que vem do
  `email-html-qa-skill`: alt presente e descritivo numa imagem decorativa
  é ruído em leitor de tela. O pior caso não é alt vazio, é **alt
  ausente**: alguns leitores leem o nome do arquivo.

Decida por imagem: descrever, ou silenciar. Nunca omitir o atributo.

### 2. Recursos que quebram (D18)

Bloqueiam. O lint pega:

- `position: absolute`
- `transform:`
- `border-radius` em `<img>`
- `@font-face` sem pilha de fallback
- `<svg>` inline
- Qualquer JavaScript. JS é bloqueado em todo cliente de e-mail. Elemento
  que parece interativo é decorativo e mente para o usuário
- `<mj-accordion>` e `<mj-carousel>`, ou seus equivalentes em HTML puro:
  o suporte de cliente é ruim demais

Duas armadilhas que nenhuma pesquisa nossa cobria e que vêm do
`email-html-qa-skill`:

- **Imagem grande sem link.** O Gmail embrulha imagem não linkada acima de
  um tamanho não documentado no próprio lightbox e abre a imagem no toque,
  em vez de seguir o CTA. Regra segura: **linke a imagem**, principalmente
  a hero. Exceção legítima: logo, espaçador, ícone pequeno.
- **Auto-link de telefone, data e endereço.** Vários clientes detectam e
  embrulham em link azul próprio, o que recolore o texto, troca a fonte e
  quebra o rodapé. Precisa dos três overrides **separados** (Apple, Gmail,
  Samsung), porque o Gmail remove seletor de atributo encadeado. Detalhe
  em `references/checklist-tecnico.md`.

### 3. Dark mode com #121212, nunca #000 puro (D19)

`#121212` no lugar de preto puro. Logo com versão para fundo escuro.

O passo que quase todo mundo pula, e que vem do `email-html-qa-skill`:
**antes de qualquer coisa, descubra se dark mode está sendo mirado.**
Procure as duas metas de opt-in no `<head>`:

```html
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
```

Se estão presentes, a peça declara suporte e precisa ser provada. Se estão
ausentes, o cliente vai decidir sozinho, em geral invertendo à força. Nem
sempre isso é errado, mas precisa ser uma decisão, não um acidente.

Matriz de prova, riscos conhecidos e a distinção entre elemento
fixo-escuro e elemento adaptativo: `references/dark-mode.md`.

**Nota sobre o `<head>`:** o `prescott-amelia-agents` manda não usar
`<!DOCTYPE>`, `<html>`, `<head>` nem `<meta>`. **Descartamos essa regra.**
Sem `<head>` não existe `color-scheme`, não existe `charset` e não existe
`lang`, e a exigência de dark mode seguro do CLAUDE.md fica impossível de
declarar.

### 4. Clipping do Gmail

O Gmail corta a mensagem acima de um tamanho e esconde o que vem depois,
incluindo, no pior caso, o link de descadastro, o que vira problema de
conformidade além de conversão.

**O limite é ~102 KB, e está marcado como a verificar.** O número é citado
por todos os repos e reconfirmado por nenhum deles nesta pesquisa.
`docs/pesquisa/evidencias-publicadas.md` lista "limite exato de 102 KB"
entre os itens a reconfirmar antes de virar citação.

O que a skill faz enquanto isso:

- Orçamento de trabalho: **abaixo de 90 KB** de HTML.
- Aviso a partir de 90 KB.
- Bloqueio a partir de ~102 KB, com o número rotulado como aproximado.
- Ao escrever para cliente: "o Gmail corta mensagens grandes, na casa de
  100 KB", nunca "o limite é 102.400 bytes".

Imagens não contam para o limite do HTML, mas contam para o peso
percebido: teto de 200 KB por imagem e 800 KB no total.

### 5. Contraste (D04, D05)

- Mínimo 4,5:1 em todo par de texto sobre fundo.
- Corpo em `#000000` ou `#1A1A1A`. Cinza claro em corpo é vício com peso
  alto no catálogo.
- Texto sobre cor é branco ou preto, nunca cinza.
- O contraste precisa passar **em modo claro e em modo escuro**. Um par
  que passa no claro pode reprovar depois da inversão forçada.
- Corpo com piso de 14px e 16px preferido; rodapé com piso de 11px. Se a
  copy só cabe abaixo disso, a seção está cheia: corte a copy, não a
  fonte.

### 6. Sem paleta autoral

- Fundo branco. Fundo creme ou bege por padrão é vício de peso alto
  (D03), e é exatamente o que o template do `email-campaign-skill` faz com
  `#FAF7F2`.
- Gradiente roxo para azul e botão índigo ou violeta: proibidos, salvo cor
  da marca (D01).
- Texto em gradiente, glow, glassmorphism e blob "aurora": proibidos,
  porque não renderizam no Outlook **e** marcam IA (D02).
- Avatar de iniciais em gradiente em depoimento: proibido. Foto real do
  cliente, ou nenhuma imagem (D10).
- Um nível de contêiner. Card dentro de card é vício (D11).
- No máximo duas famílias tipográficas: a **tipografia principal** e a
  **fonte secundária**, nomeadas assim no brief.

## Estrutura padrão da peça

```
<!DOCTYPE html>
<html lang="pt-BR" xmlns:v="urn:schemas-microsoft-com:vml" ...>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" ...>
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <meta name="format-detection" content="telephone=no,date=no,address=no,email=no">
    <!--[if mso]> ... PixelsPerInch 96 ... <![endif]-->
    <style> /* media queries e overrides de auto-link, só isso */ </style>
  </head>
  <body id="body" style="margin:0;padding:0;background:#ffffff;">
    preheader oculto
    tabela externa 100%, role=presentation, bgcolor branco
      tabela container 600px, role=presentation
        as seções, na ordem que o vault definiu
```

As 8 categorias de bloco (`header`, `hero`, `body`, `products`, `reviews`,
`cta`, `offer`, `footer`) são as do vault. A ordem e a escolha de variante
vêm do protocolo de seleção, não desta skill.

Lembrete de cobertura: `header` e `cta` têm **zero variantes** no vault
hoje. Zero candidata não é erro. Declare a lacuna conforme
`vault/componentes/lacunas/`. Não invente variante para preencher.

## Coluna única, com duas exceções

Coluna única é o padrão. As únicas exceções permitidas:

- **Grade de produto 2×2**, que empilha em coluna única no celular.
- **Tabela comparativa de 2 colunas**, que também empilha de forma
  previsível.

Regra de cards lado a lado com mesma altura, do `prescott-amelia-agents`:
cor de fundo no `<td>` **externo**, nunca num `<div>` ou `<td>` interno,
porque o `<td>` externo estica até a coluna mais alta. E altura fixa em
todas as imagens da mesma linha, com `object-fit: cover`. Nunca
`height:auto` em imagens lado a lado.

## Gate de entrega

- [ ] `scripts/lint_email.py` sem achado de bloqueio
- [ ] Container de 600px
- [ ] Toda tabela de layout com `role="presentation"`
- [ ] Todo estilo crítico inline
- [ ] Botão bulletproof com VML, altura de toque mínima de 44px
- [ ] `lang` no `<html>` e `charset=utf-8` declarado
- [ ] As duas metas de `color-scheme` presentes, ou a ausência é decisão
      registrada
- [ ] Prova de dark mode feita, com a matriz preenchida
- [ ] Nenhum logo ou ícone transparente em risco de sumir no escuro
- [ ] Toda imagem com `alt` decidido: descritivo, ou `""` se decorativa
- [ ] Ao menos uma linha de texto vivo com a oferta
- [ ] Imagem hero linkada
- [ ] Overrides de auto-link presentes, nos três seletores separados
- [ ] Preheader presente, sem caractere invisível de preenchimento
- [ ] Contraste ≥ 4,5:1 no claro **e** no escuro
- [ ] HTML abaixo de 90 KB
- [ ] Nenhum `position:absolute`, `transform`, `border-radius` em `<img>`,
      `<svg>` inline ou JS
- [ ] `[[unsubscribe_link]]` presente e resolvendo
- [ ] Nenhuma cor fora do brief
- [ ] Nenhum placeholder repetido, nenhuma seção em branco


## Contrato de variante

O **contrato novo e o canonico**. Esta skill só gera no contrato novo.

Das 75 notas de variante do vault, 32 já estao no contrato novo e **43
estao no legado**. Quando o protocolo de seleção escolher uma legada,
converta antes de usar:

```bash
python3 scripts/adaptar_variante_legado.py <slug> --json
```

O adaptador carrega os campos compartilhados, deriva `profundidade` e
aposenta `momento`, `ativa` e os outros campos que sairam do contrato.

**`aliviador` não deriva de nada.** Vem de `shared/aliviador-legado.json`,
que e o registro das decisões humanas. Slug sem entrada la volta como
`[FALTA: decisao humana]` e o adaptador sai com exit code 1.

Variante legada com pendência **não pode ser usada para gerar**: peca a
decisão de `aliviador` ou escolha outra variante. Nunca preencha por
inferencia, nem copie o `aliviador` de uma variante parecida.

Ver `docs/vault/migracao-contrato.md`.

## Referências

| Arquivo | Quando abrir |
|---|---|
| `references/checklist-tecnico.md` | Ao montar ou revisar o HTML |
| `references/dark-mode.md` | Sempre que a peça tiver logo, botão colorido ou fundo que não seja branco liso |
| `references/vicios-de-design.md` | Ao julgar se um padrão é vício ou convenção |
| `shared/anti-vicios-design.md` | Sempre |
| `vault/componentes/_protocolo-de-selecao.md` | Para escolher variante |
