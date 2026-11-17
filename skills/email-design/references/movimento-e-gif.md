# Movimento e GIF

Detalhe da `email-design`. E-mail não roda JavaScript, e quase nenhum
cliente roda animação CSS. O movimento possível é o GIF, e um pouco de
estado de hover no desktop. Por isso este arquivo é mais sobre **quando
não** animar do que sobre como.

Fontes: o framework de decisão do Emil Kowalski (deve animar? qual o
propósito? qual a curva? quanto tempo?), o `animate` do `impeccable` (um
momento de autoria, não efeito espalhado), as proibições de movimento do
`taste-skill`, e D18 (JS, transform). Créditos em `NOTICE.md`.

## Pergunta 1: isto deve se mexer?

A tabela de frequência do Emil, levada para e-mail. A pergunta é: **quantas
vezes a pessoa vê isto?**

| Frequência | Exemplo | Decisão |
|---|---|---|
| Em todo e-mail da loja | Logo, cabeçalho, rodapé, botão | **Nunca anima.** Movimento visto 3 vezes por semana vira ruído |
| Toda campanha | Hero de oferta comum | Quase nunca. Uma foto boa ganha de um GIF médio |
| Momento raro | Lançamento, Black Friday, data da marca | Pode ter um GIF, se ele tem propósito |
| Uma vez na vida do contato | Welcome 1, aniversário, primeira compra | Pode ter um GIF de encanto |

## Pergunta 2: qual é o propósito?

Um GIF precisa responder "por que isto se mexe?" com uma destas:

1. **Mostrar o que uma foto não mostra:** o produto girando, o tecido
   esticando, a tampa abrindo, as quatro cores do mesmo produto.
2. **Mostrar um estado que muda:** a contagem regressiva real, o "antes e
   depois" de um mecanismo (com produto real, não promessa: C02).
3. **Puxar o olho para a oferta** no hero de um momento raro: o número de
   oferta que aparece, o cupom que se revela.

"Fica mais bonito" não é propósito. Se o propósito não é um dos três, vira
foto.

## Pergunta 3: o primeiro quadro funciona sozinho?

O Outlook para Windows (2007 a 2019, e partes do 365) mostra **só o
primeiro quadro** do GIF. Várias pessoas leem com animação reduzida. Então:

- **O primeiro quadro é o quadro mais importante**, não uma tela em branco
  que "entra". O produto já está em cena; a oferta já está legível.
- Nada de quadro inicial preto, fade de entrada ou "carregando".
- Se a mensagem só existe no quadro 12, ela não existe para parte da base.

## Pergunta 4: tempo e curva

Os números do Emil são de interface (menos de 300ms). GIF de e-mail é
explicativo, não de interface, e a pessoa está rolando: o tempo é outro.

| O que | Tempo |
|---|---|
| Cada estado parado (cor do produto, ângulo) | 0,8 a 1,5 s |
| Transição entre estados | 0,2 a 0,4 s |
| Ciclo completo | 3 a 6 s |
| Repetição | Infinita só se o ciclo é calmo; 2 a 3 vezes e para no quadro principal, se é chamativo |

Curva, na hora de produzir o GIF no Figma, After Effects ou ferramenta de
GIF:

- **Entrada de elemento: desacelerando** (ease-out). Começa rápido, assenta
  devagar. É o que parece responsivo.
- **Movimento de algo que já está na tela: acelera e desacelera**
  (ease-in-out).
- **Nunca começar do nada.** Elemento não surge de escala zero: entra de 95%
  com opacidade (Emil: "nada no mundo real aparece do nada").
- **Saída mais rápida que a entrada.**

## Pergunta 5: o peso cabe?

- **Alvo de 500 KB por GIF; 1 MB é o máximo absoluto**, e só em peça com
  pouca outra imagem. No 4G ruim, 1 MB leva segundos, e a pessoa já rolou.
