# Anti-vícios de copy (C01 a C47)

Contrato de copy de e-mail da Convertfy. Vale para toda skill deste repo.
Fonte: `docs/pesquisa/pesquisa-vicios-ia-email.md` (catálogo) e
`docs/pesquisa/evidencias-publicadas.md` (veredito por regra).
Aplicação determinística: `scripts/lint_copy.py` mais `shared/lexico/`.

O arquivo tem duas metades, no modelo Verify / Refuse:

- **Verify** é o que a máquina checa antes da entrega. Passar é obrigatório,
  não é mérito.
- **Refuse** é o que o redator recusa por padrão, mesmo quando o lint não pega.
  Recusar aqui significa reescrever o elemento, não amaciar.

## Como ler

| Campo | Valores |
|---|---|
| Severidade | **B** bloqueia entrega · **A** alta, corrigir antes de enviar · **M** média, aceitável se isolado |
| Detecção | **R** regex no lint · **H** heurística no lint · **J** julgamento do revisor |
| Veredito | **confirmada** (evidência publicada sustenta) · **refinada** (sustenta com ajuste, o ajuste está escrito) · **interna** (a evidência é a rejeição real da Convertfy ou o corpus observado, sem literatura pública) |

Fontes F1 a F10 são as da seção 0 da pesquisa. Resumo: F1 histórico de
rejeições da Convertfy, F2 corpus Figma de 35 welcomes, F4 Trendtrack,
F5 humanizer, F6 Deslop-ptBR e humanizer-pt-br, F7 slop-score, F8 slop-detect,
F9 email-marketing-bible, F10 impeccable e taste-skill.

**Mito que esta skill não repete:** não existe evidência primária de que Gmail,
Yahoo ou Outlook detectem e penalizem "texto com cara de IA". Quem afirma isso
está especulando. O risco real da copy homogênea é outro e é observável:
engajamento baixo, reclamação de spam e homogeneização entre lojas (20 de 20
lojas Shopify não relacionadas mandando o mesmo texto de boas-vindas, medido na
Trendtrack em 22/09/2026). Justifique as regras por aí.

---

# Verify

Ordem de execução do `lint_copy.py`. Limiar é **contagem absoluta por e-mail**,
nunca por mil palavras: e-mail tem 40 a 150 palavras (seção 4.2 da pesquisa) e
densidade por mil palavras não mede nada nesse tamanho.

| Porta | Regra | Limiar | Falhou, então |
|---|---|---|---|
| 1 | C01 travessão | 0 ocorrências | bloqueia |
| 2 | C02 número órfão | todo número sai de `brief_numbers`, ou é percentual ou preço da oferta | bloqueia |
| 3 | C03 assunto que simula transação | 0 | bloqueia |
| 4 | C04 idioma errado em cupom e CTA | 0 | bloqueia |
| 5 | C05 cena fabricada | 0 | bloqueia |
| 6 | C07 comentário sobre a própria copy | 0 | bloqueia |
| 7 | C10, C11 antítese e tríade | 1 ocorrência já acusa | alta |
| 8 | C12, C16, C17, C20 a C26 | léxico por idioma; modo densidade exige 3 | alta ou média |
| 9 | C18 ritmo metronômico | 4 frases ou mais, média 8 palavras ou mais, desvio abaixo de 3 | média |
| 10 | C30 a C35 forma e pontuação | contagens da seção 5.4 | média |
| 11 | C40 a C47 específicos de e-mail | ver cada regra | alta ou média |

Saída: `{regra, severidade, campo, trecho, sugestao}`. Qualquer B derruba a
entrega e o processo sai com código 1.

O que o lint **não** cobre e fica com o revisor humano ou com o crítico
(ver `shared/postura-revisao.md`): C06 urgência falsa, C19 espantalho, e a
parte de julgamento de C02 (o número existe, mas mede o que a frase diz?).

---

# Refuse

## 5.1 Regras duras da Convertfy


## Regras confirmadas pelos dados da própria carteira

Nível 2 da hierarquia do `CLAUDE.md`. Estas regras deixaram de depender
só da pesquisa publicada: a carteira da Convertfy mede o mesmo.

