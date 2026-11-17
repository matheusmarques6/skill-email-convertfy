# Operações de design: o que fazer quando o pedido é "melhora isso"

Detalhe da `email-design`. Fecha a lacuna 7 de
`docs/lacunas-priorizadas.md` (`polish`, `distill`, `clarify`, `typeset`,
`layout` sem equivalente) e parte da 11 (`redesign` com prioridade).

Quando o pedido não é "monte a peça", e sim "deixa mais limpo", "o botão
não aparece", "tá pesado", "tá sem graça", ele cai numa destas operações.
Cada uma tem escopo, passos e o que **não** muda. Todas terminam no ciclo
de render.

Fontes: os comandos do `impeccable` (Apache 2.0) reescritos para e-mail,
com escopo próprio; o protocolo de redesenho do `taste-skill`. Nenhum nome
de comando foi mantido como gatilho. Créditos e alterações em `NOTICE.md`.

## Como escolher

| O pedido soa como | Operação |
|---|---|
| "Dá um tapa", "finaliza", "tá quase" | **Polir** |
| "Tá poluído", "tem coisa demais", "tá longo" | **Enxugar** |
| "O texto da peça tá confuso", "o botão não diz nada" | **Esclarecer** |
| "As letras tão estranhas", "título não se destaca" | **Tipografar** |
| "Tá tudo colado", "tá desalinhado", "tá bagunçado" | **Diagramar** |
| "No celular fica ruim" | **Adaptar** |
| "Tá gritando", "tá chamativo demais" | **Acalmar** |
| "Tá sem graça", "tá apagado" | **Reforçar** |
| "Refaz o template da loja" | **Redesenhar** |

Se dois servem, pergunte uma vez qual. Se a peça tem problema de estrutura
(R12, R13, PQ2), nenhuma operação de acabamento resolve: diga e volte ao
vault.

## Regra comum a todas

- **Refinar preserva; redesenhar substitui** (`impeccable`). Polir não é
  redesenho escondido. Se o conceito está errado, diga isso, em vez de
  contrabandear outro layout dentro do "tapa".
- Copy factual (oferta, preço, prazo, nome de produto) não muda sem
  pedido. Mudar a frase da oferta para "caber melhor" muda o que a loja
  promete.
- Variante do vault não se edita por dentro. A operação mexe no que está em
  volta: espaçador, bloco do arsenal, slot.
- Termina com `render.py`, `lint_email.py`, `lint_copy.py` e a tabela de
  antes, depois e por quê (`critica-visual.md`).

---

## Polir

**Escopo:** a peça está certa e quase pronta. Acabamento, não mudança.

**Ordem** (do `polish` do `impeccable`, adaptada):
1. O que quebra: link sem destino, imagem quebrada, slot vazio,
   `[FALTA: ...]`, botão sem VML.
2. Estados que faltam: bloco dinâmico sem estado para vazio (D24), merge
   tag sem fallback (C47).
3. Hierarquia e consistência: mesmo papel com o mesmo tamanho, mesma cor de
   ação, espaço da escala.
4. Detalhe visual: alinhamento óptico do botão, preço "de" e "por" na
   mesma linha de base, aspas tipográficas.
5. Limpeza do código: comentário de rascunho, estilo duplicado, `<br>`
   sobrando.

**Não muda:** estrutura, ordem de blocos, copy, imagens.

---

## Enxugar

**Escopo:** a peça tem coisa demais. Do `distill`: tirar o que não ganha o
lugar.

**Passos:**
1. Diga a única coisa que a peça precisa conseguir (o "papel do envio",
   PQ3). Uma.
2. Liste cada bloco e pergunte: se sair, a pessoa deixa de entender a
   oferta ou de confiar? Se não, sai.
3. Bloco que repete o que outro já disse sai (prova social duplicada é
   regra do vault: `prova-social-nao-duplica-na-peca`).
4. Dentro de cada bloco: uma ideia. Três diferenciais que provam a mesma
   coisa ficam; três que provam coisas diferentes viram um.
5. Visual: tire cor sem papel, divisória entre blocos de natureza
   diferente, rótulo decorativo, ícone solto (R22).

**Alvo:** a altura volta para 2.000 a 3.200px no celular (R01, R02). Uma ou
duas rolagens de texto, como manda o Max para copy.

**Não muda:** a oferta, o botão do hero, o rodapé legal.

---

## Esclarecer

**Escopo:** a interface de texto da peça: botões, rótulos, alt, legendas.
A copy longa é da `email-copy`.

**Passos:**
1. O botão diz a ação e o objeto: "Ver o casaco", "Usar meu cupom". Não
   "Saiba mais", não "Clique aqui".
