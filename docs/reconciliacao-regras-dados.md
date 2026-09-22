# Reconciliação: regras × dados da carteira

Cruzamento do catálogo (C01–C47, D01–D31, P01–P09) com os dados do pacote
BFCM e do vault.

**Índice 1 = a receita por mil média da própria loja.** Índice 2 = o
dobro. Fonte da definição: `09_Dados/Base de dados do estudo (dicionario
e metodo).md`, seção B.2.

## Regra de aplicação

| Veredito | O que foi feito |
|---|---|
| CONFIRMADA | Aplicada agora |
| REFINADA | **Redação proposta, aguardando aprovação.** Nada aplicado |
| CONTRADITA | **Redação proposta, aguardando aprovação.** Nada aplicado |
| SEM DADO INTERNO | Fica como está |

**Nenhuma regra de nível 1 foi alterada.** C02, C06 e a parte de
simulação do C03 são inegociáveis por hierarquia, mesmo quando um dado
de desempenho aponta o contrário.

---

## Os 9 conflitos que precisam de decisão

### a. C03 × família "Confirmação de algo que já é da pessoa" — REFINADA

| | |
|---|---|
| **Dado a favor** | "Your coupon has been approved ✅" = **1,86** (7.7 às 7h). "your access is confirmed ✅" = **1,48**, 3 de 3 lojas. "🚨 Your status has just changed" = **2,13** (5 de 5) e **1,71** (4 de 5) |
| **Dado contra** | Assunto com "Fwd:" ou "Enc:" = **0,39 a 0,49** |
| **Fonte** | `08_Skill/SKILL...md:118-128`; `04_Assuntos/Assunto - Confirmação de algo que já é da pessoa.md`; `04_Assuntos/Assunto - Aviso de mudança de estado.md` |

Os dados separam duas coisas que o C03 atual trata como uma só. Simular
encaminhamento (`Fwd:`) é o pior assunto da base. Afirmar um estado
verdadeiro é o melhor.

**Redação proposta:**

> **C03.** Proibido simular pedido, resposta ou encaminhamento que não
> existe: `RE:`, `Fwd:`, `Enc:`, "seu pedido foi aprovado", "confirmação
> do seu pedido", "aviso:" genérico.
>
> **Permitido** afirmar um estado verdadeiro de algo que a loja
> realmente concedeu: "seu cupom foi liberado", "seu acesso está
> confirmado", "seu status mudou", desde que o brief declare o benefício
> concedido no campo `beneficio_concedido`.
>
> Sem esse campo no brief, o assunto continua bloqueado. O teste é
> factual, não estilístico: a loja concedeu mesmo?

**Mudança no lint:** `regra_c03` ganha duas listas. A de simulação segue
bloqueando sempre. A de confirmação de estado só bloqueia quando
`beneficio_concedido` está ausente do payload. Mesmo desenho do
`encerra_ciclo` de V29.

**Recomendação: aprovar.** O dado é forte (5 de 5 lojas), a distinção é
factual e verificável, e o nível 1 continua protegido: o que a loja não
concedeu segue proibido.

---

### b. C31 e C30 × emoji validado — REFINADA

| | |
|---|---|
| **Dado** | Os assuntos de maior receita da base **têm emoji**: ✅ (1,86 e 1,48), 🚨 (2,13), 👀 (1,77), 🎟️ (1,43), 🤫 (1,50), 🟥 (1,65), 🔓 e 🎁 no Q4 |
| **Regra interna** | "no máximo 1 emoji no assunto", `05_Modelos_validados/regras-de-copy-de-campanha.md` |
| **Fonte** | `08_Skill/SKILL...md:118-128`; `04_Assuntos/` (18 notas) |

A regra da casa e o dado concordam entre si, e **discordam do nosso
padrão**, que é zero emoji sem ficha da marca.

**Redação proposta:**

> **C31.** Máximo 1 emoji no assunto, no começo ou no fim. O padrão para
> loja **sem ficha** passa de zero para um. Zero no corpo, sempre.
> Emoji no corpo continua exigindo autorização na ficha.
>
> **C30.** Máximo 1 exclamação por e-mail, mantido. O corpus humano dá
> 0,6% de exclamação, e nenhum assunto validado usa.

