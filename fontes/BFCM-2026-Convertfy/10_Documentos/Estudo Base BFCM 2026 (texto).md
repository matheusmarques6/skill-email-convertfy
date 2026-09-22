Dados brutos, fontes, dicionário de campos e limites da base: [Base de dados](file/1919cd12-26a9)

## Guia de leitura, atualizado em 18/09/2026

O documento tem quatro partes. Quem precisa decidir a Black Friday lê a Parte 1 e a seção 25. Quem vai produzir e-mail lê as seções 9, 20 e 21.

| Parte | Seções | O que tem |
| --- | --- | --- |
| 1. Estudo de mercado e estratégia | 1 a 14 | Demanda e custo de mídia no quarto trimestre, calendário mestre de 10 janelas, calendário de envios de referência, ofertas, segmentação e reputação, fluxos em modo BF, SMS, estrutura e copy de e-mail, templates do Max, pendências e fontes |
| 2. Histórico da Convertfy | 15 e 16 | Planejamento do 11.11 de 2025 e os 21 e-mails executados em novembro de 2025, comparados com o Max |
| 3. Análise de contas | 17 a 21 | Emyerre (17). Blue Wolf: números e campanhas (18), design contra resultado (19), fichas com imagem por mês (20), estrutura bloco a bloco das que mais venderam (21) |
| 4. Método e consolidado | 22 e 23 | Como comparar lojas e montar o ranking geral (22). Ranking por índice, resultado por estrutura, roteiro de coleta (23). Clube Rock (24). Consolidado de três lojas, painel de achados atualizado e decisões para a BF (25) |

Estado do estudo em 20/09/2026: 3 de 15 lojas analisadas (Emyerre, Blue Wolf, Clube Rock). 5 achados se repetiram nas três. A base consolidada tem 101 envios e 2.339 pedidos, e vai a cerca de 700 envios com as 15 lojas. O resumo para decisão está na seção 25.

Escala de evidência usada no documento: \[D\] dado primário ou de fonte citada, \[P\] prática de operador, \[I\] inferência, \[V\] a verificar na fonte.

# Estudo Base BFCM 2026 | Convertfy

2026-09-18 · @Someone

## 0. Instruções para qualquer IA ou pessoa que use este documento

Este documento é a base de conhecimento da Convertfy para planejar e produzir o Q4 de 2026 (outubro a dezembro) e o pós de Q1 de 2027. Quem for gerar calendário, estratégia ou copy deve ler esta seção primeiro e seguir as regras abaixo sem exceção.

### 0.1 Contexto fixo

- A Convertfy é uma agência brasileira de e-mail marketing e CRM com mais de 250 clientes de e-commerce, a maioria em Shopify com Omnisend.
- A carteira mistura lojas brasileiras e lojas globais (EUA, UK, UE), muitas de dropshipping com domínio jovem.
- Todos os clientes fazem uma Black antecipada em 11/11. Isso é regra da casa, não opção.
- A meta é maximizar venda sem perder reputação de domínio. Quando as duas coisas conflitam, a reputação vence em contas de nível B e C (seção 6.3).
- Datas de 2026: 11.11 em uma quarta, Black Friday em 27/11, Cyber Monday em 30/11, Natal em uma sexta.

### 0.2 Ordem de decisão ao planejar um cliente

1. Classificar o cliente em quatro eixos: mercado (BR ou global), arquétipo (marca de desconto ou marca de ângulo, seção 10.3), nível de conta A, B ou C (seção 6.3) e canais ativos (e-mail, SMS, WhatsApp, push).
2. Escolher as janelas do calendário (seção 3). Cliente pequeno roda 3 ofertas, cliente grande roda as 10 janelas.
3. Escolher uma mecânica de oferta diferente por janela (seção 4.2). Nunca repetir a mesma oferta em janelas vizinhas.
4. Aplicar a cadência da janela (seção 5 e fichas da seção 3.1) e o segmento permitido para o nível da conta.
5. Ajustar os flows para o modo BFCM (seção 7) e os pop-ups por janela.
6. Escrever a copy seguindo a seção 9 e as regras de estilo do item 0.4.
7. Checar compliance do mercado (seções 8.2 e 11) antes de entregar.

### 0.3 Regras duras

- Todo número citado para cliente precisa ter nível \[D\]. Números \[P\] entram como referência de operador. Itens \[V\] não são citados sem conferência.
- Nunca inventar benchmark. Se o dado não está neste documento, dizer que falta.
- Nunca recomendar lista cheia ou dessupressão para conta nível C.
- Nunca usar preço riscado inflado em cliente BR ou UE.
- Nunca propor sorteio de reembolso para cliente BR sem parecer jurídico.
- SMS para EUA só entre 8h e 21h no horário local do destinatário.
- A linha "oferta do ano" só aparece na janela da Black Friday.

### 0.4 Regras de estilo da casa para copy

- Português do Brasil para clientes BR. Inglês para clientes globais, no tom da marca.
- Copy curta, direta, voltada para a realidade. Sem storytelling elaborado.
- Sem travessão no texto.
- E-mail HTML em layout neutro: fundo branco, texto preto, sem paleta autoral.
- Oferta entendida em três segundos, um CTA acima da dobra, prazo com data e hora.

### 0.5 Glossário

| Termo | Significado |
| --- | --- |
| BFCM | Black Friday e Cyber Monday |
| Janela | Período do calendário com uma oferta própria |
| Kickoff | Primeira oferta de novembro, de 01 a 16/11, que contém o 11.11 |
| Early Access | Oferta fechada para a lista, de 17 a 24/11 |
| Lista cheia | Todos os perfis enviáveis, inclusive inativos |
| Engajados 90, 180, 365 | Quem abriu ou clicou nos últimos 90, 180 ou 365 dias |
| Dessuprimir | Tirar da supressão perfis antigos que nunca descadastraram nem marcaram spam |
| Sitewide | Desconto no site todo |
| Tiered ou níveis | Desconto que cresce com o valor gasto |
| BOGO | Compre um, leve outro grátis ou com desconto |
| GWP | Brinde na compra |
| MMS | SMS com imagem, cerca de 3x o custo |
| Apple MPP | Proteção de privacidade da Apple que abre e-mails automaticamente e infla a taxa de abertura |
| RPR | Receita por destinatário |
| Postmaster | Google Postmaster Tools, painel de reputação do domínio no Gmail |

### 0.6 Índice de referências visuais

As imagens abaixo foram recortadas do playbook da Wellcopy e estão dentro das seções indicadas. Os templates do Figma do Max não puderam ser exportados como imagem para cá. Eles aparecem como links diretos para o frame, na seção 9.6.

| Imagem | Seção |
| --- | --- |
| Receita contra lucro em Q4 | 2 |
| Tabela de coorte de recompra | 2.5 |
| Linha do tempo de ofertas, novembro e dezembro de 2026 | 3 |
| Calendário de envios de e-mail e SMS, dia a dia | 5.1 |
| Assinantes: somar receita, não substituir | 4.6 |
| Portões abertos: cadência de lista cheia | 6.1 |
| Reenvio do mesmo e-mail | 6.6 |
| Tempos dos flows e exemplos reais por flow | 7 |
| Pop-ups de BFCM | 7 |
| Exemplos reais de SMS e MMS | 8.4 |
| Exemplos reais de e-mails gráficos | 9.1 |
| Galeria de e-mails em texto puro | 9.3 |
| Playbook de winback de Q1 | 12 |

As cinco prints do board de planejamento do 11.11 de 2025 da Convertfy estão na seção 15, com a leitura e-mail a e-mail e o modelo proposto para 2026 na seção 15.9.

As oito prints dos e-mails executados em novembro de 2025 (Blue Wolf e Dr. Melaxin) estão na seção 16, com a anatomia dos blocos, a comparação com o Max em 16.6 e os pontos de risco da copy em 16.9.

## 1. Como ler este documento

Este estudo junta cinco fontes e marca cada afirmação com um nível de evidência, para que estratégia e copy partam de fato e não de opinião.

| Sigla | Fonte | O que entrega | Limite |
| --- | --- | --- | --- |
| TT | Trendtrack, coleta de 18/09/2026 | Calendário real de e-mails, cadência, mecânica de oferta e janela de anúncios de 11 marcas | Histórico de nov/2025 completo só para MeUndies e Shopify |
| WP | Wellcopy, "The 2026 Q4 Ecommerce Profit Playbook" | Números de Shopify, NRF, Adobe, Klaviyo, Triple Whale, calendário de envio dia a dia, 7 princípios de execução, winback de Q1 | Material de captação de agência; números são de segunda mão |
| C1 | Call do Max de 17/09/2026, "BFCM Offer Cycling + Q&A" | Rotação de ofertas, envio para lista cheia com dado real, timing de recompra, assinatura, margem | Base de clientes Klaviyo, EUA, marcas grandes |
| C2 | Call do Max de 09/07/2026, "SMS Marketing Full Playbook" | Captação, compliance, flows, copy, MMS e frequência de SMS, com testes A/B | Regras legais são dos EUA |
| FG | Figma "BFCM Templates" do Max | 177 wireframes: 116 campanhas e 61 e-mails de flow, 6 esqueletos de texto puro | Sem dado de resultado no arquivo |

Escala de evidência usada nas próximas seções:

- **\[D\] Dado**: número com fonte identificável ou coleta direta nossa.
- **\[P\] Prática de operador**: o que o Max e a Wellcopy fazem em contas reais, às vezes com um exemplo numérico de um cliente, sem amostra.
- **\[I\] Inferência**: conclusão minha cruzando as fontes. Deve ser testada antes de virar regra.
- **\[V\] Verificar**: benchmark ou regra legal que não conferi na fonte original nesta pesquisa. Não vai para material de cliente sem checagem.

A pesquisa de benchmarks de mercado (Omnisend, Braze, Attentive, Neotrust, Google Postmaster) não pôde ser confirmada por busca web. Esses itens aparecem como \[V\] e estão listados na seção 14.

## 2. Banco de números

Três fatos sustentam o plano: a demanda começa em setembro e explode na semana da BF, o anúncio dobra de preço em novembro, e e-mail mais SMS seguram 42% da receita do período.

![Receita contra lucro em Q4: loja com US$ 5,28 milhões de vendas em novembro e dezembro e US$ 12,84 de saldo depois de anúncios, descontos, custo de produto, frete e devoluções](blob/46fd7f37-3bd6)

A imagem acima é a tese do playbook da Wellcopy. No exemplo, US$ 5.284.921 de vendas viram US$ 12,84 de lucro depois de Meta Ads, descontos, custo e frete, devoluções e taxas. Desconto fundo somado a CPM caro, custo de produto e devolução consome a receita. É ilustração do autor, não dado de uma loja real. \[P, WP\]

### 2.1 Demanda e timing

| Número | O que mede | Fonte | Nível |
| --- | --- | --- | --- |
| 26% | Consumidores que começam as compras de fim de ano até o fim de setembro | Shopify, via WP | D |
| 42% | Planejam navegar e comprar antes de novembro | NRF, via WP | D |
| US$ 88,7 bi | Gasto online só em outubro de 2025, alta de 8,2% | Adobe, via WP | D |
| 13% | Marcas que rodaram promoção antes de outubro | Shopify, via WP | D |
| 63% | Fizeram a maior parte das compras na semana do Thanksgiving (era 59% no ano anterior) | WP | D |
| 15/09 a 30/11/2025 | Janela em que a Shopify rodou criativos de BF, até 69 dias por criativo | TT | D |
| 18/11/2025 | MeUndies abre "VIP Early Access", 9 dias antes da BF | TT | D |

Leitura: antecipar gera lista e venda a preço cheio, mas o pico não se move. O plano precisa das duas coisas.

### 2.2 Custo de aquisição

| Número | O que mede | Fonte | Nível |
| --- | --- | --- | --- |
| US$ 11,21 | CPM médio Meta em setembro de 2025 | Superads e Triple Whale, via WP | D |
| US$ 21,96 | CPM médio Meta em novembro de 2025 | idem | D |
| +65% | Salto de CPM de outubro para novembro | idem | D |
| 2 a 3x | CPM na semana da BF contra o leilão normal | WP | P |

Leitura: lead captado em setembro e outubro custa perto da metade. A lista é o único ativo que não reprecifica em novembro.

### 2.3 Canais próprios

| Número | O que mede | Fonte | Nível |
| --- | --- | --- | --- |
| 42% | Receita de BFCM vinda de e-mail e SMS | Klaviyo, via WP | D |
| 43,3% | Receita do dia da BF vinda desses canais | Klaviyo, via WP | D |
| +15,2% | Crescimento anual da receita de campanhas de e-mail | Klaviyo, via WP | D |
| +24,6% | Crescimento anual da receita de campanhas de SMS | Klaviyo, via WP | D |
| +13,6% e +9,1% | Crescimento de recompradores e de novos compradores via canais próprios | Klaviyo, via WP | D |
| 46% | Receita mensal vinda de e-mail em uma marca da comunidade | C1 | P |

Ressalva: os números da Klaviyo são de clientes Klaviyo com atribuição Klaviyo. Não representam o mercado inteiro nem contas Omnisend.

### 2.4 Alcance e engajamento

| Número | O que mede | Fonte | Nível |
| --- | --- | --- | --- |
| 172.000 contra 145.000 | Aberturas de um envio para lista cheia contra o segmento engajado de 90 dias, mesma marca | C1 | P |
| cerca de metade | Parcela dos envios de BFCM do Max que vai para a lista inteira | C1 | P |
| 50 a 60% | Faixa de abertura que o Max considera saudável. Acima de 70% indica segmento apertado demais | C1 | P |
| 40% para 78% | Salto de abertura que só acontece apertando o segmento, não melhorando copy | C1 | P |

### 2.5 Recompra e coorte

| Número | O que mede | Fonte | Nível |
| --- | --- | --- | --- |
| 30 a 50% menor | Taxa de recompra de clientes adquiridos em nov e dez contra os outros meses | WP, tabela de coorte | D |
| primeiros 14 dias | Onde se concentra a recompra em vestuário, acessórios, beleza e fragrância | C1, dados internos Wellcopy | P |
| 50% até o dia 35 | Segundos pedidos em marca de consumíveis; pico perto do dia 30 | C1 | P |
| 50% antes do dia 21 | Segundos pedidos (dentro de 90 dias) em marca de 9 dígitos sem SMS pós-compra | C2 | P |
| 77% | Inscritos que convertem e o fazem no dia zero | C2, dados internos Wellcopy | P |

![Tabela de coorte: clientes adquiridos em novembro e dezembro mostram taxa de recompra 30 a 50% menor que os adquiridos nos outros meses](blob/e2db5e4a-27fa)

Como ler a tabela: cada linha é o mês em que o cliente fez a primeira compra, cada coluna é a taxa de recompra nos meses seguintes. As linhas de novembro e dezembro, marcadas em vermelho, ficam abaixo de todas as outras nos quatro primeiros meses. \[D, WP\]

### 2.6 SMS e MMS

| Número | O que mede | Fonte | Nível |
| --- | --- | --- | --- |
| +50% | Cliques e performance geral de "Your order is ready to ship" contra copy passiva de abandono | C2 | P |
| 20% | Conversão de um flow de SMS de um membro | C1 | P |
| US$ 115 mil | Receita em um trimestre do flow "Espresso Shot" só por SMS, uma marca | C2 | P |
| US$ 694 contra US$ 321 | Receita de MMS contra SMS no mesmo teste. Lucro bruto US$ 658 contra US$ 309 | C2 | P |
| US$ 2.000 contra US$ 534 | MMS mostrando o brinde contra SMS texto. Custo extra perto de US$ 200 | C2 | P |
| 3x | Custo do MMS contra o SMS | C2 e WP | D |
| até US$ 20.000 | Acordo por violação de horário de silêncio nos EUA, caso real citado | C2 | P e V |
| +21% | Aumento de envio de formulário em pop-up de um membro | C2 | P |

### 2.7 Cadência observada fora de pico (TT)

| Marca | Mercado | E-mails por semana | Mecânica dominante |
| --- | --- | --- | --- |
| Insider | BR | cerca de 7 | % de desconto, frete grátis, brinde |
| Ridge | EUA | cerca de 7 | Conteúdo e urgência com crédito |
| Brooklinen | EUA | cerca de 5 | % de desconto, até 75% |
| Sallve | BR | cerca de 4 | Brinde na compra |
| Huel | UK | cerca de 2 | Ângulo e educação |
| Gymshark | UK | cerca de 1 | Frete grátis com valor mínimo, drops |
| Alpha | BR | cerca de 1 | % de desconto, copy de curiosidade |

## 3. Calendário mestre Q4 2026

O trimestre vira uma sequência de 10 janelas, cada uma com oferta própria, e o 11.11 da Convertfy passa a ser o pico e o fechamento da primeira oferta de novembro.

Base: linha do tempo de ofertas do WP e estrutura de "cerca de cinco ofertas distintas em novembro" do C1, ajustadas para o 11.11 e para o Brasil. Em 2026 a BF cai em 27/11, um dia antes de 2025, o que deixa 25 dias entre Cyber Monday e Natal.

| Janela | Datas 2026 | Papel | Oferta sugerida | Força da oferta | Origem |
| --- | --- | --- | --- | --- | --- |
| 0. Encher a lista | Setembro até meados de out | Captação com CPM baixo, aquecimento de domínio, limpeza de lista | Sorteios, isca de lista VIP, mensagem sutil de presente | Sem oferta dura | WP, C1 |
| 1. Presente antecipado | Outubro. No BR, Dia das Crianças em 12/10 | Venda a preço quase cheio, conveniência | Brinde na compra e página de coleção de presentes | Leve | WP |
| 2. Kickoff | 01 a 10/11 | Primeira oferta de novembro | Bundles e kits, desconto em valor fixo | Forte, abaixo das próximas | WP |
| 3. **11.11 Black antecipada** | 11/11, com cauda até 16/11 | Pico e fechamento do Kickoff | Mesma família do Kickoff com reforço de 24 a 48h: brinde extra ou nível adicional | Forte, mecânica diferente da BF | Convertfy + I |
| 4. Early Access | 17 a 24/11 | Oferta nova, fechada para lista | % de desconto com acesso antecipado. Exclusividade é a alavanca | Parecida com a BF, um pouco menor | WP, C1, TT (MeUndies) |
| 5. Black Friday | Quarta 25 a domingo 29/11 | A maior, mais simples e mais valiosa oferta do ano | Melhor sitewide, entendível em três segundos | Máxima | WP, C1 |
| 6. Cyber Monday | 30/11 a 03/12 | Mesmo valor, ângulo novo | O "twist": % extra, brinde, drop de produto | Máxima, com novidade | WP, C1 |
| 7. Presentes | 04 a 14/12 | Virada para presente | Gasto em níveis (gaste X, leve Y%), bundles, guias de presente | Média | WP |
| 8. Prazo de entrega | 15, 19 e 21/12 nos EUA. No BR e UE, datas da transportadora de cada cliente | O prazo é a oferta | Frete grátis, upgrade de envio, flash em cada data | Média | WP |
| 9. Última hora | 22 a 24/12 | Quem perdeu o prazo | Vale-presente digital | Leve | WP |
| 10. Pós-Natal | 26 a 31/12 | Virada de ano. No UK e UE, Boxing Day em 26/12 | Crédito de loja de fim de ano, bundles de Ano Novo | Média | WP |

![Linha do tempo de ofertas de novembro e dezembro de 2026 segundo a Wellcopy: oferta 1 de 01 a 16/11, oferta 2 de 17 a 24/11, oferta 3 de 25 a 29/11, oferta 4 de 30/11 a 03/12, oferta 5 de 04 a 19/12](blob/19bdcd6b-9c2b)

Como ler: cada cor é uma oferta. Vermelho é o Kickoff (01 a 16/11). Roxo é o Early Access (17 a 24/11). Azul é a Black Friday, que abre na quarta 25/11 e fecha no domingo 29/11. Laranja é a Cyber Monday (30/11 a 03/12). Verde é a oferta de presentes (04 a 19/12), com os três prazos de entrega dos EUA marcados em 15, 19 e 21/12. No modelo original o 11/11 é só o Veterans Day. Na Convertfy ele vira o pico da linha vermelha. \[D, WP\]

### Como o 11.11 deixa de canibalizar a BF

- A mecânica muda entre as janelas. Quem comprou bundle no 11.11 ainda tem motivo para voltar no sitewide da BF. \[P, C1: ninguém recompra na mesma oferta\]
- O maior desconto percentual do ano fica reservado para 25 a 29/11. A linha "oferta do ano" só aparece ali. \[P, C1\]
- O site inteiro troca a cada janela, não só o banner. \[P, C1\]
- Existe uma aba permanente de "ofertas de fim de ano" com remarcações, para quem navega entre um pico e outro. \[P, C1\]

### Regra de três ofertas

O próprio WP avisa: quem não tem braço para 10 janelas roda de 1 a 3 ofertas centrais com bom conteúdo e alta frequência. Para clientes pequenos, o mínimo viável é 11.11, Early Access com BF, e Cyber Monday com presentes. \[P\]

### Datas de apoio

| Data | Evento | Mercado |
| --- | --- | --- |
| 12/10 | Dia das Crianças | BR |
| 31/10 | Halloween | EUA, UK |
| 11/11 | Singles Day. Nos EUA é Veterans Day | Todos |
| até 30/11 | Primeira parcela do 13º salário | BR |
| 26/11 | Thanksgiving | EUA |
| 28/11 | Small Business Saturday | EUA |
| até 20/12 | Segunda parcela do 13º salário | BR |
| 19 e 20/12 | Último fim de semana cheio de compras, Natal cai numa sexta | Todos |
| 26/12 | Boxing Day | UK, UE |

### 3.1 Fichas por janela

Cada ficha diz o que fazer na janela, para quem enviar em cada nível de conta e que ângulo de copy usar. Os assuntos são modelos para adaptar, em PT para clientes BR e em EN para clientes globais. Volumes vêm da seção 5. Segmentos vêm da seção 6.3.

#### Ficha 1. Outubro: captação e presente antecipado (01 a 31/10)

| Item | Definição |
| --- | --- |
| Objetivo | Crescer lista com CPM ainda baixo (US$ 11,21 em setembro contra US$ 21,96 em novembro), aquecer domínio, vender a preço quase cheio |
| Oferta | Brinde na compra e página de coleção de presentes. Isca de lista VIP: acesso antecipado à Black |
| Segmento | A: engajados 120. B: engajados 90. C: engajados 60 |
| E-mail | 3 por semana, subindo para o ritmo de novembro. Clientes que enviam 1 a 2 por semana sobem aqui |
| SMS ou WhatsApp | 1 por semana. Foco em captar telefone no pop-up |
| Push | Ativar pedido de permissão. 1 a 2 por semana |
| Site e pop-up | Pop-up de lista VIP com e-mail e telefone. Frase do passo de SMS: finalize por SMS para ativar o benefício |
| Preparação técnica | Autenticação, Postmaster, limpeza de lista, dessupressão em lotes só no nível A |
| Ângulo de copy | Conveniência: resolver os presentes cedo, dividir o gasto entre salários, fugir do aperto. Só 13% das marcas promovem antes de outubro |
| Assuntos modelo | "Entre na lista VIP da Black". "Presentes resolvidos antes da correria". "Get first access to our Black Friday" |
| Freio | Spam acima de 0,1% pausa a subida de volume |

#### Ficha 2. Kickoff (01 a 10/11)

| Item | Definição |
| --- | --- |
| Objetivo | Primeira oferta de novembro. Capturar os 42% que planejam comprar antes do pico |
| Oferta | Bundles, kits e desconto em valor fixo. Forte, abaixo das próximas |
| Segmento | A: lista cheia no lançamento, engajados 365 no meio. B: engajados 365 no lançamento, 120 a 180 no meio. C: engajados 120 no lançamento, 60 a 90 no meio |
| E-mail | Dia sim, dia não. Cerca de 5 no período |
| SMS ou WhatsApp | 2 por semana, nos dias sem e-mail |
| Push | 2 a 3 por semana |
| Site e pop-up | Site inteiro troca para a oferta. Pop-up com a oferta do Kickoff |
| Ângulo de copy | Kits prontos para presentear, economia em valor (R$ ou US$), começo da temporada |
| Assuntos modelo | "Kits de fim de ano já disponíveis". "R$ 50 off nos kits". "Holiday bundles are here" |

#### Ficha 3. 11.11 Black antecipada (11/11, cauda até 16/11)

| Item | Definição |
| --- | --- |
| Objetivo | Pico e fechamento do Kickoff. Venda antecipada sem gastar a oferta da BF |
| Oferta | Mesma família do Kickoff com reforço de 24 a 48h: brinde extra, nível a mais ou frete grátis. Mecânica diferente do sitewide da BF |
| Segmento | A: lista cheia na abertura e nas últimas horas. B: engajados 365. C: engajados 120 a 180 |
| E-mail | 11/11: 2 a 3 (abertura de manhã, tarde, últimas horas). 12 a 16/11: 2 no período (continua e fechamento) |
| SMS ou WhatsApp | 1 a 2 no dia 11. 1 no fechamento |
| Push | 2 no dia 11. 1 a 2 na cauda |
| Site e pop-up | Banner e página de 11.11. Pop-up com a oferta do dia |
| Ângulo de copy | Prévia da Black, só hoje, brinde enquanto durar o estoque. Não usar "oferta do ano" |
| Assuntos modelo | "11.11: a Black começou antes aqui". "Só hoje: kit com brinde". "Últimas horas do 11.11". "11.11 is live: early Black Friday" |
| Freio | Se o spam da abertura passar de 0,2%, as últimas horas vão só para engajados 30 |

Esta ficha é o resumo. O detalhamento do 11.11, com o calendário que a Convertfy rodou em 2025 e a versão proposta para 2026 disparo a disparo, está na seção 15.

#### Ficha 4. Early Access (17 a 24/11)

| Item | Definição |
| --- | --- |
| Objetivo | Oferta nova, fechada para a lista. Exclusividade é a alavanca. MeUndies abriu VIP em 18/11/2025 |
| Oferta | % de desconto com acesso antecipado, parecida com a da BF e um pouco menor. Única janela com oferta exclusiva de lista |
| Segmento | A: lista cheia no lançamento, engajados 365 nos lembretes, lista cheia no fechamento de 24/11. B: engajados 365 e depois 180. C: engajados 120 e depois 90 |
| E-mail | 1 por dia, 8 no período |
| SMS ou WhatsApp | 4 no período: 18, 20, 23 e 24/11 |
| Push | 1 por dia |
| Site e pop-up | Página fechada por cadastro. Pop-up: "cadastre-se para liberar o acesso antecipado" |
| Ângulo de copy | Você entra antes, estoque ainda cheio, sem risco de atraso na entrega |
| Assuntos modelo | "Acesso VIP liberado". "Sua Black começa hoje". "O acesso antecipado fecha hoje". "VIP Early Access: Black Friday unlocked" |

#### Ficha 5. Black Friday (quarta 25 a domingo 29/11)

| Item | Definição |
| --- | --- |
| Objetivo | Maior receita do ano. 63% das compras de fim de ano acontecem nesta semana. 43,3% da receita do dia vem de e-mail e SMS |
| Oferta | A maior, mais simples e mais valiosa. Sitewide entendível em três segundos. Pode empilhar brinde |
| Segmento | A: lista cheia em todos os envios. B: engajados 365, inativos só na sexta. C: engajados 120 a 180, sem inativos |
| E-mail | 25/11: 2. 26/11: 2. 27/11: 3. 28/11: 3. 29/11: 2. Total 12. Primeiro envio de manhã, lembrete à noite. Reenvio com assunto novo vale |
| SMS ou WhatsApp | 1 por dia, 2 na sexta e no sábado. Total 7 |
| Push | 2 a 3 por dia |
| Flows | Carrinho e checkout com 2 e-mails, welcome com a oferta, pós-compra com "a oferta continua" |
| Site e pop-up | Site todo na oferta. Pop-up de BF com e-mail e telefone |
| Ângulo de copy | "A oferta do ano". Melhor preço que a marca vai ter, prazo claro, estoque |
| Assuntos modelo | "A oferta do ano começou". "Até 50% off no site todo". "Termina domingo às 23h59". "Black Friday is live". "Our offer of the year" |
| Freio | Spam acima de 0,3%: cortar reenvio e lista cheia por 48h |

#### Ficha 6. Cyber Monday (30/11 a 03/12)

| Item | Definição |
| --- | --- |
| Objetivo | Segunda chance para quem não comprou. Mesmo valor, ângulo novo |
| Oferta | O twist: % extra, brinde novo ou drop de produto |
| Segmento | Igual à BF no dia 30/11. Depois recua um degrau |
| E-mail | 30/11: 2 a 3. 01 a 03/12: 1 por dia |
| SMS ou WhatsApp | 1 por dia |
| Push | 2 no dia 30, 1 por dia depois |
| Ângulo de copy | Perdeu a Black, a porta ficou aberta. Novidade que não estava na BF |
| Assuntos modelo | "Perdeu a Black? Deixamos a porta aberta". "Cyber Monday: brinde novo em todo pedido". "Cyber Monday ends tonight" |

#### Ficha 7. Presentes e prazo de entrega (04 a 21/12)

| Item | Definição |
| --- | --- |
| Objetivo | Virar a mensagem para presente. O prazo de entrega vira a oferta |
| Oferta | Gasto em níveis (gaste X e leve 20%, gaste 2X e leve 30%), bundles, guias de presente. Nos prazos: frete grátis e upgrade de envio |
| Segmento | A: engajados 365, lista cheia só nos prazos. B: engajados 180. C: engajados 90 |
| E-mail | Dia sim, dia não. 11 no período. E-mail e SMS juntos nas datas de prazo |
| SMS ou WhatsApp | Alternado com o e-mail, 9 no período |
| Push | Lembrete de prazo |
| Ângulo de copy | Guia de presentes por pessoa e por faixa de preço. Data limite para chegar antes do Natal |
| Assuntos modelo | "Presentes até R$ 150". "Último dia para receber antes do Natal". "48 hours left for standard shipping" |
| Atenção | Dropshipping com prazo de 10 a 20 dias: a data limite real é no começo de dezembro. Não prometer Natal sem garantia |

#### Ficha 8. Última hora e pós-Natal (22 a 31/12)

| Item | Definição |
| --- | --- |
| Objetivo | Vender para quem perdeu o prazo e abrir o ano |
| Oferta | 22 a 24/12: vale-presente digital. 26 a 31/12: crédito de loja de fim de ano e bundles de Ano Novo. UK e UE: oferta de Boxing Day em 26/12 |
| Segmento | Engajados 90 a 180 em todos os níveis. O pico já passou |
| E-mail | 3 por semana |
| Ângulo de copy | Presente que chega na hora, por e-mail. Crédito para começar 2027 |
| Assuntos modelo | "Vale-presente: chega em 1 minuto". "Você tem crédito para usar até 31/12". "Boxing Day starts now" |

## 4. Estratégia de ofertas

Nunca uma oferta só para o período inteiro: a mesma oferta por 15 dias gera fadiga nos dias 7 a 14, uma única "última chance" e quase nenhuma recompra. \[P, WP e C1\]

### 4.1 O que a rotação entrega

- Lista engajada por 2 a 3 semanas, porque cada oferta nova é motivo para abrir e clicar.
- 3 a 4 picos de urgência no lugar de um.
- Segunda e terceira chance para quem não comprou na primeira.
- Recompra: ofertas diferentes dão motivos diferentes para voltar.
- Cobre preferências: parte do público reage a %, parte a bundle, parte a brinde.
- Permite testar ângulo e mecânica e aprender para o ano seguinte.

Critério de uma boa oferta (WP): simples, urgente, protege margem e parece diferente de tudo o que a marca rodou no ano. Se o cliente precisa interpretar, perdeu.

### 4.2 Cardápio de mecânicas

| Mecânica | Quando usar | Observação | Origem |
| --- | --- | --- | --- |
| Lançar algo novo (cor, sabor, coleção, edição limitada) | Qualquer nicho, qualquer janela | Dá à lista um motivo além de preço. Cuts fez drops semanais por 3 meses | WP |
| Coleção de bundles de fim de ano | Kickoff, 11.11, Presentes | Sobe ticket médio e facilita o presente | WP |
| "Até XX% off no site todo" | BF | Favorita do Max para catálogo grande. Fácil de ajustar no meio | WP, TT |
| Brinde empilhado no desconto | BF, CM, 11.11 | 20% mais brinde soa como duas ofertas. O brinde custa uma fração de mais 10% de desconto | WP, TT (Sallve, Insider) |
| BOGO, leve 3 pague 2, segundo com 50% | Produto de recompra ou baixo custo | "Muito forte" segundo o Max | WP |
| Desconto como crédito de loja | Presentes, pós-Natal, flows | "US$ 20 de crédito" rende mais que "US$ 20 off". Níveis: 20 em 50 a 100, 40 em 100 a 200, 75 acima de 200 | WP |
| Gasto em níveis | Presentes (04 a 14/12) | Gaste 100 leve 20%, gaste 200 leve 30% | WP |
| Bônus no lugar de desconto | Marca premium ou margem curta | IM8 deu 4 produtos bônus (US$ 118 de valor) sem baixar preço | WP |
| Sorteio de reembolso do pedido | Pico curto, por cima de outra oferta | Ver 4.4. Supera campanha de desconto comum segundo o Max, que rodou mais de 50 vezes | C2 |

### 4.3 Marcas que não dão desconto

Reformular a oferta em algo que a marca já entrega: frete grátis acima de um valor, guia em PDF, bônus de valor. O pop-up usa esse benefício como gancho. \[P, C2\]

### 4.4 Sorteio de reembolso, passo a passo

1. E-mail 1, manhã: "Vamos reembolsar três pedidos feitos hoje. Ganhadores amanhã."
2. E-mail 2, 17h: última chance, faltam poucas horas para participar.
3. E-mail 3, manhã seguinte: anuncia ganhadores e dá 15% por 24h para quem não ganhou.

Pode ser empilhado sobre a oferta da BF, desde que caiba na margem. \[P, C1\]

**Alerta legal**: nos EUA, sorteio exige opção de participação sem compra. No Brasil, promoção com sorteio normalmente exige autorização prévia do Ministério da Fazenda (SPA). Não rodar em cliente BR sem parecer jurídico. \[V\]

### 4.5 Proteção de margem

- A tese do WP: todo mundo bate recorde de receita em novembro e quase ninguém lucra, porque comprou a receita com desconto e anúncio no momento mais caro do ano.
- Empatar na aquisição só é aceitável com plano de recompra em Q1 (seção 12).
- Brinde precisa ser barato de verdade. Na conta do Max, brinde de US$ 3 exige vários pontos de retenção para empatar. A US$ 1 quase empata já no primeiro pedido. Em 10.000 assinantes, brinde em toda renovação custa de US$ 45 a 50 mil por mês. Montar calculadora antes de prometer. \[P, C1\]
- Oferta no site todo, não exclusiva de e-mail. Não há motivo para esconder a oferta de quem não é inscrito no maior período do ano. A exceção é a janela de Early Access. \[P, C1\]

### 4.6 Marcas de assinatura

- Não excluir o assinante ativo. É o cliente mais leal e também compra presente. Excluir por completo é perder receita incremental.
- Incluir em cerca de 25% dos envios gerais e dar oferta própria que soma receita: add-on com 50% no próximo pedido, via plataforma de assinatura.
- Estrutura de desconto (modelo Armra): zero no avulso, 25 a 30% no primeiro pedido da assinatura, cerca de 10% recorrente. 5% é baixo demais para reter. 20% retém mais que 10%, mas a margem cedida precisa se pagar.
- Parte do pico de cancelamento atribuído a um e-mail é coincidência de atribuição.

![Diagrama "Don't replace revenue, add to it": à esquerda a promoção sitewide faz o assinante cancelar e reassinar mais barato, à direita a oferta de add-on soma receita sem mexer na assinatura](blob/3cc797ad-a02f)

Como ler: no caminho da esquerda o assinante ativo vê o sitewide de 30 a 50%, cancela e reassina no preço promocional. A receita foi substituída. No caminho da direita ele recebe uma oferta própria de add-on, entregue junto com o próximo pedido, e mantém a assinatura. A receita foi somada. O rodapé traz o número operacional: enviar aos assinantes cerca de 25% das campanhas gerais de BFCM. \[P, WP\]

### 4.7 O que não copiar

O Max recomenda "ancorar preço": subir o preço riscado e manter o preço de venda. No Brasil isso é a prática de "metade do dobro", alvo de Procon e do CDC. Na UE, a diretiva Omnibus exige como referência o menor preço dos últimos 30 dias. **Não aplicar em clientes BR e UE.** \[V para o texto exato da regra; o risco é conhecido\]

## 5. Cadência e volume por canal

A referência da Wellcopy para uma marca que envia 3 a 4 vezes por semana é de cerca de 46 e-mails e 30 SMS entre 01/11 e 21/12. Contei célula a célula no calendário do WP.

### 5.1 Calendário de referência (WP), por janela

| Janela | Dias | E-mails | SMS | Ritmo |
| --- | --- | --- | --- | --- |
| Kickoff, 01 a 16/11 | 16 | 9 | 6 | E-mail dia sim, dia não. SMS nos dias sem e-mail. Sobe no fim da oferta |
| Early Access, 17 a 24/11 | 8 | 8 | 4 | 1 e-mail por dia. SMS em 18, 20, 23 e 24 |
| Black Friday, 25 a 29/11 | 5 | 12 | 7 | 2, 2, 3 (sexta), 3 (sábado), 2 (domingo fecha). Manhã e lembrete à noite |
| Cyber Monday, 30/11 a 03/12 | 4 | 5 a 6 | 4 | 2 a 3 no dia 30, depois 1 por dia até o fechamento |
| Presentes e prazos, 05 a 21/12 | 17 | 11 | 9 | Alternado. E-mail e SMS juntos em 15, 19 e 21/12 |