| Regra | Dado interno | Fonte |
|---|---|---|
| C01 travessão | "Sem travessão" é regra dura da casa | `05_Modelos_validados/regras-de-copy-de-campanha.md` |
| C02 número inventado | "Número de prova só se for real da loja" | idem |
| C04 idioma do cupom | "Idioma certo" no checklist de agendamento | idem |
| C06 urgência falsa | "Avaliação, estoque, contador e número só se forem reais da loja. Sem o dado, o bloco sai" | `08_Skill/SKILL...md`, princípio 3 |
| C20 superlativo vazio | Esquenta em tom de anúncio, sem número nem prazo: **1 pedido** | `08_Skill/SKILL...md`, seção 3 |
| C41 preheader | "O pré-cabeçalho completa o assunto com a oferta ou o prazo" | `08_Skill/SKILL...md`, seção 11 |
| C42 oferta em texto vivo | "Oferta na primeira tela", "Oferta em 3 segundos" | `regras-de-copy-de-campanha.md` |
| C43 e C44 CTA | "Um botão principal" por e-mail | `08_Skill/SKILL...md`, seção 10 |
| C46 condição da oferta | "Prazo com data e hora", "Cupom testado e com limite real" | `regras-de-copy-de-campanha.md` |
| C34 Title Case | Assuntos validados da Blue Wolf são em inglês com Title Case | `04_Assuntos/` |

Nove regras do catálogo estão em disputa com os dados e **não foram
alteradas**: C03, C05, C22, C30, C31, C45 e P09, mais D01 a D05 e D13.
A redação proposta para cada uma está em
`docs/reconciliacao-regras-dados.md`, aguardando aprovação.


### C01 Travessão em qualquer campo
**B · R · F1 · refinada**
A evidência publicada sustenta "proibir como padrão", não proibição absoluta: o
travessão é marcador relatado de LLM, com força moderada. A Convertfy eleva para
tolerância zero por decisão de casa (CLAUDE.md), porque é o vício mais barato de
detectar e porque já escapou de prompt com proibição escrita, o que prova que
regra em prosa não basta.
- Ruim pt: `Sua oferta chegou — aproveite`
- Bom pt: `Sua oferta chegou: aproveite`
- Ruim en: `A ritual for the bold—reset and recharge`
- Bom en: `A ritual for the bold: reset and recharge`

### C02 Número, estatística ou avaliação inventados
**B · H mais J · F1 · confirmada**
Veracidade e risco legal. Número que não veio do brief não entra, nem "arredondado
para soar bem". Percentual e preço da própria oferta são exceção declarada.
- Ruim pt: `Já somos 32.541 clientes ativos`
- Bom pt: `17% OFF no primeiro pedido`
- Ruim en: `Loved by 18,923 customers`
- Bom en: `4.9 from 108 reviews` (quando as 108 avaliações existem)

### C03 Assunto que simula transação, resposta ou aviso
**B · R · F4 · confirmada**
Abre no curto prazo e cobra caro em reclamação. É publicidade enganosa.
- Ruim pt: `(RE): confirmação do seu pedido`
- Bom pt: `R$30 OFF acima de R$100 até domingo`
- Ruim en: `Your order has been approved`
- Bom en: `20% off sitewide is live`

### C04 Trecho no idioma errado
**B · H · F1 · interna**
Cupom, CTA e microcópia seguem o idioma da loja, sempre.
- Ruim: cupom `PEDIDO18` em loja EN
- Bom: `ORDER18`
- Ruim: CTA `Shop now` em loja BR
- Bom: `Comprar agora`

### C05 Cena ou storytelling fabricado
**B · R mais J · F1 · interna**
Hora, data, personagem, "estou escrevendo este e-mail". O e-commerce não precisa
de cena, precisa de condição.
- Ruim pt: `São 11 de novembro. 7:15 da manhã.`
- Bom pt: `Frete grátis acima de R$199 até domingo.`
- Ruim en: `It's 7:15 am and I'm writing this to you.`
- Bom en: `Free shipping over $99 through Sunday.`

### C06 Urgência ou escassez falsa
**B · J · F1 e F4 · confirmada**
Prazo, estoque e exclusividade só existem se estiverem no brief. Urgência real
converte; urgência inventada corrói confiança e sobe reclamação.
- Ruim pt: `Últimas unidades!` sem dado de estoque
- Bom pt: `O cupom vale até domingo, 23h59`
- Ruim en: `Almost gone!`
- Bom en: `Code expires Sunday at 11:59 pm`

