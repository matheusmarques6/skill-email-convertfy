# Checklist manual: Q01 a Q12

O que o lint nao consegue ver. Rode depois de `lint_email.py` e
`lint_copy.py` passarem sem B.

Antes de reprovar qualquer item, leia `shared/calibracao.md`.

---

## Q01. Render real nos tres clientes (B se quebrar estrutura)

Outlook (Windows, Word engine), Gmail (web e app) e Apple Mail (iOS).

O que quebra com mais frequencia, na ordem:

1. Coluna que empilha errado no Outlook, quase sempre por espaco entre
   tags ou por `vertical-align` faltando.
2. Botao sem VML: no Outlook vira link de texto.
3. Largura que estoura os 600px por causa de `padding` somado a `width`.
4. Imagem sem `display:block`, que ganha um vao de 3px embaixo.

Nao aprove por captura de uma ferramenta so. Duas fontes, ou marque como
`nao verificado`.

## Q02. Dark mode nos tres clientes (B se sumir conteudo)

O CSS estar certo nao e prova. Force o modo escuro e olhe.

- Logo preto em fundo transparente: some. Precisa de versao clara.
- `#000` puro: o Apple Mail inverte de um jeito, o Gmail de outro. O
  padrao da casa e `#121212` (D19).
- Texto em imagem nao inverte, texto vivo inverte. A peca fica com dois
  registros na mesma dobra.
- Borda definida so por cor clara desaparece.

Confira as duas metas de `color-scheme` antes de julgar: sem elas, o
cliente aplica inversao propria e o resultado nao e o que o CSS pediu.

## Q03. Alt descritivo, nao so presente (A)

O lint checa se existe. Aqui se checa se serve.

Teste: leia **so** os alts, na ordem, sem ver a peca. A oferta e a
condicao aparecem? Se nao, o alt e decorativo disfarcado.

- Ruim: `alt="banner"`, `alt="imagem 1"`, `alt="hero"`.
- Bom: `alt="10% OFF na primeira compra, codigo BEMVINDO10, ate domingo"`.
- Imagem puramente decorativa leva `alt=""` de proposito, nunca alt
  ausente.

## Q04. Todos os links (B se quebrado)

Clique em todos, inclusive logo, imagem de produto e social do rodape.

- 404 ou dominio errado reprova.
- Link de produto que cai na home reprova.
- `http://` em vez de `https://` reprova.

## Q05. UTM presente e consistente (A)

Compare com a convencao da loja. Divergencia de `utm_campaign` entre
blocos do mesmo e-mail quebra o relatorio depois.

## Q06. Merge tag testada vazia (B, e C47)

Preview com o campo vazio, nao com o campo preenchido.

- `Oi {{nome}}, ...` com nome vazio vira `Oi , ...`. Reprova.
- A frase precisa ler bem sem o nome.

O mecanismo de valor padrao no Omnisend esta em aberto (T1 em
`skills/email-flows/references/equivalencia-klaviyo-omnisend.md`).
Enquanto estiver, a regra e a frase funcionar com o campo vazio.

## Q07. Descadastro visivel e funcional (B, conformidade)

- Ache no **render**, nao no codigo.
- Abaixo do corte do Gmail nao conta como visivel.
- Clique e confirme que a pagina abre.

## Q08. Endereco fisico do remetente (B, conformidade)

Exigencia de e-mail comercial. Ausencia reprova.

## Q09. Cupom no idioma da loja e valido (B, e C04)

- Idioma: `PEDIDO18` em loja inglesa reprova.
- Validade: confira no admin do Shopify. Cupom que a peca anuncia e o
  admin nao tem e o pior defeito possivel, porque so aparece para o
  cliente final.

## Q10. Prazo bate com o cupom real (B, e C06)

A peca diz "ate domingo" e o cupom expira sabado? Reprova. Urgencia que
nao corresponde ao dado e C06.

## Q11. Acima da dobra sem imagem (A)

Desligue as imagens. O que sobra diz a oferta e da o proximo passo?

E o cenario real de boa parte da base, e e o que o resumidor de IA do
Gmail e do Apple Mail enxerga.

## Q12. Estrutura corresponde a uma var2 (A, P08)

Compare a ordem das secoes com `vault/estruturas/<flow>/`. Peca cuja
estrutura nao corresponde a nenhuma referencia foi escrita antes de
decidir a estrutura, que e P08.

Se a estrutura for deliberada e nova, ela deveria ter virado nota no
vault. Registre como achado de processo, nao reprove a peca sozinha por
isso.
