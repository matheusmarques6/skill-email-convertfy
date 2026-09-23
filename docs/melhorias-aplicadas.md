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

## 3. O revisor virou executável

**O problema.** `skills/email-revisor` eram 163 linhas de prosa e zero
linhas de código. Nada em `scripts/` chamava o revisor. O contexto limpo
era uma instrução que dependia de alguém lembrar, e a nota que o lote
mostrava era só a mecânica do lint.

**O que foi feito.** `scripts/revisar.py`, com a divisão honesta: o
julgamento continua sendo do agente, porque exige olhar as imagens; tudo
em volta virou código.

| Comando | O que faz |
|---|---|
| `--preparar` | Copia **só** os três PNGs e a ficha para `<peça>/revisao/`, gera o formulário do papel e avisa se vazou HTML, brief ou copy |
| `--pontuar` | Recusa formulário incompleto, lê o lint do disco, aplica a regra da nota. Exit 1 se não aprovada |
| `--estado` | Diz se já foi revisada e por qual versão do catálogo |

A galeria passou a ter três estados: **aprovada** (lint limpo e revisor
passou), **aguarda revisor** (lint limpo, revisor não passou) e
**reprovada**. Antes, "lint limpo" já contava como aprovada.

**O efeito, medido na peça do Teste 1:**

```
NOTA: 6/10 · reprovada
Defeitos: 0 B · 0 A · 0 M
Padrão de qualidade: 2/6 gerais · 2/4 do papel
```

Zero defeitos e reprovada. É a peça que passava em tudo.

**E um erro meu que o revisor pegou.** Eu tinha pontuado essa peça de
cabeça em 4 de 6, sem olhar o render. Olhando: **Q1 também é não**, porque
o valor "10%" só existe no assunto e não aparece no corpo. Com o assunto
fora da tela, a peça não diz de quanto é o desconto. Corrigido em
`evals/teste-auditoria/README.md`.

## O que continua aberto

Da lista que sugeri, três não foram feitas:

| # | O quê | Por quê |
|---|---|---|
| 3 | Nada volta da realidade | Esforço G, e depende de decidir o acoplamento com o Omnisend da conta |
| 4 | `evals/casos/` vazio | Depende de você escolher os e-mails aprovados |
| 6 | `shared/` com 1.555 linhas | Esforço P, mas mexe em como toda skill carrega contexto |

A 3 continua sendo a de maior retorno: é o que transforma a suíte em algo
que melhora sozinho, em vez de melhorar quando alguém mexe.
