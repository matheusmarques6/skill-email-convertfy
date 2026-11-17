# Direção visual: ler o pedido antes de desenhar

Detalhe da `email-design`. É o passo que vem **antes** do HTML: decidir que
cara a peça vai ter, com que densidade, quanto peso de imagem e quanta
marca. Sem esse passo o agente cai no default dele, que é a cara de IA.

Fontes: a postura do CLAUDE.md (indistinguível de peça de produção), a
leitura de brief e os dials do `taste-skill`, a ideia de "modo" do
`impeccable`, a doutrina de design do Max no vault (Conhecimento/Advisors/Max/design)
e o design system real da Blue Wolf em `fontes/BFCM-2026-Convertfy/07_Design_Blue_Wolf/`.
Tudo reescrito para e-mail de e-commerce. Créditos em `NOTICE.md`.

## A pergunta que decide tudo

> Uma peça de produção desta loja, neste momento do calendário, para esta
> lista, teria que cara?

Não "o que fica bonito", nem "o que impressiona". O alvo é a peça que um
designer bom da própria loja faria numa terça-feira. Quando "impressionante"
e "indistinguível de peça real" brigam, ganha a segunda (CLAUDE.md).

## Passo 1. A leitura de design, em uma linha

Antes de gerar, escreva uma linha neste formato e mostre junto com a
leitura do brief do protocolo (item 4 de `protocolo-de-execucao.md`):

```
Leitura de design: <tipo de e-mail> para <lista>, no regime <neutro|marca>,
densidade <baixa|média|alta>, peso de imagem <baixo|médio|alto>,
apoiado em <variante do vault | ficha da marca | referência do brief>.
```

Exemplos:

- "Leitura de design: campanha de pico (Black Week) para a lista inteira,
  no regime marca, densidade média, peso de imagem alto, apoiado na ficha
  da Blue Wolf (paleta Black Week)."
- "Leitura de design: texto de fundador para compradores, no regime neutro,
  densidade baixa, peso de imagem baixo, apoiado no modelo validado
  texto-pessoa."
- "Leitura de design: carrinho abandonado de um item, no regime neutro,
  densidade baixa, peso de imagem médio, apoiado na variante do vault."

Se a leitura não fecha com o brief (o brief pede festa, a ficha pede
sobriedade), é ambiguidade: **uma pergunta só**, como manda o protocolo.

## Passo 2. Qual regime: neutro ou marca

A casa tem dois regimes, e o agente não escolhe entre eles: **a ficha
escolhe**.

### Regime neutro (o default)

Vale quando `marcas/<cliente>.md` não existe, ou tem `usa_cor_de_marca:
false`.

- Fundo branco, texto preto (`#111111` a `#1A1A1A`), cinza de apoio
  `#595959`.
- Botão preto ou quase preto. Nenhuma cor de acento.
- Tipografia de texto vivo na pilha segura (`Helvetica, Arial`).
- A personalidade vem de três lugares só: a **foto**, a **copy** e a
  **hierarquia**. Não de cor, não de enfeite.

Isto não é peça sem graça. É a peça de loja que confia no produto. Na
própria carteira, o neutro já ganhou de peça colorida: na Blue Wolf, uma
loja com paleta forte, os avisos de sistema em fundo branco e texto preto
tiveram os maiores cliques do trimestre, 3,61% e 3,20%
(`fontes/BFCM-2026-Convertfy/07_Design_Blue_Wolf/03_PALETAS_POR_MOMENTO.md`).

### Regime marca

Vale quando a ficha tem `usa_cor_de_marca: true` e os hex preenchidos, ou
quando o brief da campanha traz direção de arte aprovada (a paleta por
momento da Blue Wolf é o exemplo de referência).

- A cor primária e a cor secundária da ficha entram nos papéis que a ficha
  declara (`acento_permitido_em`). O default continua sendo acento: botão,
  link, detalhe.
- **Fundo de seção em cor só se a ficha ou o brief disser.** A Blue Wolf
  usa fundo escuro por momento, e isso está escrito na ficha; outra loja
  não herda isso por analogia.
- Tipografia da marca: na imagem e, quando a ficha nomeia, na frente da
  pilha do texto vivo (ver `tipografia.md`).
- Aviso de sistema, notificação e texto de pessoa **voltam ao neutro**
  mesmo no regime marca. A cara de sistema é o que faz esses formatos
  funcionarem.

### O que nunca acontece em nenhum dos dois

- O agente inventar paleta ("vou usar um verde-sálvia que combina").
- Cor da marca em texto corrido.
- Mistura dos dois regimes na mesma peça sem a ficha mandar (metade neutra,
  metade colorida é R19, "dois registros").

