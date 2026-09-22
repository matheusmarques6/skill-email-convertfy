# evals

Dois acervos com propositos opostos.

| Pasta | O que e | O que mede |
|---|---|---|
| `ruins/` | Pecas com vicio conhecido | Se o lint **pega** o defeito |
| `casos/` | E-mails reais aprovados por humano | Se a suite **chega perto** do aprovado |

## Rodar

```bash
python3 scripts/roda_evals.py          # taxa de deteccao sobre ruins/
python3 scripts/roda_evals.py --json   # para CI
```

Exit code 1 quando um caso detectavel por lint deixa de ser pego.

## Como ler a taxa

O relatorio separa dois grupos, e a separacao e o ponto:

- **Detectavel por lint.** Regra de vocabulario, forma, pontuacao ou
  estrutura do HTML. Tem que dar 100%. Menos que isso e regressao.
- **Depende do revisor.** Regra de posicao, sequencia entre toques, ou
  verdade externa ao texto ("o prazo declarado foi cumprido no ESP?").
  O lint nao alcanca, e isso e projeto, nao defeito.

Somar os dois e reportar uma taxa unica seria um numero bonito e sem
significado. Treze dos 31 casos existem justamente para lembrar que o
lint sozinho nao fecha a conta: eles pertencem a `email-revisor` e a
`email-qa`.

Quando o lint pega algo "de tabela" num caso de revisor, o relatorio diz.
Nao conta como acerto: pegar C02 num caso que existe para testar V16 e
coincidencia, nao cobertura.

## Estrutura de `ruins/`

```
ruins/
  _manifesto.json    id, arquivo, regra esperada, deteccao, origem
  copy/*.json        entrada do lint_copy.py
  html/*.html        entrada do lint_email.py
```

Cada caso declara `deteccao: lint | revisor`. Caso novo entra no
manifesto junto com o arquivo, senao nao roda.

Origem dos 31 casos:

| Origem | Casos |
|---|---|
| Frases contaminadas do §2.3 da pesquisa | 5 |
| Exemplos ruins do §1 da pesquisa | 9 |
| Uma por linha B de `vault-vicios.md` | 17 |

## Preencher `casos/`

Copie `casos/_template.md`. O template pede o brief **antes** da peca,
porque caso sem brief nao permite medir geracao, so leitura.

Regra que importa: se o lint acusar algo numa peca aprovada, **nao
conserte a peca**. Ou a regra esta mal calibrada, e vira correcao em
`shared/calibracao.md`, ou a peca tem o defeito e passou assim, e isso e
dado sobre o criterio real de aprovacao. Os dois casos sao achado.