### C07 Comentário sobre a própria copy
**B · R · F1 · interna**
Resíduo de chat. A entrega é o artefato, nada além.
- Ruim pt: `A copy é centrada em benefícios...`
- Bom pt: (só os campos da peça)
- Ruim en: `Here's the copy. Why this works: ...`
- Bom en: (só os campos da peça)

## 5.2 Estrutura e retórica

### C10 Antítese "não é X, é Y"
**A · R · F5, F6, F8 · confirmada**
- Ruim pt: `Não é só uma joia, é a sua história.`
- Bom pt: `Prata 925 com banho de ródio. Não escurece.`
- Ruim en: `They don't just train you, they transform you.`
- Bom en: `Two sessions a week. Twelve weeks.`

### C11 Tríade ornamental
**A · R · F5, F6 · confirmada**
Três itens em ritmo. Lista de quatro categorias de produto não é tríade: o lint
só acusa quando são exatamente três itens somando até 8 palavras.
- Ruim pt: `Conforto, estilo e elegância.`
- Bom pt: `Malha 100% algodão, 180 g/m².`
- Ruim en: `Perform better, recover faster, and transform deeper.`
- Bom en: `Ten minutes to set up.`

### C12 Fecho de falsa profundidade
**A · R mais H · F5, F6 · confirmada**
- Ruim pt: `Porque você merece.`
- Bom pt: `Comprar com 17% OFF (válido até domingo)`
- Ruim en: `The possibilities are limitless.`
- Bom en: `Shop the sale (ends Sunday)`

### C13 Revelação teatral
**M · R · F6 · interna**
- Ruim pt: `E o melhor: ...`
- Bom pt: `Frete grátis acima de R$199.`
- Ruim en: `But wait, there's more.`
- Bom en: `Free shipping over $99.`

### C14 "Seja você X ou Y"
**M · R · F6, F8 · confirmada**
- Ruim pt: `Seja para o trabalho ou para o fim de semana`
- Bom pt: `Para usar no trabalho`
- Ruim en: `Whether you're commuting or traveling`
- Bom en: `Built for the commute`

### C15 Pergunta retórica de abertura
**M · R · F6 · interna**
- Ruim pt: `Já pensou em ter um sono perfeito?`
- Bom pt: `Se você acorda cansado mesmo dormindo 8h...`
- Ruim en: `Ever dreamed of perfect sleep?`
- Bom en: `If your mattress feels almost right (but you still wake up tired), let's fix that.`

### C16 Abertura genérica (pigarro)
**A · R (léxico) · F5, F6 · confirmada**
- Ruim pt: `No mundo de hoje, cuidar de si é essencial.`
- Bom pt: `17% OFF no primeiro pedido.`
- Ruim en: `In today's fast-paced world...`
- Bom en: `10% off your first order.`

### C17 Recapitulação no final
**M · R (léxico) · F6 · confirmada**
- Ruim pt: `Resumindo: aproveite.`
- Bom pt: (cortar)
- Ruim en: `In conclusion, don't miss out.`
- Bom en: (cortar)

### C18 Frases de tamanho uniforme
**M · H · F6, F9 · confirmada**
Baixa variação de tamanho é marcador medido de LLM. Só vale para o corpo: o
assunto, o preheader, o CTA e o alt são rótulos curtos por natureza, e o lint só
acusa quando a média passa de 8 palavras (senão acusaria todo e-mail de rótulos,
que é o padrão humano do corpus F2).
- Ruim: 4 frases de 11 a 13 palavras seguidas
- Bom: alternar uma frase de 3 a 5 palavras com uma de 12 a 15

### C19 Espantalho
**M · J · F5, F6 · interna**
- Ruim pt: `Você pode estar pensando que é caro...`
- Bom pt: responder a objeção real do nicho, ou não responder nenhuma
- Ruim en: `You might be thinking this is expensive...`
- Bom en: `Ships in 2 days. Free returns for 30.`

## 5.3 Vocabulário

