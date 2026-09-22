# Vícios de IA em E-mail Marketing de E-commerce
Pesquisa base para `shared/anti-vicios-copy.md`, `shared/anti-vicios-design.md`, `lint_copy.py` e `lint_email.py`
Convertfy · setembro/2026 · v1

---

## 0. Método e fontes

| # | Fonte | O que entrou | Confiabilidade |
|---|---|---|---|
| F1 | Histórico de conversas da Convertfy com Claude (2025–2026) | Rejeições reais do Bruno a copies geradas por IA e regras que ele já impôs em prompts de produção (n8n) | Alta: é o critério real de aprovação |
| F2 | Figma "Welcome flow" (fileKey yqPg1JqRC4Bib1tmcUFjgc): 35 e-mails de marcas reais, 607 blocos de texto únicos, 3.065 palavras | Métricas de copy humana de welcome e padrões de estrutura | Alta como amostra de mercado; contém contaminação de IA (ver §2.3) |
| F3 | Figma "Flow Templates" (YZ2GoLmOS9sD8J7Guuoicl) | Estrutura de templates; a copy é quase toda lorem ipsum | Baixa para copy, útil para estrutura |
| F4 | Trendtrack: 55 e-mails de welcome, promo e cupom (90 dias); análise de cadência de Insider (40 e-mails) e True Classic (40 e-mails); HTML integral de 1 campanha Insider | Benchmarks de volume de copy, cadência, padrões de assunto e anti-padrões de mercado | Alta (dado observado) |
| F5 | blader/humanizer (51k★): 25 padrões baseados no guia da Wikipedia "Signs of AI writing" | Taxonomia de vícios de escrita | Alta: é o catálogo mais adotado |
| F6 | Henzen3d/Deslop-ptBR (W1–W38 e tabela de substituições em tiers), mackswendhell/humanizer-pt-br (25 padrões), msigor/humanizer-br | Vícios específicos do português brasileiro | Média-alta |
| F7 | sam-paech/slop-score (EQ-Bench) e antislop-sampler | Método quantitativo: score = 60% palavras de slop, 25% padrão "não X, mas Y", 15% trigramas | Alta no método; as listas são de ficção em inglês e têm pouco uso direto |
| F8 | ravidsrk/slop-detect: 27 padrões de design e 9 de copy, com limiares de densidade | Detecção de "cara de IA" em layout e copy de marketing | Média-alta; cita estudo de Adrian Krebs (abr/2026) que não verifiquei na origem |
| F9 | CosmoBlk/email-marketing-bible v2.7 (§4, §5, §8, benchmarks) | Protocolo anti-slop específico de e-mail e benchmarks de 2026 | Média-alta; a afirmação "Google filtra mais texto com alta similaridade de IA" não tem fonte primária no arquivo |
| F10 | Impeccable (craft-floor, audit), Taste Skill (§0 e §4, redesign, output-skill, research/laziness), Emil Kowalski (review-animations) | Arquitetura Verify/Refuse, postura de revisão e disciplina contra truncamento | Alta como método; os números do research/laziness (ex.: "+45% com gorjeta") são folclore sem fonte primária e ficaram fora das regras |

**Limitações honestas:**
- O vault do Obsidian não está acessível desta conversa, só pelo Claude Code (prompt no §10).
- A busca na web está desligada. Estudos de caso publicados (Litmus, Klaviyo, Omnisend, estudos acadêmicos sobre percepção de copy de IA) ficam para a pesquisa estendida.

---

## 1. Evidência interna: o que a Convertfy já rejeitou (F1)

É o sinal mais forte da pesquisa, porque mostra o que já foi reprovado em produção.

