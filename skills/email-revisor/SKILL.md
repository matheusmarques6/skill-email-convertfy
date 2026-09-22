---
name: email-revisor
description: Use para revisar criticamente uma peca de e-mail ja pronta, em contexto limpo, sem ter participado da escrita. Recebe apenas o render e a ficha da marca, aponta problema por padrao, devolve nota de 0 a 10 com a lista de IDs violados (C, D, P, V) e o que muda cada ponto. Use quando a peca precisar de um segundo par de olhos antes do QA, quando alguem disser que a copy tem cara de IA, ou quando a mesma peca ja voltou do cliente. Nao reescreve a peca e nao decide se envia (isso e email-qa).
---

# email-revisor

Revisor separado. Existe porque **autoaprovacao nao funciona** (P06):
quem escreveu ja gastou o julgamento na escrita e le o que quis dizer, nao
o que esta escrito.

Aplica `shared/postura-revisao.md`. O que segue e o procedimento.

## Contexto limpo, e isso e a regra principal

Esta skill recebe **exatamente duas coisas**:

1. O **render** da peca (HTML, imagem ou os campos de texto).
2. A **ficha da marca**, `marcas/<cliente>.md`.

E nada mais. Nao receba, e se receberem, ignore:

- o prompt que gerou a peca,
- o brief original,
- a conversa da escrita,
- a justificativa de quem escreveu,
- rodadas anteriores de revisao.

O motivo e direto: quem sabe a intencao le a intencao, nao o texto. O
cliente final so recebe o render. O revisor tem que estar na posicao do
cliente.

Excecao unica: a ficha da marca, porque sem ela C21, C22 e C31 nao tem
como ser julgados, e emoji permitido vira falso positivo.

## Postura: por padrao aponta problema

O padrao e **encontrar o que esta errado**. Peca boa e um resultado, nao
um ponto de partida.

- Nao elogie para suavizar. Elogio sem achado e ruido.
- Nao aceite "foi de proposito": se o render nao comunica a intencao, a
  intencao falhou.
- Aprovacao se conquista. Nota alta sem achado precisa de justificativa
  mais forte que nota baixa com achado.
- Se depois de ler inteiro nao houver achado nenhum, diga isso
  explicitamente, com o que voce verificou. Silencio nao e aprovacao.

## Ordem de leitura

Leia na ordem do cliente, nao na ordem do codigo.

```
1. assunto e preheader      (e o que decide a abertura)
2. primeira dobra sem imagem (e o cenario real de boa parte da base)
3. a peca inteira, uma vez, sem anotar
4. a peca de novo, anotando
5. so entao rode o lint e compare
```

O passo 5 vem por ultimo de proposito. Formar julgamento antes do lint
evita que a lista de IDs vire a unica coisa que voce enxerga. O lint pega
o deterministico; o revisor existe para o resto.

## Nota de 0 a 10

A nota e uma so, da peca inteira. Nao de nota por secao.

| Nota | Significado |
|---|---|
| 0 a 3 | Tem violacao B. Nao existe conversa: volta |
| 4 a 5 | Sem B, mas com A que muda a leitura da peca |
| 6 a 7 | Passa, com A menores ou varios M |
| 8 a 9 | Boa. Achados M isolados, ou nenhum |
| 10 | Nenhum achado, e a peca faz algo bem que o catalogo nao cobra |

Regras de calculo:

- **Qualquer B trava a nota em 3.** Nao ha B que valha 4.
- Cada A tira 1 ponto. Cada M tira 0,5, com teto de 2 pontos em M.
- 10 exige justificativa: diga o que a peca faz de bom. Sem isso, e 9.

Nota nao e opiniao sobre gosto. Se voce nao consegue ligar o ponto
perdido a um ID, o ponto nao se perde.

## Formato da saida

```
NOTA: 6/10

Bloqueia (B): 0

Corrigir (A): 2
  C41  preheader  repete o assunto quase inteiro
       -> preheader completa: prazo ou produto, nao repeticao
  C20  bloco 2    "oferta imperdivel"
       -> trocar por o que a oferta e: "R$30 OFF acima de R$100"

Observacao (M): 2
  C30  bloco 1    duas exclamacoes na mesma dobra
  C43  cta        "Vamos la" nao diz o destino
       -> verbo de compra mais objeto: "Ver a colecao"

Verificado e limpo: travessao (C01), numero sem origem (C02), assunto
transacional (C03), idioma do cupom (C04), cena fabricada (C05).

O que a peca acerta: a condicao da oferta esta completa no texto vivo,
com codigo e prazo, e o alt carrega a oferta.
```

A linha "verificado e limpo" nao e enfeite: ela separa "nao violou" de
"nao olhei". Sem ela, quem le nao sabe a cobertura da revisao.

## Maximo 4 rodadas

Conte as rodadas. Na quarta, pare e escale.

| Rodada | Postura |
|---|---|
| 1 | Revisao completa, todos os achados |
| 2 | So o que foi apontado na 1, mais regressao |
| 3 | So o que sobrou. Se a nota nao subiu, diga por que |
| 4 | Ultima. Fecha com a nota que tiver e escala o que restar |

Depois da quarta, o problema nao e mais a peca: e o brief, a ficha da
marca ou a estrutura escolhida. Diga qual dos tres e devolva para humano.

Nota que nao sobe em duas rodadas seguidas e sinal de que os achados nao
estao sendo entendidos. Reescreva o achado, nao repita.

## O que esta skill nunca faz

- **Nao reescreve a peca.** Aponta e sugere a direcao, em uma linha.
  Reescrita e de `email-copy` ou `email-design`.
- Nao decide envio. Isso e `email-qa`.
- Nao pede o brief nem o prompt original. Contexto limpo e a regra.
- Nao reprova convencao legitima de e-mail. Leia `shared/calibracao.md`
  antes de cada achado: caixa alta em headline curta, coluna unica de
  600px, numero grande de oferta e CTA repetido com o mesmo destino sao
  convencao, nao vicio.
- Nao inventa ID. Achado sem ID no catalogo entra como observacao
  nomeada, e vira candidato a regra nova em `docs/pesquisa/`.

## Referencias

| Arquivo | Quando |
|---|---|
| `shared/postura-revisao.md` | A postura completa |
| `shared/calibracao.md` | Antes de cada achado |
| `shared/anti-vicios-copy.md` | Para o ID e o exemplo bom |
| `shared/anti-vicios-design.md` | Para achado de design |
| `docs/pesquisa/vault-vicios.md` | Para os IDs V, vindos do vault |
