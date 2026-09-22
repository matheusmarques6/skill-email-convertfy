---
# ============================================================
# CONTRATO (lido por código: lint_copy.py, lint_email.py, gates)
# Campo desconhecido fica `null`. Nunca preencher por inferência:
# `null` faz o gate perguntar; um chute faz o gate mentir.
# ============================================================
tipo: marca
slug: nome-da-loja            # kebab-case, ASCII, igual ao nome do arquivo
loja: "Nome Da Loja"          # como a loja se escreve
status: rascunho              # rascunho | aprovada | superada
atualizado_em: 2026-01-01
revisado_por: null            # quem da Convertfy validou com o cliente

# --- idioma e mercado (C04: cupom e CTA no idioma da loja) ---
idioma: pt-BR                 # pt-BR | en | es
mercado: BR                   # BR | US | outro
moeda: BRL
esp: omnisend                 # omnisend | klaviyo
plataforma: shopify

# --- tipografia (nomenclatura obrigatória do CLAUDE.md) ---
tipografia_principal: null    # ex.: "Inter Tight"; null = usar a fallback
tipografia_principal_fallback: Arial
fonte_secundaria: null        # ex.: "Georgia"; nomear sempre, mesmo se igual
fonte_secundaria_fallback: Georgia

# --- cor (o default é neutro; ver "Cor" no corpo) ---
usa_cor_de_marca: false       # true SÓ quando o brief da loja exigir
cor_primaria: null            # hex; só preenchido quando usa_cor_de_marca: true
cor_secundaria: null          # hex
cor_de_fundo: "#FFFFFF"       # regra fixa da casa; trocar exige nota no corpo
cor_de_texto: "#000000"
acento_permitido_em: [botao, link, detalhe]   # nunca fundo de seção inteira

# --- oferta padrão ---
oferta_padrao_tipo: null      # percentual | valor | frete | brinde | nenhum
oferta_padrao_valor: null     # ex.: 10 (para 10%) ou 30 (para R$30)
oferta_padrao_minimo: null    # valor mínimo de carrinho, se houver
cupom_padrao: null            # código, no idioma da loja (C04)
desconto_automatico: false    # true = sem código; não convive com cupom
prazo_padrao: null            # ex.: "7 dias após o opt-in"; null = sem prazo real

# --- copy ---
emoji_permitido: false        # true libera no máximo 1 no assunto (C31)
emoji_no_corpo: false
exclamacao_maxima: 1          # por e-mail (C30)
palavras_proibidas: []        # lista da marca, além do léxico global
termos_obrigatorios: []       # marca registrada, nome de linha, grafia fixa
tratamento: voce              # voce | tu | vos | neutro
merge_tags_com_fallback: []   # ex.: ["{{first_name|Oi}}"] (C47)

# --- fatos que o lint pode conferir ---
brief_numbers: []             # todo número permitido na copy (C02). Vazio = nenhum
reviews_disponiveis: null     # true | false | null
review_com_nome: null
foto_do_depoente: null
politica_de_troca_publicada: null
prazo_de_entrega_declarado: null

# --- restrição legal do nicho ---
nicho: null                   # ex.: suplementos, joias, cosmético, pet
restricoes_legais: []         # slugs; a prosa explica cada uma
claims_proibidos: []          # afirmações que o nicho não permite
---

# Ficha de marca: <Nome Da Loja>

Uma ficha por loja em `marcas/<slug>.md`. Copie este arquivo, preencha, e
deixe `null` no que não souber. **A ficha é pré-requisito de geração**
(P01): sem ela, o agente não escreve copy.

Regra de ouro herdada do vault: **o frontmatter é contrato e é aplicado por
código; este corpo é julgamento e é lido por LLM.** Nunca escreva aqui uma
regra dura que o frontmatter não espelhe, e nunca escreva prosa dentro de um
campo do frontmatter.

Precedência: **brief da loja > vault > CLAUDE.md > skill > vendor.** Esta
ficha é o brief da loja. Quando ela contradiz o vault, ela vence, e quem
gerou a peça diz qual fonte perdeu.

## Tom

Como a marca fala, em duas ou três frases. Descreva pelo comportamento, não
por adjetivo: o que ela faz com a frase, não como ela se sente. Bom:
"explica a mecânica da oferta e para; não adjetiva produto". Ruim:
"moderna, jovem e autêntica" (isso é tríade ornamental, o vício C11).

Se a marca já tem peças aprovadas, cite duas frases reais dela aqui. Vale
mais que qualquer descrição.