2. Um texto por intenção. "Comprar agora" no hero e "Garantir o meu" no fim
   para a mesma página são dois textos para uma ação: escolha um.
3. O alt diz o que a imagem mostra e, se ela carrega oferta, a oferta.
4. Rótulo acima do título só se diz prazo ou condição.
5. Link no texto diz para onde vai.

**Não muda:** o texto de corpo e a oferta (vão para a `email-copy`).

---

## Tipografar

**Escopo:** a hierarquia tipográfica. Detalhe em `tipografia.md`.

**Passos:**
1. Liste os papéis que a peça usa (título, corpo, preço, rótulo, botão).
2. Para cada papel, um tamanho, um peso, uma entrelinha. Mesmo papel, mesmo
   valor em toda a peça.
3. Confira as razões: título do hero com o dobro do corpo (D12); nenhum par
   de papéis a menos de 2px de distância.
4. Pilha de fonte da ficha, terminando em família genérica.
5. Texto em imagem pela tabela de tamanho mínimo.

**Não muda:** a família da marca (se a ficha diz Montserrat, é Montserrat).

---

## Diagramar

**Escopo:** espaço, alinhamento, agrupamento. Detalhe em
`espaco-e-ritmo.md`.

**Passos:**
1. O teste de apertar os olhos: principal, secundário e grupos aparecem?
2. Todo espaço na escala. Valor fora da escala é sintoma, não ajuste.
3. Perto o que é junto, longe o que é separado, com razão de 2x.
4. Mais espaço acima do título do que abaixo.
5. Grade: mesma proporção de foto, mesma altura de card, preços na mesma
   linha (D25, R20).
6. Vizinhança: no máximo dois blocos de mesmo layout seguidos.

---

## Adaptar (celular)

**Escopo:** a peça funciona no desktop e não no celular. O `adapt` do
`impeccable` pensa em vários aparelhos; e-mail tem um que manda: o
celular de 375px.

**Passos:**
1. Botão do hero antes de 667px (R10).
2. Nenhuma rolagem horizontal (R09). Elemento com largura fixa em `style`
   precisa da `casca-600` ou de `max-width:100%`.
3. Colunas viram linha (técnica híbrida, `modulos-ecommerce.md`), e a soma
   das alturas empilhadas cabe no teto.
4. Texto de 16px vivo; texto em imagem pela tabela de `tipografia.md`.
5. Classe `pad` nos blocos de texto com lateral grande.
6. Botão de pelo menos 44px de altura, área de toque de 300px de largura.
7. Imagem 2x declarada na largura de exibição (não na natural).

---

## Acalmar

**Escopo:** a peça grita. Do `quieter`.

**Passos:**
1. Cor: uma faixa de cor no máximo, acento só no botão e num detalhe.
2. Peso: só o título e o preço em negrito; corpo regular.
3. Tamanho: diminua o que não é principal, não o principal.
4. Enfeite: tire selo, ícone, divisória e rótulo que não carregam
   informação.
5. Movimento: GIF fora, a menos que tenha propósito (`movimento-e-gif.md`).

**Não muda:** o número de oferta grande e o botão. Calmo não é escondido.

---

## Reforçar

**Escopo:** a peça está certa e apagada. Do `bolder`, com a mesma trava: o
reforço usa o que a marca já tem, mais alto, não algo novo.

**Passos:**
1. Um movimento decisivo, completo: o título do hero maior, ou o número da
   oferta maior, ou a foto do produto maior. Um.
2. Silencie o resto em volta, para o movimento aparecer.
3. Cor de ação da ficha no botão, se ainda está no preto do neutro e a
   ficha tem cor.
4. Um ponto alto na rolagem (respiro maior em volta da seção principal).

**Não muda:** a paleta (nenhuma cor nova), a família tipográfica, a copy.
O "teste do esqueleto" do `bolder`: tirando a cor e a foto, a hierarquia
continua forte? Se não, o problema é de escala, não de cor.

---

## Redesenhar o template da loja

**Escopo:** refazer cabeçalho, rodapé e padrões visuais que a loja usa em
toda peça. É a operação de maior risco. O protocolo é o de "Quando o pedido
é refazer um template", em `direcao-visual.md`.

**Resumo:**
1. Auditoria antes de tocar: o que existe, o que vende, o que é vício.
2. Alavancas em ordem: tipografia, espaço, botão, cor, hero, bloco. Pare
   quando resolver.
3. Nunca muda sem aprovação: logo, rodapé legal, endereço, merge tags,
   UTM, estrutura validada.
4. Entregue o antes e o depois lado a lado, com os três PNGs de cada.
5. O que muda vira campo na ficha da marca (`marcas/<cliente>.md`), senão a
   próxima peça volta ao antigo.