## Passo 3. Os três dials de e-mail

Adaptados dos dials do `taste-skill`. Na web eles vão de 1 a 10; em e-mail
a faixa útil é estreita, e por isso aqui são três níveis.

| Dial | Baixa | Média | Alta |
|---|---|---|---|
| **Densidade** (quanto cabe por tela) | Uma ideia por tela, respiro de 48 a 64px entre seções, 1 a 3 blocos | Respiro de 32 a 40px, 4 a 6 blocos | Respiro de 24 a 32px, vitrine com 6+ produtos, 7+ blocos |
| **Peso de imagem** (quanto da peça é foto) | Nenhuma ou uma foto pequena; o texto carrega | Hero com foto e produtos em foto | Hero de campanha, foto em quase todo bloco, GIF permitido |
| **Intensidade de marca** | Neutro puro | Acento de marca no botão e no detalhe | Paleta de momento da ficha, fundo de cor, display da marca |

**Intensidade de marca alta só existe no regime marca.** No regime neutro o
dial está travado em baixa.

### Presets por tipo de e-mail

Ponto de partida. A ficha e o brief podem mover um nível para cada lado, e
a linha de leitura diz qual foi movido e por quê.

| Tipo de e-mail | Densidade | Peso de imagem | Marca |
|---|---|---|---|
| Texto de pessoa, fundador, gerente | Baixa | Baixo | Baixa |
| Aviso de sistema, notificação, "status mudou" | Baixa | Baixo | Baixa |
| Cupom liberado, acesso liberado | Baixa | Médio | Média |
| Welcome 1 (oferta de entrada) | Média | Médio | Média |
| Carrinho e checkout abandonado | Baixa | Médio | Baixa |
| Lançamento de um produto | Baixa | Alto | Média |
| Coleção, mais vendidos, catálogo | Alta | Alto | Média |
| Antecipação de data (convite, lista VIP) | Média | Médio | Alta |
| Pico (Black Friday, 11.11, dia da data) | Média | Alto | Alta |
| Última chamada | Baixa | Médio | Média |
| Pós-compra, pedido de avaliação | Baixa | Baixo | Baixa |
| Newsletter e conteúdo | Média | Médio | Média |

### O que cada nível muda na prática

- **Densidade baixa:** coluna única de leitura (500 a 520px de texto),
  nenhuma grade, no máximo um bloco de prova. O teste é: dá para ler a peça
  inteira em duas rolagens no celular?
- **Densidade alta:** grade 2x2 ou 2x3, faixa de garantias, rodapé com
  categorias. O risco é passar do teto de altura (tabela em
  `modulos-ecommerce.md`): densidade alta pede blocos curtos, não mais
  blocos.
- **Peso de imagem baixo:** o hero pode ser só texto (título grande e
  botão). Isto é legítimo e é o formato de maior clique da carteira nos
  avisos.
- **Peso de imagem alto:** toda imagem precisa de alt descritivo, e a
  oferta continua em texto vivo (V02). Peso alto nunca significa e-mail
  inteiro em imagem.

## Passo 4. Os defaults de IA que precisam ser recusados

São os padrões que o modelo produz quando não decide. Cada um tem ID no
catálogo; aqui está o reflexo, para reconhecer antes de escrever.

| O reflexo | Por que é default de IA | O que fazer |
|---|---|---|
| Hero centralizado com gradiente escuro e título branco | É a "landing de startup" transplantada | Hero com foto real e texto vivo embaixo (módulo 2), ou só texto |
| Três cards iguais com ícone, título e duas linhas | Faixa de "features" de SaaS | Faixa de garantias em linhas (módulo 10), ou nada (D08) |
| Pílula acima de cada título ("NOVIDADE", "EXCLUSIVO") | Ritmo de template | Rótulo só com prazo ou condição, no máximo um a cada três seções (D07) |
| Fundo creme com acento dourado em marca "premium" | O palpite de "luxo" do modelo | Branco, ou a cor que a ficha nomear (D03) |
| Botão roxo, azul-índigo ou gradiente | A cor padrão de componente de UI | Preto no neutro, cor primária no marca (D01) |
| Estatística redonda decorativa ("10k+ clientes felizes") | Número que soa real | Número só do `brief_numbers` (C02, D09) |
| Depoimento com avatar de inicial | Placeholder que virou estilo | Foto real ou nenhuma (D10) |
| Divisória ornamental entre todo bloco | Enfeite para parecer "desenhado" | Espaço separa; linha só entre itens da mesma natureza (R22) |
| Emoji como ícone de lista | Atalho de ícone | Texto, ou ícone PNG de linha da própria marca |
| Seção "Por que escolher a gente" com 4 bullets | Estrutura de landing | A estrutura vem do vault, não do reflexo (D16) |
| Repetir o mesmo layout de bloco três vezes seguidas | Falta de decisão | Variar natureza do bloco: foto, texto, prova (regra de vizinhança abaixo) |