![Calendário de envios de e-mail e SMS da Wellcopy para novembro e dezembro de 2026, dia a dia](blob/1535c9b1-addb)

Como ler: vermelho é e-mail, azul é SMS, verde é marco do calendário. Leitura dia a dia do original:

| Período | E-mail nos dias | SMS nos dias |
| --- | --- | --- |
| Kickoff | 1, 3, 5, 7, 9, 11, 13, 15 e 16/11 | 1, 4, 6, 10, 14 e 16/11 |
| Early Access | Todo dia de 17 a 24/11. Lançamento em 17, fechamento em 24 | 18, 20, 23 e 24/11 |
| Black Friday | 25/11: 2. 26/11: 2. 27/11: 3. 28/11: 3. 29/11: 2 | 25: 1. 26: 1. 27: 2. 28: 2. 29: 1 |
| Cyber Monday | 30/11: 2 a 3. 01, 02 e 03/12: 1 por dia | 30/11, 01, 02 e 03/12 |
| Presentes | 5, 7, 9, 11, 13, 15, 16, 18, 19, 20 e 21/12 | 6, 8, 10, 12, 14, 15, 17, 19 e 21/12 |

Nota do próprio calendário: serve para marcas que enviam 3 a 4 e-mails por semana no resto do ano. Dias 2, 8 e 12/11 e 4/12 ficam sem envio. Depois de 21/12 o modelo não prevê envios. \[D, WP\]

Marcas agressivas chegam a envio diário e até 4 e-mails por dia nos picos. \[P, WP\]

### 5.2 Ajuste para o 11.11 da Convertfy

| Dias | E-mails | SMS ou WhatsApp | Push |
| --- | --- | --- | --- |
| 01 a 10/11 | Dia sim, dia não | 2 por semana | 2 a 3 por semana |
| 11/11 | 2 a 3: abertura, tarde, últimas horas | 1 a 2 | 2 |
| 12 a 16/11 | 2 no período: "continua" e fechamento | 1 no fechamento | 1 a 2 |

O restante segue a tabela 5.1. \[I\]

### 5.3 Comparação com o que o mercado já faz

Insider e Ridge enviam cerca de 7 e-mails por semana fora de pico, Brooklinen 5, Sallve 4 (TT). O ritmo do WP para o início de novembro, 4 a 5 por semana, é igual ou menor que o normal desses líderes. O risco de reputação não está na rampa. Está em quem recebe os envios do pico (seção 6). \[I\]

Para clientes que hoje enviam 1 a 2 por semana, a rampa precisa começar em outubro: subir para 3 por semana antes de novembro, para o salto não ser de 2 para 14 em uma semana. \[I\]

### 5.4 Papel de cada canal

| Canal | Papel | Custo | Onde pesa |
| --- | --- | --- | --- |
| E-mail | Âncora. Carrega a oferta, o conteúdo e o volume | Baixo | Todos os mercados |
| SMS | Urgência e lembrete. Alterna com o e-mail | Alto. MMS 3x o SMS | EUA e UK. Ver regras na seção 8 |
| WhatsApp | Faz no BR o papel que o SMS faz nos EUA | Médio, por conversa | BR. \[V\] para números de abertura |
| Push, app e web | Lembrete de custo quase zero: abertura de oferta, últimas horas, volta ao estoque | Quase zero | Clientes com app (Appsfy) e web push. \[V\] para benchmarks |

Ordem dentro de um mesmo evento: e-mail primeiro, push em seguida, SMS ou WhatsApp para as últimas horas e para VIP. Em flows, e-mail primeiro e SMS cinco minutos depois, para o filtro de conversão segurar o SMS de quem já comprou. \[P, C2\]

### 5.5 Quem comprou continua recebendo

O padrão de mercado é excluir comprador recente por 2 a 3 semanas. O Max recomenda não excluir: a recompra se concentra nos primeiros 14 dias, na fase de empolgação. Excluir tira a pessoa da janela de maior intenção. Vale para vestuário, acessórios, beleza e fragrância. \[P, C1\]

Isso corrige minha recomendação anterior de supressão cruzada de compradores. A supressão fica restrita ao mesmo e-mail no mesmo dia, não à janela seguinte. \[I\]

## 6. Segmentação e deliverability

O envio para lista cheia é, segundo o Max, a maior alavanca da BFCM, e é também o maior risco para a carteira da Convertfy. A saída é liberar por nível de conta.

### 6.1 O que o Max faz e o dado que ele mostra

- Cerca de metade dos envios de BFCM vai para a lista inteira. \[P, C1\]
- Dado real de uma marca: lista cheia gerou 172.000 aberturas contra 145.000 no segmento de 90 dias. São 27.000 aberturas a mais, cerca de 19%, só por abrir o envio. \[P, C1\]
- Esquema de segmentos: engajados de 120, 90 e 30 dias na preparação. Lista cheia no lançamento do Early Access. Engajados 365 nos lembretes. Lista cheia na última chance. Lista cheia em toda a janela BF a CM. Volta para engajados nos dias calmos. \[P, C1\]
- Inativos não recebem sequência de aquecimento nem "sentimos sua falta". Entram direto nos envios da BF: se alguém vai voltar, é pela melhor oferta do ano. \[P, C1\]
- Antes disso, dessuprimir todo perfil que já abriu, navegou ou comprou, desde que nunca tenha descadastrado ou marcado spam. \[P, WP\]
- Argumento dele: quem entra em novembro com reputação saudável aguenta três semanas de métrica pior e tem onze meses para recuperar. Por isso o aquecimento começa em setembro. \[P, WP\]
- Abertura de 50 a 60% é o alvo. Acima de 70% a marca está deixando alcance na mesa. \[P, C1\]

![Diagrama "BFCM: Open the floodgates": no envio normal só uma parte da lista recebe, na BFCM os portões abrem para compradores antigos, navegadores, engajados e reativados. Cadência: lançamento para lista cheia, meio de campanha para engajados 365 a 730, fechamento para lista cheia](blob/90b745df-5ec1)

Como ler a cadência de envio do diagrama: 1. lançamento, lista cheia. 2. meio da campanha, segmento amplo de 365 a 730 dias. 3. meio da campanha, lista cheia. 4. meio da campanha, segmento amplo. 5. fechamento, lista cheia. Esse é o modelo puro do Max e corresponde ao nível A da seção 6.3. \[P, WP\]

### 6.2 Por que não vale igual para todos os clientes da Convertfy

- O dado de 172 mil contra 145 mil mede aberturas, não receita, não reclamação de spam e não colocação na caixa de entrada nos dias seguintes. Com Apple MPP, parte dessas aberturas é automática. \[I\]
- A premissa é marca de 7 a 9 dígitos, domínio maduro, Klaviyo. Boa parte da carteira é loja nova ou dropshipping, domínio jovem, Omnisend. \[I\]
- A Omnisend revisa e bloqueia conta por pico de volume com lista fria. Conta bloqueada na semana da BF custa mais que as 27 mil aberturas. A Convertfy já tem caso de bloqueio em revisão de compliance. \[D interno\]
- Gmail e Yahoo exigem desde 2024 SPF, DKIM, DMARC, descadastro em um clique e reclamação de spam abaixo de 0,3%, com alvo abaixo de 0,1%. Microsoft passou a exigir autenticação equivalente em 2025. \[V para os limiares exatos\]

### 6.3 Proposta: três níveis de conta

Os cortes abaixo são proposta inicial e precisam ser calibrados com os dados reais das contas. \[I\]

| Nível | Perfil da conta | Lançamentos e fechamentos | Envios do meio | Dessuprimir | Inativos |
| --- | --- | --- | --- | --- | --- |
| A | Domínio com mais de 12 meses de envio contínuo, spam abaixo de 0,1% no Postmaster, já envia 3 ou mais por semana | Lista cheia | Engajados 365 | Sim, em outubro | Entram nos picos |
| B | Domínio de 6 a 12 meses ou histórico irregular, spam entre 0,1 e 0,2% | Engajados 365 | Engajados 120 a 180 | Só compradores antigos | Entram só na BF e na CM |
| C | Domínio com menos de 6 meses, conta recém-migrada, ou qualquer alerta recente da Omnisend | Engajados 120 a 180 | Engajados 60 a 90 | Não | Não entram |

### 6.4 Preparação, de agora até 31/10

1. Autenticação em todas as contas: SPF, DKIM, DMARC, domínio de envio próprio. Registrar no Google Postmaster.
2. Limpeza de inválidos e bounces agora, não em novembro.
3. Enviar só para engajados e buscar aberturas, cliques e respostas por algumas semanas para recuperar caixa principal. \[P, WP\]
4. Subir volume em degraus semanais. Regra prática de no máximo dobrar por etapa. \[V\]
5. Contas nível A: dessuprimir em outubro, em lotes, observando spam a cada lote.
6. Validar com a Omnisend o limite de envio de cada conta antes de novembro.

### 6.5 Freios durante a operação

| Sinal | Ação |
| --- | --- |
| Reclamação de spam acima de 0,2% em um envio | Próximo envio volta um degrau de segmento |
| Acima de 0,3% | Cortar reenvios e lista cheia por 48h. Só engajados 30 |
| Reputação do domínio cai no Postmaster | Pausar dessupressão e inativos até recuperar |
| Bounce acima de 2% | Parar e limpar antes do próximo envio |
| Qualquer aviso da Omnisend | Congelar volume, responder ao compliance no mesmo dia |

Métrica de decisão: clique, receita por destinatário e spam. Abertura é só sinal auxiliar por causa do Apple MPP. \[I\]

### 6.6 Reenvio

O mesmo e-mail pode ser reenviado com assunto e pré-cabeçalho novos. O cliente não lembra, a caixa recebe mais de 100 e-mails no período. Versão conservadora: reenviar só para quem não abriu. Economiza produção numa fase de alto volume. \[P, WP\]

![Diagrama de reenvio: dia 1 a pessoa vê o e-mail e não compra, em seguida recebe mais de 100 outros e-mails, em um novo dia o reenvio com assunto e pré-cabeçalho novos é visto de novo e converte](blob/fa9b767d-aeca)

Regra de produção: o corpo do e-mail fica igual. Mudam só o assunto e o pré-cabeçalho. Um e-mail produzido rende dois ou três envios na semana da BF. \[P, WP\]

Para níveis B e C, usar sempre a versão "só não abridores". \[I\]

## 7. Flows em modo BFCM

Durante o período, cada flow encolhe para 1 a 2 e-mails, carrega a oferta vigente e ganha urgência. O volume de campanhas já cobre o resto. \[P, WP e C1\]

Motivo (C1): com 2 a 3 campanhas por dia mais SMS, a pessoa que abandonou o carrinho recebe uma campanha poucas horas depois de qualquer jeito. Flow longo vira redundância.

| Flow | Versão BFCM | Templates no FG | Observação |
| --- | --- | --- | --- |
| Welcome | Destaca a oferta da janela e apresenta a marca em poucas linhas | 12 | 77% de quem converte o faz no dia zero. O primeiro e-mail carrega tudo \[P, C2\] |
| Abandono de site | Menciona a visita e destaca oferta e urgência | 9 |  |
| Abandono de navegação | 2 e-mails rápidos: o produto visto, quebra de objeção, oferta | 17 |  |
| Carrinho e checkout | Mesmos e-mails para os dois flows. Item deixado, oferta, urgência extrema | 20 | 2 e-mails bastam |
| Pós-compra | 1 a 2 e-mails: "seu pedido está sendo preparado" e "a oferta continua ativa". Depois a pessoa volta para as campanhas | 3 | Não segurar o comprador em sequência longa separada \[P, C1\] |

![Diagrama dos cinco flows em modo BFCM com gatilho, espera e e-mails de cada um](blob/69e53133-128f)

Tempos lidos do diagrama. A resolução do original é baixa, então os minutos exatos do carrinho são aproximados. \[P, WP\]

| Flow | Gatilho | Espera | E-mail 1 | Espera | E-mail 2 |
| --- | --- | --- | --- | --- | --- |
| Welcome | Entra na lista | Imediato | Explica o desconto e a marca |  |  |
| Abandono de site | Ativo no site | 45 minutos | Menciona a visita e a oferta da Black |  |  |
| Abandono de navegação | Viu um produto | 30 minutos | Cutucada com a informação do desconto | cerca de 2 horas | Urgência: melhor oferta do ano, mais recomendados |
| Carrinho e checkout | Iniciou o checkout | 20 a 30 minutos | Cutucada com a informação do desconto | cerca de 2 horas | Urgência: melhor oferta do ano, mais recomendados |
| Pós-compra | Fez o pedido | Imediato | Texto puro: obrigado e "adicione ao seu pedido agora" |  |  |

Fora da BFCM esses flows costumam ter esperas de horas ou dias e 3 a 4 e-mails. No modo BFCM tudo acontece no mesmo dia.

![Exemplos reais de e-mails de flow em modo Black Friday: welcome da Forest Ink, abandono de navegação da Breatheeze, carrinho abandonado da UDX e pós-compra da Jack Henry](blob/a249369e-159c)

O que cada exemplo faz:

| Flow | Marca | Hero | Oferta | Detalhe que vale copiar |
| --- | --- | --- | --- | --- |
| Welcome | Forest Ink | "Black Friday Sale. It's happening. Right now. Buy one get one 50% off sitewide" | BOGO 50%, código BF50 | A oferta vem antes da apresentação da marca. Prazo explícito: "live until November 30th" |
| Navegação | Breatheeze | "Checking out our nasal strips?" | Até 60% off, brindes de US$ 80 ou mais, produto inédito grátis | Três benefícios em lista com marcador, bloco dinâmico do produto visto, depois um bloco curto de como o produto funciona |
| Carrinho | UDX | "Your item is ready for checkout. Get it today for 25% off" | 25% por tempo limitado, mais leve 1 e ganhe 1 em acessórios | Usa a lógica do "pronto para envio". Abaixo, reviews de clientes e repetição da oferta no fim |
| Pós-compra | Jack Henry | Texto puro do fundador, e depois "Black Friday Sale is still live... but not for long" | 30% sitewide, frete grátis acima de US$ 60 | Agradece, avisa que o pedido está sendo preparado e pergunta "por que parar agora?". Sugere comprar mais para si ou presentear |

### O pós-compra vende

E-mail de texto puro do fundador, imediato, agradecendo e empurrando um segundo pedido para adiantar presentes. "Você se surpreenderia com quanta gente compra por aqui." \[P, WP\]

### Timing de recompra por categoria

| Categoria | Onde está a recompra | Implicação |
| --- | --- | --- |
| Vestuário, acessórios, beleza, fragrância | Primeiros 14 dias, depois cai forte | Não excluir comprador recente das campanhas |
| Consumíveis e suplementos | Espalhada em 30 dias, pico perto do dia 30, metade até o dia 35 | Não presumir que "30 dias de produto" significa silêncio por 30 dias |

Cuidado de atribuição: troca de tamanho (reembolso mais novo pedido) aparece como recompra rápida. A Wellcopy filtra isso e a tendência se mantém. \[P, C1\]

### Pop-ups

- Não desligar. O período é o de maior tráfego do ano e a maior chance de crescer lista. \[P, WP\]
- Um pop-up por janela: Early Access, BF, CM, Presentes. Oferta, prazo e urgência batendo com a campanha.
- Pedir e-mail e telefone. A pessoa não precisa se cadastrar para ter a oferta, mas muitas se cadastram, e aí recebem lembrete diário.
- Pop-up de SMS para quem já é inscrito só de e-mail, disparando perto de 50 segundos de sessão. \[P, C2\]
- Em vez de welcome por landing page, usar pop-up com quiz e adaptar os 1 a 2 primeiros e-mails à resposta. \[P, C2\]

![Quatro exemplos de pop-up de campanha: acesso a coleção de Dia das Mães, 20% off de Black Friday com pergunta de primeira compra, Black Friday com desconto e brindes, raspadinha de 4 de julho](blob/e109e890-ae4a)

Padrões nos quatro exemplos: o nome do evento no topo, a oferta em destaque, um único campo (e-mail) e um botão com verbo de resgate ("Get the deals", "Claim offer"). Dois usam mecânica de engajamento: pergunta de segmentação ("primeira vez na marca?") e raspadinha. A pergunta de segmentação é o mesmo princípio do pop-up com quiz citado acima. \[P, WP\]

### Flow extra: "Espresso Shot"

Gatilho por segmento: ativo no site 3 vezes ou mais em 30 dias, zero pedidos em 30 dias, clicou em e-mail ou SMS ao menos uma vez. Dispara 15 minutos após a entrada no segmento, com oferta de 2 horas. Rendeu US$ 115 mil em um trimestre para uma marca, só por SMS. \[P, C2\]

Na Omnisend, a montagem depende de segmento com gatilho de entrada. Testar viabilidade antes de prometer. \[I\]

## 8. Playbook de SMS e MMS

Comece a coletar telefone agora, mesmo em clientes que ainda não enviam SMS: não dá para coletar retroativamente, e 5.000 números na BF são uma alavanca real. \[P, C2\]

### 8.1 Captação

- Enquadramento do passo de SMS no pop-up: **"Finish signing up with text to activate your discount."** Em português: "Finalize o cadastro por SMS para ativar seu desconto". Funciona por viés de compromisso: quem já deu o e-mail tende a concluir.
- O texto padrão ("receba novidades exclusivas por SMS") soa como caridade. Ninguém quer isso.
- Não dar desconto maior para SMS (10% no e-mail e 15% no SMS). Piora o resultado: a pessoa para no e-mail, e os flows ficam com dois descontos diferentes.

### 8.2 Compliance por mercado

| Regra | Detalhe | Mercado | Nível |
| --- | --- | --- | --- |
| Horário de silêncio | Proibido enviar antes das 8h e depois das 21h no horário local do destinatário. Escritórios caçam consumidores para processar, acordos de até US$ 20.000 | EUA | P, V |
| Campanha por fuso | Sempre enviar no horário local do destinatário. 19h na costa oeste são 22h na leste, ilegal | EUA | P |
| Flows | Horário de silêncio ligado na plataforma. Não mexer | EUA | P |
| Zona cinzenta | Quem mudou de estado e manteve o DDD. A plataforma usa o DDD para o fuso | EUA | P |
| Um SMS por abandono | Um único SMS em até 48h do abandono. Attentive e Postscript travam isso na plataforma. O Max atribui ao TCPA. Pelo que conheço, a origem são as diretrizes da CTIA | EUA | V |
| Segundo toque | Flow separado, disparado por segmento "abandonou há mais de 24h e não comprou". Legalmente ambíguo | EUA | P |
| Responsabilidade | Mesmo a pedido do cliente, a agência pode responder. O Max passou a colocar cláusula em contrato | EUA | P |
| Consentimento | Opt-in expresso e específico para SMS (GDPR e ePrivacy na UE, LGPD no BR) | UE, BR | V |

Sugestão direta: cláusula equivalente nos contratos da Convertfy para clientes com base nos EUA. \[I\]

### 8.3 Flows de SMS

Os oito flows básicos: welcome, abandono de site, de navegação, de carrinho, de checkout, pós-compra, reposição e winback. A maioria das marcas só roda os de pré-compra e deixa dinheiro nos três últimos. \[P, C2\]

| Flow | Estrutura | Dado |
| --- | --- | --- |
| Welcome | SMS 1, dia 1: código e boas-vindas. SMS 2, dia 2 a 3: marca e desconto expirando. SMS 3, dia 4 a 5: última chance. Marcas agressivas: um por dia | 77% convertem no dia zero |
| Crédito de loja | 2 a 3 semanas após o opt-in sem compra. Valor quebrado: "Você tem US$ 13,47 de crédito" | Uma das melhores mensagens da sequência de welcome |
| Abandono | Um SMS. Compradores e não compradores em ramos separados | Ver 8.4 |
| Pós-compra | Dia 2: upsell ou cross-sell. Dia 8: dica de uso com cross-sell. Dia 21: upsell ou cross-sell | 50% dos segundos pedidos vêm antes do dia 21 |
| Winback | Perto do dia 90. Nada de "sentimos sua falta". A oferta mais forte, sem cerimônia |  |

Montagem: não fazer divisão condicional "assinante de SMS recebe só SMS". Se o abandono acontece às 21h e o SMS é barrado, a pessoa não recebe nada. Rodar em paralelo: todo mundo recebe o e-mail, e quem tem SMS recebe também, cinco minutos depois. \[P, C2\]

### 8.4 Copy de SMS

- Parar de usar "esqueceu alguma coisa?". A frase sugere que a pessoa abandonou de propósito.
- Usar **"Your order is ready to ship"** ("Seu pedido está pronto para envio"): +50% em cliques e em performance geral. O princípio é parecer que algo já está em andamento. Vale também para assunto de e-mail. \[P, C2\]
- Produto sob encomenda (joia personalizada, ticket perto de US$ 200): "Reservamos sua pedra pelas próximas 24 horas", "Seu pedido está pronto para ser personalizado", "Separamos isso para você". Útil para os clientes de joias. \[P, C2\]
- Não compradores: incluir o desconto de boas-vindas no SMS de abandono. Compradores: "Bem-vindo de volta, encontrou o que precisava?". Uma das mudanças de maior alavancagem. \[P, C2\]
- BFCM: dizer a oferta, colocar urgência e dizer como resgatar. Nada além. \[P, WP\]
- Evitar emoji. Ele muda a codificação e reduz o limite de caracteres por segmento, o que pode dobrar o custo. \[P, C2; detalhe técnico V\]
- "Restock" (voltou ao estoque) é uma das palavras de melhor desempenho em SMS. \[P, C2\]

![Seis exemplos reais de SMS e MMS de fim de ano: Michaels, Paper Source, Casely, Elemis, Venus e Dr. Martens](blob/d561a5cb-9eb8)

Transcrição dos exemplos e o que cada um ensina:

| Marca | Tipo | Texto | Estrutura |
| --- | --- | --- | --- |
| Paper Source | SMS | "Limited Time! BOGO 50% OFF Toys & Games in stores! Or, shop from home and take 25% off $75+ sitewide." | Urgência, oferta 1, oferta 2 com valor mínimo, link |
| Casely | SMS | "Hey! This case would look great on your phone! Get it right now for 50% OFF during our BIGGEST Sale of the Year! Shop Now >>" | Abertura pessoal, oferta, "maior promoção do ano", CTA |
| Elemis | MMS | "Surprise! Black Friday is BACK for 24 hours only. Enjoy 35% off & the gift of your choice with code 24HOURS >>" | Surpresa, prazo de 24h, % mais brinde, código que repete o prazo |
| Venus | MMS | "Surprise! Secret Santa has a Special Treat for You! Hurry the Treat exp 12/7." | Oferta misteriosa, data de validade |
| Michaels | SMS | "These creative gifts will make them do that Christmas-morning happy dance" | Presente, sem desconto |
| Dr. Martens | MMS | "Get an iconic pair she can put her own personal spin on. Shop gifts for her:" | Guia de presente por pessoa, imagem "Gifts for her" |

Todos começam com o nome da marca seguido de dois pontos, têm um único link e cabem em um ou dois segmentos. Os três MMS usam a imagem para mostrar a oferta ou o produto, como o Max recomenda.

### 8.4.1 Modelos de SMS por momento

Modelos para adaptar. Trocar os colchetes. Versão PT para WhatsApp e SMS no BR, versão EN para SMS nos EUA e UK. Sem emoji.

| Momento | PT | EN |
| --- | --- | --- |
| Abertura de oferta | "\[Marca\]: começou. \[Oferta\] no site todo até \[dia\] às \[hora\]. \[link\]" | "\[Brand\]: It's live. \[Offer\] sitewide until \[day\]. \[link\]" |
| Early Access | "\[Marca\]: seu acesso antecipado à Black está liberado. Só para a lista, até \[dia\]. \[link\]" | "\[Brand\]: Your early access is unlocked. List only, ends \[day\]. \[link\]" |
| Últimas horas | "\[Marca\]: últimas horas. \[Oferta\] termina hoje às 23h59. \[link\]" | "\[Brand\]: Final hours. \[Offer\] ends tonight at midnight. \[link\]" |
| Abandono, não comprador | "\[Marca\]: seu pedido está pronto para envio. Finalize com \[X\]% usando \[CÓDIGO\]. \[link\]" | "\[Brand\]: Your order is ready to ship. Complete it with \[X\]% off, code \[CODE\]. \[link\]" |
| Abandono, comprador | "\[Marca\]: bem-vindo de volta. Encontrou o que precisava? Seu carrinho está salvo. \[link\]" | "\[Brand\]: Welcome back. Did you find what you need? Your cart is saved. \[link\]" |
| Sob encomenda | "\[Marca\]: separamos sua peça pelas próximas 24 horas. \[link\]" | "\[Brand\]: We've reserved your piece for the next 24 hours. \[link\]" |
| Crédito de loja | "\[Marca\]: você tem R$ 13,47 de crédito. Vale até \[dia\]. \[link\]" | "\[Brand\]: You have $13.47 in store credit. Expires \[day\]. \[link\]" |
| Prazo de entrega | "\[Marca\]: último dia para receber antes do Natal. Peça até as \[hora\]. \[link\]" | "\[Brand\]: Last day for delivery by Christmas. Order by \[time\]. \[link\]" |
| Volta ao estoque | "\[Marca\]: \[produto\] voltou ao estoque. Da última vez acabou em \[N\] dias. \[link\]" | "\[Brand\]: \[Product\] restock is here. \[link\]" |

### 8.5 MMS

A pergunta certa é lucro bruto, não ROI. No teste do Max, o MMS teve ROI pior (3x o custo, 2x a receita) e lucro bruto maior: US$ 658 contra US$ 309. No segundo teste, mostrar o brinde na imagem rendeu US$ 2.000 contra US$ 534, por cerca de US$ 200 a mais de custo. \[P, C2\]

Quando usar: welcome (um infográfico do produto), lançamento de produto (sempre), bundle e BOGO (mostra o que a pessoa leva), uma imagem de marca de vez em quando, infográfico educativo no máximo uma vez por mês. Regra geral: cerca de 25% dos envios em MMS, raro em campanha, 1 a 2 no welcome.

### 8.6 Frequência fora de pico

| Tipo de marca | Frequência |
| --- | --- |
| Assinatura | Pode ser diária até o primeiro pedido. Depois recua |
| Reposição de alta frequência | 1 a 2 por dia se houver novidade real. Senão, 2 por semana |
| Maioria | Mínimo de 1 por semana, sempre. Parar de enviar fora de temporada derruba a entrega quando o pico volta |

Melhor tipo de campanha: oferta exclusiva de SMS uma vez por mês. Sem pauta: destaque de mais vendido ou volta ao estoque. Fonte de inspiração citada: biblioteca de SMS da Attentive. \[P, C2\]

## 9. Diretrizes de copy e design para produção

E-mail de BFCM é oferta na frente, pouco texto e um CTA. Não é hora de storytelling: as pessoas estão ali pela oferta. \[P, WP\]

### 9.1 E-mail gráfico

- A oferta é o hero. Título grande com a oferta, copy mínima, o design é a mensagem.
- Um CTA grande, de alto contraste, acima da dobra.
- Pouco conteúdo. E-mail longo atrasa produção numa fase em que o time já está no limite.
- Urgência em todo lugar: faixa, timer, assunto, CTA.
- Abaixo do hero, no máximo alguns produtos em destaque.

![Seis e-mails gráficos reais de Black Friday: dois da Dr. Squatch, Nightcity, Renuherbs, uma marca de moissanita e Bite](blob/2e3fea4a-926b)

Anatomia de cada exemplo, de cima para baixo:

| Marca | Faixa do topo | Hero | Subtexto | Blocos abaixo | Mecânica |
| --- | --- | --- | --- | --- | --- |
| Dr. Squatch, abertura | "Black Friday starts now" | "Up to 55% off sitewide" | "Add some Squatch stuff to your cart and watch the savings stack up" | Selo "Buy more, save more", foto de produtos, segundo bloco com edição limitada | Até X% com desconto progressivo no carrinho |
| Dr. Squatch, fechamento | Selo "Ends tonight" | "Get up to 55% off" | "The more you add to your cart, the better the deals get. No code needed" | Três faixas: frete grátis acima de US$ 40, 20% acima de US$ 55, 35% acima de US$ 70 marcado como "best deal" | Níveis por gasto, sem código |
| Nightcity | Logo | "Black Friday is live" | "Save up to 35% off and enjoy free shipping sitewide to guarantee Christmas deliveries" | "Bestsellers worth the hype": mínimo de 25%, 30% acima de US$ 150, 35% acima de US$ 250. Dois cartões: feminino e masculino | Níveis por gasto mais frete grátis e garantia de entrega no Natal |
| Renuherbs | Logo | "Time's running out" | "There are just three ways to save before midnight" | Três caixas: gaste US$ 149 e ganhe brinde, gaste US$ 299 e ganhe brinde mais surpresa, até 50% em selecionados. Faixa cruzada "25% off sitewide until midnight". Grid de 4 produtos. Fecho: "Tomorrow it's back to full price" | Brinde por nível de gasto mais % sitewide, com prazo de meia-noite |
| Ice Cartel (moissanita) | "VIP Black Friday is live" | "Up to 70% off" mais "Free Cuban chain" | "Beat the rush and lock in your drip before it sells out" | CTA "Shop early access". Quatro ícones: passa no teste de diamante, frete em 4 dias, compre agora e pague depois, estoque limitado. Lista de 5 produtos com selo "ships today" | Early Access VIP com brinde empilhado. Referência direta para clientes de joias |
| Bite | Logo e slogan | "30% off" | "Need another reason to shop Black Friday with us? Here are 3" | Lista numerada de 3 motivos | % simples com três razões curtas |

O que os seis têm em comum: o número da oferta é o maior elemento da tela, o prazo aparece no topo ou em selo, há no máximo uma frase de apoio, e o CTA vem antes de qualquer produto.

### 9.1.1 Esqueleto padrão de e-mail gráfico de BFCM

1. Faixa de topo com o evento e o prazo: "Black Friday começou", "Termina hoje".
2. Hero com o número da oferta como maior elemento.
3. Uma frase de apoio: como funciona ou como resgatar.
4. CTA único, alto contraste.
5. Faixa marquee repetindo a oferta.
6. Um bloco de conteúdo: níveis de gasto, grid de 4 a 6 produtos, ou 3 benefícios em ícone.
7. CTA repetido.
8. Rodapé com categorias.

Para a Convertfy o esqueleto é aplicado em layout neutro, fundo branco e texto preto. O contraste do hero vem do tamanho da tipografia, não de paleta.

### 9.2 Blocos mais frequentes nas 116 campanhas do FG

Contagem por palavra-chave em wireframes anonimizados. Os percentuais são piso, não valor exato. \[D, leitura nossa do FG\]

| Bloco | Presença | Uso |
| --- | --- | --- |
| Faixa marquee repetindo a oferta ("20% OFF SITEWIDE!!", "LAST CHANCE", "VIP PASS", "24 HOURS ONLY!") | 49% | Divisor entre hero e corpo. Reforça a oferta sem pedir leitura |
| Cupom com código visível | 30% | Bloco próprio "USE CODE: XXXX". 2 templates usam "sem código" |
| Grid de produtos (2 ou mais) | 25% | Abaixo do hero, com selo de % por produto |
| "Sitewide" ou "Everything" | 19% | Hero da BF |
| Timer ou "hours remain" | 14% | Fechamentos |
| Níveis por gasto | 9% | Janela de Presentes |
| Review ou depoimento | 6% | Rodapé de prova |
| Mock de iMessage | 2 templates | Hero que simula uma mensagem pessoal |
| Calendário com datas marcadas | 2 templates | Prazos de entrega e janela 26 a 28/11 |
| "Seu checkout pode ficar assim" (recibo simulado) | 1 template | Mostra a economia em valores |

Altura mediana de 2.806 px em 600 de largura, com mediana de 2 CTAs. Na prática: hero, faixa, um bloco de produtos ou benefícios, CTA final.

Para e-mail de flow, a mediana cai para cerca de 2.200 px em carrinho e checkout. O welcome é o mais longo, perto de 3.500 px.

Restrição de produção da Convertfy: o layout final segue o padrão neutro (fundo branco, texto preto). Os wireframes do FG entram como estrutura de blocos, não como paleta.

### 9.3 E-mail de texto puro

Alguns dos e-mails de melhor desempenho em Q4 são texto simples. Parecem mensagem 1 a 1, se destacam numa caixa cheia de banner e saem rápido. Um exemplo do WP mostra marca com mais de 50% dos envios em texto. \[P, WP\]

![Galeria de envios de uma marca em Q4: mais da metade dos e-mails é texto puro, intercalados com e-mails gráficos de oferta](blob/d0d69fc9-a64e)

Na galeria, os e-mails gráficos aparecem nos lançamentos e fechamentos de oferta, e os de texto puro preenchem os dias do meio. Esse é um bom padrão de divisão de esforço de produção: design para abrir e fechar a janela, texto para sustentar a frequência.

Regras: assinar como fundador ou alguém do time, negrito na oferta e nas informações importantes, um único CTA.

Os seis esqueletos prontos no FG:

| Esqueleto | Estrutura |
| --- | --- |
| Fundador, carrinho abandonado | Saudação. "Eu sei como é \[problema\]". "E se houvesse um jeito melhor de \[resultado\], sem \[dor\], sem \[dor\]". Produto e como funciona em uma frase. Prova. Oferta ativa e o que a pessoa leva. Bônus. CTA. Comparação de preço opcional. Garantia. CTA. Assinatura |
| Time, carrinho abandonado | "Vimos que você deixou itens". A oferta não dura para sempre. Lista: % off, brinde, bônus de fidelidade, outro benefício, suporte por resposta. Urgência. Código. CTA |
| Welcome ou navegação | "Que bom que você está conhecendo \[marca\]". Uma frase do que a marca vende. "\[Evento\] está ativo agora". Lista do que leva. Código. CTA. Urgência curta. Oferta de ajuda |
| Pós-compra, time | Obrigado pela compra durante \[evento\]. Pedido sendo preparado. "Enquanto espera, \[oferta\] continua ativa". Código. CTA. Exclusões e validade |
| Pós-compra, fundador | Obrigado pelo primeiro pedido. A coisa número 1 que o cliente novo precisa saber sobre o uso. Link para o guia. Oferta ainda ativa até \[data\]. CTA. P.S. com review de cliente |
| Genérico | Saudação e corpo livre |

Esses esqueletos batem com a preferência da casa: copy curta, realista, sem storytelling forçado.

### 9.3.1 Modelo de campanha em texto puro, em PT

Modelo para os dias do meio de uma janela. Adaptar os colchetes. Máximo de 120 palavras.

```markdown
Assunto: [Oferta] termina [dia]
Pré-cabeçalho: Vale para o site todo, sem código.

Oi, [nome].

Passando rápido para avisar: **[oferta] vale até [dia] às [hora]**.

O que entra:
- **[X]% off** em [site todo ou categoria]
- **[Brinde]** em pedidos acima de R$ [valor]
- **Frete grátis** acima de R$ [valor]

O desconto já aparece no carrinho.

[Ver as ofertas]

Qualquer dúvida, é só responder este e-mail.

[Nome], da [Marca]
```

### 9.4 Assuntos e linhas que carregam dado

| Linha | Onde usar | Origem |
| --- | --- | --- |
| "Offer of the year" ("a oferta do ano") | Só na BF. Melhor linha de conversão para a oferta grande segundo o Max | P, C1 |
| "Your order is ready to ship" | Abandono, e-mail e SMS. +50% em cliques | P, C2 |
| "VIP Early Access: Black Friday unlocked" | Abertura do Early Access | D, TT (MeUndies, 18/11/2025) |
| "Hey there, can you keep a secret?" | Dia da BF, tom pessoal | D, TT (MeUndies, 27/11/2025) |
| "50% Off Sitewide" e a variação com numerais em emoji | Mesma oferta, reenvio com assunto novo | D, TT (MeUndies, 15 e 20/11/2025) |
| "Start Your Carts!" | 24 a 48h antes de abrir a venda | D, TT (Brooklinen) |
| "Your $5 Expires Tonight" | Crédito com prazo | D, TT (Ridge) |
| "Late to the Black Friday party? We kept the door open" | Extensão | D, FG |
| "Cyber Monday ends tonight", "Early access ends soon", "48 hours left for standard shipping" | Fechamentos | D, FG |

### 9.5 Checklist por e-mail

- [ ] A oferta se entende em três segundos
- [ ] Um CTA acima da dobra
- [ ] Urgência no assunto, no hero e no CTA
- [ ] Prazo explícito, com data e hora
- [ ] Como resgatar: código visível ou "desconto aplicado no carrinho"
- [ ] Versão de reenvio com assunto e pré-cabeçalho novos
- [ ] Sem travessão na copy
- [ ] Para BR: preço "de" real e verificável

### 9.6 Catálogo de templates do Figma, com link para o frame

O arquivo do Max tem 177 wireframes. Esta tabela indica os mais úteis por momento da campanha. Cada link abre o frame exato no Figma. As imagens não puderam ser exportadas para este documento porque o ambiente bloqueia o download direto do Figma.

