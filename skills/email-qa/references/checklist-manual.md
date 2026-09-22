# Checklist manual: Q01 a Q12

O que o lint não consegue ver. Rode depois de `lint_email.py` e
`lint_copy.py` passarem sem B.

Antes de reprovar qualquer item, leia `shared/calibracao.md`.

---

## Q01. Render real nos três clientes (B se quebrar estrutura)

Outlook (Windows, Word engine), Gmail (web e app) e Apple Mail (iOS).

O que quebra com mais frequência, na ordem:

1. Coluna que empilha errado no Outlook, quase sempre por espaco entre
   tags ou por `vertical-align` faltando.
2. Botao sem VML: no Outlook vira link de texto.
3. Largura que estoura os 600px por causa de `padding` somado a `width`.
4. Imagem sem `display:block`, que ganha um vao de 3px embaixo.

Não aprove por captura de uma ferramenta só. Duas fontes, ou marque como
`nao verificado`.

## Q02. Dark mode nos três clientes (B se sumir conteudo)

O CSS estar certo não e prova. Force o modo escuro e olhe.

- Logo preto em fundo transparente: some. Precisa de versão clara.
- `#000` puro: o Apple Mail inverte de um jeito, o Gmail de outro. O
  padrão da casa e `#121212` (D19).
- Texto em imagem não inverte, texto vivo inverte. A peca fica com dois
  registros na mesma dobra.
- Borda definida só por cor clara desaparece.

Confira as duas metas de `color-scheme` antes de julgar: sem elas, o
cliente aplica inversao própria e o resultado não e o que o CSS pediu.

## Q03. Alt descritivo, não só presente (A)

O lint checa se existe. Aqui se checa se serve.

Teste: leia **só** os alts, na ordem, sem ver a peca. A oferta e a
condição aparecem? Se não, o alt e decorativo disfarcado.

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

Compare com a convenção da loja. Divergência de `utm_campaign` entre
blocos do mesmo e-mail quebra o relatorio depois.

## Q06. Merge tag testada vazia (B, e C47)

Preview com o campo vazio, não com o campo preenchido.

- `Oi {{nome}}, ...` com nome vazio vira `Oi , ...`. Reprova.
- A frase precisa ler bem sem o nome.

O mecanismo de valor padrão no Omnisend esta em aberto (T1 em
`skills/email-flows/references/equivalencia-klaviyo-omnisend.md`).
Enquanto estiver, a regra e a frase funcionar com o campo vazio.

## Q07. Descadastro visível e funcional (B, conformidade)

- Ache no **render**, não no código.
- Abaixo do corte do Gmail não conta como visível.
- Clique e confirme que a página abre.

## Q08. Endereco fisico do remetente (B, conformidade)

Exigencia de e-mail comercial. Ausencia reprova.

## Q09. Cupom no idioma da loja e valido (B, e C04)

- Idioma: `PEDIDO18` em loja inglesa reprova.
- Validade: confira no admin do Shopify. Cupom que a peca anuncia e o
  admin não tem e o pior defeito possível, porque só aparece para o
  cliente final.

## Q10. Prazo bate com o cupom real (B, e C06)

A peca diz "até domingo" e o cupom expira sabado? Reprova. Urgência que
não corresponde ao dado e C06.

## Q11. Acima da dobra sem imagem (A)

Desligue as imagens. O que sobra diz a oferta e da o próximo passo?

E o cenario real de boa parte da base, e e o que o resumidor de IA do
Gmail e do Apple Mail enxerga.

## Q12. Estrutura corresponde a uma var2 (A, P08)

Compare a ordem das seções com `vault/estruturas/<flow>/`. Peca cuja
estrutura não corresponde a nenhuma referência foi escrita antes de
decidir a estrutura, que e P08.

Se a estrutura for deliberada e nova, ela deveria ter virado nota no
vault. Registre como achado de processo, não reprove a peca sozinha por
isso.
