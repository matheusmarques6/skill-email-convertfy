# Calendário Q4 2026, como exemplo real

Extraído de `fontes/BFCM-2026-Convertfy/02_Calendario_Q4/` (67 envios).
Serve de referência de formato e de proporção, não de plano a copiar.

## Números do plano

| | |
|---|---|
| Envios | 67 |
| Validado | 60 (89%) |
| Por mês | 2026-10 19, 2026-11 31, 2026-12 17 |

Regra 80/10/10: o plano fecha acima do mínimo de 80% validado.

## Por categoria

| Categoria | Envios |
|---|---|
| oferta | 18 |
| antecipação | 17 |
| pico | 17 |
| fechamento | 10 |
| pos | 3 |
| reengajamento | 2 |

## Famílias de assunto mais usadas

| Família | Envios |
|---|---|
| Confirmação de algo que já é da pessoa | 14 |
| Texto de pessoa | 8 |
| Aviso de mudança de estado | 7 |
| Número dentro do e-mail | 5 |
| Linha do Hormozi (2025) | 5 |
| Pendência | 4 |
| Última chamada | 3 |
| Convite com o nome | 3 |

## O schema de brief por envio

Cada envio do calendário é uma nota com este frontmatter. É o contrato
que `email-calendario` produz e que `email-copy` consome:

```yaml
---
tipo: email-q4-2026
data: 2026-11-11
hora: "07:00"
janela: "11.11 Black Antecipada"
papel: "Pico: disparo 1"            # o papel decide o modelo
categoria: pico                      # antecipacao | vespera | pico | fechamento | ressaca | oferta
familia_assunto: "Confirmação de algo que já é da pessoa"
hero: "Texto de pessoa"
booster: não                         # Campaign Booster da Omnisend
teste_ab: sim
evidencia: "validado"                # validado | inspiracao | complemento
---
```

E o corpo traz, em três linhas fixas:

```markdown
**Contexto:** <o contexto da data>
**Na história:** <onde entra no arco do trimestre>
**Público:** A: <camada> · B: <camada> · C: <camada>
```

`Público` é por **nível de conta**, não por loja: A, B e C recebem
públicos diferentes no mesmo envio. Ver `shared/segmentacao-e-freios.md`.

## Como ler o campo `papel`

O `papel` é o que liga o calendário ao modelo validado. Os papéis usados
no Q4 2026:

- `Pico: disparo 1` (07h), `disparo 2` (11h), `disparo 3` (18h)
- `Antecipação 1`, `2`, `3`
- `Véspera`
- `Fechamento de prazo`
- `Ressaca`, `Catálogo de presentes`, `Reabertura`

Cada um tem um modelo titular em
`skills/email-campanhas-sazonais/references/modelos-validados.md`.
