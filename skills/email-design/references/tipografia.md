# Tipografia de e-mail: papéis, escala, pilhas e fonte em imagem

Detalhe da `email-design`. Vale para texto vivo (HTML) e para texto dentro
de imagem, que têm regras diferentes porque o celular trata os dois de
forma diferente.

Nomenclatura obrigatória (CLAUDE.md): **tipografia principal** e **fonte
secundária**. Nunca "fonte primária", "heading font" ou "display" numa spec.

Fontes: `typeset` do `impeccable` (papéis antes de tamanhos, medida de
leitura, compensação em fundo escuro), disciplina de display e de serifa do
`taste-skill`, escala real da Blue Wolf (`02_DESIGN_SYSTEM_BLUE_WOLF.md`),
D12 a D14 e D26 a D28 do catálogo. Créditos em `NOTICE.md`.

## A regra que quase todo mundo erra

**Texto vivo não encolhe no celular. Texto em imagem encolhe.**

- Um título em HTML de 34px continua com 34px num iPhone. Ele quebra em
  mais linhas, mas não diminui. Por isso o tamanho do texto vivo é
  escolhido pensando no celular.
- Uma imagem de 600px desenhada com texto de 16px é reduzida para caber na
  tela. Num iPhone de 375px, ocupando a largura toda, a escala é 0,625 e o
  texto vira **10px**. Com respiro lateral, ou num aparelho de 320px, a
  escala cai para perto de 0,55 e o texto vira 9px. Ilegível.

A conta para texto dentro de imagem desenhada a 600px, pela escala do pior
caso comum (0,57):

| Papel do texto na imagem | Tamanho no Figma (600px) | Vira no celular (×0,57) |
|---|---|---|
| Corpo, condição, prazo | **28px no mínimo** | 16px |
| Legenda, rótulo | 22px no mínimo | 12,5px |
| Título | 44px ou mais | 25px |
| Número de oferta | 80px ou mais | 46px |

É o motivo técnico de a casa preferir texto vivo: a escala mínima da Blue
Wolf (corpo de 15 a 16px em 600) está certa para texto vivo e **pequena
demais para texto dentro de imagem**. Quando o design sai em fatias de
imagem (o método do Max), essa tabela vale para cada fatia.

## Os papéis, antes dos tamanhos

Defina primeiro quais papéis a peça usa. A maioria usa cinco ou seis. Cada
papel tem um tamanho, um peso e uma entrelinha, e o mesmo papel é idêntico
na peça inteira.

### Escala de texto vivo (pilha neutra, container de 600px)

| Papel | Tamanho | `line-height` | Peso | Observação |
|---|---|---|---|---|
| Número de oferta | 56 a 72px | 1,05 (60 a 76px) | Negrito | Até 9 caracteres ("15% OFF", "R$ 50") |
| Título de hero (h1) | 30 a 36px | +6px (36 a 42px) | Negrito | Até 40 caracteres (D13) |
| Título de seção (h2) | 22 a 26px | +6px (28 a 32px) | Negrito | Até 50 caracteres |
| Proposta de valor, subtítulo | 17 a 18px | 26px | Regular | Uma frase, até 20 palavras |
| Corpo | **16px** (piso 14) | 24 a 26px | Regular | D26: piso de 14px, o lint avisa |
| Nome de produto | 16 a 17px | 22 a 24px | Negrito | Até 40 caracteres em grade |
| Preço "por" | 16 a 18px | 22 a 24px | Negrito | O número que a pessoa procura |
| Preço "de" | 14 a 15px | igual ao "por" | Regular, riscado | Cinza `#595959` |
| Botão | 15 a 16px | 20px | Negrito | 1 a 3 palavras, caixa alta opcional, `letter-spacing` 1px |
| Rótulo, selo, legenda | 12 a 13px | 16 a 18px | Negrito | Até 6 palavras; caixa alta com `letter-spacing` 1 a 2px |
| Rodapé | 12px (piso 11) | 18 a 20px | Regular | D26: piso de 11px |

### As razões que importam

- **Título de hero ÷ corpo ≥ 2** (D12). 34 ÷ 16 = 2,1. Abaixo disso, a
  hierarquia fica achatada (R14).
