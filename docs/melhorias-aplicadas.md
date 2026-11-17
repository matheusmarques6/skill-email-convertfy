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

## 4. Camada de direção visual na `email-design`

**O problema.** A `email-design` garantia que a peça não quebra (tabela,
VML, dark mode, peso) e reconhecia vício. Não dizia como fazer a peça boa:
que tamanho tem o título, quanto espaço vai entre blocos, que proporção
tem a foto da grade, que cor vai no botão. O agente preenchia isso com o
default dele.

**O que foi feito.** Estudo do `design-taste-frontend`, do `impeccable` e
das skills do Emil Kowalski, mais a doutrina de design do Max no vault e o
design system real da Blue Wolf, reescritos para e-mail de e-commerce em
onze referências novas (`skills/email-design/references/`):
`direcao-visual`, `modulos-ecommerce`, `tipografia`, `espaco-e-ritmo`,
`cor-e-contraste`, `direcao-de-imagem`, `movimento-e-gif`,
`critica-visual`, `operacoes`, `checklist-de-design` e
`extracao-de-marca`. O `SKILL.md` ganhou a seção "Camada de direção
visual" e continua abaixo de 500 linhas.

**Regra dura em código, não em prosa:**

- `lint_email.py` passou a checar D21, D26, D27, D28 e D29, todas como
  `revisar` (severidade M, D-003). 14 testes novos.
- Os 14 trechos de HTML de `modulos-ecommerce.md` são extraídos e montados
  por `scripts/vitrine_modulos.py`. O teste
  `scripts/tests/test_vitrine_modulos.py` exige zero achado de lint, todo
  slot com valor, slot com sublinhado e espaço só da escala.

**O que o render pegou que a leitura não pegava:**

1. **Botão encolhendo no celular.** `width:300px; padding:16px 0` vira um
   retângulo do tamanho do texto, porque a `casca-600` zera o `width` de
   link no celular. Os módulos usam `min-width` e padding lateral, como o
   `cta-1` do arsenal já fazia.
2. **Logo com o dobro do tamanho no celular.** A `casca-600` forçava
   `width:auto` em toda imagem; imagem exportada em 2x voltava para a
   largura natural. Medido: o cabeçalho tinha 80px no desktop e 116px no
   celular. **A regra foi corrigida na casca** (só `max-width:100%` e
   `height:auto`), e o md5 do manifesto atualizado. Com a correção, 80px
   nos dois.
3. **Slot sem sublinhado saindo cru.** `SAUDACAO` não era reconhecido como
   slot e aparecia na peça. Renomeado, e o script agora recusa slot sem
   sublinhado.

**Achados nas 44 variantes do vault** (somente leitura: registrados aqui
para correção no Obsidian), com as regras novas do lint:

| Variante | Achado |
|---|---|
| `body-6-skin-minimalism-101` | D27, `text-shadow` |
| `body-7-faq` | D26, texto de 10px (6 trechos) |
| `hero-5-cupom-em-tres-lugares` | D21, imagem principal fora de link |
| `products-3-arco-de-novidades` | D21, imagem grande fora de link |
| `products-7-dois-com-galeria-de-angulos` | D21, duas fotos grandes de produto fora de link |
| `products-9-grade-de-tamanho` | D27, `text-shadow` |
| `reviews-1-depoimento-com-credencial` | D26, texto de 10px |
| `reviews-8-ugc-de-comunidade` | D21, fotos de UGC fora de link |

8 de 44. Todas em M: avisam, não bloqueiam.

**Achado fora do escopo, registrado.** Rodando `produzir_lote.py --loja
blue-wolf --limite 4`, duas peças acusam R09 (rolagem horizontal no
celular). A causa é um link de variante do vault com `width:525px` e texto
que não quebra, que trava a tabela em 600px. O R09 é o mesmo antes e
depois da correção da casca: não foi introduzido aqui.

**O que não veio.** O zip de skills da Scalero (email-design-qa,
personalization-spec) não estava acessível pelo ambiente; quando chegar,
entra pela mesma régua de licença.

## O que continua aberto

Da lista que sugeri, três não foram feitas:

| # | O quê | Por quê |
|---|---|---|
| 3 | Nada volta da realidade | Esforço G, e depende de decidir o acoplamento com o Omnisend da conta |
| 4 | `evals/casos/` vazio | Depende de você escolher os e-mails aprovados |
| 6 | `shared/` com 1.555 linhas | Esforço P, mas mexe em como toda skill carrega contexto |

A 3 continua sendo a de maior retorno: é o que transforma a suíte em algo
que melhora sozinho, em vez de melhorar quando alguém mexe.
