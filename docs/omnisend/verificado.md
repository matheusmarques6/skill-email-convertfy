# Verificado no Omnisend

Registro do que foi testado em conta real. **Enquanto um item não tiver
linha aqui, ele vale como `nao verificado` nas skills**, com o fallback
seguro descrito em `roteiro-de-teste.md`.

Regra: sem print, não esta verificado. Memoria de teste não conta.

## Formato

Uma seção por item. Copie o bloco abaixo e preencha.

```markdown
### T<n>. <pergunta em uma linha>

- **Data:** AAAA-MM-DD
- **Conta:** <nome da loja ou sandbox>
- **Origem:** shopify | woocommerce | bigcommerce | api
- **Testado por:** <nome>
- **Resultado:** funciona | nao funciona | parcial
- **Sintaxe que funcionou:** `<a tag exata, ou "nenhuma">`
- **Print:** `docs/omnisend/prints/T<n>-AAAA-MM-DD.png`
- **Observacao:** <o que surpreendeu, ou vazio>
- **Fecha o TODO:** sim | nao, e por que

Variantes testadas e o que cada uma devolveu:

| Variante | Resultado |
|---|---|
| `[[...]]` | <o que apareceu> |
```

Campos que não podem ficar vazios: data, conta, origem, resultado e
print. `Resultado: parcial` exige observacao dizendo o que ficou de fora.

## Prints

Em `docs/omnisend/prints/`, nome `T<n>-AAAA-MM-DD.png`. Se houver mais de
um por teste, sufixo `-a`, `-b`.

O print precisa mostrar o **e-mail recebido**, não a tela do editor. O
editor mostra o que você escreveu; o recebido mostra o que o Omnisend
resolveu, que e a pergunta.

## Estado atual

| Item | Pergunta | Estado | Data |
|---|---|---|---|
| T1 | Valor padrão para tag de contato vazia | **não verificado** | |
| T3 | Propriedade de evento como merge tag em texto | **não verificado** | |
| T4 | Link de recuperacao de carrinho, origem shopify | **não verificado** | |
| T5 | Link de retomada de checkout, origem shopify | **não verificado** | |
| T2, T6 a T10 | Ver `equivalencia-klaviyo-omnisend.md` §5 | não priorizados | |

Atualize esta tabela junto com a seção do item. Tabela e seção em
desacordo: vale a seção, e a tabela esta errada.

## Registros

<!-- as seções preenchidas entram abaixo, mais recente primeiro -->

_Nenhum ainda._
