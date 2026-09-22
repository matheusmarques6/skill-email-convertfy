# Ler o `.eml`: autenticacao e one-click unsubscribe

Uma coleta resolve dois itens que nenhuma outra fonte entrega: se SPF,
DKIM e DMARC passaram de verdade **naquele envio**, e se o one-click
unsubscribe esta no cabecalho.

O MCP do Omnisend nao entrega nenhum dos dois. Ele garante
`[[unsubscribe_link]]` no corpo, que e outra coisa: link no corpo nao e
`List-Unsubscribe-Post`.

---

## Coletar

Envie um teste da campanha para uma caixa sua e baixe a mensagem crua.

| Cliente | Caminho |
|---|---|
| Gmail (web) | Abrir a mensagem, menu de tres pontos, "Fazer download da mensagem" |
| Apple Mail | Selecionar a mensagem, arrastar para o Finder |
| Outlook (desktop) | Arquivo, Salvar como, tipo "Formato de email" |

Gmail tambem mostra "Exibir original" sem baixar, e ja traz SPF, DKIM e
DMARC resumidos no topo. Serve para conferencia rapida; para o registro
do laudo, prefira o arquivo.

## Ler autenticacao

Procure `Authentication-Results`. Os tres precisam estar em `pass`:

```
Authentication-Results: mx.google.com;
       dkim=pass header.i=@loja.com.br;
       spf=pass smtp.mailfrom=loja.com.br;
       dmarc=pass header.from=loja.com.br
```

**Leia sempre o cabecalho de cima.** A mensagem acumula um
`Authentication-Results` por servidor no caminho, e os de baixo vem de
antes da entrega: podem ter sido escritos pela propria origem. O de cima
e do servidor que recebeu, e e o unico que vale.

Interpretacao:

| Resultado | Leitura |
|---|---|
| `spf=fail` | O envio nao esta autorizado pelo DNS do dominio |
| `dkim=fail` | Assinatura invalida ou chave errada no DNS |
| `dmarc=fail` | SPF e DKIM podem ate passar, mas nao alinham com o `From` |
| `dmarc=none` | Nao ha politica publicada. Nao e `pass` |

`dmarc=none` e o caso mais comum e o mais mal lido: o dominio nao tem
politica, entao nao ha o que falhar. Registre como pendencia, nunca como
aprovado.

## Ler one-click unsubscribe (RFC 8058)

Os dois cabecalhos precisam existir:

```
List-Unsubscribe: <https://...>, <mailto:...>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
```

- Sem `List-Unsubscribe-Post`, nao ha one-click, mesmo havendo
  `List-Unsubscribe`.
- O valor precisa ser exatamente `List-Unsubscribe=One-Click`.
- O `List-Unsubscribe` precisa ter uma URL `https`, nao so `mailto`.

Isso e exigencia de remetente em massa do Gmail e do Yahoo desde
fevereiro de 2024, para quem passa de 5.000 mensagens por dia.

## Registrar

Sem `.eml`, o veredito traz:

```
Nao verificado: autenticacao e one-click, sem .eml
```

Nunca `aprovado`. Nao afirme que uma checagem passou sem evidencia.
