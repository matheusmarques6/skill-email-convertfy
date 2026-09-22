# NOTICE

Creditos de referencias externas usadas na suite de skills de e-mail da
Convertfy.

`vendor/` e somente leitura e nao e versionado. Nada dali e copiado: o que
reaproveitamos e **reescrito**. Esta pagina registra o credito de cada
reaproveitamento, como exige a politica em `CLAUDE.md`.

## Como registrar

Ao reescrever uma ideia vinda de um repo abaixo, preencha a coluna
**Reaproveitado** dizendo o que foi absorvido e em qual skill. Entrada
vazia significa "clonado como referencia, nada derivado ate agora".

## Apache License 2.0 (exige NOTICE)

### pbakaus/impeccable

- Fonte: https://github.com/pbakaus/impeccable
- Licenca: Apache License 2.0
- Copyright: ver `LICENSE` e `NOTICE.md` no repo de origem
- Reaproveitado: a arquitetura **Verify / Refuse** e a postura de critica
  isolada, reescritas em `shared/anti-vicios-copy.md` e
  `shared/postura-revisao.md`. Nenhum texto copiado.

Este produto inclui trabalho derivado de Impeccable, licenciado sob a
Apache License, Version 2.0. Copia da licenca em
http://www.apache.org/licenses/LICENSE-2.0

## MIT License

| Repo | Fonte | Reaproveitado |
|---|---|---|
| Leonxlnx/taste-skill | https://github.com/Leonxlnx/taste-skill | (nada ate agora) |
| blader/humanizer | https://github.com/blader/humanizer | Taxonomia de 25 padroes de escrita de IA, reescrita nos IDs C10 a C26 de `shared/anti-vicios-copy.md` |
| Henzen3d/Deslop-ptBR | https://github.com/Henzen3d/Deslop-ptBR | A ideia de tiers por severidade, reescrita na escala B/A/M e em `shared/lexico/pt-br.txt` |
| mackswendhell/humanizer-pt-br | https://github.com/mackswendhell/humanizer-pt-br | (nada ate agora) |
| msigor/humanizer-br | https://github.com/msigor/humanizer-br | (nada ate agora) |
| ravidsrk/slop-detect | https://github.com/ravidsrk/slop-detect | Metodo de limiar por densidade (adaptado para contagem absoluta por e-mail) e o catalogo de padroes de design, em `scripts/lint_copy.py` e `shared/anti-vicios-design.md` |
| emilkowalski/skills | https://github.com/emilkowalski/skills | O principio de que aprovacao se conquista (review-animations), em `shared/postura-revisao.md` |
| CosmoBlk/email-marketing-bible | https://github.com/CosmoBlk/email-marketing-bible | Laco de critica com nota e teto de 4 rodadas (`shared/postura-revisao.md`); checklist pre-envio, par "dois leitores", ban do gradiente roxo-azul e do banho bege, `#121212` no dark mode, limiares de entregabilidade e benchmarks rotulados como direcionais (`skills/email-design/draft/`, `skills/auditoria-omnisend/draft/`) |
| 808enzo/chappie | https://github.com/808enzo/chappie | Disciplina de fronteira na `description` (o que a skill nao cobre), promessa herdada e nao inventada, gatilho como regra, e estados de bloco na montagem, em `skills/email-flows/draft/` e `skills/email-design/draft/` |
| davidharttx/email-campaign-skill | https://github.com/davidharttx/email-campaign-skill | Modelo de duas camadas (entrada por fonte / ciclo de vida), ordem de prioridade de receita, as 10 especificacoes de flow, matriz de colisao entre flows e disciplina de fallback em merge tag, em `skills/email-flows/draft/` |
| framix-team/skill-email-html-mjml | https://github.com/framix-team/skill-email-html-mjml | Gotchas de Outlook (VML, fonte com fallback), atributo de componente sobre classe CSS no Gmail, `#121212` em vez de `#000`, bug do `vertical-align`, ban de accordion e carousel, em `skills/email-design/draft/`. A toolchain MJML NAO foi adotada |
| EmailBoutique-Digital-Inc/email-html-qa-skill | https://github.com/EmailBoutique-Digital-Inc/email-html-qa-skill | O de maior aproveitamento: principio de verificar mecanica e nao suficiencia, as duas metas de `color-scheme`, alt intencional, os tres overrides de auto-link, leitura de `Authentication-Results` e `List-Unsubscribe-Post` a partir do `.eml`, matriz de QA de dark mode e escala de severidade, em `skills/email-design/draft/` e `skills/auditoria-omnisend/draft/` |
| jayreis/prescott-amelia-agents | https://github.com/jayreis/prescott-amelia-agents | Placeholder marcado em vez de invencao, um nivel de card, piso de tamanho de fonte com "corte a copy, nao a fonte", tratar `<style>` como melhor esforco, cards de mesma altura e area de toque de 44px, em `skills/email-design/draft/`. Title Case em headline e a proibicao de `<head>` foram DESCARTADOS |
| thatrebeccarae/claude-marketing | https://github.com/thatrebeccarae/claude-marketing | Framework de auditoria em 4 fases, recomendacao em tres camadas e checklist dos 10 flows essenciais (klaviyo-analyst), em `skills/auditoria-omnisend/draft/` |
| olivalcf/klaviyo-audit-agent-skill | https://github.com/olivalcf/klaviyo-audit-agent-skill | Regras de seguranca inegociaveis, marcar `unverifiable` em vez de afirmar que uma checagem passou, os tres modos de auditoria, formato do achado e estrutura da rubrica (repontuada), em `skills/auditoria-omnisend/draft/` |

A licenca MIT exige preservar aviso de copyright e de permissao em copias
ou porcoes substanciais do software. Como nao copiamos, o credito acima
cumpre a intencao; se algum trecho for copiado literalmente, o aviso
completo do repo de origem tem que vir junto.

## Sem licenca declarada

| Repo | Fonte | Situacao |
|---|---|---|
| Join-Ground-AI/Ground-Retention-Skills | https://github.com/Join-Ground-AI/Ground-Retention-Skills | Nenhum arquivo de licenca no repo. Sem licenca nao ha permissao de uso ou derivacao. Tratar como leitura para entender o problema, nunca como base. Nao derivar ate que o autor publique uma licenca. |
