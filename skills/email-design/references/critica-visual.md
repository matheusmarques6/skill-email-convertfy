# Crítica visual: o olhar de diretor de arte no ciclo de render

Detalhe da `email-design`. É o que fazer com os três PNGs do
`render.py` nas rodadas 1 a 3 do ciclo (`ciclo-de-render.md`): um método
para **achar** o que está errado no design, por eixo, e transformar cada
achado num ID que o revisor consegue conferir.

**Isto não é a nota.** A nota de 0 a 10 é do `email-revisor`, em contexto
limpo, com as regras de cálculo dele. A crítica daqui é o trabalho de quem
monta a peça, antes de entregar ao revisor. Ela usa os mesmos IDs (D, R,
PQ, V), para que o revisor encontre menos, não coisas diferentes.

Fontes: o `critique` do `impeccable` (duas avaliações isoladas, veredito de
especificidade, personas, P0 a P3, prioridade antes de quantidade), o
formato antes/depois/por quê do Emil Kowalski, o pré-voo do `taste-skill` e
`shared/postura-revisao.md`. Créditos em `NOTICE.md`.

## Duas leituras, nesta ordem

O `impeccable` separa a avaliação de design da evidência mecânica, para que
o número do detector não ancore o julgamento. Aqui:

1. **Primeiro, a leitura de design**, só com os PNGs e a ficha. Sem abrir o
   relatório do lint. Anote os achados por eixo (abaixo).
2. **Depois, a evidência mecânica**: `lint_email.py`, `lint_copy.py` e o
   `relatorio.md` do render. Cruze. Anote o que um pegou e o outro não.

Se o lint achou algo que a leitura de design não viu, o olho estava
apressado. Se a leitura achou algo que o lint não tem, é achado de R11 em
diante, que só o olho pega: é exatamente o trabalho desta etapa.

## Os oito eixos

Cada eixo tem a pergunta, onde olhar, e os IDs em que o achado vira
registro. Dê a cada eixo uma marca de **0 a 4** para se orientar (4 =
excelente; a maioria das peças reais fica entre 2 e 3). A marca é
ferramenta de quem monta, não vai para a nota.

| # | Eixo | A pergunta | Onde olhar | IDs |
|---|---|---|---|---|
| 1 | **Primeira dobra** | Dá para saber o que é, quanto vale, até quando e onde clicar sem rolar? | Cubra abaixo de 500px no desktop e abaixo de 667px no mobile | R08, R10, R21, PQ1 |
| 2 | **Hierarquia** | Apertando os olhos, aparece o principal, o secundário e os grupos? | `desktop-600.png` desfocado | R14, D12, D13 |
| 3 | **Tipografia** | Os papéis são reconhecíveis? Algum texto pequeno demais? | `mobile-375.png` em tamanho real | D26, D28, D14, R16 |
| 4 | **Espaço e ritmo** | Grupos juntos, blocos separados, algum ponto parece o fim? | Rolar o `mobile-375.png` inteiro | R11, R15, D20 |
| 5 | **Imagem** | Foto real, assunto claro, proporções iguais na grade, nada essencial só na imagem? | As três capturas | D15, D17, D21, D25, R20, V02 |
| 6 | **Clique** | O botão parece botão, é um só por intenção, o polegar acerta? | `mobile-375.png` | R17, D29, D30, PQ4 |
| 7 | **Cor e dark mode** | Cada cor tem papel? Algo some ou vira bloco no escuro? | `dark-600.png` lado a lado com o claro | D01 a D05, D19, R18, R19 |
| 8 | **Especificidade** | Trocando o logo, a peça serve para outra loja? | Leia só o hero e o primeiro bloco | PQ2, D16, R12, D15 |

### O veredito de especificidade vem primeiro

O `impeccable` manda começar pela especificidade, e aqui também. Antes de
qualquer detalhe, uma frase:

> "Esta peça é desta loja porque ______." ou "Esta peça serve para qualquer
> loja de <categoria>."

Se a frase sai com o segundo formato, o problema é de conteúdo (PQ2: o fato
que só esta loja diz) ou de estrutura (D16, R12), e nenhum ajuste de pixel
resolve. Volte à copy ou ao vault antes de polir.

## As personas de e-mail

O `impeccable` testa a interface pelos olhos de usuários diferentes. Para
e-mail de e-commerce, cinco leitores cobrem quase toda a base. Escolha dois
ou três por peça e percorra a ação principal com cada um, anotando o que
quebra **para ele**, com o elemento exato.

### Carla, celular numa mão, no ônibus
Abre no app do Gmail, rola com o polegar, dá 3 segundos para a peça.
- O botão está na primeira tela e no alcance do polegar (centro, embaixo)?
- O texto é legível sem dar zoom (16px vivo; texto em imagem pela tabela
  de `tipografia.md`)?
- A grade empilhada não fez a peça ter 5 telas antes da oferta?

### Roberto, Outlook do trabalho, imagens bloqueadas
Abre no Outlook para Windows. As imagens só carregam se ele clicar.
- Com as imagens desligadas, a oferta e o botão continuam lá (PQ5, V02)?
- O alt das imagens grandes diz algo útil?
- O botão é VML, com a cor certa? GIF mostra só o primeiro quadro: ele
  serve sozinho?

