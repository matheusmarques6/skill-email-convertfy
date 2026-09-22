# Decisoes de rumo

Registro do que foi decidido, quando, e o que muda. Decisao sem registro
volta a ser discutida em duas semanas.

Formato: decisao, data, o que muda no repo, e o que faria revisitar.

---

## D-001. Container: 600 e o padrao, 598 e legado aceito

**Data:** 2026-09-22

600px e o padrao para peca nova. 598px continua aceito como legado: o
lint avisa em severidade **M** e **nao manda regerar** peca que ja existe.

- `scripts/lint_email.py`: `E_CONTAINER_LEGADO` (M) para 598,
  `E_CONTAINER` (A) para qualquer outra largura, silencio para 600.
- Peca nova com 598 recebe o aviso M e deve ir para 600. Peca antiga com
  598 fica como esta.

**Revisitar se:** aparecer quebra de render atribuivel a 598, ou o
arsenal padronizar em 600 e as pecas legadas forem migradas de qualquer
forma.

---

## D-002. MJML: nao adotar agora

**Data:** 2026-09-22

O HTML continua sendo escrito a mao, com tabela e estilo inline.

Motivo: adotar MJML significaria um passo de compilacao e um segundo
formato convivendo com `assets/arsenal/` e com o HTML que ja vem do
vault em `_html/`. O custo de manter dois formatos supera o ganho, no
tamanho atual da operacao.

O que foi aproveitado do `skill-email-html-mjml` sao os **gotchas
tecnicos**, nao a toolchain: VML so onde funciona, fonte com fallback,
atributo de componente sobre classe CSS no Gmail, `#121212` em vez de
`#000`, o bug do `vertical-align`, espaco entre tags causando
empilhamento, e o ban de accordion e carousel. Tudo em
`skills/email-design/`.

**Revisitar se:** o volume de pecas novas por semana passar do que da
para escrever a mao com qualidade, ou se entrar mais de um montador na
equipe e a consistencia cair.

---

## D-003. D21 a D31 entram no catalogo com status `revisar`

**Data:** 2026-09-22

Os onze itens que vieram da destilacao entram em
`shared/anti-vicios-design.md` com status `revisar`, mesmo onde a fonte
propunha `vicio` ou `bloqueia`.

`revisar` significa: o revisor olha e julga no contexto. Nao e achado
automatico do lint e nao reprova sozinho.

Motivo: nenhum dos onze tem evidencia nas duas pesquisas. Vem de repo de
referencia, que e experiencia de mercado, nao estudo. Entrar como `vicio`
seria dar a eles o mesmo peso de D01 a D20, que tem origem diferente.

**Revisitar quando:** houver caso real que sustente subir um item. Os
dois candidatos mais fortes sao D22 (auto-link no rodape, mecanica
verificavel e consequencia visivel no iOS) e D27 (`text-shadow`, mesmo
perfil de D18, que ja bloqueia).

---

## D-004. Contrato de variante: o novo e canonico

**Data:** 2026-09-22

As skills so geram no contrato novo. As 43 notas legadas sao convertidas
em memoria por `scripts/adaptar_variante_legado.py` quando escolhidas.

Detalhe em `docs/vault/migracao-contrato.md`.

---

## D-005. C34 vale so para pt-BR

**Data:** 2026-09-22

Loja de idioma ingles pode usar Title Case no assunto. Emoji no assunto
so quando `marcas/<cliente>.md` autoriza; sem ficha, o padrao e nao
permitir.

Correcao a fazer no vault em `docs/pesquisa/vault-correcoes.md`, VC01.

---

## D-006. T1, T3, T4 e T5 do Omnisend: `nao verificado`

**Data:** 2026-09-22

Nenhum foi testado em conta real. Ficam marcados como `nao verificado`
nas skills, com fallback seguro. Nenhum nome de variavel foi inventado.

Roteiro de teste em `docs/omnisend/roteiro-de-teste.md`.

---

## D-007. Rubrica de auditoria repontuada

**Data:** 2026-09-22

Ver `skills/auditoria-omnisend/references/rubrica.md` para a pontuacao e
a premissa declarada.
