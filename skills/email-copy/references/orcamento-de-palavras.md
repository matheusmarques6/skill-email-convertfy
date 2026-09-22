# Orçamento de palavras por tipo de e-mail

Detalhe da regra C45. Carregado sob demanda pela `email-copy`.

## Veredito da evidência: REFINADA

Registrado aqui porque a skill precisa ser honesta sobre o que sustenta o
número.

`docs/pesquisa/evidencias-publicadas.md`, linha "Corpo curto por tipo de
e-mail": força **fraca a moderada**, veredito **REFINADA**. A literatura
não sustenta "copy curta sempre vence". O que ela sustenta é mais estreito:
oferta direta vence em promocional e em carrinho, enquanto welcome e peça
de marca toleram mais texto.

Logo, os tetos abaixo **não vêm da literatura**. Vêm de duas fontes
internas, ambas de alta confiabilidade como observação:

- **Corpus humano de 35 welcomes reais** (Figma, 607 blocos, 3.065
  palavras): média de 5,0 palavras por bloco, mediana 3, 77% dos blocos com
  5 palavras ou menos, e apenas 2,3% dos blocos acima de 20 palavras.
- **Mercado brasileiro de alto volume** (Trendtrack, 90 dias): Insider com
  corpo médio de 605 caracteres, cerca de 100 palavras contando rodapé
  legal. True Classic (EUA) com 935 caracteres.

E de uma rejeição interna registrada: na sequência da Vivazz (jun/2026) a
curva aceita foi de ~150 para 140 e depois 85 palavras ao longo da semana.

Consequência prática: **o teto é um alvo de escrita, auditável, não uma lei
de conversão.** Se um A/B interno da Convertfy mostrar que um welcome de
120 palavras converte melhor numa base específica, o teto sobe para aquela
loja e a exceção é registrada no `marcas/<cliente>.md`.

## Os tetos

| Tipo | Teto do corpo | Observação |
|---|---|---|
| Welcome, e-mail 1 | 80 palavras | O e-mail 1 entrega o incentivo prometido. Quanto antes a condição aparecer, menos palavra sobra |
| Welcome, e-mails seguintes | 80 palavras | Mesmo teto. Não há razão para crescer |
| Campanha promocional | 80 palavras | Peso vai para assunto, preheader e imagem |
| Carrinho abandonado | 60 palavras | A intenção já existe. Lembrar custa menos que convencer |
| Checkout abandonado | 60 palavras | Intenção ainda maior. O e-mail é quase só o link de retomada mais a condição |
| Navegação abandonada | 60 palavras | Mesmo teto do carrinho |
| Pós-compra, agradecimento | 60 palavras | Sem venda no primeiro toque |
| Pós-compra, instrução de uso | 80 palavras | Único caso em que explicar é o trabalho |
| Winback | 60 palavras | Reconhecer o intervalo custa uma linha, não um parágrafo |
| Sunset | 40 palavras | Uma pergunta e dois botões |
| Reposição | 60 palavras | Recompra é atrito, não argumento |
| Pedido de avaliação | 40 palavras | Um pedido, um link |
| Editorial ou carta, pedida no brief | sem teto | Exceção. Precisa estar escrita no brief, com a palavra "editorial" ou "carta" |

## O que conta e o que não conta

**Não consome orçamento:**

- Nome de produto (`Camiseta Pima Manga Curta`)
- Preço e percentual (`R$ 129,00`, `15% OFF`)
- Código de cupom
- Texto dos botões
- Rodapé legal, endereço, descadastro
- Alt de imagem
- Assunto e preheader (têm regra própria)

**Consome orçamento:**

- Headline e subheadline
- Todo parágrafo de corpo
- Rótulos de diferencial (`Frete grátis`, `Troca em 30 dias`)
- Legenda de bloco de produto que não seja o nome do produto
- Linha de condição da oferta

Motivo da separação: nome de produto e preço são **fato**, e fato não é o
que infla a copy. O que infla é argumento. A regra existe para conter
argumento.

## Curva ao longo de uma sequência

Quando o brief pede uma sequência de campanha na mesma semana, a copy
encurta a cada envio. O padrão aceito internamente:

| Posição | Proporção do teto |
|---|---|
| Primeiro envio | 100% do teto |
| Segundo envio | ~90% |
| Terceiro envio e seguintes | ~55% |

Razão: o contexto já foi dado. Repetir o contexto é o que produz o
e-mail 3 mais longo que o e-mail 1, que é o sintoma clássico.

## Como contar

`scripts/lint_copy.py` faz a contagem. Manualmente:

1. Junte todos os campos que consomem orçamento, na ordem da peça.
2. Remova nomes de produto, preços, percentuais e códigos.
3. Conte palavras separadas por espaço. Hífen não separa (`pós-compra` é
   uma palavra).

## Quando o orçamento estoura

Na ordem, e nunca pulando para o passo 4:

1. **Corte o argumento mais fraco por inteiro.** Não encurte três frases;
   apague uma.
2. **Troque argumento por fato.** Uma linha com número real do brief
   substitui três linhas de persuasão, e ainda remove cara de IA (§4.3 da
   pesquisa: especificidade é o humanizador mais barato).
3. **Mova para outro e-mail.** Se sobra argumento, sobra e-mail. Duas
   mensagens são dois e-mails.
4. **Peça exceção editorial no brief.** Último recurso, e só quando o
   cliente pedir peça editorial de fato.

O que **nunca** é solução: reduzir o corpo de texto abaixo de 14px ou o
rodapé abaixo de 11px para caber. Se a copy só cabe encolhendo, a copy é
que está grande.

## Falso positivo conhecido

§8 da pesquisa, calibração: **um parágrafo de 25 a 40 palavras no e-mail
inteiro não é vício** quando é a única explicação do produto. Um welcome de
80 palavras em que 35 são um único parágrafo explicando o que a loja vende
está correto. O que é vício é o e-mail com quatro parágrafos de 30
palavras cada.
