# Dark mode

Detalhe da `email-design`. Regra D19 e o que ela não cobre.

Dark mode é a área de maior risco de renderização em e-mail. Pixel-perfect
em todos os clientes é **impossível**. O objetivo é **robusto e gracioso**,
não idêntico.

## Combinar antes de construir

Três decisões que precisam estar tomadas antes de escrever HTML, e
registradas no `marcas/<cliente>.md`:

1. **Os três comportamentos de motor de dark mode:** sem alteração,
   inversão parcial, inversão total. A meta é consistência, não perfeição.
2. **A estratégia de cabeçalho e logo.** O padrão mais seguro é cabeçalho
   escuro com logo claro, porque um logo escuro sobre fundo invertido
   desaparece.
3. **A lista de clientes que a peça precisa suportar**, e onde limites
   documentados vão ser aceitos.

Sem essas três, a discussão vira retrabalho depois do envio.

## Primeiro passo da revisão: dark mode está sendo mirado?

Antes de julgar qualquer cor, procure as duas metas no `<head>`:

```html
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
```

| Estado | Leitura |
|---|---|
| Presentes | A peça **declara** suporte. Precisa ser provada em modo escuro |
| Ausentes | A peça **não mira** dark mode. Os clientes vão decidir sozinhos, em geral invertendo à força. Sinalize e decida com o brief se isso é aceitável |

Ausência não é automaticamente erro. Ausência **não declarada** é.

## As cores

| Regra | Valor |
|---|---|
| Fundo escuro | `#121212`. **Nunca `#000000` puro** |
| Logo | Versão para fundo escuro, ou cabeçalho escuro por padrão |
| Cor de texto | Sempre explícita. Cor herdada é o que some |
| Cor de botão e do texto do botão | Sempre explícitas, e julgadas juntas |

O `skill-email-html-mjml` sugere também `#F1F1F1` no lugar de branco puro
para o claro. **Não adotamos:** o CLAUDE.md manda fundo branco. Se algum
dia isso mudar, a mudança vem do vault, não da skill.

## Fixo-escuro contra adaptativo

Distinção que vem do `email-html-qa-skill` e que evita o erro mais sutil
da área.

| Tipo | O que é | Como tratar |
|---|---|---|
| **Fixo-escuro** | O elemento já é escuro no modo claro e precisa renderizar **idêntico** no escuro | Gradiente como cor sólida, com wrap de blend-mode |
| **Adaptativo** | O elemento é claro por padrão e deve inverter **de propósito** no escuro | Classe de dark mode com override deliberado |

**Nunca misture as duas técnicas no mesmo elemento.** É a fonte mais comum
de resultado imprevisível.

## Logo e ícone transparentes

O caso concreto que mais quebra:

Um PNG transparente com arte escura (logo em preto, ícone social em
cinza-escuro) afunda no fundo escuro e **desaparece**. O elemento continua
lá, ocupando espaço, invisível.

Três correções, nesta ordem de preferência:

1. **Chip de fundo:** uma caixa clara ou na cor da marca, com padding,
   atrás do logo.
2. **Cabeçalho deliberadamente escuro com logo claro.** É o padrão mais
   seguro, porque funciona nos dois modos sem truque.
3. **Troca de imagem por media query.** Funciona principalmente no iOS, e
   depende de CSS que vários clientes removem. Trate como reforço, nunca
   como única defesa.

O lint sinaliza imagem em risco (transparente, tamanho de ícone, sem fundo
atrás). Só a prova em modo escuro confirma. Imagem sinalizada em geral
significa voltar ao design para pedir uma variante.

## Botão colorido

O caso número um de quebra em Gmail no modo escuro forçado: **o texto do
botão some.**

- Julgue **cada** botão pela própria combinação de preenchimento e texto.
- Nunca assuma que um truque de blend-mode funciona sobre preenchimento
  claro ou colorido.
- Teste o botão principal separadamente dos secundários.

## Contraste depois da inversão

Contraste que passa no modo claro pode reprovar no escuro. Confira o par
**contra o fundo invertido**, não contra o original.

Mínimo 4,5:1 nos dois modos.

## Matriz de prova

Preencha por envio. Registre `passa`, `problema` ou `limite documentado`
em cada célula.

| Superfície | Gmail (app, escuro forçado) | Outlook Windows | Outlook Mac | Apple Mail e iOS | Android |
|---|---|---|---|---|---|
| Fundo geral e superfícies | | | | | |
| Contraste do corpo | | | | | |
| **Logo no escuro** | | | | | |
| Cabeçalho ou banner | | | | | |
| **Botão colorido, texto visível** | | | | | |
| Links e CTAs secundários | | | | | |
| Imagens e fotos de produto | | | | | |
| Divisores e bordas | | | | | |

## Células de maior risco

Olhe primeiro:

1. **Gmail escuro forçado em botão colorido.** O texto some.
2. **Outlook para Mac.** Teste separado do Windows e do Apple Mail. Não
   assuma que são iguais.
3. **Logo no escuro.** Wordmark escuro desaparece.
4. **Plataformas que não aplicam o seu CSS de dark mode.** Alguns ESPs e
   plataformas removem as classes e as media queries em que você está
   apostando. **Verifique na plataforma real**, não no preview do editor.

O item 4 vale em dobro para nós: a prova precisa sair do Omnisend, com
`post_automations_id_blocks_block_id_test_email` ou
`post_campaigns_id_test_email`, e não do HTML local.

## Registro por peça

```
Loja:
Peça:
Estratégia de logo:      [cabeçalho-escuro-logo-claro / classe-dark / troca-de-logo]
Clientes obrigatórios:
Data do teste:
Limites aceitos:         [ex.: "troca de logo não funciona fora do iOS, aceito"]
Problemas abertos:       [lista, por severidade]
```

Guarde o registro junto da peça. A próxima pessoa que mexer nessa conta
precisa saber o que já foi decidido e o que já foi aceito como limite.

## Aviso de validade

Motores de renderização e de dark mode mudam. Novo Outlook, atualização de
Gmail, versão de Apple Mail. Trate comportamento específico de cliente como
informação com prazo de validade e reconfirme quando algo mudar, em vez de
refazer a peça do zero.
