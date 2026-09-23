# Teste de resultado

A pergunta: a suíte entrega para e-mail o nível que Impeccable e Taste
entregam para site, e aplica o que a carteira provou?

Dois testes, cada um com a peça da suíte (**A**) e a peça de Claude sem a
suíte (**B**), medidas pelo mesmo lint.

---

## Teste 1: welcome de joias, pt-BR

Brief: 10% OFF com cupom `BEMVINDA10`, 3 produtos, prazo de 7 dias.

### Resultado

| | A, com a suíte | B, Claude puro |
|---|---|---|
| **Copy: bloqueia** | **não** | **sim** |
| Achados de copy | **0** | **16** (2 B, 10 A, 4 M) |
| IDs de copy | nenhum | C01, C02, C11, C12, C20, C21, C26, C30, C31, C40, C41, C43, C46 |
| **HTML: bloqueia** | **não** | **sim** |
| Achados de HTML | **0** | 6 (3 B, 3 A) |
| IDs de HTML | nenhum | D02, D17, D18, E_CONTAINER, E_PREHEADER |
| Tamanho | 2.075 B | 1.593 B |
| Altura estimada | ~900 px | não medível (layout em `div`) |
| **Nota do revisor** | **8/10** | **3/10** (trava em 3 por ter B) |

### O que B fez de errado, com o ID

| Trecho de B | ID |
|---|---|
| "10% OFF na sua primeira compra **—** porque você merece" | C01, travessão |
| "Mais de 5.000 clientes já descobriram" | C02, número sem origem no brief |
| "Elegância, sofisticação e atemporalidade" | C11, tríade |
| "porque você merece o melhor" | C12, fecho de falsa profundidade |
| "algo extraordinário" | C20, superlativo vazio |
| "Sua jornada... possibilidades são infinitas" | C21, vocabulário de IA |
| "não são apenas acessórios, são a sua história" | C26 e C10, clichê e antítese |
| Preheader idêntico ao assunto | C41 |
| "Descubra agora" | C43, CTA sem objeto |
| `alt="banner"` | D17 |
| Gradiente e `-webkit-background-clip` | D02, quebra no Outlook |
| `border-radius` em `img`, `<svg>` inline | D18 |
| Container 640 px | E_CONTAINER |

---

## Teste 2: 11.11 das 07h, Blue Wolf

Brief real: `02_Calendario_Q4/Novembro/2026-11-11 0700 Você foi
selecionado (texto do fundador).md`. Papel "Fase 6, envio 2 de 5".
Oferta: até 50% + 22% extra com o cupom `1111`, até 23h59.

### Resultado

| | A, com a suíte | B, Claude puro |
|---|---|---|
| **Copy: bloqueia** | **sim** | **sim** |
| Achados de copy | **1** (1 B) | **14** (2 B, 10 A, 2 M) |
| IDs de copy | **V29** | C01, C02, C10, C21, C30, C31, C40, C41, C46 |
| **HTML: bloqueia** | **não** | **sim** |
| Achados de HTML | **0** | 6 (3 B, 3 A) |
| Tamanho | 2.190 B | 1.515 B |
| **Nota do revisor** | **3/10** (trava por ter B) | **3/10** |

### Comparação com a referência validada

| | Referência real | A, com a suíte | Mudou? |
|---|---|---|---|
| Modelo | `cupom-liberado-7h`, texto puro | igual | não |
| Família de assunto | Confirmação de algo que já é da pessoa | igual | não |
| Assunto | "Seu cupom foi liberado ✅" / "Your coupon has been released ✅" | "Your coupon has been released" | **sim: sem o ✅** |
| Preheader | "1111: 22% extra nos 24 mais vendidos. Só hoje." | igual, em inglês | não |
| Estrutura | saudação → promessa cumprida com cupom → link → alerta de estoque → assinatura | igual | não |
| CTA | "USAR MEU CUPOM" | "USE MY COUPON" | não |
| Prazo | "Vale até 23h59 de hoje" | "Valid until 11:59 PM today" | não |

**A única diferença é o emoji ✅ que o C31 removeu.** A peça da suíte
reproduz a estrutura validada bloco a bloco.

### O V29 é falso positivo aqui

A peça A bloqueou em **V29** (hora fechada em toque que não encerra o
ciclo), no trecho `11:59`.

A campanha real, validada, faz exatamente isso: o brief diz
`**Urgência:** Até 23h59` no envio das **07h**, que é o envio 2 de 5 e
não encerra nada.

**Veredito: falso positivo.** V29 deveria pegar o caso de *renovar prazo
morto* (que é V13 e V52), não o de *declarar o prazo verdadeiro da
oferta*. A regra como está impede a suíte de reproduzir a campanha de
maior receita do papel.

Proposta: V29 só dispara quando a hora declarada **não coincide** com o
prazo real da oferta no brief. Com `prazo_oferta` no payload, compara.
Sem o campo, avisa em M em vez de bloquear.

---

## Onde a peça da suíte ainda parece genérica

