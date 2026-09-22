---
cliente: blue-wolf
dominio: wolfbluestore.com
idioma: en
moeda: USD
esp: omnisend
nivel_conta: A
tipografia_principal: Montserrat
fonte_secundaria: Tusker Grotesk 5500 Medium
cor_primaria: "#29506D"
cor_secundaria: "#4588B9"
marca_usa_emoji: true
container_px: 600
altura_alvo_px: [2000, 3200]
media_por_mil_trimestre_usd: 43.58
endereco: "[FALTA: endereco fisico do remetente, exigido por CAN-SPAM]"
---

# Blue Wolf

Loja da carteira com mais dado no estudo BFCM: 46 campanhas medidas entre
17/06 e 17/09/2026. Média do trimestre: **US$ 43,58 por mil envios**, que
é o índice 1 desta loja.

Fonte: `fontes/BFCM-2026-Convertfy/07_Design_Blue_Wolf/` e
`09_Dados/Base de dados do estudo (dicionario e metodo).md`, seção B.3.

## Tom e público

Idioma **inglês**. Assunto em Title Case é convenção, não vício: C34 não
se aplica aqui (ver `docs/decisoes.md`, D-005).

Registro: exclusivo e formal nos momentos de acesso restrito, direto e
alto contraste no pico. Nunca infantil.

## Tipografia

- **Tipografia principal: Montserrat** (Regular, Medium, SemiBold, Bold).
  Corpo, botões, legendas e preços.
- **Fonte secundária: Tusker Grotesk 5500 Medium.** Títulos de seção em
  caixa alta condensada. Alternativa: Anton ou Bebas Neue.
- Display: Stretch Pro, para nome de evento e número grande. Alternativa:
  Unbounded ou Syncopate.
- Apoio: Staatliches, para etiqueta e pílula.
- Wordmark: "Blue Wolf" em Montaga Regular.

Escala mínima em 600 px: corpo 15 a 16 px, legenda 12 px, título de seção
30 a 40 px, número de oferta 70 a 110 px.

**Em e-mail, a maioria dos clientes cai no fallback** (Helvetica, Arial).
Tipografia da marca vale para o que é imagem; o texto vivo usa a pilha de
fallback.

## Cores

- **Cor primária: `#29506D`** (navy Blue Wolf). Título em fundo claro
  também usa `#284D68`.
- **Cor secundária: `#4588B9`** (azul aço). Botões e destaques.
- Escuro de apoio: `#010115`. Branco: `#FFFFFF`.
- Alerta: `#E05252`, **só em aviso de sistema**.
- Cinza de texto secundário: `#64748B`.

### Paleta por momento

A marca não muda: tipografia, wordmark, rodapé e a cor primária ficam
iguais o trimestre inteiro. **Mudam o fundo, o acento e o clima.**

| Momento | Datas | Acento | Fundo |
|---|---|---|---|
| 10.10 Perfect 10 | 01 a 13/10 | `#C9A45C` dourado | Gradiente `#1E3A52` → `#29506D` |
| Lista de espera e Pré-Black | 14 a 24/10 | `#FFFFFF` | `#010115` com brilho azul |
| Halloween | 25/10 a 01/11 | `#C8662B` laranja queimado, só em detalhe | `#121212` |
| 11.11 Black Antecipada | 02 a 16/11 | `#C7CED6` prata | `#010115` → `#0E2233` |
| Black Week | 17 a 29/11 | `#F2C200` amarelo de fita | `#000000` |
| Cyber | 30/11 a 02/12 | `#4588B9` | `#010115`, secundária vira `#35C8FF` |
| 12.12 e Natal | 03 a 22/12 | `#C9A45C` dourado | `#F6F1E7` creme nas seções de texto |
| Boxing Day | 26/12 | `#9E2B34` | `#29506D` |
| Fim de ano | 27 a 31/12 | `#FFFFFF` | `#0B0B0F`, secundária `#C9A45C` |

### A exceção que vence tudo

**Aviso de sistema é sempre fundo branco, texto preto**, em qualquer
momento e em qualquer marca: notificação do futuro, aviso de estoque,
"Lamentamos informar".

Motivo: foi o visual de maior clique do trimestre (**3,61% e 3,20%**). A
cara de sistema é o que faz o e-mail funcionar, e cor da marca atrapalha.

Esta regra vence a paleta por momento e vence a ficha.

## Componentes fixos

1. Cabeçalho: wordmark centralizado sobre o hero, cerca de 90 px.
2. Pílula de etiqueta em Staatliches, caixa alta, sobre o título.
3. Pílulas de horário (00h · 07h · 11h · 18h), iguais em toda antecipação.
4. Caixa de cupom: rótulo "COUPON:" mais código, sempre perto do botão.
5. Botão principal: caixa alta Montserrat Bold, mínimo 44 px de altura,
   **um por e-mail**.
6. Grade de produtos 2x2 com foto, nome, preço e botão.
7. Mockups de celular: sempre o mesmo aparelho e o mesmo papel de parede
   navy com o wordmark.

## Técnica

- 600 px de largura, exportar em 2x.
- Altura de **2.000 a 3.200 px**. Acima de 4.000 px é o que a carteira
  mediu como fracasso (o 11h do 9.9 tinha 4.136 px).
- Oferta, cupom, prazo e botão nos **primeiros 500 px**.
- Um botão principal.
- Blocos que dá para fatiar.

## Palavras proibidas desta marca

Herda o léxico geral. Sem restrição adicional declarada.

## Restrições legais

Mercado principal EUA e UK. Preço de referência precisa ser legal em UE
quando a campanha for para lá. CAN-SPAM: endereço físico e descadastro
funcional obrigatórios.