- **Dois tamanhos vizinhos não podem estar a menos de 2px um do outro** com
  papéis diferentes. 16 e 15 lado a lado parecem erro, não decisão. Se dois
  papéis estão perto em tamanho, diferencie por peso ou cor.
- **No máximo 5 tamanhos na peça inteira** (fora o número de oferta). Mais
  que isso é coleção de valores, não escala.
- **No máximo 3 pesos:** regular, negrito e, quando a tipografia principal
  tem, um intermediário. Fino (300 ou menos) em texto vivo some no Windows.

### Comprimento de linha

- Corpo entre **45 e 75 caracteres por linha.** Num container de 600px com
  respiro lateral de 40px sobram 520px: a 16px em Helvetica são cerca de 65
  caracteres. É o ponto certo.
- Respiro lateral de 24px (552px úteis) dá cerca de 75 caracteres a 16px: é
  o limite. Texto corrido com respiro menor que isso cansa.
- No celular, a 16px numa largura de 343px, são cerca de 40 caracteres. Por
  isso parágrafo de e-mail tem 2 a 3 frases, não 6.

### Alinhamento

- Título, proposta curta e botão: centralizados (convenção de e-mail, §8).
- **Texto corrido de 3 linhas ou mais: à esquerda.** Centralizar parágrafo
  longo é R16.
- Nunca justificado. Em coluna estreita, justificar abre rios de espaço.

## A entrelinha e o Outlook

O Outlook (motor do Word) calcula `line-height` de outro jeito e, sem
instrução, abre espaço extra acima de títulos grandes ou corta o topo das
letras.

1. `line-height` **sempre em px** em título e número de oferta. Em fator
   (1,2) o Outlook arredonda diferente.
2. `mso-line-height-rule:exactly` em todo título, número de oferta e
   espaçador.
3. Em fundo escuro, dê **2px a mais** de entrelinha e use um peso acima
   (regular passa a semibold). Texto claro em fundo escuro parece mais fino
   e mais apertado (`impeccable`, compensação em fundo escuro).
4. Itálico com descendente (`g`, `j`, `p`, `q`, `y`) num título com
   `line-height` 1,0 corta a perna da letra. Mínimo 1,1 em itálico.

## Pilhas de fonte (texto vivo)

Boa parte da base **não vê a fonte web**. Gmail (web e app) e Outlook
para Windows usam a fallback; Apple Mail, iOS, Outlook para Mac e Samsung
Mail carregam. Como o Gmail sozinho costuma ser a maior fatia de uma lista
de e-commerce, desenhe para a fallback e trate a fonte web como bônus.
Então:

- A pilha começa pela fonte da marca e termina numa fonte segura que se
  pareça com ela.
- **Toda `font-family` termina em família genérica** (`sans-serif`,
  `serif`). Sem fallback, o Outlook cai em Times New Roman.
- O `@font-face` ou o `<link>` da fonte web fica no `<head>`; sem pilha de
  fallback no texto, o lint bloqueia (D18).

| Se a tipografia principal da marca é... | Pilha de texto vivo |
|---|---|
| Sem fonte nomeada (regime neutro) | `Helvetica,Arial,sans-serif` |
| Grotesca neutra (Inter, Helvetica Now, Neue Haas, Söhne) | `'Nome',Helvetica,Arial,sans-serif` |
| Geométrica (Montserrat, Poppins, Futura, Gilroy) | `'Nome','Century Gothic',Arial,sans-serif` |
| Humanista (Open Sans, Lato, Source Sans) | `'Nome','Segoe UI',Tahoma,Arial,sans-serif` |
| Condensada de título (Bebas, Oswald, Tusker) | `'Nome','Arial Narrow',Arial,sans-serif`, **só em título**, nunca em corpo |
| Serifa de texto (Georgia, Lora, Merriweather) | `'Nome',Georgia,'Times New Roman',serif` |
| Serifa de display (Playfair, Canela, Freight) | `'Nome',Georgia,serif`, só em título de 24px ou mais |

Exemplo, Blue Wolf (Montserrat como tipografia principal):

```html
style="font-family:'Montserrat','Century Gothic',Arial,sans-serif;"
```

E no `<head>`, quando a loja hospeda a fonte ou usa o Google Fonts:

```html
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
<!--<![endif]-->
```

