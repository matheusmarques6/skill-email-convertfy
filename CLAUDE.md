# Suite de skills de e-mail marketing (Convertfy)

## Proposito

Conjunto de skills que produzem e-mail marketing para e-commerce em escala
na Convertfy: agencia com 250+ lojas Shopify, ESP principal Omnisend,
secundario Klaviyo.

O objetivo central e **eliminar vicios de IA em copy e design de e-mail**.
Uma peca gerada aqui precisa passar por humano sem parecer gerada: copy que
soa de loja, nao de assistente; layout que soa de template de producao, nao
de demonstracao de capacidade. Quando uma skill tiver que escolher entre
"impressionante" e "indistinguivel de uma peca real", escolhe a segunda.

O repo serve tres consumidores: o agente que monta a peca, o humano que
revisa, e as evals que medem se o vicio voltou.

## Fonte de verdade: o vault

`vault/` e um symlink para `Admin Convertfy/Emails` do Obsidian da
Convertfy (repo `matheusmarques6/all-for-eficiencia`, sincronizado por Git).

**Somente leitura. Nunca copie, nunca edite, nunca gere arquivo dentro
dele por aqui.** Mudanca de conteudo do vault acontece no Obsidian, nao
neste repo. O symlink esta no `.gitignore`: o vault nao e versionado aqui.

O vault ja tem protocolo proprio e manda sobre qualquer heuristica que uma
skill invente:

- `vault/_INDEX.md` comeca aqui
- `vault/componentes/_protocolo-de-selecao.md` as regras de escolha de
  variante, em ordem (9 passos, elimina antes de rankear)
- `vault/componentes/_julgamento.md` o que nunca fazemos e quando recusar
- `vault/componentes/_catalogo.md` as variantes em tabela unica (gerado)
- `vault/_PADRAO-DO-VAULT.md` como as notas sao escritas

Regra de ouro herdada do vault: frontmatter e contrato aplicado por codigo,
corpo e julgamento lido por LLM. Nunca escreva regra dura so em prosa.

## Hierarquia de fontes

Sete niveis. Quando duas fontes discordam, vence a de numero menor.

| # | Fonte | Onde |
|---|---|---|
| **1** | **Regras legais e eticas, inegociaveis** | C02, C06 e a parte de simulacao do C03 |
| **2** | **Dados de desempenho da propria carteira** | `fontes/BFCM-2026-Convertfy/09_Dados/`, `10_Documentos/`, `08_Skill/`, `05_Modelos_validados/ranking-de-modelos.md`, resumidos em `docs/dados/` |
| **3** | **Vault canonico** | `vault-repo/` (o symlink `vault/` e a parte de e-mail) |
| **4** | **Regras fixas da Convertfy** | este CLAUDE.md: layout neutro, 600px, sem travessao, copy curta |
| **5** | **Evidencia publicada, so forca forte ou moderada** | `docs/pesquisa/evidencias-publicadas.md` |
| **6** | **Catalogo de vicios** | `docs/pesquisa/pesquisa-vicios-ia-email.md` |
| **7** | **Referencia externa** | `vendor/` |

Alem desses, o **brief da loja** decide o que e especifico daquela loja
(oferta, produto, prazo, cor da marca). Ele nao revoga o nivel 1.

### Nivel 1: o que nenhum dado revoga

Vale mesmo que um numero de desempenho diga o contrario:

- **C02.** Nao inventar numero, estoque, avaliacao, contador ou
  depoimento. Sem o dado real da loja, o bloco sai.
- **C06.** Nao criar urgencia falsa. Contador so se for real.
- **C03, parte de simulacao.** Nao simular pedido, resposta ou
  encaminhamento que nao existe.

Um assunto que vende mais sendo enganoso continua proibido. Desempenho
nao e argumento contra o nivel 1.

### Quando o nivel 2 contradiz os niveis 4 a 7

**O dado ganha, e a regra e refinada, nao apagada.** A regra recebe a
condicao que o dado mostrou, e a mudanca fica registrada em
`docs/reconciliacao-regras-dados.md` com o numero e a fonte.

Refinar significa estreitar ou abrir o escopo com uma condicao nomeada.
Nunca significa remover a regra e deixar o campo livre.

### Indice 1

A unidade de comparacao dos dados de nivel 2 e o **indice**: receita por
mil da campanha dividida pela receita por mil media daquela loja no
trimestre. Indice 1 e a media da propria loja, indice 2 e o dobro. Serve
para comparar lojas de tamanho e moeda diferentes.

Precedencia resumida:
**nivel 1 > brief da loja > dados da carteira > vault > este CLAUDE.md >
evidencia publicada > catalogo > vendor.**

## Regras fixas da Convertfy

Valem para toda skill deste repo, sem excecao silenciosa. Skill que precise
divergir declara a divergencia no proprio SKILL.md.

### Layout

- Fundo branco, texto preto. **Sem paleta autoral.**
- Cor da marca entra **somente quando o brief da loja exigir**, e mesmo
  assim em acento (botao, link, detalhe), nunca como fundo de secao inteira.
- O agente nao escolhe paleta. Se o brief nao deu cor, a peca fica neutra.

### Tecnica

- Container de **600px**.
- Tabelas com `role="presentation"`.
- **Estilos inline.** Nada de `<style>` como unica fonte de estilo.
- Botao **bulletproof** (VML para Outlook).
- Compativel com **Outlook** (Word rendering engine).
- **Seguro para dark mode**: nada que suma ou inverta errado quando o
  cliente forcar inversao.