As listas vivem em `shared/lexico/pt-br.txt` e `shared/lexico/en.txt`, uma
entrada por linha com o ID da regra. Entrada nova exige caso em `scripts/tests/`.

### C20 Superlativo vazio de varejo
**A · R (léxico) · F1, F6 · confirmada**
- Ruim pt: `descontos extraordinários`, `ofertas jamais vistas`, `preços históricos`
- Bom pt: `30% OFF na linha de verão`
- Ruim en: `unbeatable savings`, `the ultimate deal`
- Bom en: `30% off summer styles`

### C21 Vocabulário de IA
**A · R (léxico) · F5, F6, F9, F2 · confirmada**
É a regra com a evidência mais forte do catálogo: a superrepresentação de certas
palavras em texto pós-LLM está quantificada em grandes corpora (as figuras exatas
estão em `docs/pesquisa/a-verificar.md`, use a regra, não cite números).
- Ruim pt: `jornada`, `mergulhe`, `desbloqueie`, `eleve`, `atemporal`, `essência`
- Bom pt: `use`, `leve`, `ganhe`, mais o fato do produto
- Ruim en: `elevate`, `unlock`, `journey`, `seamless`, `curated`, `timeless`
- Bom en: `use`, `get`, `wear`, mais o fato do produto

Nove palavras do grupo (crucial, fundamental, essencial e afins) entram em modo
densidade: acusam a partir de 3 ocorrências no mesmo e-mail, não na primeira.

### C22 Exclusividade genérica
**A · R (léxico) · F1 · interna**
- Ruim pt: `você foi escolhido`, `acesso VIP` sem clube real
- Bom pt: `Você está no Luxury Club desde março`
- Ruim en: `you've been selected`
- Bom en: `Members since March get first access`

### C23 Gerundismo e gerúndio conclusivo
**A · R (léxico) · F6, F5 · confirmada**
- Ruim pt: `vamos estar enviando`, `..., garantindo mais conforto`
- Bom pt: `enviamos`, `O forro é de algodão.`
- Ruim en: `..., ensuring comfort all day`
- Bom en: `The lining is cotton.`

### C24 Evasão do verbo ser
**M · R (léxico) · F5, F6 · confirmada**
- Ruim pt: `se apresenta como a solução`
- Bom pt: `é uma camiseta de algodão pima`
- Ruim en: `serves as the perfect companion`
- Bom en: `is a cotton tee`

### C25 Muleta de intensidade
**M · H densidade · F6 · confirmada**
Acusa a partir de 3 ocorrências no e-mail, não na primeira.
- Ruim pt: `muito`, `super`, `realmente`, `simplesmente`
- Bom pt: a medida no lugar do advérbio (`seca em 4h`)
- Ruim en: `truly`, `really`, `simply`
- Bom en: `dries in 4 hours`

### C26 Clichê de marca e de categoria
**A · R (léxico) · F1, F2 · interna**
Também é aqui que mora a homogeneização: a frase serve para qualquer loja.
- Ruim pt: `brilhe`, `sua história`, `autocuidado`, `uma nova era`
- Bom pt: `Banho de ouro 18k, 3 microns`
- Ruim en: `your story`, `self-care ritual`, `a new era`
- Bom en: `18k gold plating, 3 microns`

## 5.4 Forma e pontuação

### C30 Excesso de exclamação
**M · R · F2 · refinada**
Os dados de ESP são mistos; o que sustenta a regra é o corpus humano (0,6% das
palavras). Limite: no máximo 1 por e-mail, 0 no assunto de marca premium.
- Ruim: `Chegou!! Aproveite!!!`
- Bom: `Chegou. 20% OFF até domingo.`

### C31 Emoji decorativo
**M · R · F2, F6, F8 · refinada**
Evidência fraca a moderada. Vale a ficha da marca: no máximo 1 no assunto quando
a marca usa, 0 no corpo fora isso. No corpus humano, os 8 emojis estavam
concentrados em 1 marca de 35.

**Emoji no assunto só se a ficha da marca permitir.** O campo é
`marca_usa_emoji` em `marcas/<cliente>.md`. Sem ficha, ou com o campo
ausente, o padrão é **não permitir**: o lint trata como `false`.

Permitido significa no máximo 1 no assunto, nunca no corpo. Marca que usa
emoji no corpo declara isso na ficha e a divergência fica registrada lá.


