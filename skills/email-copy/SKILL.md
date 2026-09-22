---
name: email-copy
description: Use ao escrever ou reescrever assunto, preheader, headline, corpo, CTA ou texto de alt de um e-mail de e-commerce; ao decidir o tamanho da copy por tipo de e-mail; ao redigir a condição de uma oferta com cupom, prazo ou valor mínimo; ou quando uma copy pronta precisa passar pelo gate anti-vício antes de ir para o cliente. Não cobre estrutura da peça (isso é o vault), HTML (isso é email-design) nem a lógica do flow (isso é email-flows).
---

# email-copy

Escreve os campos de texto de um e-mail de e-commerce de forma que um
humano da Convertfy aprove sem perceber que foi gerado.

Esta skill **usa** as regras anti-vício, não as reescreve. A lista de
vícios, os exemplos de ruim e bom, e os limiares de detecção estão em
`shared/anti-vicios-copy.md`. Leia lá antes de escrever qualquer campo. A
verificação determinística é `scripts/lint_copy.py`, e a entrega é
bloqueada por qualquer achado de severidade B.

Divergências desta skill em relação ao CLAUDE.md: nenhuma.


## Protocolo obrigatório

Esta skill segue `shared/protocolo-de-execucao.md` inteiro. Em resumo:

1. **Ficha e brief (P01, P02).** Le `marcas/<cliente>.md` quando existir.
   Sem ficha e sem brief com **oferta, produto e prazo**, não gera: pede o
   que falta. Campo ausente vira `[FALTA: <campo>]`, nunca invencao.
2. **Anti-vícios.** Aplica `shared/anti-vicios-copy.md`,
   `anti-vicios-design.md`, `anti-vicios-processo.md` e, junto,
   `shared/calibracao.md`, para não reprovar convenção legitima de e-mail.
3. **Gate de lint.** Roda `scripts/lint_copy.py` e `scripts/lint_email.py`
   antes de entregar. **Violacao B: não entrega.** O gate e o exit code.
4. **Leitura do brief.** Antes de gerar, uma linha dizendo o que entendeu.
   Se estiver ambíguo, **uma pergunta só**, juntando tudo que falta.
5. **Só o artefato (C07).** Sem comentario sobre a própria copy, sem
   explicar a escolha, sem variacao que ninguem pediu.
6. **Ordem de trabalho (P08).** intencao (var1) -> estrutura (var2) ->
   variantes do arsenal -> copy por schema. Nunca escreve antes de
   decidir a estrutura.

## Ordem de trabalho

1. **Ler o brief da loja** em `marcas/<cliente>.md`. Sem brief com oferta,
   produto e prazo, não escreva: pergunte. Gerar sem brief é P01.
2. **Ler a intenção do toque** no vault, em `intencoes/<flow>/<n>.md`.
   Ela diz qual objeção este e-mail ataca. A copy responde à objeção, não
   ao tema.
3. **Ler a estrutura** escolhida (`estruturas/<flow>/<slug>.md`) e o
   `schema_campos` de cada variante. A copy é escrita **dentro** do schema
   da variante, campo por campo. Nunca escreva prosa solta e depois tente
   encaixar: isso é P08.
4. **Escrever por campo**, respeitando o orçamento de palavras do tipo.
5. **Rodar `scripts/lint_copy.py`.** Corrigir todo B e todo A.
6. **Entregar só os campos.** Nenhum comentário sobre a própria copy
   (C07), nenhuma explicação de por que funciona.

## As quatro regras que bloqueiam sozinhas

Resumo operacional. A lista completa está em `shared/anti-vicios-copy.md`.

1. **Travessão é proibido** em qualquer campo, inclusive assunto,
   preheader, alt e texto de botão. Use vírgula, ponto, dois pontos ou
   parênteses. É o primeiro item de toda eval.
2. **Número sem origem no brief é proibido.** Contagem de clientes,
   avaliação, estoque, percentual: se não está no brief, não existe. Se o
   campo exige um número que você não tem, escreva `[FALTA: número de
   avaliações]` e pare. Inventar é P02, e a evidência de risco legal aqui
   é forte (CDC art. 37 e CAN-SPAM).
3. **Assunto não simula transação.** Nada de "RE:", "Seu pedido foi
   aprovado", "Aviso:". Assunto enganoso é proibido por CAN-SPAM e tratado
   como publicidade enganosa pelo CDC.
4. **Cupom no idioma da loja.** `PEDIDO18` em loja inglesa é bloqueio.

## Orçamento de palavras por tipo

Esta é a regra C45. **Veredito da evidência: REFINADA, depende do tipo.**
A evidência pública sobre "copy curta vence" é fraca a moderada e não vale
igual para todo e-mail: oferta direta vence em promocional e carrinho,
enquanto welcome e peça de marca toleram mais texto. O que sustenta os
números abaixo é o corpus interno, não a literatura.

