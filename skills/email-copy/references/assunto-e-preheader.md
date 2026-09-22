# Assunto e preheader

Detalhe das regras C40 e C41. Carregado sob demanda pela `email-copy`.

## Veredito da evidência para o assunto: REFINADA

`docs/pesquisa/evidencias-publicadas.md`, linha "Assunto curto (≤25 a 40
caracteres)": força **moderada**, veredito **REFINADA**. A formulação
exata do relatório: *"benchmarks de ESP recomendam assuntos curtos (faixa
frequentemente citada de ~30 a 50 caracteres, ou ~6 a 10 palavras) por
truncamento em mobile. A regra da skill de ≤25 a 40 caracteres é agressiva
mas defensável para mobile."*

Traduzindo para o que a skill pode afirmar:

| Pode afirmar | Não pode afirmar |
|---|---|
| Assunto longo trunca em celular, e o que trunca não é lido | "Assunto com até 25 caracteres converte mais" |
| A oferta deve caber na parte que não trunca | Um número exato como se fosse lei |
| O limite ótimo desta loja sai de teste | Que o limite ótimo é o mesmo em todas as lojas |

O `email-marketing-bible` afirma "abaixo de ~25 caracteres abre mais" sem
fonte primária. É **direcional** e está na lista de quarentena em
`docs/destilacao/matriz.md`.

Além disso: **abertura é métrica ruim.** MPP pré-carrega pixel e os
resumidores de IA abrem a mensagem sozinhos. Otimizar assunto por abertura
mede cada vez menos. Quando testar assunto, olhe clique e receita por
destinatário junto.

## Como o Omnisend trata o campo

- `post_campaigns` exige `subject`, `senderName` e `templateID`. O
  `preheader` é **opcional** na API.
- Não há limite documentado de caracteres para assunto ou preheader na
  referência oficial consultada. A afirmação de "até 250 caracteres" que
  circulava foi removida da nossa pesquisa por não ser verificável.
- O limite prático é muito menor que qualquer limite técnico, e vem de
  truncamento em celular, não da API.
- O Omnisend tem A/B nativo com `winningMetric` por `openRate` ou
  `clickRate`, mais seleção automática ou manual de vencedor. É o caminho
  para descobrir o limite de cada base.

## Receita do assunto

Ordem dos elementos, do mais para o menos importante:

1. **Mecânica ou valor da oferta.** O que a pessoa ganha e como.
2. **Prazo,** se houver e se couber.
3. **Produto ou categoria,** se a oferta não for do site inteiro.
4. **Tom da marca,** se ainda sobrar espaço. Geralmente não sobra, e
   tudo bem: no corpus da Anthropologie o tom aparece em cerca de 1 de
   cada 5 assuntos.

Alvo ≤ 40 caracteres, meta ≤ 25. Ultrapassar 40 é achado A no lint, não
bloqueio: um assunto de 44 caracteres que carrega a oferta inteira vence um
de 23 que não carrega nada.

### Assuntos observados no mercado, que a skill pode imitar em forma

De marcas reais, para mostrar a forma. Não são modelos de copiar literal.

- "Combine e ganhe 1 best-seller" (Insider): mecânica, sem adjetivo.
- "Frete grátis e 1 item de brinde nessa combinação." (Insider): dois
  benefícios concretos.
- "Último dia para combinar e ganhar com frete grátis" (Insider): prazo
  mais mecânica.
- "20% Off Sitewide Is Live" (True Classic): valor mais escopo.
- "Extra 40% Off Sale is LIVE" (Anthropologie): valor mais estado.
- "24hrs early: extra 50% off sale" (Anthropologie): prazo mais valor.

O que todos têm em comum: **número no começo, adjetivo em lugar nenhum.**

### Anti-padrão de mercado que a skill nunca reproduz

Uma loja brasileira de suplementos na base Trendtrack manda campanha
promocional disfarçada de transacional: "Resposta: Seu pedido foi
aprovado", "(RE): confirmação do seu pedido", "Aviso: Seu novo pedido está
confirmado". Isso é C03 e bloqueia.

Não é vício de IA: é vício de desespero. Mas a IA reproduz na hora em que
alguém pede "aumente a abertura". Gera reclamação de spam, que é o que de
fato move o filtro, e é risco regulatório: CAN-SPAM proíbe assunto
enganoso, e o CDC art. 37 trata publicidade enganosa.

## Receita do preheader

O preheader é a **segunda informação**, nunca a repetição da primeira.

| Se o assunto traz | O preheader traz |
|---|---|
| O valor ("30% OFF") | A condição ou o prazo ("acima de R$150, até domingo") |
| A mecânica ("Combine e ganhe") | O produto ou a categoria |
| O produto | O valor ou a condição |
| Curiosidade curta | O fato que resolve a curiosidade |

Checagens do lint:

- Similaridade Jaccard com o assunto acima de 0,6 é achado A.
- Preheader ausente é achado A.
- Travessão no preheader bloqueia (C01).

### Preheader e o resumidor de IA

O Gemini no Gmail e o Apple Intelligence resumem a partir de **texto vivo**,
com peso alto em assunto e preheader. Um e-mail quase todo em imagem dá
pouco texto ao resumo.

O que a Insider faz, e que a skill não faz: preencher o restante do
preheader com caracteres invisíveis para empurrar o texto do corpo para
fora do preview. A prática esconde o que viria depois, e o que viria depois
é justamente o que o resumidor e o leitor de tela leem.

Recomendação prática, que serve a quatro coisas ao mesmo tempo (resumidor,
acessibilidade, dark mode e clipping):

1. Preheader específico com a oferta em texto.
2. Primeira seção do HTML em texto vivo, com proposta e condição.
3. Alt descritivo em cada imagem-chave.

Força da evidência sobre o impacto dos resumidores em abertura e clique:
**moderada, sem dado público de impacto**. O item está na lista de lacunas
que exigem teste interno. A recomendação vale de qualquer forma, porque as
outras três razões (acessibilidade, dark mode, clipping) têm evidência
forte por conta própria.

## Checklist do par

- [ ] Assunto começa por número, valor ou mecânica
- [ ] Assunto ≤ 40 caracteres, idealmente ≤ 25
- [ ] Assunto não simula transação, resposta ou aviso de pedido
- [ ] Assunto sem superlativo vazio
- [ ] Zero a um emoji, e só se a ficha da marca usa
- [ ] Preheader existe
- [ ] Preheader não repete o assunto
- [ ] Preheader carrega condição, prazo ou produto
- [ ] Nenhum travessão nos dois campos
- [ ] Nenhum caractere invisível de preenchimento
- [ ] O cupom, se citado, está no idioma da loja