| Vício observado em saída de IA | Onde apareceu | Reação / regra resultante |
|---|---|---|
| Travessão (— e –) mesmo com proibição no prompt | Prompt de copy n8n (ago/2025): "Uso de travessões apesar das proibições" | Proibição repetida em vários pontos, checklist e autocorreção. **Prova de que a regra no prompt não basta: precisa de lint determinístico.** |
| Cupom no idioma errado (PEDIDO18 em loja inglesa) | Mesmo prompt | Regra: cupom sempre no idioma da loja |
| Excesso de opções e texto longo na hero | Hero de antecipação de Black Friday (nov/2025): 5 variações de 4 linhas | "está muito grande, deve ser mais compacto" |
| Superlativo vazio de varejo: "descontos extraordinários", "ofertas jamais vistas", "preços históricos", "prepare-se para o impossível", "você foi escolhido" | Mesmas variações | Ficaram como padrão a evitar (sem fato que sustente) |
| Storytelling com cena fabricada ("são 11 de novembro, 7:15 da manhã", "pela segunda vez esse mês, estou escrevendo…") | Adaptação de e-mail de Clube VIP (nov/2025) | Origem da preferência "storytelling forçado" |
| **Números inventados** ("32.541 clientes ativos", "18.923 compraram", "menos de 1%") | Mesma adaptação | Não houve regra explícita, mas é risco legal e de confiança. Vira regra dura |
| Copy de framework (Hormozi, "meu contador disse que sou LOUCO", "PARTE 1: EDUCAÇÃO") | Estratégia 11.11 (nov/2025) | Tom de infoproduto transplantado para e-commerce |
| Rebranding com clichês ("Uma Nova Era Começa", "Evoluímos para Você", "Porque você merece sempre o melhor") | Visuprime → LensEvo (set/2025) | Frases genéricas que servem para qualquer marca |
| Explicação da própria copy junto da entrega ("A copy é totalmente centrada nos benefícios…", "Por que esse post vai performar") | Vários | Em produção, a saída deve ser só o artefato |
| Copy informacional sem nada em jogo | Ganchos de reels (jul/2026) | Diagnóstico: "eram informacionais, nenhum tocava um pecado" |
| Body longo em sequência de campanha | Vivazz (jun/2026) | Curva de tamanho: ~150 → 140 → 85 palavras ao longo da semana |
| Preferência confirmada pelo que foi escolhido | Luxury Club (jan/2026) | Escolheu "Sua entrada no Luxury Club começa com 17% OFF" + "Acessórios, roupas, relógios e sapatos premium": benefício direto, sem narrativa |
| Fichas e descrições com linguagem interpretativa | Arsenal de heros (2026) | "Sem frases de efeito ou linguagem interpretativa"; "texto de exemplo extraído literalmente, nada inventado" |

**Padrão por trás de tudo:** a IA escolhe **intensidade** (superlativo, drama, cena, número grande) quando falta **fato**. O vício de fundo é compensar ausência de informação com volume.

---

## 2. Corpus humano: 35 e-mails de welcome no Figma (F2)

### 2.1 Métricas

| Métrica | Valor | Leitura |
|---|---|---|
| Palavras por bloco de texto | média 5,0 · mediana 3 · máx. 38 | E-mail de welcome é feito de rótulos, não de parágrafos |
| Blocos com ≤5 palavras | 465 de 607 (77%) | Headline, benefício, nome de produto, CTA |
| Blocos com >20 palavras | 14 de 607 (2,3%) | Parágrafo longo é exceção, geralmente 1 por e-mail |
| Blocos com número, %, $ ou código | 113 (19%) | Fato concreto aparece a cada ~5 blocos |
| Exclamação | 19 em 3.065 palavras (0,6%) | Rara |
| Travessão | 10 em 3.065 (≈1 a cada 300 palavras) | Aparece, e sempre nas linhas com mais cara de IA (§2.3) |
| Emoji | 8, concentrados em 1 marca (Bible Welcome) | Não é padrão do corpus |
| Verbo inicial dos CTAs (n=64) | shop 18 · claim 9 · explore 7 · start 5 · add 4 · save 3 · discover 3 · find 3 | CTA humano é verbo de compra + objeto, sem criatividade |

### 2.2 Padrões humanos que a skill deve copiar

1. **Oferta em texto, com código visível:** "Use code WELCOME10 today and start your AB BIO® routine with savings." A frase só entrega o código e a ação.
2. **Benefício físico e mensurável:** "Hot baths, anywhere. The Joolca HOTTUB inflates fast and keeps water warm for hours." / "Feel sharper in 3 minutes."
3. **Reconhecimento do problema em linguagem do cliente:** "If your mattress feels almost right (but you still wake up tired), let's fix that." (Helix). É a melhor linha do corpus: problema específico, sem drama.
4. **Rótulos de 2 a 3 palavras** para diferenciais: "Cruelty Free / Women Founded / Ethically Sourced"; "Ice Making / Plug & Play / 1 Year Warranty".
5. **Prova com número:** "Proven by 370+ reviews", "4.9 - 108 Reviews", "82% increased deep sleep cycles".
6. **Navegação por intenção:** "A few best places to begin, depending on your goal:" / "Shop by concern".

