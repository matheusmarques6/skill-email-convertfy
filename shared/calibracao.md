# Calibração: o que NÃO é vício em e-mail de e-commerce

Fonte: `docs/pesquisa/pesquisa-vicios-ia-email.md` seção 8.

Esta lista existe para impedir falso positivo. Metade do que um catálogo de slop
de web chama de "cara de IA" é convenção de produção em e-mail. Reprovar peça boa
custa mais caro que deixar passar um vício médio: o operador perde a confiança no
lint e passa a ignorar também os B.

**Regra de uso:** antes de adicionar entrada no léxico, regra no linter ou item
num catálogo anti-vício, confira esta lista. Se a proposta reprova algum item
daqui, ela está errada ou precisa de condição mais estreita.

## Os sete casos protegidos

### 1. Caixa alta em headline curta, rótulo e botão
Protege contra **C35** e **C34**.
`COMPRAR AGORA`, `FRETE GRÁTIS`, `NOVO` são padrão de arsenal.
Guarda no lint: C35 só acusa a partir de 6 palavras seguidas em caixa alta, o que
é parágrafo gritado, não rótulo. C34 (Title Case) exige 4 palavras capitalizadas
seguidas e só vale em pt-BR.

### 2. Layout centralizado e coluna única de 600px
Protege contra **D16** e contra qualquer importação de lista de web.
É a regra técnica da Convertfy, não um sintoma. O `lint_email.py` acusa quando o
container **não** é 600 (598 aceito), ou seja, na direção oposta.

### 3. Número grande de oferta como elemento visual
Protege contra **C02**, **D09** e **D13**.
`15% OFF` em display gigante é o contrário de número inventado: é o fato da peça.
Guarda no lint: percentual e preço da oferta são isentos de C02; o que C02 pega é
número sem origem no brief, tipo contagem de clientes.

### 4. Repetir o mesmo CTA com o mesmo destino
Protege contra **C44**.
Um e-mail com o mesmo botão três vezes apontando para a mesma URL é boa prática.
Guarda no lint: C44 só acusa quando há mais de um **destino** distinto entre os
CTAs principais.

### 5. "Comprar agora", "Shop now", "Aproveitar" como CTA
Protege contra **C43** e **C21**.
CTA humano é verbo de compra mais objeto, sem criatividade. No corpus de 35
welcomes, 64 CTAs se resumem a oito verbos.
Guarda no lint: C43 tem lista de verbos aceitos por idioma e acusa o que está
fora dela, nunca o que está dentro.

### 6. Frase pronta curta de boas-vindas seguida imediatamente da oferta
Protege contra **C16**, **C12** e **C26**.
`Que bom ter você aqui` mais a oferta é padrão até de marca grande (L.L.Bean usa).
O vício não é a frase pronta: é a frase pronta **sozinha**, sem a oferta logo
depois, ou o pigarro longo antes de chegar ao ponto.
Guarda no lint: as entradas de C16 são frases específicas de pigarro
("no mundo de hoje", "quando se trata de"), nunca saudação curta.

### 7. Um parágrafo de 25 a 40 palavras, quando é a única explicação do produto
Protege contra **C45** e **C18**.
No corpus humano, 2,3% dos blocos passam de 20 palavras, tipicamente 1 por
e-mail. Um parágrafo explicativo é humano; três é vício.
Guarda no lint: C45 mede o corpo inteiro contra o teto do tipo (80 palavras em
welcome e campanha, 60 em carrinho), não parágrafo a parágrafo. C18 só roda no
corpo e só quando a média passa de 8 palavras por frase.

## Casos de calibração já cobertos por teste

Os sete itens acima viram teste executável em
`scripts/tests/test_lint_copy.py` e `scripts/tests/test_lint_email.py`, na classe
de casos positivos. Falso positivo neles é falha de build, não discussão de gosto.

Linhas humanas usadas como referência positiva (seção 2.2 da pesquisa):

- `Use code WELCOME10 today and start your AB BIO® routine with savings.`
- `If your mattress feels almost right (but you still wake up tired), let's fix that.`
- `Cruelty Free / Women Founded / Ethically Sourced`
- `Acessórios, roupas, relógios e sapatos premium` (lista de categoria, não tríade)
- `Que bom ter você aqui` seguido da oferta

## O que ainda gera falso positivo conhecido

Registrado aberto, para não fingir precisão que o lint não tem:

- **C21 com palavra literal do nicho.** `mergulhe` em loja de mergulho,
  `ritual` em marca de skincare que usa a palavra no rótulo do produto,
  `robusto` na descrição de uma mochila. São severidade A, então o revisor
  derruba com justificativa, mas o lint vai apontar.
- **C22 com clube real.** `acesso exclusivo` é vício genérico e fato quando o
  clube existe. Depende da ficha da marca, que o lint de copy ainda não lê.
- **C34 com nome próprio composto.** Quatro palavras capitalizadas seguidas de
  nome de marca ou de linha podem disparar Title Case.
- **C02 com número de especificação.** `caixa de aço 316L` e `5 ATM` precisam
  estar em `brief_numbers`, senão contam como órfãos. Isso é intencional: obriga
  a ficha do produto a existir.
