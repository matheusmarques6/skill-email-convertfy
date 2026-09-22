# Índice do vault: intenções, estruturas e aprendizados

Levantamento de leitura do `vault/` (symlink somente leitura para o Obsidian
da Convertfy). Uma linha por nota, com o que o frontmatter declara. Campo que
a nota não tem aparece como `n/d`, nunca preenchido por inferência.

Lido em 22/09/2026. Cobre `vault/intencoes/`, `vault/estruturas/` e
`vault/aprendizados/`. As notas de componente (`vault/componentes/`) estão
fora deste índice: o mapa delas é `vault/componentes/_catalogo.md` e o
glossário reverso é `shared/vocabulario-arsenal.md`.

**Totais:** 15 intenções, 8 estruturas, 18 aprendizados. 41 notas.

---

## 1. Intenções (var1)

`vault/intencoes/<flow>/`. O contrato do toque: modo, número de objeções,
riscos elegíveis, aliviadores, trabalhos fixos e proibições.

| Caminho | Flow | Toque | Status |
|---|---|---|---|
| `vault/intencoes/welcome/_flow.md` | welcome | escopo de flow (8 toques) | aprovada |
| `vault/intencoes/welcome/_progressao.md` | welcome | cobre 1 a 8 (camada descritiva) | aprovada |
| `vault/intencoes/welcome/welcome-1.md` | welcome | 1 | aprovada |
| `vault/intencoes/welcome/welcome-2.md` | welcome | 2 | aprovada |
| `vault/intencoes/welcome/welcome-3.md` | welcome | 3 | aprovada |
| `vault/intencoes/welcome/welcome-4.md` | welcome | 4 | aprovada |
| `vault/intencoes/welcome/welcome-5.md` | welcome | 5 | aprovada |
| `vault/intencoes/welcome/welcome-6.md` | welcome | 6 | aprovada |
| `vault/intencoes/welcome/welcome-7.md` | welcome | 7 | aprovada |
| `vault/intencoes/welcome/welcome-8.md` | welcome | 8 | aprovada |
| `vault/intencoes/abandoned_cart/_flow.md` | abandoned_cart | escopo de flow (8 toques) | rascunho |
| `vault/intencoes/abandoned_cart/abandoned_cart-1.md` | abandoned_cart | 1 | rascunho |
| `vault/intencoes/abandoned_cart/abandoned_cart-2.md` | abandoned_cart | 2 | rascunho |
| `vault/intencoes/abandoned_cart/abandoned_cart-3.md` | abandoned_cart | 3 | rascunho |
| `vault/intencoes/abandoned_cart/abandoned_cart-4.md` | abandoned_cart | 4 | rascunho |

**Contagem por flow:** welcome 10 (8 toques + `_flow` + `_progressao`),
abandoned_cart 5 (4 toques + `_flow`).

**Lacunas visíveis nesta camada**

- `abandoned_cart` declara 8 toques no `_flow`, e só os toques 1 a 4 têm
  nota. Os toques 5 a 8 (incentivo, last chance, sino, epílogo) existem como
  linha na tabela do `_flow` e não como contrato.
- Todo o `abandoned_cart` está em `status: rascunho`. Pelo
  `_PADRAO-DO-VAULT` A3, só `aprovada` é servida a agente, então hoje o
  único flow gerável é `welcome` (o próprio `_flow` do welcome diz isso:
  "flows sem intenção não geram").
- Nenhum outro flow tem camada de intenção. `browse_abandonment`,
  `post_purchase`, campanha e sazonal existem como valor do eixo `momento`,
  sem contrato.

---

## 2. Estruturas de referência (var2)

`vault/estruturas/<flow>/`. Peça real catalogada: quais seções, em que
ordem, com que papel. Mostra o que existe, não prova o que funciona.