### 2.3 Contaminação: o swipe também tem vício de IA

Linhas do próprio corpus que o lint deve reprovar:
- "Together, they don't just train you, **they transform you.**" (não X, mas Y)
- "A science-backed ritual for the bold**—**reset, recharge, and perform at your peak." (travessão + tríade)
- "perform better, recover faster, and transform deeper" (tríade rítmica)
- "Your journey with DYC is just beginning, and the possibilities are limitless." (jornada + possibilidades ilimitadas)
- "Reignite your routine, reset your goals, and return stronger, no pressure, just results."

**Consequência para o vault:** toda nota var2 que cita copy literal de swipe precisa passar pelo `lint_copy.py` antes de virar referência, senão o Estruturador e o redator aprendem o vício com o exemplo. Sugestão: marcar a amostra com `lint_status: limpa | contaminada` no frontmatter.

---

## 3. Mercado: o que marcas grandes realmente mandam (F4)

| Observação | Dado | Implicação para a skill |
|---|---|---|
| Insider (BR, moda) | ~8 e-mails/semana, corpo médio de **605 caracteres** (≈100 palavras incluindo rodapé legal) | Campanha brasileira de alto volume tem copy mínima; o peso vai para assunto, preheader e imagem |
| Campanha Insider "Mês do Cliente: pense melhor" | HTML de 6,3 KB: 1 imagem 600px (headline e oferta dentro da imagem) + rodapé. Imagem principal **sem alt**; preheader "Até 40% OFF em produtos selecionados para escolher melhor." seguido de caracteres invisíveis de preenchimento | Formato viável, mas falha em acessibilidade e no resumo por IA do Gmail/Apple (lê o texto vivo). A skill deve exigir alt descritivo com a oferta e 1 linha de texto vivo |
| Assuntos Insider | "Combine e ganhe 1 best-seller", "Frete grátis e 1 item de brinde nessa combinação.", "Último dia para combinar e ganhar com frete grátis" | Assunto = mecânica da oferta, sem adjetivo |
| True Classic (EUA, DTC) | Corpo médio de 935 caracteres; assuntos "20% Off Sitewide Is Live", "You've Missed A Few Things" | Mesmo padrão: oferta literal ou curiosidade curta |
| Anthropologie | "Extra 40% Off Sale is LIVE", "24hrs early: extra 50% off sale", "we call these "personality pieces"" | Números e prazos no assunto; tom da marca aparece só em 1 de cada ~5 |
| L.L.Bean welcome | "We're só glad you stopped by. Let's celebrate! 10% OFF YOUR ORDER" + "One-time-use offer, exclusions apply." | Até a marca grande usa a frase de boas-vindas pronta; o diferencial está na condição clara |
| **Anti-padrão de mercado: Always Fit** (BR, suplementos) | Assuntos de campanha promocional disfarçados de transacional: "Resposta: Seu pedido foi aprovado", "(RE): confirmação do seu pedido", "✅ Seu pedido foi revisado", "Aviso: Seu novo pedido está confirmado ✅" | **Assunto enganoso** é o vício de desespero, não de IA, mas IA reproduz quando mandada "aumentar abertura". Gera reclamação de spam, risco regulatório (CAN-SPAM proíbe assunto enganoso; LGPD e CDC tratam publicidade enganosa) e desconfiança. Regra dura na skill |

**Benchmarks de referência (F9, meados de 2026, direcionais):** welcome 50–60% abertura / 5–8% clique; carrinho 40–50% / 5–10%; promocional 15–20% / 2–3%; reclamação saudável < 0,05%, crítica > 0,1%; frequência DTC 3–5×/semana. Assuntos abaixo de ~25 caracteres abrem mais; um único CTA supera vários (+42%); botão supera link de texto (+27%). São números agregados do mercado americano; servem para calibrar, não como promessa.

---

## 4. O que a pesquisa externa diz sobre vício de IA

