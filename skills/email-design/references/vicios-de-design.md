# Vícios de design, com a coluna que importa

Detalhe da `email-design`. Catálogo D01 a D20 da pesquisa, mais os itens
novos que a destilação dos repos trouxe.

## Por que este arquivo existe

**Metade dos padrões de "cara de IA" catalogados para a web é convenção
legítima de e-mail.** Centralizado, caixa alta, número grande de oferta,
coluna única: tudo isso é normal em e-mail e anormal numa landing page.

Importar lista de web sem filtro quebraria o arsenal inteiro. A coluna
**Status em e-mail** resolve. Use sempre ela.

| Status | Significa |
|---|---|
| **Vício** | Não fazemos |
| **Revisar** | Depende do contexto. Há uso legítimo e há uso viciado |
| **Bloqueia** | Quebra tecnicamente. O lint impede |

## Catálogo

| ID | Padrão | Status | Regra |
|---|---|---|---|
| D01 | Gradiente roxo para azul, CTA índigo ou violeta | **Vício** | Proibido, salvo cor da marca no brief |
| D02 | Texto em gradiente, glow colorido, glassmorphism, blob "aurora" | **Vício mais quebra** | Proibido: não renderiza no Outlook e marca IA |
| D03 | Fundo creme ou bege por padrão | **Vício** | Fundo branco por padrão. Bege só se for da marca |
| D04 | Cinza claro em texto de corpo, abaixo de 4,5:1 | **Vício** | Contraste mínimo 4,5:1. Corpo em `#000` ou `#1A1A1A` |
| D05 | Texto cinza sobre fundo colorido | **Vício** | Texto sobre cor é branco ou preto |
| D06 | Fonte padrão de IA como voz display (Inter, Geist, Space Grotesk) | **Revisar** | Em e-mail o risco é menor: a maioria dos clientes cai no fallback. Quando a marca tem fonte própria, usar a da marca nos títulos e nas imagens |
| D07 | Pílula "eyebrow" acima da headline | **Revisar** | Legítima quando carrega informação (prazo, condição). Proibida quando é decorativa ou tem emoji de brilho |
| D08 | Grade de cards idênticos com ícone no topo | **Revisar** | Permitida como faixa curta de diferenciais. Proibida como estrutura principal do e-mail |
| D09 | Banner de estatísticas ("10k+ / 4.9 / 98%") | **Revisar** | Só com números reais do brief. Número inventado é C02 |
| D10 | Avatar de iniciais em gradiente em depoimento | **Vício** | Foto real do cliente ou do produto, ou imagem nenhuma |
| D11 | Card dentro de card, borda colorida grossa à esquerda | **Vício** | Um nível de contêiner |
| D12 | Hierarquia tipográfica achatada | **Vício** | Razão de ao menos 2:1 entre headline e corpo |
| D13 | Headline gigante com frase longa | **Vício** | Headline display com até ~40 caracteres. Frase longa desce para o corpo |
| D14 | Tracking negativo forte no display, tracking largo no corpo | **Vício** | Display nunca abaixo de -0,02em. Corpo em 0 |
| D15 | Imagem de IA genérica (pessoa plástica, produto flutuando em fundo abstrato) | **Vício** | Foto real da loja. IA só para fundo ou cena quando o brief aprova, com checklist |
| D16 | Centralizado mais 3 cards mais CTA | **Revisar** | Centralizado é convenção. O vício é a **sequência genérica**. A estrutura vem do vault |
| D17 | E-mail só imagem, sem alt | **Vício** | Alt descritivo com a oferta, mais 1 linha de texto vivo |
| D18 | Recursos que quebram | **Bloqueia** | `position:absolute`, `transform`, `border-radius` em `<img>`, `@font-face` sem fallback, `<svg>` inline, JS |
| D19 | Dark mode por inversão ingênua | **Vício** | `#121212` em vez de `#000`. Logo com versão para fundo escuro |
| D20 | Espaço vazio órfão, respiro irregular entre blocos | **Vício** | Ritmo vertical fixo, por seção do arsenal |

## Itens novos, vindos da destilação

Não estão no catálogo da pesquisa. Candidatos a virar D21 em diante,
decisão do dono do repo.

