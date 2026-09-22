# skill-email-convertfy

Suite de skills de e-mail marketing para e-commerce da Convertfy: 250+
lojas Shopify, ESP principal Omnisend, secundario Klaviyo.

O objetivo central e eliminar vicios de IA em copy e design de e-mail. A
peca tem que parecer feita por uma loja, nao gerada por um assistente.

## Comece por aqui

- **`CLAUDE.md`** as regras fixas da Convertfy (layout, tecnica, copy,
  specs), a taxonomia de blocos, a politica de licenca e a convencao de
  skills. Leia antes de escrever qualquer skill.
- **`vault/`** a fonte de verdade, somente leitura. Comece em
  `vault/_INDEX.md` e siga `vault/componentes/_protocolo-de-selecao.md`.
- **`NOTICE.md`** creditos das referencias externas.

## Estrutura

| Pasta | Conteudo |
|---|---|
| `skills/` | As skills, uma pasta cada (`skills/<nome>/SKILL.md`, ate 500 linhas) |
| `shared/` | Regras e trechos usados por mais de uma skill |
| `marcas/` | Brief por loja: cor, tipografia, tom, restricao |
| `assets/arsenal/` | Blocos HTML prontos e validados |
| `scripts/` | Validadores, linters de copy, build |
| `evals/casos/` | Casos bons: entrada esperada e saida aceita |
| `evals/ruins/` | Casos ruins: pecas com vicio, para o linter pegar |
| `docs/` | Documentacao interna |
| `vendor/` | 12 repos de referencia, somente leitura, fora do git |
| `.claude-plugin/` | Manifesto do plugin |

## Setup local

O `vault/` e um symlink e o `vendor/` sao clones. Nenhum dos dois e
versionado, entao recrie os dois apos clonar:

```bash
./scripts/setup.sh
```

O script clona o vault (`matheusmarques6/all-for-eficiencia`) e os 12
repos de referencia, e aponta o symlink `vault` para
`Admin Convertfy/Emails`. Se voce ja tem o vault em disco (Obsidian
local), aponte o caminho com a variavel de ambiente:

```bash
CONVERTFY_VAULT="/caminho/para/Admin Convertfy/Emails" ./scripts/setup.sh
```

## Regras que nao se negociam

- Layout neutro: fundo branco, texto preto, sem paleta autoral.
- 600px, `role="presentation"`, estilos inline, botao bulletproof, Outlook,
  dark mode.
- Copy curta, generica e realista. Sem storytelling elaborado.
- Travessao proibido em qualquer copy.
- `vendor/` nunca e editado nem copiado: o que reaproveitamos e reescrito,
  com credito em `NOTICE.md`.