## Idioma

O idioma do frontmatter vale para **todos** os campos: assunto, preheader,
corpo, alt e, principalmente, o código do cupom. Cupom em idioma errado é
bloqueio de entrega (C04). Se a loja vende em dois mercados, são duas
fichas, não uma ficha bilíngue.

## Público

Quem abre. Um parágrafo: quem compra, o que já sabe da categoria, e qual é
a dúvida que essa pessoa traz antes de confiar. Essa dúvida é o que o vault
chama de objeção dominante, e é o que decide a estrutura do welcome 1.

Não invente segmento. Se a loja não sabe quem compra, escreva "n/d" e trate
como pergunta ao cliente.

## Oferta padrão

O que a loja oferece por default no welcome e em campanha: tipo, valor,
mínimo, código, prazo. Se o prazo do frontmatter é `null`, a copy usa no
máximo "por tempo limitado", nunca hora fechada (regra 3 do flow de welcome
no vault, e V29 em `docs/pesquisa/vault-vicios.md`).

Registre também o que **não** existe: sem estoque integrado, sem cap de
cupom, sem contagem real de uso. Isso mata as estruturas de escassez antes
de alguém propor uma (V19, V31).

## Tipografia principal e fonte secundária

Use exatamente estes dois nomes, aqui e em qualquer spec de peça. Não
escreva "fonte primária", "heading font" nem "display".

- **Tipografia principal:** onde entra (título, corpo, botão) e qual é a
  fallback real em e-mail. A maioria dos clientes cai na fallback, então a
  fonte da marca vive nas imagens e nos títulos renderizados.
- **Fonte secundária:** nomeie sempre, mesmo quando for a mesma. Diga onde
  ela aparece e onde não aparece.

## Cor primária e cor secundária

**O default da casa é neutro: fundo branco, texto preto, sem paleta
autoral.** O agente não escolhe paleta.

Cor de marca só entra quando **este brief exigir**, com
`usa_cor_de_marca: true` e os hex preenchidos. Mesmo então ela entra em
**acento**: botão, link, detalhe. Nunca como fundo de seção inteira, nunca
em texto corrido.

Se a loja tem paleta e mesmo assim as peças devem sair neutras, deixe
`usa_cor_de_marca: false` e registre o motivo aqui. Um campo que contradiz
a prosa é bug: o código lê o campo.

## Uso de emoji

`emoji_permitido: false` é o default. Ligue só se a marca já usa emoji em
peça aprovada, e diga onde: assunto, nunca corpo, é o caso comum. Emoji
decorativo no corpo é C31, e no começo de linha é sinal de peça gerada.

## Palavras proibidas da marca

Lista específica desta loja, além do léxico global de
`shared/lexico/`. Entram aqui três coisas:

1. **Clichê da categoria** que a marca não usa ("brilhe", "sua história",
   "atemporal" em joias; "ritual", "autocuidado" em beleza).
2. **Termo jurídico ou técnico errado** para o nicho (ver a seção abaixo).
3. **Palavra que o cliente já reprovou.** Quando souber, anote a data e
   quem reprovou: é a evidência mais forte que a ficha pode carregar.

Para cada palavra da lista, escreva em uma linha o que se usa no lugar. Uma
proibição sem substituto vira rodeio, e rodeio é outro vício.

## Restrições legais do nicho

O que o nicho proíbe afirmar, e o que ele obriga a escrever. Uma linha por
restrição, com a fonte quando houver.

Exemplos de onde isto morde:

- **Suplemento e cosmético:** promessa de cura, tratamento ou resultado
  terapêutico; antes e depois; percentual de eficácia sem estudo.
- **Qualquer nicho, Brasil:** publicidade enganosa é vedada (CDC art. 37).
  Prazo, estoque e desconto anunciados precisam existir.
- **Qualquer nicho, envio em massa:** assunto que simula transação ou
  resposta é proibido e é risco regulatório (C03). Vale para "RE:",
  "Aviso:", "Seu pedido foi confirmado".
- **Descadastro:** link presente e funcional, acima do corte de 102 KB do
  Gmail.

Se a loja opera fora do Brasil, registre a regra do mercado dela, não a
daqui.

## O que esta ficha não resolve

- Ela não decide estrutura. Estrutura vem do vault (intenção e estrutura de
  referência).
- Ela não substitui o brief da campanha: oferta específica, prazo específico
  e produto específico vêm no pedido, não aqui.
- Campo `null` não é permissão. É pergunta pendente, e gate que depende dele
  reprova até a resposta chegar.