Honestidade obrigatória. A peça A passa no lint e **ainda tem problemas
que o lint não vê**:

1. **O teste 1 é correto e esquecível.** "Prata 925 com banho de ródio.
   Não escurece no uso diário." é informação boa, mas qualquer loja de
   prata mandaria a mesma frase. Falta o que só aquela loja tem. O lint
   mede ausência de vício, não presença de personalidade.
2. **"Três peças que saem mais rápido:" é uma promessa de prova que a
   peça não cumpre.** Sem os nomes reais dos produtos, é rótulo vazio.
   O lint não pega porque não sabe se o bloco de produto foi preenchido.
3. **O teste 2 depende de a persona existir.** "Nathan, Blue Wolf" só é
   legítimo se houver um Nathan. A suíte não tem como verificar, e o
   protocolo apenas manda declarar. É C05 refinado, ainda aguardando
   aprovação.
4. **Nenhuma das duas peças tem direção de imagem.** O hero é o que mais
   pesa na conversão e a suíte não produz brief de imagem: é a lacuna
   6e da auditoria (`imagegen` do Taste sem equivalente).
5. **A altura não é medida.** As peças da carteira têm 2.000 a 3.200 px
   e a nossa não sabe onde está. Sem isso, não dá para saber se a peça
   respeita "oferta nos primeiros 500 px".

## Conclusão

| Pergunta | Resposta |
|---|---|
| A suíte impede o vício de IA? | **Sim.** 16 e 14 achados em B contra 0 e 1 em A |
| A suíte reproduz o que a carteira validou? | **Sim, na estrutura.** A peça do teste 2 é bloco a bloco a campanha real |
| A suíte entrega o nível de Impeccable e Taste? | **Ainda não.** Impeccable produz direção visual; a suíte produz ausência de defeito. Falta direção de imagem, medição de altura e os dials |
| Alguma regra atrapalha? | **Sim.** V29 bloqueou a reprodução de uma campanha validada. C31 removeu um emoji que o dado sustenta |


---

## Reavaliação pelo padrão de qualidade

Catálogo `cat-ccfd3472`. Aplicando `shared/padrao-de-qualidade.md` às mesmas peças,
depois que o padrão passou a existir.

### Teste 1, peça da suíte: de 8/10 para **6/10**

Zero defeitos no lint, e ainda assim cai. É o ponto do padrão.

| # | Pergunta | Resposta |
|---|---|---|
| Q1 | Oferta e condição sem rolar? | **não** |
| Q2 | Diz um fato que só esta loja poderia dizer? | **não** |
| Q3 | O papel do envio está cumprido? | **não** |
| Q4 | Ação única e óbvia? | sim |
| Q5 | Funciona com as imagens desligadas? | sim |
| Q6 | Alguém da loja assina, e existe? | **não** |

**2 de 6.** Abaixo do mínimo de 5, então a nota trava em 6.

**Correção a esta tabela.** A primeira versão dela dizia Q1 e Q3 sim, e
eu a escrevi de cabeça, sem olhar o render. Rodando o revisor de verdade
sobre `desktop-600.png`:

- **Q1 é não.** O corpo diz "Use o código BEMVINDA10" e "Válido por 7
  dias, sem valor mínimo", mas **o valor 10% só existe no assunto**. Com
  o assunto fora da tela, a peça não diz de quanto é o desconto.
- **Q3 é não.** Lendo só a peça, não dá para saber que é um welcome: lê
  como um e-mail de cupom qualquer.

É o tipo de erro que o padrão existe para pegar, e que eu cometi
exatamente por não ter olhado a imagem antes de pontuar.

```
PQ2  "Prata 925 com banho de ródio" serve para qualquer loja de prata.
     Troque o nome da loja: a peça continua fazendo sentido.
PQ6  Não há assinatura. Os 4 modelos titulares do ranking são formato de
     pessoa, e este envio é um welcome, onde a apresentação importa.
```

Na Fase 5 eu escrevi que a peça era "correta e esquecível" em prosa, no
fim do relatório, como observação. Agora isso tem ID, entra no veredito e
muda a nota. Era a lacuna exata que o padrão fecha.

### Teste 2, peça da suíte: segue em 3/10

Já travava em 3 pelo V29. O padrão não muda o resultado, mas muda o
diagnóstico:

| # | Pergunta | Resposta |
|---|---|---|
| Q1 | Oferta e condição sem rolar? | sim |
| Q2 | Fato que só esta loja poderia dizer? | sim, o cupom 1111 e os 24 mais vendidos |
| Q3 | Papel cumprido? | sim |
| Q4 | Ação única? | sim |
| Q5 | Sem imagens? | sim |
| Q6 | Assina alguém real? | **não**, "Nathan" não está na ficha |

**5 de 6**, e no bloco de pico 4 de 4. A peça do teste 2 é
substancialmente melhor que a do teste 1, e antes as duas apareciam
como "sem violações".

### O que isso mostra

O lint separava peça errada de peça certa. O padrão separa peça certa de
peça boa, e as duas do teste caem em lados diferentes dessa linha.