### 4.1 Mecanismo (por que a IA escreve assim)
- **Previsão da mediana:** o modelo tende ao texto mais provável para a categoria. Resultado: toda loja de joias vira "atemporal", "elegância", "sua história" (F9 §5: "LLMs predict the median; divergence has to come from outside the model").
- **Intensidade no lugar de fato** (F5 grupo C, "Inflation and borrowed authority"): sem dado concreto, o modelo infla o significado.
- **Ritmo por regra** (F5 grupo B): tríades, frases com mesma abertura, travessão como conector universal, frases de tamanho uniforme (F6 msigor: "uniformidade no tamanho das frases").
- **Encenação no lugar de afirmação** (F5 grupo A): "não X, mas Y", fecho de uma linha dramático, frase que soa profunda, rodeio antes do ponto, discutir com ninguém.
- **Resíduo de chat** (F5 grupo E): "Aqui está…", explicar a versão anterior, ressalvas.
- **Truncamento deliberado** (F10 Taste research): o modelo encurta quando a tarefa tem muitos requisitos. Em e-mail, aparece como seção faltando, placeholder repetido e "o resto segue o mesmo padrão".

### 4.2 Como medir (e não só listar)
- **Slop score EQ-Bench (F7):** composição ponderada (60% vocabulário, 25% construção não-X-mas-Y, 15% trigramas), normalizada por mil palavras.
- **slop-detect (F8):** limiar por **densidade**, não por ocorrência. "Um travessão é normal; um a cada 40 palavras é máquina." Exemplos de limiar: travessão ≥4 com ≥7/1000 palavras; antítese ≥2; tríades ≥3; "seja você X ou Y" ≥1; emoji no início de linha ≥3; buzzwords ≥4 distintas.
- **Adaptação para e-mail:** e-mail tem 40–150 palavras, então limiar por mil palavras não funciona. **Usar contagem absoluta por e-mail**, com tolerância zero para os itens da Convertfy (travessão, número inventado, assunto enganoso).

### 4.3 Especificidade é o humanizador mais barato (F9 §4)
Troca simples que remove mais "cara de IA" que qualquer lista de palavras: um número real, um nome de produto real, uma condição real (prazo, valor mínimo, frete). O corpus humano (§2.1) confirma: 19% dos blocos carregam número ou código.

---

## 5. Catálogo consolidado: vícios de COPY

Severidade: **B** = bloqueia entrega · **A** = alta, corrigir · **M** = média, aceitável se isolado.
Detecção: **R** = regex no lint · **H** = heurística no lint · **J** = julgamento do revisor (LLM crítico).

### 5.1 Regras duras da Convertfy

| ID | Vício | Sev. | Det. | Ruim | Bom | Fonte |
|---|---|---|---|---|---|---|
| C01 | Travessão — ou – em qualquer campo (assunto, preheader, alt, botão) | B | R | "Sua oferta chegou — aproveite" | "Sua oferta chegou: aproveite" | F1 |
| C02 | Número, estatística, contagem de clientes ou avaliação inventados | B | J+H (número sem origem no brief) | "32.541 clientes ativos" | usar só números do brief/loja ou omitir | F1 |
| C03 | Assunto que simula transação, resposta ou pedido ("RE:", "Seu pedido foi aprovado", "Aviso:") em campanha | B | R | "(RE): confirmação do seu pedido" | "R$30 OFF acima de R$100 até domingo" | F4 |
| C04 | Cupom, CTA ou qualquer trecho em idioma diferente do idioma da loja | B | H | PEDIDO18 em loja EN | ORDER18 | F1 |
| C05 | Cena ou storytelling fabricado (hora, data, "estou escrevendo este e-mail…", personagem) | B | R+J | "São 11 de novembro. 7:15 da manhã." | ir direto à condição | F1 |
| C06 | Urgência ou escassez falsa (estoque, prazo ou exclusividade que não existem no brief) | B | J | "Últimas unidades" sem dado de estoque | prazo real do cupom | F1, F4 |
| C07 | Comentário sobre a própria copy junto da entrega | B | R ("a copy", "essa versão", "por que funciona") | "A copy é centrada em…" | entregar só os campos | F1 |

### 5.2 Estrutura e retórica