O `<link>` fica dentro do condicional `!mso` porque o Outlook do Windows,
ao ver uma fonte web que não consegue carregar, às vezes abandona a pilha
inteira e cai em Times.

### Fonte condensada e de display

Condensadas (Tusker, Bebas, Anton) e displays largas (Stretch Pro) só
funcionam como desenhadas, e quase nenhum cliente as carrega. **Na prática
vivem em imagem**: o título de seção da Blue Wolf em Tusker é uma imagem
com alt, e o texto vivo ao lado é Montserrat ou a fallback.

Se o título condensado for texto vivo, o fallback (`Arial Narrow`, ou
Arial) muda a largura do texto: um título que cabia em uma linha em Tusker
ocupa duas em Arial. Teste com a fallback, não com a fonte.

### Duas famílias, no máximo (D28)

A **tipografia principal** e a **fonte secundária** da ficha. O lint conta
a primeira família de cada pilha e avisa a partir de três (Arial e
Helvetica contam como uma, porque são a mesma escolha de fallback).

Quando a ficha lista mais (a Blue Wolf tem principal, secundária, display,
apoio e wordmark), as extras vivem em imagem: no HTML aparecem só a
principal e a secundária.

## Serifa: quando sim

Do `taste-skill`, adaptado: serifa não é atalho para "premium". O reflexo
"marca de luxo, então serifa" é um dos padrões de IA mais reconhecíveis.

Serifa entra quando **uma** destas é verdade:

1. A ficha nomeia uma serifa como tipografia principal ou fonte secundária.
2. O site e as peças aprovadas da loja já usam serifa nos títulos.

Fora disso, a pilha neutra. E uma palavra em serifa no meio de um título
sem serifa, para "dar charme", é amador: ênfase se faz com negrito ou
itálico da mesma família.

## Caixa alta e espaçamento entre letras

- Caixa alta em título curto, rótulo e botão não é vício em e-mail (§8).
- Texto em caixa alta com mais de 6 palavras cansa: vira caixa baixa.
- Caixa alta pede `letter-spacing` positivo: 1px em botão, 1 a 2px em
  rótulo de 12 a 13px, 0 a 0,5px em título grande.
- **Nunca espaçamento negativo em corpo.** Em título de 30px ou mais, até
  -0,5px (cerca de -0,02em, D14). Mais apertado que isso, as letras colam
  no Windows.

## Números, preço e data

- Moeda e formato da ficha (`moeda`, `idioma`): `R$ 149,90` (pt-BR),
  `$149.90` (en-US), `£149.90` (en-GB), `149,90 €` (de, fr, it, es, pt-PT).
- Espaço inseparável (`&nbsp;`) entre a moeda e o número, para "R$" nunca
  ficar sozinho no fim da linha.
- Desconto em percentual sem espaço: "15% OFF". "15 % OFF" quebra.
- Data e hora no formato do mercado: "domingo, 23h59" (pt-BR),
  "Sunday, 11:59 PM" (en-US). A hora só se é real (V29).
- Preço sempre em texto vivo. Preço só dentro da imagem some com imagem
  bloqueada e não aparece no resumidor de IA.

## Ênfase dentro do texto

- Negrito para o que a pessoa precisa achar ao passar o olho: valor,
  código, prazo. No máximo um trecho em negrito por parágrafo.
- Sublinhado é reservado para link.
- Itálico só para nome de coleção ou citação curta.
- Cor diferente no meio da frase só no regime marca, e só na cor de acento.

## Verificação (para o ciclo de render)

Responda cada uma olhando o PNG, não o código:

- [ ] No `mobile-375.png`, o título do hero tem 3 linhas ou menos?
- [ ] Algum texto parece menor que o corpo de uma mensagem de WhatsApp? É
      corpo abaixo de 14px, ou texto em imagem abaixo da tabela de cima.
- [ ] Os papéis são reconhecíveis sem ler: título, corpo, preço, rótulo?
- [ ] O mesmo papel tem o mesmo tamanho em toda a peça?
- [ ] Algum botão quebrou o texto em duas linhas?
- [ ] O texto corrido de 3+ linhas está à esquerda?
- [ ] No `dark-600.png`, algum texto fino ficou ilegível?
- [ ] O `lint_email.py` está sem D26 e sem D28? Se avisou, a exceção está
      justificada no relatório.