### Júlia, iPhone em modo escuro, à noite
Apple Mail com dark mode do sistema ligado.
- O logo sumiu (R18)? A caixa do cupom virou um bloco sólido?
- Alguma foto de fundo branco virou um retângulo estourado no escuro?
- A peça ficou com "duas temperaturas" (R19)?

### Paulo, leitor de tela
Ouve o e-mail no VoiceOver.
- Os títulos são `h1`/`h2`, na ordem?
- O alt da hero diz o que a imagem diz, com a oferta? A imagem decorativa
  está com `alt=""`?
- O link diz para onde vai ("Ver o casaco"), não "clique aqui"?
- O preço riscado e o preço atual fazem sentido lidos em sequência?

### Dona Lúcia, desconfiada, primeira compra
Nunca comprou da loja; vai olhar se é golpe.
- O nome da loja e o logo estão claros no topo?
- A prova é real e assinada (C02, D10)? Tem endereço e descadastro no
  rodapé?
- O desconto é crível, ou "70% OFF + frete grátis + brinde" parece golpe?
- Algo parece simulação de pedido ou de resposta (C03)?

| Tipo de peça | Personas principais |
|---|---|
| Campanha de oferta | Carla, Roberto, Dona Lúcia |
| Welcome | Dona Lúcia, Carla |
| Carrinho abandonado | Carla, Júlia |
| Texto de pessoa, fundador | Roberto, Paulo |
| Peça com fundo escuro ou muita imagem | Júlia, Roberto, Paulo |

Escreva o que quebrou para a persona, não a descrição da persona. Bom:
"Carla: o botão do hero cai em 712px no mobile, fora da primeira tela."
Ruim: "Usuários de celular podem ter dificuldade."

## Prioridade

O `impeccable` usa P0 a P3. A casa já tem severidade (`SKILL.md`). A
correspondência:

| `impeccable` | Severidade da casa | Exemplo |
|---|---|---|
| P0, impede a tarefa | **Bloqueia** | Texto invisível no dark mode, oferta só na imagem, botão quebrado |
| P1, dificulta muito | **Alta** | Botão fora da primeira dobra no celular, logo sumido, grade desalinhada |
| P2, incomoda | **Média** | Ritmo irregular, centralização de parágrafo, enfeite demais |
| P3, acabamento | **Baixa** | Espaço de 4px a mais, peso de fonte um passo acima |

Na dúvida entre dois níveis, a pergunta do `impeccable`: **alguém da loja
reclamaria disso com a agência?** Se sim, é no mínimo Alta.

**Cinco achados no máximo por rodada**, do mais grave para o menos. Se tudo
é importante, nada é. O resto vai como observação menor.

## O formato do achado

Do Emil: problema de design se reporta como tabela de antes, depois e por
quê. Aqui com o ID e a captura, que o `anti-vicios-visuais.md` exige para o
revisor conseguir conferir.

| ID | Captura | Antes | Depois | Por quê |
|---|---|---|---|---|
| R10 | mobile-375 | Botão do hero em 712px | Hero 4:3 em vez de 1:1; botão em 598px | O celular mostra 667px antes da primeira rolagem |
| D26 | mobile-375 | Condição da oferta em 12px, 14 palavras | 16px, cortada para 8 palavras | Corpo abaixo de 14px; corte a copy, não a fonte |
| R18 | dark-600 | Logo PNG preto transparente | Logo com contorno claro de 2px | No fundo escuro o logo some |
| D29 | desktop-600 | Botão do hero preto, da grade vermelho | Grade com link "COMPRAR" sublinhado | Uma cor de ação por peça |
| PQ2 | desktop-600 | Título "Novidades da estação" | "O casaco que esgotou em maio voltou" | O título genérico serve para qualquer loja |

Achado sem ID e sem captura não entra. Se você não consegue ligar o
problema a um ID, ou ele é gosto (e não é achado), ou é um vício novo: nesse
caso, registre em `docs/pesquisa/a-verificar.md` em vez de inventar regra.

## O que é gosto, e não entra

Da `postura-revisao.md`: a nota não é opinião. Não são achados:

- "Eu usaria outra foto" sem um ID que a foto viole.
- "Ficaria mais moderno com cantos arredondados."
- Coluna única centralizada, caixa alta em botão, número de oferta grande,
  CTA repetido (§8, convenção de e-mail).
- Rodapé denso e cinza (é legal, não é descuido).

## O fechamento da rodada

Depois dos achados, três perguntas que o `impeccable` usa para destravar a
peça. Escolha a que se aplica e responda em uma linha:

- "E se o principal fosse o dobro do tamanho e o resto ficasse igual?"
- "Isto precisa ter tantas partes?"
- "Como seria a versão segura de si desta peça?"

E a regra de parada, também do `impeccable`: **rodadas limitadas, não
laço.** Monta inteiro, inspeciona uma vez, corrige tudo de uma vez,
confirma no máximo mais uma vez. O teto da casa é 3 rodadas no ciclo de
render e 4 no revisor.
