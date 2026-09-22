# Vícios registrados no vault (V01 a V60)

Mineração do vault pedida no §10.1 de `pesquisa-vicios-ia-email.md`. Fonte:
`vault/aprendizados/` inteiro, as seções "quando não usar", "ressalvas
conhecidas" e "o que varia por loja" de `vault/estruturas/`, e as
`proibicoes` e "o que este e-mail NÃO deve fazer" de `vault/intencoes/`.
Lido em 22/09/2026. **Nada foi escrito no vault.**

Regra de coleta: só entra o que está escrito na nota. Onde a nota não diz,
a linha traz `n/d`, não interpretação.

Convenções herdadas do catálogo da pesquisa:
severidade **B** bloqueia entrega, **A** alta (corrigir), **M** média
(aceitável se isolado); detecção **R** regex no lint, **H** heurística,
**J** julgamento do revisor.

A coluna **coincide com** aponta a regra já existente em
`pesquisa-vicios-ia-email.md` (C01 a C47, D01 a D20, P01 a P09) ou outro
V que diz a mesma coisa. Onde ela está preenchida, **o lint deve ter uma
regra só**, e o V serve como evidência interna e caso de teste, não como
segunda regra.

---

## 1. Aprendizados globais (`vault/aprendizados/_global/`)

| ID | Vício | Sev. | Det. | Ruim | Bom | Coincide com | Fonte |
|---|---|---|---|---|---|---|---|
| V01 | Alegação (diferencial, garantia, item riscado numa comparação) sem lastro operacional verificável | B | J | listar "frete rápido" numa varredura quando a entrega demora | cruzar cada item com o que a loja entrega e **remover** o que não tem lastro, nunca suavizar | C02, C06 | `vault/aprendizados/_global/cada-alegacao-e-uma-promessa-operacional.md` |
| V02 | Código, valor ou prazo do incentivo existindo só dentro da imagem | B | R+H | cupom entregue no hero, que é imagem: com imagens bloqueadas o código some | duplicar código, valor e prazo em texto real, ou descartar o bloco | C42, D17 | `vault/aprendizados/_global/incentivo-precisa-existir-em-texto.md` |
| V03 | Bloco defensivo (comparação, FAQ, garantia) posicionado antes de a dúvida existir | A | J | abrir carrinho abandonado com FAQ; comparar contra a categoria no toque 1 | perguntar "neste toque o leitor já tem essa dúvida?" antes de posicionar | P08 (ordem intenção → estrutura) | `vault/aprendizados/_global/posicao-muda-o-efeito-do-dispositivo.md` |
| V04 | Toque de encerramento com o mesmo formato dos sete anteriores | M | J | oitavo e-mail desenhado igual aos outros, descartado pelo padrão visual antes da primeira palavra | escolher o formato do último e-mail **contra** o padrão que o flow criou | n/d (novo) | `vault/aprendizados/_global/quebra-de-formato-atravessa-a-cegueira.md` |
| V05 | Remoção de risco no rodapé em compra de ticket médio para cima | M | J | garantia depois do preço, fora do campo de visão da decisão | garantia antes da vitrine quando o ticket e o medo de qualidade pedem | n/d (novo) | `vault/aprendizados/_global/remocao-de-risco-escala-com-o-ticket.md` |
| V06 | Títulos que não carregam o argumento sozinhos (falha o teste de escaneabilidade) | A | J | lista cujo sentido só aparece lendo o corpo dos itens | título de item conta a história para quem não parou | C43 (parcial: CTA), F5 | `vault/aprendizados/_global/titulos-precisam-carregar-o-argumento.md` |
| V07 | Itens de uma varredura com naturezas repetidas | M | H | cinco variações de "qualidade" | uma trava de natureza diferente por item | n/d (novo) | `vault/aprendizados/_global/titulos-precisam-carregar-o-argumento.md` (corolário) |
| V08 | Vários CTAs disputando com peso visual igual | A | H | três CTAs genéricos mais um botão por produto na grade | um CTA dominante; os outros recuam por hierarquia, não por posição | C44 | `vault/aprendizados/_global/um-cta-dominante-em-email-curto.md` |

## 2. Aprendizados de welcome (`vault/aprendizados/welcome/`)

