# Lote Blue Wolf: por que as 5 foram reprovadas

Resultado honesto do primeiro lote. **5 peças, 0 aprovadas.**

A reprovação está certa, e o motivo é o mesmo em todas.

## O bloqueio: `E_PLACEHOLDER`

Os briefs do Q4 trazem placeholders que a loja precisa preencher:

```
[Gerente]   nome de quem assina
[Loja]      nome da loja no corpo
[N], [valor], [produto]
```

Mais o `[FALTA: endereco fisico do remetente]`, que a ficha
`marcas/blue-wolf.md` não tem e que a CAN-SPAM exige.

O próprio brief manda preencher: *"Nada de número inventado: o que está
entre colchetes ([N], [valor...]"*.

**A suíte não preenche isso.** Inventar nome de gerente ou endereço é C02
e P02, que são nível 1 da hierarquia. O pipeline recusar é o
comportamento correto, não uma falha.

## O que falta para aprovar

Três dados da loja, em `marcas/blue-wolf.md`:

| Campo | Para quê |
|---|---|
| `gerente` | assinatura dos e-mails de outubro |
| `fundador` | assinatura dos e-mails do 11.11 |
| `endereco` | rodapé, exigência legal |

Com os três preenchidos, as 5 peças passam a depender só do ciclo de
render e do revisor.

## O que o ciclo já corrigiu, em 3 rodadas

| Rodada | Achado | Correção |
|---|---|---|
| 1 | **R10** botão fora da primeira dobra no mobile (aparecia em ~1.650 px) | Oferta e CTA subiram para a primeira dobra, como a carteira manda (oferta, cupom, prazo e botão nos primeiros 500 px) |
| 1 | `[FALTA: cta]` em todas | O CTA estava dentro da descrição do bloco, entre aspas. Extraído por regex |
| 2 | **R13** descrição de estrutura virando corpo do e-mail: *"Hero: 'QUER JOGAR UM JOGO?' + grade de 8 botões com os códigos"* aparecia para o cliente | Separada copy real de instrução de montagem. Só a frase entre aspas entra |
| 3 | Resto de montagem: *"'Onde testar': grade 2x2 com..."* | Detector de montagem (` + ` entre aspas, "grade 2x2", "botão único") |

## O que ficou, e é honesto dizer

Depois das 3 rodadas, sobrou:

1. **Duplicação de headline.** "Quer jogar um jogo?" aparece no assunto,
   no hero e de novo em caixa alta. O brief tem os três campos e o
   montador não deduplica.
2. **R12, peça anêmica.** O brief pede uma grade de 8 cupons e uma grade
   2x2 de produtos. O esqueleto entrega texto. **Falta o arsenal de
   blocos**: `header` e `cta` têm zero variantes no vault, e não há bloco
   de grade em `assets/arsenal/`.
3. **Sem direção de imagem.** O brief traz `prompt_imagem` em todos os 67
   e o pipeline ignora. É a lacuna 6e da auditoria.

Os três são de estrutura, não de CSS, e é por isso que a regra manda
parar na terceira rodada e devolver.
