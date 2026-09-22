# skill-email-convertfy

Suite de skills de e-mail marketing para e-commerce da Convertfy: 250+
lojas Shopify, ESP principal Omnisend, secundario Klaviyo.

O objetivo central e eliminar vícios de IA em copy e design de e-mail. A
peca tem que parecer feita por uma loja, não gerada por um assistente.

## Comece por aqui

- **`CLAUDE.md`** as regras fixas da Convertfy (layout, técnica, copy,
  specs), a taxonomia de blocos, a politica de licença e a convenção de
  skills. Leia antes de escrever qualquer skill.
- **`vault/`** a fonte de verdade, somente leitura. Comece em
  `vault/_INDEX.md` e siga `vault/componentes/_protocolo-de-selecao.md`.
- **`NOTICE.md`** creditos das referências externas.

## As 8 skills

Entre pelo roteador. Ele decide a rota e aplica o gate.

| Skill | Faz |
|---|---|
| `convertfy-email` | **Roteador.** Ponto de entrada, modos e despacho |
| `email-copy` | Assunto, preheader, headline, corpo, CTA, alt |
| `email-design` | HTML: 600px, inline, bulletproof, Outlook, dark mode |
| `email-flows` | Os 10 flows no Omnisend, com equivalencia Klaviyo |
| `email-qa` | Gate final antes do envio: vai ou não vai |
| `email-revisor` | Revisor separado, contexto limpo, nota /10 |
| `email-variantes` | 3 versões por eixo (oferta, prova, problema) |
| `auditoria-omnisend` | Audita a conta inteira, com evidência |

Cadeia completa de uma peca do zero:

```
flow (se for automacao)  ->  copy  ->  design  ->  qa
```

## Instalar como plugin

```
/plugin marketplace add matheusmarques6/skill-email-convertfy
```

Para subir uma skill avulsa no claude.ai, gere o zip:

```bash
python3 scripts/build_zip.py            # todas, em dist/
python3 scripts/build_zip.py email-qa   # so uma
```

Cada zip e autocontido: leva junto os arquivos de `shared/` e `scripts/`
que a skill cita, com os caminhos reescritos.

## O gate

Nada sai com violacao de severidade B.

```bash
python3 scripts/lint_copy.py  --json peca.json
python3 scripts/lint_email.py --json peca.html
```

Exit code 1 significa que existe B. O gate e o exit code, não a leitura
humana da saída.

## Estrutura

| Pasta | Conteudo |
|---|---|
| `skills/` | As 8 skills (`SKILL.md` até 500 linhas, detalhe em `references/`) |
| `shared/` | Regras usadas por mais de uma skill: anti-vícios, calibração, protocolo, lexicos |
| `marcas/` | Ficha por loja: cor, tipografia, tom, restrição |
| `assets/arsenal/` | Blocos HTML e manifesto |
| `scripts/` | Os dois linters, os testes, o setup e o empacotador |
| `evals/casos/` | Casos bons |
| `evals/ruins/` | Casos ruins, para o linter pegar |
| `docs/pesquisa/` | As pesquisas base e o que ainda precisa ser verificado |
| `docs/destilacao/` | O que foi aproveitado de cada repo de referência |
| `LICENSES/` | Licenças de origem dos repos dos quais derivamos algo |
| `vendor/` | 17 repos de referência, somente leitura, fora do git |
| `.claude-plugin/` | Manifesto do plugin e do marketplace |

## Setup local

O `vault/` e um symlink e o `vendor/` são clones. Nenhum dos dois e
versionado, então recrie os dois após clonar:

```bash
./scripts/setup.sh
```

O script clona o vault (`matheusmarques6/all-for-eficiencia`) e os 12
repos de referência, e aponta o symlink `vault` para
`Admin Convertfy/Emails`. Se você já tem o vault em disco (Obsidian
local), aponte o caminho com a variavel de ambiente:

```bash
CONVERTFY_VAULT="/caminho/para/Admin Convertfy/Emails" ./scripts/setup.sh
```

## Regras que não se negociam

- Layout neutro: fundo branco, texto preto, sem paleta autoral.
- 600px, `role="presentation"`, estilos inline, botao bulletproof, Outlook,
  dark mode.
- Copy curta, genérica e realista. Sem storytelling elaborado.
- Travessão proibido em qualquer copy.
- `vendor/` nunca e editado nem copiado: o que reaproveitamos e reescrito,
  com credito em `NOTICE.md`.