| Tipo de e-mail | Orçamento do corpo | Base |
|---|---|---|
| Welcome | ≤ 80 palavras | Corpus de 35 welcomes: mediana de 3 palavras por bloco, 77% dos blocos com ≤5 palavras |
| Campanha promocional | ≤ 80 palavras | Insider (BR): corpo médio de ~605 caracteres, cerca de 100 palavras com rodapé legal |
| Carrinho e checkout abandonados | ≤ 60 palavras | Intenção já existe: lembrar custa menos palavra que convencer |
| Editorial ou carta, **explicitamente pedida no brief** | Sem teto fixo | Exceção declarada. Se o brief não pediu, não é exceção |

Contagem: **fora de nomes de produto**. Nome de produto, preço e código de
cupom não consomem orçamento.

O que fazer quando não cabe: cortar, não encolher. Se a copy só cabe
reduzindo o corpo para 12px, o problema é a copy, não o tamanho da fonte.

Detalhe, curva de tamanho ao longo de uma sequência e como contar:
`references/orcamento-de-palavras.md`.

## Assunto (C40)

**Veredito da evidência: REFINADA.** Assunto curto é recomendação
sustentada por truncamento em celular, e isso é real. O **limite numérico
exato não é lei**: os benchmarks de ESP citam faixas que variam de ~25 a
~50 caracteres, com metodologias diferentes, e nenhum deles é um teste
limpo na base da Convertfy.

Como escrever, na ordem:

1. **Mecânica da oferta primeiro.** "R$30 OFF acima de R$100 até domingo"
   antes de qualquer adjetivo. O corpus de mercado confirma: Insider,
   True Classic e Anthropologie colocam número e prazo no começo.
2. **Alvo ≤ 40 caracteres, meta ≤ 25.** Trate como alvo de escrita, não
   como aprovação. Um assunto de 43 caracteres que diz a oferta inteira
   vence um de 24 que não diz nada.
3. **Sem adjetivo de intensidade.** Sem "imperdível", "incrível",
   "histórico".
4. **Zero a um emoji**, e só quando a ficha da marca já usa.
5. **Nunca simular transação** (C03).

Honestidade obrigatória ao entregar: quando o cliente perguntar qual é o
tamanho certo, a resposta é *"curto, e o número exato sai do A/B da sua
base"*, não *"25 caracteres convertem mais"*. O Omnisend tem A/B nativo com
`winningMetric` por taxa de abertura ou de clique; é ali que o limite
desta loja se descobre.

## Preheader (C41)

O preheader **completa** o assunto. Nunca repete e nunca fica vazio.

- Se o assunto traz o valor, o preheader traz a condição ou o prazo.
- Se o assunto traz a mecânica, o preheader traz o produto.
- Similaridade com o assunto acima de 0,6 (Jaccard) é achado de
  severidade A no lint.
- Preheader vazio preenchido com caracteres invisíveis é o que a Insider
  faz e é anti-padrão: o resumidor do Gmail e do Apple lê essa primeira
  linha viva, e um leitor de tela também.

Detalhe e exemplos de par assunto mais preheader:
`references/assunto-e-preheader.md`.

## Condição da oferta (C46)

Se há desconto, a copy carrega a condição **completa**. Faltar condição é
achado de severidade A.

A condição tem três partes obrigatórias e uma condicional:

| Parte | Obrigatória? | Forma aceita |
|---|---|---|
| Valor | Sim | "15% OFF", "R$30 OFF" |
| Como aplicar | Sim | Código visível **ou** a frase "aplicado no carrinho" |
| Prazo | Sim | Data real **ou** a frase "por tempo limitado" |
| Mínimo | Só se existir | "acima de R$100" |

Regras de forma:

- **O código é do idioma da loja** (C04).
- **O prazo é real.** "Últimas unidades" sem dado de estoque é C06.
  "Por tempo limitado" é aceitável justamente porque não afirma um prazo
  que não existe.
- **Mínimo omitido quando não existe.** Não invente piso de pedido.
- **No Omnisend, o código não é texto.** O bloco de desconto emite um
  código único por destinatário e o placeholder é `XXXX-XXXX-XXXX`. Escrever
  "use o código BEMVINDO15" cria uma promessa que a loja não emitiu.
  A copy escreve a condição; o código nasce no bloco. Ver
  `skills/email-flows/`.

Detalhe, formas aceitas em pt-BR e em inglês, e o que fazer quando o brief
só deu metade da condição: `references/oferta-e-condicao.md`.

## CTA (C43, C44)

- **Verbo de compra mais objeto.** "Comprar com 10% OFF", "Ver a coleção",
  "Resgatar o cupom". O corpus humano de 64 CTAs é dominado por shop,
  claim e explore: CTA humano não é criativo.