| ID proposto | Padrão | Status | Regra | Origem |
|---|---|---|---|---|
| D21 | Imagem grande sem link | **Revisar** | O Gmail embrulha imagem não linkada acima de certo tamanho no próprio lightbox e abre a imagem no toque, roubando o clique do CTA. Linke a hero e as imagens grandes. Logo, espaçador e ícone pequeno podem ficar sem link | `email-html-qa-skill` |
| D22 | Auto-link de telefone, data e endereço no rodapé | **Bloqueia** | Recolore o texto e quebra o rodapé. Exige os três overrides separados (Apple, Gmail, Samsung), porque o Gmail remove seletor de atributo encadeado | `email-html-qa-skill` |
| D23 | Alt descritivo em imagem decorativa | **Revisar** | Refina D17. Decorativa recebe `alt=""`. O pior caso é alt ausente: alguns leitores de tela leem o nome do arquivo | `email-html-qa-skill`, `skill-email-html-mjml` |
| D24 | Bloco dinâmico sem estado para vazio | **Vício** | Bloco de produto, de avaliação ou de desconto que pode sair vazio precisa de estado definido. Padrão: a seção não aparece, em vez de aparecer com furo | `chappie/email-design` |
| D25 | Cards lado a lado com altura desigual | **Vício** | Cor de fundo no `<td>` externo, nunca no interno. Altura fixa em todas as imagens da mesma linha | `prescott-amelia-agents` |
| D26 | Texto de corpo abaixo de 14px, ou rodapé abaixo de 11px, para caber | **Vício** | O problema é excesso de copy, não tamanho de fonte. Corte a copy | `prescott-amelia-agents` |
| D27 | Sombra em texto (`text-shadow`) | **Bloqueia** | Reduz legibilidade e é removida ou quebrada por vários clientes. Contraste e opacidade de overlay são as ferramentas corretas | `prescott-amelia-agents` |
| D28 | Três ou mais famílias tipográficas | **Vício** | No máximo duas: a **tipografia principal** e a **fonte secundária** | `prescott-amelia-agents` |
| D29 | Duas cores de CTA principal na mesma peça | **Vício** | Uma cor de CTA. Duas criam ambiguidade sobre qual ação importa | `prescott-amelia-agents` |
| D30 | Dois CTAs concorrentes no hero | **Vício** | O hero tem um botão. Dois CTAs no hero significam duas mensagens, e duas mensagens são dois e-mails | `prescott-amelia-agents` |
| D31 | SVG decorativo (flor, brilho, forma abstrata, divisor ornamental) | **Vício** | Salvo quando o design existente da marca já usa. SVG funcional (marcador de lista com ícone, divisor de seção) é a exceção | `prescott-amelia-agents` |

## Falsos positivos: o que um revisor pode reprovar por engano

Lista de calibração, §8 da pesquisa. Um revisor que reprova qualquer item
desta lista está aplicando régua de web num e-mail.

| Padrão | Por que não é vício |
|---|---|
| Layout centralizado | Convenção de e-mail há vinte anos |
| Coluna única de 600px | Convenção, e é o que o CLAUDE.md exige |
| Caixa alta em headline curta, rótulo ou botão | Convenção. Só é vício em parágrafo (C35) |
| Número grande de oferta ("15% OFF") como elemento visual | É o conteúdo do e-mail, não decoração |
| O mesmo CTA repetido, com o mesmo destino | Boa prática em peça longa. O vício é **dois CTAs com destinos diferentes** (C44) |
| "Comprar agora", "Aproveitar", "Shop now" | O corpus humano de 64 CTAs é dominado por verbos assim. CTA humano não é criativo (C43) |
| Frase pronta curta de boas-vindas | A L.L.Bean usa. O diferencial não está na frase, está na condição que vem depois |
| Um parágrafo de 25 a 40 palavras no e-mail inteiro | Aceitável quando é a única explicação do produto |

## O que sustenta cada item

Origens do catálogo original:

- **Peso alto no detector de "cara de IA"** (D01, D03, D04, D06): vêm de
  um repositório de detecção de padrão. **Atenção:** o estudo de Adrian
  Krebs (abr/2026) e o próprio repositório `ravidsrk/slop-detect` estão
  marcados como **a verificar** em `evidencias-publicadas.md`. Não cite
  nenhum dos dois em documento de cliente até confirmar que existem.
- **D17 e a exigência de texto vivo:** evidência **FORTE**, por quatro
  razões independentes (entregabilidade, acessibilidade, resumidor de IA,
  clipping) mais observação direta na base Trendtrack.
- **D19:** decorre do comportamento documentado de inversão forçada.
- **D18:** decorre do suporte real de cliente de e-mail.

## O que este arquivo não faz

Não escolhe estrutura. A ordem das seções e a escolha da variante vêm do
`vault/componentes/_protocolo-de-selecao.md`, nove passos, eliminando
antes de rankear. Esta lista só diz o que **não** pode aparecer dentro da
variante escolhida.
