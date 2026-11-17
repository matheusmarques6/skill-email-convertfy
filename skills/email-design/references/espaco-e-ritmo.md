# Espaço e ritmo

Detalhe da `email-design`. O Max credita 3x de receita em teste A/B a
"spacing, sizing and style" (vault, `Conhecimento/Advisors/Max/design/por-que-design-importa.md`;
o número não tem amostra declarada, cite como relato dele). Espaço é a
ferramenta mais barata de hierarquia e a que o agente mais erra: ou cola
tudo, ou espalha valores aleatórios (R15).

Fontes: `layout` do `impeccable` (agrupar por proximidade, contraste entre
intervalos curtos e longos, mais espaço acima do título do que abaixo),
densidade do `taste-skill`, R11, R15, D20 e a transição do Max.

## A escala

Um só conjunto de valores, em px, para padding e espaçador:

```
4   8   12   16   24   32   40   48   64
```

Nada fora dela. 14, 18, 22, 30, 36 e 45 não existem como espaço (existem
como tamanho de fonte, que é outra escala). Se um valor fora da escala
parece necessário, o problema é outro: texto demais, imagem na proporção
errada, ou dois blocos que deviam ser um.

**Variante do vault não se edita.** Ela traz os próprios valores. Entre duas
variantes, o ajuste é o espaçador da escala, nunca mexer no padding dela.

## Os três níveis de espaço

A regra do `impeccable`: **perto o que é junto, longe o que é separado, e
a diferença entre os dois tem que ser óbvia.** Se tudo está a 24px de
tudo, nada está agrupado.

| Nível | Entre o quê | Valor | Exemplo |
|---|---|---|---|
| **Dentro do grupo** | Elementos que se leem juntos | 4 a 12px | Rótulo e número de oferta (8); nome e preço (8); título e proposta (12) |
| **Entre grupos de um bloco** | Partes do mesmo bloco | 12 a 24px | Texto e botão (24); foto e nome do produto (16); cupom e prazo (12) |
| **Entre blocos** | Seções diferentes | 32 a 48px | Fim do hero e início da oferta (40); vitrine e avaliação (40) |

A razão entre o nível de dentro e o de fora tem que ser de **pelo menos
2x**: título a 12px da proposta e a 40px do bloco seguinte lê como grupo;
título a 24px da proposta e a 32px do próximo bloco não lê.

### Mais espaço acima do título do que abaixo

Um título pertence ao que vem depois dele. Por isso:

- Acima de um título de seção: 40px (o espaço entre blocos).
- Abaixo dele, até o texto: 8 a 12px.

Título com o mesmo espaço em cima e embaixo parece flutuar entre dois
blocos, e é um dos sinais mais fortes de peça montada sem olhar.

## Valores padrão por bloco

Padding de referência dos módulos (`modulos-ecommerce.md`), em
`cima direita baixo esquerda`:

| Bloco | Padding | Por quê |
|---|---|---|
| Cabeçalho | 24 24 16 24 | Logo perto do topo; a primeira dobra é cara |
| Imagem do hero | 0 | Largura total, sem moldura |
| Texto do hero | 32 40 0 40 | 40 laterais dão a medida de leitura de 520px |
| Botão do hero | 24 24 40 24 | 24 do texto, 40 até o próximo bloco |
| Oferta | 40 40 0 40 | |
| Produto, grade | 32 24 0 24, e 0 8 32 8 no card | Colunas de 276; calha de 16 entre os cards |
| Avaliação | 40 48 40 48 | Laterais maiores estreitam a citação para 3 linhas |
| Texto de pessoa | 40 48 40 48 | Medida de cerca de 65 caracteres |
| Rodapé | 32 16 16 16, depois 18 24 26 24 | |

No celular, a classe `pad` da `casca-600` troca os laterais por 16px. Use
`class="pad"` em todo bloco de texto com lateral de 32px ou mais, senão o
texto fica numa coluna de 290px no iPhone.

## Ritmo vertical

**Repetição com intenção.** O mesmo espaço entre blocos da mesma natureza
(todos os cards da grade a 32 de distância) cria ritmo. Mudar o espaço
sinaliza mudança de assunto.