### Copy

- **Curta, generica e realista.** Frase de loja, nao frase de agencia
  premiada.
- **Proibido storytelling elaborado.** Sem jornada do heroi, sem abertura
  cinematografica, sem "imagine que...".
- **Proibido travessao (—) em qualquer copy.** Use virgula, ponto, dois
  pontos ou parenteses. Esse e o vicio de IA mais facil de detectar e o
  mais caro: e o primeiro item de toda eval.
- Sem superlativo vazio, sem tricolon ("mais rapido, mais leve, mais seu"),
  sem antitese de efeito ("nao e X, e Y"), sem emoji decorativo.

### Specs

Nomenclatura obrigatoria ao escrever uma spec de peca:

- **tipografia principal** (nao "fonte primaria", nao "heading font")
- **fonte secundaria** nomeada explicitamente
- **cor primaria**
- **cor secundaria**

## Taxonomia: as 8 categorias de bloco

Todo bloco pertence a exatamente uma destas. Mesmos nomes do vault, em
`vault/componentes/secoes/_<categoria>.md`.

| Categoria | Papel |
|---|---|
| `header` | Topo: logo, navegacao minima, barra de aviso |
| `hero` | Primeira dobra: promessa e imagem de abertura |
| `body` | Corpo argumentativo: texto, beneficio, explicacao |
| `products` | Vitrine: grade ou carrossel de produto com preco |
| `reviews` | Prova social: avaliacao, nota, depoimento, UGC |
| `cta` | Chamada isolada: botao como bloco proprio |
| `offer` | Oferta: cupom, desconto, prazo, condicao |
| `footer` | Rodape: legal, descadastro, endereco, social |

Cobertura atual do vault: **75 notas de variante** em disco (`body` 18,
`hero` 18, `products` 16, `reviews` 10, `offer` 9, `footer` 4), e
**`header` e `cta` com zero variantes**. Zero candidata nao e erro:
declare a lacuna conforme `vault/componentes/lacunas/`, nao invente
variante para preencher.

Atencao ao descompasso: das 75 notas, so **44 estao em `_catalogo.md` e
tem HTML em `_html/`**. As outras 31 vieram da catalogacao de 19/09, usam
contrato novo (`aliviador`, `profundidade`, sem `ativa`, sem `momento`) e
ainda nao foram geradas no catalogo. O `_INDEX.md` e o `_PADRAO-DO-VAULT`
do vault ainda descrevem o contrato antigo. Skill que dependa do catalogo
alcanca 44; skill que leia a pasta alcanca 75. Declare qual das duas voce
usa. Ver `docs/pesquisa/vault-vicios.md`.

## Licenca: vendor/ e somente leitura

`vendor/` guarda 17 repos de referencia clonados com `--depth 1`. Esta no
`.gitignore` e **nunca e versionado**.

Regras:

1. **Nunca edite nada dentro de `vendor/`.**
2. **Nunca copie codigo ou texto de `vendor/` para `skills/`.** Tudo que
   reaproveitarmos e **reescrito** com nossas palavras e nossas regras.
3. **Todo reaproveitamento recebe credito em `NOTICE.md`**, na entrada do
   repo de origem, dizendo o que foi absorvido.

Licencas mapeadas:

- `pbakaus/impeccable` e **Apache 2.0** e **exige NOTICE**. Qualquer
  derivacao obriga entrada em `NOTICE.md`.
- Quinze repos sao **MIT**: taste-skill, skills (emilkowalski),
  email-marketing-bible, chappie, email-campaign-skill,
  skill-email-html-mjml, email-html-qa-skill, prescott-amelia-agents,
  claude-marketing, klaviyo-audit-agent-skill, humanizer (blader),
  Deslop-ptBR, humanizer-pt-br, humanizer-br, slop-detect.
- `Join-Ground-AI/Ground-Retention-Skills` **nao declara licenca**. Sem
  licenca nao ha permissao: use apenas como leitura para entender o
  problema, nunca como base de derivacao.

Ver `NOTICE.md` para a tabela completa e para registrar creditos.

## Convencao de skills

- Uma skill por pasta: `skills/<nome>/SKILL.md`.
- **Maximo 500 linhas por SKILL.md.** E limite duro, nao alvo.
- Detalhe que nao couber vai para `skills/<nome>/references/<tema>.md`,
  carregado sob demanda. O SKILL.md aponta, nao transcreve.
- Frontmatter com `name` e `description`. A `description` diz **quando**
  acionar, nao o que a skill acha de si mesma.

Estrutura do repo:

| Pasta | Conteudo |
|---|---|
| `skills/` | As skills, uma pasta cada |
| `shared/` | Regras e trechos usados por mais de uma skill |
| `marcas/` | Brief por loja: cor, tipografia, tom, restricao |
| `assets/arsenal/` | Blocos HTML prontos e validados |
| `scripts/` | Validadores, linters de copy, build |
| `evals/casos/` | Casos bons: entrada esperada e saida aceita |
| `evals/ruins/` | Casos ruins: pecas com vicio, para o linter pegar |
| `docs/` | Documentacao interna |
| `fontes/` | Pacotes de origem versionados (.md, .csv, .json) |
| `vault-repo/` | Clone do vault completo, somente leitura, fora do git |
| `vendor/` | Referencia externa, somente leitura, fora do git |
| `.claude-plugin/` | Manifesto do plugin |