| Caminho | Flow | Toque | Loja | Seções | Status |
|---|---|---|---|---|---|
| `vault/estruturas/welcome/avelmore-inspecao-antecipada.md` | welcome | 1 | avelmore | header, hero, body, body, products, cta, reviews, footer | aprovada |
| `vault/estruturas/welcome/avelmore-deadline-objecao.md` | welcome | 2 | avelmore | header, hero, body, offer, products, footer | aprovada |
| `vault/estruturas/welcome/avelmore-mecanismo-e-origem.md` | welcome | 3 | avelmore | header, body, body, products, footer | aprovada |
| `vault/estruturas/welcome/avelmore-prova-social-cirurgica.md` | welcome | 4 | avelmore | header, hero, body, reviews, cta, footer | aprovada |
| `vault/estruturas/welcome/medicube-comparacao-categoria.md` | welcome | 5 | medicube | header, body, products, footer | aprovada |
| `vault/estruturas/welcome/medicube-escassez-com-prova-de-demanda.md` | welcome | 6 | medicube | hero, body, reviews, offer, footer | aprovada |
| `vault/estruturas/welcome/medicube-ultima-batida.md` | welcome | 7 | medicube | header, offer, footer | aprovada |
| `vault/estruturas/welcome/carta-plain-text-extensao.md` | welcome | 8 | carta (sem marca) | body | aprovada |

**Contagem por flow:** welcome 8, abandoned_cart 0.

**Campo `performance`:** presente e vazio nas 8. Nenhuma estrutura carrega
número de desempenho. `procedencia: nossa` nas 8; `revisado_por: Convertfy`
em 2 (inspecao-antecipada, deadline-objecao) e ausente nas outras 6.

**O que ler junto**

- Todas as 8 declaram `header` ou `cta` em alguma posição, e as duas seções
  têm zero variantes no catálogo. As próprias notas marcam esses blocos como
  "não realizável hoje", apontando para `vault/componentes/lacunas/
  header-sem-variante.md` e `cta-sem-variante.md`.
- `carta-plain-text-extensao` deixa `loja` como "carta" por não haver sinal
  de marca na peça, e a assinatura entregue é o placeholder literal.

---

## 3. Aprendizados

`vault/aprendizados/_global/` vale para todo flow; `vault/aprendizados/
welcome/` é do welcome. Todas declaram `origem_estrutura`, e é isso que as
separa de opinião.

### 3.1 Globais (cross-flow)

| Caminho | Flow | Toque (`serve_a`) | Tipo de regra | Status |
|---|---|---|---|---|
| `vault/aprendizados/_global/cada-alegacao-e-uma-promessa-operacional.md` | cross-flow | todos | restrição-dura | aprovada |
| `vault/aprendizados/_global/incentivo-precisa-existir-em-texto.md` | cross-flow | todos | restrição-dura | aprovada |
| `vault/aprendizados/_global/posicao-muda-o-efeito-do-dispositivo.md` | cross-flow | welcome 1 a 5 | preferência | aprovada |
| `vault/aprendizados/_global/quebra-de-formato-atravessa-a-cegueira.md` | cross-flow | welcome 8 | preferência | aprovada |
| `vault/aprendizados/_global/remocao-de-risco-escala-com-o-ticket.md` | cross-flow | welcome 1, 2, 3, 6 | preferência | aprovada |
| `vault/aprendizados/_global/titulos-precisam-carregar-o-argumento.md` | cross-flow | todos | preferência | aprovada |
| `vault/aprendizados/_global/um-cta-dominante-em-email-curto.md` | cross-flow | todos | preferência | aprovada |

### 3.2 Welcome

| Caminho | Flow | Toque (`serve_a`) | Tipo de regra | Status |
|---|---|---|---|---|
| `vault/aprendizados/welcome/ausencia-de-prova-social-assume-abertura.md` | welcome | 2, 3, 4 | preferência | aprovada |
| `vault/aprendizados/welcome/cadencia-decide-fechamento-ou-farsa.md` | welcome | 6, 7, 8 | restrição-dura | aprovada |
| `vault/aprendizados/welcome/cupom-repetido-precisa-de-papel.md` | welcome | 1 a 6 | preferência | aprovada |
| `vault/aprendizados/welcome/deadline-antes-do-argumento.md` | welcome | 2 | preferência | aprovada |
| `vault/aprendizados/welcome/deadline-falso-queima-o-proximo.md` | welcome | 2, 3, 6, 7, 8 | preferência | aprovada |
| `vault/aprendizados/welcome/depoimento-nao-repete-pessoa.md` | welcome | 1, 4, 6 | preferência | aprovada |
| `vault/aprendizados/welcome/extensao-declarada-quatro-condicoes.md` | welcome | 8 | restrição-dura | aprovada |
| `vault/aprendizados/welcome/numeros-de-escassez-precisam-de-backing.md` | welcome | 6, 7 | restrição-dura | aprovada |
| `vault/aprendizados/welcome/prazo-vago-enfraquece-a-extensao.md` | welcome | 8 | preferência | aprovada |
| `vault/aprendizados/welcome/prova-de-terceiro-antes-do-cta.md` | welcome | 1, 4, 6 | preferência | aprovada |
| `vault/aprendizados/welcome/saida-rapida-no-primeiro-terco.md` | welcome | 3 | preferência | aprovada |