**Um pico por peça.** Do `bolder` do `impeccable`: a seção mais importante
pode ter um respiro maior (48 a 64px em volta) para virar o ponto alto da
rolagem. Se toda seção tem 64px, nenhuma é pico.

**Densidade e altura andam juntas.** Densidade baixa usa 48px entre blocos;
densidade alta usa 32px (`direcao-visual.md`). O que nunca muda com a
densidade: o espaço dentro do grupo. Apertar nome e preço não economiza
nada; apertar o espaço entre blocos economiza.

## Primeira dobra: o orçamento mais caro

O celular mostra 667px antes da primeira rolagem (iPhone de tela pequena,
o caso que o `render.py` mede). A carteira manda oferta, cupom, prazo e
botão nos primeiros 500px em e-mail de venda (R21). Isso define o espaço
da parte de cima:

- Cabeçalho até 88px no total. Barra de aviso de 32 a 36px, quando houver.
- Hero com imagem 4:3. A 1:1 empurra o botão para fora da dobra.
- Entre o título e o botão, no máximo 24px de respiro em cada passo.
- Preheader oculto não ocupa espaço; um preheader visível ("Ver no
  navegador") no topo ocupa 30px e quase sempre pode sair.

A conta completa do hero está no módulo 2 de `modulos-ecommerce.md`.

## O espaço no fim da peça

- O rodapé termina com 24 a 32px de respiro. Mais que isso é deserto
  branco (R11).
- Nenhum espaçador depois do rodapé.
- Se a peça ficou curta e sobra branco, corte o espaço; não preencha com
  enfeite (R11, R12: peça anêmica é problema de estrutura).

## Transição entre seções sem "blocky"

O Max chama de "blocky" a peça em que cada seção parece terminar o e-mail
(vault, `doutrina/transicoes-entre-secoes.md`). No regime neutro:

1. **O espaço é a costura.** 32 a 40px entre blocos, sem linha, sem caixa,
   sem fundo diferente: o olho segue para baixo.
2. **O bloco seguinte começa com algo que puxa o olho**: foto ou título.
   Começar com texto pequeno depois de um respiro grande é onde a pessoa
   para.
3. **Fundo de seção diferente em sequência é o que mais cria degrau.**
   Branco, cinza claro, branco, preto, branco: cinco blocos que leem como
   cinco e-mails. Se a ficha permite fundo de cor, uma faixa só, no ponto
   alto.
4. **Divisória só entre itens da mesma natureza** (dois produtos em linha).
   Entre seções diferentes, a linha vira "fim".

Os métodos de gradiente e de forma por trás da foto, que o Max prefere,
existem apenas dentro de uma imagem desenhada assim, por decisão de direção
de arte da ficha. Em HTML, gradiente é bloqueado (D02).

## Espaçador: a técnica

Quando o espaço não cabe no padding de nenhum vizinho (por exemplo, entre
duas variantes do vault):

```html
<tr>
  <td height="32" style="height:32px;font-size:0;line-height:0;mso-line-height-rule:exactly;background:#FFFFFF;">&nbsp;</td>
</tr>
```

- `height` no atributo e no estilo: o Outlook lê um, os outros leem o
  outro.
- `font-size:0` e `line-height:0`: sem isso, o Outlook estica a linha até a
  altura de uma linha de texto (cerca de 19px), e um espaçador de 8 vira de
  19.
- O `&nbsp;` impede alguns clientes de colapsar a célula vazia.
- Fundo igual ao dos vizinhos, senão o espaçador vira faixa.

Nunca `<br><br>` como espaço: cada cliente dá uma altura diferente.

## Verificação (para o ciclo de render)

- [ ] Todo padding e espaçador está na escala (4, 8, 12, 16, 24, 32, 40, 48,
      64)?
- [ ] Nos PNGs, os grupos se leem como grupos: nome e preço juntos, título
      e texto juntos, blocos separados?
- [ ] Algum título tem tanto espaço embaixo quanto em cima?
- [ ] No `mobile-375.png`, o botão do hero termina antes de 667px?
- [ ] Algum ponto da peça parece o fim do e-mail antes do rodapé?
- [ ] Mais de uma tela de branco em algum lugar (R11)?
- [ ] Há um ponto alto, ou todas as seções têm o mesmo peso?