| ID | Vício | Sev. | Det. | Ruim | Bom | Fonte |
|---|---|---|---|---|---|---|
| C10 | Antítese "não é X, é Y" / "não só X, mas Y" / "mais que X" | A | R | "Não é só uma joia, é a sua história." | "Prata 925, banho de ródio. Não escurece." | F5 #1, F6 W5, F8 |
| C11 | Tríade ornamental (três adjetivos ou três verbos em ritmo) | A | R (`\w+, \w+ e \w+` em adjetivos/verbos) | "Conforto, estilo e elegância" | 1 atributo com prova | F5 #6, F6 W6 |
| C12 | Fecho de falsa profundidade / frase de efeito solta | A | H (linha final curta sem fato) | "Porque você merece." | CTA + condição | F5 #2–3, F6 W13 |
| C13 | Revelação teatral com dois-pontos ou reticências | M | R | "E o melhor: …" / "Só que tem um detalhe…" | afirmar direto | F6 W7 |
| C14 | "Seja você X ou Y" / "Para quem X e para quem Y" | M | R | "Seja para o trabalho ou para o fim de semana" | escolher um uso | F6 W11, F8 |
| C15 | Pergunta retórica de abertura | M | R (linha 1 termina em ?) | "Já pensou em ter um sono perfeito?" | "Se você acorda cansado mesmo dormindo 8h…" | F6 W17 |
| C16 | Abertura genérica / pigarro | A | R | "No mundo de hoje…", "Quando se trata de…", "Estamos muito felizes em…" | primeira frase = oferta ou problema | F5 #4, F6 W4, W10 |
| C17 | Recapitulação no final ("Em resumo", "Não perca") | M | R | "Resumindo: …" | cortar | F6 W14 |
| C18 | Frases de tamanho uniforme (ritmo metronômico) | M | H (desvio-padrão baixo do tamanho das frases) | 4 frases de 11–13 palavras | alternar 3–5 palavras com 12–15 | F6 W27, F9 §4 |
| C19 | Discutir com objeção que ninguém fez / espantalho | M | J | "Você pode estar pensando que é caro…" | responder objeção real do nicho | F5 #5, F6 W37 |

### 5.3 Vocabulário (listas vivas, por idioma)

| ID | Vício | Sev. | Det. | Exemplos (pt-BR) | Exemplos (EN) | Fonte |
|---|---|---|---|---|---|---|
| C20 | Superlativo vazio de varejo | A | R | extraordinário, jamais visto, histórico, imperdível, incrível, inédito, sem igual, único | unbeatable, incredible, unmatched, ultimate | F1, F6 W8 |
| C21 | Vocabulário de IA | A | R | jornada, mergulhar, desbloquear, elevar, transformar, potencializar, alavancar, ecossistema, universo, experiência única, atemporal (sem contexto), essência | elevate, unlock, journey, seamless, effortless, curated, crafted, timeless, delve, unleash | F5 #12, F6 tier 1A, F9 §4, F2 |
| C22 | Exclusividade genérica | A | R | "você foi escolhido", "seleto grupo", "só para você" (sem segmentação real), "acesso VIP" (sem clube real) | "you've been selected", "exclusive access" | F1 |
| C23 | Gerundismo e gerúndio conclusivo | A | R | "vamos estar enviando", "…, garantindo mais conforto" | "…, ensuring comfort" | F6 W1–W2, F5 #15 |
| C24 | Evasão do verbo ser | M | R | "se apresenta como", "atua como", "funciona como a solução" | "serves as", "stands as" | F5 #18, F6 #9 |
| C25 | Muleta de intensidade | M | H (densidade) | muito, super, realmente, totalmente, simplesmente | truly, really, simply | F6 W28 |
| C26 | Clichê de marca/categoria | A | R + lista por nicho | joias: "brilhe", "sua história", "atemporal"; moda: "estilo que fala por você"; beleza: "autocuidado", "ritual" | "your story", "self-care ritual" | F1, F2 |

### 5.4 Forma e pontuação

| ID | Vício | Sev. | Det. | Regra | Fonte |
|---|---|---|---|---|---|
| C30 | Excesso de exclamação | M | R | máx. 1 por e-mail; 0 em assunto de marca premium | F2 (0,6% no corpus) |
| C31 | Emoji decorativo | M | R | máx. 1 no assunto quando a marca usa; 0 no corpo, salvo marca que usa (ficha da marca) | F2, F6 W21, F8 |
| C32 | Negrito pulverizado | M | R (>2 `<strong>` por parágrafo) | negrito só em código de cupom e valor da oferta | F5 #19, F6 W30 |
| C33 | Aspas curvas/tipográficas misturadas, caracteres invisíveis, letras "fake bold" Unicode | M | R | normalizar | F5 #21, F8 unicode_artifacts |
| C34 | Title Case em pt-BR ("Frete Grátis Em Todo O Site") | M | R | caixa de frase ou caixa alta total, nunca Title Case em PT | F6 #17 |
| C35 | Caixa alta em parágrafo | M | R | caixa alta só em headline curta, rótulo e botão | arsenal |

