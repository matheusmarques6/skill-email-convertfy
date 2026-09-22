# `lint_status` por nota var2

Valor proposto do campo `lint_status` para cada nota de estrutura do
vault. **Nada foi aplicado**: o vault e somente leitura deste repo. Este
arquivo existe para voce aplicar no Obsidian.

Gerado rodando `scripts/lint_copy.py` sobre
`docs/pesquisa/vault-copy-extraida.json`, que traz 59 trechos
de copy literal citados nas 8 notas var2.

## Por que isto importa

Nota var2 e referencia: o Estruturador e o redator aprendem com o exemplo
que ela cita. Copy contaminada em nota de referencia ensina o vicio, e o
lint so pega depois, na peca. E o P07 do catalogo.

`lint_status: contaminada` nao quer dizer que a nota esta errada. Quer
dizer que a copy citada nela **nao deve ser usada como modelo de escrita**,
mesmo que a estrutura que ela documenta esteja certa.

## Resumo

| | |
|---|---|
| Notas analisadas | 8 |
| `limpa` | 2 |
| `contaminada` | 6 |
| Trechos no corpus | 59 |

## Valor por nota

| Nota | `lint_status` | IDs violados | Severidade |
|---|---|---|---|
| `avelmore-deadline-objecao` | **contaminada** | C02 | B |
| `avelmore-inspecao-antecipada` | **limpa** | nenhum | - |
| `avelmore-mecanismo-e-origem` | **contaminada** | C02, C43 | B, M |
| `avelmore-prova-social-cirurgica` | **contaminada** | C02, C15 | B, M |
| `carta-plain-text-extensao` | **limpa** | nenhum | - |
| `medicube-comparacao-categoria` | **contaminada** | C43 | M |
| `medicube-escassez-com-prova-de-demanda` | **contaminada** | C01, C02, C21, C35, C43 | A, B, M |
| `medicube-ultima-batida` | **contaminada** | C02, C21 | A, B |

## Como aplicar

No frontmatter da nota, em `vault/estruturas/<flow>/<slug>.md`:

```yaml
lint_status: contaminada
```

Valores: `limpa` ou `contaminada`. Nota nova nasce sem o campo ate passar
pelo lint.

Rode de novo depois de editar qualquer nota var2:

```bash
python3 scripts/lint_copy.py --json docs/pesquisa/vault-copy-extraida.json
```

O corpus precisa ser reextraido quando a nota mudar; ele nao se atualiza
sozinho.

## Detalhe dos achados

### `avelmore-deadline-objecao`

- **C02** (B, pt-BR) `hoje, 23:59`
- **C02** (B, pt-BR) `hoje, 23:59`

### `avelmore-mecanismo-e-origem`

- **C02** (B, en) `today, 11:59 p.m.`
- **C02** (B, en) `today, 11:59 p.m.`
- **C43** (M, en) `READ THE FULL STORY`

### `avelmore-prova-social-cirurgica`

- **C02** (B, en) `4.8/5 from 3,847 verified reviews`
- **C02** (B, en) `4.8/5 from 3,847 verified reviews`
- **C02** (B, en) `4.8/5 from 3,847 verified reviews`
- **C15** (M, en) `STILL WANT 10% OFF?`

### `medicube-comparacao-categoria`

- **C43** (M, en) `ENJOY DISCOUNT`

### `medicube-escassez-com-prova-de-demanda`

- **C02** (B, en) `LAST 12 HOURS FOR YOUR DISCOUNT`
- **C02** (B, en) `412 women already used WELCOME10 this week`
- **C02** (B, en) `only 16 codes remaining`
- **C02** (B, en) `THE CODE WELCOME10 EXPIRES AT 11:59 PM TODAY`
- **C02** (B, en) `THE CODE WELCOME10 EXPIRES AT 11:59 PM TODAY`
- **C21** (A, en) `start your style journey`
- **C35** (M, en) `LAST 12 HOURS FOR YOUR DISCOUNT`
- **C35** (M, en) `THE CODE WELCOME10 EXPIRES AT 11:59 PM TODAY`
- **C43** (M, en) `SECURE MY 10% OFF`
- **C01** (B, pt-BR) `$35 mais barato que o site oficial — mesma caixa, mesmos selos`
- **C02** (B, pt-BR) `no outro site, zero tracking por 3 semanas; aqui, tracking em 24h`

### `medicube-ultima-batida`

- **C02** (B, en) `...our exclusive discount expires today at 11:59 PM`
- **C02** (B, en) `... exclusive discount expires today at 11:59 PM`
- **C21** (A, en) `start your style journey with a discount`

