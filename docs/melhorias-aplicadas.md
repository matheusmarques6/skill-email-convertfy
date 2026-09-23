# Melhorias aplicadas

## 1. Padrão positivo de qualidade

**O problema.** Todo o catálogo dizia o que **não** fazer: C, D, P, R, V,
113 regras, todas negativas. Peça com zero violações tirava nota alta e
podia ser esquecível. Aconteceu no Teste 1 da Fase 5: a peça passou limpa
e eu escrevi "correta e esquecível" em prosa, no fim do relatório, sem ID
e sem efeito na nota.

**O que foi feito.** `shared/padrao-de-qualidade.md`: 6 perguntas que
valem para toda peça e 4 por papel (antecipação, pico, fechamento,
pós-pico). Sim ou não, sem meio-termo. Cada uma com o número da carteira
atrás.

A nota do revisor passa a ter dois lados: defeitos pela escala de sempre,
acertos pelo padrão. Menos de 5 sim em Q1 a Q6, ou menos de 3 no bloco do
papel, e a nota não passa de 6 **mesmo com o lint limpo**. Os "não" viram
achados `PQ<n>`.

**O efeito, medido.** A peça do Teste 1 caiu de **8/10 para 6/10**, com
zero defeitos, por PQ2 (não diz nada que só aquela loja poderia dizer) e
PQ6 (sem assinatura de pessoa real). A do Teste 2 fez 5 de 6 e 4 de 4 no
bloco de pico. Antes, as duas apareciam como "sem violações".

## 2. Versão do catálogo, derivada do conteúdo

**O problema.** As regras mudavam e as medições antigas continuavam
parecendo atuais. Aconteceu de verdade: o `lint_status` do vault foi de 2
notas limpas para 1 depois que V29, V36 e V52 entraram, e o texto
continuava dizendo 2. Eu escrevi a conclusão antes de ler o número.

**O que foi feito.** `scripts/versao_catalogo.py` calcula a versão a
partir do **conteúdo** dos 10 arquivos que definem regra: os dois linters,
os dois léxicos e os seis documentos de vício e calibração. Versão escrita
à mão desatualiza sem ninguém perceber; esta não tem como.

Carimbada em:

| Onde | Campo |
|---|---|
| `lint_copy.py` e `lint_email.py` | `versao_catalogo` no JSON |
| Relatório de cada peça | linha na tabela |
| Galeria do lote | rodapé do cabeçalho |
| `lint-status-vault.md` | aviso no topo |

**Prova de que funciona.** Ao editar os dois linters para adicionar o
carimbo, a versão mudou sozinha de `cat-55633817` para `cat-ccfd3472`.

Cinco testes travam o comportamento, incluindo um que edita o léxico,
confere que a versão andou, e restaura.

## O que continua aberto

Da lista que sugeri, três não foram feitas:

| # | O quê | Por quê |
|---|---|---|
| 2 | O revisor não roda em código | Esforço M. Exige o `produzir_lote` abrir os PNGs e chamar o revisor de verdade |
| 3 | Nada volta da realidade | Esforço G, e depende de decidir o acoplamento com o Omnisend da conta |
| 4 | `evals/casos/` vazio | Depende de você escolher os e-mails aprovados |
| 6 | `shared/` com 1.555 linhas | Esforço P, mas mexe em como toda skill carrega contexto |

A 3 continua sendo a de maior retorno: é o que transforma a suíte em algo
que melhora sozinho, em vez de melhorar quando alguém mexe.
