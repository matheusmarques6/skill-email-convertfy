# Ciclo de render: olhar e corrigir

A diferença entre a suíte e uma ferramenta de design não é o HTML: é que
o designer **vê o resultado e corrige**. Sem este ciclo, o HTML sai sem
ninguém olhar.

Máximo **3 rodadas**. Se sobrar problema, entrega com a lista.

---

## A rodada

```
1. gerar o HTML
2. python3 scripts/render.py peca.html --nome <slug>
3. ABRIR os três PNGs e olhar
4. listar os problemas, cada um com ID e captura
5. corrigir
6. renderizar de novo
```

**O passo 3 é o ciclo inteiro.** Gerar PNG sem abrir é o mesmo que não
rodar: o `render.py` mede R01 a R10, e de R11 em diante só o olho pega.

## O que olhar, em cada captura

### `desktop-600.png`

| O quê | Como |
|---|---|
| Primeira dobra (R21) | Cubra tudo abaixo de 500 px. Dá para saber a oferta, o cupom e o prazo? |
| Hierarquia (R14) | Aperte os olhos. Algo salta? Razão mínima 2:1 entre título e corpo |
| Ritmo vertical (R15) | Os espaços entre blocos seguem uma escala, ou são aleatórios? |
| Grade (R20) | A linha de baixo dos cards fecha? Preços na mesma linha de base? |
| Enfeite (R22) | Mais de dois elementos decorativos sem função? |
| Deserto branco (R11) | Sobra vazio entre blocos ou depois do rodapé? |

### `mobile-375.png`

É onde a maioria lê. Defeito aqui pesa mais.

| O quê | Como |
|---|---|
| Botão na primeira dobra (R10) | O botão aparece nos primeiros 667 px? |
| Rolagem horizontal (R09) | A peça cabe em 375 px, ou corta? |
| Área de toque (R17) | O polegar acerta o botão sem mirar? Mínimo 44 px |
| Texto legível | Corpo abaixo de 14 px reprova (D26) |
| Deserto branco (R11) | Mais de uma tela de branco? |

### `dark-600.png`

O defeito mais comum e o mais invisível, porque quem monta olha só no
claro.

| O quê | Como |
|---|---|
| Texto sumido (R18) | Algum texto desapareceu? Logo preto em fundo preto? |
| Dois registros (R19) | Metade inverteu e metade não, por causa de texto dentro de imagem? |
| Caixa de cupom | Virou bloco sólido sem contraste? |
| Bordas | Sumiram? |

Esta captura emula **duas coisas ao mesmo tempo**:
`prefers-color-scheme: dark` e a **inversão forçada** que o app do Gmail
aplica em vários aparelhos. Emular só a primeira esconde metade dos
defeitos.

## Como listar o problema

Com ID e captura. Achado sem captura não é verificável.

```
R18 dark-600.png   o wordmark sumiu, preto sobre preto
R13 desktop-600    "Três peças que saem mais rápido:" sem grade depois
R10 mobile-375     botão só aparece em 980 px, abaixo da primeira dobra
R15 desktop-600    espaços de 14, 23 e 31 px entre os blocos
```

Catálogo completo em `shared/anti-vicios-visuais.md`.

## As 3 rodadas

| Rodada | O que fazer |
|---|---|
| 1 | Render completo, lista completa, corrigir tudo que for estrutural |
| 2 | Render, conferir o que foi corrigido, pegar o que a correção quebrou |
| 3 | Última. Corrigir o que der, e **entregar com a lista do que ficou** |

Depois da terceira, pare. Peça que não fecha em 3 rodadas tem problema de
estrutura ou de brief, não de CSS: diga qual dos dois e devolva.

**Nunca entregue dizendo que está limpo sem ter rodado o render.** A
lista do que ficou é parte da entrega, não uma falha dela.

## Depois do ciclo

Na ordem:

```bash
python3 scripts/lint_email.py --json peca.html
python3 scripts/lint_copy.py  --json copy.json
```

E então o **revisor em contexto limpo**: `skills/email-revisor` recebe
**apenas os três PNGs e a ficha da marca**. Não recebe o HTML, não recebe
o brief, não recebe esta lista de correções.

O motivo é o de sempre: quem participou da montagem lê a intenção, não o
resultado. O revisor precisa estar na posição de quem só recebeu o
e-mail.

## Referência visual, quando existir

Se houver `briefs/<campanha>/referencia.png`, vindo do Claude Design ou
do Figma, o ciclo ganha um passo:

```
3b. comparar desktop-600.png com a referência, lado a lado
```

Aproxime **o que dá**, respeitando as regras de e-mail. E registre o que
não dá, porque a diferença inevitável não é defeito.

### Diferenças que são limitação de e-mail, não erro

Registre assim, e não tente contornar:

| A referência tem | Por que não dá em e-mail |
|---|---|
| Gradiente de fundo ou em texto | Não renderiza no Outlook (D02, B) |
| Cantos arredondados em imagem | `border-radius` em `img` quebra no Outlook (D18, B) |
| Sombra | Removida ou quebrada em vários clientes |
| Webfont sem fallback | A maioria dos clientes cai em Helvetica ou Arial |
| SVG | Não renderiza em boa parte dos clientes (D18) |
| Grade fluida ou flexbox | E-mail é tabela. Coluna única de 600 px |
| Sobreposição de elementos | `position:absolute` não funciona (D18) |
| Animação ou hover | Não há JS, e hover não existe no celular |
| Altura de linha muito apertada | O Outlook aplica a própria |

O relatório da peça traz uma seção "Diferenças inevitáveis" com as que
apareceram. Aproximar o que dá e nomear o que não dá é o trabalho; fingir
que a peça ficou igual não é.
