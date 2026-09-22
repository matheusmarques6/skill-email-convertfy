# Suite de skills de e-mail marketing (Convertfy)

## Proposito

Conjunto de skills que produzem e-mail marketing para e-commerce em escala
na Convertfy: agencia com 250+ lojas Shopify, ESP principal Omnisend,
secundario Klaviyo.

O objetivo central e **eliminar vícios de IA em copy e design de e-mail**.
Uma peca gerada aqui precisa passar por humano sem parecer gerada: copy que
soa de loja, não de assistente; layout que soa de template de produção, não
de demonstracao de capacidade. Quando uma skill tiver que escolher entre
"impressionante" e "indistinguivel de uma peca real", escolhe a segunda.

O repo serve três consumidores: o agente que monta a peca, o humano que
revisa, e as evals que medem se o vício voltou.

## Fonte de verdade: o vault

`vault/` e um symlink para `Admin Convertfy/Emails` do Obsidian da
Convertfy (repo `matheusmarques6/all-for-eficiencia`, sincronizado por Git).

**Somente leitura. Nunca copie, nunca edite, nunca gere arquivo dentro
dele por aqui.** Mudanca de conteudo do vault acontece no Obsidian, não
neste repo. O symlink esta no `.gitignore`: o vault não e versionado aqui.

O vault já tem protocolo próprio e manda sobre qualquer heuristica que uma
skill invente:

- `vault/_INDEX.md` comeca aqui
- `vault/componentes/_protocolo-de-selecao.md` as regras de escolha de
  variante, em ordem (9 passos, elimina antes de rankear)
- `vault/componentes/_julgamento.md` o que nunca fazemos e quando recusar
- `vault/componentes/_catalogo.md` as variantes em tabela única (gerado)
- `vault/_PADRAO-DO-VAULT.md` como as notas são escritas

Regra de ouro herdada do vault: frontmatter e contrato aplicado por código,
corpo e julgamento lido por LLM. Nunca escreva regra dura só em prosa.

## Hierarquia de fontes

Sete níveis. Quando duas fontes discordam, vence a de número menor.

| # | Fonte | Onde |
|---|---|---|
| **1** | **Regras legais e eticas, inegociaveis** | C02, C06 e a parte de simulacao do C03 |
| **2** | **Dados de desempenho da própria carteira** | `fontes/BFCM-2026-Convertfy/09_Dados/`, `10_Documentos/`, `08_Skill/`, `05_Modelos_validados/ranking-de-modelos.md`, resumidos em `docs/dados/` |
| **3** | **Vault canonico** | `vault-repo/` (o symlink `vault/` e a parte de e-mail) |
| **4** | **Regras fixas da Convertfy** | este CLAUDE.md: layout neutro, 600px, sem travessão, copy curta |
| **5** | **Evidência publicada, só força forte ou moderada** | `docs/pesquisa/evidencias-publicadas.md` |
| **6** | **Catalogo de vícios** | `docs/pesquisa/pesquisa-vicios-ia-email.md` |
| **7** | **Referência externa** | `vendor/` |

Além desses, o **brief da loja** decide o que e específico daquela loja
(oferta, produto, prazo, cor da marca). Ele não revoga o nível 1.

### Nível 1: o que nenhum dado revoga

Vale mesmo que um número de desempenho diga o contrario:

- **C02.** Não inventar número, estoque, avaliacao, contador ou
  depoimento. Sem o dado real da loja, o bloco sai.
- **C06.** Não criar urgência falsa. Contador só se for real.
- **C03, parte de simulacao.** Não simular pedido, resposta ou
  encaminhamento que não existe.

Um assunto que vende mais sendo enganoso continua proibido. Desempenho
não e argumento contra o nível 1.

### Quando o nível 2 contradiz os níveis 4 a 7

**O dado ganha, e a regra e refinada, não apagada.** A regra recebe a
condição que o dado mostrou, e a mudanca fica registrada em
`docs/reconciliacao-regras-dados.md` com o número e a fonte.

Refinar significa estreitar ou abrir o escopo com uma condição nomeada.
Nunca significa remover a regra e deixar o campo livre.

### Índice 1

A unidade de comparação dos dados de nível 2 e o **índice**: receita por
mil da campanha dividida pela receita por mil media daquela loja no
trimestre. Índice 1 e a media da própria loja, índice 2 e o dobro. Serve
para comparar lojas de tamanho e moeda diferentes.

Precedencia resumida:
**nível 1 > brief da loja > dados da carteira > vault > este CLAUDE.md >
evidência publicada > catalogo > vendor.**

## Regras fixas da Convertfy

Valem para toda skill deste repo, sem exceção silenciosa. Skill que precise
divergir declara a divergência no próprio SKILL.md.

### Layout

- Fundo branco, texto preto. **Sem paleta autoral.**
- Cor da marca entra **somente quando o brief da loja exigir**, e mesmo
  assim em acento (botao, link, detalhe), nunca como fundo de seção inteira.
- O agente não escolhe paleta. Se o brief não deu cor, a peca fica neutra.

### Técnica

