# Padrão de qualidade: o que faz a peça ser boa

Todo o resto do catálogo diz **o que não fazer**: C, D, P, R, V, mais de
cem regras, todas negativas. Peça com zero violações tira nota alta e
ainda pode ser esquecível.

Este arquivo é o outro lado. São perguntas de **sim ou não** sobre o que a
peça precisa **ter**. Zero violações mais zero "sim" aqui é uma peça
correta que não vende.

Fonte: os 24 modelos validados, as 9 famílias de assunto e a estrutura do
dia de pico, em `docs/dados/resumo-carteira.md`.

---

## Como usar

O revisor responde cada pergunta com **sim** ou **não**. Não há "mais ou
menos": se precisa de ressalva, é não.

- **Q1 a Q6 valem para toda peça.** Menos de 5 sim reprova, mesmo com o
  lint limpo.
- **Q7 a Q10 dependem do papel.** Só conta o bloco do papel do envio.

A nota do revisor passa a ter dois lados: quantos defeitos (o catálogo) e
quantos acertos (aqui). Ver `shared/postura-revisao.md`.

---

## Q1 a Q6: valem para toda peça

### Q1. A oferta e a condição aparecem sem rolar?

Valor, código e prazo visíveis nos primeiros 500 px, no desktop **e** no
mobile.

**Por quê:** é o que a carteira manda em `08_Skill`, seção 10. E o que
falhou quando não: o esquenta em tom de anúncio, sem número nem prazo,
fez **1 pedido**.

**Como verificar:** cobrir tudo abaixo de 500 px no `desktop-600.png`.

### Q2. A peça diz um fato que só esta loja poderia dizer?

Um número real, um nome de produto real, uma condição concreta, um
detalhe de material, um prazo de entrega verdadeiro.

**Por quê:** é o humanizador mais barato que existe, e é o que separa a
peça de um template. O corpus humano traz número ou código em **19% dos
blocos**.

**Como verificar:** trocar o nome da loja por outro. A peça continua
fazendo sentido? Se sim, é genérica: responda **não**.

Esta é a pergunta que o Teste 1 da Fase 5 reprovaria. A peça passou no
lint inteira e "Prata 925 com banho de ródio" serve para qualquer loja de
prata.

### Q3. O papel do envio está cumprido?

Antecipação antecipa e pede uma tarefa. Véspera prepara. Pico vende.
Fechamento fecha. Reabertura reabre para quem clicou.

**Por quê:** "referência do mesmo papel" é o princípio 2 da carteira. Peça
que confunde o papel perde o lugar na sequência.

**Como verificar:** ler só a peça, sem o brief. Dá para dizer qual é o
envio da sequência?

### Q4. Existe uma ação única e óbvia?

Um botão principal. CTA repetido com o mesmo destino conta como um.

**Por quê:** "um botão principal" está nas regras de copy da casa, e é
convenção confirmada no §8.

### Q5. A peça funciona com as imagens desligadas?

Desligue as imagens. Sobra a oferta, a condição e o próximo passo?

**Por quê:** é o cenário real de boa parte da base, e é o que o resumidor
de IA do Gmail e do Apple Mail enxerga.

### Q6. Alguém da loja assina, e essa pessoa existe?

Nome de gerente, fundador ou equipe, real e verificável.

**Por quê:** 4 dos 6 modelos titulares do ranking são formato de pessoa:
cupom liberado (1,66), status mudou (1,48), ligação (1,17), reabertura
(1,15).

**Atenção:** persona inventada é C05 e é nível 1. Sem a pessoa real, a
resposta é **não**, e a correção é tirar a assinatura, nunca inventar uma.

---

## Q7 a Q10: por papel

### Antecipação

| # | Pergunta | Por quê |
|---|---|---|
| Q7a | Traz uma **notícia nova** que os toques anteriores não deram? | Regra da receita de antecipação |
| Q8a | Pede uma **tarefa** (votar, confirmar vaga, salvar favorito)? | Quem cumpre entra antes, às 00h |
| Q9a | **Não repete a promessa** do toque anterior? | Promessa repetida mede 0,39 a 0,52 |
| Q10a | Diz o que acontece **na data**, não só que algo vem? | O esquenta vago fez 1 pedido |

### Pico

| # | Pergunta | Por quê |
|---|---|---|
| Q7b | O cupom está **visível e colado no botão**? | Regra de copy da casa |
| Q8b | O prazo tem **data e hora**? | Checklist antes de agendar |
| Q9b | O formato bate com o horário? (07h texto de pessoa, 18h mudança de estado) | 07h 1,66 · 18h 1,48 com assunto 2,13 |
| Q10b | A peça **não anuncia a próxima janela** de oferta? | "Nunca citar a oferta da próxima janela" |

### Fechamento

| # | Pergunta | Por quê |
|---|---|---|
| Q7c | O prazo declarado é **real e será cumprido** no ESP? | V16. Prazo não cumprido queima a lista |
| Q8c | **Não há prorrogação** nem extensão anunciada? | Extensão mede 0,49 e 0,52 |
| Q9c | A urgência vem de um **fato**, não de adjetivo? | C06, nível 1 |
| Q10c | Fecha de verdade, sem "ainda dá tempo" no dia seguinte? | V52 |

### Pós-pico

| # | Pergunta | Por quê |
|---|---|---|
| Q7d | **Não traz cupom novo** entre um evento e o próximo? | Quebra a escada do Q4 |
| Q8d | O aviso de estoque está em **fundo branco e texto preto**? | Foi o visual de maior clique: 3,61% e 3,20% |
| Q9d | A reabertura vai **só para quem clicou e não comprou**? | Regra da carteira |
| Q10d | Favoritos entre **D+5 e D+8**? | 1,12 com 3,19% de clique |

---

## A conta

```
sim em Q1 a Q6      : ___ de 6     (mínimo 5)
sim no bloco do papel: ___ de 4     (mínimo 3)
```

**Abaixo do mínimo, a peça reprova mesmo com o lint limpo.** O motivo
entra no veredito como `PQ<n>`, no mesmo formato de um ID de vício:

```
PQ2  a peça não diz nada que só esta loja poderia dizer
PQ6  assinatura sem pessoa real por trás
```

## O que este arquivo não é

Não é checklist de entrega, que é o `protocolo-de-execucao.md`. Não é
gosto: toda pergunta tem um número da carteira atrás. E não substitui o
catálogo de vícios: uma peça precisa passar nos dois, porque não errar e
acertar são coisas diferentes.
