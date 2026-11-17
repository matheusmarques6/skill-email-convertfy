# Checklist de design: o pré-voo antes do revisor

Detalhe da `email-design`. O `Gate de entrega` do `SKILL.md` é técnico
(tabela, VML, alt, peso). Este é o de **design**: o que um diretor de arte
conferiria antes de mandar a peça. Roda depois do ciclo de render e antes
do `email-revisor`.

Inspirado no pré-voo do `taste-skill` ("se uma caixa não pode ser marcada
com honestidade, a peça não está pronta"), filtrado para e-mail e ligado
aos IDs da casa. O que o lint já mede está marcado com **[lint]**: não
precisa olhar, precisa estar verde.

## Leitura e regime

- [ ] A linha de leitura de design foi escrita (`direcao-visual.md`)?
- [ ] O regime (neutro ou marca) é o que a ficha manda?
- [ ] Densidade, peso de imagem e intensidade de marca batem com o preset
      do tipo de e-mail, ou o desvio está justificado?
- [ ] O teste de especificidade passa: trocando o logo, a peça **não**
      serve para outra loja?

## Primeira dobra

- [ ] Oferta, cupom, prazo e botão nos primeiros 500px do desktop (R21)?
- [ ] Botão do hero antes de 667px no `mobile-375.png` (R10) **[render]**?
- [ ] O título do hero tem até 40 caracteres e até 3 linhas no celular
      (D13)?
- [ ] O hero tem no máximo quatro elementos de texto: rótulo (opcional),
      título, proposta, botão?
- [ ] Um botão só no hero (D30)?

## Hierarquia e tipografia

- [ ] Apertando os olhos, o principal, o secundário e os grupos aparecem
      (R14)?
- [ ] Título do hero com pelo menos o dobro do corpo (D12)?
- [ ] No máximo 5 tamanhos e 3 pesos na peça?
- [ ] Mesmo papel com o mesmo tamanho na peça inteira?
- [ ] Corpo de 16px (piso 14), rodapé de 12px (piso 11) (D26) **[lint]**?
- [ ] No máximo duas famílias (D28) **[lint]**?
- [ ] Texto corrido de 3+ linhas alinhado à esquerda (R16)?
- [ ] Texto dentro de imagem no tamanho mínimo da tabela de
      `tipografia.md`?
- [ ] Nenhum botão com o texto quebrado em duas linhas?

## Espaço e ritmo

- [ ] Todo padding e espaçador na escala 4, 8, 12, 16, 24, 32, 40, 48, 64?
- [ ] Perto o que é junto, longe o que é separado (razão de 2x)?
- [ ] Mais espaço acima de cada título do que abaixo?
- [ ] Nenhum ponto antes do rodapé parece o fim do e-mail?
- [ ] Nenhuma tela de branco sobrando (R11)?
- [ ] No máximo dois blocos de mesmo layout em sequência; ziguezague uma
      vez só?
- [ ] Altura entre 2.000 e 3.200px, contando o celular com a grade
      empilhada (R01, R02)?

## Rótulos e enfeite

- [ ] Rótulo acima de título no máximo uma vez a cada três seções, e só
      com prazo ou condição (D07)?
- [ ] No máximo dois elementos decorativos sem função na peça (R22)?
- [ ] Divisória só entre itens da mesma natureza?
- [ ] Nenhum ícone em emoji, nenhum SVG decorativo (D31) **[lint: SVG]**?
- [ ] Nenhuma sombra em texto (D27) **[lint]**?

## Imagem

- [ ] Foto real da loja, ou imagem gerada com aprovação no brief e o
      checklist D15 aplicado?
- [ ] Toda imagem grande linkada (D21) **[lint]**?
- [ ] Fotos da grade na mesma proporção (D25, R20)?
- [ ] Nada de compra (preço, código, prazo) só dentro da imagem (V02)
      **[lint]**?
- [ ] Alt decidido em cada imagem (D17, D23) **[lint, em parte]**?
- [ ] Peso total de imagem abaixo de 800 KB; GIF até 1 MB?
- [ ] O brief de imagem foi entregue para cada slot sem foto?

## Produto e oferta

- [ ] Grade com exatamente o número de produtos que há (sem célula vazia)?
- [ ] CTA por produto (link "COMPRAR" ou botão) e um fecho geral depois da
      vitrine?
- [ ] Preço "de" só com preço anterior real (C02)?
- [ ] Moeda e formato do mercado da ficha?
- [ ] Prova social com dado real, assinada, sem avatar inventado (C02,
      D10)? Sem dado, o bloco não aparece (D24)?
- [ ] Contagem regressiva só com prazo real, também em texto vivo (C06)?

## Clique

- [ ] Botão de 48 a 56px de altura e cerca de 300px de largura (R17)?
- [ ] Uma cor de botão na peça (D29) **[lint]**?
- [ ] Um texto por intenção de clique?
- [ ] O botão do hero repete no fim da peça, com o mesmo texto e destino?
- [ ] Rodapé com 3 a 5 categorias reais?

## Cor e dark mode

- [ ] Cada cor com papel; nenhuma cor fora da ficha **[lint com --marca]**?
- [ ] Contraste 4,5:1 no claro (D04, D05) **[lint]** e conferido no
      `dark-600.png`?
- [ ] Texto sobre cor em branco ou preto?
- [ ] Nada sumiu ou virou bloco no `dark-600.png` (R18)? Peça sem duas
      temperaturas (R19)?

## Personas

- [ ] Duas ou três personas de `critica-visual.md` percorridas, com o que
      quebrou para cada uma anotado (ou "nada quebrou")?

## Entrega

- [ ] Três PNGs olhados, não só gerados.
- [ ] Achados restantes listados com ID, captura e a tabela antes, depois e
      por quê.
- [ ] Lint de copy e de e-mail sem B.
- [ ] Pronto para o `email-revisor` em contexto limpo.