## Passo 5. Regras de vizinhança entre blocos

Adaptadas do `taste-skill` (repetição de layout e ziguezague) e da regra de
transição do Max (o e-mail não pode parecer "blocky", com pontos onde a
pessoa acha que acabou).

1. **Dois blocos de mesmo layout seguidos, no máximo.** Três "foto à
   esquerda, texto à direita" em sequência viram ladainha. Quebre com um
   bloco de largura total.
2. **Ziguezague (foto à esquerda, depois à direita) só uma vez por peça.**
3. **Cada bloco de meio tem natureza diferente do anterior** (o eixo `meio`
   do vault já pede isso: mecanismo, prova, catálogo, comparação).
4. **O fim de um bloco não pode parecer o fim do e-mail.** Se depois do
   botão vem um respiro de 80px e uma linha, a pessoa para ali. Respiro
   entre seções sai da escala (`espaco-e-ritmo.md`), e o bloco seguinte
   começa com algo que puxa o olho (título ou foto), não com uma linha
   solta.
5. **No regime neutro, a transição é o espaço e a foto.** Gradiente entre
   seções (o método 1 do Max) não renderiza no Outlook e é bloqueado (D02).
   A "transição atrás da foto", o favorito dele, só existe dentro de uma
   imagem já desenhada assim, que é decisão de direção de arte da ficha.

## Passo 6. O teste de especificidade

Vem do `impeccable` ("design specificity") e coincide com o PQ2 do padrão
de qualidade. Depois do render:

> Se eu trocar o logo e o nome desta peça pelo de outra loja da carteira,
> ela continua fazendo sentido?

Se continua, a peça é genérica. As correções, em ordem de custo:

1. Foto do produto real da loja no hero, em vez de cena genérica.
2. Um fato que só esta loja pode dizer na proposta de valor (o produto que
   esgotou, o prazo de entrega real, a avaliação real).
3. A tipografia e o acento da ficha, quando o regime é marca.

Nunca "mais enfeite". Especificidade vem de fato, não de decoração.

## Passo 7. O teste de apertar os olhos

Do `impeccable` (squint test), aplicado ao `desktop-600.png` e ao
`mobile-375.png`:

> Desfoque a captura (ou afaste o rosto). Ainda dá para dizer qual é o
> elemento principal, qual é o secundário e onde estão os grupos?

- O principal na primeira tela tem que ser a oferta ou o produto, e o
  segundo tem que ser o botão.
- Se três coisas pesam igual, a hierarquia está achatada (R14). Corrija
  diminuindo o que não é principal, não aumentando o principal.

## Quando o pedido é refazer um template que a loja já usa

O `taste-skill` separa "preservar" de "reformar". Em e-mail, quase sempre é
preservar: a loja tem um rodapé, um cabeçalho e uma cara que a lista
reconhece.

**Audite antes de mexer:** o que existe (cabeçalho, rodapé, botões, fontes,
cores), o que funciona (pergunte pelo e-mail que mais vendeu), o que é vício
(pelo catálogo D e R).

**Alavancas, nesta ordem. Pare quando o problema estiver resolvido:**

1. Tipografia: escala e hierarquia (`tipografia.md`). Maior ganho por
   menor risco.
2. Espaço e ritmo (`espaco-e-ritmo.md`).
3. Botão: tamanho, contraste, posição na primeira dobra.
4. Cor: tirar o que não tem papel; manter o acento da marca.
5. Hero: recompor a primeira dobra.
6. Trocar o bloco inteiro: só quando nada acima resolve.

**Nunca mudar sem aprovação explícita:** logo e wordmark, texto legal do
rodapé, endereço do remetente, merge tags e seus fallbacks, parâmetros de
UTM e nomes de link que alimentam relatório, e a ordem de blocos de uma
estrutura validada pela carteira (o prompt mestre da Blue Wolf diz o mesmo:
"mudar a estrutura de um e-mail validado sem avisar" está na lista do que
evitar).

## O que este arquivo não faz

- Não escolhe estrutura. Isso é o vault.
- Não escolhe paleta. Isso é a ficha.
- Não substitui o render. A leitura de design é uma hipótese; o render é a
  prova.