| ID | Vício | Sev. | Det. | Ruim | Bom | Coincide com | Fonte |
|---|---|---|---|---|---|---|---|
| V09 | Cortar prova social sem que ela exista num e-mail anterior e sem assumir o risco de não abertura | M | J | e-mail com cinco alegações da própria marca e nenhuma voz externa | uma linha de terceiro, ou prova distribuída (avaliação nos cards) | n/d (novo) | `vault/aprendizados/welcome/ausencia-de-prova-social-assume-abertura.md` |
| V10 | Dois e-mails seguidos sem voz externa | A | H | toques 2 e 3 sem depoimento direto | limite de dois; no e-mail de convicção, prova direta | n/d (novo) | idem |
| V11 | Prova social parafraseada pela própria marca contada como prova | A | J | "Thousands of pairs shipped... feedback is about durability" | citação atribuída a pessoa | C02 (autoridade emprestada) | idem |
| V12 | Gastar o depoimento que espelha o cético no toque de menor abertura | M | J | o "I was skeptical..." aparecendo no toque 4 | o depoimento vai no toque em que aquele estado mental é dominante | n/d (novo) | idem |
| V13 | Dois e-mails consecutivos citando o mesmo prazo com intervalo medido em dias | B | H | #6 e #7 com a mesma hora, separados por dias: renova um prazo que morreu | delay em horas, ou o segundo e-mail não existe | C06 | `vault/aprendizados/welcome/cadencia-decide-fechamento-ou-farsa.md` |
| V14 | Repetir a oferta sem mudar o papel dela no argumento | M | H | cupom quatro vezes na mesma peça com a mesma função | duas ocorrências, com papéis distintos (entrega e fechamento) | n/d (novo) | `vault/aprendizados/welcome/cupom-repetido-precisa-de-papel.md` |
| V15 | Bloco de argumentação longo antes do bloco de prazo, em e-mail de decisão | M | H | varredura de 5 razões antes do deadline | acima de 4 razões: cortar a lista ou subir o prazo | C45 | `vault/aprendizados/welcome/deadline-antes-do-argumento.md` |
| V16 | Prazo declarado no e-mail e não cumprido no ESP | B | J | #2 diz "today, 11:59 p.m." e o #3 chega com o mesmo cupom vivo, sem uma palavra | prazo cumprido, ou o toque seguinte reconhece ("reativamos seu código") | C06 | `vault/aprendizados/welcome/deadline-falso-queima-o-proximo.md` |
| V17 | Mesmo depoente em e-mails diferentes do mesmo flow com falas diferentes | A | H | David M. repetindo do toque 1 com outro texto | pessoas distintas por e-mail em produção | C02 | `vault/aprendizados/welcome/depoimento-nao-repete-pessoa.md` |
| V18 | Extensão de prazo sem as quatro condições simultâneas (explícita, única, final, última) | B | J | "seu código ainda funciona!" | admitir que venceu, nomear a exceção, dar definitividade, só no toque de encerramento | C06 | `vault/aprendizados/welcome/extensao-declarada-quatro-condicoes.md` |
| V19 | Número de escassez sem mecanismo de backing | B | J+H | "412 usaram", "restam 16" como texto fixo | cap real, código único por contato, contagem vinda de dado; sem isso a estrutura é descartada, não adaptada | C02 | `vault/aprendizados/welcome/numeros-de-escassez-precisam-de-backing.md` |
| V20 | Repetir número perecível no segundo tempo do fechamento | M | H | repetir "restam 16" horas depois | o segundo e-mail carrega só o que continua verdadeiro (a hora) | n/d (novo) | idem (corolário) |
| V21 | Prazo da extensão sem hora, depois de prazos com hora | M | R+H | "one more day" depois de dois e-mails cravando 11:59 PM | extensão com hora, no mesmo formato dos prazos anteriores | C46 (condição da oferta) | `vault/aprendizados/welcome/prazo-vago-enfraquece-a-extensao.md` |
| V22 | Prova de terceiro depois do último CTA, quando ela fecha o arco da objeção | M | H | depoimento na posição 7, depois de todos os CTAs | prova colada no bloco de compromisso ou na grade | n/d (novo) | `vault/aprendizados/welcome/prova-de-terceiro-antes-do-cta.md` |
| V23 | Subir prova social por padrão, onde a objeção dominante não é desconfiança | M | J | bloco de reviews promovido num e-mail de preço ou adequação | prova onde a objeção está ativa; ela não é universalmente aditiva | n/d (novo) | idem (refinamento) |
| V24 | E-mail de profundidade sem saída rápida de compra no primeiro terço | M | H | primeiro CTA de compra depois de ~7 parágrafos | atalho de compra cedo, sem tirar a profundidade | n/d (novo) | `vault/aprendizados/welcome/saida-rapida-no-primeiro-terco.md` |

## 3. Estruturas: "quando não usar", ressalvas e artefatos (`vault/estruturas/welcome/`)

