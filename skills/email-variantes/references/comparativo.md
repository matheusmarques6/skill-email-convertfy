# O `index.html` do comparativo

Um arquivo autocontido. Sem CDN, sem fonte remota, sem build. Abre com
duplo clique e funciona offline, porque quem decide costuma abrir no
próprio computador.

## Estrutura de pastas

```
<saida>/
  index.html
  oferta.html      variante 1
  prova.html       variante 2
  problema.html    variante 3
  dados.json       metricas por variante (opcional, ver abaixo)
```

Nome do arquivo e o nome do eixo. Não use `v1`, `v2`, `v3`: o nome tem
que dizer a aposta.

## Regras da página

1. **600px por `iframe`.** E a largura real do e-mail. Comparar em
   largura diferente esconde justamente o que quebra.
2. **Cabeçalho por coluna** com: eixo, assunto e preheader. Assunto e
   preheader decidem a abertura e não aparecem dentro do corpo, então
   precisam estar visiveis no comparativo.
3. **Linha de dados** por variante: palavras no corpo, número de CTAs,
   resultado do lint.
4. **Um botao de dark mode** que alterna as três ao mesmo tempo. Comparar
   uma clara com outra escura não compara nada.
5. **Sem vencedora.** Sem estrela, sem "recomendada", sem ordenar por
   qualidade. A ordem e sempre oferta, prova, problema.
6. A própria página de comparação segue o layout neutro da casa: fundo
   branco, texto preto. Ela não e a peca, mas cor autoral aqui contamina
   a leitura das três.

## Esqueleto

Adapte, não copie sem ler. O que importa e o contrato acima.

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Comparativo: <loja> <tipo></title>
<style>
  :root { color-scheme: light; }
  body { margin:0; padding:24px; background:#fff; color:#000;
         font:14px/1.5 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif; }
  h1 { font-size:16px; margin:0 0 4px; }
  .brief { color:#444; margin:0 0 20px; }
  .grid { display:flex; gap:20px; align-items:flex-start; overflow-x:auto; }
  .col { flex:0 0 600px; }
  .eixo { font-weight:700; text-transform:uppercase; letter-spacing:.04em;
          font-size:12px; margin-bottom:8px; }
  .campo { margin:0 0 2px; }
  .campo b { font-weight:600; }
  .dados { margin:8px 0; font-size:12px; color:#444; }
  .lint-limpo { color:#0a6b2e; }
  .lint-a { color:#8a5a00; }
  .lint-b { color:#a10000; font-weight:700; }
  iframe { width:600px; height:1400px; border:1px solid #ddd; background:#fff; }
  body.escuro { background:#121212; color:#fff; }
  body.escuro .brief, body.escuro .dados { color:#bbb; }
  body.escuro iframe { border-color:#333; }
</style>
</head>
<body>

<h1>Comparativo: &lt;loja&gt;, &lt;tipo de e-mail&gt;</h1>
<p class="brief">Leitura: &lt;a mesma linha de leitura do brief das tres&gt;</p>
<p><button onclick="document.body.classList.toggle('escuro');
   for (const f of document.querySelectorAll('iframe'))
     f.contentDocument.documentElement.classList.toggle('escuro');">
   Alternar dark mode</button></p>

<div class="grid">

  <div class="col">
    <div class="eixo">Oferta</div>
    <p class="campo"><b>Assunto:</b> &lt;assunto&gt;</p>
    <p class="campo"><b>Preheader:</b> &lt;preheader&gt;</p>
    <p class="dados">&lt;n&gt; palavras · &lt;n&gt; CTA ·
       <span class="lint-limpo">lint limpo</span></p>
    <iframe src="oferta.html" title="Variante oferta"></iframe>
  </div>

  <!-- prova e problema seguem o mesmo bloco -->

</div>

</body>
</html>
```

## `dados.json`, quando gerar

Só se o comparativo for arquivado ou entrar em relatorio. Para escolha
rapida, a linha de dados na página basta.

```json
[
  {"eixo":"oferta","arquivo":"oferta.html","palavras":62,"ctas":2,
   "lint":{"b":0,"a":0,"m":1}},
  {"eixo":"prova","arquivo":"prova.html","palavras":71,"ctas":2,
   "lint":{"b":0,"a":1,"m":0}}
]
```

## Variante reprovada

Variante com B **não entra** no `iframe`. No lugar dela, a coluna mostra
o eixo, o ID que bloqueou e o trecho:

```html
<div class="col">
  <div class="eixo">Problema</div>
  <p class="dados lint-b">Reprovada: C02, numero sem origem no brief
     ("mais de 3 mil clientes")</p>
</div>
```

Manter a coluna visível importa: mostra que o eixo foi tentado e por que
caiu. Sumir com ela faz parecer que só duas foram pensadas.
