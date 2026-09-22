# Anti-vícios de processo (P01 a P09)

Estes não aparecem no texto final: são a origem dos vícios de copy e de design.
Fonte: `docs/pesquisa/pesquisa-vicios-ia-email.md` seção 7.

Cada item traz a **correção concreta na skill**: o que a skill tem que fazer,
não o que ela deve "ter em mente". Regra dura em prosa não se aplica sozinha
(é o próprio P05).

## P01 Gerar sem ler marca, produto e oferta reais

**Correção:** a skill bloqueia a geração enquanto não tiver `marcas/<cliente>.md`
mais um brief com oferta, produto e prazo. Sem os três, a saída é uma pergunta,
não uma peça. O campo de números do brief alimenta `brief_numbers` do
`lint_copy.py`, que é o que torna C02 verificável.

## P02 Preencher lacuna com invenção

**Correção:** campo sem dado vira **uma** pergunta ao operador, ou o marcador
`[FALTA: <o que falta>]`. Nunca número, estoque, prazo ou depoimento inventado.
O `lint_email.py` reprova `[FALTA: ...]` que sobreviveu até o HTML, com
severidade B: a lacuna é para ser vista e preenchida, não entregue.

## P03 Variações que são tintas da mesma ideia

**Correção:** cada variante declara o eixo em que diverge (oferta, prova ou
problema) antes de ser escrita. Duas variantes com o mesmo eixo contam como uma
só e a skill gera outra. Vale a disciplina do protótipo lado a lado: variar para
decidir, não para encher.

## P04 Truncar a entrega

**Correção:** contar entregáveis antes e depois. A skill declara quantos blocos
vai entregar, entrega, e compara. Placeholder enumerado repetido, seção faltando
e qualquer forma de "o resto segue o mesmo padrão" reprovam a rodada. O
`lint_email.py` cobre a parte detectável (placeholder idêntico repetido, B).

## P05 Confiar só no prompt para regra dura

**Correção:** toda regra dura tem lint determinístico e gate de entrega. A prova
está registrada na própria história da Convertfy: o travessão escapou de um
prompt que o proibia em vários pontos, com checklist e autocorreção. Regra sem
código é preferência, não regra. Se uma regra nova não puder ser checada por
código, ela entra como julgamento explícito em `shared/postura-revisao.md`, não
como parágrafo perdido numa skill.

## P06 Autoaprovação

**Correção:** revisor separado, contexto limpo, nota de 0 a 10, no máximo 4
rodadas, e postura padrão de apontar problema. O protocolo inteiro está em
`shared/postura-revisao.md`. Quem escreveu não aprova.

## P07 Copiar o vício do exemplo

**Correção:** amostra de swipe citada em nota do vault passa pelo
`lint_copy.py` antes de virar referência, e o resultado fica registrado como
`lint_status: limpa | contaminada` no frontmatter da nota. O corpus humano de 35
welcomes tem pelo menos 5 linhas com vício de IA (seção 2.3 da pesquisa): sem
esse passo, o redator aprende o vício com o exemplo aprovado.
Lembrete de escopo: a alteração do frontmatter acontece no Obsidian. Este repo
lê o vault, nunca escreve nele.

## P08 Escrever antes de decidir a estrutura

**Correção:** ordem fixa. Intenção (var1), estrutura (var2), variantes do
arsenal, copy por schema. A estrutura vem do vault pelo protocolo de seleção de
9 passos, que elimina antes de rankear. Escrever copy antes de ter estrutura é o
que produz a peça centralizada genérica (D16).

## P09 Tom de outro mercado

**Correção:** a ficha da marca define o registro, e o léxico carrega as frases de
infoproduto que não entram em e-commerce. Transplante típico já rejeitado:
"meu contador disse que sou LOUCO", "PARTE 1: EDUCAÇÃO", promessa de framework de
lançamento. Quando o brief pedir tom agressivo, ele precisa dizer isso com
palavras, e mesmo assim as regras C01 a C07 continuam valendo.

## Vício de processo que a pesquisa não cobre e a skill precisa evitar

**Justificar regra por mecanismo inventado.** Escrever que "o provedor penaliza
texto de IA" é especulação contrariada pela evidência. Toda justificativa de
regra nesta suite aponta para um destes quatro: renderização, conformidade legal,
acessibilidade ou engajamento medido. Quando não houver nenhum dos quatro, a
regra é preferência de casa e deve dizer isso.