| ID | Vício | Sev. | Det. | Ruim | Bom | Coincide com | Fonte |
|---|---|---|---|---|---|---|---|
| V25 | Estrutura monotemática de produto usada quando a objeção dominante é do canal | M | J | inspeção antecipada numa loja cuja dúvida é legitimidade ou falsificação | comparação contra a categoria | n/d (novo) | `avelmore-inspecao-antecipada.md` ("Quando usar / quando não usar") |
| V26 | Estrutura que depende de incentivo aplicada em loja sem cupom ativo | A | H | hero e bloco de fechamento perdem o objeto; a estrutura desmonta | declarar a lacuna e escolher outra estrutura | P01, P02 | idem |
| V27 | Estrutura que depende de depoimento real aplicada sem depoimento com nome | A | H | arco sem confirmação, ou depoimento preenchido no chute | escolher estrutura que não dependa de prova | C02, P02 | idem |
| V28 | Varredura de objeções onde a objeção é uma, conhecida e profunda | M | J | varrer cinco travas quando a dúvida é uma: dilui | aprofundar (mecanismo e origem) | n/d (novo) | `avelmore-deadline-objecao.md` |
| V29 | Hora fechada em toque que não encerra o ciclo da oferta | B | R | "hoje, 23:59" no segundo toque | "por tempo limitado" nos intermediários; hora só no fechamento | C06, V16 | `avelmore-deadline-objecao.md` (regra dura de posição) e `intencoes/welcome/_flow.md` (regra 3) |
| V30 | Comparação contra a categoria em toque inicial | A | J | comparar antes de a dúvida amadurecer: planta a dúvida que queria curar | toque tardio, depois dos registros gastos | V03 | `medicube-comparacao-categoria.md` ("Quando NÃO usar") |
| V31 | Estrutura de escassez em loja sem como sustentar os números | B | J | contagem decorativa | descartar a estrutura | V19, C02 | `medicube-escassez-com-prova-de-demanda.md` ("Quando NÃO usar") |
| V32 | Estrutura de fechamento cujo toque seguinte não honra a expiração | B | J | prazo anunciado e cupom vivo depois | flow que honra, ou não fixa prazo | V16, C06 | idem |
| V33 | Última batida com delay em dias desde o e-mail de prazo | B | H | terceiro deadline queimado do mesmo código | mesmo dia, medido em horas | V13 | `medicube-ultima-batida.md` ("Quando NÃO usar") |
| V34 | Segunda extensão no mesmo flow, ou extensão fora do toque de encerramento | B | H | duas cortesias: todos os prazos da marca viram decorativos retroativamente | uma por flow, no último toque | V18 | `carta-plain-text-extensao.md` ("Quando NÃO usar") |
| V35 | Artefato de montagem vazando na peça: copy de outro nicho, rodapé de outra marca | A | J | "start your style journey" num e-mail de skincare; rodapé Avelmore num e-mail Medicube | copy e rodapé da loja que envia | C21 (parcial: "journey") | `medicube-escassez-com-prova-de-demanda.md` e `medicube-ultima-batida.md` (notas "Artefatos do template compartilhado") |
| V36 | Placeholder literal entregue na peça | B | R | assinatura "The [Brand] Team" | assinatura da loja, ou bloqueio na entrega | P04 | `carta-plain-text-extensao.md` ("Pontas de placeholder") |
| V37 | Typo carregado da referência para a peça | A | R | "reply to his email" onde cabia "this" | revisão ortográfica no gate de entrega | n/d (novo) | idem |

## 4. Intenções: proibições por toque (`vault/intencoes/`)

As `proibicoes` do frontmatter e o "o que este e-mail NÃO deve fazer" do
corpo dizem a mesma coisa nas duas camadas. A linha cita a proibição, não
a prosa.

