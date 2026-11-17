# Cor e contraste

Detalhe da `email-design`. O default da casa é neutro e **o agente não
escolhe paleta** (CLAUDE.md). Este arquivo diz como aplicar a cor que a
ficha dá, com que papel, e como provar que ela passa no claro e no escuro.

Fontes: `colorize` e `quieter` do `impeccable` (cor por papel, raridade dá
força ao acento, nunca cinza sobre cor), travas de consistência do
`taste-skill` (uma cor de ação, uma paleta por peça), D01 a D05, D19, D29,
e a ficha da Blue Wolf como caso real. Todas as razões de contraste abaixo
foram calculadas com a mesma função do `lint_email.py` (luminância relativa
da WCAG 2.x).

## Cor tem papel, não gosto

Antes de pôr uma cor, diga o papel dela. Uma cor sem papel sai.

| Papel | Regime neutro | Regime marca |
|---|---|---|
| Fundo da peça | `#FFFFFF` | `cor_de_fundo` da ficha (o default continua `#FFFFFF`) |
| Título | `#111111` | `#111111`, ou a cor primária se a ficha manda título em cor |
| Corpo | `#1A1A1A` | `#1A1A1A`. **Nunca cor de marca em corpo** |
| Apoio (prazo, legenda, preço "de", rodapé) | `#595959` | `#595959` |
| Ação (botão principal) | `#111111` | Cor primária (ou a secundária, se a ficha diz que botão é a secundária) |
| Link no texto | Cor do texto, sublinhado | Cor de ação, sublinhado |
| Linha divisória | `#E3E3E3` | `#E3E3E3` |
| Alerta (aviso de sistema) | Só se o formato pede, e com o vermelho da ficha | Idem |

### Os cinzas que passam e os que não passam

Sobre branco (`#FFFFFF`). O piso é 4,5:1 para texto de até 18px e 3:1 para
texto grande (24px, ou 18,66px em negrito).

| Cinza | Contraste | Uso |
|---|---|---|
| `#1A1A1A` | 17,40 | Corpo |
| `#333333` | 12,63 | Corpo, quando a ficha pede menos peso |
| `#595959` | 7,00 | **Apoio. O cinza da casa** |
| `#6B6B6B` | 5,33 | Apoio, aceitável |
| `#767676` | 4,54 | O limite. Não use: qualquer arredondamento reprova |
| `#808080` | 3,95 | Reprova em texto normal |
| `#999999` | 2,85 | Reprova sempre. É o "cinza claro de IA" (D04) |

Sobre cinza claro de fundo (`#F5F5F5`), `#6B6B6B` cai para 4,89: passa, sem
folga. Em fundo cinza, use `#595959` ou mais escuro.

## A cor de ação é uma só (D29)

- **Uma cor de botão principal na peça inteira.** O lint avisa quando há
  duas.
- Botão secundário não ganha outra cor: vira link sublinhado ou botão
  fantasma (fundo branco, borda de 2px na cor do texto).
- A cor de ação não aparece em enfeite. Se o botão é vermelho, não há
  divisória vermelha, ícone vermelho e título vermelho: a cor deixa de
  apontar para o clique. É a lição do `impeccable`: raridade é o que dá
  força ao acento.
- Mesma cor do primeiro ao último bloco. Botão azul no hero e verde no fim
  é peça montada de pedaços (`taste-skill`, trava de consistência).

### Testar a cor do botão antes de usar

A cor da ficha nem sempre passa com texto branco. Calcule antes:

| Fundo do botão | Texto branco | Veredito |
|---|---|---|
| `#111111` (neutro) | 18,88 | Passa |
| `#29506D` (navy Blue Wolf) | 8,53 | Passa |
| `#C8102E` (vermelho de oferta) | 5,88 | Passa |
| `#B00020` (vermelho escuro) | 7,33 | Passa |
| **`#4588B9` (azul aço Blue Wolf)** | **3,84** | **Reprova em 16px.** Só passa em texto de 24px ou mais |
| **`#E05252` (alerta Blue Wolf)** | **3,82** | **Reprova em 16px** |
| `#F2C200` (amarelo Black Week) | 1,68 | Reprova. Com texto **preto** dá 12,49 e passa |

O caso da Blue Wolf é o exemplo prático: a ficha diz que a cor secundária
`#4588B9` é a de "botões e destaques", e com texto branco de 16px ela não
passa. As saídas, sem mexer na cor da marca: (1) manter `#4588B9` com
texto **preto** (`#000000`), que dá 5,48 e passa; (2) botão na cor primária
`#29506D` com texto branco, 8,53; (3) levar a questão ao cliente, se
nenhuma das duas serve à marca. **O agente não escurece a cor da
marca por conta própria**: a cor é da ficha; a decisão de mudá-la também.

