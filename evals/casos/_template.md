---
id: <loja>-<tipo>-<aaaammdd>
loja: <nome da loja>
idioma: pt-br | en
tipo: campanha | flow-recuperacao | transacional | editorial
flow: <welcome | abandoned_cart | ...>   # so se for flow
toque: <n de N>                          # so se for flow
aprovado_por: <quem aprovou>
aprovado_em: <AAAA-MM-DD>
enviado: sim | nao
---

# <id>

Caso **bom**: e-mail real que passou por humano e foi aprovado. Serve de
referencia do que a suite deve conseguir produzir.

Caso ruim vai em `evals/ruins/`, que e outra coisa: la se mede se o lint
pega o defeito. Aqui se mede se a suite chega perto do que foi aprovado.

---

## 1. Brief

O que existia **antes** de escrever. Sem isto o caso nao serve: nao da
para medir geracao sem saber a entrada.

- **Oferta:** <valor, codigo, prazo, minimo se houver>
- **Produto:** <o que esta sendo vendido>
- **Prazo:** <data ou "por tempo limitado" com a data real>
- **Publico:** <segmento>
- **Objetivo:** <o que este e-mail precisa fazer>
- **Restricao:** <o que nao pode, vindo da ficha ou do cliente>

Ficha da marca usada: `marcas/<cliente>.md`. Se nao existir, diga.

## 2. Estrutura escolhida

- **Intencao (var1):** `<caminho da nota>`
- **Estrutura (var2):** `<caminho da nota>`
- **Variantes por secao:**

| Secao | Variante | Contrato |
|---|---|---|
| header | `<slug>` | novo / legado |
| hero | `<slug>` | |
| ... | | |

Variante legada precisa ter passado pelo adaptador. Diga se passou.

## 3. A peca aprovada

### Campos

- **Assunto:** `<...>`
- **Preheader:** `<...>`
- **CTA principal:** `<...>`
- **Alt das imagens-chave:** `<...>`

### Corpo

```
<a copy aprovada, literal, exatamente como saiu>
```

Copie literal, sem corrigir. Se tem defeito e foi aprovada assim, o
defeito faz parte do caso: e informacao sobre o criterio real de
aprovacao, que e o que interessa medir.

### HTML

`evals/casos/<id>.html`, se existir.

## 4. O que o lint diz

Rode e cole a saida, mesmo que acuse coisa.

```bash
python3 scripts/lint_copy.py  --json evals/casos/<id>.json
python3 scripts/lint_email.py --json evals/casos/<id>.html
```

```
<saida>
```

**Se o lint acusar algo numa peca aprovada, isto e o achado mais valioso
do caso.** Significa uma de duas coisas, e voce precisa dizer qual:

- a regra esta calibrada errado e gera falso positivo, e entao vira
  correcao em `shared/calibracao.md`;
- a peca tem mesmo o defeito e passou assim, e entao vira dado sobre o
  criterio real de aprovacao.

Nao conserte a peca para o lint ficar limpo. Isso destroi o caso.

## 5. Resultado, se houver

| Metrica | Valor |
|---|---|
| Enviados | |
| Abertura | |
| Clique | |
| Receita atribuida | |
| Descadastro | |
| Reclamacao | |

Abertura e metrica poluida por MPP e por resumidor. Use clique e receita
para julgar, e mantenha abertura so como serie historica.

Sem numero ainda: deixe vazio. Caso sem metrica continua util como
referencia de escrita.

## 6. Por que este caso entrou

Uma ou duas linhas. O que ele ensina que outro caso nao ensina.

Exemplos: primeira loja em ingles do acervo, oferta sem cupom, peca que
funcionou com corpo acima do teto de C45, hero sem imagem.