| ID | Vício | Sev. | Det. | Ruim | Bom | Coincide com | Fonte |
|---|---|---|---|---|---|---|---|
| V38 | Urgência artificial no primeiro toque | B | J | pressão no welcome 1 | pressão só a partir do toque que a pede | C06 | `vault/intencoes/welcome/welcome-1.md` |
| V39 | Pedido de engajamento paralelo (rede social, preferências) junto do pedido principal | M | H | "e siga a gente no Instagram" no welcome 1 | um pedido por e-mail | C44, V08 | `welcome-1.md` |
| V40 | História longa da fundação fora do toque que a comporta | M | J | origem da marca no toque 1 | o toque 3 é o da profundidade | C05 (parcial), C45 | `welcome-1.md` |
| V41 | Condição nova no incentivo prometido | B | J | cupom entregue com regra que o opt-in não tinha | incentivo inteiro, sem fricção, no toque 1 | n/d (novo) | `welcome-1.md` e `intencoes/welcome/_flow.md` (regra 1) |
| V42 | Esgotar os argumentos num toque de objeção única | M | H | cinco argumentos onde `n_objecoes: [1, 1]` | uma objeção, bem atacada | C45 | `welcome-1.md`, `welcome-3.md` |
| V43 | Repetir a tese ou o registro do toque anterior | A | J | mesmo argumento com outras palavras | trocar o tipo de argumento, não as palavras | n/d (novo) | `welcome-2.md`, `welcome-3.md`, `welcome-4.md`, `welcome-5.md`, `welcome-7.md` |
| V44 | Aumentar o incentivo, ou sinalizar que ele pode melhorar | B | J | "fica atento que vem coisa melhor" | valor fixo do começo ao fim: insistir não pode pagar | n/d (novo) | `welcome-2.md`, `welcome-3.md`, `_flow.md` (regra 2) |
| V45 | Depender de prova social no toque em que ela está vetada | M | H | bloco de reviews no toque 2, cujo assunto é decisão | prova distribuída, ou nenhuma | n/d (novo) | `welcome-2.md` (`aliviadores_vetados`) |
| V46 | Argumentar em voz de marca no toque de terceiros | A | J | a marca voltando a se elogiar no toque 4 | o texto substantivo é de clientes | n/d (novo) | `welcome-4.md` |
| V47 | Empurrar catálogo no toque em que falta confiança, não opção | M | H | grade de produtos no toque 4 | sem vitrine | n/d (novo) | `welcome-4.md` |
| V48 | Nomear concorrente específico | B | J | citar a loja rival pelo nome | comparar contra a categoria | n/d (novo; risco jurídico declarado na nota) | `welcome-5.md` |
| V49 | Superlativo vazio no lugar de compromisso | A | R | "somos os melhores" | compromisso contra medo nomeado | C20 | `welcome-5.md`, `abandoned_cart-4.md` |
| V50 | Reargumentar ou reabrir deliberação no toque de fechamento | A | H | prova, catálogo ou história no e-mail do prazo | só o tempo | C45 | `welcome-6.md`, `welcome-7.md`, `welcome-8.md` |
| V51 | Conteúdo extra no sino | A | H | argumento, prova ou vitrine no toque 7 | uma informação: que horas são | C45 | `welcome-7.md` |
| V52 | Fingir que o prazo não venceu | B | R | "seu código ainda funciona" | admitir que venceu | V18, C06 | `welcome-8.md` |
| V53 | Pedir desculpas pelo prazo | M | J | "desculpa a insistência" | cortesia de quem podia, não recuo | n/d (novo) | `welcome-8.md` |
| V54 | Aparato visual de campanha no toque de carta | A | J | hero, grade e botões no e-mail que existe para parecer mensagem | texto simples, link, assinatura | V04 | `welcome-8.md` |
| V55 | Desconto, ou sinal de que virá desconto, antes do toque que o carrega | A | J | "fique de olho, vem desconto" nos toques 1 a 4 do carrinho | incentivo entra uma vez, no toque 5 | n/d (novo) | `abandoned_cart-1.md` a `abandoned_cart-4.md` (as quatro repetem) |
| V56 | Bloco dinâmico ou botão abaixo da dobra em e-mail de abandono | A | H | item recuperado escondido no meio da peça | item e botão no topo | n/d (novo) | `abandoned_cart-1.md` |
| V57 | FAQ, garantia ou bloco defensivo no primeiro toque de carrinho | A | J | abrir com FAQ | guardar para o toque 3 | V03 | `abandoned_cart-1.md` |
| V58 | Lista longa de prova no toque de texto pessoal | M | H | seis pontos de prova numa mensagem que imita e-mail de pessoa | dois ou três pontos | C45 | `abandoned_cart-2.md` |
| V59 | Varrer objeções no toque de objeção única do carrinho | M | H | cobrir tudo no toque 3 | uma trava, cercada de ângulos diferentes | V42 | `abandoned_cart-3.md` |
| V60 | Reapresentar a prova ou o argumento do toque anterior no carrinho | M | J | repetir os pontos do toque 2 | mudar de registro | V43 | `abandoned_cart-3.md`, `abandoned_cart-4.md` |

**Resumo:** 60 linhas. 36 com coincidência declarada (regra já existente no
catálogo C/D/P ou em outro V), 24 sem coincidência: material novo que o
vault traz e a pesquisa externa não tinha. Por severidade: 17 B, 20 A,
23 M.

As 24 sem coincidência são a contribuição própria do vault, e quase todas
são de **posição e sequência**, não de vocabulário: V04, V05, V07, V09,
V10, V12, V14, V20, V22, V23, V24, V25, V28, V37, V41, V43, V44, V45, V46,
V47, V48, V53, V55, V56. A pesquisa externa cobre bem o que não se escreve;
o vault cobre onde cada coisa entra no flow. Um lint de copy não alcança a
maioria delas: são regra de estrutura, e o lugar delas é o gate do
Estruturador, não o regex.

