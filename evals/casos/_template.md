---
id: <loja>-<tipo>-<aaaammdd>
loja: <nome da loja>
idioma: pt-br | en
tipo: campanha | flow-recuperacao | transacional | editorial
flow: <welcome | abandoned_cart | ...>   # só se for flow
toque: <n de N>                          # só se for flow
aprovado_por: <quem aprovou>
aprovado_em: <AAAA-MM-DD>
enviado: sim | não
---

# <id>

Caso **bom**: e-mail real que passou por humano e foi aprovado. Serve de
referência do que a suite deve conseguir produzir.

Caso ruim vai em `evals/ruins/`, que e outra coisa: la se mede se o lint
pega o defeito. Aqui se mede se a suite chega perto do que foi aprovado.

---

## 1. Brief

O que existia **antes** de escrever. Sem isto o caso não serve: não da
para medir geração sem saber a entrada.

- **Oferta:** <valor, código, prazo, mínimo se houver>
- **Produto:** <o que esta sendo vendido>
- **Prazo:** <data ou "por tempo limitado" com a data real>
- **Público:** <segmento>
- **Objetivo:** <o que este e-mail precisa fazer>
- **Restrição:** <o que não pode, vindo da ficha ou do cliente>

Ficha da marca usada: `marcas/<cliente>.md`. Se não existir, diga.

## 2. Estrutura escolhida

- **Intencao (var1):** `<caminho da nota>`
- **Estrutura (var2):** `<caminho da nota>`
- **Variantes por seção:**

| Seção | Variante | Contrato |
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
defeito faz parte do caso: e informação sobre o critério real de
aprovação, que e o que interessa medir.

### HTML

`evals/casos/<id>.html`, se existir.

## 4. O que o lint diz

Rode e cole a saída, mesmo que acuse coisa.

```bash
python3 scripts/lint_copy.py  --json evals/casos/<id>.json
python3 scripts/lint_email.py --json evals/casos/<id>.html
```

```
<saida>
```

**Se o lint acusar algo numa peca aprovada, isto e o achado mais valioso
do caso.** Significa uma de duas coisas, e você precisa dizer qual:

- a regra esta calibrada errado e gera falso positivo, e então vira
  correção em `shared/calibracao.md`;
- a peca tem mesmo o defeito e passou assim, e então vira dado sobre o
  critério real de aprovação.

Não conserte a peca para o lint ficar limpo. Isso destroi o caso.

## 5. Resultado, se houver

| Métrica | Valor |
|---|---|
| Enviados | |
| Abertura | |
| Clique | |
| Receita atribuida | |
| Descadastro | |
| Reclamação | |

Abertura e métrica poluida por MPP e por resumidor. Use clique e receita
para julgar, e mantenha abertura só como serie historica.

Sem número ainda: deixe vazio. Caso sem métrica continua útil como
referência de escrita.

## 6. Por que este caso entrou

Uma ou duas linhas. O que ele ensina que outro caso não ensina.

Exemplos: primeira loja em ingles do acervo, oferta sem cupom, peca que
funcionou com corpo acima do teto de C45, hero sem imagem.