- Menos quadros antes de menos cor. 12 a 24 quadros resolvem quase tudo.
- Paleta de 64 a 128 cores para foto; menos para gráfico chapado.
- Largura de exibição de até 600px; 2x só se o peso couber.
- Um GIF por peça. Dois disputam o olho, e o peso dobra.
- O teto de 800 KB de imagem do e-mail inteiro (`SKILL.md`) conta o GIF.
  Um GIF de 900 KB já estoura sozinho: ou o GIF desce, ou as outras imagens
  descem.

## O que é proibido

| Proibido | Por quê |
|---|---|
| JavaScript, de qualquer tipo | Bloqueado em todo cliente (D18). Elemento que parece interativo e não é mente para a pessoa |
| `transform` e `@keyframes` com `transform` | O lint bloqueia (D18). O Outlook quebra o layout |
| Carrossel e acordeão "interativos" em CSS | Suporte ruim demais (D18) |
| Contagem regressiva sem prazo real | C06, nível 1: nenhum dado revoga |
| Contagem que reinicia a cada abertura | Idem: é prazo falso |
| Piscar mais de 3 vezes por segundo | Risco de convulsão fotossensível (WCAG 2.3.1). Também irrita |
| Texto de corpo em GIF | Some no primeiro quadro, não é lido por leitor de tela, não é selecionável |
| GIF de "seta pulando" apontando para o botão | Enfeite. O botão é que precisa ser óbvio |

## Hover: o único estado "interativo" possível

Funciona no Apple Mail do Mac e em parte dos webmails no desktop. Não existe
no celular, onde está a maioria da base. Então hover é **acabamento, nunca
informação**:

- Escurecer o botão em 8 a 10% no hover. Só cor de fundo.
- Sublinhar o link de texto no hover, se ele não é sublinhado por padrão.
- Nunca esconder informação atrás de hover ("passe o mouse para ver o
  preço").
- Nunca `transform` no hover (o lint bloqueia).

Hover entra no `<style>` do `<head>`, que é melhor esforço: se o Gmail
remover, nada se perde.

```css
@media (hover:hover) {
  .btn:hover { background-color:#2B2B2B !important; }
}
```

O `@media (hover:hover)` vem do Emil: impede que o hover "grude" em tela de
toque, onde o primeiro toque ativa o hover e não o link.

## A contagem regressiva

O único GIF com regra própria, porque é o que mais tenta mentir.

- Prazo real do brief ou da ficha. Hora só se a hora é real (V29).
- Gerada por serviço de contagem com a data e o fuso do mercado da loja.
- O prazo também em texto vivo, embaixo, e no alt.
- O primeiro quadro mostra o tempo restante no momento do envio, que é o
  que o Outlook vai congelar.
- Quando o prazo passa, o GIF mostra "Encerrado" ou o equivalente, não
  zeros piscando.
- HTML em `modulos-ecommerce.md`, módulo 13.

## Revisão de movimento: o formato

Do Emil: revisão de movimento é uma tabela de antes, depois e por quê. Uma
linha por problema.

| Antes | Depois | Por quê |
|---|---|---|
| GIF de 2,4 MB no hero | GIF de 850 KB, 18 quadros, 96 cores | Peso: no 4G a pessoa rola antes de carregar |
| Primeiro quadro em branco, produto entra no quadro 6 | Produto em cena no quadro 1 | O Outlook mostra só o primeiro quadro |
| Três GIFs na peça | Um GIF no hero, o resto em foto | Um movimento por peça; três disputam o olho |
| Seta pulando apontando para o botão | Seta removida, botão maior | Enfeite; o botão é que precisa ser óbvio |

## Verificação

- [ ] O GIF tem um dos três propósitos?
- [ ] O primeiro quadro funciona sozinho?
- [ ] Até 1 MB, e o total de imagem da peça abaixo de 800 KB?
- [ ] Um GIF por peça?
- [ ] Nada pisca mais de 3 vezes por segundo?
- [ ] Contagem regressiva com prazo real, em texto vivo e no alt?
- [ ] Nenhum `transform`, `@keyframes` ou JS (o lint bloqueia)?
- [ ] Hover, se existe, é só acabamento e está dentro de `@media (hover:hover)`?