- **Duas a quatro palavras.**
- **Uma ação principal por e-mail.** Repetir o mesmo botão duas ou três
  vezes com o **mesmo destino** é permitido e comum. O que não é permitido
  é dois CTAs principais com destinos diferentes.
- **Caixa alta em botão não é vício.** É convenção de e-mail. Ver §8 da
  pesquisa.

## Alt de imagem

O alt é campo de copy, não sobra técnica.

- Imagem que carrega sentido recebe **alt descritivo que inclui a oferta**.
- Imagem puramente decorativa recebe `alt=""`, para o leitor de tela
  pular.
- Imagem **sem atributo alt** é o pior caso: alguns leitores de tela leem
  o nome do arquivo.
- O alt também é copy para o lint: travessão no alt bloqueia igual.

## Personalização (C47)

Toda merge tag exige fallback, e a frase precisa funcionar sem o nome.

- Omnisend usa `[[contact.first_name]]`. O comportamento de valor ausente
  precisa ser confirmado no painel antes de virar regra desta skill: ver
  o TODO em `skills/email-flows/references/equivalencia-klaviyo-omnisend.md`.
- Regra que vale já: **escreva a frase de modo que ela leia bem com o
  campo vazio.** "Oi [[contact.first_name]], seu cupom" continua lendo se
  o nome sumir; "Preparamos isso especialmente para [[contact.first_name]]"
  não.
- Personalização por nome no assunto tem efeito pequeno e às vezes
  negativo na literatura. Não é alavanca: é higiene.

## O que esta skill nunca faz

- Não inventa número, depoimento, estoque ou prazo.
- Não escreve cena, hora, data fabricada ou personagem (C05).
- Não faz tríade ornamental nem antítese "não é X, é Y".
- Não escreve Title Case em pt-BR (C34). Caixa de frase ou caixa alta
  total.
- Não usa travessão, nem mesmo quando a frase pede uma pausa longa.
- Não comenta a própria copy na entrega.
- Não escolhe a estrutura da peça. Isso vem do vault.

## Gate de entrega

A copy só sai quando:

- [ ] `scripts/lint_copy.py` roda sem nenhum achado B
- [ ] Todo achado A foi corrigido ou tem justificativa escrita
- [ ] Todo número na peça existe no brief
- [ ] A condição da oferta está completa (valor, como aplicar, prazo, e
      mínimo se houver)
- [ ] Assunto e preheader não se repetem
- [ ] Existe pelo menos uma linha de texto vivo com a oferta, fora de
      imagem (C42)
- [ ] O orçamento de palavras do tipo foi respeitado, ou a exceção
      editorial está declarada no brief
- [ ] Nenhum placeholder `[FALTA: ...]` sobrou sem virar pergunta ao
      cliente


## Não verificado no Omnisend

Quatro comportamentos do Omnisend **não foram verificados em conta real**.
Até que sejam, valem os fallbacks abaixo, e o código nunca afirma que a
checagem passou.

| Item | Pergunta aberta | Fallback obrigatório |
|---|---|---|
| **T1** | Existe valor padrão para merge tag de contato vazia? | A frase precisa ler bem **com o campo vazio**. Prefira o nome no fim da frase, ou não use nome. Nunca entregue `Oi , tudo bem?` |
| **T3** | Propriedade de evento serve como merge tag em bloco de texto? | **Não cite o produto no texto.** Headline genérica ("Você deixou algo para tras"), e o bloco de produto faz o trabalho |
| **T4** | Qual a tag do link de recuperacao de carrinho na origem `shopify`? | **O link e sempre testado com clique antes do envio**, e o carrinho precisa abrir com o item dentro. Na dúvida, página da coleção, que converte menos e nunca abre carrinho vazio |
| **T5** | Qual a tag do link de retomada de checkout na origem `shopify`? | Igual ao T4: clique de teste obrigatório, e o checkout precisa reabrir com itens e e-mail preenchidos |

Nunca invente nome de variavel para fechar um destes. Nome de tag que
não resolve entrega e-mail com colchete cru para o cliente final.

Para fechar: `docs/omnisend/roteiro-de-teste.md` (cinco envios para um
e-mail seed). Registro em `docs/omnisend/verificado.md`. O que o teste
não responder vira chamado, com o texto pronto em
`docs/omnisend/perguntas-suporte.md`.

## Referências

| Arquivo | Quando abrir |
|---|---|
| `shared/anti-vicios-copy.md` | Sempre, antes de escrever |
| `references/orcamento-de-palavras.md` | Ao decidir tamanho por tipo e por posição na sequência |
| `references/assunto-e-preheader.md` | Ao escrever o par assunto mais preheader |
| `references/oferta-e-condicao.md` | Ao redigir desconto, cupom, prazo ou mínimo |
| `docs/pesquisa/evidencias-publicadas.md` | Quando alguém perguntar "por que essa regra?" |
