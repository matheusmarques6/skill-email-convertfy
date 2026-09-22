# Anti-vícios de design (D01 a D20)

Contrato de layout de e-mail da Convertfy. Fonte:
`docs/pesquisa/pesquisa-vicios-ia-email.md` seção 6 e
`docs/pesquisa/evidencias-publicadas.md` seção 6.
Aplicação determinística: `scripts/lint_email.py` sobre o HTML final.

## Aviso que sustenta a coluna "status"

**Metade dos padrões de "cara de IA" catalogados na web é convenção legítima de
e-mail.** Layout centralizado, coluna única, caixa alta em rótulo, número grande
de oferta e CTA repetido são padrão de produção em e-mail, não sintoma. Importar
uma lista de slop de landing page sem filtro quebraria o arsenal e faria o lint
reprovar peça boa.

A coluna **status em e-mail** existe só para isso:

| Status | Significado | Severidade no lint |
|---|---|---|
| **Vício** | padrão de IA também em e-mail | A |
| **Revisar** | legítimo em e-mail dependendo do uso; o vício é o uso decorativo | M, quase sempre julgamento |
| **Bloqueia** | quebra de renderização ou de conformidade | B |

A lista de falso positivo a proteger está em `shared/calibracao.md`. Antes de
adicionar regra nova aqui, confira lá.

## Catálogo

| ID | Padrão | Status | Regra | Fonte |
|---|---|---|---|---|
| D01 | Gradiente roxo para azul, CTA índigo ou violeta | Vício | proibido, salvo se a cor constar em `marcas/<cliente>.md` | F8, F9 |
| D02 | Texto em gradiente, glow, glassmorphism, blob aurora | Bloqueia | proibido: não renderiza no Outlook e marca IA | F8, F10 |
| D03 | Fundo creme ou bege por padrão | Vício | fundo branco por padrão; bege só se for da marca | F8, F9 |
| D04 | Cinza claro em texto de corpo | Vício | contraste mínimo 4,5:1; corpo em #000 ou #1A1A1A | F8, F10 |
| D05 | Texto cinza sobre fundo colorido | Vício | sobre cor, texto branco ou preto | F8 |
| D06 | Fonte padrão de IA como voz display (Inter, Geist, Space Grotesk) | Revisar | em e-mail a maioria dos clientes cai no fallback, então o risco é menor; com fonte própria da marca, use a da marca em imagem e título | F8, arsenal |
| D07 | Pílula eyebrow acima da headline | Revisar | legítima quando carrega informação (prazo, condição); proibida quando é decorativa ou tem emoji de brilho | F8, F10 |
| D08 | Grade de cards iguais com ícone no topo | Revisar | permitida como faixa curta de diferenciais; proibida como estrutura principal | F8, F10 |
| D09 | Banner de estatística | Revisar | só com número real do brief (ver C02) | F8 |
| D10 | Avatar de inicial em gradiente no depoimento | Vício | foto real do cliente ou do produto, ou nenhuma imagem | F8 |
| D11 | Card dentro de card, borda colorida grossa à esquerda | Vício | 1 nível de contêiner | F8, F10 |
| D12 | Hierarquia tipográfica achatada | Vício | razão mínima de 2:1 entre headline e corpo | F8 |
| D13 | Headline gigante com frase longa | Vício | display até cerca de 40 caracteres; frase longa desce para o corpo | F8 |
| D14 | Tracking negativo forte no display, largo no corpo | Vício | display a partir de -0,02em; corpo em 0 | F8 |
| D15 | Imagem de IA genérica (pessoa plástica, produto flutuando) | Vício | foto real da loja; imagem gerada só com aprovação no brief | F9, F10 |
| D16 | Centralizado mais 3 cards mais CTA | Revisar | centralizado é convenção; o vício é a sequência genérica. A estrutura vem do vault (var2) | F9 |
| D17 | E-mail só imagem, sem alt | Vício | alt descritivo com a oferta mais 1 linha de texto vivo | F4 |
| D18 | position absolute, transform, border-radius em img, webfont sem fallback, SVG inline | Bloqueia | lint | arsenal, F10 |
| D19 | Dark mode por inversão ingênua | Vício | #121212 no lugar de #000 puro; logo com versão para fundo escuro | F9 |
| D20 | Espaço vazio órfão, respiro irregular | Vício | ritmo vertical fixo por seção do arsenal | F9 |

## O que o `lint_email.py` checa

O lint cobre o que dá para provar em HTML. O resto é revisão (ver
`shared/postura-revisao.md`).

| Checagem | Regra | Severidade |
|---|---|---|
| `position:absolute`, `transform:`, `border-radius` em `img`, `@font-face` sem pilha de fallback, `<svg>` | D18 | B |
| `linear-gradient`, `radial-gradient`, `backdrop-filter` | D02 | B |
| Tamanho acima de 102 KB (corte do Gmail) | E_TAMANHO | B |
| Placeholder idêntico repetido, `[FALTA: ...]` não preenchido, lorem ipsum | E_PLACEHOLDER | B |
| `img` sem alt, ou alt vazio, com largura acima de 200px | D17 | A |
| Contraste abaixo de 4,5:1 entre cor inline do texto e fundo do `td` pai | D04 (fundo branco) ou D05 (fundo colorido) | A |
| Container diferente de 600 (598 aceito) | E_CONTAINER | A |
| Preheader ausente | E_PREHEADER | A |
| CTA só em imagem, sem nenhum link com texto vivo | E_CTA_IMAGEM | A |
| Índigo ou violeta em botão, fundo bege, sem constar na ficha da marca | D01, D03 | A |
| `img` sem largura declarada e sem alt | D17 | M |

Uso:

```
python3 scripts/lint_email.py peca.html --json
python3 scripts/lint_email.py peca.html --marca marcas/luxury-club.json
```

A ficha da marca é um JSON com `{"cores": ["#4F46E5"]}`. Sem ficha, a peça é
julgada como neutra: fundo branco, texto preto, que é a regra fixa da Convertfy.

## Por que o tamanho e o alt estão aqui, e não em copy

São as duas regras de design com evidência publicada mais forte, e as duas valem
por quatro motivos somados, não por estética:

- **Texto vivo mais alt:** entregabilidade (razão texto sobre imagem),
  acessibilidade (leitor de tela), resumo de IA na caixa de entrada (Gemini e
  Apple Intelligence resumem a partir do texto) e imagem bloqueada. Na Trendtrack,
  o preview de e-mails só imagem sai como OCR ilegível: é literalmente o que o
  resumidor e o leitor de tela recebem.
- **102 KB:** acima disso o Gmail corta a mensagem e pode esconder o link de
  descadastro, o que é problema de conformidade, não de layout. O valor exato de
  102 KB está em `docs/pesquisa/a-verificar.md` para reconfirmação; a regra de
  manter a peça pequena não depende do dígito.

## O que não é motivo para nenhuma dessas regras

Não escreva, em skill nenhuma, que provedor filtra "texto com cara de IA". Não
há evidência primária disso. O que existe é filtro por reputação, autenticação,
engajamento e reclamação. Justifique o design por renderização, acessibilidade e
conversão.