### 5.5 Específicos de e-mail

| ID | Vício | Sev. | Det. | Regra | Fonte |
|---|---|---|---|---|---|
| C40 | Assunto longo | A | R | alvo ≤ 40 caracteres, ideal ≤ 25; oferta ou mecânica no começo | F9 §8, F4 |
| C41 | Preheader repetindo o assunto ou vazio | A | R (similaridade) | preheader completa a informação: condição, prazo ou produto | F4 |
| C42 | Oferta só dentro da imagem | A | H (nenhum texto vivo com %, R$ ou código) | 1 linha de texto vivo com a oferta, e alt com a oferta | F4, F9 §5 |
| C43 | CTA criativo ou vago | M | R | verbo de compra + objeto: "Comprar com 10% OFF", "Ver a coleção" (F2: shop/claim/explore dominam) | F2 |
| C44 | Mais de 1 CTA principal com destinos diferentes | M | H | 1 ação principal; CTAs repetidos com o mesmo destino são permitidos | F9 §8 |
| C45 | Body acima do orçamento do tipo de e-mail | A | H | welcome/campanha ≤ 80 palavras fora de nomes de produto; carrinho ≤ 60; editorial/carta explicitamente pedida é exceção | F1, F2, F4 |
| C46 | Condição da oferta ausente | A | H | se há desconto: valor + código ou "aplicado no carrinho" + prazo ou "por tempo limitado" + mínimo, se houver | F2, F4 |
| C47 | Personalização sem fallback | A | R | `{{first_name}}` exige default; frase deve funcionar sem o nome | F9, chappie |

---

## 6. Catálogo consolidado: vícios de DESIGN de e-mail

**Atenção:** metade dos padrões de "cara de IA" na web é **convenção legítima de e-mail** (centralizado, caixa alta, número grande de oferta, coluna única). Importar lista de web sem filtro quebraria o arsenal. A coluna "Status em e-mail" resolve isso.

