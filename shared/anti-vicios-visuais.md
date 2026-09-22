# Anti-vícios visuais: o que só o render mostra

Série **R**. São vícios de IA que não têm marca no HTML: só aparecem
quando alguém olha a peça renderizada.

O lint estático lê o código. Estas regras leem a **imagem**. Por isso o
ciclo de `skills/email-design` obriga a abrir os três PNGs, e não apenas
a gerá-los.

Severidade: **B** bloqueia · **A** corrige · **M** julgamento.

## Como usar

```bash
python3 scripts/render.py peca.html --nome <slug>
```

Depois **abra** `desktop-600.png`, `mobile-375.png` e `dark-600.png`.
Gerar sem olhar é o mesmo que não rodar.

O `render.py` mede sozinho R01 a R10. De R11 em diante é olho humano ou
leitura de imagem pelo agente.

---

## Medidos pelo render.py

| ID | Vício | Sev. | Limiar |
|---|---|---|---|
| R01 | Peça acima de 4.000 px | **B** | É o valor que a carteira mediu como fracasso (o 11h do 9.9 tinha 4.136 px) |
| R02 | Peça acima de 3.200 px | A | Alvo é 2.000 a 3.200 |
| R03 | Peça abaixo de 800 px | A | Seção faltando, ou peça que não entrega |
| R04 | Peso acima de 102 KB | **B** | O Gmail corta |
| R05 | Container acima de 600 px | A | |
| R06 | Imagem quebrada | **B** | |
| R07 | Imagem sem alt | A | |
| R08 | Sem botão na primeira dobra do desktop | A | 900 px |
| R09 | Rolagem horizontal no mobile | **B** | Largura acima de 375 |
| R10 | Sem botão na primeira dobra do mobile | **B** | 667 px. É onde a maioria lê |

---

## Vistos na imagem: a cara de IA em layout

Estes são os que o Claude Design pega olhando, e que nenhum linter pega.

### R11. Deserto branco — A

Bloco de espaço vazio que não separa nada. Acontece quando a peça tem
menos conteúdo do que a estrutura previa: o container fica esticado e
sobra vazio no fim.

**Sinal:** no `mobile-375.png`, mais de uma tela de branco depois do
rodapé, ou entre dois blocos.

**Correção:** cortar a altura, não preencher com enfeite.

### R12. Peça anêmica — A

Tecnicamente correta e visualmente vazia: três parágrafos soltos, um
botão, nenhum peso. Passa em todo lint e não parece um e-mail de loja.

**Sinal:** a peça inteira cabe em uma tela e não tem hero, nem produto,
nem prova.

**Correção:** é defeito de estrutura, não de CSS. Voltar ao vault e
escolher variante que preveja hero e produto.

### R13. Promessa de bloco que não existe — **B**

A copy anuncia algo que o layout não entrega: "três peças que saem mais
rápido:" e depois não há grade de produto. "Veja o antes e depois" sem
imagem.

**Sinal:** frase que termina em dois-pontos e não é seguida de bloco.

**Correção:** entregar o bloco, ou cortar a frase. É o vício mais caro
porque o cliente vê a falha.

### R14. Hierarquia achatada — A

Título, corpo e legenda com peso visual parecido. A peça não diz por
onde começar.

**Sinal:** no `desktop-600.png`, apertar os olhos: se nada salta, está
achatada. Razão mínima de 2:1 entre título e corpo (D12).

### R15. Ritmo vertical irregular — M

Espaços entre blocos em valores aleatórios (14, 23, 31, 18). Dá aparência
de peça montada por tentativa.

**Correção:** uma escala só (8, 16, 24, 32, 48) e repetir.

### R16. Centralização total — M

Tudo centralizado, inclusive parágrafo corrido de quatro linhas.
Centralizar título e botão é convenção de e-mail (§8). Centralizar texto
longo é cansativo e é marca de template genérico.

### R17. Botão que não parece botão — A

Retângulo sem contraste suficiente, ou com altura abaixo de 44 px, ou
com padding tão pequeno que parece etiqueta.

**Sinal:** no `mobile-375.png`, o polegar acerta sem mirar?

### R18. Dark mode com texto invisível — **B**

No `dark-600.png`: texto que sumiu, logo preto em fundo preto, borda que
desapareceu, caixa de cupom que virou bloco sólido.

**É o defeito mais comum e o mais invisível**, porque quem monta olha só
no claro.

### R19. Dark mode com dois registros — A

Metade da peça inverteu e metade não, porque parte do texto está dentro
de imagem. A peça fica com duas temperaturas.

**Correção:** ou o texto é vivo, ou a imagem tem fundo que sobrevive à
inversão.

### R20. Grade desalinhada — A

Cards de alturas diferentes na mesma linha, preços em linhas de base
diferentes, imagem de produto em proporções diferentes.

**Sinal:** no `desktop-600.png`, a linha de baixo dos cards não fecha.

### R21. Primeira dobra sem a oferta — **B**

O botão aparece, mas o **valor, o cupom e o prazo** não. A carteira manda
oferta, cupom, prazo e botão nos primeiros 500 px.

**Sinal:** cobrir tudo abaixo de 500 px no `desktop-600.png`. Dá para
saber qual é a oferta e até quando?

### R22. Densidade de enfeite — M

Mais de dois elementos decorativos sem função (divisor ornamental, ícone
solto, faixa vazia, aspas gigantes). Cada um sozinho passa; juntos viram
a estética de template de IA.

---

## Como reportar

Na lista de problemas vistos, sempre com o ID e a captura:

```
R18 dark-600.png  o logo sumiu no topo, fundo preto em fundo preto
R13 desktop-600   "Três peças que saem mais rápido:" sem grade depois
R11 mobile-375    uma tela inteira de branco depois do rodapé
```

Achado visual sem o nome da captura não é verificável, e o revisor não
consegue conferir.

## O que NÃO é vício visual

Convenção legítima de e-mail, protegida como no `shared/calibracao.md`:

- Coluna única de 600 px, mesmo parecendo estreita no desktop.
- Título centralizado e botão centralizado.
- Caixa alta em headline curta, rótulo e botão.
- Número de oferta gigante ocupando um terço da dobra.
- Mesmo CTA repetido ao longo da peça, com o mesmo destino.
- Rodapé denso e cinza: é legal, não é descuido.
- Peça longa, quando o conteúdo é longo de verdade e cada bloco entrega.