Regra geral para texto sobre cor: **branco ou preto, nunca cinza** (D05).
Se nenhum dos dois passa, a cor não serve para fundo de texto.

## Regime marca: onde a cor pode ir

O campo `acento_permitido_em` da ficha manda. O default é
`[botao, link, detalhe]`. "Detalhe" quer dizer: borda do cupom, estrelas da
avaliação, número de oferta, sublinhado. Nunca um bloco inteiro.

Fundo de seção em cor (a faixa preta da Black Week, o navy do convite) só
quando a ficha ou o brief aprovado declara. Quando declara:

- Uma faixa de cor por peça, no ponto alto, salvo se a ficha manda a peça
  inteira em fundo escuro (os momentos da Blue Wolf).
- O texto na faixa é branco ou preto, testado com a tabela acima.
- A transição para o branco acontece num ponto natural: depois do hero,
  antes do rodapé. Faixas alternadas são o "blocky" do Max.

### Paleta por momento

Algumas fichas mudam o fundo e o acento conforme o calendário (a Blue Wolf
tem nove momentos, de 10.10 a fim de ano). A regra é a da própria ficha:
**a marca não muda; muda o clima.** Tipografia, logo, rodapé e cor primária
ficam iguais. Na peça:

1. Leia o momento pela data do envio, na tabela da ficha.
2. Use o fundo e o acento do momento. Não misture dois momentos na mesma
   peça.
3. Aviso de sistema, notificação e texto de pessoa ignoram o momento e
   ficam no neutro (a exceção que a própria ficha da Blue Wolf declara).

## Vermelho de oferta

Muita loja usa vermelho para preço e desconto. Pode, com três cuidados:

- Só se a ficha tem um vermelho. O agente não acrescenta vermelho para
  "dar urgência".
- Vermelho em número grande de oferta, nunca em corpo.
- Preço "por" em vermelho e preço "de" riscado em cinza funciona; preço
  "por" em vermelho e botão de outra cor cria duas cores de ação disputando.
  Escolha: ou o preço é vermelho, ou o botão é.

## Dark mode: a cor depois da inversão

O detalhe completo está em `dark-mode.md`. O que importa para cor:

- `#121212` no lugar de `#000000` puro em fundo escuro desenhado (D19).
- Uma cor que passa no claro pode reprovar depois da inversão. Medido sobre
  `#121212`:

| Cor | Sobre `#121212` | Veredito |
|---|---|---|
| `#FFFFFF` | 18,73 | Passa |
| `#F1F1F1` | 16,59 | Passa (o claro seguro de texto em fundo escuro) |
| `#9E9E9E` | 6,99 | Passa, como apoio |
| `#C8102E` (vermelho) | 3,18 | Reprova em texto normal |
| `#29506D` (navy) | 2,20 | Reprova: some |
| `#4588B9` (azul aço) | 4,88 | Passa, sem folga |

  Ou seja: o navy da Blue Wolf, ótimo como botão no claro, **some como texto
  no escuro**. Título em cor primária escura precisa de prova no
  `dark-600.png`.

- Botão com cor sólida sobrevive à inversão melhor que botão com borda
  fina. Borda de 1px em cinza claro desaparece.
- Logo e ícone em PNG transparente preto somem no fundo escuro (R18). Ver a
  troca de logo em `dark-mode.md`.

## O que fazer quando a peça está "barulhenta"

Do `quieter` do `impeccable`, adaptado. Sinais: três cores disputando,
tudo em negrito, fundo diferente a cada bloco.

1. Tire cores sem papel (a cor que só "combina").
2. Uma faixa de cor, não três.
3. Volte títulos secundários para `#111111`.
4. Deixe o acento só no botão e num detalhe.
5. Hierarquia por tamanho e peso, não por cor.

E o contrário, quando a peça está apagada (do `bolder`): primeiro aumente
o contraste de escala (título maior, corpo igual), depois dê ao botão a cor
de ação da ficha. Não acrescente cor nova.

## Verificação (para o ciclo de render)

- [ ] Cada cor da peça tem um papel da tabela de cima?
- [ ] Uma cor de botão só (o lint avisa com D29)?
- [ ] Todo texto passa 4,5:1 (o lint mede D04 e D05 no claro)?
- [ ] Texto sobre cor é branco ou preto?
- [ ] No `dark-600.png`, título em cor de marca continua legível?
- [ ] Nenhuma cor fora da ficha (o lint mede com `--marca`)?
- [ ] No regime marca, a cor está só nos papéis de `acento_permitido_em`,
      ou o fundo de cor está declarado na ficha ou no brief?