| ID | Padrão | Status em e-mail | Regra | Fonte |
|---|---|---|---|---|
| D01 | Gradiente roxo→azul, CTA índigo/violeta | **Vício** | proibido salvo cor da marca | F8 purple_accent, F9 |
| D02 | Texto em gradiente, glow colorido, glassmorphism, blobs "aurora" | **Vício + quebra** | proibido (não renderiza em Outlook e marca IA) | F8, F10 |
| D03 | Fundo creme/bege por padrão | **Vício** | fundo branco por padrão Convertfy; bege só se for da marca | F8 cream_default_bg (peso 7), F9 "beige wash" |
| D04 | Cinza-claro em texto de corpo (<4,5:1) | **Vício** | contraste mínimo 4,5:1; corpo em #000/#1A1A1A | F8 low_contrast (peso 7), Impeccable |
| D05 | Texto cinza sobre fundo colorido | **Vício** | texto sobre cor = branco ou preto | F8 gray_on_color |
| D06 | Fonte padrão de IA como voz display (Inter, Geist, Space Grotesk) | **Revisar** | o arsenal usa Inter Tight/Inter. Em e-mail, a maioria dos clientes cai no fallback (Helvetica/Arial), então o risco é menor. Ainda assim, quando a marca tem fonte própria, usar a da marca nas imagens e títulos | F8 slop_fonts (peso 8), memória do arsenal |
| D07 | Pílula "eyebrow" acima da headline ("NOVO", "✨ Lançamento") | **Revisar** | sobrescrito é legítimo quando carrega informação (prazo, condição). Proibido quando é decorativo ou com emoji ✨ | F8 hero_eyebrow_pill, Impeccable ban |
| D08 | Grade de cards idênticos com ícone no topo (3 benefícios) | **Revisar** | permitido em faixa de diferenciais curta; proibido como estrutura principal do e-mail | F8 icon_card_grid, Impeccable |
| D09 | Banner de estatísticas ("10k+ / 4.9 / 98%") | **Revisar** | permitido apenas com números reais do brief | F8 stat_banner + C02 |
| D10 | Avatares de iniciais em gradiente nos depoimentos | **Vício** | foto real do cliente/produto ou nenhuma imagem; nunca avatar genérico | F8 gradient_letter_avatars |
| D11 | Cards dentro de cards, bordas coloridas grossas à esquerda | **Vício** | 1 nível de contêiner | F8 nested_cards, accent_stripe; Impeccable |
| D12 | Hierarquia tipográfica achatada (tamanhos próximos) | **Vício** | razão ≥ 2:1 entre headline e corpo | F8 flat_type_hierarchy |
| D13 | Headline gigante com frase longa | **Vício** | headline display ≤ ~40 caracteres; frase longa desce para corpo | F8 oversized_hero_h1 |
| D14 | Tracking negativo forte em display / tracking largo em corpo | **Vício** | display ≥ −0,02em; corpo 0 | F8 |
| D15 | Imagem de IA genérica (pessoas plásticas, produto flutuando em fundo abstrato) | **Vício** | foto real da loja; IA só para fundo/cena quando o brief aprova, com checklist | F9 §5, Taste imagegen |
| D16 | Centralizado + 3 cards + CTA (template de landing page) | **Revisar** | centralizado é convenção; o vício é a sequência genérica. Estrutura deve vir do vault (var2) | F9 "centred hero + three cards" |
| D17 | E-mail só imagem, sem alt | **Vício** | alt descritivo com oferta; 1 linha de texto vivo | F4 Insider |
| D18 | Recursos que quebram (position:absolute, transform, border-radius em img, webfont sem fallback, SVG inline) | **Bloqueia** | lint | arsenal, F10 |
| D19 | Dark mode por inversão ingênua (#000 puro, logo branco sem fundo) | **Vício** | #121212 em vez de #000; logos com versão para fundo escuro | F9 §5 |
| D20 | Espaço vazio órfão / blocos com respiros irregulares | **Vício** | ritmo vertical fixo por seção do arsenal | CosmoBlk email-design |

---

## 7. Vícios de PROCESSO do agente

Não aparecem no texto final, mas são a origem dos vícios acima.

| ID | Vício | Correção na skill | Fonte |
|---|---|---|---|
| P01 | Gerar sem ler marca, produto e oferta reais | Bloquear geração sem `marcas/<cliente>.md` + brief com oferta, produto e prazo | F9 "context beats prompt" |
| P02 | Preencher lacuna com invenção (número, estoque, prazo, depoimento) | Campo sem dado → pergunta única ou placeholder `[FALTA: …]`, nunca invenção | F1 |
| P03 | Várias variações "tintas da mesma ideia" | Variantes divergem em eixo nomeado (oferta / prova / problema) | Emil prototype |
| P04 | Truncar: seção faltando, "o resto segue o padrão", placeholder repetido | Contar entregáveis antes e depois; checar placeholders enumerados | Taste output-skill, arsenal |
| P05 | Confiar só no prompt para regra dura | Regra dura = lint determinístico + gate de entrega | F1 (travessão escapou mesmo proibido) |
| P06 | Autoaprovação | Revisor separado, contexto limpo, nota /10, máx. 4 rodadas; "por padrão aponta problema" | F9 critic loop, Emil review |
| P07 | Copiar vício do exemplo | Lint nas amostras do vault (`lint_status`) | §2.3 |
| P08 | Escrever antes de decidir a estrutura | Ordem: intenção (var1) → estrutura (var2) → variantes do arsenal → copy por schema | vault Estruturador |
| P09 | Tom de outro mercado (infoproduto/Hormozi em e-commerce) | Ficha de marca define registro; lista de frases de infoproduto no lint | F1 |

---

## 8. Calibração: o que NÃO é vício em e-mail de e-commerce

Para o lint não gerar falso positivo:
- Caixa alta em headline curta, rótulo e botão.
- Layout centralizado e coluna única de 600px.
- Número grande de oferta ("15% OFF") como elemento visual.
- Repetir o mesmo CTA com o mesmo destino ao longo do e-mail.
- "Shop now", "Comprar agora", "Aproveitar" como CTA.
- Frases prontas curtas de boas-vindas ("Que bom ter você aqui") quando seguidas imediatamente da oferta. Marcas grandes usam (L.L.Bean).
- Um parágrafo de 25–40 palavras no e-mail inteiro, quando é a única explicação do produto.

---

## 9. Especificação dos linters

### 9.1 `lint_copy.py` (entrada: JSON com assunto, preheader, blocos, CTAs, alts; idioma da loja)

| Regra | Implementação | Limiar |
|---|---|---|
| C01 | `[—–]` em qualquer campo | 0 → bloqueia |
| C03 | `^\(?(RE|FW|Fwd)\)?:`, `pedido (foi )?(aprovado|confirmado|revisado)`, `^aviso:` no assunto de campanha | 0 → bloqueia |
| C04 | detecção de idioma por campo + regex de cupom com palavra do idioma errado | 0 → bloqueia |
| C05 | `\b\d{1,2}(:\d{2})? da (manhã|tarde|noite)\b`, `estou escrevendo`, `são \d+ de \w+` | 0 → bloqueia |
| C07 | `\b(a copy|essa versão|por que (isso )?funciona|aqui está)\b` | 0 → bloqueia |
| C02 | todo número no output precisa existir no brief (`brief_numbers`) ou ser preço/percentual da oferta | 0 números órfãos → senão bloqueia |
| C10 | `n[ãa]o (é|e) (s[óo] )?\w+.{0,40}(é|mas)`, `mais (do )?que (um|uma)`, `not (just|only)`, `it'?s not` | ≥1 → alta |
| C11 | três itens separados por vírgula + "e/and" em ≤ 8 palavras | ≥1 → alta |
| C16, C17, C20–C26 | listas em `shared/lexico/<idioma>.txt` (vivas, com contagem por e-mail) | ≥1 → alta; C25 por densidade |
| C18 | desvio-padrão do tamanho das frases < 3 palavras com ≥4 frases | média |
| C30–C35 | contagens simples | ver §5.4 |
| C40–C47 | tamanho, similaridade assunto×preheader (Jaccard > 0,6), presença de %/R$/código em texto vivo, fallback de merge tag | ver §5.5 |

Saída: `{regra, severidade, campo, trecho, sugestao}`. Entrega bloqueada se houver qualquer B.

### 9.2 `lint_email.py` (entrada: HTML final)
- D18: `position:\s*absolute`, `transform:`, `<img[^>]*border-radius`, `@font-face` sem fallback, `<svg`
- D17: `<img` sem `alt` ou alt vazio em imagem >200px de largura
- D04/D05: cores inline de texto × fundo do `td` pai → contraste < 4,5
- Tamanho > 102 KB (clipping do Gmail)
- Container ≠ 600/598 (decisão pendente do arsenal)
- Preheader ausente
- CTA como imagem sem texto vivo equivalente
- Placeholder repetido idêntico (regra do arsenal)
- D01–D03: cores índigo/violeta em botão e fundo bege, quando não constam em `marcas/<cliente>.md`

---

## 10. Próximas etapas desta pesquisa

1. **Minerar o vault no Claude Code:**
   > Leia vault/ inteiro. Liste toda correção, rejeição ou "não usar" registrada em aprendizados/, estruturas/ (seções "quando não usar" e "o que varia por loja") e intencoes/. Para cada uma, gere uma linha no formato do catálogo (ID, vício, severidade, detecção, ruim, bom, fonte = caminho da nota) e junte em docs/pesquisa/vault-vícios.md. Depois rode lint_copy.py em toda copy literal citada nas notas var2 e adicione `lint_status` ao relatório (não edite o vault).
2. **Ampliar o corpus Figma:** exportar os 166 templates de seção (EFXQtHBW2mJ3itOZxtHeFe) e medir o mesmo que no §2.1 por categoria de bloco.
3. **Corpus Trendtrack por nicho dos clientes:** 20 lojas (joias, moda masculina, suplementos, casa), BR e EUA; medir tamanho de corpo, assunto, presença de alt/texto vivo e cadência. Isso vira `docs/pesquisa/benchmark-nicho.md`.
4. **Casos A/B internos:** transformar os testes que a Convertfy já rodou (HeroBoxers contra estruturas próprias, popup de roleta da Palm Row) em evidência para as regras com status `confirmado`.
5. **Estudos de caso publicados:** percepção de copy de IA pelo consumidor, impacto no inbox placement e testes de marcas com copy gerada vs editada. Depende de busca na web (abaixo).