**Mudança no lint:** `regra_c31` passa a permitir 1 emoji no assunto por
padrão. `marca_usa_emoji: false` na ficha volta o limite a zero, para
marca premium. C30 não muda.

**Recomendação: aprovar.** É a regra da própria casa, sustentada por 9
famílias de assunto validadas. O risco fica coberto pelo opt-out da ficha.

---

### c. C05 × formatos de persona — REFINADA

| | |
|---|---|
| **Dado** | "Cupom liberado (texto de pessoa)" = **1,66** nas 9 lojas, 1,78 na Clube Rock. "Status mudou (conversa de celular)" = **1,48** em 33 lojas. "Reabertura (texto do fundador)" = **1,15**. "Ligação" = **1,17**, promovido a titular |
| **Dado contra** | "Depoimento sem oferta: abre, mas vende pouco" |
| **Fonte** | `08_Skill/SKILL...md:30-56`, `05_Modelos_validados/ranking-de-modelos.md` |

O catálogo trata "cena fabricada" e "formato de conversa" como a mesma
coisa. Os dados mostram que o formato é dos melhores da carteira.

**Redação proposta:**

> **C05.** Proibida **cena fabricada**: hora inventada, data inventada,
> personagem que não existe, "são 11 de novembro, 7:15 da manhã", "pela
> segunda vez esse mês estou escrevendo".
>
> **Permitido formato de conversa ou persona** (texto de pessoa, texto
> do fundador, texto da gerente, conversa de celular, ligação,
> notificação, jornal) quando: (1) a pessoa existe e assina de verdade,
> (2) nenhum fato dentro do formato é inventado, e (3) o formato carrega
> a oferta, não substitui ela.
>
> O teste: tire o formato. Sobra uma oferta com condição? Se não sobra,
> é cena.

**Mudança no lint:** a regex de C05 deixa de casar assinatura de pessoa e
marcador de conversa. Continua casando hora e data fabricadas. Novo
campo opcional `formato_persona` no payload declara o formato.

**Recomendação: aprovar.** São 4 dos 6 modelos titulares do ranking. Sem
esse refinamento a suíte não consegue produzir o que a carteira mais usa.

---

### d. C22 × "Você foi selecionado" e lista VIP — REFINADA

| | |
|---|---|
| **Dado** | "Você foi selecionado (texto do fundador)" é o e-mail das 07h do 11.11 no Q4. Segmentação real por tag: "Lista VIP só com tag", `regras-de-copy-de-campanha.md`. Camada VIP definida em `segmentacao-e-freios.md` como "tag de quem clicou em confirmar presença" |
| **Fonte** | `04_Assuntos/Assunto - Confirmação de algo que já é da pessoa.md`; `05_Modelos_validados/segmentacao-e-freios.md` |

**Redação proposta:**

> **C22.** Proibida exclusividade **genérica**: "você foi escolhido",
> "seleto grupo", "acesso VIP" quando não há segmento por trás.
>
> **Permitido** quando a segmentação é real e nomeada: o envio vai para
> uma camada declarada (VIP, E30, E90) e o brief traz o campo
> `segmento`. "Você foi selecionado" para a tag `VIP-1111` é fato.

**Mudança no lint:** C22 só dispara quando `segmento` está ausente do
payload ou é a lista toda (`LT`).

**Recomendação: aprovar.** A casa já exige tag para lista VIP, então a
regra de negócio já existe. O lint só passa a enxergá-la.

---

### e. P09 × linha do Hormozi — REFINADA

| | |
|---|---|
| **Dado** | "Linha do Hormozi (2025)" é família de assunto validada, usada como **variação B do A/B** contra um assunto validado. A sequência do 11.11 de 2025 foi "o maior mês da carteira". A oferta do 11.11 está montada no modelo Hormozi |
| **Ressalva do próprio dado** | Resultado "sem número por assunto" |
| **Fonte** | `04_Assuntos/Assunto - Linha do Hormozi (2025).md`; `01_Estrategia/1.2 A oferta do 11.11 montada no modelo Hormozi.md` |

**Redação proposta:**

> **P09.** O tom de infoproduto continua proibido como **voz padrão** da
> loja: "meu contador disse que sou louco", "eu poderia cobrar", "presta
> atenção nisso".
>
> **Permitida a estrutura de oferta do Hormozi** (empilhar bônus,
> garantia nomeada, prazo) e a **linha de assunto que abre loop com
> número ou prazo**, exclusivamente como variação B de um A/B contra um
> assunto validado. Nunca como variação A, nunca sem teste.

