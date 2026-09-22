# Calibração a propor: falsos positivos em copy aprovada

Resultado de rodar `scripts/lint_copy.py` nas **58 peças reais aprovadas**
de `evals/referencias-reais/`, extraídas de
`fontes/BFCM-2026-Convertfy/06_Figma_copy_real/`.

Estas peças foram aprovadas por humano e enviadas. Achado do lint aqui é,
na maioria, **defeito de calibração**, não defeito da peça.

**Nada foi aplicado.** Cada item traz a proposta e o efeito.

## Resultado bruto

| | |
|---|---|
| Peças | 58 |
| Bloqueiam (têm B) | 18 |
| Achados totais | 115 |

| Regra | Achados | Veredito |
|---|---|---|
| C02 | 39 | **Falso positivo parcial** |
| C45 | 24 | Legítimo em parte |
| V29_SEM_CONTEXTO | 20 | Esperado, é aviso |
| C21 | 9 | **Falso positivo** |
| C35 | 9 | **Falso positivo** |
| C11 | 5 | **Falso positivo** |
| C43 | 4 | Legítimo |
| C40, C15, C18, C46, C04, C22, C10, C42 | 1 a 3 | Misto |

---

## FP01. C02 conta data como número inventado

**Achados:** 39, o maior bloco.

Exemplos de copy aprovada acusada:

```
Only on 8.8. Valid sitewide.
And on 8.8, flash deals unlock at three set times.
Come back on 8.8. Stay ahead on both.
```

`8.8` é **o nome da data**, não uma alegação numérica. O mesmo vale para
`11.11`, `10.10`, `7AM`, `11AM`, `18h`.

**Proposta:** C02 ignora token que casa com padrão de data de campanha
(`\d{1,2}\.\d{1,2}`), hora (`\d{1,2}(h|AM|PM|:\d{2})`) e ano. Continua
pegando alegação: `6,747 REVIEWS` é acusação correta e deve permanecer.

**Efeito:** derruba cerca de 30 dos 39 achados, e mantém os que importam.

---

## FP02. C35 acusa rótulo em caixa alta

**Achados:** 9.

```
ALREADY ON SALE IN THE WARM-UP:
STILL NOT SURE WHAT TO GET?
AINDA DÁ TEMPO DE GARANTIR ESSES:
```

São **rótulos de seção**, e o §8 da calibração protege explicitamente
"caixa alta em headline curta, rótulo e botão".

**Proposta:** C35 não dispara em linha de até 8 palavras que termina em
`:` ou `?`, ou que é bloco isolado sem ponto final. A regra passa a
valer só para caixa alta **dentro de parágrafo corrido**, que é o que ela
sempre quis pegar.

**Efeito:** zera os 9. É o falso positivo mais claro do conjunto, porque
contradiz a própria calibração que já está escrita.

---

## FP03. C11 acusa lista de horários

**Achados:** 5.

```
7AM, 11AM, and 6PM
07h, 11h e 18h
```

A tríade ornamental que C11 persegue é de **adjetivo ou verbo em ritmo**
("conforto, estilo e elegância"). Uma lista de três horários é **fato
operacional**: são os horários reais de disparo do dia de pico.

**Proposta:** C11 não conta item que é número, hora, data ou código. Três
fatos não formam tríade retórica.

**Efeito:** zera os 5.

---

## FP04. C21 acusa "unlock" usado literalmente

**Achados:** 9.

```
flash deals unlock at three set times
unlock dad's gift
UNLOCK WITH THE KEY:
```

`unlock` está no léxico como vocabulário de IA, e com razão quando é
enchimento ("unlock your potential"). Aqui é **mecânica literal**: a
oferta destrava em horário definido, e há uma chave no criativo.

**Proposta:** marcar no léxico os verbos que têm uso literal
(`unlock`/`destravar`, `reveal`/`revelar`, `release`/`liberar`) com um
modo novo, `contextual`: só acusa quando o objeto é abstrato (potential,
journey, experience). Quando o objeto é concreto (gift, deals, coupon,
site), passa.

**Efeito:** derruba os 9 sem abrir mão do uso vazio.

Nota: "seamless" no mesmo bloco é acusação **correta** e deve permanecer.

---

## FP05. C10 acusa negação factual

**Achados:** 1.

```
It's not on the website or in the app.
```

Não é a antítese "não é X, é Y". É **negação factual**: diz onde a oferta
não está. A estrutura que C10 persegue tem a segunda metade afirmativa.

**Proposta:** C10 exige que a segunda metade seja afirmação contrastante
(`é`, `mas`, `it's`, `but`). `not ... or ...` é enumeração negativa e sai.

**Efeito:** 1 achado, mas é erro de conceito e vai reaparecer.

---

## Achados que são legítimos, não mexer

| Regra | Por quê |
|---|---|
| C02 em `6,747 REVIEWS` | Número de prova precisa de origem no brief. Correto |
| C43 em `GRAB IT WHILE YOU CAN` | CTA sem objeto. Correto |
| C45 acima do teto | Peça longa é longa mesmo. Ver a proposta de altura em px na reconciliação |
| C40 assunto longo | O primeiro texto da peça virou assunto na extração; conferir caso a caso |
| C18 desvio baixo | Dois casos, ambos com média acima de 8 palavras. Correto |

---

## Limite desta medição

A extração do Figma não traz assunto nem pré-cabeçalho separados: usei o
primeiro e o segundo texto da ordem de leitura como aproximação. Por isso
**C40, C41 e C42 não são confiáveis** neste corpus, e ficaram fora das
propostas.

Uma primeira versão desta extração classificava todo texto em caixa alta
como CTA, e produziu **513 achados de C43**. Eram rótulos de selo de
rodapé ("SECURE PAYMENT", "ENVIO EXPRESSO"), não CTAs. Corrigida a
extração, sobraram 4. Fica o registro de que **falso positivo em massa
costuma ser defeito de quem chamou o lint**, não do lint.

## Resumo da proposta

| # | Regra | Achados hoje | Depois | Risco |
|---|---|---|---|---|
| FP01 | C02 | 39 | ~9 | Baixo. Data não é alegação |
| FP02 | C35 | 9 | 0 | Nenhum. Já está na calibração escrita |
| FP03 | C11 | 5 | 0 | Baixo |
| FP04 | C21 | 9 | ~1 | Médio. Exige o modo `contextual` no léxico |
| FP05 | C10 | 1 | 0 | Baixo |

Total: de 115 para cerca de 60 achados, sem perder nenhum achado real
identificado.