| Momento | Template | O que tem | Link |
| --- | --- | --- | --- |
| Abertura de BF | Hero "Up to XX% off site-wide" com 4 produtos e selo de % | Número gigante repetido, CTA, grid vertical | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-10081) |
| Abertura de BF | "XX% off everything, no code needed" com 6 produtos | Marquee "20% off sitewide!!" em cima e embaixo | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-11922) |
| Abertura de BF | Marquee "Black Friday Sale!" com 3 níveis de % | Níveis lado a lado | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-11985) |
| Early Access | "VIP Pass" | Faixa VIP, título, lista de benefícios | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-10401) |
| Early Access | "Early Black Friday Sale" | Marquee de early sale, blocos de mensagem | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-11315) |
| Early Access | "And you've got early access" | CTA "Shop early Black Friday" | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-21262) |
| Early Access | "Use code: EARLY40" | Código de acesso antecipado em destaque | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-24984) |
| Early Access, fechamento | "Early access ends soon! 50% off" | Urgência de fechamento da janela | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-19307) |
| Urgência | "XX hours remain" | Contador de horas como hero | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-11727) |
| Urgência | Cupom com timer 00:00:00 | "Use code at checkout" e contador | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-10269) |
| Urgência | "24 hours only!" | Marquee de 24h e grid de 4 produtos. Serve para o 11.11 | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-10309) |
| Urgência | "Ends at midnight!" | Marquee de meia-noite | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-25057) |
| Fechamento | "25% off, last chance" | Marquee de última chance | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-19582) |
| Fechamento | "Your final hours to save up to 50% off. BOGO deals + new drops" | Oferta empilhada com drops | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-21414) |
| Extensão | "Late to the Black Friday party? We kept the door open" | Texto curto, categorias de produto | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-21636) |
| Cyber Monday | "Cyber Monday ends tonight" | Fechamento da CM | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-22598) |
| Fechamento | "This rodeo is drawing to a close" | Fechamento com tom de marca | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-22378) |
| Calendário | Datas 26, 27 e 28 de novembro marcadas | Mostra a janela da oferta em calendário | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-20167) |
| Prazo de entrega | "48 hours left for standard shipping" | Contagem para a data limite | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-23340) |
| Prazo de entrega | Calendário de dezembro com datas limite | Dias 10 a 24 marcados | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-23910) |
| Prova de economia | "Your checkout could look like this" | Recibo simulado com item, preço e total | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-24866) |
| Tom pessoal | Hero com mock de iMessage | Simula mensagem 1 a 1 com a oferta | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-10439) |
| Desconto em valor | "$X off" por produto | 3 produtos com valor fixo de desconto. Serve para o Kickoff | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=79-10804) |
| Flow, welcome | "Shop early access" | Welcome em modo Early Access | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-3535) |
| Flow, welcome | Welcome com BOGO, teste A/B de assinatura | Variante de welcome com oferta BOGO | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-2563) |
| Flow, site | "Don't forget you still have 20% off your first purchase" | Código, frete grátis acima de US$ 75, prova social em números | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-8450) |
| Flow, navegação | "Pick up where you left off and enjoy our Black Friday Sale", código BF50 | Bloco dinâmico do produto visto | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-7711) |
| Flow, navegação | "Your order is expiring" | Urgência com bloco dinâmico | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-9479) |
| Flow, carrinho | "Finish my order" com frete grátis mundial, garantia de 12 meses, combine qualquer relógio | Benefícios em ícone. Referência direta para clientes de relógio | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-1716) |
| Flow, carrinho | "10% off Cyber Monday Sale, free gift with every order" | Faixa de CM no topo do e-mail de carrinho | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-2032) |
| Flow, carrinho, texto | Fundador: problema, solução, prova, oferta, garantia | Esqueleto 1 da seção 9.3 | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-2028) |
| Flow, carrinho, texto | Time: lista do que a pessoa leva, código, urgência | Esqueleto 2 da seção 9.3 | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-2030) |
| Flow, welcome ou navegação, texto | "Our sale is live right now" | Esqueleto 3 da seção 9.3 | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-8266) |
| Flow, pós-compra, texto | "While you wait, the sale is still live" | Esqueleto 4 da seção 9.3 | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-2682) |
| Flow, pós-compra, texto | Fundador com dica de uso e P.S. de review | Esqueleto 5 da seção 9.3 | [abrir](https://www.figma.com/design/khyIZcAy2eDOk1pjnCsONb/?node-id=118-9630) |

## 10. Referências de mercado

As marcas que mais cresceram em 2025 fizeram quatro coisas em comum: cadência alta o ano todo, uma oferta simples e memorável, abertura do pico por acesso antecipado e oferta rotativa por semanas. \[I, cruzando TT e WP\]

### 10.1 Calendários de 2025

| Marca | Nicho | O que fez | Fonte |
| --- | --- | --- | --- |
| MeUndies | Underwear, EUA | 15/11 "50% Off Sitewide". 18/11 "VIP Early Access". 20/11 reforço da mesma oferta. 27/11 tom pessoal. 09/12 drop de produto no lugar de desconto | TT |
| Gymshark | Activewear, UK | 09 a 15/11 acesso ao anúncio, remarcações até 50%. 16 a 27/11 early access, até 50% em tudo. Níveis de oferta por período | WP |
| Cuts Clothing | Moda masculina, EUA | 31/10 a 27/11 "Early Early BF" até 60% com drops semanais de cores e produtos. Sitewide por cerca de 3 meses | WP |
| Create Wellness | Suplementos | 24 a 26/11 early access a bundles e brinde misterioso acima de US$ 100. 27/11 a 03/12 remarcação sitewide | WP |
| IM8 | Suplementos | 19/11 a 01/12 quatro produtos bônus (US$ 118) na assinatura, mudando a mensagem ao longo do período. Bônus no lugar de desconto | WP |
| AG1 | Assinatura | 27/11 a 01/12 e-mails em texto com preço especial só no primeiro envio da assinatura | WP |
| Shopify | Plataforma | Anúncios de BF de 15/09 a 30/11/2025. Um criativo com alcance de 29 milhões | TT |

### 10.2 Correspondência com a carteira da Convertfy

| Referência | Clientes parecidos | O que copiar |
| --- | --- | --- |
| MeUndies | Underwear e meias | Oferta única sitewide, VIP 9 dias antes, drop em dezembro |
| Cuts, True Classic | Moda masculina premium | Drops semanais como motivo de abertura. Sitewide em datas âncora |
| Gymshark | Moda e streetwear | Níveis de oferta por período. Frete grátis com mínimo fora de pico |
| Ridge | Relógios, acessórios, produto único | Cadência alta por ângulo de produto. Crédito com prazo |
| IM8, Create | Skincare, bem-estar, margem curta | Bônus e bundle no lugar de % |
| Sallve, Insider | Clientes BR | Brinde na compra, frete grátis, até 40% |
| Casos de joia sob encomenda (C2) | Joias e moissanita | Copy de reserva: "separamos sua peça por 24h" |

### 10.3 Dois arquétipos

Marca de desconto (MeUndies, Brooklinen, True Classic, Cuts) ancora em % sitewide agressivo. Marca de ângulo (Ridge, Huel, Gymshark, IM8) sustenta cadência com produto e conteúdo, e usa bônus. Classificar cada cliente antes de montar o calendário define o cardápio da seção 4. \[I\]

### 10.4 O que ainda não foi possível ver

O Trendtrack só reteve nov/2025 completo para MeUndies. Para reconstruir funil de anúncios e página de BF das outras marcas, as fontes são Milled, Meta Ad Library e o histórico do próprio Trendtrack com marca no Brandtracker a partir de agora. \[lacuna\]

## 11. Brasil x Global

O material do Max é todo de EUA. A estrutura de janelas vale para os dois mercados. Mudam a mecânica da oferta, o canal de urgência, as datas e as regras.

| Tema | Global (EUA, UK, UE) | Brasil |
| --- | --- | --- |
| Oferta central | % sitewide, níveis por gasto, BOGO | Frete grátis e brinde pesam tanto quanto o %. Parcelamento e Pix com desconto na copy \[D, TT\] |
| 11.11 | Data fraca nos EUA (Veterans Day). Funciona como pico do Kickoff | Data já conhecida por Shopee, AliExpress e Mercado Livre \[V para participação\] |
| Canal de urgência | SMS, com MMS em lançamentos | WhatsApp e push. SMS com papel menor \[V\] |
| Horário de SMS | 8h às 21h locais nos EUA. Alguns estados são mais restritos \[V\] | Sem regra equivalente conhecida. Seguir bom senso e LGPD \[V\] |
| Preço riscado | UE: referência é o menor preço dos últimos 30 dias (Omnibus) \[V\] | "Metade do dobro" é alvo de Procon e CDC. Guardar histórico de preço |
| Sorteio de reembolso | EUA: exige entrada sem compra | Exige autorização prévia. Não rodar sem jurídico \[V\] |
| Consentimento | TCPA (EUA), GDPR e ePrivacy (UE) | LGPD |
| Prazos de entrega | 15, 19 e 21/12 nos EUA | Definir por transportadora. Dropshipping internacional: prazo real bem antes de dezembro |
| Datas extras | Thanksgiving 26/11, Small Business Saturday 28/11, Boxing Day 26/12 | Dia das Crianças 12/10, 13º salário até 30/11 e 20/12 |
| Desconfiança | Menor | "Black Fraude" é tema recorrente. Preço real, prazo real e prova social na copy |

### Dropshipping com prazo longo

Para lojas com entrega de 10 a 20 dias, a janela de Presentes (04 a 14/12) só funciona se o prazo for comunicado com honestidade. A janela de prazo de entrega acontece mais cedo, e a virada para vale-presente digital começa antes de 15/12. Prometer Natal sem conseguir entregar gera chargeback, que já é problema em contas da carteira. \[I\]

## 12. Pós-BFCM: recuperação de lucro em Q1

A coorte de BFCM é a pior do ano: adquirida com o CPM mais caro, no maior desconto, e recompra 30 a 50% menos que as outras. O lucro do trimestre se decide entre janeiro e março. \[D, WP\]

Por que ela é fraca: veio pelo preço e não pela marca. Metade comprou presente, e quem usa o produto não está na lista. Comprou fora do ciclo normal. Por padrão, compra uma vez só.

| Período | Ação | Oferta |
| --- | --- | --- |
| Janeiro | Série de conteúdo só para a coorte de BFCM: história do fundador, como o produto é feito, que problema resolve, resultados de clientes. São cerca de 60 dias antes de a pessoa esquecer a marca | Nenhuma. Objetivo é converter a preço cheio e recuperar a margem |
| Fevereiro e março | Dividir a coorte. Quem recomprou a preço cheio vai para o ciclo normal. Quem não comprou desde novembro recebe oferta forte, parecida com a da BF | Forte. O cliente já está pago, segundo pedido com desconto é aceitável |
| Fevereiro | Calcular o CAC real da BFCM. Antes disso as devoluções não assentaram. Algumas marcas têm dias de receita negativa em janeiro |  |
| O ano todo | Marcar os compradores de Q4 e incluir na lista de inclusão da BFCM de 2027, mesmo que não recomprem em Q1 |  |

![Diagrama do playbook de winback de Q1: comprador de BFCM entra em janeiro na série de marca sem desconto, em fevereiro e março a coorte é dividida entre quem recomprou e quem recebe oferta forte, com linha do tempo de devoluções até fevereiro](blob/8b1b4d1d-59fe)

Como ler: o comprador de novembro entra em janeiro numa série com quatro temas (história do fundador, processo do produto, resultados de clientes, por que importa), sem desconto. Em fevereiro e março a pergunta é "comprou de novo?". Sim: cliente real, vai para o ciclo normal. Não: oferta forte de winback, parecida com a da BF. A faixa de baixo mostra que as devoluções começam em dezembro, atingem o pico em janeiro e assentam em fevereiro, quando o CAC real pode ser calculado. \[P, WP\]

Nota de coerência: a série de janeiro é conteúdo de marca. Deve ser curta e concreta (processo, prova, uso do produto), sem narrativa elaborada. \[I\]

Isso amplia o escopo do projeto: o calendário da Convertfy deveria cobrir de outubro a março, não parar em dezembro. \[I\]

## 13. Conflitos entre fontes e decisão proposta

Onde as fontes discordam, ou onde o material do Max bate de frente com a restrição de reputação, esta é a posição proposta.

| Tema | Posição A | Posição B | Decisão proposta | Evidência |
| --- | --- | --- | --- | --- |
| Intervalo 12 a 22/11 | Minha primeira pesquisa: conteúdo sem oferta para evitar fadiga | Max: nunca ficar sem oferta, rotacionar | Adotar rotação. Cauda do 11.11 até 16/11, Early Access a partir de 17/11 | MeUndies e Cuts rodaram oferta contínua. A minha era inferência |
| Início da BF | Sexta 27/11 | Quarta 25/11, até domingo | Quarta 25/11 | P, WP e C1 |
| Lista cheia | Pesquisa: expandir de 90 para 180 dias | Max: lista cheia em metade dos envios | Por nível de conta (6.3) | Dado do Max mede aberturas. Risco Omnisend é real |
| Inativos | Pesquisa: não reativar na BF | Max: incluir direto, sem aquecimento | Nível A sim, B só nos dois picos, C não | P contra risco de conta |
| Comprador recente | Pesquisa: suprimir de quem já comprou | Max: não excluir, recompra vem em 14 dias | Não excluir. Corrige a pesquisa | P com dado interno, C1 |
| Flow de carrinho | Prática comum: 3 a 4 e-mails | Max: 2 e-mails na BFCM | 2 e-mails, só para clientes que estão com 2 ou mais campanhas por dia. Os demais mantêm 3 | P, C1 |
| Oferta exclusiva de e-mail | Exclusividade gera valor para a lista | Max: oferta no site todo | Site todo, exceto Early Access | P, C1 |
| Desconto extra para SMS | Prática comum: 10% e-mail, 15% SMS | Max: não, piora resultado | Mesmo desconto | P, C2 |
| Taxa de abertura | Meta alta como sinal de saúde | Max: 50 a 60%. Acima de 70% é alcance perdido | Parar de reportar abertura alta como vitória. Reportar clique, receita por destinatário e spam | P, C1, e Apple MPP |
| Preço âncora inflado | Max recomenda | Procon, CDC, Omnibus | Não usar em BR e UE | Risco legal |
| Sorteio de reembolso | Max rodou mais de 50 vezes | Exigência legal no BR | Só clientes EUA, com entrada gratuita. BR só com jurídico | V |

O que no material do Max é opinião de operador sem número: frequência ideal, "descadastro tudo bem", texto puro performar melhor, reenvio. São plausíveis e vindos de contas grandes. Entram como hipótese a testar em 2 ou 3 clientes nível A antes de virar padrão.

## 14. Lacunas e próximos passos

A meta de 75% das decisões com base em dado ainda não foi atingida: a parte de oferta, cadência e SMS está bem coberta, e a parte de push, WhatsApp, Brasil e limiares de deliverability segue sem fonte conferida.

### 14.1 Dados internos que faltam

- [ ] Por cliente: idade do domínio de envio, tamanho da lista, frequência atual, spam no Postmaster. Fecha os níveis A, B e C
- [ ] Resultado da BF 2025 da carteira: receita por janela, por canal, campanha contra automação. É o dado mais valioso e é da própria Convertfy
- [ ] Desempenho do 11.11 de 2025 contra a BF de 2025 nos mesmos clientes. Responde se houve canibalização
- [ ] Margem e maior desconto sustentável por cliente
- [ ] Prazo real de entrega por cliente, para fixar as datas de corte
- [ ] Base com consentimento de SMS e de WhatsApp por cliente
- [ ] Limite de envio e histórico de revisão de cada conta Omnisend

### 14.2 Fontes externas a conferir

- [ ] Omnisend: relatório de BFCM e estatísticas de e-mail, SMS e push. É a fonte mais próxima da carteira
- [ ] Klaviyo, Shopify, Adobe e NRF: conferir na origem os números citados pelo WP
- [ ] Google e Yahoo (2024) e Microsoft (2025): limiares oficiais de remetente
- [ ] Braze, Airship, OneSignal: opt-in e clique de push, app e web
- [ ] Brasil: Neotrust Confi, NielsenIQ Ebit, ABComm, Opinion Box (WhatsApp), Zenvia (SMS)
- [ ] CTIA e TCPA: regra de um SMS por abandono e horários por estado
- [ ] Jurídico BR: sorteio de reembolso e regra de preço riscado

### 14.3 Material ainda a extrair da comunidade do Max

A lista de calls mostra pelo menos quatro aulas diretamente ligadas ao projeto e ainda não lidas: "BFCM 2026 Strategy" (13/08), "Offer Strategy Deep Dive" (20/08), "Live Campaign Calendar Build" (02/07) e "Campaign Calendars" (28/05). Também úteis: "Abandonment Flows" (01/05), "Post Purchase Strategy" (23/07), "Best Performing Emails" (09/03) e "Copy Strategy, Banger Angles" (04/06).

### 14.4 Entregáveis seguintes

1. Mapa mental no Figma a partir das seções 3 a 8 deste estudo.
2. Skill de planejamento: recebe o perfil do cliente (mercado, arquétipo, nível de conta, margem, canais) e devolve calendário, ofertas por janela e cadência.
3. Skill de copy de BFCM: usa a seção 9 (estrutura, esqueletos de texto puro, linhas com dado) e as regras de estilo da casa.
4. Planilha de classificação dos clientes: mercado, arquétipo, nível A, B ou C, canais ativos.
5. Extensão do calendário até março com o winback de Q1.

## 15. Caso interno: o 11.11 de 2025 da Convertfy

Em 2025 a Convertfy rodou o 11.11 como um evento de 14 dias e 16 e-mails: 3 de Halloween, 8 de aquecimento sem oferta e 5 disparos no dia 11/11 com 22% de desconto adicional para uma "lista selecionada". Segundo o Bruno, deu muito resultado. Os números ainda não estão neste documento. \[D interno, resultado a quantificar\]

Este é o único material do estudo que vem da própria carteira. Por isso, onde ele conflita com prática de operador \[P\] do Max, o caso interno pesa mais, desde que os números confirmem.

![Visão geral do board de planejamento do 11.11 de 2025 no Figma: coluna de outubro com 3 e-mails de Halloween, sequência de aquecimento de 02 a 10/11 e coluna do dia do evento com 5 disparos](blob/31c1a8b1-9647)

### 15.1 Linha do tempo de 2025

| Data | E-mail | Proposta e formato | Oferta |
| --- | --- | --- | --- |
| 29/10 | 01 Soft sell | Halloween. Texto ou carta de vendas com grid de produtos 2x2 no fim | Progressivo: 1 produto 10%, 2 produtos 15%, 3 ou mais 20% |
| 31/10 | 02 Catálogo | Banner com copy batendo na oferta e catálogo de 8 produtos | Mesmo progressivo. Linha de frete grátis só se a loja oferecer |
| 01/11 | 03 Texto puro | Gerente de relacionamento encerra a promoção e dá um presente. Assunto: "Última chance de Halloween + um presentinho especial pra você" | Cupom HALLOWEEN15, 15% |
| 02/11 | 01 Texto puro | CEO manda e-mail muito formal cancelando a promoção da gerente, adia tudo para o 11.11 e, como pedido de desculpa, coloca o contato na lista "ultra" selecionada | Sem oferta. Cria a lista selecionada |
| 03/11 | 02 Teaser | "Não compre nada até anunciarmos as promoções do 11.11" | Sem oferta |
| 05/11 | 03 Criação de desejo e seleção | Texto estruturado em 7 blocos. "Você está na lista. De graça." | Sem oferta |
| 06/11 | 04 Tangibilização e prova | Texto com lista de 5 a 7 produtos, estoque e prova social. Anuncia dia e hora do evento | Sem oferta |
| entre 07 e 08/11 | Híbrido: educação e bônus | Longo, duas partes com separador. Ensina algo e revela os bônus do evento | Sem oferta |
| 09/11 | 07 Nós x Eles | Tabela comparativa quebrando as 5 principais objeções | Sem oferta |
| 10/11 | 08 Preparação final e checklist | Timeline por hora, revelação final, checklist. "Menos de \[tempo\]" | Sem oferta |
| 11/11 07h | 10 Single day | "Você foi selecionado: Black Antecipada começou agora e você está na lista selecionada". Acesso VIP e ofertas gerais | 22% de desconto adicional |
| 11/11 11h | 11 Single day | "24h, 24 produtos, 22% off. Acesso VIP acaba em poucas horas". Seleção especial com contagem do fim do acesso | 22% |
| 11/11 14h | 12 Catálogo Clube (VIP) | Curadoria exclusiva VIP liberada. Editorial com ofertas relâmpago | 22% adicional |
| 11/11 18h | 13 Desconto surpresa e escassez | "Surpresa: você ganhou \[XX\]% de desconto extra. Estoque crítico". Código surpresa e atualização de estoque | Desconto não explícito, descoberto no carrinho |
| 11/11 22h | 09 Campanha da madrugada | Desconto da madrugada | Desconto prorrogado |

A data do e-mail híbrido não aparece na print. A numeração indica que ele ocupa as posições 5 e 6, entre 06 e 09/11.

### 15.2 Outubro: Halloween com desconto progressivo

![Coluna de outubro do board: e-mail 01 soft sell de 29/10 com estrutura completa, e-mail 02 catálogo de 31/10 e e-mail 03 em texto puro de 01/11 assinado pela gerente de relacionamento](blob/26447341-36e8)

Estrutura do e-mail 01, de cima para baixo: hero com headline de gancho de Halloween e a mecânica do desconto, subheadline explicando "quanto mais compra, maior o desconto", CTA, selo com o desconto máximo de 20%, corpo em três parágrafos (por que a promoção existe, mecânica clara, urgência e prazo), mini proposta de valor com 2 a 4 benefícios em ícone, grid de produtos 2x2 com preço "de" e "por", e reforço da mecânica no fim.

O e-mail 03 é o ponto de virada. É texto puro, assinado pela gerente de relacionamento, com saudação pelo primeiro nome, encerramento oficial da "Promoção Progressiva de Halloween" e um cupom de 15% como agradecimento. Ele planta a personagem que o CEO vai desautorizar no dia seguinte.

### 15.3 Aquecimento de 02 a 06/11

![Trecho do board com os e-mails de 02, 03, 05 e 06 de novembro: CEO cancela a promoção, teaser "não compre nada", criação de desejo e seleção, tangibilização e prova](blob/8220a515-3116)

| E-mail | Blocos obrigatórios | Técnicas marcadas no board |
| --- | --- | --- |
| 05/11 Criação de desejo e seleção | 1. Hook emocional em 2 linhas ("Imagine..."). 2. Segmentação por problema em 3 bullets, uma persona por linha. 3. Ancoragem de valor: quanto o cliente costuma investir e o que vai acontecer no dia. 4. Gratuidade e seleção: "Você está na lista. De graça." 5. Escassez real do negócio. 6. Pergunta ao leitor com pedido de resposta ao e-mail. 7. PS estratégico com uma ação para não perder nada | Ancoragem de expectativa, segmentação por dor, inversão de valor, engajamento direto, curiosidade para o próximo e-mail |
| 06/11 Tangibilização e prova | 1. Abertura direta em nome de uma pessoa da marca. 2. Revelação de dados: "estes são os produtos que sempre esgotam primeiro". 3. Lista dos 5 a 7 principais com estoque atual e prova social por item. 4. Razão da revelação: "não vai ter 'vou pensar depois'. Vai ser: vi, gostei, cliquei, comprei". 5. Detalhes do evento com dia, hora e 3 benefícios. 6. PS com gancho para o próximo e-mail | Prova concreta com números reais, escassez quantificada, prova social específica, timeline clara, loop de curiosidade |

Exemplos de prova social sugeridos no board: "Última vez esgotou em 2h47min", "Clientes pedem reposição toda semana", "Mais vendido em 2024", "Nº 1 em avaliações 5 estrelas". Esses números só podem ser usados se forem verdadeiros para o cliente.

### 15.4 Aquecimento de 07 a 10/11

![Trecho do board com o e-mail híbrido de educação e bônus, o e-mail 7 Nós x Eles de 09/11 com o prompt completo para IA e o e-mail 8 de preparação final e checklist de 10/11](blob/c6c4e91a-5d1a)

| E-mail | Estrutura | Observação |
| --- | --- | --- |
| Híbrido: educação e bônus | Abertura dupla ("estamos a X dias e X% das pessoas me perguntaram..."), parte 1 de educação com problema comum e consequência e um de três formatos (método passo a passo, 3 erros fatais, comparação por nível), "regra de ouro", conexão com a oferta e inversão de risco, parte 2 com a revelação dos bônus | Framework no estilo Hormozi. É o e-mail mais longo da sequência |
| 09/11 Nós x Eles | Abertura forte em 3 a 5 linhas, contexto rápido em 2 a 3 parágrafos, tabela comparativa "nós x outras lojas" com 5 critérios, explicação de 3 diferenciais | O board traz o prompt inteiro para IA: tom direto sem enrolação, português humanizado, frases de até 2 linhas, AIDA, e saída com 3 opções de assunto (conservadora, equilibrada, ousada) de 40 a 50 caracteres, pré-cabeçalho de 50 a 70 caracteres e sugestão de teste A/B |
| 10/11 Preparação final e checklist | 1. Urgência temporal: "Menos de \[tempo\]". 2. Timeline hora a hora do evento. 3. Revelação final com 5 itens e estoque. 4. Checklist de ações preparatórias. 5. Contraste de resultados: quem aproveitou e quem se arrependeu. 6. Despedida antecipando o horário. 7. PS triplo | Técnicas marcadas: timeline específica, checklist acionável, contraste vencedores e perdedores, fechamento de todos os loops |

### 15.5 O dia 11/11

![Coluna do dia do evento: cinco disparos em 11/11 às 7h, 11h, 14h, 18h e 22h, todos com proposta, objetivo e tipo](blob/a4511212-3265)

Cinco disparos em 15 horas, cada um com um motivo novo para abrir: privilégio às 7h, prazo do acesso VIP às 11h, curadoria às 14h, surpresa e estoque às 18h, prorrogação às 22h. A oferta base é a mesma o dia todo (22% adicional). O que roda é o ângulo.

### 15.6 O que o estudo confirma no modelo de 2025

Nove decisões de 2025 batem com dado ou com prática de operador levantada neste estudo.

| O que a Convertfy fez | O que o estudo diz | Onde |
| --- | --- | --- |
| Trocou de oferta entre Halloween (progressivo por quantidade) e 11.11 (22% adicional) | Nunca uma oferta só. Rotação evita fadiga e gera recompra | 4.1, C1 |
| Desconto progressivo 10, 15 e 20% por quantidade | Mesma mecânica do "Buy more, save more" da Dr. Squatch e dos níveis da Nightcity | 9.1 |
| Texto puro assinado por pessoa (gerente, CEO) | E-mails de texto estão entre os de melhor desempenho em Q4. Assinar como fundador ou alguém do time | 9.3, WP |
| "Lista selecionada" e acesso VIP | Exclusividade é a alavanca do acesso antecipado. MeUndies abriu VIP 9 dias antes da BF. Ice Cartel: "VIP Black Friday is live" | 3, 9.1, TT |
| Pedido de resposta ao e-mail em 05/11 | Aberturas, cliques e respostas nas semanas anteriores recuperam a caixa principal. É a melhor ação de reputação antes do pico | 6.4, WP |
| Vários disparos no dia com ângulo novo em cada um | Frequência é como a marca fica visível numa caixa com mais de 100 e-mails. Marcas agressivas chegam a 4 por dia | 5.1, 6.6, WP |
| Desconto surpresa às 18h | Mesmo gatilho dos SMS da Elemis e da Venus ("Surprise!") e do "twist" da Cyber Monday | 8.4, 3 |
| Campanha da madrugada com prorrogação | Mesmo papel do "Late to the party? We kept the door open" do Figma e da cauda de 12 a 16/11 | 9.4, 3 |
| Três opções de assunto por e-mail (conservadora, equilibrada, ousada) | Alimenta o reenvio: o mesmo e-mail volta com outro assunto e outro pré-cabeçalho | 6.6, WP |

### 15.7 O que o estudo questiona

| Ponto | Modelo de 2025 | O que o estudo diz | Leitura |
| --- | --- | --- | --- |
| Nove dias sem oferta (02 a 10/11) com "não compre nada" | Segura a compra para concentrar no dia 11 | Max: nunca ficar sem oferta. 42% planejam comprar antes de novembro. Outubro de 2025 movimentou US$ 88,7 bi | Conflito real. O modelo de 2025 tem resultado interno, o do Max é prática de operador. Sem os números da carteira não dá para dizer qual rende mais. Decisão proposta na seção 15.9 |
| Cinco disparos no mesmo dia | 7h, 11h, 14h, 18h e 22h para a mesma lista | A referência mais agressiva do Max é 3 no dia da BF e até 4 em marcas agressivas | Cinco está acima do teto de referência. Em conta nível A com lista aquecida pela sequência, aceitável. Em nível B e C, os disparos de 18h e 22h deveriam ir só para quem abriu ou clicou no dia |
| E-mails longos (híbrido, Nós x Eles) | Educação e comparação antes do evento | WP: não é hora de storytelling, e-mail longo atrasa a produção | O alerta do WP é sobre os dias de pico. Antes do evento o papel é outro: gerar resposta, clique e expectativa. Manter, com o cuidado de não virar texto forçado |
| "Lista selecionada" para toda a base | Todo mundo recebe o e-mail do CEO e entra na lista | A exclusividade só funciona se for crível | Se toda a base é "selecionada" todo ano, o efeito cai. Em 2026 a seleção pode ser real: quem respondeu, clicou ou se cadastrou no pop-up VIP |
| Prorrogação às 22h | Prazo anunciado e depois estendido | Não há dado no estudo | Usada em toda campanha, ensina a lista a ignorar o prazo. Alternar com fechamento real |
| Prova social e estoque do e-mail de 06/11 | "Esgotou em 2h47min", estoque por item | Regra da casa e do Procon: número precisa ser verdadeiro | Usar só dado real do cliente |
| Desconto não explícito às 18h | Descobre no carrinho | Sem conflito legal conhecido, desde que o desconto exista para todos que receberam | Conferir por cliente |

### 15.8 O que o estudo acrescenta e o modelo de 2025 não tinha

- **Segmento por disparo.** O board não diz quem recebe cada e-mail. O estudo traz os níveis A, B e C (6.3) e os freios de spam (6.5).
- **SMS, WhatsApp e push.** O plano de 2025 é só e-mail. O estudo traz cadência alternada (5.2), modelos de mensagem (8.4.1) e a regra de enviar o SMS cinco minutos depois do e-mail.
- **Pop-up e site.** Pop-up próprio do 11.11 com e-mail e telefone, e site inteiro na oferta (7, C1).
- **Flows em modo evento.** Welcome, navegação e carrinho com a oferta do 11.11, 1 a 2 e-mails cada (7).
- **O que vem depois do dia 11.** O board termina em 11/11. O estudo traz a cauda de 12 a 16/11, o Early Access de 17 a 24/11 e a BF a partir de quarta 25/11 (3.1).
- **A janela de 14 dias.** A recompra se concentra nos 14 dias após a compra (C1). Quem compra em 11/11 está no auge da intenção até 25/11, exatamente o dia em que a BF abre. O comprador do 11.11 não deve ser excluído da BF. Ele é o melhor público dela.
- **Reenvio.** Com 3 assuntos prontos por e-mail, cada e-mail do dia 11 pode voltar para quem não abriu, sem produção extra.
- **MMS nos picos para clientes dos EUA.** Mostrar o brinde ou o produto na imagem rendeu US$ 2.000 contra US$ 534 no teste do Max (8.5).

### 15.9 Modelo 11.11 de 2026

A proposta é manter a espinha do modelo de 2025, que tem resultado na própria carteira, e corrigir os quatro pontos em que o estudo traz evidência: segmento por disparo, canais além do e-mail, seleção real da lista VIP e continuidade depois do dia 11. \[I\]

Sobre o conflito dos nove dias sem oferta, a recomendação é testar, não escolher no escuro:

| Grupo | Clientes | Modelo |
| --- | --- | --- |
| Controle | Maioria da carteira | Modelo de 2025: aquecimento sem oferta de 02 a 10/11 e pico em 11/11 |
| Teste | 10 a 20 clientes nível A, com volume | Aquecimento igual, mas com a aba permanente de "ofertas de fim de ano" no site e sem o teaser "não compre nada". O 11.11 segue como pico |

Métrica de comparação: receita total de 01 a 16/11 por mil contatos, não só a receita do dia 11. É isso que responde se segurar a compra concentra ou só adia a venda.

#### Calendário proposto, 29/10 a 16/11 de 2026

| Data | E-mail | Mudança em relação a 2025 | Segmento A, B, C | Outros canais |
| --- | --- | --- | --- | --- |
| 29/10 qui | Soft sell de Halloween, progressivo | Igual | 120, 90, 60 dias | Push |
| 31/10 sáb | Catálogo de Halloween | Igual | 120, 90, 60 |  |
| 01/11 dom | Texto da gerente, cupom de 15% | Igual | 120, 90, 60 | WhatsApp ou SMS com o cupom |
| 02/11 seg | Texto do CEO, cria a lista selecionada | A entrada na lista passa a exigir uma ação: responder, clicar ou cadastrar o telefone no pop-up VIP | 365, 180, 90 | Pop-up VIP no ar com e-mail e telefone |
| 03/11 ter | Teaser | No grupo de teste sai o "não compre nada" e entra "o que vem no 11.11" | 365, 180, 90 |  |
| 05/11 qui | Criação de desejo e seleção | Igual. Manter o pedido de resposta | 365, 180, 90 |  |
| 06/11 sex | Tangibilização e prova | Só números reais do cliente | 365, 180, 90 | Push: data e hora do evento |
| 08/11 dom | Híbrido: educação e bônus | Encurtar. Uma ideia por e-mail | 180, 120, 90 |  |
| 09/11 seg | Nós x Eles | Igual | 180, 120, 90 |  |
| 10/11 ter | Preparação final e checklist | Igual | Lista cheia, 365, 120 a 180 | WhatsApp ou SMS: "amanhã às 7h" |
| 11/11 qua 07h | Abertura: você foi selecionado | Igual | Lista cheia, 365, 120 a 180 | SMS ou WhatsApp 5 minutos depois. Push |
| 11/11 qua 11h | 24 produtos, acesso VIP acabando | Reenvio da abertura para quem não abriu, com o assunto 2 | Igual às 7h, só não abridores |  |
| 11/11 qua 14h | Catálogo Clube VIP | Igual | 365, 180, 90 | Push |
| 11/11 qua 18h | Desconto surpresa e estoque | Nível B e C: só quem abriu ou clicou no dia | Lista cheia, engajados do dia, engajados do dia | SMS ou WhatsApp de últimas horas. EUA: antes das 21h locais |
| 11/11 qua 22h | Madrugada | Alternar por cliente entre prorrogação e fechamento real | 365, engajados do dia, engajados do dia | Push |
| 12 a 16/11 | Cauda: 2 e-mails | Novo. "Continua até segunda" e fechamento em 16/11, uma segunda-feira | 365, 180, 90 | 1 SMS ou WhatsApp no fechamento |
| 17/11 ter | Abre o Early Access da BF | Novo. Compradores do 11.11 entram primeiro: estão na janela de 14 dias de recompra até 25/11 | Conforme ficha 4 | Conforme ficha 4 |

Total de 29/10 a 16/11: 17 e-mails, contra 16 em 2025, com dois disparos do dia 11 restritos a parte da lista nos níveis B e C.

#### Flows e site no período

- Welcome, navegação e carrinho passam a mostrar a oferta do 11.11 de 11 a 16/11, com 1 a 2 e-mails cada.
- Pós-compra de 11/11: texto curto de agradecimento e aviso de que a lista de compradores entra primeiro na Black.
- Site inteiro na oferta no dia 11. Pop-up do 11.11 substitui o pop-up VIP às 7h.

#### O que medir para transformar o caso em dado

- [ ] Receita por janela: Halloween, aquecimento, dia 11, cauda
- [ ] Receita por disparo do dia 11, para saber quanto rendem os envios das 18h e 22h
- [ ] Descadastro e reclamação de spam por disparo do dia 11
- [ ] Taxa de resposta ao e-mail de 05/11 e efeito na abertura dos dias seguintes
- [ ] Receita de 01 a 16/11 por mil contatos, controle contra teste
- [ ] Quantos compradores do 11.11 recompram entre 17 e 29/11

## 16. Caso interno: os e-mails executados em novembro de 2025

O board "Emails Black Friday" mostra 21 e-mails gráficos de 05/11 a 01/12 de 2025, em um template mestre em inglês aplicado a mais de uma marca (Blue Wolf em tema escuro, Dr. Melaxin em tema branco). A Convertfy rodou 9 mecânicas de oferta em 27 dias, mais rotação que o próprio Max recomenda, com menos envios que ele e com e-mails bem mais longos. \[D interno, leitura das prints\]

![Visão geral do board de 05/11 a 14/11 de 2025, marca Blue Wolf: seis e-mails de aquecimento, quatro disparos do dia 11/11, abertura ao público em 12/11 e Prize Friday em 14/11](blob/9989ce59-b817)

![Visão geral do board de 11/11 a 01/12 de 2025: dia 11/11, 12/11, 14/11, preparação da Black Week em 17, 19 e 23/11, Black Week em 24, 25 e 26/11, dois e-mails de Black Friday em 28/11 e Cyber Monday em 01/12](blob/23e464a1-7cad)

### 16.1 Linha do tempo executada

| Data | Título do hero | Papel | Oferta e cupom |
| --- | --- | --- | --- |
| 05/11 | "Blue Wolf with up to 60% off". "The time is coming! 11.11" | Anúncio. Lista VIP, 4 motivos, contagem de 7 dias, 3 passos para garantir o desconto | Até 60% anunciado para o dia 11 |
| 06/11 | "Early access to the Black: 24 hours of exclusive discounts on November 11 at 7 A.M." | Criação de desejo e seleção. "You are in VIP list", 3 personas, estoque físico limitado | Sem oferta |
| 07/11 | "You've secured access to Black Friday, November 11th at 7 AM" | Tangibilização. "These are the 6 products that always sell out", "Why am I showing you this?" | Sem oferta |
| 08/11 | "Black Friday Advance, day only 11.11". "It's coming: Big Day" | Híbrido de educação. "Most people do this", "Method correct" com 4 perfis, e bônus | Bônus progressivo 10, 15 e 20% só para os 100 primeiros |
| 09/11 | "Here a Black Friday it's out of the ordinary". "73%" | Nós x Eles. Tabela "Our differential", 4 motivos para não perder | Sem oferta |
| 10/11 | "24 hours of exclusive offers 11.11 at 7 A.M." | Preparação final. Horários dos envios (7h, 10h59, 17h59, 21h59), checklist de 4 ações | Sem oferta |
| 11/11 nº 1 | "Black Friday Early Access. Até 50% off + 22% off extra" | Abertura. 24 horas, 24 produtos. "It's simple" em 4 passos, "Why can't you leave it for later?" com 5 motivos | Cupom 24HOURS, 22% adicional |
| 11/11 nº 2 | "Early access open to only 39 VIPs. 22% off" | Clube VIP. "It is 1:27 P.M. on November 11", "The data proves", 3 filtros do "seu e-mail" | Cupom BLACKVIP, 22% no site todo |
| 11/11 nº 3 | "Pop the balloon and win" | Gamificação. Botão "Burst". E-mail curto | BLACKVIP, 22% |
| 11/11 nº 4 | "Black November Advance, 22% off sitewide. Only in the next 100 orders" | Extensão. "It ended so quickly that we decided to unlock it for another 100 people" | BLACKVIP, 22% |
| 12/11 | "Missed the VIP? 11.11 open to everyone" | Abertura ao público por 12h | Progressivo 10, 17 e 20%. Cupons BLACK10, BLACK17, BLACK20 |
| 14/11 | "Black November. Offers up to 50% off". "Enjoy the Prize Friday" | Sexta premiada. "We released 100 exclusive 14% off coupons. Only 49 are left" | Cupom FRIDAY14, 14% |
| 17/11 | "Black Week: 5 days of deals, new offers every day at 11AM" | Anúncio da semana. "Here's how it works" com os 5 dias, "Mark your calendar", "Remember this number: 1,247" | Sem oferta |
| 19/11 | "The number of frustration: 1,247" | Prova e preparação. 6 produtos que esgotam, reviews, "Do this now" (lista de desejos), conferir pagamento | Sem oferta |
| 23/11 | "Last chance: VIP List ends today in 24h" | Inscrição na lista VIP. Quem entra ganha o quê, quem não entra perde o quê | Sem oferta |
| 24/11 seg | "Black Week has arrived. 24 hours, 24 products. 20% off" | Dia 1. "20% off exclusive on Mondays" | Cupom BLACKWEEK, 20% |
| 25/11 ter | "Black Week up to 60% off + 20% extra" | Dia 2. Navegação por coleção (4 fotos) e por preço (US$ 99, 199, 299, 399) | BLACKWEEK |
| 26/11 qua | "Build your premium leather collection today. The more pieces you add, the more you save" | Dia 3. Kit progressivo e brinde surpresa para os 100 primeiros pedidos | Cupons BLACK12, BLACK18, BLACK22 |
| 28/11 nº 1 | "The day has arrived: Black Friday. Up to 50% off + extra 23%" | Black Friday. "It's simple", "Why you shouldn't wait" com 5 motivos, "At midnight this page disappears" | Cupom BLACK, 23% adicional |
| 28/11 nº 2 | "Black Friday 23% off storewide. Surprise gift with order at your door" | Segundo envio, tom de presente. "Exclusive Black Friday via email" | BLACK, 23% |
| 01/12 | "Cyber Monday VIP exclusive. Last chance for get 23% off" | Extensão. "Missed Black Friday? Relax, there's still time" | Cupom VIP23, 23% |

Não há e-mail no board para 13, 15, 16, 18, 20, 21, 22, 27, 29 e 30/11. Os e-mails de texto de 02 e 03/11 do planejamento (seção 15) não aparecem aqui porque o board é só de peças com design.

### 16.2 Planejado contra executado no 11.11

| Item | Planejamento (seção 15) | Execução |
| --- | --- | --- |
| Início | 02/11 com o e-mail do CEO | 05/11 no board de design |
| Disparos no dia 11 | 5: 7h, 11h, 14h, 18h, 22h | 4: 7h, 10h59, 17h59, 21h59, anunciados no e-mail de 10/11 |
| Oferta do dia | 22% adicional para a lista selecionada | Igual: até 50% mais 22% com cupom |
| Catálogo Clube VIP das 14h | Curadoria editorial | Virou o e-mail nº 2, "VIP Club", com os 3 filtros |
| Desconto surpresa das 18h | Desconto não explícito no carrinho | Virou "Pop the balloon and win", com o mesmo cupom de 22% |
| Madrugada, 22h | Desconto prorrogado | Virou "Only in the next 100 orders" |
| Depois do dia 11 | Não previsto | 12/11 aberto ao público e 14/11 Prize Friday |

### 16.3 Escada de ofertas de 2025

| Janela | Mecânica | Desconto anunciado |
| --- | --- | --- |
| 08/11 | Bônus progressivo para os 100 primeiros | 10, 15, 20% |
| 11/11 | Seleção de 24 produtos com cupom adicional, depois cupom no site todo | Até 50% mais 22% |
| 12/11 | Progressivo por quantidade, aberto ao público | 10, 17, 20% |
| 14/11 | Lote de 100 cupons | 14% |
| 24/11 | 24 produtos por 24 horas | 20% |
| 25/11 | Até X% mais cupom, navegação por coleção e preço | Até 60% mais 20% |
| 26/11 | Kit progressivo mais brinde surpresa para 100 pedidos | 12, 18, 22% |
| 28/11 | Até X% mais cupom adicional | Até 50% mais 23% |
| 01/12 | Extensão com cupom VIP | 23% |

### 16.4 Anatomia dos e-mails da Convertfy

O template de 2025 é modular: 14 blocos se repetem em combinações diferentes, o que permite trocar a marca e o tema sem refazer a estrutura.

![E-mails de 05, 06 e 07/11 de 2025 ampliados: anúncio com lista VIP e 3 passos, criação de desejo com 3 personas e estoque limitado, tangibilização com os 6 produtos que sempre esgotam](blob/444d4782-291e)

![E-mails de 08, 09 e 10/11 de 2025 ampliados: híbrido de educação com método e bônus progressivo, Nós x Eles com tabela de diferenciais, preparação final com horários e checklist](blob/cc70adc7-bdae)

| Bloco | Como aparece | Frequência nos 21 e-mails | Equivalente no material do Max |
| --- | --- | --- | --- |
| Faixa de topo em marquee | "Save the date 11.11" repetido | Todos até 14/11 | Marquee, 49% dos templates do Figma |
| Hero com número gigante | "60% off", "11.11", "22% off", "1,247", "100 orders" | Todos | Hero de oferta, regra 1 do WP |
| Bloco de cupom | "Coupon: BLACKVIP" em caixa, logo abaixo do hero | Todos os de oferta | Código visível, 30% dos templates |
| Selo "You are in VIP List" | Caixa clara com subtítulo "with guaranteed early access" | 05, 06, 07, 17, 23/11 | "VIP Pass" do Figma |
| Lista de motivos com ícone de check | "Why you can't miss", 3 a 4 itens | Quase todos | Lista de 3 benefícios (Breatheeze) |
| Contagem regressiva em texto | "Only 7 days left until the Black Friday pre-sale", depois 6, 5, 3 | 05 a 09/11 | Timer e "hours remain" |
| Passos numerados | "Step 1, 2, 3" e "It's simple" em 4 passos | 05, 11 nº 1, 24, 28/11 | Sem equivalente direto |
| Personas ou perfis | 3 personas em 06/11, 4 perfis em 08/11 ("The minimalist", "The upgrader"...) | 2 | Sem equivalente. Vem do framework interno |
| Tabela Nós x Eles | "Our differential": 4 linhas de check contra 4 de X | 09/11 | Sem equivalente |
| Checklist de preparação | "11.11 Checklist": alarme às 6h55, endereço, produto, cartão | 10 e 19/11 | Sem equivalente |
| Calendário em blocos | "Mark your calendar" com os 5 dias às 11AM | 17 e 19/11 | Template de calendário do Figma |
| "Why can't you leave it for later?" | 5 motivos numerados | 11 nº 1, 24, 28/11 | "Here are 3" da Bite |
| Grid de produtos | 2, 4 ou 6 produtos com preço e botão | Todos | Grid, 25% dos templates |
| Rodapé de garantias | Frete expresso, qualidade, pagamento seguro | Todos | 4 ícones da Ice Cartel |

![E-mails de 17, 19 e 23/11 de 2025 ampliados: anúncio da Black Week com calendário, o número 1.247 com produtos que esgotam e lista de desejos, última chance da lista VIP](blob/92a4e18c-2c4e)

![E-mails de 24, 25 e 26/11 de 2025 ampliados: 24 horas e 24 produtos com 20%, até 60% com navegação por coleção e por preço, kit progressivo 12, 18 e 22% com brinde para os 100 primeiros pedidos](blob/7e9b6412-9531)

![E-mails de 28/11 e 01/12 de 2025 ampliados: Black Friday com até 50% mais 23% e 5 motivos para não esperar, segundo envio com tom de presente, Cyber Monday VIP com 23%](blob/5aeb0dec-4a8e)

### 16.5 Estrutura por tipo de e-mail

| Tipo | Ordem dos blocos | Tamanho estimado |
| --- | --- | --- |
| Aquecimento (05 a 10/11, 17 a 23/11) | Marquee, hero com foto ou número, selo VIP, corpo de argumento (personas, prova, comparação ou checklist), contagem de dias, 2 produtos, lembrete "11.11, 7 A.M.", rodapé de garantias | 3.000 a 4.200 px |
| Abertura de oferta (11/11 nº 1, 24/11, 28/11 nº 1) | Marquee, data e prazo, hero com % e cupom, caixa de explicação, "It's simple" em 4 passos, 2 a 4 produtos, faixa Black Friday, "Why can't you leave it for later?" com 5 motivos, fecho com a regra da oferta, cupom repetido, rodapé | 3.700 a 4.200 px |
| Reforço curto (11/11 nº 3 e nº 4, 25/11) | Hero, cupom, um bloco (balão, 100 pedidos, coleção e preço), produtos, rodapé | 1.700 a 2.000 px |
| Extensão (12/11, 01/12) | Hero "perdeu? ainda dá tempo", texto curto, cupons, grid de 6 a 8 produtos, rodapé | 2.800 px |

Os tamanhos são estimados pela proporção das prints, com 600 px de largura.

### 16.6 Convertfy 2025 contra o Max

A Convertfy e o Max concordam na rotação de ofertas e no acesso VIP. Divergem em quatro coisas: quando o volume acontece, o tamanho do e-mail, o uso de texto puro e o fim de semana da BF.

| Dimensão | Convertfy 2025 | Max e Wellcopy | Leitura |
| --- | --- | --- | --- |
| Total de e-mails de 05/11 a 01/12 | 21 | Cerca de 31 no calendário de referência | A Convertfy envia um terço a menos |
| Onde está o volume | No aquecimento (6 e-mails sem oferta em 6 dias) e no dia 11 (4) | Na semana da BF (12 em 5 dias) | Modelos opostos: a Convertfy investe em preparar, o Max em repetir a oferta |
| Dia 11/11 | 4 e-mails | 1 e-mail comum | O 11.11 é invenção da casa, sem paralelo no Max |
| 12 a 23/11 | 5 e-mails em 12 dias, 3 deles sem oferta | 12 e-mails, diário a partir de 17/11 | Maior diferença de frequência. É a janela de Early Access do Max |
| Semana da BF | Segunda 24 a sexta 28: 5 e-mails, nenhum em 27/11 | Quarta 25 a domingo 29: 12 e-mails | A Convertfy começa 2 dias antes e envia menos da metade |
| Dia da BF | 2 e-mails | 3 e-mails | Próximo |
| Sábado e domingo após a BF | Nenhum envio em 29 e 30/11 | 3 no sábado, 2 no domingo | Dois dias da semana de maior compra do ano ficaram sem e-mail |
| Cyber Monday | 1 e-mail, extensão do mesmo desconto | 2 a 3 no dia mais 3 dias de cauda, com oferta nova | Na Convertfy a CM é um apêndice |
| Dezembro | Nada no board depois de 01/12 | 11 e-mails de presentes e prazo de entrega até 21/12 | Janela inteira sem cobertura |
| Número de ofertas | 9 mecânicas em 27 dias | Cerca de 5 no mês | A Convertfy roda mais que o Max. Ponto forte |
| Tipo de oferta | Quase sempre % com cupom, empilhado sobre "até X%". Brinde uma vez (26/11) | Mistura de %, bundle, brinde, crédito de loja, drop de produto | Pouca variação de mecânica, muita variação de número |
| Resgate | Sempre cupom digitado, 12 códigos diferentes no mês | Código ou desconto automático | Muitos códigos aumentam erro no checkout. Testar desconto automático nos picos |
| Exclusividade | "Exclusive via email", oferta atrás de cupom | Oferta no site todo, exclusividade só no Early Access | Conflito. Ver 13 |
| Tamanho do e-mail | 3.000 a 4.200 px na maioria, até 6 seções de argumento | Mediana de 2.806 px, "keep it light" | Os e-mails de pico da Convertfy são os mais longos. No Max é o contrário |
| CTA acima da dobra | Sim, em todos | Sim | Igual |
| Texto puro | Nenhum no board de novembro | Mais de 50% dos envios em alguns clientes | Maior diferença de formato. Todo e-mail da Convertfy exige design |
| Reenvio | Não aparece | Mesmo e-mail com assunto novo | Não usado |
| Copy de argumento | Personas, método, Nós x Eles, checklist, número-âncora (1.247) | Oferta, urgência, como resgatar | A Convertfy vende a razão de comprar. O Max vende só a oferta |
| Gamificação | "Pop the balloon" no e-mail | Raspadinha só no pop-up | A Convertfy leva o jogo para o e-mail |
| SMS, push, pop-up, flows | Não aparecem no board | Parte central do plano | Lacuna de canal |
| Template | Um mestre com dois temas para várias marcas | Wireframes avulsos | Escala de produção é ponto forte da Convertfy |

### 16.7 O que a Convertfy faz e o Max não ensina

- **Sequência de preparação com papel definido por e-mail.** Anúncio, desejo, prova, educação, comparação, checklist. O Max não tem nada equivalente antes de uma oferta.
- **Número-âncora entre e-mails.** "Remember this number: 1,247" em 17/11, explicado em 19/11. Cria motivo para abrir o e-mail seguinte.
- **Tarefa para o leitor.** Pôr alarme, conferir endereço, salvar na lista de desejos, testar o checkout. Gera clique fora do dia de oferta, o que ajuda a reputação antes do pico.
- **Navegação por preço.** "Shop by price: US$ 99, 199, 299, 399" em 25/11. Útil para presente e para ticket alto.
- **Abertura ao público no dia seguinte.** "Missed the VIP? Open to everyone" em 12/11 dá uma segunda onda sem repetir a mesma oferta.

### 16.8 O que o Max faz e a Convertfy não fez em 2025

- Envio diário de 17 a 24/11 com oferta fechada para a lista.
- Sábado e domingo da BF com 2 a 3 e-mails por dia.
- Cyber Monday como janela própria de 4 dias, com novidade.
- Dezembro: presentes, níveis de gasto, prazo de entrega, vale-presente.
- E-mails de texto puro intercalados, que dobram a frequência sem dobrar o design.
- Reenvio para não abridores.
- SMS alternado com o e-mail, pop-up por janela, flows encurtados.
- Mecânicas além do %: bundle, brinde, crédito de loja, drop de produto.

### 16.9 Pontos de risco encontrados nos e-mails

Cinco problemas aparecem na copy de 2025 e não devem ser repetidos como estão. O formato funciona. O que precisa mudar é a origem dos números e das promessas.

![Zoom nos quatro disparos de 11/11 e no de 12/11 na versão Dr. Melaxin: cupom 24HOURS com 50% mais 22%, "open to only 39 VIPs" com os três filtros, balão, 100 pedidos e abertura ao público](blob/711e2f11-fdd1)

| Problema | Onde aparece | Por que é risco | Correção para 2026 |
| --- | --- | --- | --- |
| Números iguais em marcas diferentes | "18,432 active customers", "12,876 people bought from us this year", "less than 5% received this email", "open to only 39 VIPs", "you opened 78% of our emails", "clicked on 64%" aparecem idênticos na Blue Wolf e na Dr. Melaxin | São dados do template, não da loja. No BR é publicidade enganosa pelo CDC. Nos EUA e UE, prática comercial enganosa. Fere a regra 0.3 deste documento. Também vale para "1,247", "2,847 people marked", "387 units in 57 minutes", "+8,000 people", "73% of stores inflate prices" | Preencher com dado real da conta: base ativa, compradores do ano e estoque saem do Shopify e da Omnisend. Sem dado real, o bloco sai do e-mail |
| Soma de descontos | "50% + 22% extra = 72% total" em 11/11 e "50% + 23% = 73% total" em 28/11 | Desconto em cascata não soma. 50% e depois 22% dá 61% sobre o preço cheio. 50% e 23% dá 61,5%. O número anunciado é maior que o real | Anunciar "até 50% mais 22% no carrinho" sem total, ou o total correto |
| Promessa sobre a BF quebrada | 11/11: "On Black Friday it will be a maximum of 50%, without an extra coupon" e "will not be repeated this year". 28/11: até 50% mais 23% | A BF foi melhor que o 11.11, o contrário do prometido. Quem comprou no dia 11 confiando na frase foi prejudicado. Isso ensina a lista a esperar | Nunca falar da BF na copy do 11.11. A diferença entre as datas é de mecânica, não de promessa (seção 3) |
| Seleção que não seleciona | "Only 5% of our customers have access", "VIP list ends today", "will enter the regular queue" | Se todos recebem e não há fila, a frase é falsa | Tornar verdadeiro: ver 16.10 |
| Escassez de cupom | "100 coupons, only 49 are left", "only in the next 100 orders", "unlock for another 100 people" | Só é aceitável se o limite existir no Shopify | Criar o cupom com limite de uso real |

### 16.10 Lista VIP de verdade: resolve a copy e a reputação juntas

A mecânica mais forte de 2025 é a lista VIP. Em 2026 ela pode ser real com uma mudança simples: o botão "I want to be VIP" marca o contato com uma tag na Omnisend, e só quem tem a tag recebe os envios exclusivos. \[I\]

- A copy passa a ser verdadeira: existe uma lista, existe um prazo de entrada, existe quem ficou de fora.
- A tag cria um segmento de quem clicou nos últimos dias. É o público mais seguro para os envios de alta frequência, exatamente o que contas nível B e C precisam (seção 6.3).
- Os números do e-mail "VIP Club" viram reais: tamanho da lista VIP sobre a base ativa.
- O comprador do 11.11 entra automaticamente na lista VIP da Black Week e fica na janela de 14 dias de recompra até 25/11 (seção 15.8).

### 16.11 O que levar para 2026

| Manter | Ajustar | Acrescentar |
| --- | --- | --- |
| Template mestre com temas por marca | Números de prova: só reais, por cliente | Texto puro intercalado, usando os esqueletos da seção 9.3 |
| Sequência de preparação com papel por e-mail | Sem soma de descontos e sem promessa sobre a BF | Reenvio para não abridores com o assunto 2 |
| Rotação de 9 mecânicas | E-mails de abertura de oferta mais curtos: hero, cupom, 4 passos, produtos. Os 5 motivos vão para o reenvio | Envio diário de 17 a 24/11 |
| Número-âncora e tarefas para o leitor | Lista VIP com tag real | Sábado 28 e domingo 29/11, com 2 e-mails por dia |
| Navegação por coleção e por preço | Menos códigos de cupom, desconto automático nos picos | Cyber Monday com oferta nova, de 30/11 a 03/12 |
| Abertura ao público no dia seguinte | Variar a mecânica além do %: brinde, bundle, crédito | Dezembro: presentes, prazo de entrega, vale-presente |
| Gamificação no e-mail |  | SMS ou WhatsApp, push, pop-up por janela e flows em modo evento |

Com esses acréscimos, o volume de 05/11 a 03/12 sobe de 21 para cerca de 35 envios, e metade do aumento é texto puro ou reenvio, sem custo de design.

## 17. Análise de contas Omnisend: loja 1, Emyerre

Na Emyerre o e-mail responde por 14,2% da receita da loja, e 78% disso vem de automações. As 25 campanhas somam US$ 1.479 e 11 pedidos em seis semanas. O gargalo não é o calendário nem o assunto: é o tamanho da lista e o número de cliques que cada envio gera. \[D, API da Omnisend, coleta em 18/09/2026\]

Dados de 20/07 a 18/09/2026, em dólar, fuso de Londres. Conta criada no fim de julho de 2026, com cerca de sete semanas de envio. Só canal de e-mail. Nenhuma campanha de SMS ou push.

### 17.1 Retrato da conta

| Indicador | Valor |
| --- | --- |
| Loja | emyerre.com, global, inglês, moeda USD |
| Receita total da loja no período | US$ 46.243,88 em 443 pedidos |
| Ticket médio | US$ 104,39 |
| Receita atribuída ao e-mail | US$ 6.582,15 em 63 pedidos, 14,2% da loja |
| Automações | US$ 5.102,82, 52 pedidos, 11,0% da loja. 12.525 envios, abertura 42,3%, clique 4,76%, US$ 0,41 por envio |
| Campanhas | US$ 1.479,33, 11 pedidos, 3,2% da loja. 10.823 envios, abertura 35,4%, clique 2,66%, US$ 0,14 por envio |
| Descadastro | 0,23% em campanhas, 0,17% em automações |
| Reclamação de spam | 0 em campanhas, 1 em automações (0,008%) |
| Falha de entrega | 0,60% em campanhas, 0,97% em automações |
| Segmentos | Um único: "TODOS OS LEADS", com 1.096 contatos |
| Formulários | Um pop-up: "Get 10% off your first order", pede nome e e-mail |

Referência do estudo: no material do Max, e-mail e SMS respondem por 42% da receita de BFCM em contas Klaviyo (seção 2.3). Os 14,2% daqui são de conta nova, fora de pico e só com e-mail, então os números não são comparáveis um a um. Servem como linha de base da loja.

### 17.2 Funil de captação

| Etapa | Número | Taxa |
| --- | --- | --- |
| Exibições do pop-up, 07/08 a 18/09 | 31.070 |  |
| Interações | 1.435 | 4,6% das exibições |
| Envios do formulário | 556 | 1,79% das exibições |
| Inscritos novos | 486 | 1,56% das exibições |
| Exibições em celular | 29.450 | 94,8% do total |
| Conversão em celular | 534 envios | 1,81% |
| Conversão em computador | 18 envios de 1.234 | 1,46% |

Configuração: aparece após 12 segundos ou 70% de rolagem, com saída de intenção ligada, uma vez por dia, fora do carrinho e do checkout. Dois campos (nome e e-mail). Sem telefone. Sem etapa de SMS.

Crescimento da lista por semana, por origem:

| Semana | Pop-up | Externa (checkout da loja) | Manual |
| --- | --- | --- | --- |
| 03/08 | 27 | 6 | 72 |
| 10/08 | 81 | 10 | 0 |
| 17/08 | 83 | 9 | 0 |
| 24/08 | 82 | 9 | 0 |
| 31/08 | 93 | 15 | 0 |
| 07/09 | 74 | 24 | 0 |
| 14/09 | 84 | 9 | 424 |

O pop-up entrega cerca de 83 inscritos por semana, estável. Na semana de 14/09 entraram 424 contatos marcados como "inscritos manualmente", e o segmento foi editado no mesmo dia. O envio saltou de 553 contatos em 14/09 para 994 em 15/09. O efeito aparece na seção 17.6.

### 17.3 Receita da loja e do e-mail, por semana

| Semana | Pedidos da loja | Receita da loja | Receita de automações | Receita de campanhas | Envios de campanha |
| --- | --- | --- | --- | --- | --- |
| 20/07 | 5 | US$ 379 | 0 | 0 | 0 |
| 27/07 | 30 | US$ 3.664 | 0 | 0 | 0 |
| 03/08 | 32 | US$ 3.976 | US$ 336 | 0 | 262 |
| 10/08 | 62 | US$ 7.063 | US$ 812 | US$ 538 | 280 |
| 17/08 | 61 | US$ 5.541 | US$ 470 | US$ 64 | 668 |
| 24/08 | 61 | US$ 6.255 | US$ 689 | US$ 70 | 913 |
| 31/08 | 62 | US$ 6.858 | US$ 1.161 | 0 | 1.205 |
| 07/09, semana do 9.9 | 84 | US$ 8.530 | US$ 931 | US$ 684 | 2.917 |
| 14/09, parcial | 46 | US$ 3.978 | US$ 704 | US$ 123 | 4.570 |

A semana do 9.9 foi a melhor da loja: 84 pedidos, 24% acima da semana anterior. A campanha atribuída explica US$ 684 desse total. O restante da alta pode ter vindo de anúncios ou de compra sem clique no e-mail. Para separar, é preciso olhar o uso dos cupons no Shopify. \[lacuna\]

Na semana de 14/09 os envios de campanha subiram 57% e a receita de campanha caiu 82%.

### 17.4 As 25 campanhas, em ordem

Todas foram para o mesmo segmento, "TODOS OS LEADS". O horário é o local do destinatário (otimização de fuso ligada), exceto o primeiro disparo de cada pico.

| Data | Papel | Assunto | Pré-cabeçalho | Envios | Abertura | Clique | Cliques | Pedidos | Receita | Descad. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 08/08 07h | 8.8, disparo 1 | Fwd: I was able to add your name to this list | You now have access to 8.8 before the official launch. | 88 | 52,3% | 3,4% | 3 | 0 | 0 | 0 |
| 08/08 11h | 8.8, disparo 2 | This email is only valid for the first 100 | The special 8.8 offer has been released... | 87 | 39,1% | 0% | 0 | 0 | 0 | 0 |
| 08/08 18h | 8.8, disparo 3 | Your status has just changed | Open this and see what I've set aside for you. | 87 | 63,2% | 9,2% | 8 | 0 | 0 | 0 |
| 11/08 | Ressaca 8.8 | Missed our 8.8 sale? There's still time... | Only a few of our bestsellers are left... | 125 | 40,0% | 4,8% | 6 | 0 | 0 | 0 |
| 14/08 | Sextou | Your Friday deserves this... | Offers are available only through Sunday. | 155 | 39,4% | 3,2% | 5 | 1 | US$ 538,23 | 0 |
| 17/08 | Segunda Turbo | Are you among the first 100? | Apply the code at checkout and find out. Until midnight. | 198 | 35,4% | 5,1% | 10 | 1 | US$ 64,26 | 1 |
| 19/08 | UGC, Dia da Fotografia | Yours is missing here... | Choose yours. It'll be worth it. | 222 | 39,2% | 3,6% | 8 | 0 | 0 | 2 |
| 21/08 | Catálogo indecisão | Either you choose today, or you keep putting it off... | There is no wrong choice here. | 248 | 33,9% | 2,8% | 7 | 1 | US$ 69,90 | 2 |
| 24/08 | Semana 15%, 1: On & Off | I've activated a discount for you | It's valid sitewide through Friday. | 281 | 40,6% | 3,2% | 9 | 0 | 0 | 0 |
| 26/08 | Semana 15%, 2: Escolha o caminho | \[Nome\], choose your path... | Whichever you choose, you win. Through Friday. | 303 | 43,6% | 2,3% | 7 | 0 | 0 | 0 |
| 28/08 | Semana 15%, 3: Notificação do futuro | \[Nome\], you still need to confirm your order... | Only available until today at 11:59 PM. | 329 | 41,6% | 4,6% | 15 | 0 | 0 | 1 |
| 31/08 | Catálogo fecha mês | Ignore this email after 11:59 PM | Until then, August prices still apply | 366 | 35,0% | 3,0% | 11 | 0 | 0 | 2 |
| 03/09 | Esquenta 9.9, 1 | Fwd: You Were Not Supposed to Know About This | Your Name Is on the 9.9 List | 407 | 35,1% | 2,5% | 10 | 1 | US$ 111,84 | 2 |
| 05/09 | Esquenta 9.9, 2 | I promised I'd let you know in advance, \[nome\] | 09/09, three times: 7 AM, 11 AM, and 6 PM. | 432 | 35,2% | 1,9% | 8 | 0 | 0 | 1 |
| 07/09 | Esquenta 9.9, 3 | \[Nome\], you've secured early access | Those who arrive at 7 AM get the best selection | 465 | 33,3% | 1,7% | 8 | 0 | 0 | 1 |
| 08/09 | Esquenta 9.9, 4 | \[Nome\], you have something scheduled for tomorrow | 9.9: 7 AM, 11 AM, and 6 PM. Be ready! | 475 | 31,8% | 2,1% | 10 | 3 | US$ 386,17 | 2 |
| 09/09 07h | 9.9, disparo 1 | Your coupon has been released | Your 9.9 access is now available. Only until midnight | 490 | 34,3% | 2,4% | 12 | 1 | US$ 71,32 | 1 |
| 09/09 11h | 9.9, disparo 2 | Your access has been granted (today only) | The best 9.9 offer is now available | 487 | 34,7% | 2,9% | 14 | 0 | 0 | 0 |
| 09/09 18h | 9.9, disparo 3 | Your status has just changed | Open it and see what I selected for you | 489 | 48,9% | 2,7% | 13 | 1 | US$ 114,18 | 0 |
| 11/09 | Ressaca 9.9 | We regret to inform you that... | Low stock, but still available at promotional prices | 511 | 36,8% | 2,5% | 13 | 0 | 0 | 1 |
| 14/09 | Antecipação VIP Day | Confirmed: you're on the list for tomorrow | One exclusive coupon will be sent at 7:00 AM. Available by email only | 553 | 42,5% | 5,1% | 28 | 0 | 0 | 1 |
| 15/09 07h | VIP Day, disparo 1 | \[Nome\], you've been selected | VIP Day is exclusive to this list, until midnight | 994 | 32,9% | 2,6% | 26 | 0 | 0 | 1 |
| 15/09 11h | VIP Day, disparo 2 | Were you approved? | The result is valid until midnight | 990 | 32,0% | 1,4% | 14 | 0 | 0 | 1 |
| 15/09 18h | VIP Day, disparo 3 | Prize reserved for \[nome\] | It's yours until 11:59 PM | 993 | 29,9% | 2,2% | 22 | 1 | US$ 64,22 | 3 |
| 17/09 | VIP Week, 1 | VIP Day just became VIP WEEK | Your coupon is still valid until Sunday | 1.039 | 27,6% | 2,0% | 21 | 1 | US$ 59,21 | 3 |

Nenhuma campanha teve reclamação de spam. A campanha "VIP Week, 2", de 19/09, estava em envio no momento da coleta e ficou de fora.

### 17.5 Leitura por tipo de campanha

| Tipo | Campanhas | Envios | Abertura | Clique | Pedidos | Receita | Receita por envio | Descadastro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dia de pico (8.8, 9.9, VIP Day) | 9 | 4.705 | 35,1% | 2,38% | 3 | US$ 249,72 | US$ 0,053 | 0,13% |
| Esquenta e antecipação, sem oferta | 5 | 2.332 | 35,8% | 2,74% | 4 | US$ 498,01 | US$ 0,214 | 0,30% |
| Recorrentes (Sextou, Segunda Turbo, UGC, catálogos) | 5 | 1.189 | 36,2% | 3,45% | 3 | US$ 672,39 | US$ 0,566 | 0,59% |
| Semana de 15% (3 ângulos) | 3 | 913 | 41,9% | 3,40% | 0 | 0 | 0 | 0,11% |
| Ressaca | 2 | 636 | 37,4% | 2,99% | 0 | 0 | 0 | 0,16% |
| Extensão (VIP Week) | 1 | 1.039 | 27,6% | 2,02% | 1 | US$ 59,21 | US$ 0,057 | 0,29% |
| **Total** | 25 | 10.814 | 35,4% | 2,66% | 11 | US$ 1.479,33 | US$ 0,137 | 0,23% |

Leitura por ciclo:

| Ciclo | E-mails | Envios | Cliques | Pedidos | Receita |
| --- | --- | --- | --- | --- | --- |
| 8.8 (3 disparos e ressaca) | 4 | 387 | 17 | 0 | 0 |
| 9.9 (4 de esquenta, 3 disparos, ressaca) | 8 | 3.756 | 88 | 6 | US$ 683,51 |
| VIP Day e VIP Week (antecipação, 3 disparos, extensão) | 5 | 4.569 | 111 | 2 | US$ 123,43 |

**Aviso de amostra.** São 11 pedidos em 25 campanhas. Com zero a três pedidos por envio, o ranking por receita é ruído: a Sextou lidera por causa de um único pedido de US$ 538. Nesta loja, o que dá para ler com alguma segurança é abertura e clique. Receita por tipo de campanha só vira dado quando as 15 lojas forem somadas (seção 17.10).

Dos 288 cliques únicos somados saíram 11 pedidos: 3,8% de conversão de clique em pedido. É uma taxa normal de loja. O problema está antes: cada campanha gera entre 3 e 28 cliques.

### 17.6 Automações, mensagem a mensagem

Duas mensagens carregam a conta: o primeiro e-mail do welcome (US$ 1.827) e o primeiro e-mail do checkout abandonado (US$ 1.281 somando as duas variantes). Juntas são 47% de toda a receita de e-mail da loja.

| Automação | Mensagens | Envios | Abertura | Clique | Pedidos | Receita | Receita por envio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Welcome Series | 8 | 3.127 | 33,8% | 1,98% | 22 | US$ 2.134,51 | US$ 0,68 |
| Checkout Abandoned | 9 | 3.121 | 33,5% | 2,31% | 20 | US$ 1.772,52 | US$ 0,57 |
| Upsell | 4 | 1.430 | 49,9% | 4,69% | 4 | US$ 349,32 | US$ 0,24 |
| Cart Abandoned | 9 | 1.122 | 34,9% | 2,14% | 3 | US$ 343,28 | US$ 0,31 |
| Shipment Tracking | 2 | 815 | 69,3% | 36,3% | 1 | US$ 250,45 | US$ 0,31 |
| Site Abandoned | 1 | 280 | 46,1% | 1,07% | 1 | US$ 160,56 | US$ 0,57 |
| Confirmação de pedido e separação | 4 | 1.493 | 65,6% | 3,62% | 1 | US$ 92,18 | US$ 0,06 |
| Viewed Product | 5 | 1.057 | 36,3% | 1,61% | 0 | 0 | 0 |
| Winback | 1 | 80 | 45,0% | 1,25% | 0 | 0 | 0 |

Welcome, por posição na sequência:

| Posição | Envios | Abertura | Clique | Pedidos | Receita |
| --- | --- | --- | --- | --- | --- |
| E-mail 1 | 497 | 41,6% | 6,04% | 18 | US$ 1.826,65 |
| E-mail 2 | 432 | 31,9% | 1,39% | 0 | 0 |
| E-mail 3 | 418 | 32,1% | 1,91% | 3 | US$ 193,76 |
| E-mail 4 | 388 | 32,2% | 1,55% | 0 | 0 |
| E-mail 5 | 369 | 32,2% | 1,08% | 1 | US$ 114,10 |
| E-mail 6 | 353 | 33,4% | 0,85% | 0 | 0 |
| E-mail 7 | 341 | 30,8% | 0,29% | 0 | 0 |
| E-mail 8 | 329 | 33,7% | 1,22% | 0 | 0 |

O e-mail 1 faz 86% da receita do welcome e 82% dos pedidos. Bate com o dado do Max de que 77% de quem converte o faz no dia zero (seção 2.5). Os e-mails 6, 7 e 8 somam 1.023 envios, 8 cliques e nenhum pedido.

Checkout abandonado, por posição:

| Posição | Envios | Abertura | Clique | Pedidos | Receita |
| --- | --- | --- | --- | --- | --- |
| E-mail 1, variante A | 276 | 36,6% | 4,71% | 7 | US$ 574,25 |
| E-mail 1, variante B | 256 | 43,0% | 5,47% | 7 | US$ 706,75 |
| E-mail 2 | 420 | 37,6% | 2,38% | 4 | US$ 305,87 |
| E-mail 3 | 405 | 34,8% | 2,72% | 2 | US$ 185,65 |
| E-mails 4 a 8 | 1.764 | 30,4% | 1,36% | 0 | 0 |

Do e-mail 4 em diante: 1.764 envios, nenhum pedido e 3 descadastros. No carrinho abandonado o padrão é parecido: 9 mensagens, 3 pedidos. O Viewed Product tem 5 mensagens, 1.057 envios e nenhum pedido.

Isso confirma com dado da própria carteira o que o Max faz por prática: abandono com 2 a 3 e-mails (seção 7). As posições finais não vendem e consomem volume de envio numa conta nova.

Os transacionais têm a maior atenção da conta: rastreio com 69% de abertura e 36% de clique, confirmação com 66% de abertura. Geram US$ 343. É o espaço menos aproveitado: o Max coloca ali o e-mail de texto do fundador com "a oferta continua" (seção 7).

### 17.7 Pontos positivos e por quê

| Ponto positivo | Evidência | Por que funciona |
| --- | --- | --- |
| Reputação limpa | Zero reclamação de spam em 10.823 envios de campanha. Descadastro de 0,23%. Falha de 0,60% | A lista veio quase toda de pop-up com consentimento, e o volume cresceu aos poucos: de 88 para 553 contatos em cinco semanas |
| Assunto de mudança de status | "Your status has just changed" teve 63,2% de abertura no 8.8 e 48,9% no 9.9, contra 34% dos outros disparos do mesmo dia | Promete uma novidade sobre a pessoa, não sobre a loja. É o mesmo princípio do "Your order is ready to ship" do Max (seção 8.4) |
| Terceiro disparo do dia, às 18h | No 9.9 foi o de maior abertura e o único com pedido além do primeiro | Pega quem não abriu de manhã. Confirma que vários disparos no dia de pico valem a pena |
| E-mail da véspera | "You have something scheduled for tomorrow", de 08/09: 3 pedidos e US$ 386, a melhor campanha de setembro | Parte da lista compra quando é lembrada, mesmo sem cupom. Há demanda antes do pico |
| Confirmação de lista | "Confirmed: you're on the list for tomorrow", de 14/09: 42,5% de abertura e 28 cliques, o maior número de cliques da conta | Confirmação pessoal gera clique. É o momento de maior intenção da sequência |
| Campanhas recorrentes com mecânica de jogo | "Are you among the first 100?" com 5,1% de clique. Recorrentes têm o melhor clique médio, 3,45% | Desafio com resultado imediato no checkout |
| Welcome e checkout, e-mail 1 | US$ 3.108 em duas mensagens | Chegam no momento de intenção. A variante B do checkout abre 43% contra 36,6% da A |
| Personalização com primeiro nome | 7 dos 25 assuntos usam o nome, captado no pop-up | O campo de nome no pop-up custa conversão (seção 17.8), mas é usado |

### 17.8 Gargalos e por quê

| Gargalo | Evidência | Por quê | O que fazer |
| --- | --- | --- | --- |
| 1. Lista pequena para o tráfego | 31.070 exibições de pop-up viraram 486 inscritos: 1,56%. Cerca de 83 por semana | Dois campos no celular (95% do tráfego), oferta genérica de 10%, sem etapa de telefone, uma exibição por dia | Testar pop-up de um campo com o nome na segunda etapa. Pop-up por evento (seção 7). Passo de SMS com a frase de ativação do desconto (seção 8.1). Cada ponto de conversão a mais rende cerca de 50 inscritos por semana |
| 2. Poucos cliques por campanha | 2,66% de clique. Entre 3 e 28 pessoas clicam em cada envio. No dia de pico o clique é o mais baixo de todos os tipos: 2,38% | A conversão de clique em pedido é normal (3,8%). Falta gente chegando ao site. E-mails de pico longos e com cupom digitado pedem esforço antes do clique | E-mail de pico curto, com CTA acima da dobra e desconto automático (seção 16.11). Reenvio para não abridores. Texto puro intercalado |
| 3. A maior intenção não tem onde comprar | O e-mail de confirmação de 14/09 teve 28 cliques e zero pedido. O esquenta do 9.9 vendeu mais (US$ 498) que os três disparos do dia (US$ 186) | O esquenta aponta para a loja sem oferta ativa. Quem clica na véspera encontra preço cheio | Dar algo para fazer no clique: página de espera com cadastro de telefone, lista de desejos, ou acesso antecipado real para quem clicou. É o ponto em que o dado da loja concorda com o Max: não deixar a janela sem oferta (seção 15.7) |
| 4. Importação manual de 424 contatos em 14/09 | Envio foi de 553 para 994 de um dia para o outro. Abertura caiu de 42,5% para 32,9%, 32,0%, 29,9% e 27,6%. Receita por envio caiu de US$ 0,28 no esquenta do 9.9 para US$ 0,02 no VIP Day. Descadastros por envio subiram de 1 para 3 | Os contatos novos não pediram para receber. O segmento único também inclui "não inscritos" | Risco de reputação numa conta de sete semanas, a dois meses da BF, e risco de consentimento (loja com público no Reino Unido e na UE). Separar esses contatos em segmento próprio, enviar só a quem abrir ou clicar, e não repetir importação sem opt-in antes de novembro. É o perfil de conta nível C (seção 6.3) |
| 5. Um segmento só | Todas as 25 campanhas foram para "TODOS OS LEADS" | Não há engajados 30, 60 ou 90 dias, nem compradores, nem quem clicou | Criar os segmentos de engajamento e o segmento de quem clicou na semana. Sem eles não dá para aplicar nenhuma regra da seção 6 nem a lista VIP real (seção 16.10) |
| 6. Flows longos demais | Welcome com 8 e-mails: 86% da receita no primeiro. Checkout com 8 posições: zero pedido da quarta em diante em 1.764 envios. Viewed Product: 5 e-mails, zero pedido | A decisão acontece nas primeiras horas | Cortar para 3 e-mails no abandono e rever as posições 6 a 8 do welcome. Na BF, 2 por flow (seção 7) |
| 7. Transacionais sem oferta | Rastreio com 69% de abertura e 36% de clique gera US$ 250 | São os e-mails mais lidos da conta e só informam | Bloco de "a oferta continua" e cross-sell no rastreio e na confirmação |
| 8. Erros de digitação na base | Envios para gnail.com, gamil.com, gmaiil.com, hotnail.com, gmail.co, gmail.con, gmail.vom | Pop-up sem validação de domínio | Limpar e ativar validação. Cada envio inválido conta como falha |
| 9. Ressaca e semana de 15% sem pedido | 2 ressacas e 3 e-mails da semana de 15%: 1.549 envios, nenhum pedido | Amostra pequena, mas a ressaca repete a oferta que já não converteu | Na ressaca, trocar a mecânica em vez de estender (seção 4.1) |
| 10. Sem SMS, push ou WhatsApp | Nenhum envio fora do e-mail | Pop-up não capta telefone | Começar a captar agora: não dá para captar retroativamente (seção 8) |

Ordem de impacto para a BF: 1, 4 e 5 primeiro, porque definem quantas pessoas recebem e se a conta aguenta o volume. Depois 2 e 3, que definem quanto cada envio rende. O resto é ajuste.

### 17.9 O que desta loja é reaproveitável na Black Friday

| Reaproveitar | Onde |
| --- | --- |
| Assunto de mudança de status ("Your status has just changed") | Disparo da tarde de 11/11 e de 27/11 |
| Três disparos no dia de pico, com o das 18h | 11/11, 27/11 e 30/11 |
| E-mail da véspera com horários | 10/11 e 26/11, agora com link para algo que converta |
| E-mail de confirmação de lista | 02/11 e 23/11, com o botão que grava a tag VIP (seção 16.10) |
| Mecânica "primeiros 100" com resultado no checkout | Dias do meio da Black Week |
| E-mail 1 do welcome e do checkout, variante B | Base dos flows em modo BFCM |

| Não repetir | Motivo |
| --- | --- |
| Importar contatos sem opt-in perto do pico | Derrubou abertura e receita por envio em um dia |
| Enviar tudo para um segmento só | Impede proteger a reputação |
| Ressaca com a mesma oferta | Zero pedido nas duas vezes |
| Flow de abandono com mais de 3 e-mails | Zero pedido da quarta posição em diante |

### 17.10 Protocolo para as próximas lojas e para consolidar

Uma loja sozinha tem pedidos de menos para dizer o que performa. Somando 15 lojas com o mesmo calendário, cada tipo de campanha passa a ter centenas de pedidos, e aí o ranking vira dado. Para isso, toda loja precisa ser lida do mesmo jeito.

O que é coletado em cada loja, sempre nos últimos 90 dias:

1. Identificação: loja, mercado, moeda, idade da conta, tamanho do segmento principal.
2. Receita total da loja e receita atribuída por semana, separada em campanha e automação.
3. Todas as campanhas enviadas: data, hora, nome, assunto, pré-cabeçalho, segmento, envios, abertura, clique, cliques únicos, pedidos, receita, descadastro, spam, falha.
4. Todas as automações, mensagem a mensagem, com os mesmos números.
5. Pop-up: exibições, envios, inscritos, por dispositivo. Campos pedidos e oferta.
6. Origem dos inscritos por semana, para detectar importação manual.
7. Segmentos existentes e suas regras.

Como cada campanha é classificada, a partir do padrão de nome que a Convertfy já usa:

| Campo | Valores |
| --- | --- |
| Ciclo | 7.7, 8.8, 9.9, VIP Day, semana de desconto, avulsa |
| Papel | Esquenta, véspera, pico disparo 1, pico disparo 2, pico disparo 3, ressaca, extensão, recorrente |
| Ângulo do assunto | Status ou acesso, lista ou seleção, cupom liberado, prazo, pergunta, encaminhado ("Fwd:"), lembrete de agenda, perda |
| Usa primeiro nome | Sim ou não |
| Usa emoji | Sim ou não |
| Oferta | Tipo e percentual |

Métricas de comparação entre lojas, sempre normalizadas:

- Abertura e clique por papel e por ângulo de assunto.
- Receita por mil envios, por papel.
- Conversão de clique em pedido, por loja.
- Participação do e-mail na receita da loja.
- Receita do welcome por posição e do checkout por posição.
- Conversão do pop-up.
- Queda de abertura depois de qualquer salto de lista.

Regra para declarar um padrão: aparecer em pelo menos 10 das 15 lojas, ou somar 100 pedidos no agregado. Abaixo disso entra como hipótese.

Limite prático da API da Omnisend: 55 consultas de análise por dia por conta. Esta loja usou 4. O detalhamento por domínio de e-mail devolve uma resposta grande demais e não deve ser repetido: a consulta por tipo de falha resolve.

O que ainda falta nesta loja:

- [ ] Ler o corpo e o layout de 3 campanhas de topo e 3 de fundo, para ligar estrutura a clique
- [ ] Ver as regras e os tempos de espera de cada automação
- [ ] Cruzar os cupons do 9.9 e do VIP Day com os pedidos no Shopify
- [ ] Confirmar de onde vieram os 424 contatos de 14/09 e se há consentimento

## 18. Análise de contas Omnisend: loja 2, Blue Wolf

A Blue Wolf é a primeira loja com volume para ler receita por tipo de campanha: 46 campanhas, 742 mil envios, 389 pedidos e US$ 32.338 em três meses. O melhor formato é o e-mail que imita uma notificação de sistema, o melhor horário é o disparo das 18h do dia de pico, e o pior formato é prova social. \[D, API da Omnisend, coleta em 18/09/2026\]

Dados de 17/06 a 18/09/2026, em dólar. Conta criada em abril de 2026. Loja wolfbluestore.com, em inglês. Lista de envio entre 13,6 mil e 16,8 mil contatos. Só e-mail.

### 18.1 Números por mês

| Mês | Campanhas | Envios | Abertura | Clique | Pedidos | Receita | Receita por mil envios | Descadastro | Spam por 100 mil |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Junho, a partir de 17/06 | 3 | 41.070 | 34,3% | 1,90% | 23 | US$ 1.753 | US$ 42,69 | 0,44% | 21,9 |
| Julho | 15 | 222.646 | 36,2% | 1,87% | 159 | US$ 12.484 | US$ 56,07 | 0,57% | 28,3 |
| Agosto | 15 | 239.656 | 36,0% | 1,71% | 108 | US$ 9.394 | US$ 39,20 | 0,45% | 14,2 |
| Setembro, até 17/09 | 13 | 238.669 | 31,7% | 1,92% | 99 | US$ 8.706 | US$ 36,48 | 0,31% | 13,0 |
| **Total** | 46 | 742.041 | 34,6% | 1,84% | 389 | US$ 32.338 | US$ 43,58 | 0,44% | 18,5 |

Ficaram fora da tabela cinco envios pequenos de teste (570 a 961 contatos), a reativação de 17/08 e o envio de 19/09, ainda em andamento.

Julho foi o melhor mês: mesmo número de campanhas que agosto, 47% mais pedidos. A receita por mil envios cai mês a mês desde então. Setembro teve 13 envios em 17 dias, e a abertura caiu para 31,7% porque o esquenta do 9.9 foi para um segmento maior (seção 18.5).

Conversão de clique em pedido: 2,9% no período, contra 3,8% na Emyerre.

### 18.2 Automações, 17/06 a 18/09

| Automação | Envios | Abertura | Clique | Pedidos | Receita | Receita por mil envios |
| --- | --- | --- | --- | --- | --- | --- |
| Welcome Series | 94.856 | 27,4% | 2,86% | 415 | US$ 37.711 | US$ 398 |
| Checkout abandonado | 40.838 | 29,6% | 4,57% | 317 | US$ 30.315 | US$ 742 |
| Shipment Tracking | 26.010 | 65,3% | 27,1% | 89 | US$ 10.414 | US$ 400 |
| Abandoned Cart | 27.922 | 30,2% | 4,05% | 101 | US$ 9.103 | US$ 326 |
| Viewed Product | 54.131 | 31,9% | 3,33% | 100 | US$ 8.914 | US$ 165 |
| Upsell | 17.366 | 50,2% | 6,35% | 76 | US$ 6.322 | US$ 364 |
| Em trânsito | 4.188 | 71,3% | 43,1% | 29 | US$ 2.471 | US$ 590 |
| Pedido entregue | 4.449 | 58,4% | 10,8% | 22 | US$ 2.045 | US$ 460 |
| Site Abandoned | 3.647 | 39,1% | 4,85% | 15 | US$ 1.110 | US$ 304 |
| Em rota de entrega | 4.106 | 56,6% | 20,9% | 8 | US$ 651 | US$ 158 |
| Winback | 6.684 | 36,4% | 2,77% | 10 | US$ 592 | US$ 89 |
| Pronto para retirada e tentativa falhada | 279 | 71,7% | 44,1% | 1 | US$ 152 |  |
| **Total** | 284.476 |  |  | 1.183 | US$ 109.800 | US$ 386 |

As automações fazem 77% da receita de e-mail, a mesma proporção da Emyerre (78%). Campanha rende US$ 44 por mil envios. Automação rende US$ 386, quase nove vezes mais.

A régua de logística (rastreio, em trânsito, em rota, entregue) soma US$ 15.580, 14% da receita de automação. Na Emyerre esse espaço rende US$ 343 e apareceu como gargalo 7. Aqui está implementado e paga. É padrão para replicar.

O Viewed Product, que na Emyerre não vendeu nada, aqui fez 100 pedidos. A diferença é volume: 54 mil envios contra mil.

### 18.3 Campanha a campanha

Colunas: abertura, clique, pedidos, receita e receita por mil envios (RPM). A estratégia foi lida do nome interno, do assunto e do pré-cabeçalho. O corpo dos e-mails é feito de imagens e a API não entrega o texto (seção 18.7).

#### Junho

| Data | Campanha e estratégia | Assunto | Abert. | Clique | Ped. | Receita | RPM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 17/06 | Semana Copa 2. Tema do momento: cartão vermelho para quem perde a oferta | A red card for anyone who misses out on these deals... | 37,6% | 3,07% | 12 | US$ 896 | 65,9 |
| 19/06 | Álbum de figurinha. Gamificada: código revela o desconto. Único envio para "leads engajados" | You've unlocked the golden sticker | 36,4% | 1,60% | 6 | US$ 513 | 37,5 |
| 26/06 | Social proof. Prova social de clientes | What do they know that you don't yet? | 29,1% | 1,04% | 5 | US$ 344 | 24,9 |

#### Julho

| Data | Campanha e estratégia | Assunto | Abert. | Clique | Ped. | Receita | RPM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01/07 | Antecipação 7.7, 1. Convite com pedido de confirmação de presença | \[Nome\], you have received an invitation | 41,0% | 2,46% | 8 | US$ 654 | 46,8 |
| 03/07 | Antecipação 7.7, 2. Agenda do evento liberada | \[Nome\], have you seen what is coming? | 44,3% | 1,90% | 14 | US$ 1.171 | 84,1 |
| 06/07 | Antecipação 7.7, 3. Véspera: acesso pendente, confirmar horários | Your access for tomorrow is still pending | 39,2% | 1,56% | 7 | US$ 874 | 63,5 |
| 07/07 07h | 7.7, disparo 1. Cupom aprovado, até meia-noite | Your coupon has been approved | 40,2% | 1,47% | 6 | US$ 337 | 24,6 |
| 07/07 11h | 7.7, disparo 2. Oferta só para quem rola até o fim | Scroll to the end of this email (there's a surprise) | 33,1% | 1,27% | 12 | US$ 738 | 53,9 |
| 07/07 18h | 7.7, disparo 3. Última chamada | \[FINAL CALL\] Expires at 11:59 PM | 38,8% | 3,06% | 14 | US$ 1.435 | 105,3 |
| 15/07 | Favoritos do 7.7. Ressaca tardia: os mais vendidos do evento, enquanto durar | \[Nome\], your 7.7 favorites are waiting for you | 36,7% | 3,19% | 14 | US$ 1.121 | 71,3 |
| 18/07 | Final da Copa. Seleção para "clientes especiais" | \[Nome\], I've set something aside just for our special customers | 34,8% | 2,30% | 13 | US$ 863 | 55,5 |
| 20/07 | Revele seu desconto. Gamificada: botão "Reveal now" | (1) hidden discount for \[nome\] inside this email | 35,8% | 1,66% | 18 | US$ 1.066 | 68,5 |
| 22/07 | Jornal. Notificação: a notícia que você não queria ouvir, oferta até sexta | \[Nome\], the news you did not want to hear has arrived... | 35,3% | 2,04% | 15 | US$ 1.123 | 71,9 |
| 24/07 | Ligação. Notificação: chamada recebida, última chance do dia | \[Nome\], you have an incoming call | 34,5% | 1,69% | 11 | US$ 756 | 49,0 |
| 25/07 | Reabertura. Um dia a mais de cupom | I decided to reopen everything for one more day. | 36,7% | 1,23% | 8 | US$ 776 | 50,1 |
| 27/07 | Segunda da sorte. Gamificada: ofertas da semana | Careful: this email contains luck | 34,6% | 1,82% | 3 | US$ 267 | 17,2 |
| 29/07 | UGC social proof. Depoimento de recompra | "I came back to buy again because..." | 26,6% | 0,91% | 7 | US$ 522 | 33,6 |
| 31/07 | Sexta premiada. Recompensa com resgate até sábado | You've received a reward today | 33,4% | 1,58% | 9 | US$ 782 | 50,2 |

#### Agosto

| Data | Campanha e estratégia | Assunto | Abert. | Clique | Ped. | Receita | RPM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 03/08 | Esquenta 8.8, 1. Anúncio: ofertas já no ar, mais chegando | The 8.8 Warm-Up Has Begun | 34,0% | 1,22% | 1 | US$ 73 | 4,6 |
| 05/08 | Esquenta 8.8, 2. Curiosidade, faltam 3 dias | There's a good reason to open this email | 34,1% | 0,99% | 6 | US$ 478 | 30,7 |
| 07/08 | Esquenta 8.8, 3. Véspera com horários | Tomorrow is 8.8. Are you ready? | 34,1% | 1,32% | 10 | US$ 718 | 45,9 |
| 08/08 07h | 8.8, disparo 1. E-mail "encaminhado": coloquei seu nome na lista | Fwd: I was able to add your name to this list | 39,0% | 1,19% | 7 | US$ 504 | 32,1 |
| 08/08 11h | 8.8, disparo 2. Válido para os 100 primeiros | This email is only valid for the first 100 | 33,9% | 1,31% | 8 | US$ 572 | 36,5 |
| 08/08 18h | 8.8, disparo 3. Notificação de status | Your status has just changed | 42,2% | 2,09% | 18 | US$ 1.674 | 107,5 |
| 11/08 | Ressaca 8.8. Perdeu? ainda dá tempo | Missed our 8.8 sale? There's still time... | 38,7% | 1,23% | 8 | US$ 629 | 40,4 |
| 14/08 | Sextou. Oferta de fim de semana | Your Friday deserves this... | 34,6% | 1,41% | 6 | US$ 544 | 34,9 |
| 17/08 | Segunda turbo. Gamificada: aplique o código e descubra se está entre os 100 | Are you among the first 100? | 33,8% | 1,50% | 6 | US$ 950 | 60,4 |
| 19/08 | UGC Dia da Fotografia. Fotos de clientes | Yours is missing here... | 32,3% | 1,01% | 5 | US$ 408 | 24,9 |
| 21/08 | Catálogo indecisão. Catálogo contra paralisia de escolha | Either you choose today, or you keep putting it off... | 34,1% | 1,89% | 5 | US$ 395 | 24,1 |
| 24/08 | Semana de 15%, 1: On & Off. Desconto ativado até sexta | I've activated a discount for you | 37,8% | 2,89% | 8 | US$ 779 | 47,2 |
| 26/08 | Semana de 15%, 2: Escolha o caminho | \[Nome\], choose your path... | 37,4% | 0,97% | 3 | US$ 208 | 12,6 |
| 28/08 | Semana de 15%, 3: Notificação do futuro. Notificação de pedido a confirmar | \[Nome\], you still need to confirm your order... | 37,0% | 3,61% | 9 | US$ 648 | 39,1 |
| 31/08 | Catálogo fecha mês. Preços de agosto até meia-noite | Ignore this email after 11:59 PM | 36,2% | 2,91% | 8 | US$ 815 | 49,1 |

#### Setembro

| Data | Campanha e estratégia | Assunto | Abert. | Clique | Ped. | Receita | RPM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 03/09 | Esquenta 9.9, 1. E-mail "vazado": seu nome está na lista. Segmento de 22 mil | Fwd: You Were Not Supposed to Know About This | 29,3% | 0,83% | 4 | US$ 482 | 22,2 |
| 05/09 | Esquenta 9.9, 2. Aviso dos três horários. 22 mil | I promised I'd let you know in advance, \[nome\] | 27,5% | 2,30% | 12 | US$ 730 | 33,4 |
| 07/09 | Esquenta 9.9, 3. Acesso antecipado garantido. 22 mil | \[Nome\], you've secured early access | 26,0% | 2,21% | 3 | US$ 287 | 13,0 |
| 08/09 | Esquenta 9.9, 4. Véspera: compromisso agendado. 22 mil | \[Nome\], you have something scheduled for tomorrow | 28,8% | 2,42% | 5 | US$ 427 | 19,3 |
| 09/09 07h | 9.9, disparo 1. Cupom liberado | Your coupon has been released | 35,3% | 1,15% | 13 | US$ 1.216 | 72,3 |
| 09/09 11h | 9.9, disparo 2. Acesso concedido, só hoje | Your access has been granted (today only) | 34,9% | 2,70% | 7 | US$ 512 | 30,5 |
| 09/09 18h | 9.9, disparo 3. Notificação de status | Your status has just changed | 41,8% | 3,56% | 15 | US$ 1.028 | 61,4 |
| 11/09 | Ressaca 9.9. Tom de comunicado: estoque baixo, preço promocional mantido | We regret to inform you that... | 34,6% | 3,20% | 14 | US$ 1.303 | 77,7 |
| 14/09 | Antecipação VIP Day. Confirmação de lista, cupom só por e-mail às 7h | Confirmed: you're on the list for tomorrow | 33,5% | 1,54% | 5 | US$ 441 | 26,2 |
| 15/09 07h | VIP Day, disparo 1. Você foi selecionado | \[Nome\], you've been selected | 33,2% | 1,27% | 5 | US$ 542 | 32,3 |
| 15/09 11h | VIP Day, disparo 2. Você foi aprovado? | Were you approved? | 31,7% | 1,14% | 6 | US$ 847 | 50,5 |
| 15/09 18h | VIP Day, disparo 3. Prêmio reservado | Prize reserved for \[nome\] | 31,3% | 1,37% | 4 | US$ 324 | 19,4 |
| 17/09 | VIP Week, 1. O dia virou semana, cupom até domingo | VIP Day just became VIP WEEK | 29,5% | 1,24% | 6 | US$ 567 | 33,9 |

Caso à parte, 17/08, reativação de base não engajada ("You're being removed from our list!"): 18.699 envios, 7,3% de abertura, 120 cliques, 1 pedido, US$ 78, 68 descadastros e 3 reclamações de spam. Em agosto as falhas de entrega da conta foram de cerca de 1.300 por mês para 3.213.

### 18.4 Como as datas duplas foram antecipadas

O modelo é sempre o mesmo: 3 a 4 e-mails de antecipação sem cupom, três disparos no dia (7h, 11h, 18h) e uma ressaca. É o mesmo desenho do 11.11 de 2025 (seção 15), em escala mensal.

| Ciclo | Antecipação | Dia de pico | Depois | Total do ciclo |
| --- | --- | --- | --- | --- |
| 7.7 | 3 e-mails em 6 dias (convite, agenda, acesso pendente): 29 pedidos, US$ 2.700 | 3 disparos: 32 pedidos, US$ 2.510 | Favoritos do 7.7, oito dias depois: 14 pedidos, US$ 1.121 | 75 pedidos, US$ 6.330 |
| 8.8 | 3 e-mails em 5 dias (warm-up, curiosidade, véspera): 17 pedidos, US$ 1.269 | 3 disparos: 33 pedidos, US$ 2.749 | Ressaca em 11/08: 8 pedidos, US$ 629 | 58 pedidos, US$ 4.646 |
| 9.9 | 4 e-mails em 6 dias para segmento de 22 mil: 24 pedidos, US$ 1.926 | 3 disparos: 35 pedidos, US$ 2.756 | Ressaca em 11/09: 14 pedidos, US$ 1.303 | 73 pedidos, US$ 5.986 |
| VIP Day, 15/09 | 1 e-mail na véspera: 5 pedidos, US$ 441 | 3 disparos: 15 pedidos, US$ 1.713 | VIP Week: 6 pedidos, US$ 567 | 26 pedidos, US$ 2.721 |

Quatro leituras:

1. **A antecipação vende, mesmo sem cupom.** No 7.7 os três e-mails de antecipação venderam mais (US$ 2.700) que os três disparos do dia (US$ 2.510). No 8.8 e no 9.9 fizeram 46% e 70% da receita do pico. Na Emyerre o padrão foi o mesmo. Já são duas lojas de duas: existe demanda antes do pico, e ela está comprando a preço cheio ou com o cupom de boas-vindas.
2. **A melhor antecipação foi a do 7.7**, com tom de convite e agenda: aberturas de 41%, 44% e 39%, as mais altas do trimestre. O esquenta do 8.8, com tom de anúncio ("The 8.8 Warm-Up Has Begun"), foi o pior: 1 pedido no primeiro e-mail.
3. **O dia de pico rende quase igual nos três meses**: 32, 33 e 35 pedidos. O que muda o total do ciclo é a antecipação e a ressaca.
4. **O VIP Day rendeu cerca de 35% menos que os outros picos.** Veio seis dias depois do 9.9, no 10º envio do mês. É o primeiro sinal de fadiga de oferta na carteira, e é exatamente o risco entre o 11.11 e a BF.

### 18.5 Lista maior não trouxe abertura

O esquenta do 9.9 foi para um segmento de 22 mil contatos, contra 16,8 mil dos outros envios do mês. Os 5,2 mil contatos a mais (31%) não abriram: as aberturas ficaram entre 5.732 e 6.370, a mesma faixa dos envios para a lista menor (5.319 a 6.998). A taxa de abertura caiu para 26 a 29% e a receita por mil envios ficou em US$ 22, contra US$ 55 dos disparos do pico.

É o teste interno do argumento do Max (seção 6.1). Lá, abrir o envio em 19% trouxe 19% mais aberturas. Aqui, abrir em 31% trouxe zero. Somado à reativação de 17/08 (18.699 envios, 1 pedido), o dado da carteira diz que contato inativo não volta com envio comum. Se volta com a oferta da BF, como o Max afirma, ainda é hipótese, e só deve ser testada em conta nível A.

### 18.6 Ranking por formato

| Formato | Campanhas | Abertura | Clique | Pedidos | Receita por mil envios | Descadastro |
| --- | --- | --- | --- | --- | --- | --- |
| Pico, disparo das 18h | 4 | 38,4% | 2,50% | 51 | US$ 71,22 | 0,55% |
| Temática do momento (Copa) | 2 | 36,1% | 2,66% | 25 | US$ 60,37 | 0,55% |
| Ressaca e reabertura | 4 | 36,6% | 2,24% | 44 | US$ 60,27 | 0,48% |
| Notificação de sistema (Jornal, Ligação, pedido a confirmar) | 3 | 35,6% | 2,47% | 35 | US$ 53,05 | 0,53% |
| Gamificada (revele, figurinha, primeiros 100, sorte, premiada) | 5 | 34,7% | 1,63% | 42 | US$ 47,04 | 0,46% |
| Pico, disparo das 11h | 4 | 33,4% | 1,63% | 33 | US$ 42,43 | 0,36% |
| Pico, disparo das 7h | 4 | 36,7% | 1,26% | 31 | US$ 41,27 | 0,45% |
| Catálogo | 2 | 35,2% | 2,41% | 13 | US$ 36,65 | 0,45% |
| Véspera | 4 | 33,3% | 1,78% | 27 | US$ 36,02 | 0,44% |
| Esquenta | 7 | 32,6% | 1,70% | 48 | US$ 31,05 | 0,42% |
| Semana de 15% | 2 | 37,6% | 1,93% | 11 | US$ 29,88 | 0,40% |
| Prova social e UGC | 3 | 29,4% | 0,99% | 17 | US$ 27,89 | 0,34% |

O disparo das 18h foi o melhor do dia no 7.7, no 8.8 e no 9.9 (14, 18 e 15 pedidos). Só perdeu no VIP Day, quando o assunto trocou o tom de notificação por "Prize reserved" (4 pedidos).

### 18.7 O que se sabe do template

A campanha de maior receita (8.8 das 18h) foi lida pela API. Estrutura: seis fatias de imagem no topo (100, 210, 415, 613, 260 e 192 px), um bloco dinâmico de quatro produtos em grade 2x2 ("vistos recentemente", com os mais populares como reserva), três fatias finais (159, 381 e 303 px) e o rodapé de descadastro. Cerca de 3.600 px no total.

- O e-mail é 100% imagem. Não há texto vivo além do bloco de produtos.
- **Todas as fatias apontam para a página inicial da loja**, não para a coleção ou para a oferta. Quem clica no cupom cai na home. É a hipótese mais forte para a conversão de clique em pedido de 2,9%.
- O bloco de produtos "vistos recentemente" personaliza o e-mail sem produção extra. Vale manter.

O texto dentro das imagens não é legível pela API. Para ligar layout a resultado, faltam as prints ou o link do Figma das cinco melhores e das cinco piores campanhas desta seção.

### 18.8 Melhores e piores

| Melhores, por receita por mil envios | RPM | Por quê |
| --- | --- | --- |
| 08/08 18h, "Your status has just changed" | US$ 107,5 | Notificação pessoal no último disparo do dia. 42% de abertura |
| 07/07 18h, "\[FINAL CALL\] Expires at 11:59 PM" | US$ 105,3 | Prazo explícito no assunto. 3,06% de clique |
| 03/07, "Have you seen what is coming?" | US$ 84,1 | Maior abertura do trimestre, 44,3%. Antecipação com agenda |
| 11/09, "We regret to inform you that..." | US$ 77,7 | Ressaca com tom de comunicado formal. 3,20% de clique |
| 09/09 07h, "Your coupon has been released" | US$ 72,3 | Só 1,15% de clique, mas 6,7% de quem clicou comprou. Pega quem já estava decidido |
| 22/07, "The news you did not want to hear has arrived" | US$ 71,9 | Notificação em formato de jornal, fora de data dupla |
| 15/07, "Your 7.7 favorites are waiting" | US$ 71,3 | Ressaca com os mais vendidos. 3,19% de clique |
| 20/07, "(1) hidden discount inside this email" | US$ 68,5 | Gamificada com revelação. 18 pedidos, recorde junto com o 8.8 das 18h |

| Piores | RPM | Por quê |
| --- | --- | --- |
| 03/08, "The 8.8 Warm-Up Has Begun" | US$ 4,6 | Anúncio genérico da marca. Nada sobre a pessoa |
| 26/08, "Choose your path..." | US$ 12,6 | Abre bem (37%) e ninguém clica (0,97%). O conceito pede esforço |
| 07/09, "You've secured early access" | US$ 13,0 | Terceiro esquenta seguido com a mesma promessa, para o segmento de 22 mil |
| 27/07, "This email contains luck" | US$ 17,2 | Gamificada sem mecânica clara no assunto |
| 15/09 18h, "Prize reserved" | US$ 19,4 | Pico fraco, seis dias depois do 9.9 |
| 08/09, véspera do 9.9 | US$ 19,3 | Mesmo e-mail que foi o melhor da Emyerre. Aqui foi para 22 mil |
| Prova social e UGC, três envios | US$ 24,9 a 33,6 | As menores aberturas (26,6 a 32,3%) e o menor clique da conta (cerca de 1%) |

### 18.9 Pontos positivos e gargalos

| Pontos positivos | Evidência |
| --- | --- |
| Régua de logística monetizada | US$ 15.580 em quatro fluxos transacionais |
| Reputação sob controle com volume alto | Spam de 18,5 por 100 mil envios (0,0185%), bem abaixo do limite de 0,1% |
| Assunto de notificação pessoal | Seis dos oito melhores usam status, cupom, prazo ou comunicado |
| Disparo das 18h | Melhor do dia em três picos de quatro |
| Ressaca | 44 pedidos e US$ 3.829 em quatro envios. Aqui funciona, ao contrário da Emyerre |

| Gargalo | Evidência | O que fazer |
| --- | --- | --- |
| Clique vai para a home | Todas as fatias do melhor e-mail apontam para a página inicial. Clique em pedido: 2,9% | Link para a coleção da oferta com o cupom já aplicado |
| Queda de rendimento mês a mês | US$ 56, US$ 39 e US$ 36 por mil envios. 13 envios em 17 dias em setembro | Espaçar picos. Não colar um evento no outro |
| Descadastro alto | 0,44% por envio, o dobro da Emyerre. Em três meses, 3.273 descadastros em campanhas | Segmentar por engajamento. O disparo das 18h do 8.8 sozinho perdeu 129 contatos |
| Segmento maior sem retorno | 5,2 mil contatos a mais, zero abertura a mais | Tirar os inativos do envio comum |
| Reativação sem resultado | 18.699 envios, 1 pedido, falhas de entrega dobraram no mês | Não repetir antes da BF |
| Prova social não vende por campanha | Pior formato nos três envios | Usar prova como bloco dentro de e-mail de oferta, não como e-mail próprio |
| Sem SMS, push ou WhatsApp | Só e-mail | Captar telefone desde já |

### 18.10 O que as duas lojas já dizem juntas

| Achado | Emyerre | Blue Wolf | Situação |
| --- | --- | --- | --- |
| Automações fazem perto de 78% da receita de e-mail | 78% | 77% | Repetiu |
| Antecipação sem cupom vende | Vendeu mais que o pico | 46% a 108% do pico | Repetiu |
| Disparo das 18h é o melhor do pico | Sim, no 9.9 | Sim, em 3 de 4 | Repetiu |
| "Your status has just changed" é o melhor assunto | 63% e 49% de abertura | 42% de abertura e maior receita | Repetiu |
| Ampliar o envio para quem não engaja derruba o resultado | Importação de 424 contatos | Segmento de 22 mil e reativação | Repetiu |
| Ressaca vende | Não | Sim | Divergiu. A Emyerre tem amostra pequena |
| Viewed Product vende | Não | Sim, 100 pedidos | Divergiu por volume |
| Régua de logística com oferta | Não tem | US$ 15.580 | Oportunidade para todas as contas |

Pelo critério da seção 17.10, nada disso é padrão ainda: são duas lojas de quinze. Mas a Blue Wolf sozinha já soma 115 pedidos em disparos de pico, acima do corte de 100, e os cinco achados repetidos são a base mais sólida do estudo até aqui.

## 19. Blue Wolf: o design de cada campanha ligado ao resultado

O que separa as melhores das piores campanhas da Blue Wolf é a primeira tela, não o tamanho do e-mail. As melhores abrem com um número de desconto, um cupom e um prazo. As piores abrem com um conceito e não têm oferta. A altura do e-mail não tem correlação com receita (r = -0,02) nem com clique (r = -0,05). \[D, Figma lido via conector em 18/09/2026, cruzado com a seção 18\]

Os três arquivos do Figma (julho, agosto, setembro) guardam as campanhas de todos os clientes, uma linha por loja. A linha da Blue Wolf foi localizada pelo rótulo da loja e os frames foram casados com as campanhas da Omnisend pela data no nome do frame. As imagens de cada campanha estão embutidas na seção 20, em fichas por mês. A tabela abaixo mantém o link direto para o frame no Figma.

### 19.1 Mapa das campanhas: frame, altura e resultado

RPM é a receita por mil envios.

| Data | Campanha | Altura | Abert. | Clique | Ped. | RPM | Frame |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01/07 | Antecipação 7.7, convite | 2.514 px | 41,0% | 2,46% | 8 | 46,8 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=1124-3517) |
| 03/07 | Antecipação 7.7, agenda | 3.133 px | 44,3% | 1,90% | 14 | 84,1 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3139-11059) |
| 07/07 11h | 7.7, disparo 2 | 3.414 px | 33,1% | 1,27% | 12 | 53,9 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3139-11682) |
| 07/07 18h | 7.7, disparo 3, last call | 3.178 px | 38,8% | 3,06% | 14 | 105,3 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3139-11215) |
| 15/07 | Favoritos do 7.7 | 2.520 px | 36,7% | 3,19% | 14 | 71,3 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3357-2827) |
| 18/07 | Final da Copa | 3.154 px | 34,8% | 2,30% | 13 | 55,5 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3493-4327) |
| 20/07 | Revele seu desconto | 2.169 px | 35,8% | 1,66% | 18 | 68,5 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3493-4473) |
| 22/07 | Jornal | 2.469 px | 35,3% | 2,04% | 15 | 71,9 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3589-6700) |
| 24/07 | Ligação | 2.312 px | 34,5% | 1,69% | 11 | 49,0 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3589-6548) |
| 27/07 | Segunda da sorte | 1.796 px | 34,6% | 1,82% | 3 | 17,2 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3728-18089) |
| 29/07 | UGC social proof | 3.960 px | 26,6% | 0,91% | 7 | 33,6 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3728-18345) |
| 31/07 | Sexta premiada | 1.934 px | 33,4% | 1,58% | 9 | 50,2 | [abrir](https://www.figma.com/design/6rrFgoIn3rLs89DTFQ5vpe/?node-id=3728-18218) |
| 03/08 | Esquenta 8.8, warm-up | 2.830 px | 34,0% | 1,22% | 1 | 4,6 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6014-1805) |
| 05/08 | Esquenta 8.8, 2 | 3.399 px | 34,1% | 0,99% | 6 | 30,7 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6014-1956) |
| 07/08 | Esquenta 8.8, véspera | 3.250 px | 34,1% | 1,32% | 10 | 45,9 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6014-2127) |
| 08/08 11h | 8.8, disparo 2 | 2.770 px | 33,9% | 1,31% | 8 | 36,5 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6208-111) |
| 08/08 18h | 8.8, disparo 3, status | 3.230 px | 42,2% | 2,09% | 18 | 107,5 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6208-264) |
| 11/08 | Ressaca 8.8 (frame nomeado "11/11") | 1.863 px | 38,7% | 1,23% | 8 | 40,4 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6208-439) |
| 14/08 | Sextou | 2.579 px | 34,6% | 1,41% | 6 | 34,9 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6555-2980) |
| 17/08 | Segunda turbo | 2.635 px | 33,8% | 1,50% | 6 | 60,4 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6555-3221) |
| 19/08 | UGC Dia da Fotografia | 2.803 px | 32,3% | 1,01% | 5 | 24,9 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6555-3110) |
| 21/08 | Catálogo indecisão | 3.121 px | 34,1% | 1,89% | 5 | 24,1 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6876-4936) |
| 24/08 | Semana 15%, On & Off | 3.210 px | 37,8% | 2,89% | 8 | 47,2 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=6876-5139) |
| 26/08 | Semana 15%, Escolha o caminho | 1.964 px | 37,4% | 0,97% | 3 | 12,6 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=7080-111) |
| 28/08 | Semana 15%, Notificação do futuro | 2.128 px | 37,0% | 3,61% | 9 | 39,1 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=7080-358) |
| 31/08 | Catálogo fecha mês | 3.012 px | 36,2% | 2,91% | 8 | 49,1 | [abrir](https://www.figma.com/design/hBrwHZnGuySRZvAEZFGUyD/?node-id=7080-231) |
| 05/09 | Esquenta 9.9, 2 | 2.661 px | 27,5% | 2,30% | 12 | 33,4 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9075-13126) |
| 07/09 | Esquenta 9.9, 3 | 3.207 px | 26,0% | 2,21% | 3 | 13,0 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9075-13263) |
| 08/09 | Esquenta 9.9, véspera | 3.767 px | 28,8% | 2,42% | 5 | 19,3 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9075-13423) |
| 09/09 11h | 9.9, disparo 2 | 4.136 px | 34,9% | 2,70% | 7 | 30,5 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9296-10897) |
| 09/09 18h | 9.9, disparo 3, status | 2.469 px | 41,8% | 3,56% | 15 | 61,4 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9296-11195) |
| 11/09 | Ressaca 9.9 | 1.735 px | 34,6% | 3,20% | 14 | 77,7 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9296-11324) |
| 14/09 | Antecipação VIP Day | 1.081 px | 33,5% | 1,54% | 5 | 26,2 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9517-19742) |
| 15/09 11h | VIP Day, disparo 2 | 3.176 px | 31,7% | 1,14% | 6 | 50,5 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9507-5901) |
| 15/09 18h | VIP Day, disparo 3 | 3.553 px | 31,3% | 1,37% | 4 | 19,4 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9507-6075) |
| 17/09 | VIP Week, 1 | 2.788 px | 29,5% | 1,24% | 6 | 33,9 | [abrir](https://www.figma.com/design/fhSNExXUuZa6qpSNZZ7kCT/?node-id=9733-208) |

Não estão na linha da Blue Wolf nos arquivos: 06/07, o primeiro disparo de cada pico (07/07 7h, 08/08 7h, 09/09 7h, 15/09 7h), 25/07 e 03/09. É provável que sejam e-mails de texto ou reaproveitados, montados direto na Omnisend.

### 19.2 Altura contra resultado

| Faixa de altura | E-mails | Abertura | Clique | Pedidos | RPM |
| --- | --- | --- | --- | --- | --- |
| Até 2.200 px | 8 | 35,6% | 1,96% | 69 | US$ 41,5 |
| 2.200 a 2.900 px | 12 | 34,3% | 1,92% | 107 | US$ 43,7 |
| 2.900 a 3.300 px | 10 | 35,5% | 2,16% | 99 | US$ 55,2 |
| Acima de 3.300 px | 6 | 31,3% | 1,68% | 41 | US$ 29,9 |

E-mail curto não vendeu mais. A faixa de melhor resultado é a de 2.900 a 3.300 px. Só os e-mails acima de 3.300 px rendem menos, e esse grupo está contaminado: três dos seis foram para o segmento de 22 mil ou são prova social. Isso corrige a leitura que eu vinha fazendo a partir do Max ("keep it light"): nesta carteira, encurtar por encurtar não é alavanca. O que pesa é o que aparece antes da primeira rolagem.

### 19.3 Anatomia das campanhas lidas

| Campanha | Primeira tela | Corpo | Oferta | Resultado |
| --- | --- | --- | --- | --- |
| 08/08 18h, a melhor | Conversa simulada entre dois clientes: "18% OFF on everything today with coupon 0808", "Already got mine. Half the stuff I had my eye on is already sold out", "I'm going now!!" | Foto de modelo com o produto, cupom, 4 produtos ("There's still time to grab these"), bloco final "Now or never" com o cupom repetido | 18% com cupom 0808, até meia-noite | 18 pedidos, RPM 107,5 |
| 07/07 18h | "Last call 7.7 Summer Sale", 17% OFF, cupom 0707, "Expires: tonight, 11:59 PM" | Texto curto de prazo, 4 produtos, linha do tempo do dia (7AM, 11AM, 18PM, 12AM) com o horário atual marcado, CTA final | 17% com cupom 0707 | 14 pedidos, RPM 105,3 |
| 03/07, melhor antecipação | Selo "Invitation update", 7.7 gigante, os três horários em caixas, "Those who know, arrive early" | "The 3 moments of 7.7" (7AM acesso antecipado, 11AM destaque, 18PM chamada final), FAQ com 4 perguntas reais, barra de progresso "Invitation status: sent, read, confirmed, ready" | Nenhuma. Sem produtos | 14 pedidos, RPM 84,1, maior abertura do trimestre |
| 11/09, ressaca 9.9 | Faixa "Active deals, no coupon required". Caixa de aviso de sistema: "Notice: September 11, 2026", estoque baixo, preços promocionais ativos enquanto durar | 4 produtos ("Get the last items"), CTA | Preço promocional sem cupom | 14 pedidos, RPM 77,7, clique de 3,20% |
| 22/07, Jornal | Capa de jornal "Breaking News", data, manchete "48h until the end of the mid-year Black Sale", até 37% no site mais 15% com cupom EXTRA | Foto da embalagem, CTA, 4 produtos ("The headline highlights") | Até 37% mais 15% | 15 pedidos, RPM 71,9 |
| 20/07, Revele | "Reveal your mid-year sale discount", "until 37% OFF" com papel rasgado revelando "+15% OFF", cupom EXTRA, validade | 4 produtos e CTA. O mais curto entre os melhores | Até 37% mais 15% | 18 pedidos, RPM 68,5 |
| 29/07, UGC, entre as piores | "6,747 reviews don't lie", CTA "See the gifts" | Três blocos longos de foto de cliente com depoimento, um CTA por bloco. O mais longo de julho | Nenhuma | 7 pedidos, RPM 33,6, clique de 0,91% |
| 03/08, warm-up, a pior | Selo "Warm up", 8.8 "End of summer", "Start claiming your summer favorites now" | Texto de conceito, bloco "Mark these times" com cadeado, 4 produtos. Dois CTAs vagos ("Shop the warm-up", "Shop active deals") | Nenhum número, cupom ou prazo | 1 pedido, RPM 4,6 |

### 19.4 O que as melhores têm em comum

1. **Número, cupom e prazo na primeira tela.** Cinco das seis melhores mostram o percentual, o código e a hora de término antes da primeira rolagem.
2. **Um formato emprestado de fora do e-mail.** Conversa de celular, capa de jornal, aviso de sistema, papel rasgado, barra de status. É o mesmo princípio do assunto de notificação (seção 18.8), levado para o layout.
3. **Quatro produtos logo abaixo do hero**, com título que retoma a urgência ("There's still time to grab these", "Get the last items").
4. **Cupom repetido no fim** nos e-mails de pico.
5. **A ressaca que mais vendeu não pede cupom.** "No coupon required" tira uma etapa. É o único e-mail da amostra sem código e teve o segundo melhor clique do trimestre.

### 19.5 O que as piores têm em comum

1. **Sem número na primeira tela.** O warm-up do 8.8 e a prova social abrem com conceito.
2. **CTA vago.** "Shop the warm-up" e "See the gifts" não dizem o que a pessoa ganha.
3. **Prova social como e-mail inteiro.** Três depoimentos longos sem oferta. Funciona melhor como um bloco dentro de um e-mail de oferta.
4. **Mesma promessa repetida.** No esquenta do 9.9, três e-mails seguidos dizem que o acesso está garantido. O terceiro rende US$ 13 por mil envios.

### 19.6 Ligação com o material do Max

- A melhor campanha da Blue Wolf usa o mesmo recurso de dois templates do Figma do Max: o mock de conversa no hero (seção 9.6).
- A estrutura "hero com oferta, um CTA, poucos produtos" do Max (seção 9.1) bate com as seis melhores.
- O ponto em que a carteira diverge do Max é o tamanho: aqui os e-mails de 2.900 a 3.300 px são os que mais rendem.

### 19.7 Regras de layout para a Black Friday, a partir deste dado

- Primeira tela de todo e-mail de oferta: percentual, cupom ou "sem cupom", data e hora de término.
- Um formato de fora do e-mail por peça: conversa, jornal, aviso, status, recibo.
- Quatro produtos abaixo do hero, com título de urgência.
- E-mail de antecipação sem produto: agenda com horários, FAQ e barra de status. Foi o modelo do 7.7, o melhor esquenta do trimestre.
- Nada de e-mail só de prova social na janela de BF. Prova entra como bloco.
- Testar "sem cupom, preço já aplicado" em um dos disparos de pico.
- Todo link para a coleção da oferta, não para a home (seção 18.7).

## 20. Fichas de campanha por loja e por mês: Blue Wolf

Esta seção é o formato padrão do estudo para todas as lojas: contexto da loja, depois um bloco por mês, depois uma ficha por campanha com a imagem do e-mail embutida, a estratégia e os números. As imagens foram recortadas das exportações do Figma enviadas em 18/09/2026 e ficam salvas dentro do documento.

### 20.1 Contexto da loja

| Item | Blue Wolf |
| --- | --- |
| Site e mercado | wolfbluestore.com. Loja global, comunicação em inglês, moeda USD |
| O que vende | Acessórios masculinos de couro: bolsas transversais, carteiras, mochilas. Também aparecem calçados e relógios nas campanhas de setembro |
| Conta Omnisend | Criada em abril de 2026. Fuso de São Paulo. Só canal de e-mail |
| Lista de envio | 13,6 mil contatos em junho, 16,8 mil em setembro. Um segmento maior, de 22 mil, foi usado no esquenta do 9.9 |
| Segmentos usados | "TODOS OS LEADS" em quase tudo. "LEADS ENGAJADOS" uma vez (19/06). Um segmento de não engajados na reativação de 17/08 |
| Campanhas no trimestre | 46 campanhas, 742 mil envios, 389 pedidos, US$ 32.338. Abertura de 34,6%, clique de 1,84%, US$ 43,58 por mil envios |
| Automações no trimestre | 13 fluxos, 284 mil envios, 1.183 pedidos, US$ 109.800. Fazem 77% da receita de e-mail |
| Principais fluxos | Welcome (US$ 37,7 mil), checkout abandonado (US$ 30,3 mil), rastreio de envio (US$ 10,4 mil), carrinho (US$ 9,1 mil), produto visto (US$ 8,9 mil), upsell (US$ 6,3 mil) |
| Diferencial da conta | Régua de logística com oferta (rastreio, em trânsito, em rota, entregue): US$ 15.580 |
| Reputação | Descadastro de 0,44% por envio. Spam de 0,0185% |
| Identidade visual | Tema azul escuro com fundo de folhagem e faixas em azul claro. Tipografia principal condensada em caixa alta nos títulos. Rodapé fixo com três garantias: envio expresso, qualidade, pagamento seguro |
| Modelo de calendário | Todo mês uma data dupla (7.7, 8.8, 9.9) com 3 a 4 e-mails de antecipação, 3 disparos no dia (7h, 11h, 18h) e ressaca. No resto do mês, campanhas temáticas, gamificadas e de catálogo, cerca de 3 por semana |
| Pontos de atenção | Todo clique leva à página inicial. Rendimento por envio caindo mês a mês. Segmento de 22 mil sem ganho de abertura. Sem SMS, push ou WhatsApp |

O que não está nos arquivos de design: o primeiro disparo de cada pico (7h), 06/07, 25/07 e 03/09. Esses e-mails existem na Omnisend e têm números, mas não têm imagem aqui.

### 20.2 Julho de 2026

Resumo do mês: 15 campanhas, 222.646 envios, abertura de 36,2%, clique de 1,87%, 159 pedidos, US$ 12.484, US$ 56,07 por mil envios. Melhor mês do trimestre.

Estratégia do mês: o 7.7 Summer Sale na primeira semana, com três e-mails de convite e agenda antes do dia. Depois, a "Mid-Year Black Sale" de 20 a 24/07 (até 37% no site mais 15% com o cupom EXTRA), contada em quatro formatos diferentes: revelação, jornal, ligação e reabertura. O mês fecha com uma gamificada, uma prova social e uma sexta de recompensa.

#### 01/07, Antecipação 7.7, e-mail 1: convite

![E-mail de 01/07 da Blue Wolf: convite oficial para o 7.7 Summer Sale com os três horários, datas dos próximos e-mails e barra de status do convite](blob/15aef474-cf3a)

- **Assunto:** "\[Nome\], you have received an invitation". Pré-cabeçalho: "Confirm your attendance for 7.7"
- **Estratégia:** transformar a promoção em evento com convite. Primeira tela com selo "You're officially invited", os três horários e o botão "Confirm your spot". Depois, as datas dos próximos e-mails (03/07, 06/07, 07/07) e a barra "Your invitation status: sent, read, confirmed"
- **Oferta:** nenhuma. Sem produtos
- **Números:** 13.961 envios, abertura 41,0%, clique 2,46%, 8 pedidos, US$ 654, US$ 46,8 por mil envios. Altura 2.514 px
- **Leitura:** segunda maior abertura do trimestre. O pedido de confirmação gera clique sem oferta

#### 03/07, Antecipação 7.7, e-mail 2: agenda

![E-mail de 03/07 da Blue Wolf: atualização do convite com os três momentos do 7.7, perguntas frequentes e barra de status](blob/07bc29c7-3b36)

- **Assunto:** "\[Nome\], have you seen what is coming?". Pré-cabeçalho: "The schedule has already been released..."
- **Estratégia:** entregar a agenda prometida. "The 3 moments of 7.7": 7AM acesso antecipado, 11AM destaque de produto, 18PM chamada final. FAQ com 4 perguntas reais (preciso me inscrever, vale no site, e se eu perder as 7h, vai ser prorrogado). Barra de status avançando para "confirmed"
- **Oferta:** nenhuma. Sem produtos
- **Números:** 13.937 envios, abertura 44,3%, clique 1,90%, 14 pedidos, US$ 1.171, US$ 84,1 por mil envios. Altura 3.133 px
- **Leitura:** maior abertura do trimestre e terceira maior receita por envio, sem cupom. É o modelo de antecipação para copiar na BF

#### 07/07 11h, 7.7, disparo 2: role até o fim

![E-mail de 07/07 às 11h da Blue Wolf: painéis borrados que vão revelando 17% OFF com o cupom 0707 conforme a rolagem](blob/33ab6e65-4593)

- **Assunto:** "Scroll to the end of this email (there's a surprise)". Pré-cabeçalho: "The 7.7 offer only appears for those who scroll all the way down."
- **Estratégia:** gamificação de rolagem. Cinco painéis, do borrado ao nítido, revelam "17% OFF, coupon 0707" só no fim
- **Oferta:** 17% com o cupom 0707, até 23h59
- **Números:** 13.679 envios, abertura 33,1%, clique 1,27%, 12 pedidos, US$ 738, US$ 53,9 por mil envios. Altura 3.414 px
- **Leitura:** clique baixo. A oferta fica escondida por 2.500 px. Quem chega ao fim compra (12 pedidos em 174 cliques), mas pouca gente chega

#### 07/07 18h, 7.7, disparo 3: última chamada

![E-mail de 07/07 às 18h da Blue Wolf: last call do 7.7 com 17% OFF, cupom 0707, prazo de meia-noite, quatro produtos e linha do tempo do dia](blob/4a1ad145-5dba)

- **Assunto:** "\[FINAL CALL\] Expires at 11:59 PM". Pré-cabeçalho: "7.7: Open now and claim your coupon today"
- **Estratégia:** número, cupom e prazo na primeira tela. Texto curto de urgência ("The morning sun is starting to fade"), 4 produtos, e a linha do tempo "The sun is clocking out" com 7AM, 11AM, 18PM e 12AM
- **Oferta:** 17% com o cupom 0707
- **Números:** 13.629 envios, abertura 38,8%, clique 3,06%, 14 pedidos, US$ 1.435, US$ 105,3 por mil envios. Altura 3.178 px
- **Leitura:** segunda melhor campanha do trimestre. Mesma oferta do disparo das 11h, mostrada na primeira tela: o dobro de clique

#### 15/07, Favoritos do 7.7

![E-mail de 15/07 da Blue Wolf: os mais vendidos do 7.7 com unidades limitadas, foto do produto ao pôr do sol e quatro campeões](blob/6cf1f0a2-216f)

- **Assunto:** "\[Nome\], your 7.7 favorites are waiting for you". Pré-cabeçalho: "Only while supplies last. Hurry to secure yours."
- **Estratégia:** ressaca tardia com prova de venda. "The bestsellers 7.7, limited units left", foto grande do produto, "The 7.7 champions" com 4 produtos
- **Oferta:** preços do 7.7 mantidos nos mais vendidos, sem cupom novo
- **Números:** 15.714 envios, abertura 36,7%, clique 3,19%, 14 pedidos, US$ 1.121, US$ 71,3 por mil envios. Altura 2.520 px
- **Leitura:** terceiro melhor clique do trimestre. Produto real na primeira tela e escassez

#### 18/07, Final da Copa

![E-mail de 18/07 da Blue Wolf: a final é amanhã, sua vitória é hoje, com troféu, texto personalizado, ofertas do campeão e anúncio da venda de meio de ano](blob/71882bd5-fd75)

- **Assunto:** "\[Nome\], I've set something aside just for our special customers". Pré-cabeçalho: "Open this email to see what I selected for you."
- **Estratégia:** tema do momento (final da Copa do Mundo). Texto longo personalizado com nome e e-mail do contato, "The champion's offers" com 4 produtos, e no fim o anúncio da Mid-Year Sale para segunda 20/07 às 10h
- **Oferta:** seleção para "clientes especiais". Serve de ponte para a venda da semana seguinte
- **Números:** 15.542 envios, abertura 34,8%, clique 2,30%, 13 pedidos, US$ 863, US$ 55,5 por mil envios. Altura 3.154 px
- **Leitura:** temáticas do momento têm o segundo melhor rendimento por formato

#### 20/07, Revele seu desconto

![E-mail de 20/07 da Blue Wolf: revele seu desconto de meio de ano, até 37% OFF com papel rasgado mostrando mais 15% OFF e cupom EXTRA](blob/a41685b3-7d33)

- **Assunto:** "(1) hidden discount for \[nome\] inside this email". Pré-cabeçalho: "Click 'Reveal Now' to see how much you can save."
- **Estratégia:** abertura da Mid-Year Sale. Papel rasgado revela "+15% OFF" sobre "until 37% OFF". Cupom e validade logo abaixo. 4 produtos
- **Oferta:** até 37% no site mais 15% com o cupom EXTRA, até 24/07
- **Números:** 15.575 envios, abertura 35,8%, clique 1,66%, 18 pedidos, US$ 1.066, US$ 68,5 por mil envios. Altura 2.169 px
- **Leitura:** recorde de pedidos do trimestre, empatado com o 8.8 das 18h. Oferta grande, e-mail curto, tudo na primeira tela

#### 22/07, Jornal

![E-mail de 22/07 da Blue Wolf em formato de capa de jornal: breaking news, 48 horas para o fim da Mid-Year Black Sale, cupom EXTRA](blob/5bad21b2-ab71)

- **Assunto:** "\[Nome\], the news you did not want to hear has arrived...". Pré-cabeçalho: "This offer ends Friday at 11:59 p.m."
- **Estratégia:** mesma oferta em formato de jornal. Manchete "48h until the end", data do dia no cabeçalho, foto da embalagem, "The headline highlights" com 4 produtos
- **Oferta:** até 37% mais 15% com EXTRA
- **Números:** 15.606 envios, abertura 35,3%, clique 2,04%, 15 pedidos, US$ 1.123, US$ 71,9 por mil envios. Altura 2.469 px
- **Leitura:** prova de que a mesma oferta aguenta um segundo envio quando o formato muda. É o princípio do reenvio, feito com design

#### 24/07, Ligação

![E-mail de 24/07 da Blue Wolf: sua última chance está ligando, com mock de celular mostrando chamada recebida e a oferta de 37% mais 15%](blob/dc7459ad-423a)

- **Assunto:** "\[Nome\], you have an incoming call". Pré-cabeçalho: "Answer quickly. This is your last chance today."
- **Estratégia:** último dia da oferta em formato de chamada recebida. Celular com "Incoming call", botões de recusar e atender, e "Accept" como CTA. "The products on the line" com 4 produtos
- **Oferta:** até 37% mais 15% com EXTRA, último dia
- **Números:** 15.437 envios, abertura 34,5%, clique 1,69%, 11 pedidos, US$ 756, US$ 49,0 por mil envios. Altura 2.312 px
- **Leitura:** terceiro envio da mesma oferta na semana e ainda 11 pedidos. Somados, os três formatos renderam 44 pedidos e US$ 2.944

#### 27/07, Segunda da sorte

![E-mail de 27/07 da Blue Wolf: lucky Monday com moedas, seleção da semana e quatro produtos](blob/9e4f7ce3-c57e)

- **Assunto:** "Careful: this email contains luck". Pré-cabeçalho: "I've selected this week's offers just for you."
- **Estratégia:** gamificada leve. "Lucky Monday", "This week's selection" com 4 produtos
- **Oferta:** nenhum número, cupom ou prazo
- **Números:** 15.521 envios, abertura 34,6%, clique 1,82%, 3 pedidos, US$ 267, US$ 17,2 por mil envios. Altura 1.796 px
- **Leitura:** uma das piores do trimestre. É o e-mail mais curto de julho, o que mostra que ser curto não resolve: falta oferta na primeira tela

#### 29/07, UGC social proof

![E-mail de 29/07 da Blue Wolf: 6.747 reviews don't lie, com fotos de clientes e três depoimentos longos](blob/8a7d4044-f7a3)

- **Assunto:** "I came back to buy again because...". Pré-cabeçalho: "See what real customers say."
- **Estratégia:** prova social como e-mail inteiro. Faixa de fotos de clientes e três blocos de depoimento, cada um com botão
- **Oferta:** nenhuma
- **Números:** 15.531 envios, abertura 26,6%, clique 0,91%, 7 pedidos, US$ 522, US$ 33,6 por mil envios. Altura 3.960 px
- **Leitura:** menor abertura e menor clique de julho. É o mais longo do mês e não tem oferta. O número "6,747 reviews" precisa ser o real da loja

#### 31/07, Sexta premiada

![E-mail de 31/07 da Blue Wolf: Friday Rewards com chave dourada, cupom SUMMER e quatro produtos para destravar o desconto](blob/7bdd4550-f5ce)

- **Assunto:** "You've received a reward today". Pré-cabeçalho: "Redeem your discount by 11:59 PM on Saturday."
- **Estratégia:** recompensa de fim de mês. Chave dourada, cupom SUMMER, "Unlock with the key": o desconto de cada item só aparece no checkout
- **Oferta:** cupom SUMMER com desconto não revelado, até sábado 23h59
- **Números:** 15.584 envios, abertura 33,4%, clique 1,58%, 9 pedidos, US$ 782, US$ 50,2 por mil envios. Altura 1.934 px
- **Leitura:** mesma estrutura curta da Segunda da sorte, mas com cupom e prazo: três vezes mais pedidos

### 20.3 Agosto de 2026

Resumo do mês: 15 campanhas, 239.656 envios, abertura de 36,0%, clique de 1,71%, 108 pedidos, US$ 9.394, US$ 39,20 por mil envios. Mesmo número de envios de julho, 32% menos pedidos.

Estratégia do mês: o 8.8 End of Summer na primeira semana, com três e-mails de esquenta em tom de anúncio, três disparos no dia com 18% e o cupom 0808, e ressaca. Na segunda quinzena, recorrentes (Friyay, Turbo Monday), duas peças de conteúdo (fotos de clientes, catálogo contra indecisão) e a semana de 15% com o cupom WEEK15 em três ângulos. Fecha com "August ends today". As imagens de agosto foram exportadas a 76% do tamanho original.

#### 03/08, Esquenta 8.8, e-mail 1: warm-up

![E-mail de 03/08 da Blue Wolf: warm-up do 8.8 End of Summer com horários dos flash drops e quatro produtos já em oferta](blob/0a88eb25-cc39)

- **Assunto:** "The 8.8 Warm-Up Has Begun". Pré-cabeçalho: "Offers are live now, with more coming soon..."
- **Estratégia:** anunciar que o esquenta começou. Texto de conceito ("Every summer ends the same way"), bloco "Mark these times" com cadeado e os três horários, 4 produtos "Already live in the warm-up"
- **Oferta:** "active deals", sem número, cupom ou prazo
- **Números:** 15.680 envios, abertura 34,0%, clique 1,22%, 1 pedido, US$ 73, US$ 4,6 por mil envios. Altura 2.830 px
- **Leitura:** pior campanha do trimestre. Fala da marca e do evento, não da pessoa. Dois botões vagos

#### 05/08, Esquenta 8.8, e-mail 2

![E-mail de 05/08 da Blue Wolf: faltam 3 dias para o 8.8, como o dia vai funcionar em três horários e produtos já em oferta](blob/69ad5011-40f9)

- **Assunto:** "There's a good reason to open this email". Pré-cabeçalho: "Only 3 days until 8.8, get ready!"
- **Estratégia:** contagem regressiva e explicação do dia. "How many days left until 8.8?", "How 8.8 will work" com 7AM, 11AM e 18PM, 4 produtos do warm-up
- **Oferta:** nenhuma nova
- **Números:** 15.591 envios, abertura 34,1%, clique 0,99%, 6 pedidos, US$ 478, US$ 30,7 por mil envios. Altura 3.399 px
- **Leitura:** segundo pior clique do trimestre. Mesma informação do 7.7, sem o convite, o FAQ e a barra de status

#### 07/08, Esquenta 8.8, e-mail 3: véspera

![E-mail de 07/08 da Blue Wolf: é amanhã, com os três horários, checklist de preparação, produtos em oferta e bilhete first come first served](blob/d5a6b60e-de30)

- **Assunto:** "Tomorrow is 8.8. Are you ready?". Pré-cabeçalho: "7 AM, 11 AM, 6 PM. The earlier you arrive, the better the selection."
- **Estratégia:** véspera com checklist. "Ready for tomorrow?" com quatro ações, produtos já em oferta, bilhete "First come, first served"
- **Oferta:** nenhuma nova
- **Números:** 15.643 envios, abertura 34,1%, clique 1,32%, 10 pedidos, US$ 718, US$ 45,9 por mil envios. Altura 3.250 px
- **Leitura:** o melhor dos três esquentas do 8.8. A véspera vende, como na Emyerre

#### 08/08 11h, 8.8, disparo 2: primeiros 100

![E-mail de 08/08 às 11h da Blue Wolf: os 100 primeiros levam 18% OFF no site com o cupom 0808, foto de carteira e quatro destaques](blob/9723fc17-3a25)

- **Assunto:** "This email is only valid for the first 100". Pré-cabeçalho: "The special 8.8 offer has been released."
- **Estratégia:** escassez por quantidade. Cupom na primeira tela, foto de produto, "Today's top picks" com 4 produtos, bloco "Still not sure what to get?"
- **Oferta:** 18% no site com o cupom 0808, para os 100 primeiros, até 23h59
- **Números:** 15.644 envios, abertura 33,9%, clique 1,31%, 8 pedidos, US$ 572, US$ 36,5 por mil envios. Altura 2.770 px
- **Leitura:** resultado médio. O limite de 100 só vale se existir no cupom do Shopify

#### 08/08 18h, 8.8, disparo 3: conversa

![E-mail de 08/08 às 18h da Blue Wolf: conversa simulada entre dois clientes sobre os 18% do 8.8, foto de modelo, cupom 0808, quatro produtos e bloco now or never](blob/363ad780-597c)

- **Assunto:** "Your status has just changed". Pré-cabeçalho: "Open this and see what I've set aside for you."
- **Estratégia:** prova social em formato de conversa de celular na primeira tela, foto de modelo com o produto, cupom, "There's still time to grab these" com 4 produtos, "Now or never" com o cupom repetido
- **Oferta:** 18% com o cupom 0808, até meia-noite
- **Números:** 15.561 envios, abertura 42,2%, clique 2,09%, 18 pedidos, US$ 1.674, US$ 107,5 por mil envios. Altura 3.230 px. 129 descadastros, o maior número do trimestre
- **Leitura:** melhor campanha do trimestre. Assunto de notificação pessoal mais conversa na primeira tela. O custo é o descadastro alto do terceiro disparo do dia

#### 11/08, Ressaca 8.8

![E-mail de 11/08 da Blue Wolf: still available, com aviso da marca e os quatro mais escolhidos do 8.8](blob/4e23fea0-c8a6)

- **Assunto:** "Missed our 8.8 sale? There's still time...". Pré-cabeçalho: "Only a few of our bestsellers are left."
- **Estratégia:** e-mail curto. Foto noturna, caixa de aviso da marca, "The most chosen from 8.8" com 4 produtos
- **Oferta:** preços do 8.8 mantidos no que sobrou
- **Números:** 15.572 envios, abertura 38,7%, clique 1,23%, 8 pedidos, US$ 629, US$ 40,4 por mil envios. Altura 1.863 px. O frame está nomeado "11/11" no Figma
- **Leitura:** abre bem e clica pouco. A ressaca do 9.9, com aviso de estoque e "sem cupom", rendeu o dobro

#### 14/08, Sextou

![E-mail de 14/08 da Blue Wolf: Friyay, o fim de semana começa agora, com foto do produto na mão e quatro destaques do site](blob/5dd334a0-329f)

- **Assunto:** "Your Friday deserves this...". Pré-cabeçalho: "Offers are available only through Sunday."
- **Estratégia:** recorrente de sexta. Foto de uso do produto, "Some highlights of what's on the site", despedida "Have a great weekend"
- **Oferta:** ofertas do site até domingo, sem número na primeira tela
- **Números:** 15.577 envios, abertura 34,6%, clique 1,41%, 6 pedidos, US$ 544, US$ 34,9 por mil envios. Altura 2.579 px

#### 17/08, Segunda turbo

![E-mail de 17/08 da Blue Wolf: Turbo Monday só para os 100 primeiros, cupom TURBO100 com desconto misterioso revelado no checkout](blob/0934869c-ee6c)

- **Assunto:** "Are you among the first 100?". Pré-cabeçalho: "Apply the code at checkout and find out. Until midnight."
- **Estratégia:** desconto misterioso. Símbolos "$ % ?" em papel rasgado, "Only the fastest win: enter the coupon TURBO100 and discover the surprise at checkout", 4 produtos
- **Oferta:** cupom TURBO100 com valor não revelado, para os 100 primeiros, até meia-noite
- **Números:** 15.725 envios, abertura 33,8%, clique 1,50%, 6 pedidos, US$ 950, US$ 60,4 por mil envios. Altura 2.635 px
- **Leitura:** poucos pedidos e ticket alto (US$ 158 por pedido). Mesmo dia da reativação de base, que rendeu 1 pedido em 18.699 envios

#### 19/08, UGC Dia da Fotografia

![E-mail de 19/08 da Blue Wolf: as melhores fotos não são nossas, com polaroides de clientes no Dia Mundial da Fotografia](blob/efb3e061-2988)

- **Assunto:** "Yours is missing here...". Pré-cabeçalho: "Choose yours. It'll be worth it."
- **Estratégia:** data comemorativa com fotos de clientes em polaroide ("Captured by you")
- **Oferta:** nenhuma
- **Números:** 16.361 envios, abertura 32,3%, clique 1,01%, 5 pedidos, US$ 408, US$ 24,9 por mil envios. Altura 2.803 px
- **Leitura:** segunda prova social do trimestre, segundo resultado fraco

#### 21/08, Catálogo indecisão

![E-mail de 21/08 da Blue Wolf: tantas opções e nenhuma escolha errada, com quatro produtos, reviews de quem teve a mesma dúvida e chamada final](blob/6e614bc9-0006)

- **Assunto:** "Either you choose today, or you keep putting it off...". Pré-cabeçalho: "There is no wrong choice here."
- **Estratégia:** catálogo contra paralisia de escolha. "Your right choices" com 4 produtos, "They had the same doubt" com dois reviews, "Now it's your turn"
- **Oferta:** nenhuma
- **Números:** 16.394 envios, abertura 34,1%, clique 1,89%, 5 pedidos, US$ 395, US$ 24,1 por mil envios. Altura 3.121 px

#### 24/08, Semana de 15%, e-mail 1: On & Off

![E-mail de 24/08 da Blue Wolf: interruptor com preço cheio desligado e 15% OFF ligado, cupom WEEK15 válido até sexta](blob/2e744a33-06fe)

- **Assunto:** "I've activated a discount for you". Pré-cabeçalho: "It's valid sitewide through Friday."
- **Estratégia:** interruptor visual. "Full price: OFF", "15% OFF: ON", cupom e validade, "The easy picks" com 4 produtos, interruptor repetido no fim
- **Oferta:** 15% no site com o cupom WEEK15, até sexta 23h59
- **Números:** 16.516 envios, abertura 37,8%, clique 2,89%, 8 pedidos, US$ 779, US$ 47,2 por mil envios. Altura 3.210 px
- **Leitura:** melhor dos três da semana. A oferta se entende sem ler

#### 26/08, Semana de 15%, e-mail 2: Escolha o caminho

![E-mail de 26/08 da Blue Wolf: encontre seu ponto de partida, com fluxograma de objeções e caixa de 15% OFF](blob/650ffcec-c49f)

- **Assunto:** "\[Nome\], choose your path...". Pré-cabeçalho: "Whichever you choose, you win. Through Friday."
- **Estratégia:** fluxograma de objeções ("It's expensive", "I don't know which", "I'm in no rush") levando à mesma oferta
- **Oferta:** 15% com WEEK15
- **Números:** 16.519 envios, abertura 37,4%, clique 0,97%, 3 pedidos, US$ 208, US$ 12,6 por mil envios. Altura 1.964 px
- **Leitura:** abre bem e ninguém clica. Pede leitura e não mostra produto. Sem grade de produtos

#### 28/08, Semana de 15%, e-mail 3: Notificação do futuro

![E-mail de 28/08 da Blue Wolf em fundo branco: notificação do futuro dizendo que o pedido está a caminho, com resumo de pedido simulado e cupom WEEK15](blob/61822391-a88f)

- **Assunto:** "\[Nome\], you still need to confirm your order...". Pré-cabeçalho: "Only available until today at 11:59 PM."
- **Estratégia:** e-mail com cara de transacional. Fundo branco, "Your order will be on its way", resumo de pedido simulado com o cupom aplicado, "Last hours to take advantage" com 4 produtos
- **Oferta:** 15% com WEEK15, último dia
- **Números:** 16.577 envios, abertura 37,0%, clique 3,61%, 9 pedidos, US$ 648, US$ 39,1 por mil envios. Altura 2.128 px
- **Leitura:** maior clique do trimestre. Formato de aviso de sistema em fundo branco, o mesmo da ressaca do 9.9. Cuidado: o assunto sugere um pedido que a pessoa não fez. Vale checar descadastro e reclamação antes de repetir

#### 31/08, Catálogo fecha mês

![E-mail de 31/08 da Blue Wolf: August ends today, com foto do produto, quatro cartões explicando o fechamento do mês e quatro produtos](blob/8da59a66-4625)

- **Assunto:** "Ignore this email after 11:59 PM". Pré-cabeçalho: "Until then, August prices still apply"
- **Estratégia:** virada de mês como prazo. "August closing: 31", quatro cartões curtos, "Today is still August. Tomorrow isn't." com 4 produtos
- **Oferta:** preços de agosto até meia-noite, sem cupom
- **Números:** 16.620 envios, abertura 36,2%, clique 2,91%, 8 pedidos, US$ 815, US$ 49,1 por mil envios. Altura 3.012 px
- **Leitura:** prazo sem desconto novo e clique alto. Reaproveitável em 30/11

### 20.4 Setembro de 2026

Resumo do mês, até 17/09: 13 campanhas, 238.669 envios, abertura de 31,7%, clique de 1,92%, 99 pedidos, US$ 8.706, US$ 36,48 por mil envios. Pior rendimento do trimestre, com 13 envios em 17 dias.

Estratégia do mês: 9.9 New Season Sale com quatro e-mails de esquenta enviados ao segmento de 22 mil, três disparos no dia com 19% e o cupom 0909, e ressaca em tom de aviso. Seis dias depois, um segundo evento, o VIP Day (15/09), com 17% e o cupom VIP, estendido para VIP Week até 20/09. As imagens de setembro foram exportadas a 97% do tamanho original.

#### 05/09, Esquenta 9.9, e-mail 2: calendário

![E-mail de 05/09 da Blue Wolf: it's coming, 9.9 New Season Sale, com calendário de setembro marcando o dia 9, três horários e produtos do warm-up](blob/91c16808-9874)

- **Assunto:** "I promised I'd let you know in advance, \[nome\]". Pré-cabeçalho: "09/09, three times: 7 AM, 11 AM, and 6 PM. Mark your calendar."
- **Estratégia:** folha de calendário com o dia 9 circulado, "Three time slots in one day", promessa "The biggest deal that Blue Wolf has ever launched", botão "Secure my access", 4 produtos do warm-up
- **Oferta:** nenhuma nova. Produtos já em oferta
- **Números:** 21.862 envios (segmento de 22 mil), abertura 27,5%, clique 2,30%, 12 pedidos, US$ 730, US$ 33,4 por mil envios. Altura 2.661 px
- **Leitura:** melhor dos quatro esquentas do 9.9. "A maior oferta que já lançamos" é uma promessa que o 19% do dia 9 precisa cumprir, e a BF vai ter de superar

#### 07/09, Esquenta 9.9, e-mail 3

![E-mail de 07/09 da Blue Wolf: warm-up do 9.9, faltam 2 dias, com os horários, explicação de como funciona e produtos em oferta](blob/42800d8c-8053)

- **Assunto:** "\[Nome\], you've secured early access". Pré-cabeçalho: "Those who arrive at 7 AM get the best selection"
- **Estratégia:** contagem "2 days to go", texto "In two days", "How it works" com os três horários, "The warm-up has begun" com 4 produtos
- **Oferta:** nenhuma nova
- **Números:** 22.042 envios, abertura 26,0%, clique 2,21%, 3 pedidos, US$ 287, US$ 13,0 por mil envios. Altura 3.207 px
- **Leitura:** menor abertura do trimestre. Terceiro e-mail seguido com a mesma informação dos horários

#### 08/09, Esquenta 9.9, e-mail 4: véspera

![E-mail de 08/09 da Blue Wolf: é amanhã, a melhor oferta da temporada, com horários, perguntas frequentes, produtos incluídos e bilhete de um dia para o 9.9](blob/0cc8c90d-7558)

- **Assunto:** "\[Nome\], you have something scheduled for tomorrow". Pré-cabeçalho: "9.9: 7 AM, 11 AM, and 6 PM. Be ready!"
- **Estratégia:** véspera com FAQ ("Still have questions?"), "What's included in tomorrow's sale" com 4 produtos, bilhete "08/09 → 09/09, 1 day to go"
- **Oferta:** nenhuma nova
- **Números:** 22.093 envios, abertura 28,8%, clique 2,42%, 5 pedidos, US$ 427, US$ 19,3 por mil envios. Altura 3.767 px
- **Leitura:** na Emyerre este mesmo e-mail foi o melhor do 9.9. Aqui foi para 22 mil contatos e rendeu pouco

#### 09/09 11h, 9.9, disparo 2: relógio

![E-mail de 09/09 às 11h da Blue Wolf: 19% OFF com o cupom 0909, relógio e linha do tempo hora a hora do dia, mais quatro produtos](blob/f664f264-38ab)

- **Assunto:** "Your access has been granted (today only)". Pré-cabeçalho: "The best 9.9 offer is now available"
- **Estratégia:** cabeçalho com os três horários e os dois primeiros marcados. Cupom na primeira tela, relógio, linha do tempo de 07:00 a 00:00 com "11:00, 19% OFF is live for everyone" em destaque. "On sale now" com 4 produtos e texto de fechamento
- **Oferta:** 19% no site com o cupom 0909, até meia-noite
- **Números:** 16.790 envios, abertura 34,9%, clique 2,70%, 7 pedidos, US$ 512, US$ 30,5 por mil envios. Altura 4.136 px, o mais longo do trimestre
- **Leitura:** bom clique e poucos pedidos. É o e-mail mais longo da amostra

#### 09/09 18h, 9.9, disparo 3: jornal

![E-mail de 09/09 às 18h da Blue Wolf em formato de jornal: breaking news, 6 horas para o fim do 9.9 New Season Sale, cupom 0909](blob/02d6bbdb-3c42)

- **Assunto:** "Your status has just changed". Pré-cabeçalho: "Open it and see what I selected for you"
- **Estratégia:** reaproveita o formato Jornal de 22/07. Manchete "6 hours left", cupom, foto da embalagem, "Headline highlights" com 4 produtos
- **Oferta:** 19% com o cupom 0909
- **Números:** 16.743 envios, abertura 41,8%, clique 3,56%, 15 pedidos, US$ 1.028, US$ 61,4 por mil envios. Altura 2.469 px
- **Leitura:** segundo maior clique do trimestre. Formato que já tinha funcionado em julho, com o assunto que funcionou em agosto. Reaproveitar o que deu certo dá certo

#### 11/09, Ressaca 9.9

![E-mail de 11/09 da Blue Wolf em fundo branco: aviso de estoque baixo após o 9.9, ofertas ativas sem cupom e quatro últimos itens](blob/141ce5cc-d60d)

- **Assunto:** "We regret to inform you that...". Pré-cabeçalho: "Low stock, but still available at promotional prices"
- **Estratégia:** aviso de sistema em fundo branco. Faixa "Active deals, no coupon required", caixa "Notice: September 11, 2026" com o motivo (alta demanda, estoque baixo), "Get the last items" com 4 produtos
- **Oferta:** preços promocionais mantidos, sem cupom
- **Números:** 16.771 envios, abertura 34,6%, clique 3,20%, 14 pedidos, US$ 1.303, US$ 77,7 por mil envios. Altura 1.735 px
- **Leitura:** melhor campanha de setembro. Curto, claro, sem etapa de cupom. Descadastro de 0,29%, abaixo da média

#### 14/09, Antecipação VIP Day

![E-mail de 14/09 da Blue Wolf em fundo branco: amanhã você tem acesso às melhores ofertas do VIP Day, com data, horários e um cupom exclusivo por e-mail](blob/1b9e8e6b-0d65)

- **Assunto:** "Confirmed: you're on the list for tomorrow". Pré-cabeçalho: "One exclusive coupon will be sent at 7:00 AM. Available by email only"
- **Estratégia:** e-mail mínimo, quase texto. Três linhas: a data, os horários, um cupom exclusivo por e-mail. Um botão
- **Oferta:** nenhuma. Promete cupom exclusivo de lista
- **Números:** 16.818 envios, abertura 33,5%, clique 1,54%, 5 pedidos, US$ 441, US$ 26,2 por mil envios. Altura 1.081 px, o mais curto do trimestre
- **Leitura:** uma única antecipação, na véspera, para um evento sem data conhecida. O 7.7 teve três e-mails em seis dias

#### 15/09 11h, VIP Day, disparo 2: teste de visão

![E-mail de 15/09 às 11h da Blue Wolf: teste rápido de visão com o cupom VIP Day, legenda de cores, 17% OFF e favoritos do dia](blob/4870f71e-e507)

- **Assunto:** "Were you approved?". Pré-cabeçalho: "The result is valid until midnight"
- **Estratégia:** gamificada. "Quick vision test: what color do you see?", legenda em que azul significa "seu cupom está pronto", 17% OFF com o cupom VIP, explicação da brincadeira, "Today's favorites" com 4 produtos, "What we promise"
- **Oferta:** 17% no site com o cupom VIP, só para a lista, até meia-noite
- **Números:** 16.766 envios, abertura 31,7%, clique 1,14%, 6 pedidos, US$ 847, US$ 50,5 por mil envios. Altura 3.176 px
- **Leitura:** clique baixo. A brincadeira ocupa a primeira tela e a oferta vem depois

#### 15/09 18h, VIP Day, disparo 3: quiz

![E-mail de 15/09 às 18h da Blue Wolf: quiz do VIP Day com três perguntas sobre a oferta do dia, prêmio de 17% OFF e produtos](blob/c7baa7be-1b7b)

- **Assunto:** "Prize reserved for \[nome\]". Pré-cabeçalho: "It's yours until 11:59 PM"
- **Estratégia:** quiz com três perguntas já respondidas (qual o desconto, até quando vale, quantos clientes satisfeitos). "Got all three right? Here's your prize", cupom, produtos
- **Oferta:** 17% com o cupom VIP
- **Números:** 16.699 envios, abertura 31,3%, clique 1,37%, 4 pedidos, US$ 324, US$ 19,4 por mil envios. Altura 3.553 px
- **Leitura:** único disparo das 18h que foi mal. O cupom só aparece depois do quiz, o assunto não é de notificação, e é o 12º envio do mês. A terceira pergunta afirma "more than 10,000" clientes satisfeitos: precisa ser o número real

#### 17/09, VIP Week, e-mail 1

![E-mail de 17/09 da Blue Wolf: VIP Week com 17% OFF no site, cupom VIP, colagem de bolsa, sapato e relógio, e prazo até domingo](blob/532009fc-fa69)

- **Assunto:** "VIP Day just became VIP WEEK". Pré-cabeçalho: "Your coupon is still valid until Sunday"
- **Estratégia:** extensão. Número e cupom na primeira tela, colagem de produtos, "The VIP Week didn't end on Tuesday", 4 produtos, "Sunday, 11:59 PM"
- **Oferta:** 17% com o cupom VIP até domingo 20/09
- **Números:** 16.762 envios, abertura 29,5%, clique 1,24%, 6 pedidos, US$ 567, US$ 33,9 por mil envios. Altura 2.788 px
- **Leitura:** estender uma oferta que já tinha ido mal não a recupera. Menor abertura do mês fora do segmento de 22 mil

#### 19/09, VIP Week, e-mail 2

![E-mail de 19/09 da Blue Wolf: VIP Week termina domingo à meia-noite, 17% OFF com o cupom VIP e destaques da semana](blob/74582861-2398)

- **Estratégia:** último aviso da VIP Week. "Ends Sunday at midnight", 17% grande, foto de produtos, cupom VIP, "This week's highlights"
- **Números:** envio em andamento na data da coleta (705 envios processados). Sem leitura ainda

### 20.5 O que o trimestre da Blue Wolf ensina, com o design à vista

1. **A oferta precisa estar na primeira tela.** Mesmo cupom, mesmo dia: o 7.7 das 11h esconde os 17% atrás de 2.500 px de rolagem e tem 1,27% de clique. O das 18h mostra no topo e tem 3,06%. No VIP Day, o teste de visão e o quiz repetem o erro.
2. **Mesma oferta, formato novo, vende de novo.** A Mid-Year Sale foi enviada três vezes em cinco dias (revelação, jornal, ligação) e fez 44 pedidos e US$ 2.944. É reenvio feito com design.
3. **O que funcionou pode voltar.** O jornal de julho voltou em setembro com o assunto "status changed" de agosto: 15 pedidos e 3,56% de clique.
4. **Fundo branco com cara de aviso de sistema tem os maiores cliques da conta**: 3,61% (28/08) e 3,20% (11/09). São os dois e-mails que menos parecem campanha.
5. **Antecipação boa é convite, agenda e FAQ, sem produto.** O esquenta do 7.7 rendeu o dobro do esquenta do 8.8, que trocou o convite por "o warm-up começou" e uma grade de produtos.
6. **Prova social e conteúdo sem oferta não pagam o envio.** Três provas sociais e o catálogo de indecisão ficaram entre US$ 24 e US$ 34 por mil envios.
7. **Dois eventos em seis dias é demais.** O VIP Day rendeu 35% menos que os outros picos, e a extensão não recuperou.
8. **Números de prova nos e-mails** ("6,747 reviews", "more than 10,000 customers", "first 100") precisam ser verificáveis na loja. É o mesmo ponto levantado no 11.11 de 2025 (seção 15).

## 21. Blue Wolf: estrutura bloco a bloco das campanhas que mais venderam

As dez campanhas de maior receita do trimestre usam quatro estruturas: pico com oferta na primeira tela, antecipação em formato de convite, aviso de sistema em fundo branco e texto puro assinado pelo fundador. As quatro estão descritas abaixo bloco a bloco, na ordem em que aparecem no e-mail. \[D, Figma e API da Omnisend, 18/09/2026\]

### 21.1 Os e-mails em modelo de texto

Os e-mails que não têm frame no Figma (o disparo das 7h de cada pico, 06/07, 25/07 e 03/09) são texto puro. Dois foram lidos pela API e confirmam o modelo: um único bloco de HTML, fundo branco, Arial 14 ou 15 px preto, sem logo, sem imagem, sem botão. Os links são texto azul em negrito. Rodapé só com o nome da loja e o descadastro.

| E-mail de texto | Abertura | Clique | Pedidos | Receita | Por mil envios | Clique em pedido |
| --- | --- | --- | --- | --- | --- | --- |
| 09/09 7h, "Your coupon has been released" | 35,3% | 1,15% | 13 | US$ 1.216 | US$ 72,3 | 6,7% |
| 06/07, "Your access for tomorrow is still pending" | 39,2% | 1,56% | 7 | US$ 874 | US$ 63,5 | 3,3% |
| 25/07, Reabertura | 36,7% | 1,23% | 8 | US$ 776 | US$ 50,1 | 4,2% |
| 15/09 7h, "You've been selected" | 33,2% | 1,27% | 5 | US$ 542 | US$ 32,3 | 2,3% |
| 08/08 7h, "Fwd: I was able to add your name" | 39,0% | 1,19% | 7 | US$ 504 | US$ 32,1 | 3,8% |
| 03/09, "Fwd: You Were Not Supposed to Know" | 29,3% | 0,83% | 4 | US$ 482 | US$ 22,2 | 2,2% |
| 07/07 7h, "Your coupon has been approved" | 40,2% | 1,47% | 6 | US$ 337 | US$ 24,6 | 3,0% |
| **Soma dos 7** | 35,7% | 1,22% | 50 | US$ 4.731 | US$ 41,5 | 3,6% |

O texto puro abre mais que a média da conta (35,6% contra 34,6%) e clica menos (1,21% contra 1,84%), porque tem um link só. Quem clica compra mais: 3,6% contra 2,9%. Rende quase o mesmo por envio que os e-mails de imagem (US$ 41,5 contra US$ 43,6) com custo de produção perto de zero. É a confirmação interna do que o Max defende (seção 9.4) e do que o 11.11 de 2025 já fazia (seção 15).

### 21.2 Estrutura A: pico com oferta na primeira tela

Usada em 08/08 18h (US$ 1.674), 07/07 18h (US$ 1.435), 22/07 Jornal (US$ 1.123), 20/07 Revele (US$ 1.066) e 09/09 18h (US$ 1.028).

**08/08 18h, a campanha de maior receita, 3.230 px**

1. **CABEÇALHO:** logo Blue Wolf centralizado sobre fundo preto.
2. **HERO, parte 1, selo do evento:** "8.8 End of Summer" em tipografia grande.
3. **HERO, parte 2, conversa simulada:** quatro balões entre dois clientes. "Check the site. 18% OFF on everything today with coupon 0808." / "Already got mine. Half the stuff I had my eye on is already sold out." / "Really? Is there still good stuff?" / "They do! But it's going fast... and only until midnight." / "I'm going now!!". A oferta, o cupom, a escassez e o prazo são ditos por terceiros.
4. **HERO, parte 3, foto e oferta:** foto de modelo usando o produto à noite. Sobre a foto: "18% OFF", caixa "Coupon: 0808", botão "Shop now" e a linha "Only until midnight tonight".
5. **BODY, grade de produtos:** título "There's still time to grab these:". Quatro produtos em grade 2x2 (na Omnisend, bloco dinâmico de vistos recentemente, com os mais populares como reserva). Botão "View all products".
6. **FECHAMENTO, segunda chamada:** título "Now or never". Duas linhas: a oferta acaba à meia-noite. "18% OFF", caixa do cupom repetida, botão "Get it before midnight".
7. **RODAPÉ:** três garantias com ícone (Express shipping, Product quality, Secure payment), logo e descadastro.

**07/07 18h, segunda maior receita, 3.178 px**

1. **CABEÇALHO:** logo.
2. **HERO:** selo "Last call", "7.7 Summer Sale", "17% OFF", caixa "Use code: 0707", botão "Shop now", linha "Expires: tonight, 11:59 PM". Tudo antes da primeira rolagem.
3. **BODY, parte 1, texto de urgência:** título "The morning sun is starting to fade." Quatro parágrafos de duas linhas: faltam poucas horas, o que sobrou ainda está disponível, quem chegou cedo já levou, depois da meia-noite os 17% viram memória.
4. **BODY, parte 2, grade de produtos:** "What's still in the Summer Sale:". Quatro produtos 2x2. Botão "View all".
5. **BODY, parte 3, linha do tempo:** cartão "The sun is clocking out" com 7AM, 11AM, 18PM e 12AM, cada um com marcadores que vão apagando.
6. **FECHAMENTO:** "Every good summer comes to a close. This one? It ends at midnight." Oferta repetida em uma linha, botão "Enter the Summer Sale", prazo repetido.
7. **RODAPÉ:** garantias, logo, descadastro.

**22/07 Jornal e 09/09 18h, mesmo formato, 2.469 px**

1. **CABEÇALHO em formato de jornal:** "Breaking News", data por extenso do dia do envio e o nome da loja.
2. **HERO:** manchete com o prazo ("48h until the end" ou "6 hours left"), nome da venda, duas linhas com a oferta e a data de término, caixa do cupom.
3. **BODY, parte 1, foto:** foto da embalagem do produto. Botão preto "Buy now".
4. **BODY, parte 2, grade de produtos:** "The headline highlights:", uma linha lembrando o cupom, quatro produtos 2x2, botão "See all offers".
5. **RODAPÉ:** garantias, logo, descadastro.

**20/07 Revele, 2.169 px, o mais curto do grupo**

1. **CABEÇALHO:** logo.
2. **HERO:** "Reveal your mid-year sale discount", "until 37% OFF", faixa de papel rasgado mostrando "+15% OFF", caixa "Coupon: EXTRA", linha com a validade, botão "Take advantage of offers now".
3. **BODY:** "Mid-year sale highlights:", quatro produtos 2x2, botão "View all products".
4. **RODAPÉ:** garantias, logo, descadastro.

**Molde da estrutura A**

| Bloco | Conteúdo | Regra |
| --- | --- | --- |
| HERO | Nome do evento, percentual, cupom, prazo com hora, um botão | Tudo visível sem rolar. Um formato emprestado de fora do e-mail: conversa, jornal, papel rasgado |
| BODY 1 (opcional) | Texto de urgência ou foto de produto | No máximo quatro parágrafos de duas linhas |
| BODY 2 | Quatro produtos 2x2 com título de urgência | Bloco dinâmico da Omnisend. Título retoma o prazo |
| FECHAMENTO | Oferta e cupom repetidos, segundo botão | Só nos e-mails acima de 3.000 px |
| RODAPÉ | Três garantias, logo, descadastro | Fixo |

### 21.3 Estrutura B: antecipação em formato de convite

Usada em 03/07 (US$ 1.171, maior abertura do trimestre) e 01/07 (US$ 654). Nenhuma das duas tem produto ou cupom.

**03/07, 3.133 px**

1. **CABEÇALHO:** logo.
2. **HERO:** selo "Invitation update", "7.7 Summer Sale", três caixas com os horários (7AM, 11AM, 18PM), linha "3 windows. 3 moments. Those who know, arrive early.", botão "(I) want to get ready".
3. **BODY, parte 1, gancho de continuidade:** título "On Wednesday we sent you an invitation." Quatro linhas curtas: hoje, como prometido, a agenda completa.
4. **BODY, parte 2, agenda:** título "The 3 moments of 7.7:". Três cartões, um por horário, cada um com nome e função: Early access, Spotlight drop, Final call. Linha "3 windows. 3 moments. Each one with its own purpose."
5. **BODY, parte 3, FAQ:** título "Questions we have been receiving:". Quatro cartões de pergunta e resposta: preciso me inscrever, vale no site e por e-mail, e se eu perder as 7h, o 7.7 vai ser prorrogado.
6. **FECHAMENTO, barra de status:** cartão "Invitation status" com quatro etapas (Sent, Read, Confirmed, Ready) e as três primeiras marcadas. Linha "Just one last step: show up on the day." Botão "Get ready for 7.7".
7. **RODAPÉ:** garantias, logo, descadastro.

**01/07, 2.514 px:** mesma estrutura, com hero "You're officially invited", um bloco "What's coming next" com as datas dos três próximos e-mails no lugar da agenda, e a barra de status parada em "Read".

**Molde da estrutura B**

| Bloco | Conteúdo | Regra |
| --- | --- | --- |
| HERO | Selo de convite, nome do evento, horários, botão de confirmação | O botão pede uma ação da pessoa, não uma compra |
| BODY 1 | Gancho com o e-mail anterior | Cada e-mail da sequência cita o anterior e anuncia o próximo |
| BODY 2 | Agenda do dia, um cartão por horário | Cada horário com nome e função diferentes |
| BODY 3 | FAQ com quatro perguntas | Responde objeções reais antes do dia |
| FECHAMENTO | Barra de status que avança a cada e-mail | Elemento fixo que dá continuidade à sequência |

O esquenta do 8.8 e o do 9.9 trocaram esse molde por "o warm-up começou" mais grade de produtos, e renderam metade.

### 21.4 Estrutura C: aviso de sistema em fundo branco

Usada em 11/09, ressaca do 9.9 (US$ 1.303, terceira maior receita) e em 28/08 (maior clique do trimestre).

**11/09, 1.735 px**

1. **FAIXA SUPERIOR:** barra azul com "Active deals · No coupon required".
2. **CABEÇALHO:** logo sobre fundo branco.
3. **HERO, caixa de aviso:** cartão com borda e ícone vermelho de alerta. Título "Notice: September 11, 2026". Três frases: por causa da alta demanda no 9.9, o estoque de vários produtos está bem abaixo do normal. Em vermelho: os preços promocionais continuam ativos, mas quando o estoque atual acabar não será possível manter. Última linha: o sistema mostra estoque baixo em vários itens, veja o que ainda está disponível. Botão largo "See remaining stock".
4. **BODY, grade de produtos:** título "Get the last items". Quatro produtos 2x2.
5. **FECHAMENTO:** uma linha ("Promotional prices are active while stocks last") e botão "See all deals".
6. **RODAPÉ:** garantias, logo, descadastro.

**Molde da estrutura C**

| Bloco | Conteúdo | Regra |
| --- | --- | --- |
| FAIXA | Condição da oferta em uma linha | "Sem cupom" remove uma etapa |
| HERO | Caixa de aviso datada, com motivo e consequência | Tom de comunicado, não de promoção. Data real do envio |
| BODY | Quatro produtos | Título de escassez |
| FECHAMENTO | Uma linha e um botão | E-mail inteiro abaixo de 2.000 px |

O motivo do aviso (estoque baixo) precisa ser verdadeiro na loja.

### 21.5 Estrutura D: texto puro do fundador

**09/09 7h, "Your coupon has been released", quinta maior receita do trimestre**

1. **SAUDAÇÃO:** "Hello, \[nome\]!"
2. **QUEM FALA:** "This is Michael, founder of \[loja\], speaking directly to you."
3. **MOTIVO DA OFERTA:** hoje começa a nova temporada e, antes disso, a maior liquidação do ano: tudo no site precisa sair para dar lugar ao que vem.
4. **O EVENTO E A VANTAGEM DA HORA:** "today is the 9.9 New Season Sale". Agora, às 7h, com o site recém-aberto, quem chega primeiro leva a melhor parte.
5. **CONFIRMAÇÃO PESSOAL:** "Just to confirm this access is going to the right customer:" seguido de duas linhas com o nome e o e-mail do contato.
6. **OFERTA:** o cupom **0909** em fonte maior e "19% OFF across the entire site".
7. **LINK ÚNICO:** "Click here and claim your 19% OFF >>>" em azul e negrito.
8. **REFORÇO:** estoque cheio, catálogo completo. "This is the part of the day no one gets to repeat." É o único dia do ano em que o site inteiro entra em liquidação.
9. **AGENDA DO DIA:** às 11h o site abre para todos, às 18h é a última chamada. "But these first hours? They belong only to those who were on the list."
10. **ASSINATURA:** "Warm regards, Michael".
11. **P.S.:** à meia-noite o cupom expira, e muita coisa não volta.

**06/07, "Your access for tomorrow is still pending", véspera do 7.7**

1. **SAUDAÇÃO.**
2. **ANÚNCIO:** amanhã começa o 7.7 Summer Sale.
3. **AGENDA:** "you will receive 3 emails": 7 AM early access, 11 AM a surprise, 6 PM last call.
4. **ESCASSEZ:** muitos itens vão esgotar rápido.
5. **TRÊS TAREFAS PARA O ACESSO ANTECIPADO:** mover o e-mail para a aba principal, responder "Confirmed", clicar no link.
6. **SEGREDO:** "here is something few people know": o cupom é 0707 e passa a valer amanhã às 7h. Quanto ele tira? Só aplicando para descobrir.
7. **LINK PARA O SITE** com as ofertas atuais.
8. **DESPEDIDA.**

O pedido de resposta e de mover para a aba principal é uma alavanca de reputação de domínio, a mesma do planejamento do 11.11 de 2025. O endereço de resposta deste e-mail está como bruno@convertfy.me, e não o da loja como nos demais. Se não foi intencional, vale conferir para onde foram as respostas "Confirmed".

**Molde da estrutura D**

| Bloco | Conteúdo | Regra |
| --- | --- | --- |
| Abertura | Saudação com nome e uma frase de quem fala | Pessoa real, com nome e cargo |
| Motivo | Por que a oferta existe hoje | Uma razão concreta, em duas ou três frases |
| Confirmação | Nome e e-mail do contato em linhas separadas | Reforça que é individual |
| Oferta | Cupom em destaque e percentual | Uma linha |
| Link | Um único link em texto | Azul, negrito, com o benefício escrito |
| Agenda | O que acontece nas próximas horas | Dá motivo para agir agora |
| Assinatura e P.S. | Nome e o prazo | O P.S. repete só o prazo |

### 21.6 O que levar para a Black Friday

| Momento da BF | Estrutura | Referência |
| --- | --- | --- |
| Antecipação, 17 a 24/11 | B, convite com agenda, FAQ e barra de status | 03/07 |
| Véspera | D, texto com três tarefas e o cupom revelado antes | 06/07 |
| Primeiro disparo de cada dia de pico, 7h | D, texto do fundador com confirmação pessoal | 09/09 7h |
| Disparo do meio do dia | A, com formato emprestado (jornal, conversa) | 22/07 |
| Último disparo, 18h, e último dia | A, com prazo na primeira tela e fechamento repetindo o cupom | 08/08 18h e 07/07 18h |
| Ressaca e Cyber Monday estendida | C, aviso de sistema sem cupom | 11/09 |

Dois ajustes valem para as quatro estruturas: todo link deve ir para a coleção da oferta com o cupom aplicado, não para a home, e os números de prova (clientes, reviews, primeiros 100) precisam ser os reais da loja.

## 22. Como chegar ao ranking geral da Convertfy: o que coletar e como comparar lojas

A unidade de comparação entre lojas deve ser o modelo de campanha, não a campanha isolada. Os arquivos do Figma mostram que o mesmo modelo ("campanha - 03/07", "campanha - 22/07") é aplicado a dezenas de lojas na mesma data, com a marca trocada. Isso permite medir cada modelo em 15 ou mais lojas ao mesmo tempo e separar o que é efeito do modelo do que é efeito da loja. \[I, a partir das seções 18 a 21\]

### 22.1 A chave que liga tudo

Cada linha da base é um envio: **modelo de campanha × loja × data**. O modelo é identificado pelo nome interno que vocês já usam na Omnisend ("\[data\] - \[hora\] - \[segmento\] - \[nome\] - \[idioma\]") e pelo nome do frame no Figma. Para o ranking funcionar, o nome do modelo precisa ser o mesmo em todas as lojas. Onde não for, a data e a hora resolvem.

### 22.2 Campos a coletar por envio

| Grupo | Campo | De onde vem |
| --- | --- | --- |
| Identificação | Loja, data, hora, nome do modelo, idioma, segmento usado | API, lista de campanhas |
| Texto | Assunto, pré-cabeçalho, nome do remetente, endereço de resposta | API, lista de campanhas |
| Resultado bruto | Envios, aberturas únicas, cliques únicos, pedidos, receita, descadastros, reclamações de spam, falhas | API, relatório por campanha |
| Teste | Se teve teste A/B, variantes e vencedora | API, campo de teste A/B da campanha |
| Reenvio | Se teve reenvio para quem não abriu e o resultado dele | API, campanhas do tipo reforço |
| Design | Altura, modelo de imagem ou de texto, estrutura (A, B, C, D ou outra), número de produtos, link de destino | Figma e conteúdo do e-mail na API |

### 22.3 Campos de classificação, preenchidos uma vez por modelo

Como o modelo é o mesmo em todas as lojas, a classificação é feita uma vez e vale para todas.

| Campo | Valores |
| --- | --- |
| Ciclo | 7.7, 8.8, 9.9, 11.11, BF, fora de ciclo |
| Papel na sequência | Antecipação, véspera, pico 7h, pico 11h, pico 18h, ressaca, extensão, avulsa |
| Tipo | Oferta, gamificada, notificação, temática do momento, catálogo, prova social, conteúdo, reativação |
| Estrutura | A pico com oferta na primeira tela, B convite, C aviso de sistema, D texto do fundador, outra |
| Oferta | Percentual, tipo (site todo, cupom, sem cupom, mistério, brinde, frete), prazo em horas |
| Primeira tela | Tem número, tem cupom, tem prazo (sim ou não para cada um) |
| Assunto | Notificação pessoal, prazo, curiosidade, anúncio da marca, prova social. Usa nome, usa emoji |
| Formato emprestado | Conversa, jornal, ligação, papel rasgado, status, recibo, calendário, quiz, nenhum |

### 22.4 Contexto por loja, para separar o efeito da loja

| Campo | Por que importa |
| --- | --- |
| Nicho e ticket médio | Um modelo pode funcionar em moda e não em suplemento |
| Mercado e idioma | Brasil, EUA, Reino Unido, Europa. Muda data comemorativa, fuso e regra legal |
| Tamanho e idade da lista | Lista de mil contatos dá ruído. Lista nova abre mais |
| Idade da conta e nível A, B ou C | Define o quanto dá para abrir o envio |
| Receita total da loja no período | Para calcular a participação do e-mail. Ainda não coletado em nenhuma loja |
| Receita de automações e de campanhas | A proporção ficou em 77% a 78% nas duas lojas |
| Canais ativos | E-mail, SMS, push, WhatsApp |
| Pop-up | Exibições, inscritos, taxa, campos pedidos |
| Média da loja no mês | Receita por mil envios, abertura e clique médios. É a régua do índice abaixo |

### 22.5 Métricas normalizadas

| Métrica | Conta | Para que serve |
| --- | --- | --- |
| Receita por mil envios | Receita ÷ envios × 1.000 | Comparar campanhas da mesma loja |
| **Índice do modelo** | Receita por mil envios da campanha ÷ média da loja no mês | Comparar o mesmo modelo entre lojas de tamanhos e nichos diferentes. Índice 2,0 significa o dobro da média daquela loja |
| Clique em pedido | Pedidos ÷ cliques | Separa problema de e-mail de problema de página de destino |
| Descadastros por pedido | Descadastros ÷ pedidos | Custo de lista de cada venda. O 08/08 18h da Blue Wolf custou 7 contatos por pedido |
| Receita por descadastro | Receita ÷ descadastros | Mesmo custo, em dinheiro |
| Abertura relativa | Abertura da campanha ÷ média da loja | Mede o assunto sem o efeito da reputação da conta |

Na Blue Wolf, calculado sobre a média do trimestre (US$ 43,58), o índice já mostra a ordem real: 08/08 18h com 2,47, 07/07 18h com 2,42, 03/07 com 1,93, 11/09 com 1,78. O warm-up de 03/08 fica em 0,11.

### 22.6 Os rankings a produzir

| Ranking | Pergunta que responde |
| --- | --- |
| Top modelos de todos os tempos | Quais modelos têm a maior mediana de índice, contando só os que rodaram em pelo menos 10 lojas |
| Top modelos por mês | O que funcionou em cada mês, para ver sazonalidade e fadiga |
| Modelos consistentes | Quais ficam no quarto superior em 70% ou mais das lojas. São os obrigatórios da BF |
| Modelos polarizados | Muito bons em umas lojas e ruins em outras. Pedem segmentação por nicho ou mercado |
| Piores consistentes | O que sai do calendário |
| Por papel na sequência | Melhor antecipação, melhor véspera, melhor disparo de cada horário, melhor ressaca |
| Por estrutura e formato emprestado | Se conversa, jornal, aviso e texto puro repetem o resultado fora da Blue Wolf |
| Por nicho, mercado e idioma | O que muda entre Brasil e lojas globais |
| Assuntos | Melhores assuntos por abertura relativa, separados por tipo |
| Texto contra imagem | Mesma data, mesmo papel, em todas as lojas |
| Custo de lista | Modelos que vendem, mas custam muitos descadastros |

### 22.7 Regras para o ranking não enganar

1. **Mediana, não média.** Um pedido de US$ 538 na Emyerre distorceu uma campanha inteira.
2. **Volume mínimo.** Campanha entra no ranking da loja com pelo menos 5 mil envios. Modelo entra no ranking geral com pelo menos 10 lojas ou 100 pedidos somados.
3. **Mesmo segmento.** Envio para segmento ampliado (o de 22 mil da Blue Wolf) é marcado e comparado à parte.
4. **Campanha em andamento fica fora.** Esperar 5 dias depois do envio, por causa da janela de atribuição.
5. **Envios de teste pequenos ficam fora**, como os de 570 a 961 contatos da Blue Wolf.
6. **Atribuição é a da Omnisend**, igual em todas as contas. Não misturar com receita total da loja na mesma conta.
7. **Um modelo bom em uma loja é hipótese. Em dez, é padrão.**

### 22.8 O que ainda vale puxar de cada conta

| Dado | O que responde | Custo |
| --- | --- | --- |
| Automações por mensagem | Quais e-mails de cada fluxo vendem e onde cortar. Feito na Emyerre, não na Blue Wolf | 1 consulta |
| Receita total da loja por mês | Participação do e-mail no faturamento | 1 consulta |
| Envios por hora do dia | Se 7h, 11h e 18h são os melhores horários ou só os que vocês usam | 1 consulta |
| Testes A/B de assunto | Banco de assuntos vencedores com prova direta | Vem na lista de campanhas |
| Reenvios para quem não abriu | Se o reenvio do Max se paga na carteira | Vem na lista de campanhas |
| Pop-ups | Taxa de conversão por formato e por campos pedidos | 1 consulta por formulário |
| Crescimento e perda de lista por mês | Se a lista cresce mais do que o calendário queima | 1 consulta |
| Texto dos e-mails em modelo de texto | Banco de copy com resultado. Só esses são legíveis pela API | 1 leitura por e-mail |
| Novembro de 2025 | Resultado real do 11.11 e da BF nas contas que já existiam. É o dado que faltava na seção 15 | 1 consulta por conta |

O último item é o mais valioso: as contas mais antigas ainda guardam novembro de 2025 na Omnisend. Vale priorizar a conexão de lojas que já eram clientes na última Black Friday.

### 22.9 Ordem sugerida das próximas lojas

Para o ranking geral valer, a amostra precisa variar. Sugestão de critérios para escolher as próximas 13 lojas: pelo menos 4 do Brasil em português, pelo menos 3 com conta ativa desde antes de novembro de 2025, pelo menos 2 com SMS ou WhatsApp ativo, nichos diferentes (moda, joias, casa, beleza, suplemento), e listas de tamanhos diferentes (abaixo de 5 mil, de 5 a 30 mil, acima de 30 mil).

### 22.10 Onde guardar

A base começou em um arquivo CSV com as 46 campanhas da Blue Wolf já no formato acima, incluindo o índice por campanha. Cada nova loja entra como novas linhas. Com 15 lojas serão perto de 700 envios, o suficiente para os rankings da seção 22.6.

## 23. Base consolidada e painel de achados

Esta seção é o ponto de chegada de cada loja analisada: o ranking da loja pelo índice, o resultado por estrutura e o painel que acumula o que já se repetiu entre lojas. Hoje tem uma loja completa (Blue Wolf) e uma parcial (Emyerre). \[D, base de 18/09/2026\]

### 23.1 Ranking da Blue Wolf pelo índice

RPM é a receita por mil envios. O índice divide o RPM da campanha pela média da loja no trimestre (US$ 43,58). Descadastros por pedido mede o custo de lista de cada venda.

| # | Data | Modelo | Papel | Estrutura | RPM | Índice | Pedidos | Clique em pedido | Descadastros por pedido |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 08/08 18h | 8.8, disparo 3, status mudou | pico 18h | A | 107,5 | 2,47 | 18 | 5,5% | 7,2 |
| 2 | 07/07 18h | 7.7, disparo 3, final call | pico 18h | A | 105,3 | 2,42 | 14 | 3,4% | 6,7 |
| 3 | 03/07 | Antecipação 7.7, agenda | antecipação | B | 84,1 | 1,93 | 14 | 5,3% | 6,9 |
| 4 | 11/09 | Ressaca 9.9 | ressaca | C | 77,7 | 1,78 | 14 | 2,6% | 3,5 |
| 5 | 09/09 7h | 9.9, disparo 1, cupom liberado | pico 7h | D texto | 72,3 | 1,66 | 13 | 6,7% | 3,6 |
| 6 | 22/07 | Jornal | notificação | A | 71,9 | 1,65 | 15 | 4,7% | 6,7 |
| 7 | 15/07 | Favoritos do 7.7 | ressaca | outra | 71,3 | 1,64 | 14 | 2,8% | 6,7 |
| 8 | 20/07 | Revele seu desconto | gamificada | A | 68,5 | 1,57 | 18 | 7,0% | 5,5 |
| 9 | 17/06 | Semana Copa 2 | temática | outra | 65,9 | 1,51 | 12 | 2,9% | 7,3 |
| 10 | 06/07 | Antecipação 7.7, acesso pendente | véspera | D texto | 63,5 | 1,46 | 7 | 3,3% | 16,4 |
| 11 | 09/09 18h | 9.9, disparo 3, jornal | pico 18h | A | 61,4 | 1,41 | 15 | 2,5% | 5,6 |
| 12 | 17/08 | Segunda turbo | gamificada | outra | 60,4 | 1,39 | 6 | 2,5% | 9,2 |
| 13 | 18/07 | Final da Copa | temática | outra | 55,5 | 1,27 | 13 | 3,6% | 5,5 |
| 14 | 07/07 11h | 7.7, disparo 2, role até o fim | pico 11h | outra | 53,9 | 1,24 | 12 | 6,9% | 5,8 |
| 15 | 15/09 11h | VIP Day, teste de visão | pico 11h | outra | 50,5 | 1,16 | 6 | 3,1% | 6,7 |
| 16 | 31/07 | Sexta premiada | gamificada | outra | 50,2 | 1,15 | 9 | 3,6% | 7,3 |
| 17 | 25/07 | Reabertura | ressaca | D texto | 50,1 | 1,15 | 8 | 4,2% | 10,5 |
| 18 | 31/08 | Catálogo fecha mês | catálogo | outra | 49,1 | 1,13 | 8 | 1,7% | 9,6 |
| 19 | 24/07 | Ligação | notificação | A | 49,0 | 1,12 | 11 | 4,2% | 6,3 |
| 20 | 24/08 | Semana 15%, On & Off | semana 15% | outra | 47,2 | 1,08 | 8 | 1,7% | 8,4 |
| 21 | 01/07 | Antecipação 7.7, convite | antecipação | B | 46,8 | 1,07 | 8 | 2,3% | 12,1 |
| 22 | 07/08 | Esquenta 8.8, véspera | véspera | outra | 45,9 | 1,05 | 10 | 4,9% | 5,9 |
| 23 | 11/08 | Ressaca 8.8 | ressaca | outra | 40,4 | 0,93 | 8 | 4,2% | 10,0 |
| 24 | 28/08 | Notificação do futuro | notificação | C | 39,1 | 0,90 | 9 | 1,5% | 9,4 |
| 25 | 19/06 | Álbum de figurinha | gamificada | outra | 37,5 | 0,86 | 6 | 2,7% | 7,2 |
| 26 | 08/08 11h | 8.8, disparo 2, primeiros 100 | pico 11h | A | 36,5 | 0,84 | 8 | 3,9% | 8,0 |
| 27 | 14/08 | Sextou | recorrente | outra | 34,9 | 0,80 | 6 | 2,7% | 9,3 |
| 28 | 17/09 | VIP Week, 1 | extensão | A | 33,9 | 0,78 | 6 | 2,9% | 5,3 |
| 29 | 29/07 | UGC social proof | prova social | outra | 33,6 | 0,77 | 7 | 4,9% | 6,4 |
| 30 | 05/09 | Esquenta 9.9, calendário | antecipação | outra | 33,4 | 0,77 | 12 | 2,4% | 5,6 |
| 31 | 15/09 7h | VIP Day, disparo 1 | pico 7h | D texto | 32,3 | 0,74 | 5 | 2,3% | 11,2 |
| 32 | 08/08 7h | 8.8, disparo 1, Fwd | pico 7h | D texto | 32,1 | 0,74 | 7 | 3,8% | 12,4 |
| 33 | 05/08 | Esquenta 8.8, 2 | antecipação | outra | 30,7 | 0,70 | 6 | 3,9% | 8,7 |
| 34 | 09/09 11h | 9.9, disparo 2, relógio | pico 11h | A | 30,5 | 0,70 | 7 | 1,5% | 7,4 |
| 35 | 14/09 | Antecipação VIP Day | véspera | C | 26,2 | 0,60 | 5 | 1,9% | 12,0 |
| 36 | 19/08 | UGC Dia da Fotografia | prova social | outra | 24,9 | 0,57 | 5 | 3,0% | 12,4 |
| 37 | 26/06 | Social proof | prova social | outra | 24,9 | 0,57 | 5 | 3,5% | 9,6 |
| 38 | 07/07 7h | 7.7, disparo 1, cupom aprovado | pico 7h | D texto | 24,6 | 0,56 | 6 | 3,0% | 15,2 |
| 39 | 21/08 | Catálogo indecisão | catálogo | outra | 24,1 | 0,55 | 5 | 1,6% | 14,2 |
| 40 | 03/09 | Esquenta 9.9, Fwd | antecipação | D texto | 22,2 | 0,51 | 4 | 2,2% | 21,0 |
| 41 | 15/09 18h | VIP Day, quiz | pico 18h | outra | 19,4 | 0,45 | 4 | 1,8% | 9,5 |
| 42 | 08/09 | Esquenta 9.9, véspera | véspera | outra | 19,3 | 0,44 | 5 | 0,9% | 13,2 |
| 43 | 27/07 | Segunda da sorte | gamificada | outra | 17,2 | 0,40 | 3 | 1,1% | 28,0 |
| 44 | 07/09 | Esquenta 9.9, 3 | antecipação | outra | 13,0 | 0,30 | 3 | 0,6% | 22,7 |
| 45 | 26/08 | Semana 15%, Escolha o caminho | semana 15% | outra | 12,6 | 0,29 | 3 | 1,9% | 21,7 |
| 46 | 03/08 | Esquenta 8.8, warm-up | antecipação | outra | 4,6 | 0,11 | 1 | 0,5% | 65,0 |

### 23.2 Resultado por estrutura

| Estrutura | Campanhas | Pedidos | RPM | Índice | Clique em pedido | Descadastros por pedido |
| --- | --- | --- | --- | --- | --- | --- |
| B, convite com agenda | 2 | 22 | US$ 65,4 | 1,50 | 3,6% | 8,8 |
| A, pico com oferta na primeira tela | 9 | 112 | US$ 61,6 | 1,41 | 3,7% | 6,5 |
| C, aviso de sistema em fundo branco | 3 | 28 | US$ 47,7 | 1,09 | 2,0% | 6,9 |
| D, texto puro | 7 | 50 | US$ 41,5 | 0,95 | 3,6% | 11,3 |
| Outra (conceito, catálogo, prova social, gamificada sem oferta na primeira tela) | 25 | 177 | US$ 35,9 | 0,82 | 2,5% | 9,0 |

Três leituras. As estruturas A e B rendem 40% a 50% acima da média da loja, e mais da metade do calendário (25 de 46) usa "outra", que rende 18% abaixo. O texto puro converte bem quem clica, mas é o que mais custa descadastro por pedido (11,3): a linha de assunto de alta curiosidade abre, e parte de quem abre sai. A estrutura C tem o menor custo de lista nos e-mails de oferta real (3,5 na ressaca do 9.9).

### 23.3 Painel de achados acumulados

| # | Achado | Emyerre | Blue Wolf | Situação | Uso na BF |
| --- | --- | --- | --- | --- | --- |
| 1 | Automações fazem perto de 78% da receita de e-mail | 78% | 77% | Repetiu em 2 de 2 | Revisar fluxos antes de escalar campanhas |
| 2 | Antecipação sem cupom vende | Sim | Sim, de 46% a 108% do pico | Repetiu em 2 de 2 | Não deixar novembro sem oferta ativa no site |
| 3 | Disparo das 18h é o melhor do dia de pico | Sim | Sim, em 3 de 4 | Repetiu em 2 de 2 | Guardar o melhor criativo para as 18h |
| 4 | Assunto de notificação pessoal lidera a abertura | Sim | Sim | Repetiu em 2 de 2 | Banco de assuntos de status, cupom, prazo, comunicado |
| 5 | Ampliar o envio para não engajados não traz resultado | Importação de 424 contatos | Segmento de 22 mil e reativação | Repetiu em 2 de 2 | Inativos só em conta nível A e só na oferta máxima |
| 6 | Oferta na primeira tela dobra o clique | Não medido | 3,06% contra 1,27% no mesmo dia | 1 de 1 | Regra de layout |
| 7 | Mesma oferta em formato novo vende de novo | Não medido | 44 pedidos em 3 envios | 1 de 1 | Substitui o reenvio simples |
| 8 | Altura do e-mail não explica resultado | Não medido | r = -0,02 | 1 de 1 | Não encurtar por encurtar |
| 9 | Prova social como e-mail inteiro é o pior formato | Não medido | 3 de 3 | 1 de 1 | Prova entra como bloco |
| 10 | Dois eventos em menos de 7 dias derrubam o segundo | Não medido | VIP Day 35% abaixo | 1 de 1 | Espaçar 11.11, Early Access e BF |
| 11 | Régua de logística com oferta paga | Não tem | US$ 15.580 | Oportunidade | Implantar nas contas antes de novembro |
| 12 | Todo clique vai para a página inicial | Não verificado | Sim | A verificar nas demais | Link para a coleção com cupom aplicado |
| 13 | Ressaca vende | Não | Sim, 44 pedidos | Divergiu | Aguardar mais lojas |
| 14 | Viewed Product vende | Não | Sim, 100 pedidos | Divergiu por volume | Aguardar mais lojas |

Um achado vira padrão com 10 de 15 lojas ou 100 pedidos somados (seção 17.10). Pelo critério de pedidos, só o achado 6 já passa na Blue Wolf sozinha (112 pedidos na estrutura A). O disparo das 18h soma 51.

### 23.4 Roteiro de coleta por loja, versão 2

| Passo | O que fazer | Consultas |
| --- | --- | --- |
| 1 | Confirmar a conta conectada e o fuso | 1 |
| 2 | Listar campanhas enviadas dos últimos 3 meses, com assunto e pré-cabeçalho | 1 |
| 3 | Relatório por campanha, por automação e por mês | 1 |
| 4 | Automações por mensagem | 1 |
| 5 | Receita total da loja por mês | 1 |
| 6 | Se a conta existia: campanhas e resultado de novembro de 2025 | 2 |
| 7 | Ler o texto dos e-mails em modelo de texto entre os 10 melhores | 2 a 4 |
| 8 | Receber as prints da linha da loja no Figma, recortar e embutir | sem consulta |
| 9 | Gerar as linhas da loja na base e o ranking pelo índice | sem consulta |
| 10 | Escrever a ficha no molde da seção 20 e atualizar o painel 23.3 | sem consulta |

Total de 9 a 11 consultas por loja, dentro do limite de 55 por dia por conta.

### 23.5 Pendências atualizadas em 18/09/2026

| Pendência | Depende de |
| --- | --- |
| Emyerre no molde da seção 20, com imagens | Prints da linha da Emyerre no Figma |
| Emyerre na base consolidada | Reprocessar os dados da seção 17 |
| Blue Wolf: automações por mensagem, receita total da loja, texto dos outros 5 e-mails de texto | 4 a 7 consultas |
| Novembro de 2025 em contas antigas | Conectar lojas que já eram clientes na última BF |
| Conferir o endereço de resposta do e-mail de 06/07 da Blue Wolf | Bruno |
| Conferir os números de prova usados nos e-mails (reviews, clientes, primeiros 100) | Time de produção |
| Origem e consentimento dos 424 contatos importados na Emyerre em 14/09 | Bruno |
| Próximas 13 lojas, com a variedade da seção 22.9 | Bruno |
| Material do Max ainda não lido e fontes externas a conferir | Seção 14 |
| Entregas finais: mapa mental, skills de planejamento e de copy, planilha de classificação, calendário até março de 2027 | Depois do consolidado de lojas |

## 24. Análise de contas Omnisend: loja 3, Clube Rock

A Clube Rock é a primeira loja brasileira e a maior da amostra: 55 campanhas, 2,5 milhões de envios, 1.950 pedidos e R$ 284 mil em três meses. Ela confirma quatro achados das outras lojas e muda um: aqui o melhor e-mail do trimestre é um texto puro do fundador às 7h, com índice 3,52. \[D, API da Omnisend, coleta em 19/09/2026\]

Dados de 17/06 a 17/09/2026, em reais. Ainda faltam para esta loja: prints do Figma, automações por mensagem e receita total da loja.

### 24.1 Contexto da loja

| Item | Clube Rock |
| --- | --- |
| Site e mercado | cluberock.com.br. Brasil, português, BRL |
| O que vende | Camisetas de bandas de rock. Oferta recorrente de kit: 3 peças por R$ 169 a R$ 189, com frete grátis |
| Conta Omnisend | Criada em abril de 2026. Só e-mail. Sem dados de novembro de 2025 |
| Lista de envio | De 33 mil contatos em junho a 50 mil em setembro. Um segmento ampliado de 80 mil foi usado no esquenta do 9.9 e no 7 de Setembro |
| Remetente | "Clube Rock" nas campanhas de imagem. "Henrique da Clube Rock" nos textos do fundador |
| Campanhas no trimestre | 55 campanhas, 2.517.644 envios, abertura de 23,0%, clique de 0,75%, 1.950 pedidos, R$ 284.022, R$ 112,8 por mil envios, ticket de R$ 146 |
| Reputação | Descadastro de 0,33% por envio. Spam de 0,0148% |
| Automações no trimestre | 9 fluxos, R$ 800.479. Fazem 74% da receita de e-mail |
| Principais fluxos | Welcome R$ 368 mil (2.751 pedidos), carrinho abandonado R$ 177 mil, checkout abandonado R$ 149 mil, produto visto R$ 34 mil, rastreio criado R$ 24 mil, pedido confirmado R$ 18 mil, upsell R$ 14 mil |
| Calendário | Os mesmos modelos da Blue Wolf traduzidos, mais datas e lançamentos próprios: Dia Mundial do Rock (13/07), coleção Ouro Nacional, lançamento Oversized, estampa da turnê do System of a Down, Rock in Rio, 7 de Setembro, Dia do Cliente (15/09) |

### 24.2 Números por mês

| Mês | Campanhas | Envios | Abertura | Clique | Pedidos | Receita | Por mil envios | Índice |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Junho, a partir de 17/06 | 3 | 100.512 | 23,8% | 0,61% | 103 | R$ 13.877 | R$ 138,1 | 1,22 |
| Julho | 20 | 775.554 | 24,8% | 0,98% | 735 | R$ 108.219 | R$ 139,5 | 1,24 |
| Agosto | 17 | 774.271 | 24,4% | 0,80% | 590 | R$ 86.099 | R$ 111,2 | 0,99 |
| Setembro, até 17/09 | 15 | 867.307 | 20,2% | 0,51% | 522 | R$ 75.826 | R$ 87,4 | 0,77 |

Mesma curva da Blue Wolf: julho é o melhor mês e o rendimento por envio cai em agosto e setembro. Em setembro, quatro envios foram para o segmento de 80 mil.

### 24.3 Datas duplas e eventos

| Ciclo | Antecipação | Dia de pico, 3 disparos | Relação |
| --- | --- | --- | --- |
| 7.7 | 3 e-mails: 79 pedidos, R$ 9.830 | 143 pedidos, R$ 23.019 | Antecipação fez 43% do pico |
| Dia do Rock, 13/07 | 1 e-mail: 33 pedidos, R$ 4.490 | 128 pedidos, R$ 21.302 | Seis dias depois do 7.7 e rendeu quase o mesmo |
| 8.8 | 3 e-mails: 88 pedidos, R$ 14.485 | 162 pedidos, R$ 23.824 | 61% |
| 9.9 | 3 e-mails para 80 mil: 83 pedidos, R$ 12.056 | 208 pedidos, R$ 31.314 | 39% |
| Dia do Cliente, 15/09 | 1 e-mail: 15 pedidos, R$ 2.573 | 93 pedidos, R$ 13.153 | Seis dias depois do 9.9. 47% abaixo da média dos outros picos |

O Dia do Rock e o Dia do Cliente vieram seis dias depois de uma data dupla. O primeiro rendeu quase igual ao 7.7, o segundo caiu pela metade. A diferença: o Dia do Rock é uma data do nicho, com oferta concreta e nova (3 camisetas por R$ 169 com frete grátis, "R$ 56 a camiseta"). O Dia do Cliente repetiu a mecânica do 9.9 com outro nome. Isso refina o achado 10: o problema não é o intervalo curto, é o segundo evento sem motivo próprio nem oferta nova.

### 24.4 Ranking por papel na sequência

| Papel | Campanhas | Abertura | Clique | Pedidos | Por mil envios | Índice | Descadastros por pedido |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pico, disparo das 7h | 5 | 26,5% | 0,93% | 277 | R$ 201,3 | 1,78 | 2,6 |
| Pico, disparo das 18h | 5 | 27,2% | 0,97% | 275 | R$ 180,2 | 1,60 | 3,0 |
| Notificação de sistema | 3 | 24,9% | 1,18% | 124 | R$ 151,0 | 1,34 | 4,0 |
| Prova social e UGC | 3 | 23,7% | 0,47% | 110 | R$ 137,5 | 1,22 | 4,2 |
| Pico, disparo das 11h | 5 | 22,5% | 0,81% | 182 | R$ 136,8 | 1,21 | 3,7 |
| Gamificada | 5 | 24,3% | 1,18% | 199 | R$ 126,5 | 1,12 | 4,2 |
| Semana de 15% | 2 | 23,4% | 0,70% | 71 | R$ 96,5 | 0,86 | 4,5 |
| Ressaca e reabertura | 5 | 25,5% | 0,75% | 152 | R$ 91,0 | 0,81 | 6,4 |
| Antecipação | 7 | 19,2% | 0,54% | 214 | R$ 84,2 | 0,75 | 5,0 |
| Lançamento e coleção própria | 4 | 23,5% | 0,53% | 87 | R$ 81,2 | 0,72 | 6,4 |
| Temática do momento | 4 | 20,3% | 0,64% | 110 | R$ 75,7 | 0,67 | 5,5 |
| Catálogo | 2 | 23,2% | 0,72% | 49 | R$ 67,3 | 0,60 | 5,3 |
| Véspera | 4 | 20,1% | 0,59% | 84 | R$ 57,8 | 0,51 | 5,4 |

### 24.5 Melhores e piores

| Melhores | Índice | Por mil envios | Pedidos | Observação |
| --- | --- | --- | --- | --- |
| 07/07 7h, "Seu cupom foi aprovado", texto do Henrique | 3,52 | R$ 397,6 | 89 | Maior abertura do trimestre fora do "status" (34,5%), maior clique (2,07%) e menor custo de lista (1,3 descadastro por pedido) |
| 08/08 18h, "Seu status mudou agora" | 2,45 | R$ 276,1 | 95 | Mesmo modelo que lidera a Blue Wolf, com índice quase idêntico (2,47 lá) |
| 09/09 18h, "Seu status acaba de mudar" | 2,25 | R$ 253,3 | 94 | Terceira vez que o assunto lidera um pico |
| 13/07 7h, "3 camisetas por R$ 169 + FRETE GRÁTIS", texto do Henrique | 1,95 | R$ 220,0 | 49 | Oferta concreta no assunto |
| 09/09 7h, "Seu cupom foi liberado" | 1,91 | R$ 215,9 | 67 | Mesmo modelo de texto que foi o 5º da Blue Wolf |
| 13/07 11h, "R$ 56 a camiseta? Só HOJE no Dia do Rock" | 1,82 | R$ 205,4 | 50 | Preço por unidade no assunto |
| 22/07, Jornal | 1,76 | R$ 199,0 | 48 | Repete o resultado da Blue Wolf (1,65 lá) |
| 29/07, UGC com gancho de Dia dos Pais | 1,60 | R$ 180,5 | 39 | Prova social amarrada a uma data de presente |

| Piores | Índice | Observação |
| --- | --- | --- |
| 08/09, véspera do 9.9, para 80 mil | 0,29 | Abertura de 13,9% |
| 17/09, Semana do Cliente | 0,37 | Extensão de um evento que já tinha ido mal. Igual à VIP Week da Blue Wolf (0,78 lá) |
| 07/09, 7 de Setembro, para 80 mil | 0,39 | Desconto misterioso em data sem ligação com o nicho |
| 15/09 11h, "Será que você foi aprovado?" | 0,40 | Mesmo modelo do teste de visão |
| 14/09, antecipação do Dia do Cliente | 0,46 |  |
| 03/09 e 05/09, esquenta do 9.9, para 80 mil | 0,49 e 0,55 |  |
| 31/08, Catálogo fecha mês | 0,53 | Na Blue Wolf ficou em 1,13 |

### 24.6 Segmento ampliado, terceira confirmação

Cinco envios foram para um segmento maior: 54 mil em 10/07 e cerca de 80 mil no esquenta do 9.9 e no 7 de Setembro, contra 49 mil dos envios normais. As aberturas ficaram entre 11,4 mil e 12,4 mil, a mesma faixa dos envios para 49 mil (10,8 mil a 12,5 mil). Foram cerca de 31 mil contatos a mais por envio em setembro, perto de 140 mil envios extras no total, sem abertura adicional. A taxa caiu de 23% para 14 a 16%. É o mesmo resultado da Blue Wolf, agora em escala maior.

### 24.7 Um cuidado com a atribuição nesta loja

Dois e-mails de texto sem link nenhum (08/07, "Obrigado", e 22/08, antecipação da Oversized) têm zero clique e, mesmo assim, 31 e 16 pedidos atribuídos. A Omnisend atribui pedido a quem abriu o e-mail, não só a quem clicou. Numa loja com muito tráfego próprio e oferta de kit sempre ativa, parte da receita atribuída às campanhas viria de qualquer jeito. Consequências para o estudo:

- O índice continua válido para comparar campanhas da mesma loja, porque o viés é igual para todas.
- A métrica "clique em pedido" não serve nesta loja.
- Prova social aparece bem aqui (índice 1,22) com o menor clique da conta (0,47%). Pode ser efeito de atribuição por abertura. O achado 9 fica como divergente até ter mais lojas.
- Vale conferir a janela de atribuição configurada em cada conta antes do consolidado.

### 24.8 O que esta loja muda no painel de achados

| # | Achado | Clube Rock | Situação agora |
| --- | --- | --- | --- |
| 1 | Automações fazem perto de 78% da receita de e-mail | 74% | Repetiu em 3 de 3 |
| 2 | Antecipação sem cupom vende | 39% a 61% do pico | Repetiu em 3 de 3 |
| 3 | Disparo das 18h é o melhor do pico | É o segundo. O das 7h, em texto do fundador, é o primeiro | Ajustado: 7h em texto e 18h com "status" são os dois disparos fortes. O das 11h tem o menor índice agregado dos três nesta loja (1,21) |
| 4 | Assunto de notificação pessoal lidera | "Status mudou" com índices 2,45 e 2,25 | Repetiu em 3 de 3. Passa de 100 pedidos só nesta loja (189) |
| 5 | Ampliar o envio não traz abertura | 31 mil contatos a mais, zero abertura a mais | Repetiu em 3 de 3 |
| 9 | Prova social é o pior formato | Índice 1,22 | Divergiu. Ver 24.7 |
| 10 | Dois eventos em menos de 7 dias derrubam o segundo | Dia do Cliente 47% abaixo. Dia do Rock não caiu | Refinado: cai quando o segundo evento não tem motivo nem oferta próprios |
| 13 | Ressaca vende | Índice 0,81. A do 9.9 ficou em 0,61 | Divergiu de novo. Na Blue Wolf a mesma ressaca teve 1,78 |
| 15, novo | Texto puro do fundador às 7h | Índice 3,52, 1,95 e 1,91, com o menor custo de lista da conta | Na Blue Wolf o mesmo modelo teve 1,66 no 9.9 e abaixo de 1 nos outros. Funciona melhor com remetente pessoal ("Henrique da Clube Rock") e oferta concreta no assunto |
| 16, novo | Data do nicho com oferta concreta rende como data dupla | Dia do Rock: R$ 21,3 mil em um dia | Cada cliente deve ter sua data própria mapeada para o quarto trimestre |
| 17, novo | Lançamento e coleção própria rendem abaixo da média | Índice 0,72 | Lançamento sozinho não substitui oferta. Combinar com preço de abertura e prazo |

### 24.9 Pontos positivos e gargalos

| Pontos positivos | Evidência |
| --- | --- |
| Fluxo de boas-vindas muito forte | R$ 368 mil e 2.751 pedidos em três meses |
| Texto do fundador com remetente pessoal | Os três melhores disparos das 7h |
| Data própria do nicho bem explorada | Dia do Rock com três disparos e oferta de kit |
| Reputação estável com volume alto | 2,5 milhões de envios com spam de 0,015% |

| Gargalo | Evidência | O que fazer |
| --- | --- | --- |
| Segmento de 80 mil | Perto de 140 mil envios extras sem abertura | Tirar do envio comum. Testar só na oferta máxima da BF |
| Clique muito baixo | 0,75% por envio, contra 1,84% na Blue Wolf | Conferir o link de destino e a primeira tela dos e-mails de imagem, quando as prints chegarem |
| Rendimento caindo mês a mês | Índice de 1,24 em julho para 0,77 em setembro | Menos eventos genéricos, mais datas do nicho |
| Régua de logística rende pouco | Rastreio e pedido confirmado somam R$ 42 mil, 5% das automações. Na Blue Wolf são 14% | Levar a oferta da régua da Blue Wolf para cá |
| Disparo das 11h | Menor índice agregado dos três (1,21). Foi o pior do dia no 9.9 e no Dia do Cliente | Testar texto curto ou formato emprestado nesse horário |
| Sem SMS, push ou WhatsApp | Só e-mail em uma lista brasileira de 50 mil | WhatsApp é o canal natural para o Brasil na BF |

## 25. Consolidado de três lojas: o que já dá para decidir

Com três lojas analisadas, a base consolidada tem 101 envios e 2.339 pedidos de campanha (Blue Wolf e Clube Rock; a Emyerre entra só no painel de achados). Dez modelos foram bem nas duas lojas grandes e catorze foram mal nas duas. Entre esses extremos, o resultado de um modelo em uma loja prevê pouco o resultado na outra (correlação de 0,25). A decisão da Black Friday deve se apoiar nos modelos dos dois extremos e tratar o meio como teste. \[D, base consolidada de 20/09/2026\]

### 25.1 O mesmo modelo em duas lojas

Blue Wolf e Clube Rock rodaram 45 modelos em comum, na mesma data, um em inglês e outro em português. O índice é a receita por mil envios da campanha dividida pela média da própria loja. A Emyerre ficou fora desta tabela: a lista dela (1.096 contatos) é pequena demais para o índice ser estável.

**Foram bem nas duas lojas (índice acima de 1 nas duas)**

| Data | Modelo | Blue Wolf | Clube Rock | Média | Pedidos somados |
| --- | --- | --- | --- | --- | --- |
| 08/08 18h | 8.8, disparo 3, "status mudou", conversa simulada | 2,47 | 2,45 | 2,46 | 113 |
| 09/09 18h | 9.9, disparo 3, "status mudou", jornal | 1,41 | 2,25 | 1,83 | 109 |
| 09/09 7h | 9.9, disparo 1, "cupom liberado", texto do fundador | 1,66 | 1,91 | 1,79 | 80 |
| 22/07 | Jornal, 48h para o fim | 1,65 | 1,76 | 1,71 | 63 |
| 03/07 | Antecipação 7.7, agenda e FAQ | 1,93 | 1,03 | 1,48 | 44 |
| 20/07 | Revele seu desconto | 1,57 | 1,22 | 1,39 | 57 |
| 17/06 | Semana Copa, cartão vermelho | 1,51 | 1,18 | 1,35 | 42 |
| 31/07 | Sexta premiada | 1,15 | 1,42 | 1,28 | 60 |
| 07/07 11h | 7.7, disparo 2, role até o fim | 1,24 | 1,17 | 1,20 | 43 |
| 24/08 | Semana de 15%, On & Off | 1,08 | 1,06 | 1,07 | 48 |

**Foram mal nas duas lojas (índice abaixo de 1 nas duas)**

| Data | Modelo | Blue Wolf | Clube Rock | Média |
| --- | --- | --- | --- | --- |
| 08/09 | Esquenta 9.9, véspera, segmento ampliado | 0,44 | 0,29 | 0,37 |
| 26/08 | Semana de 15%, Escolha o caminho | 0,29 | 0,65 | 0,47 |
| 03/09 | Esquenta 9.9, "Enc: você não deveria saber", segmento ampliado | 0,51 | 0,49 | 0,50 |
| 03/08 | Esquenta 8.8, warm-up | 0,11 | 0,94 | 0,52 |
| 14/09 | Antecipação do VIP Day e do Dia do Cliente | 0,60 | 0,46 | 0,53 |
| 17/09 | VIP Week e Semana do Cliente | 0,78 | 0,37 | 0,57 |
| 27/07 | Segunda da sorte | 0,40 | 0,82 | 0,61 |
| 21/08 | Catálogo indecisão | 0,55 | 0,67 | 0,61 |
| 05/09 | Esquenta 9.9, calendário, segmento ampliado | 0,77 | 0,55 | 0,66 |
| 15/09 18h | VIP Day e Dia do Cliente, prêmio reservado | 0,45 | 0,98 | 0,71 |
| 19/08 | UGC Dia da Fotografia | 0,57 | 0,89 | 0,73 |
| 11/08 | Ressaca 8.8 | 0,93 | 0,59 | 0,76 |
| 15/09 7h | VIP Day e Dia do Cliente, disparo 1 | 0,74 | 0,95 | 0,85 |
| 14/08 | Sextou | 0,80 | 0,93 | 0,86 |

**Divergiram: bem em uma loja, mal na outra (21 modelos). Os casos que mais ensinam:**

| Data | Modelo | Blue Wolf | Clube Rock | Leitura |
| --- | --- | --- | --- | --- |
| 07/07 7h | 7.7, disparo 1, texto "cupom aprovado" | 0,56 | 3,52 | Na Clube Rock saiu com remetente pessoal ("Henrique da Clube Rock"). Na Blue Wolf o remetente era o nome da loja. Falta ler o texto dos dois para comparar |
| 07/07 18h | 7.7, disparo 3, última chamada | 2,42 | 0,90 | Na Clube Rock o disparo das 7h já tinha levado a maior parte da demanda do dia |
| 11/09 | Ressaca 9.9, aviso de estoque | 1,78 | 0,61 | Ressaca segue sem padrão entre lojas |
| 29/07 | Prova social | 0,77 | 1,60 | Na Clube Rock veio com gancho de Dia dos Pais. Pode haver efeito de atribuição por abertura (seção 24.7) |
| 28/08 | Notificação do futuro | 0,90 | 1,43 | Maior clique da Blue Wolf, mas receita só na Clube Rock |
| 31/08 | Catálogo fecha mês | 1,13 | 0,53 |  |
| 15/07 | Favoritos do evento | 1,64 | 0,89 | Eventos diferentes: 7.7 em uma, Dia do Rock na outra |

Dos 45 modelos, 24 caíram do mesmo lado nas duas lojas. É pouco acima do acaso no miolo da tabela, e muito consistente nas pontas. Com mais lojas, o miolo tende a se definir.

### 25.2 Painel de achados, versão com três lojas

| # | Achado | Emyerre | Blue Wolf | Clube Rock | Situação |
| --- | --- | --- | --- | --- | --- |
| 1 | Automações fazem de 74% a 78% da receita de e-mail | 78% | 77% | 74% | Repetiu em 3 de 3 |
| 2 | Antecipação sem cupom vende | Sim | 46% a 108% do pico | 39% a 61% do pico | Repetiu em 3 de 3 |
| 3 | Os disparos fortes do pico são o das 18h com assunto de status e o das 7h em texto | 18h | 18h em 3 de 4 | 7h e 18h | Repetiu em 3 de 3, ajustado |
| 4 | "Seu status mudou" lidera | 63% e 49% de abertura | Índice 2,47 e 1,41 | Índice 2,45 e 2,25 | Repetiu em 3 de 3. Passa de 100 pedidos |
| 5 | Ampliar o envio para quem não engaja não traz abertura | Importação de 424 | Segmento de 22 mil | Segmento de 80 mil | Repetiu em 3 de 3 |
| 6 | Oferta na primeira tela dobra o clique | Não medido | Sim | Aguardando prints | 1 de 1 |
| 7 | Mesma oferta em formato novo vende de novo | Não medido | 44 pedidos em 3 envios | Revele, Jornal e Ligação: 111 pedidos | Repetiu em 2 de 2 |
| 8 | Altura do e-mail não explica resultado | Não medido | r = -0,02 | Aguardando prints | 1 de 1 |
| 9 | Prova social é o pior formato | Não medido | Sim | Não, índice 1,22 | Divergiu |
| 10 | Segundo evento colado no primeiro cai, se não tiver motivo e oferta próprios | Não medido | VIP Day 35% abaixo | Dia do Cliente 47% abaixo. Dia do Rock não caiu | Repetiu em 2 de 2, refinado |
| 11 | Régua de logística com oferta paga | Não tem | 14% das automações | 5% das automações | Oportunidade |
| 12 | Todo clique vai para a página inicial | Não verificado | Sim | A verificar | Pendente |
| 13 | Ressaca vende | Não | Sim | Não | Sem padrão |
| 14 | Viewed Product vende | Não | 100 pedidos | 262 pedidos | Vende quando há volume |
| 15 | Texto puro do fundador às 7h | Não medido | Índice 1,66 no 9.9 | Índice 3,52, 1,95 e 1,91 | Repetiu em 2 de 2, mais forte com remetente pessoal |
| 16 | Data do nicho com oferta concreta rende como data dupla | Não medido | Não tem | Dia do Rock: R$ 21,3 mil | 1 de 1 |
| 17 | Rendimento por envio cai de julho a setembro | Não medido | 1,29, 0,90, 0,84 | 1,24, 0,99, 0,77 | Repetiu em 2 de 2 |
| 18 | Modelos de conceito sem oferta ficam abaixo da média | Não medido | Sim | Sim | Repetiu em 2 de 2: Escolha o caminho, Catálogo indecisão, Segunda da sorte, Sextou |

### 25.3 O que isso já define para a Black Friday

| Decisão | Base |
| --- | --- |
| Disparo das 7h em texto do fundador, com remetente pessoal, cupom e oferta concreta no assunto | Achado 15. Três dos cinco melhores e-mails da Clube Rock |
| Disparo das 18h com assunto de status e formato emprestado (conversa ou jornal) | Achados 3 e 4. Melhor modelo das duas lojas grandes, índice 2,46 |
| Disparo do meio do dia é o lugar do teste | É o mais fraco e o que mais varia |
| Antecipação no molde do 7.7: convite, agenda, FAQ, barra de status | Achado 2 e modelo de 03/07, acima de 1 nas duas lojas |
| Mesma oferta reapresentada em formatos diferentes ao longo da semana | Achado 7. Substitui o reenvio simples |
| Nada de segmento ampliado no aquecimento | Achado 5, três lojas |
| Não criar evento genérico colado na BF ou no 11.11 | Achado 10. VIP Day, Dia do Cliente e as extensões de semana foram mal nas duas lojas |
| Mapear a data própria de cada cliente no quarto trimestre | Achado 16 |
| Tirar do calendário de novembro: e-mails de conceito sem oferta, catálogo de indecisão, "escolha o caminho" | Achado 18 |
| Revisar fluxos antes de escalar campanhas, e levar oferta para a régua de logística | Achados 1 e 11 |
| Ressaca e prova social: manter como teste, sem contar com a receita | Achados 9 e 13 |

### 25.4 Pendências em 20/09/2026

| Pendência | Depende de |
| --- | --- |
| Clube Rock: prints do Figma, fichas com imagem, automações por mensagem, receita total da loja, texto dos e-mails do Henrique | Prints do Bruno e 4 a 6 consultas |
| Emyerre: converter para o molde da seção 20 e incluir na base | Prints e reprocessamento da seção 17 |
| Blue Wolf: automações por mensagem, receita total, texto dos outros 5 e-mails de texto | 4 a 7 consultas |
| Janela e regra de atribuição de cada conta | Conferir na Omnisend |
| Novembro de 2025 | Conectar lojas que já eram clientes na última BF. As três atuais são de 2026 |
| Próximas 12 lojas, com a variedade da seção 22.9 | Bruno |
| Itens da seção 23.5 que seguem abertos | Endereço de resposta de 06/07, números de prova nos e-mails, origem dos 424 contatos da Emyerre |
| Entregas finais | Mapa mental, skills de planejamento e de copy, planilha de classificação, calendário até março de 2027 |
