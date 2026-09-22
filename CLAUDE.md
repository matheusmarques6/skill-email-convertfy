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

Precedencia quando houver conflito:
**brief da loja > vault > este CLAUDE.md > skill > vendor.**

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

Cobertura atual do vault (44 variantes): `body` 18, `hero` 18,
`products` 16, `reviews` 10, `offer` 9, `footer` 4, e **`header` e `cta`
com zero variantes**. Zero candidata nao e erro: declare a lacuna conforme
`vault/componentes/lacunas/`, nao invente variante para preencher.

## Licenca: vendor/ e somente leitura

`vendor/` guarda 12 repos de referencia clonados com `--depth 1`. Esta no
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
- Dez repos sao **MIT**: taste-skill, skills (emilkowalski),
  email-marketing-bible, chappie, email-campaign-skill,
  skill-email-html-mjml, email-html-qa-skill, prescott-amelia-agents,
  claude-marketing, klaviyo-audit-agent-skill.
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
| `vendor/` | Referencia externa, somente leitura, fora do git |
| `.claude-plugin/` | Manifesto do plugin |
