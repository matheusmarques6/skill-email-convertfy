# Arsenal e montador: o que foi construído

Fecha a lacuna 20 de `docs/lacunas-priorizadas.md` (`header` e `cta` com
zero variantes) e tira a peça do estado anêmico que o teste da Fase 5
apontou.

## O que entrou no arsenal

Só o que o `README.md` da pasta permite: seção **sem** variante no vault.

| Arquivo | Seção | Situação |
|---|---|---|
| `blocos/header/header-1-wordmark-centralizado.html` | header | proposta |
| `blocos/header/header-2-wordmark-com-barra-de-aviso.html` | header | proposta |
| `blocos/cta/cta-1-botao-isolado.html` | cta | proposta |
| `blocos/cta/cta-2-botao-com-cupom.html` | cta | proposta |

Mais quatro fragmentos técnicos: `casca-600`, `preheader`,
`head-dark-mode`, `rodape-legal`.

`manifesto.json` tem os 4 blocos, os 4 fragmentos e **44 ponteiros com
md5 para o HTML do vault**, que é como o README manda referenciar seção
que já tem variante.

## O montador não copia o vault

`scripts/montador.py` lê `vault/componentes/_html/<slug>.html` **em tempo
de execução**, pelo symlink, e monta a seção em memória. Nenhuma cópia é
gravada. Isso respeita a regra do CLAUDE.md e do README do arsenal.

Ordem de montagem:

```
casca-600
  header    arsenal
  hero      título da peça
  offer     oferta na primeira dobra, como a carteira manda
  cta       arsenal, com cupom quando o brief traz código
  body      parágrafos da copy
  products  vault, lido em tempo de execução
  rodapé    fragmento
```

Seção sem variante resolvida **não é inventada**: sai como lacuna no
relatório e a peça vai sem vitrine.

## Três bugs que só o render pegou

Nenhum deles tem marca no HTML, e o lint estático passou em todos.

### 1. Peça renderizando duplicada, com tabelas em cascata

O comentário de cabeçalho de cada bloco **documenta os slots**, e por isso
contém os nomes deles: `Slots: LANG, TITULO, BLOCOS`. A substituição
injetava o conteúdo inteiro **dentro do comentário**, e o `-->` fechava no
meio do HTML.

Sintoma: a peça renderizava duas vezes, com a altura dobrada (3.564 px
onde deviam ser 1.928) e as tabelas encaixadas em cascata.

Correção: tirar o cabeçalho **antes** da substituição, não depois.

### 2. Fatiar a seção do vault por `<tr>` destruía o encaixe

`re.findall(r"<tr[^>]*>.*?</tr>")` casa os `<tr>` aninhados das tabelas
internas. O resultado era HTML com encaixe quebrado.

Correção: a seção inteira entra dentro de **uma** célula, preservando a
estrutura de tabela que o vault já validou.

### 3. Imagem quebrada por slot não preenchido

O vault tem 120 nomes de slot diferentes (`URL_FOTO_1`,
`URL_COMPOSICAO_PRODUTO_1`, ...). Listar token por token não escala.

Correção: qualquer `src` que seja um token em CAIXA_ALTA vira placeholder
neutro, que é o que o design system da marca já manda enquanto não há
foto real. De 4 imagens quebradas para **0** nas 5 peças.

## O que o lote de 5 dá hoje

| Peça | Altura | Peso | Imagens quebradas | Rola no mobile |
|---|---|---|---|---|
| Quer jogar um jogo? | 1.928 px | 28 KB | 0 | **sim** |
| Reativação 1 | 900 px | 8 KB | 0 | não |
| Seu convite para o 10.10 | 2.126 px | 31 KB | 0 | **sim** |
| Qual dos nota 10 | 900 px | 10 KB | 0 | não |
| A votação está apertada | 900 px | 11 KB | 0 | não |

As duas que rolam são as que usam seção do vault. **O defeito é do vault**,
não do montador: ver `docs/pesquisa/vault-correcoes.md`, VC07.

## O que ainda reprova as 5

Nenhuma mudou de status, e o motivo continua correto:

1. **`E_PLACEHOLDER`**, em todas. Os briefs trazem `[Gerente]` e `[Loja]`,
   e a ficha não tem endereço físico. Preencher seria C02 e P02.
2. **R09** nas duas com vitrine, pelo VC07.
3. **`C02`** em uma, número sem origem no brief.

## O que ficou para a próxima rodada

1. **Slots de produto não são preenchidos.** A vitrine mostra
   `PRODUCT NAME 1` e `SECTION TITLE 1`, que são o texto de exemplo do
   vault. Falta ligar o catálogo real da loja.
2. **Dois CTAs na peça** quando a seção do vault traz o próprio botão.
   É C44, e o montador não deduplica.
3. **Duplicação de headline**: o assunto aparece no topo e de novo no
   corpo, porque o brief tem os dois campos.