---

## 5. Onde o vault contradiz uma regra fixa da Convertfy

Não são vícios; são conflitos de fonte que precisam de decisão humana.
Registrados aqui porque um lint construído sem eles vai reprovar o próprio
vault, ou passar o que a casa proíbe.

1. **Title Case e emoji no assunto.**
   `vault/componentes/doutrina/subject-line-e-preview.md` reproduz o
   framework de terceiro: "2-5 words in Length · Title Case, Like This
   Sentence · Builds curiosity · Ends with 1-2 emojis (optional)", com os
   exemplos "A Taste of Sunshine ☀️" e "Myth. Busted. 👀". Isso colide com
   C34 (Title Case é vício em pt-BR) e tensiona C31 (emoji). A própria nota
   ressalva que são regras de forma em inglês e que a pesquisa da loja
   precede a doutrina. **Decisão pendente:** o lint aplica C34 sempre em
   pt-BR e ignora a doutrina, ou a doutrina vale para assunto em inglês?
2. **Travessão na prosa das notas.** Várias notas de variante e de
   estrutura usam travessão no corpo. Isso é prosa de vault lida por LLM,
   não copy entregue, e não deve entrar no lint de copy. Mas o redator que
   lê o vault inteiro aprende o hábito pelo exemplo. O lint roda na saída,
   não na fonte; a mitigação é `shared/anti-vicios-copy.md`, não editar o
   vault.