**Mudança no lint:** as 8 frases de infoproduto do léxico continuam. Não
há mudança de código: o refinamento é de estrutura de oferta, que o lint
não lê.

**Recomendação: aprovar com a ressalva.** O dado é o mais fraco do
conjunto ("sem número por assunto"). Aprovar só a estrutura e o uso em
variação B, que é como a própria casa já usa.

---

### f. C45 e D13 × altura em px — REFINADA

| | |
|---|---|
| **Dado** | "E-mail longo demais (o 11h do 9.9 tinha **4.136 px**)" está na lista do que não funcionou. A técnica validada manda **2.000 a 3.200 px de altura** e "oferta, cupom, prazo e botão nos primeiros **500 px**" |
| **Fonte** | `08_Skill/SKILL...md:65`, `:174-179` |

O catálogo mede copy em palavras. A carteira mede peça em pixels. São
eixos diferentes e os dois importam: 80 palavras espalhadas em 4.000 px
é o mesmo defeito.

**Redação proposta:**

> **C45** mantém o teto de palavras (campanha 80, carrinho 60).
>
> **Novo D32, altura da peça.** Alvo de 2.000 a 3.200 px. Acima de 3.500
> px é achado A. Acima de 4.000 px é B, porque é o valor que a carteira
> mediu como fracasso.
>
> **Novo D33, primeiros 500 px.** Oferta, cupom, prazo e botão precisam
> caber na primeira tela de 500 px.

**Mudança no lint:** `lint_email.py` ganha estimativa de altura somando
`height` das imagens e altura de linha do texto vivo. É estimativa
declarada, não medição: o valor exato exige render.

**Recomendação: aprovar D32 e D33 como `revisar`**, não como B, até a
estimativa de altura ser validada contra 5 peças reais medidas no Figma.
Estimar altura de HTML sem render erra fácil, e um B errado trava entrega.

---

### g. C06 × contador — CONFIRMADA

| | |
|---|---|
| **Dado** | "Nada inventado: avaliação, estoque, **contador** e número só se forem reais da loja. Sem o dado, o bloco sai" |
| **Fonte** | `08_Skill/SKILL...md:16`, princípio 3 |

A regra interna e o C06 dizem exatamente a mesma coisa. **Aplicada, sem
mudança de texto.** O dado interno vira fonte adicional de C06 no
catálogo.

**Recomendação: nada a decidir.** Já aplicado.

---

### h. C34 × Title Case em inglês — CONFIRMADA

| | |
|---|---|
| **Dado** | Os assuntos validados da Blue Wolf são em inglês e usam Title Case: "Your coupon has been approved", "Your status has just changed" |
| **Fonte** | `04_Assuntos/` (várias), `09_Dados/...B.3` |

Coincide com a decisão D-005 já tomada: C34 vale só para pt-BR. Loja
inglesa pode usar Title Case. **Nada muda.**

**Recomendação: nada a decidir.** Já aplicado e coberto por teste.

---

### i. Layout neutro × Design Blue Wolf — REFINADA

| | |
|---|---|
| **Dado** | A Blue Wolf **não é preto e branco**. Cor primária `#29506D` (navy), secundária `#4588B9` (azul aço), mais paleta por momento com dourado, prata, amarelo, ciano e vinho |
| **Exceção interna** | "Aviso de sistema: sempre em fundo branco com texto preto. É o visual com os maiores cliques" (3,61% e 3,20%) |
| **Fonte** | `07_Design_Blue_Wolf/02_DESIGN_SYSTEM_BLUE_WOLF.md`, `03_PALETAS_POR_MOMENTO.md` |

**Correção à premissa da pergunta:** a Blue Wolf é navy e azul aço, com
9 paletas por momento. Há conflito real com o layout neutro, e ele não
se resolve dizendo que a marca é neutra.

Mas o conflito é menor do que parece, porque a regra do CLAUDE.md já
prevê a saída: cor da marca entra **quando o brief da loja exigir**. O
Design Blue Wolf é exatamente esse brief.

**Redação proposta:**