**Contagem por flow:** `_global` 7 (todas com `aplica_a` citando welcome,
abandoned_cart, browse_abandonment e post_purchase), welcome 11.

**Distribuição por `tipo_regra`:** 5 `restricao-dura`, 13 `preferencia`.
Pelo `_PADRAO-DO-VAULT` A10, `restricao-dura` só é aceita quando a regra
também está expressa em frontmatter de variante, eixo ou convivência. Das 5,
duas foram promovidas a doutrina do flow (`deadline-falso-queima-o-proximo`
virou regra transversal 4 e `extensao-declarada-quatro-condicoes` virou
regra transversal 5 em `intencoes/welcome/_flow.md`); as outras três
(`cada-alegacao-e-uma-promessa-operacional`,
`incentivo-precisa-existir-em-texto`, `cadencia-decide-fechamento-ou-farsa`)
não têm espelho em frontmatter de variante, e isso é o que este repo precisa
cobrir com lint, não com prosa.

**Estrutura de origem, por contagem:** avelmore-deadline-objecao 5,
avelmore-inspecao-antecipada 4, carta-plain-text-extensao 3,
medicube-comparação-categoria 2, avelmore-mecanismo-e-origem 2,
avelmore-prova-social-cirurgica 1, medicube-escassez-com-prova-de-demanda 1,
medicube-última-batida 1. As 8 estruturas geraram aprendizado; nenhuma ficou
sem rendimento.

---

## 4. Observações de leitura (não são conteúdo do vault)

Anotado aqui porque afeta quem for consumir o vault deste repo. Nada disto
foi alterado no vault.

1. **O catálogo está atrasado em relação às notas de variante.**
   `vault/componentes/_catalogo.md` (gerado em 14/09) lista 44 variantes e
   `vault/componentes/_html/` tem 44 arquivos, mas
   `vault/componentes/variantes/` tem **75 notas**: body 18, hero 18,
   products 16, reviews 10, offer 9, footer 4. As 31 notas a mais vieram da
   catalogação de 19/09 (`vault/componentes/_relatorio-catalogacao-2026-09-19.md`,
   que declara 32 notas novas, uma delas substituindo uma nota-esqueleto).
   O `CLAUDE.md` deste repo diz "44 variantes" e, na mesma frase, lista a
   distribuição que soma 75: os dois números vieram de momentos diferentes.
2. **As notas de seção também estão atrasadas.** `secoes/_reviews.md` diz 7
   variantes; a pasta tem 10. `secoes/_body.md` diz 9; a pasta tem 18.
   A chave de desempate de cada seção só cobre as variantes antigas.
3. **Contrato novo de variante, não documentado no padrão.** As 32 notas de
   19/09 usam `aliviador` e `profundidade`, não usam `ativa`, `momento` nem
   `momento_vetado` ("momento aposentado", diz o relatório) e não têm HTML em
   `_html/`. O `_PADRAO-DO-VAULT` A4 ainda descreve o contrato antigo.
4. **12 valores de `exige` sem nota de requisito:** `oferta-bogo-real`,
   `politica-real`, `review-com-nome`, `1-produto-com-link`,
   `2-produtos-com-link`, `3-produtos-com-link`, `4-produtos-com-link`,
   `3-reviews-com-nome`, `nota-real`, `6-diferencas-defensaveis`,
   `duas-fotos-comparaveis`, `4-detalhes-verificaveis`. O próprio relatório
   de catalogação registra a pendência. Pelo protocolo, `exige` é o passo 4
   (eliminação por código), então gate sem nota é gate que não resolve.
5. **Colisão de numeração em reviews:** `reviews-8-tres-cards-com-nota` e
   `reviews-8-ugc-de-comunidade` são variantes distintas com o mesmo número.
   O relatório de 19/09 já registra colisões parecidas de `nome_no_banco`
   ("body 21" em duas seções) e manda endereçar por `variant_id`.
