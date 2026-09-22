---
name: email-campanhas-sazonais
description: Use ao montar uma campanha de data sazonal ou de pico (10.10, 11.11, Black Friday, Cyber, Natal, Boxing Day, 12.12) e ao escolher qual modelo validado usar em cada papel da sequência (antecipação, véspera, pico 07h, 11h, 18h, fechamento, reabertura, pós-pico). Traz o ranking de modelos da carteira com índice de receita, o que não funcionou e não deve ser repetido, e a estrutura do dia de pico. Não escreve a copy (isso é email-copy), não monta o HTML (isso é email-design) e não planeja o mês inteiro (isso é email-calendario).
---

# email-campanhas-sazonais

Escolhe **qual modelo** usar em cada papel de uma sequência sazonal, com
base no que a carteira mediu, não no que parece bom.

A regra que manda aqui: **cada e-mail parte de uma campanha validada que
fazia a mesma função.** No máximo duas referências, e as duas no mesmo
papel.

Divergências desta skill em relação ao CLAUDE.md: nenhuma.

## Protocolo obrigatorio

Segue `shared/protocolo-de-execucao.md` inteiro. Especificidades:

1. **Ficha e brief (P01, P02).** Além de oferta, produto e prazo, o brief
   sazonal precisa de **papel** (qual envio da sequência) e **data**.
2. **Anti-vícios.** Com `shared/calibracao.md` junto.
3. **Gate de lint.** Violação B não entrega.
4. **Leitura do brief**, uma linha, incluindo o papel e o modelo escolhido.
5. **Só o artefato (C07).**
6. **Ordem de trabalho (P08).**

## Os 5 princípios da carteira

Fonte: `fontes/BFCM-2026-Convertfy/08_Skill/`, seção 1.

1. **80/10/10.** 80% do calendário com campanhas validadas, 10% com
   variações delas (mesma estrutura, contexto novo), 10% com inspiração
   externa. Ver `shared/principios-carteira.md`.
2. **Referência do mesmo papel.** Máximo duas, as duas no mesmo papel.
3. **Nada inventado.** Avaliação, estoque, contador e número só se forem
   reais. Sem o dado, **o bloco sai**. É C02 e C06, nível 1.
4. **As melhores campanhas nos momentos de maior intenção** (picos e
   fechamentos). Dias comuns usam as outras validadas.
5. **Toda data tem contexto.** 8.8 Dia dos Pais, 9.9 do Cliente, 10.10
   Nota 10, 11.11 Black Antecipada. No global, estação.

## Como escolher o modelo

```
1. qual o papel do envio?        antecipação 1/2/3, véspera, pico 07/11/18,
                                  fechamento, último dia, reabertura, pós-pico
2. abra references/modelos-validados.md, seção "Por papel"
3. o titular do papel serve?      sim -> use
                                  não -> o segundo do mesmo papel
4. checou a situação?             "Fora do calendário" nunca entra
                                  "Ressalva" exige justificativa no brief
                                  "Teste" no máximo 1 por plano
5. o modelo já foi usado nesta semana?  sim -> escolha outro
```

Detalhe e o ranking completo em `references/modelos-validados.md`.

## A escada de oferta do Q4

Não quebrar, sob nenhuma circunstância:

```
10.10  ≤  Pré-Black  <  11.11  <  Black Friday
```

**Nada depois da Black passa a Black.** A Cyber tem oferta própria (o
combo), não é a Black esticada.

Mecânicas que sobem o ticket sem aprofundar o desconto: progressivo por
quantidade, kit, brinde para os 100 primeiros, desconto revelado no
checkout, crédito em dinheiro no lugar de porcentagem.

## Fechamento e pós

- **Fechamento real, sem prorrogação.** A prorrogação ensina a lista a
  esperar. Extensão mede 0,49 a 0,52: está fora do calendário.
- **D+2:** aviso de estoque em fundo branco.
- **D+5 a D+8:** favoritos.
- **Nada de cupom novo** entre um evento e o próximo.
- **Reabertura:** só para quem clicou na semana e não comprou, no dia
  seguinte ao fim.

## O que esta skill nunca faz

- Não usa modelo marcado "Fora do calendário".
- Não repete `status-mudou-18h` fora das 18h do pico.
- Não inventa número para preencher bloco de prova (C02, nível 1).
- Não prorroga oferta nem cria extensão.
- Não cita a oferta da próxima janela.
- Não escreve a copy nem monta o HTML.

## Referências

| Arquivo | Quando |
|---|---|
| `references/modelos-validados.md` | Escolher o modelo do papel |
| `shared/principios-carteira.md` | 80/10/10 e os outros princípios |
| `skills/email-copy/references/familias-de-assunto.md` | O assunto do papel |
| `skills/email-calendario/SKILL.md` | Planejar o mês, não o envio |
| `docs/dados/resumo-carteira.md` | Os números que a skill cita |