3. **Medição por abertura.** A mesma nota de doutrina registra a
   contradição interna da fonte ("track open rates" contra "less about
   opens"). O repo mede por receita e por reclamação, conforme
   `evidencias-publicadas.md`.

---

## 6. Relatório de contaminação da copy citada em var2

### 6.1 Caminho usado

**Os dois.** A análise manual de C10 a C26 foi feita primeiro, quando
`scripts/` ainda tinha só `setup.sh`. `scripts/lint_copy.py` apareceu no
meio desta tarefa (está sendo escrito em paralelo), e aí o corpus foi
passado por ele. Os dois resultados estão abaixo, e a divergência entre
eles é o achado mais útil desta seção.

**Como o linter foi rodado.** Ele espera **um e-mail** (`assunto`,
`preheader`, `blocos`, `ctas`, `alts`), e o corpus é uma lista de trechos
soltos. O corpus foi agrupado por nota var2 e por idioma, os trechos de
`campo: cta` foram para `ctas` e o resto para `blocos`:

```python
# agrupa docs/pesquisa/vault-copy-extraida.json por (nota, idioma) e chama
# python3 scripts/lint_copy.py --json  para cada grupo
```

Rodadas: 11 (8 notas, duas delas com trechos nos dois idiomas). Saída
bruta: **40 violações**. Dessas, **16 são ruído do formato**, não da copy:
`C41` (preheader vazio) 12 vezes, `C42` (oferta só na imagem) 2, `C46`
(condição da oferta ausente) 2. Um fragmento não tem preheader nem
condição; quem tem é o e-mail. Regras dependentes de peça inteira (C40,
C41, C42, C44, C45, C46, C47, C03, C18) foram suprimidas nesta leitura.
Restam **24 violações reais**.

### 6.2 O corpus

`docs/pesquisa/vault-copy-extraida.json`: **59 trechos** de copy literal
citados nas 8 notas var2. 49 `bloco`, 10 `cta`. 36 em inglês, 23 em pt-BR.
Por nota: medicube-comparação-categoria 17, medicube-escassez 10,
avelmore-mecanismo-e-origem 9, carta-plain-text-extensao 8,
medicube-última-batida 6, avelmore-prova-social-cirurgica 5,
avelmore-deadline-objecao 3, avelmore-inspecao-antecipada 1.

Critério de extração, para quem for auditar:

- Entrou o que a nota cita entre aspas ou em itálico **como texto da peça**
  (headline, item de lista, depoimento, rótulo, código, CTA).
- Ficou de fora a prosa da nota: glosa do autor ("existe um lugar real"),
  descrição da objeção-alvo ("parece bom na foto e decepciona na mão") e
  aspas de ênfase ("por quê", "qual", "como").
- Parte das notas traduz para pt-BR copy que na peça é inglesa (os 12 itens
  da tabela de comparação da Medicube, os três depoimentos do toque 6, a
  paráfrase da carta do toque 8). Estão no JSON com `idioma: pt-BR` porque é
  assim que a nota as apresenta, e é assim que o redator as vai copiar.
  **Ressalva:** o lint de idioma (C04) não deve concluir nada sobre a loja a
  partir dessas entradas.
- `avelmore-inspecao-antecipada` quase não cita copy: descreve dispositivos.
  Uma entrada só não é amostra.

### 6.3 O que o `lint_copy.py` pegou

24 violações reais, por nota. `C02` aparece muito porque o corpus roda sem
`brief_numbers`: todo número fica órfão por construção. Separei os dois
tipos, porque só um é problema de copy.

| Nota | Regra | Sev. | Trecho | Leitura |
|---|---|---|---|---|
| medicube-escassez | **C01** | B | "$35 mais barato que o site oficial — mesma caixa, mesmos selos" | Travessão. O único B que não depende de contexto |
| medicube-escassez | **C21** | A | "start your style journey" | Vocabulário de IA ("journey") |
| medicube-última-batida | **C21** | A | "start your style journey with a discount" | Idem |
| avelmore-prova-social | **C15** | M | "STILL WANT 10% OFF?" | Pergunta retórica |
| medicube-escassez | **C02** | B | "412 women already used WELCOME10 this week", "only 16 codes remaining" | Número de escassez. Casa com V19: só com backing |
| avelmore-prova-social | **C02** | B | "4.8/5 from 3,847 verified reviews" | Agregado. Modelo de formato, nunca de valor |
| medicube-escassez | **C02** | B | "no outro site, zero tracking por 3 semanas; aqui, tracking em 24h" | Número dentro de depoimento |
| avelmore-deadline-objecao, avelmore-mecanismo, medicube-escassez, medicube-última-batida | **C02** | B | "hoje, 23:59", "today, 11:59 p.m.", "LAST 12 HOURS...", "THE CODE WELCOME10 EXPIRES AT 11:59 PM TODAY", "your exclusive discount expires today at 11:59 PM" | **Falso positivo de contexto:** é hora de prazo, não estatística. Com `brief_numbers` preenchido pela ficha da marca, some |
| medicube-escassez | **C35** | M | "LAST 12 HOURS FOR YOUR DISCOUNT", "THE CODE WELCOME10 EXPIRES AT 11:59 PM TODAY" | **Falso positivo:** caixa alta em headline é legítima (§8 da pesquisa). O linter não sabe que o trecho é headline |
| avelmore-mecanismo, medicube-comparação, medicube-escassez | **C43** | M | "READ THE FULL STORY", "ENJOY DISCOUNT", "SECURE MY 10% OFF" | Discutível: os três são verbo mais objeto. "READ THE FULL STORY" de fato não é CTA de compra, e a própria nota diz que isso é deliberado (tira o e-mail do funil) |

### 6.4 O que o linter não pegou e a leitura manual pegou

Cinco itens. Cada um é uma regra a apertar, e foi conferido rodando o
trecho isolado pelo linter (nenhum deles dispara nada).

| Trecho | ID | Por que escapou | O que fazer no `lint_copy.py` |
|---|---|---|---|
| "We're not your average Korean skincare store" | **C10** | A regex do §9.1 cobre `not (just\|only)` e `it'?s not`; "not your average" não casa | acrescentar `not your (average\|typical\|usual\|ordinary)` e, em pt-BR, `n[ãa]o (é\|e) (mais )?um[a]? \w+ qualquer` |
| "Promoções generosas" | **C20** | "generoso" não está no léxico de superlativo | acrescentar ao `shared/lexico/pt-br.txt`: generoso, imbatível, exclusivo (quando sem objeto), especial |
| "before it's gone forever" | **C20** | "forever" não está no léxico en | acrescentar: forever, ever, once-in-a-lifetime |
| "your exclusive discount", "Since you're new to the club" | **C22** | exclusividade genérica em inglês sem gancho no léxico | acrescentar: exclusive, VIP, members only, insider, "the club"; e deixar a ficha da marca desligar a regra quando o clube existir de verdade |
| "What sets each pair apart", "nem planejava comprar... why not" | **C16**, **C13** | fórmula de abertura e reticências de suspense | C16 precisa de lista de fórmulas em inglês ("what sets ... apart", "when it comes to", "in today's"); C13 precisa pegar `\.\.\.` e `…` no meio de frase, não só no fim |

Duas observações de implementação, para quem mantém o linter:

1. O docstring documenta `blocos: [{"texto": ..., "papel": "body"}]`, mas
   `papel` não é lido em lugar nenhum do arquivo. Sem ele, **C35** e
   **C43** não têm como distinguir headline de parágrafo e CTA de compra de
   CTA de conteúdo, e vão gerar falso positivo em toda peça.
2. **C02** só é utilizável com `brief_numbers` vindo de `marcas/<loja>.md`.
   O campo já existe no template de marca. Sem ele, C02 bloqueia qualquer
   e-mail que tenha hora de prazo.

### 6.5 Violações pela leitura manual (C10 a C26)

| Nota | Trecho citado | ID violado | Leitura |
|---|---|---|---|
| medicube-comparação-categoria | "We're not your average Korean skincare store" | **C10** (A) | Antítese de efeito na headline que carrega o e-mail inteiro. A regex proposta no §9.1 (`not (just\|only)`, `it'?s not`) **não pega** "not your average": ampliar para `not your (average\|typical\|usual)` e `n[ãa]o (é\|e) mais um`. |
| medicube-comparação-categoria | "Promoções generosas" | **C20** (A) | Superlativo sem objeto, e primeira linha da coluna que sustenta o argumento. Trocar por mecânica ("10% na primeira compra") resolve as duas coisas. |
| medicube-escassez-com-prova-de-demanda | "start your style journey" | **C21** (A) | "journey" está na lista de vocabulário de IA. A própria nota marca a frase como artefato de montagem (é copy de moda num e-mail de skincare): V35 e C21 batem no mesmo trecho. |
| medicube-última-batida | "start your style journey with a discount" | **C21** (A) | Idem, agravado: é o corpo do único bloco do e-mail. |
| medicube-última-batida | "your exclusive discount" | **C22** (A) | Exclusividade genérica. Contestável: aqui existe cupom real e a nota defende o enquadramento de posse ("não perca o que já é seu"). Fica como alta com ressalva; o desempate é a ficha da marca. |
| avelmore-prova-social-cirurgica | "STILL WANT 10% OFF?" | **C15** (M) | Pergunta retórica de abertura: é a headline do hero, primeira linha da peça. A nota a chama de "reabertura em uma pergunta", ou seja, o dispositivo é intencional. Se a casa quiser manter, C15 precisa de exceção nomeada para o toque de reabertura. |
| avelmore-mecanismo-e-origem | "What sets each pair apart" | **C16** (A) | Fórmula de abertura de marketing, da mesma família de "Quando se trata de…". Detecção J, não R: depende de ler que é o título do bloco. |
| carta-plain-text-extensao | "before it's gone forever" | **C20** (A) | Intensidade no lugar de fato ("forever" contra um prazo de um dia). Ao lado de "one more day" sem hora, ainda cai em V21. |
| carta-plain-text-extensao | "Since you're new to the club" | **C22** (M) | Exclusividade genérica quando não existe clube. Se a loja tem programa real, não é vício. |
| medicube-escassez-com-prova-de-demanda | "nem planejava comprar... why not" | **C13** (M) | Reticências de suspense dentro do depoimento, mais mistura de idioma no mesmo trecho. Como depoimento real citado, a reticência pode ser corte legítimo; o que não se sustenta é entregar assim numa peça pt-BR. |

**Fora da faixa C10 a C26, mas encontrado no mesmo corpus e mais caro:**

| Nota | Trecho citado | ID | Leitura |
|---|---|---|---|
| medicube-escassez-com-prova-de-demanda | "$35 mais barato que o site oficial — mesma caixa, mesmos selos" | **C01** (B) | Travessão em copy citada como referência. Preservado literalmente aqui porque é evidência. É o item que mais importa: um redator que copia este depoimento como modelo reproduz o travessão, e o lint só pega depois. |
| medicube-escassez-com-prova-de-demanda | "412 women already used WELCOME10 this week", "only 16 codes remaining" | **C02** (B) + V19 | Números que só podem existir com backing. O vault já trata isso como restrição dura. |
| avelmore-prova-social-cirurgica | "4.8/5 from 3,847 verified reviews" | **C02** (B) | Agregado numérico da amostra. Serve de modelo de formato, nunca de valor. |
| carta-plain-text-extensao | "The [Brand] Team" | **P04** / V36 | Placeholder literal. |
| carta-plain-text-extensao | "reply to his email" | V37 | Typo registrado na própria nota. |

**Limpos e úteis como modelo:** os 9 CTAs distintos do corpus
("READ THE FULL STORY", "APPLY MY DISCOUNT", "SHOP WITH WELCOME10",
"SHOP 10% OFF", "ENJOY DISCOUNT", "GET 10% OFF", "SECURE MY 10% OFF",
"CLAIM MY DISCOUNT", "SHOP NOW") são verbo mais objeto e batem com o corpus
humano do §2.1 da pesquisa, onde shop, claim e explore dominam. O linter
marcou três deles em C43, e discordo em dois: "ENJOY DISCOUNT" e
"SECURE MY 10% OFF" são verbo mais objeto; "READ THE FULL STORY" de fato
não leva à compra, e a nota var2 diz que isso é deliberado. É o tipo de
decisão que precisa do campo `papel`, não de mais regex.

Também passam, por serem mecânica e condição sem adjetivo:
"escolha o seu com o desconto", "por tempo limitado", "hoje, 23:59",
"THE CODE WELCOME10 EXPIRES AT 11:59 PM TODAY" e
"sem exceção para itens de Final Sale". Caixa alta em headline e rótulo não
conta como vício (§8 da pesquisa), embora o linter a marque (C35).

### 6.6 `lint_status` proposto por nota var2 (proposta, não aplicada)

Campo sugerido no §2.3 da pesquisa. **Não editei o vault.** Se a Convertfy
aceitar, a edição acontece no Obsidian, uma linha no frontmatter de cada
nota:

| Nota var2 | `lint_status` proposto | Motivo |
|---|---|---|
| `vault/estruturas/welcome/avelmore-inspecao-antecipada.md` | `limpa` | 1 trecho citado, zero violação nos dois caminhos. Amostra pequena demais para servir de modelo de copy. |
| `vault/estruturas/welcome/avelmore-deadline-objecao.md` | `limpa` | 3 trechos, todos mecânica ou condição. O único C02 do linter é a hora do prazo, não estatística. |
| `vault/estruturas/welcome/avelmore-mecanismo-e-origem.md` | `contaminada` | C16 em "What sets each pair apart". Única violação, de julgamento. |
| `vault/estruturas/welcome/avelmore-prova-social-cirurgica.md` | `contaminada` | C15 na headline, C02 no agregado. |
| `vault/estruturas/welcome/carta-plain-text-extensao.md` | `contaminada` | C20, C22, placeholder literal (P04) e typo. |
| `vault/estruturas/welcome/medicube-comparacao-categoria.md` | `contaminada` | C10 na headline principal, C20 na tabela. |
| `vault/estruturas/welcome/medicube-escassez-com-prova-de-demanda.md` | `contaminada` | C01 (travessão), C21, C13, C02. A mais contaminada do conjunto. |
| `vault/estruturas/welcome/medicube-ultima-batida.md` | `contaminada` | C21 e C22 no único bloco do e-mail. |

**Placar: 2 limpas, 6 contaminadas**, e os dois caminhos concordam nas 8
notas. Em 59 trechos: o linter devolveu 24 violações reais (das quais 7 são
hora de prazo lida como número órfão e 2 são caixa alta em headline), e a
leitura manual achou 10 violações de C10 a C26, 5 delas que o linter não
pega hoje. Nenhuma nota mudou de veredito por causa do linter: o que ele
acrescentou foi precisão sobre C01, C02 e C21, e a lista de buracos da §6.4.

**Como usar o campo, quando existir:** `contaminada` não invalida a
estrutura. As 8 continuam boas como estrutura (ordem, papel e dispositivo
das seções, que é o que o Estruturador lê). O campo serve para a fase de
copy: de nota `contaminada`, o redator copia a **anatomia**, nunca a
**frase**. Isso é o P07 da pesquisa ("copiar vício do exemplo") virando
gate.

---

## 7. O que não foi coberto e deveria ser

1. **As 75 notas de variante têm copy literal de exemplo e não entraram
   neste corpus.** O escopo pedido era var2. Mas
   `## Orientações de copy para a IA` traz exemplos citados como literais
   ("Recommended by Vets", "Aprovado por dermatologistas", "Dr. Carin
   Beene"), e é essa a camada que o redator lê na hora de preencher o
   schema. **TODO:** segunda extração, `vault-copy-variantes.json`, mesmo
   formato, com `campo` novo para `exemplo_de_slot`.
2. **`vault/componentes/doutrina/` não entrou nas linhas V.** As oito notas
   de doutrina ensinam critério de copy (o que evitar, subject line,
   varredura contra leitura, botão e clique) e, pelo `_PADRAO-DO-VAULT`
   A10, nunca contêm regra dura. Puxei delas só os conflitos da §5.
   **TODO:** decidir se doutrina vira linha V (com severidade M, detecção J)
   ou fica de fora por não ser correção observada.
3. **`vault/componentes/convivencia/` (6 notas) e `lacunas/` (24 notas)**
   descrevem restrição entre blocos e buraco de biblioteca. São regra de
   montagem, não vício de copy. O lint de HTML (`lint_email.py`) é quem tem
   uso para as 6 de convivência.
4. **Nenhum V tem eval.** Cada linha B deveria ter um caso em
   `evals/ruins/`. Hoje `evals/ruins/` está vazio.
