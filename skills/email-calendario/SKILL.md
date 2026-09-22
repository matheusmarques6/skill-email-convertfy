---
name: email-calendario
description: Use ao planejar o calendário de campanhas de um mês ou de um trimestre para uma loja: quais envios, em que data e hora, com qual papel, qual público por nível de conta, e qual modelo validado em cada um. Aplica a proporção 80/10/10, a escada de oferta do Q4, os freios de entrega e a matriz de colisão entre campanha e automação. Produz um brief por envio, no formato que email-copy e email-design consomem. Não escreve a copy nem monta o HTML.
---

# email-calendario

Planeja o **mês**, não o envio. A saída é um brief por e-mail, com data,
hora, papel, público e modelo, pronto para `email-copy` consumir.

Fecha a lacuna do `/campaign-calendar` do `email-campaign-skill`, que não
tinha sido aproveitado (item 1c de `docs/auditoria-fusao.md`).

Divergências desta skill em relação ao CLAUDE.md: nenhuma.

## Protocolo obrigatório

Segue `shared/protocolo-de-execucao.md`. Especificidades:

1. **Ficha e brief (P01, P02).** Para planejar o mês, o brief precisa de
   **nível da conta** (A, B, C ou LP), tamanho do E90 e as datas que a
   loja já tem compromisso. Sem o nível, não planeje: o nível decide
   quantas vezes a lista toda pode ser usada.
2. **Anti-vícios** e `shared/calibracao.md`.
3. **Gate.** O gate desta skill não é o lint de copy: é o **gate de
   proporção** da seção abaixo. Um plano reprovado não vira brief.
4. **Leitura do brief**, uma linha, com mês, loja, nível e número de envios.
5. **Só o artefato (C07).** A saída é a tabela do plano mais os briefs.
6. **Ordem de trabalho.** Calendário vem **antes** de P08: ele decide o
   papel, e o papel decide a intenção que `email-copy` vai buscar.

## O gate de proporção, 80/10/10

Nenhum plano é entregue sem passar:

| Categoria | Regra |
|---|---|
| Validado | **mínimo 80%** |
| Inspiração | máximo 10% |
| Complemento | máximo 10% |

Conte antes de entregar. Plano abaixo de 80% validado volta para a
seleção de modelos, não para o cliente.

Referência: o plano Q4 2026 real fechou em 93/0/7.

Detalhe em `shared/principios-carteira.md`.

## Ordem de planejamento

```
1. nível da conta          decide o teto de lista toda no trimestre
2. datas com contexto      toda data tem contexto, senão não é data
3. papéis por data         antecipação, véspera, pico 07/11/18, fechamento, pós
4. modelo por papel        do ranking, respeitando a situação
5. público por envio       por camada e por nível de conta
6. gate de proporção       80/10/10
7. brief por envio         no schema da referência
```

## Público por nível de conta

| Nível | Critério | Lista toda no trimestre |
|---|---|---|
| A | Domínio com mais de 12 meses, spam abaixo de 0,05% | 2 |
| B | Domínio de 6 a 12 meses, ou spam entre 0,05% e 0,1% | 1 |
| C | Domínio com menos de 6 meses, ou spam acima de 0,1% | **0** |
| LP | Lista abaixo de 3 mil contatos | Só envios marcados `lista_pequena` |

Camadas: VIP, E30, E90, E180, LT, NA_*, CNC. Definição em
`shared/segmentacao-e-freios.md`.

**Padrão do envio comum: E90.** Nenhum envio passa de 2x o tamanho do E90
da conta.

## Os freios

Param o plano no meio, sem discussão:

| Sinal | Ação |
|---|---|
| spam acima de 0,1% num envio | Próximo envio desce um degrau de público |
| spam acima de 0,3% | Para de ampliar até o fim do plano. Só E90 |
| descadastro acima de 0,5% | Revisar assunto e frequência antes do próximo pico |
| bounce acima de 2% | **Parar e limpar** antes do próximo envio |
| queda no Postmaster | Pausar LT e reativação |
| aviso da Omnisend | Congelar volume e responder no mesmo dia |

Métrica de decisão: clique, pedidos e receita por mil, e spam. **Abertura
é sinal auxiliar**, por causa do Apple Mail.

## A escada de oferta do Q4

```
10.10  ≤  Pré-Black  <  11.11  <  Black Friday
```

Nada depois da Black passa a Black. A Cyber tem oferta própria.

## O que nunca entra no calendário

Com o dado, de `references/modelos-validados.md` da skill sazonal:

| O que | Dado |
|---|---|
| Extensão de oferta ("virou semana", "VIP Week") | 0,49 e 0,52 |
| Evento colado em outro | 0,38 a 0,50 |
| Esquenta em tom de anúncio | 1 pedido |
| `vespera` como modelo | 0,10 na amostra ampla |
| Cupom novo entre um evento e o próximo | Quebra a escada |
| Segmento ampliado sem critério | Por mil caiu de US$ 55 para US$ 22 |

## Antes da Black

Duas reativações em outubro, com **supressão de quem não clicar**. A
limpeza é o que sustenta o volume de novembro.

## O que esta skill nunca faz

- Não entrega plano abaixo de 80% validado.
- Não usa a lista toda além do teto do nível da conta.
- Não prorroga oferta nem cria extensão.
- Não planeja data sem contexto.
- Não escreve copy nem monta HTML.

## Referências

| Arquivo | Quando |
|---|---|
| `references/calendario-q4-2026.md` | O schema de brief e o exemplo real |
| `shared/principios-carteira.md` | 80/10/10 e os cinco princípios |
| `shared/segmentacao-e-freios.md` | Camadas, níveis e freios |
| `skills/email-campanhas-sazonais/references/modelos-validados.md` | Modelo por papel |
| `skills/email-copy/references/familias-de-assunto.md` | Família por papel |
