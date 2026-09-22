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
