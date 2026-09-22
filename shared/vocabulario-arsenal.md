# Vocabulário do arsenal: da descrição vaga ao slug da variante

Glossário reverso. O humano descreve o bloco pelo que ele parece ("hero com
foto grande e a oferta embaixo"); aqui ele vira o slug exato do vault, que é
o que o Curador, a telemetria e o `_catalogo` entendem.

**Isto não substitui o protocolo.** A escolha final é
`vault/componentes/_protocolo-de-selecao.md`, nove passos, eliminar antes de
rankear. Este arquivo serve dois momentos: traduzir um pedido falado em
candidata nomeada, e conferir depois se o que foi montado é o que foi
pedido. Quando o glossário e o protocolo discordarem, vence o protocolo.

**Fonte:** `vault/componentes/variantes/<secao>/` (75 notas, lidas em
22/09/2026) e `vault/componentes/_catalogo.md` (gerado em 14/09, 44 linhas).

## Como ler as marcas

- **`[cat]`** a variante está no `_catalogo.md` e tem HTML em
  `vault/componentes/_html/`. É candidata hoje.
- **`[19/09]`** veio da catalogação de 19/09: nota escrita, **sem linha no
  catálogo, sem HTML no vault e sem campo `momento`**
  (`vault/componentes/_relatorio-catalogacao-2026-09-19.md` diz "momento
  aposentado"). Pedir por nome funciona; montar depende do banco.
- **`[inativa]`** `ativa: false`. O passo 3 elimina antes de qualquer
  ranking.
- **`[sem schema]`** `schema_campos: 0`. Não é preenchível: mesmo escolhida,
  a fase de copy não tem onde escrever.

Slug é o endereço, mas o identificador estável é o `variant_id`. Há colisão
de número em reviews (duas variantes "reviews-8") e de `nome_no_banco`
("body 21" em duas seções): nunca enderece por número solto.

---

## 1. Hero (18 notas)

| O humano fala | Slug | O que define |
|---|---|---|
| "hero de boas-vindas que entrega o cupom" | `hero-3-cupom-de-captacao` `[cat]` | welcome 1: headline é a oferta, código em texto, CTA repete o valor. Exige cupom ativo |
| "hero de boas-vindas bonito, de marca de moda" | `hero-4-editorial-de-pertencimento` `[cat]` | welcome 1 editorial: acolhe como membro, foto de campanha própria, serif display, cupom |
| "hero que martela o código" | `hero-5-cupom-em-tres-lugares` `[cat]` | código na barra do topo, na pílula da oferta e no rótulo do CTA. Foto lifestyle na base |
| "hero com o desconto gigante" | `hero-6-percentual-gigante` `[cat]` | o percentual é o maior elemento; caixa sólida assentada na borda da foto; monocromático |
| "hero de campanha, sem cupom" | `hero-7-campanha-sem-cupom` `[cat]` | percentual como headline, desconto automático, três barras de cor como assinatura |
| "hero que pergunta e compara" | `hero-2-pergunta-comparativa` `[cat]` | pergunta comparativa com o diferencial em peso e cor; CTA já carrega a oferta |
| "hero no meio do e-mail, mostrando a linha toda" | `hero-10-lineup-de-colecao` `[cat]` | anuncia rotina, kit ou linha e manda para a coleção. Papel `meio`, não abre |
| "igual ao de cima, mas lembrando a oferta" | `hero-8-lineup-com-lembrete-de-oferta` `[cat]` | mesmo dispositivo com lembrete de oferta. Duplicata de decisão do hero-10 |
| "hero de 'precisa de ajuda?'" | `hero-9-atendimento-proativo` `[cat]` | atendimento proativo, dois caminhos em escada (sólido e contorno), sem oferta |
| "hero de compre e leve" | `hero-11-bogo-em-manchete` `[19/09]` | oferta BOGO em manchete; o resgate fica para outra posição. Papel `peca-inteira` |
| "hero com contador regressivo" | `hero-12-contador-com-oferta` `[19/09]` | faixa de contador acima de tudo, oferta em três partes com botão. Exige prazo real |
| "hero de Black Friday inclinado" | `hero-13-black-friday-card-inclinado` `[19/09]` | card inclinado e faixas diagonais, código na mão. Exige cupom e motivo sazonal |
| "hero que é só tipografia" | `hero-14-lockup-tipografico` `[19/09]` | lockup monumental do valor; declara a oferta **sem** entregar código |
| "hero de Cyber com selo redondo" | `hero-15-cyber-com-selo` `[19/09]` | selo circular deslocado nomeia a data, headline de oferta, cupom. Fundo escuro |
| "hero tipo capa de revista, com arco" | `hero-16-arco-editorial` `[19/09]` | arco fotográfico, headline em duas partes, sem oferta e sem urgência |
| "abertura editorial mais curtinha" | `hero-17-abertura-com-lead` `[19/09]` | meia tela: título, lead e corpo curto. A mais leve das três editoriais (556px) |
| "abertura que ocupa a tela inteira" | `hero-18-abertura-alta-centrada` `[19/09]` | foto alta com logo, headline, parágrafo e CTA empilhados no centro |
| "hero retrô, com letreiro" | `hero-19-retro-com-letreiro` `[19/09]` | moldura retrô/arcade, letreiro repetindo a palavra da campanha |

**Desempate de hero.** Ordem real: momento (filtro) → gates de `exige` →
`objecao` → `registro` (`vault/componentes/secoes/_hero.md`). Os atalhos que
resolvem a maioria dos casos:

- Tem cupom para publicar? Sem `cupom-ativo`, caem hero-3, hero-4, hero-5,
  hero-6, hero-13 e hero-15 de uma vez. É o gate que mais elimina.
- É o toque 1 de welcome? Só hero-3, hero-4, hero-5 e hero-6 declaram
  `momento: welcome-1`.
- Abre a peça ou vive no meio? hero-8 e hero-10 são `papel_na_peca: meio`.
  Pedir "hero" quando se quer abertura e receber um deles é erro de papel,
  não de gosto.
- **hero-8 contra hero-10:** empate total declarado
  (`vault/componentes/lacunas/hero-8-duplicata-de-hero-10.md`). Vence a menos
  usada no histórico de envios; sem histórico, o menor número do slug, ou
  seja hero-8.
- Três editoriais de pertencimento (hero-16, hero-17, hero-18) empatam em
  `objecao`, `registro` e `paleta`. O que as separa é peso: 966px, 556px e
  977px. O critério é o orçamento vertical da peça, não o estilo.

---

## 2. Body (18 notas)

| O humano fala | Slug | O que define |
|---|---|---|
| "bloco que compara a gente com os outros, em colunas" | `body-4-comparativo-em-duas-colunas` `[cat]` | duas colunas com foto circular, atributos numerados, linha-resumo |
| "tabela nós contra eles" | `body-16-tabela-nos-x-eles` `[19/09]` | seis atributos, coluna "eles" contra coluna "nós", selo de fechamento |
| "comparação nós contra eles, versão antiga" | `body-5-comparacao-nos-vs-eles` `[cat] [inativa]` | única do catálogo antigo com `confianca-no-canal`, e está inativa |
| "pitch de vale-presente" | `body-3-pitch-de-gift-card` `[cat]` | headline anti-objeção, dois parágrafos, faixa de três selos. Exige gift card digital |
| "colagem de data comemorativa" | `body-2-colagem-de-data-comemorativa` `[cat]` | fitas diagonais, cena de uso, colagem de duas fotos inclinadas |
| "lista educativa numerada" | `body-10-listicle-educativo` `[cat] [inativa]` | três itens com explicação e miniatura; converte só depois de ensinar |
| "FAQ" | `body-7-faq` `[cat] [sem schema]` | existe no HTML, sem julgamento e sem schema: hoje não é candidata |
| "cards de vidro" | `body-8-cards-de-vidro-por-ocasiao` `[19/09]` | os cards são recorte **dentro da foto**, não cards de texto. O HTML está em `_html/body-8-cards-vidro.html`, com o nome antigo |
| "pílulas de features" | `body-9-key-features-pilulas` `[cat] [sem schema]` | idem: renderizável, não preenchível |
| "bloco de skincare 101" | `body-6-skin-minimalism-101` `[cat] [sem schema]` | idem |
| "a tese da marca num quadro só" | `body-12-tese-em-degrade` `[19/09]` | alegação, frase de sustentação e o produto como única prova. Fundo em degradê |
| "antes e depois" | `body-13-antes-e-depois-em-quadro` `[19/09]` | duas fotos comparáveis com rótulo curto. Sem texto corrido, sem CTA. 528px |
| "três razões com foto em faixa" | `body-14-tres-faixas-com-imagem` `[19/09]` | três faixas idênticas de texto mais imagem, título em caixa alta, CTA sólido |
| "apontar as partes na foto do produto" | `body-15-quatro-callouts-na-foto` `[19/09]` | infográfico apontado: foto vertical e quatro callouts nomeando o detalhe |
| "uma linha só entre dois blocos, com foto sangrada" | `body-17-foto-sangrada-com-headline` `[19/09]` | três campos: headline, CTA e foto que sangra. Papel `ponte`, 403px |
| "cinco motivos, só título e texto" | `body-18-cinco-itens-com-titulo` `[19/09]` | a varredura escaneável em forma de bloco. Cinco itens sem imagem |
| "três cards em zigue-zague com ícone" | `body-19-tres-cards-alternados-com-icone` `[19/09]` | cards claros sobre fundo escuro, ícone nomeando o argumento |
| "três selos e a política de troca" | `body-21-tres-selos-e-garantia` `[19/09]` | remoção de risco: três selos, política por extenso, CTA e foto. Bloco de meio |

**Desempate de body.**

- "Comparação" é a palavra mais ambígua do arsenal. São três dispositivos
  diferentes: **duas colunas com foto** (body-4), **tabela de seis linhas**
  (body-16) e **antes e depois em foto** (body-13). Pergunte o que está
  sendo comparado: marca contra marca (body-4, body-16) ou estado antes
  contra depois do produto (body-13).
- `confianca-no-canal` hoje só é declarada por `body-16` e por `body-5`
  (inativa). Se o e-mail é o toque 5 do welcome e o `body-16` não estiver
  disponível no banco, o resultado correto é **lacuna declarada**, não a
  segunda melhor
  (`vault/componentes/lacunas/welcome-5-sem-variante-ativa.md`).
- Faixa de garantias **compacta, de apoio**, continua sem variante:
  `body-21` é bloco de meio, com headline, corpo, CTA e foto. A lacuna
  `vault/componentes/lacunas/body-garantias-3-selos.md` segue aberta. Não
  force o `body-21` no lugar dela.

---

## 3. Products (16 notas)

| O humano fala | Slug | O que define |
|---|---|---|
| "grade 2x2 simples" | `products-14-grade-2x2-com-filete` `[19/09]` | a mais enxuta: título com filete, quatro molduras, botão por célula |
| "grade 2x2 com etiqueta em cima" | `products-12-grade-2x2-com-pilula` `[19/09]` | pílula dourada nomeando o recorte, quatro células, CTA final |
| "grade com o cupom junto" | `products-15-grade-com-cupom` `[19/09]` | quatro produtos mais a linha de cupom antes do CTA. Exige cupom ativo |
| "dois produtos lado a lado, só isso" | `products-16-par-de-cards` `[19/09]` | escolha entre A e B, dois cards empilhados |
| "vitrine com uma frase por produto" | `products-13-vitrine-narrada-alternada` `[19/09]` | zigue-zague: foto de um lado, nome e frase de curadoria do outro |
| "grade grande, nove produtos" | `products-8b-grade-3x3` `[cat]` | nove itens, sem preço e sem descrição. Peça inteira (3071px) |
| "quatro recomendações com indicação de uso" | `products-8a-quatro-recomendacoes` `[cat]` | quatro itens com nome, indicação e botão próprio, mais CTA de coleção |
| "um produto só, com o prazo" | `products-4-produto-unico-com-prazo` `[cat]` | preço antes e depois, selo circular com o prazo. Exige prazo real |
| "um produto só, com três features" | `products-11-produto-unico-com-tres-features` `[19/09]` | parágrafo de abertura, foto vertical grande, três atributos na moldura |
| "produto com depoimento junto" | `products-10-winback-com-relato` `[19/09]` | sintoma nomeado, desejo nomeado e voz de cliente sobre a foto. Winback |
| "três produtos com selo de desconto" | `products-5-tres-com-selo-de-percentual` `[cat]` | três itens com benefícios em lista e selo de percentual colado na foto |
| "vitrine de sale" | `products-6-vitrine-de-sale` `[cat]` | faixa xadrez, dois produtos com frase, sem preço e sem botão por item |
| "o que tem dentro do produto" | `products-2-tres-ingredientes` `[cat]` | foto central e três marcadores: ingrediente, origem, certificação |
| "novidades em arco" | `products-3-arco-de-novidades` `[cat]` | foto de campanha recortada em arco, quatro linhas enumerando o que entrou |
| "dois produtos com vários ângulos" | `products-7-dois-com-galeria-de-angulos` `[cat]` | painel por produto com foto grande e três miniaturas de ângulo |
| "o que ainda tem no meu tamanho" | `products-9-grade-de-tamanho` `[cat]` | quatro produtos com grade de tamanhos; esgotados aparecem apagados |

**Desempate de products.**

- Comece por **quantos slots a loja preenche**: 1 (products-4,
  products-10, products-11), 2 (products-6, products-7, products-16), 3
  (products-2, products-5, products-13), 4 (products-3, products-8a,
  products-9, products-12, products-14, products-15), 9 (products-8b).
  Capacidade é passo 6 e elimina antes de qualquer gosto.
- **Preço.** Nenhuma grade nova (12, 14, 15, 16) tem campo de preço, e as
  antigas escondem preço também. Se o pedido é "vitrine com preço cheio", a
  resposta correta é a lacuna
  `vault/componentes/lacunas/products-grade-preco-cheio.md`, não a grade
  mais parecida.
- `products-12` e `products-14` são o par mais próximo do arsenal: mesma
  grade 2x2, a 14 sem campo de foto. O relatório de 19/09 manda reavaliar
  se o admin adicionar fotos ao schema da 14.
- `products-13` tem schema incoerente (quatro pares de nome contra três
  fotos) e foi resolvida a favor de três itens, pendente de confirmação.

---

## 4. Reviews (10 notas). Prova social é onde mais se erra

| O humano fala | Slug | Tipo de prova que ele exige |
|---|---|---|
| "depoimento de especialista, com o cargo" | `reviews-1-depoimento-com-credencial` `[cat]` | depoimento com credencial + foto do depoente. 2 cards |
| "depoimento longo, com a cara de texto de máquina de escrever" | `reviews-3a-depoimento-longo-monoespacado` `[cat]` | foto de uso real + reviews longos. Preto e branco. 2 cards |
| "o mesmo de cima" | `reviews-3b-depoimento-longo-monoespacado` `[cat]` | duplicata byte a byte da 3a, só `variant_id` e `slug` mudam |
| "prova de que muita gente comprou" | `reviews-5-prova-por-volume` `[cat]` | foto de uso real + reviews curtos. 3 depoimentos |
| "um review por produto que a pessoa comprou" | `reviews-6-review-por-variante` `[cat]` | catálogo de variantes + packshot vertical + 3 reviews distintos |
| "reviews em zigue-zague, com cupom no fim" | `reviews-7-zigue-zague-com-cupom` `[cat]` | selo de compra verificada + reviews curtos. Gate de cupom ativo |
| "foto de cliente de verdade, tipo Instagram" | `reviews-8-ugc-de-comunidade` `[cat]` | UGC autorizado, CTA por depoimento. Peça inteira (2500px) |
| "três cards com a nota geral em cima" | `reviews-8-tres-cards-com-nota` `[19/09]` | nota agregada no subtítulo e três vozes nomeadas. Exige nota real |
| "um review só, discreto" | `reviews-9-card-com-estrelas` `[19/09]` | card de contorno fino com pílula preta de estrelas. 562px, 1 item |
| "um review só, gritado" | `reviews-10-card-unico-verificado` `[19/09]` | card branco de contorno grosso sobre cinza, com selo verificado. 1 item |

### 4.1 Regra de desempate obrigatória: as três de prova social clássica

`reviews-1`, `reviews-3a` (e sua duplicata `3b`) e `reviews-7` **declaram a
mesma objeção**, `qualidade-eficacia`. O eixo empata e não decide nada. A
chave de decisão da seção
(`vault/componentes/secoes/_reviews.md`) resolve pelo **tipo de prova que a
loja tem**, não pela objeção:

| Use | Quando a loja tem | E o e-mail é | Não use se |
|---|---|---|---|
| `reviews-1-depoimento-com-credencial` | depoente com **cargo ou credencial verificável** e **foto da pessoa** (veterinário, dermatologista, técnico) | consideração, welcome-meio ou reengajamento, em categoria com objeção de eficácia ou segurança | o depoente é cliente comum: o slot de função fica vazio e a variante perde a função. Idem sem foto da pessoa, ou com um depoimento só |
| `reviews-3a-depoimento-longo-monoespacado` | **foto do produto em uso real** (não packshot) e **reviews longos** | carrinho ou checkout abandonado: é o momento declarado dela | a loja só tem review de uma linha, ou a peça já tem outro bloco de prova (`prova-social-nao-duplica-na-peca`), ou a peça usa serif display (`monoespacado-nao-convive-com-serif-display`) |
| `reviews-7-zigue-zague-com-cupom` | **selo de compra verificada** real e **reviews curtos** | consideração **com cupom ativo**: sem cupom, o passo 4 elimina antes do ranking | não há cupom para publicar, ou o selo é decorativo |

Em uma frase: **credencial** (quem disse), **foto de uso real** (mostra
funcionando) e **selo verificado mais cupom** (prova de compra e empurrão
para conversão). A escolha é do ativo disponível.

Os outros perfis da seção não competem com esses três, porque atacam outra
objeção: `reviews-5` é `adesao-social` (volume), `reviews-6` é
`escolha-variedade` (prova e vitrine ao mesmo tempo) e
`reviews-8-ugc-de-comunidade` é `pertencimento`.

**Empate total 3a contra 3b:** são a mesma peça cadastrada duas vezes
(`vault/componentes/lacunas/reviews-3-duplicado.md`). Vence a menos usada no
histórico; sem histórico, `reviews-3a`.

### 4.2 TODO: a chave da seção não cobre as três variantes novas

`vault/componentes/secoes/_reviews.md` foi escrita quando a seção tinha 7
variantes. Hoje tem 10, e as três novas mudam dois desempates:

- **`qualidade-eficacia` agora tem cinco candidatas**, não três:
  entram `reviews-9-card-com-estrelas` e `reviews-10-card-unico-verificado`,
  as duas de **um item só** e com gate `review-com-nome` (requisito que
  ainda não tem nota em `vault/componentes/requisitos/`). Critério
  provisório, derivado só do frontmatter, **a confirmar no vault**: com um
  único review disponível, a escolha é entre `reviews-9` (registro
  `minimalista-leve`, 562px, prova que não interrompe) e `reviews-10`
  (registro `bold-alto-contraste`, 658px, prova dita alto). Com dois ou mais
  reviews, volta a tabela de 4.1. **TODO: o vault precisa declarar isto na
  chave de decisão da seção.**
- **`adesao-social` agora tem duas:** `reviews-5-prova-por-volume` (3
  depoimentos com foto de uso real, 1992px) e
  `reviews-8-tres-cards-com-nota` (3 cards mais nota agregada, 1359px,
  exige nota real). **TODO: sem critério declarado no vault.** O que o
  frontmatter permite dizer: `reviews-8` pede nota agregada real e é mais
  leve; `reviews-5` pede foto de uso real. Não inventar critério além disso.
- **Colisão de número:** `reviews-8-tres-cards-com-nota` e
  `reviews-8-ugc-de-comunidade` são variantes distintas com o mesmo número.
  Sempre pelo slug inteiro.

---

## 5. Offer (9 notas)

| O humano fala | Slug | O que define |
|---|---|---|
| "só a condição da oferta, sem imagem" | `offer-1-condicao-sem-imagem` `[cat]` | 400px, o mais leve do arsenal. Fecha peça ou faz ponte. Exige contexto acima |
| "lembrete do cupom" | `offer-3-lembrete-de-cupom` `[cat]` | código, percentual e condição em quatro linhas, produto embaixo. Peça inteira |
| "lembrete do cupom com o produto de volta" | `offer-20-codigo-relembrado-com-mecanica` `[19/09]` | mecânica em cima (código em pílula e condição), painel com quatro detalhes e foto |
| "duas ofertas ao mesmo tempo" | `offer-2-duas-ofertas-sazonais` `[cat]` | percentual e combo em caixas separadas sobre foto de cena. Exige prazo real |
| "manifesto antes de dar o código" | `offer-4-manifesto-antes-do-cupom` `[cat] [inativa]` | três parágrafos de missão e só então o código. Sem imagem |
| "três diferenciais e o cupom no fim" | `offer-5-tres-diferenciais-e-cupom` `[cat] [inativa]` | argumento de qualidade antes do preço |
| "recuperação de carrinho em preto e branco" | `offer-6-carrinho-preto-e-branco` `[cat]` | duas metades de fundo oposto separadas por faixa de papel rasgado |
| "o código num respiro, fundo desfocado" | `offer-11-codigo-sobre-fundo-difuso` `[19/09]` | pilha de texto branco centralizada sobre fundo difuso. Registro minimalista |
| "brinde se comprar acima de X, com selos" | `offer-21-brinde-condicionado-com-selos` `[19/09]` | condição com o código embutido na frase, foto do brinde e três selos |

**Desempate de offer.** Quase toda offer tem gate de `cupom-ativo` (3, 4, 5,
6, 11, 20, 21). Sem cupom sobram `offer-1` e `offer-2`, e a `offer-2` ainda
exige duas ofertas simultâneas, motivo sazonal e prazo real. Depois disso, o
que separa é papel na peça: `fecha` (offer-1, 2, 5, 11, 21), `peca-inteira`
(offer-3, 4, 6), `meio` (offer-20) e `ponte` (offer-1).

**TODO:** as duas offer com julgamento completo para welcome (`offer-4` e
`offer-5`) estão inativas. Para o welcome, o arsenal de offer hoje é
`offer-1` e as de carrinho. Nenhuma lacuna do vault registra isso; vale
abrir.

---

## 6. Footer (4 notas)

| O humano fala | Slug | O que define |
|---|---|---|
| "rodapé padrão, menu em botões vazados" | `footer-1-menu-outline` `[cat]` | grid 2x3 de botões outline, 4 sociais com label. Registro minimalista-leve |
| "rodapé de alto contraste" | `footer-2-menu-solido` `[cat]` | 5 botões sólidos, 3 sociais sem label, unsubscribe em evidência |
| "rodapé escuro e editorial" | `footer-3-dark-editorial` `[cat]` | logo tipográfico grande, 3 links entre hairlines, bloco legal completo |
| "rodapé escuro com menu grande" | `footer-4-dark-mega-menu` `[cat] [sem schema]` | 7 links em pills. Ativa e julgada, mas sem schema: fora do passo 3 |

**Desempate de footer.** Os quatro declaram `objecao: []` de propósito, e o
ranking degrada direto para `registro` e depois `paleta`. Na prática decide
o número de destinos de navegação que a loja tem: 4 a 6 (footer-1), 5
(footer-2), 3 (footer-3), 6 a 7 (footer-4, hoje não elegível).

---

## 7. Header e CTA: zero variantes

Não há nada a traduzir. `vault/componentes/secoes/_header.md` e
`_cta.md` declaram zero variantes, e as pastas não existem.

Isso não é detalhe: **as 8 estruturas de referência do welcome pedem
`header`, e duas pedem `cta`**. Quando o blueprint chega nessas posições, o
pipeline cai no template global sem registro. O comportamento correto é
declarar a lacuna e parar o batch, nunca escolher "o mais parecido".

- "barra de logo", "logo sobreposto ao hero", "tagline no topo", "barra de
  aviso": sem variante. Ver `vault/componentes/lacunas/header-sem-variante.md`.
- "botão isolado", "faixa de CTA": sem variante. Ver
  `vault/componentes/lacunas/cta-sem-variante.md`.

---

## 8. Palavras que o humano usa e não viram slug

Vocabulário de pedido que **não** existe como variante. Registrado para o
agente não improvisar.

| Pedido | Situação |
|---|---|
| "carrossel de produto" | não existe no arsenal. Grade ou vitrine narrada são o vizinho |
| "barra de aviso no topo" | é `header`, e header tem zero variantes |
| "botão sozinho no meio do e-mail" | é `cta`, zero variantes |
| "banner de estatísticas (10k+, 4.9, 98%)" | não há variante; e números só com lastro no brief (C02, V19) |
| "faixa compacta de três selos" | lacuna aberta, `body-garantias-3-selos`. `body-21` é bloco de meio, não faixa |
| "grade com preço cheio" | lacuna aberta, `products-grade-preco-cheio` |
| "e-mail inteiro" | não é bloco. Ver `vault/componentes/convivencia/peca-inteira-nao-e-bloco.md`: variantes com `papel_na_peca: peca-inteira` não compõem com outras |

---

## 9. Regras de convivência que derrubam combinações

Seis notas em `vault/componentes/convivencia/`, aplicadas no passo 8. As
que mais aparecem num pedido falado:

- **Prova social não duplica na peça:** um bloco de reviews por e-mail.
  Pedir "reviews no meio e depoimento no fim" é pedir o que o vault veta.
- **Grade de produtos não convive com review-vitrine:** `reviews-6` já é
  vitrine; com uma grade na mesma peça, o e-mail repete a mesma função.
- **Raio alto não convive com canto vivo:** `hero-5`, `reviews-1` e
  `reviews-5` têm cantos arredondados; não misturar com blocos de canto
  reto na mesma peça.
- **Monoespaçado não convive com serif display:** pega `reviews-3a` e
  `reviews-3b`.
- **Exige hero ou contexto acima:** `offer-1`, `products-5`,
  `products-8b`, `reviews-3a` e `3b` não abrem peça.
- **Peça inteira não é bloco:** vale para `reviews-8-ugc-de-comunidade` e
  `hero-11`.

---

## 10. Manutenção

Este glossário é derivado: quando o vault muda, ele fica errado em silêncio.
Reconferir quando `vault/componentes/_catalogo.md` for regerado, e depois de
qualquer catalogação nova. O sinal de que está velho é simples: a contagem
de notas por seção aqui (hero 18, body 18, products 16, reviews 10, offer 9,
footer 4) deixar de bater com `ls vault/componentes/variantes/<secao>/`.
