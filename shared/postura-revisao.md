# Postura de revisão

Como uma peça é criticada antes de ir para o humano. Corrige **P06
(autoaprovação)** e fecha o que o lint não alcança.

Base: seção 7 da pesquisa (P06), o laço de crítica do email-marketing-bible, a
postura de "aprovação se conquista" da skill de revisão de animação do Emil
Kowalski, e a arquitetura de avaliações isoladas do impeccable. Tudo reescrito
para e-mail e para as regras da Convertfy.

## As cinco condições

1. **Revisor separado.** Quem escreveu não aprova. O crítico é outra passada,
   idealmente outro modelo, e nunca a continuação da conversa que produziu a
   peça.
2. **Contexto limpo.** O crítico recebe a peça renderizada e a ficha da marca.
   Não recebe o histórico, nem o brief interno, nem as críticas anteriores, nem a
   nota alvo. Saber que a rodada anterior tirou 7 contamina a próxima nota.
3. **Por padrão aponta problema.** Aprovação é conquistada, não presumida. Uma
   peça que "funciona" mas soa de assistente é uma reprovação, não um empate. Se
   o crítico não achou nada, ele diz o que procurou e onde procurou.
4. **Nota de 0 a 10.** Alvo 9. A nota entra no relatório e serve de tendência
   entre rodadas; ela não substitui a lista de problemas.
5. **No máximo 4 rodadas.** Se a peça não chegou a 9 na quarta, ela sobe para o
   humano com a lista do que travou. Rodada 5 é sinal de brief ruim, não de
   redator ruim.

## Ordem obrigatória

O lint roda **antes** do crítico. São papéis diferentes e misturar os dois
estraga os dois:

```
copy em JSON  ->  lint_copy.py   ->  B? para. Corrige e repete.
HTML final    ->  lint_email.py  ->  B? para. Corrige e repete.
peça limpa    ->  crítico        ->  nota e lista de problemas
nota 9        ->  humano
```

O crítico nunca discute o que o lint já decidiu. Travessão não é questão de
gosto: é porta fechada. O crítico também não "perdoa" um B.

## O que o crítico avalia (e o lint não)

Os itens de julgamento do catálogo, mais a pergunta que resume todos:

| Pergunta | Regra |
|---|---|
| Alguma urgência ou escassez que não está no brief? | C06 |
| Algum número que existe, mas não mede o que a frase diz? | C02 (parte J) |
| A peça responde a alguma objeção que ninguém fez? | C19 |
| O tom é da categoria certa, ou é infoproduto transplantado? | P09 |
| A estrutura veio do vault, ou é a sequência genérica de landing page? | D16, P08 |
| A imagem é real da loja? | D15 |
| A hierarquia tem razão mínima de 2:1 entre headline e corpo? | D12 |
| O dark mode não some com nada? | D19 |

**A pergunta que resume:** trocando o logo e o nome do produto, esta peça serve
para qualquer outra loja do mesmo nicho? Se serve, ela é homogênea, e
homogeneidade é o problema observado de verdade (20 de 20 lojas Shopify não
relacionadas mandando o mesmo texto de boas-vindas na Trendtrack). Não é o
provedor que penaliza: é o cliente que já viu esse e-mail.

## Formato do relatório do crítico

Curto e acionável, nesta ordem:

1. Nota de 0 a 10.
2. De 3 a 5 problemas prioritários, cada um com o ID da regra quando houver, o
   trecho e a correção proposta.
3. Observações menores, se existirem.
4. O que está bom, em no máximo 2 linhas. Serve para o redator não destruir o que
   funcionou na próxima rodada.

Sem preâmbulo, sem resumo do que a peça tenta fazer, sem elogio de abertura.
Comentário sobre a própria análise é o mesmo vício de C07, do outro lado da mesa.

## Quando recusar em vez de revisar

O crítico recusa a rodada inteira, sem nota, quando:

- falta ficha da marca ou brief com oferta, produto e prazo (P01);
- a peça chegou com `[FALTA: ...]` ou placeholder repetido (P02, P04);
- o número de blocos entregues não bate com o declarado (P04);
- a peça foi escrita antes da estrutura estar decidida (P08).

Recusar é mais barato que revisar peça que nasceu errada.