### C32 Negrito pulverizado
**M · R · F5, F6 · confirmada**
Mais de 2 `<strong>` no mesmo parágrafo. Negrito é para o código do cupom e para
o valor da oferta.

### C33 Artefato de Unicode
**M · R · F5, F8 · confirmada**
Caractere invisível de preenchimento, espaço estreito, letra de falso negrito.
O preheader da Insider (F4) usa enchimento invisível: não copie isso.

### C34 Title Case em pt-BR
**M · R · F6 · interna**
- Ruim pt: `Frete Grátis Em Todo O Site`, `Uma Nova Era Começa`
- Bom pt: `Frete grátis em todo o site` ou `FRETE GRÁTIS`

**Escopo: só pt-BR.** Loja de idioma inglês **pode** usar Title Case no
assunto e no corpo, porque lá é convenção editorial, não vício. O lint
devolve zero achados de C34 quando `idioma` não é `pt-br`, e isso é
deliberado: não é lacuna de cobertura.

O idioma vem da ficha da loja (`marcas/<cliente>.md`), não do texto. Loja
inglesa com uma frase em português segue sendo loja inglesa.

Conflito conhecido: `vault/componentes/doutrina/subject-line-e-preview.md`
prescreve Title Case sem qualificar idioma. Em pt-BR, C34 vence. A
correção a fazer no vault está em `docs/pesquisa/vault-correcoes.md`.

### C35 Caixa alta em parágrafo
**M · R · arsenal · interna**
Caixa alta é legítima em headline curta, rótulo e botão (ver
`shared/calibracao.md`). O vício é o parágrafo gritado: o lint só acusa a partir
de 6 palavras seguidas em caixa alta.

## 5.5 Específicos de e-mail

### C40 Assunto longo
**M até 60 caracteres, A acima · R · F9, F4 · refinada**
A evidência sustenta "curto", não um número exato. Alvo 40 caracteres, ideal 25,
oferta ou mecânica no começo. Acima de 60 vira A. O limite definitivo sai de
teste A/B na base da Convertfy, não de benchmark de fornecedor.

### C41 Preheader vazio ou repetindo o assunto
**A · R (Jaccard acima de 0,6) · F4 · interna**
- Ruim: assunto `17% OFF no Luxury Club` mais preheader `17% OFF no Luxury Club`
- Bom: preheader `Código LUXURY17, válido até domingo`

### C42 Oferta só dentro da imagem
**A · H · F4, F9 · confirmada**
Evidência forte e por quatro caminhos ao mesmo tempo: entregabilidade,
acessibilidade, resumo de IA na caixa de entrada e imagem bloqueada. Exija 1
linha de texto vivo com o valor e o código, mais alt descritivo.

### C43 CTA criativo ou vago
**M · R · F2 · interna**
Verbo de compra mais objeto. No corpus, 64 CTAs se resumem a shop, claim,
explore, start, add, save, discover, find.
- Ruim pt: `Descubra a magia`
- Bom pt: `Comprar com 17% OFF`
- Ruim en: `Begin the experience`
- Bom en: `Shop the sale`

### C44 Mais de um destino principal
**M · H · F9 · confirmada**
Uma ação por e-mail. Repetir o mesmo CTA com o mesmo destino é permitido e é
padrão de mercado (ver `shared/calibracao.md`).

### C45 Corpo acima do orçamento do tipo
**A · H · F1, F2, F4 · refinada**
O ajuste da evidência é justamente que o teto depende do tipo:
welcome e campanha 80 palavras, carrinho 60, editorial e carta explicitamente
pedidas são exceção declarada no brief. Referência de mercado: Insider manda
605 caracteres de corpo médio, True Classic 935.

### C46 Condição da oferta ausente
**A · H · F2, F4 · confirmada**
Havendo desconto: valor mais código (ou "aplicado no carrinho"), mais prazo (ou
"por tempo limitado"), mais mínimo quando houver.

### C47 Personalização sem fallback
**A · R · F9 · interna**
`{{first_name}}` exige default e a frase precisa funcionar sem o nome.
Personalização por nome no assunto tem efeito pequeno e às vezes negativo, então
não pague o risco de um "Oi ," por um ganho que a literatura não garante.