- Container de **600px**.
- Tabelas com `role="presentation"`.
- **Estilos inline.** Nada de `<style>` como única fonte de estilo.
- Botao **bulletproof** (VML para Outlook).
- Compatível com **Outlook** (Word rendering engine).
- **Seguro para dark mode**: nada que suma ou inverta errado quando o
  cliente forcar inversao.

### Copy

- **Curta, genérica e realista.** Frase de loja, não frase de agencia
  premiada.
- **Proibido storytelling elaborado.** Sem jornada do heroi, sem abertura
  cinematografica, sem "imagine que...".
- **Proibido travessão (—) em qualquer copy.** Use virgula, ponto, dois
  pontos ou parenteses. Esse e o vício de IA mais fácil de detectar e o
  mais caro: e o primeiro item de toda eval.
- Sem superlativo vazio, sem tricolon ("mais rapido, mais leve, mais seu"),
  sem antitese de efeito ("não e X, e Y"), sem emoji decorativo.

### Specs

Nomenclatura obrigatória ao escrever uma spec de peca:

- **tipografia principal** (não "fonte primaria", não "heading font")
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
| `products` | Vitrine: grade ou carrossel de produto com preço |
| `reviews` | Prova social: avaliacao, nota, depoimento, UGC |
| `cta` | Chamada isolada: botao como bloco próprio |
| `offer` | Oferta: cupom, desconto, prazo, condição |
| `footer` | Rodape: legal, descadastro, endereco, social |

Cobertura atual do vault: **75 notas de variante** em disco (`body` 18,
`hero` 18, `products` 16, `reviews` 10, `offer` 9, `footer` 4), e
**`header` e `cta` com zero variantes**. Zero candidata não e erro:
declare a lacuna conforme `vault/componentes/lacunas/`, não invente
variante para preencher.

Atenção ao descompasso: das 75 notas, só **44 estao em `_catalogo.md` e
tem HTML em `_html/`**. As outras 31 vieram da catalogacao de 19/09, usam
contrato novo (`aliviador`, `profundidade`, sem `ativa`, sem `momento`) e
ainda não foram geradas no catalogo. O `_INDEX.md` e o `_PADRAO-DO-VAULT`
do vault ainda descrevem o contrato antigo. Skill que dependa do catalogo
alcanca 44; skill que leia a pasta alcanca 75. Declare qual das duas você
usa. Ver `docs/pesquisa/vault-vicios.md`.

## Licença: vendor/ e somente leitura

`vendor/` guarda 17 repos de referência clonados com `--depth 1`. Esta no
`.gitignore` e **nunca e versionado**.

Regras:

1. **Nunca edite nada dentro de `vendor/`.**
2. **Nunca copie código ou texto de `vendor/` para `skills/`.** Tudo que
   reaproveitarmos e **reescrito** com nossas palavras e nossas regras.
3. **Todo reaproveitamento recebe credito em `NOTICE.md`**, na entrada do
   repo de origem, dizendo o que foi absorvido.

Licenças mapeadas:

- `pbakaus/impeccable` e **Apache 2.0** e **exige NOTICE**. Qualquer
  derivação obriga entrada em `NOTICE.md`.
- Quinze repos são **MIT**: taste-skill, skills (emilkowalski),
  email-marketing-bible, chappie, email-campaign-skill,
  skill-email-html-mjml, email-html-qa-skill, prescott-amelia-agents,
  claude-marketing, klaviyo-audit-agent-skill, humanizer (blader),
  Deslop-ptBR, humanizer-pt-br, humanizer-br, slop-detect.
- `Join-Ground-AI/Ground-Retention-Skills` **não declara licença**. Sem
  licença não ha permissao: use apenas como leitura para entender o
  problema, nunca como base de derivação.

Ver `NOTICE.md` para a tabela completa e para registrar creditos.

## Convenção de skills

- Uma skill por pasta: `skills/<nome>/SKILL.md`.
- **Máximo 500 linhas por SKILL.md.** E limite duro, não alvo.
- Detalhe que não couber vai para `skills/<nome>/references/<tema>.md`,
  carregado sob demanda. O SKILL.md aponta, não transcreve.
- Frontmatter com `name` e `description`. A `description` diz **quando**
  acionar, não o que a skill acha de si mesma.

Estrutura do repo:

| Pasta | Conteudo |
|---|---|
| `skills/` | As skills, uma pasta cada |
| `shared/` | Regras e trechos usados por mais de uma skill |
| `marcas/` | Brief por loja: cor, tipografia, tom, restrição |
| `assets/arsenal/` | Blocos HTML prontos e validados |
| `scripts/` | Validadores, linters de copy, build |
| `evals/casos/` | Casos bons: entrada esperada e saída aceita |
| `evals/ruins/` | Casos ruins: pecas com vício, para o linter pegar |
| `docs/` | Documentacao interna |
| `fontes/` | Pacotes de origem versionados (.md, .csv, .json) |
| `vault-repo/` | Clone do vault completo, somente leitura, fora do git |
| `vendor/` | Referência externa, somente leitura, fora do git |
| `.claude-plugin/` | Manifesto do plugin |
