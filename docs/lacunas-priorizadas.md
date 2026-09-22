# Lacunas priorizadas

Da auditoria (Fase 1), da reconciliação (Fase 2) e dos testes (Fase 5).
Ordenado por quanto trava trabalho real.

Esforço: **P** até meio dia · **M** um a dois dias · **G** mais que isso.

## As 5 que mais importam

### 1. V29 bloqueia campanha validada — P

**O quê:** a peça do teste 2 reproduz a campanha de 07h do 11.11 bloco a
bloco e é **bloqueada em V29** por declarar "11:59 PM", que é o prazo
real da oferta e está no brief da própria campanha.

**Onde:** `scripts/lint_copy.py`, `regra_v29`.

**Correção:** V29 compara a hora declarada com `prazo_oferta` do payload.
Coincide, passa. Diverge, bloqueia. Sem o campo, avisa em M.

**Por que é a número 1:** é a única regra que hoje impede a suíte de
produzir o que a carteira mais valida.

### 2. As 9 regras em disputa da Fase 2 — M

**O quê:** C03, C05, C22, C30, C31, C45, P09, D01 a D05 e D13 têm redação
proposta e **aguardam aprovação**. Enquanto isso, a suíte não consegue
produzir 4 dos 6 modelos titulares do ranking (texto de pessoa, conversa,
fundador, ligação) nem os assuntos de maior receita.

**Onde:** `docs/reconciliacao-regras-dados.md`.

**Correção:** decisão do dono. Cada uma tem redação e mudança no lint
escritas.

### 3. Direção de imagem por slot — G

**O quê:** o hero é o que mais pesa, e a suíte não produz brief de
imagem. Lacuna 6e da auditoria (`imagegen` do Taste sem equivalente).

**Onde:** `assets/arsenal/`, nova `references/direcao-de-imagem.md` em
`email-design`.

**Correção:** por slot do arsenal, uma proporção nomeada e um prompt
pronto. O material existe: `07_Design_Blue_Wolf/04_PROMPTS_POR_LOTE.md`
tem 8 lotes de prompt já escritos.

### 4. Altura da peça não é medida — M

**O quê:** a carteira mede em px (2.000 a 3.200 alvo, 4.136 foi o
fracasso) e a suíte mede em palavras. São eixos diferentes e o de px é o
que a carteira provou.

**Onde:** `scripts/lint_email.py`, novos D32 e D33.

**Correção:** estimar altura somando `height` de imagem e linha de texto.
Entrar como `revisar`, não como B, até validar contra 5 peças medidas.

### 5. Os 5 falsos positivos em copy aprovada — P

**O quê:** rodar o lint nas 58 peças aprovadas deu 115 achados. Cerca de
metade é calibração errada: C02 conta data como número inventado, C35
acusa rótulo em caixa alta que o §8 protege, C11 acusa lista de horários,
C21 acusa "unlock" literal, C10 acusa negação factual.

**Onde:** `docs/pesquisa/calibracao-a-propor.md`.

**Correção:** as cinco estão escritas com efeito estimado. De 115 para
cerca de 60 achados, sem perder achado real.

---

## O resto, por bloco

### Da auditoria da fusão

| # | Lacuna | Alvo | Esforço |
|---|---|---|---|
| 6 | Snapshot do revisor não é salvo, não dá para comparar evolução (5e) | `skills/email-revisor/` | P |
| 7 | `polish`, `distill`, `clarify`, `typeset`, `layout` sem equivalente (5h) | roteador | M |
| 8 | `doctor`: divergência entre skill, vault e arsenal (5j) | `scripts/doctor.py` | M |
| 9 | 3 dials de e-mail ligados à variante (6b) | `shared/` | M |
| 10 | Contagem de entregáveis do anti-truncamento (6c) | `shared/protocolo-de-execucao.md` | P |
| 11 | `redesign` com prioridade e "o que a IA esquece" (6d) | nova reference | M |
| 12 | PLAN-TEMPLATE de repasse para o admin (7d) | `docs/` | P |
| 13 | Subagentes finish-reviewer, asset-producer, documenter (5i) | `skills/` | G |
| 14 | Responsivo e acessibilidade ausentes do `email-qa` (3a) | `skills/email-qa/` | P |
| 15 | Retina e `lang` só mencionados, não são regra (2b) | `email-design` | P |

### Do vault e das fontes

| # | Lacuna | Alvo | Esforço |
|---|---|---|---|
| 16 | Os 43 `aliviador` por decidir | `shared/aliviador-legado.json` | M |
| 17 | `eixos/aliviador/` e `eixos/profundidade/` não existem no vault | Obsidian | M |
| 18 | 11 referências de e-mail do vault não usadas | `evals/referencias-reais/` | P |
| 19 | 212 notas do Max sem ponte para a suíte | `shared/` | G |
| 20 | `header` e `cta` com zero variantes | `assets/arsenal/blocos/` | M |
| 21 | T1, T3, T4 e T5 do Omnisend por testar | conta real | M |
| 22 | `list-growth` como skill futura de captação | `skills/` | G |
| 23 | Campaign Booster, SMS e WhatsApp sem lugar definido | `email-calendario` | P |

### Regras novas propostas, sem aplicar

N01 a N06 em `docs/reconciliacao-regras-dados.md`: extensão de oferta,
evento colado, segmento ampliado, promessa repetida, assunto que repete a
promessa anterior, e o gate 80/10/10. Esforço P cada uma.