> O layout neutro é o **padrão de quem não tem ficha**. Loja com ficha
> aprovada em `marcas/<cliente>.md` usa a paleta da ficha, inclusive
> fundo colorido, quando a ficha declara.
>
> Duas coisas continuam valendo para toda loja, com ficha ou sem:
> 1. O agente **nunca escolhe** paleta. Ou está na ficha, ou é neutro.
> 2. **Aviso de sistema é sempre fundo branco e texto preto**, em
>    qualquer marca e em qualquer momento. É a exceção que a carteira
>    mediu como o visual de maior clique.

**Mudança no lint:** `regra_cores_marca` já aceita cores da ficha. Passa
a exigir que peça marcada `tipo: aviso-de-sistema` seja branco e preto,
mesmo com ficha.

**Recomendação: aprovar.** Sem isso a suíte não consegue produzir para a
Blue Wolf, que é a loja com mais dado na base.

---

## Varredura do catálogo

Regras sem conflito, verificadas contra os dados.

| Regra | Veredito | Dado |
|---|---|---|
| C01 travessão | CONFIRMADA | "Sem travessão", `regras-de-copy-de-campanha.md` |
| C02 número inventado | CONFIRMADA | "Número de prova só se for real da loja" |
| C04 idioma do cupom | CONFIRMADA | "Idioma certo" no checklist de agendamento |
| C07 meta-copy | SEM DADO INTERNO | |
| C10 antítese | SEM DADO INTERNO | |
| C11 tríade | SEM DADO INTERNO | |
| C12 a C19 | SEM DADO INTERNO | |
| C20 superlativo | CONFIRMADA (indireto) | Esquenta em tom de anúncio = 1 pedido |
| C21 vocabulário de IA | SEM DADO INTERNO | |
| C23 a C29 | SEM DADO INTERNO | |
| C32 a C33, C35 | SEM DADO INTERNO | |
| C40 assunto curto | SEM DADO INTERNO | A base não mede por comprimento |
| C41 preheader | CONFIRMADA | "O pré-cabeçalho completa o assunto com a oferta ou o prazo" |
| C42 oferta em texto vivo | CONFIRMADA | "Oferta na primeira tela", "Oferta em 3 segundos" |
| C43 CTA | CONFIRMADA | "Um botão principal" |
| C44 um CTA principal | CONFIRMADA | "Um botão principal por e-mail" |
| C46 condição da oferta | CONFIRMADA | "Prazo com data e hora", "Cupom testado e com limite real" |
| C47 fallback | SEM DADO INTERNO | |
| D01 a D05 | CONFIRMADA (com i) | Sujeito à ficha da marca |
| D17 alt e texto vivo | CONFIRMADA | "Oferta na primeira tela" |
| D18 recursos que quebram | SEM DADO INTERNO | |
| D19 dark mode | SEM DADO INTERNO | |
| D21 a D31 | SEM DADO INTERNO | Entraram como `revisar` |
| P01 contexto antes de gerar | CONFIRMADA | "Toda data tem contexto" |
| P02 não inventar | CONFIRMADA | Princípio 3 |
| P03 variantes divergentes | CONFIRMADA | A/B com A conservador e B equilibrado |
| P04 a P08 | SEM DADO INTERNO | |

## Regras novas que os dados pedem

Não existem no catálogo e a carteira sustenta. Propostas, não aplicadas.

| ID | Regra | Dado |
|---|---|---|
| **N01** | Extensão de oferta não entra no calendário | "virou semana", "VIP Week" = 0,49 e 0,52. `extensao-lista-toda` = 0,52, fora do calendário |
| **N02** | Evento colado em outro reprova | VIP Day logo depois do 9.9 = 0,38 a 0,50 |
| **N03** | Segmento ampliado sem critério reprova | Os 5,2 mil a mais não abriram; por mil caiu de US$ 55 para US$ 22 |
| **N04** | Promessa repetida na antecipação reprova | "na lista", "prometi", "garantido" = 0,39 a 0,52 |
| **N05** | Assunto não repete a promessa do anterior | Regra de assunto do SKILL BFCM |
| **N06** | 80/10/10 no calendário | Plano só aprovado com validado ≥ 80% |

**Recomendação:** N01 a N04 viram regras de `email-calendario` e
`email-flows`, severidade A. N05 vira regra de `email-copy` que só o
revisor consegue ver (precisa da sequência). N06 é gate de calendário.
