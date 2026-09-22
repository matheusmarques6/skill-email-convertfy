# Conformidade de remetente em massa

Detalhe da `auditoria-omnisend`. Os três itens com evidência **FORTE** que
entram em toda auditoria, em qualquer modo.

## Por que estes três são diferentes do resto

Quase tudo numa auditoria de e-mail é julgamento calibrado por benchmark
direcional. Estes três não são.

`docs/pesquisa/evidencias-publicadas.md`, recomendação 1, *"Adote agora,
evidência forte"*: autenticação, taxa de reclamação e one-click
unsubscribe **não precisam de teste**. São conformidade e higiene.

São também a única parte da auditoria que a skill pode afirmar sem
ressalva. Tudo o mais vem com "direcional", "mercado americano" ou
"confiança baixa".

Ressalva honesta que vale para os três: a documentação de plataforma que
os sustenta está marcada como **[reconfirmar o link oficial]** no relatório
de evidências, porque não houve `web_fetch` naquele ambiente. O conteúdo é
registro público estabelecido; **reconfirme o link antes de citar em
documento de cliente.**

---

## 1. Autenticação: SPF, DKIM e DMARC

### O requisito

Remetente com mais de 5.000 mensagens por dia ao Gmail precisa de SPF,
DKIM e DMARC, a partir de fevereiro de 2024. O Yahoo adotou o mesmo
conjunto. O Outlook exige SPF, DKIM e DMARC alinhado com ao menos `p=none`
a partir de 5.000 por dia, e devolve 550 quando falta.

Detalhe técnico que costuma faltar na configuração:

| Registro | O que verificar |
|---|---|
| SPF | Termina em `-all`. Respeita o limite de 10 consultas de DNS. O domínio de envio do Omnisend está incluído |
| DKIM | 2048 bits. Rotacionado anualmente. **Alinhado** com o domínio do `From` |
| DMARC | Política publicada. Caminho de maturidade: `p=none`, depois `p=quarantine`, depois `p=reject`. Alinhamento é o que importa, não só a existência do registro |

### Como obter

**Não é obtenível pelo MCP Omnisend.** Nenhuma das operações do catálogo
retorna registro de autenticação nem estado de verificação de domínio.
`get_brands_current` devolve metadados de marca, não DNS.

Três caminhos, e o terceiro é o único que mostra a verdade:

**a) Painel do Omnisend.** Configurações de remetente: estado de
verificação do domínio. Mostra o que o Omnisend precisa e se foi
configurado. **Checar no painel.**

**b) Consulta DNS ao domínio de envio.** TXT de SPF, TXT do seletor de
DKIM, TXT em `_dmarc.<dominio>`. Mostra o que foi publicado.

**c) Cabeçalho `Authentication-Results` de um `.eml` recebido.** Mostra o
que o **receptor decidiu**, que é diferente do que foi publicado. É o
único dos três que pega alinhamento quebrado.

### O procedimento do `.eml`

O cliente precisa mandar um e-mail **como recebido**, não o HTML
pré-envio. O HTML pré-envio não tem cabeçalho de autenticação: quem
carimba é o servidor que recebe.

Como o cliente obtém:

| Cliente de e-mail | Caminho |
|---|---|
| Gmail | Abrir a mensagem, menu de três pontos, "Mostrar original", "Baixar mensagem original" |
| Apple Mail | Menu Visualizar, "Mensagem", "Origem bruta" |
| Outlook | Abrir a mensagem, "Exibir origem" |

Peça um e-mail de **campanha real**, recente, recebido numa conta Gmail.
Gmail porque é onde o requisito morde mais e onde está a maior parte da
base brasileira.

### Como ler o cabeçalho

Use o `Authentication-Results` **mais de cima**, o que o seu próprio
receptor adicionou. Os de baixo vieram de servidores intermediários e
podem ser forjados.

| Resultado | Veredito |
|---|---|
| `pass` | Aprovado |
| `fail` | Reprovado |
| `softfail`, `none`, `neutral`, `temperror`, `permerror` | Aviso |

Campos para registrar no achado: seletor e `header.i` do DKIM, domínio do
`mailfrom` do SPF, e do DMARC a política `p=`, a política de subdomínio
`sp=`, a disposição `dis=` e o `header.from`.

### Onde termina o escopo

A skill **lê e reporta** o que o provedor determinou. Ela não configura
registro, não faz aquecimento de IP e não faz pontuação de spam. Isso é do
Omnisend, do time de DNS do cliente, ou de um especialista em
entregabilidade. Sinalize e encaminhe.

---

## 2. Taxa de reclamação de spam

### Os números

| Faixa | Leitura | Ação |
|---|---|---|
| Abaixo de 0,05% | Saudável | Nenhuma |
| 0,05% a 0,1% | Atenção | Observar tendência, revisar origem de aquisição |
| **Acima de 0,1%** | **Meta prática estourada** | Pausar envio amplo. Restringir a quem clicou nos últimos 30 dias. Inspecionar origem de aquisição e descompasso de expectativa. Confirmar que o descadastro está visível |
| **Acima de 0,3%** | **Limite duro do Gmail** | Incidente. Parar campanha e escalar |

0,3% é o limite documentado do Gmail. 0,1% é a meta prática, e é o número
que a Convertfy usa como gatilho de ação, porque quando a conta chega em
0,3% o estrago já aconteceu.

### Como obter

**Parcialmente pelo MCP.**

`post_analytics_reports` tem:

- `markedAsSpamUnique`: mensagens únicas marcadas como spam
- `markedAsSpamRate`: razão sobre enviadas

`post_analytics_statistics` tem `markedAsSpamUnique`, com série temporal.

Combinação recomendada, numa requisição:

- Query 1: `markedAsSpamRate` e `unsubscribeRate` por
  `marketingActivityType`, últimos 30 dias contra os 30 anteriores.
- Query 2: `markedAsSpamUnique` e `sent` por `timestamp` semanal, para ver
  a tendência.

**O que o MCP não dá:** a taxa que o **Gmail** enxerga. O limite de 0,3% é
medido pelo Google, na base de destinatários Gmail, e vive no **Google
Postmaster Tools**. A taxa do Omnisend é uma boa aproximação e um bom
alarme, e não substitui o Postmaster.

**Checar no Postmaster Tools.** Se o cliente não tem Postmaster Tools
configurado para o domínio de envio, isso é achado próprio, de esforço
baixo e impacto alto: sem ele, ninguém enxerga o número que decide se o
Gmail vai bloquear.

### Interpretação

Volume baixo distorce a taxa. Uma campanha para 300 pessoas com 1
reclamação marca 0,33% e não significa nada. Registre confiança baixa
abaixo de alguns milhares de envios e diga isso no achado.

Reclamação subindo junto com descadastro é descompasso de expectativa:
origem de aquisição ruim, promessa de captura que o e-mail não cumpre, ou
frequência acima do combinado. Reclamação subindo **sem** descadastro subir
costuma ser descadastro difícil de achar, e o remédio é tornar o link
visível.

---

## 3. One-click unsubscribe (RFC 8058)

### O requisito

Exigido para remetente em massa pelo Gmail e pelo Yahoo, e pelo Microsoft
a partir de 5.000 por dia. São dois cabeçalhos, e os dois precisam estar
lá:

```
List-Unsubscribe: <https://...>, <mailto:...>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
```

Só o `List-Unsubscribe` não basta: sem o `List-Unsubscribe-Post`, o
provedor não mostra o botão de descadastro de um clique.

O pedido precisa ser honrado em poucos dias. A prática recomendada é
dentro de 48 horas.

### Como obter

**Não é obtenível pelo MCP Omnisend.** Nenhuma operação retorna cabeçalho
de mensagem enviada.

Duas checagens diferentes, que não se substituem:

| Checagem | Onde | O que prova |
|---|---|---|
| Link de descadastro no **corpo** | MCP: `get_email_content_id` | Que existe o link clicável dentro do e-mail. O Omnisend rejeita conteúdo sem ao menos um bloco de texto ou HTML com `[[unsubscribe_link]]`, então isso é quase sempre verdade |
| Cabeçalho `List-Unsubscribe-Post` | `.eml` recebido | Que o botão de um clique aparece na interface do provedor. **Esta é a checagem de conformidade** |

O `[[unsubscribe_link]]` garantido no corpo **não** implica o cabeçalho.
São coisas diferentes, e só a segunda cumpre a RFC 8058.

Use o mesmo `.eml` coletado para a checagem de autenticação. Uma coleta
resolve as duas.

### Checagens complementares no corpo

Enquanto o `.eml` não chega, o que dá para verificar pelo MCP e pelo HTML:

- O link de descadastro **resolve**, não é placeholder nem `#`.
- O link não está abaixo do corte de clipping do Gmail. Peça acima de
  ~102 KB pode esconder o descadastro, e aí o problema deixa de ser
  conversão e vira conformidade.
- Existe bloco de identidade do remetente e endereço físico, onde exigido.
- O link está visível, não em cinza claro de 9px no fim do rodapé.
  Descadastro difícil de achar é o que produz reclamação de spam, que é
  pior para a conta do que o descadastro.

---

## O que escrever no relatório

Modelo para as três checagens, quando o dado não veio do MCP:

```yaml
checagem: entrega.autenticacao
dimensao: entregabilidade_conformidade
status: nao_verificavel
pontos: 5
evidencia: >
  Nenhuma operação do MCP Omnisend retorna registro de autenticação
  ou estado de verificação de domínio. get_brands_current retorna
  metadados de marca (plataforma, site, moeda), não estado de DNS.
fonte: catálogo de operações do MCP Omnisend, consultado em <data>
observado_em: <ISO-8601>
confianca: alta
impacto: >
  Requisito de remetente em massa do Gmail e do Yahoo para volume
  acima de 5.000 por dia. Sem SPF, DKIM e DMARC alinhado, a entrega
  degrada e o Outlook devolve 550.
acao: >
  1. Checar no painel do Omnisend, em Configurações de remetente, o
     estado de verificação do domínio.
  2. Consultar o DNS do domínio de envio: SPF, seletor de DKIM e _dmarc.
  3. Pedir ao cliente um .eml de campanha recente recebido no Gmail e
     ler o Authentication-Results mais de cima.
esforco: baixo
```

**Nunca** transforme `nao_verificavel` em reprovação. E nunca deixe
`nao_verificavel` sem a lista de ações: é isso que separa uma auditoria de
uma reclamação.

---

## Nota sobre o que esta seção NÃO afirma

Não existe evidência primária de que Gmail, Yahoo ou Outlook detectem e
penalizem texto por "parecer gerado por IA". Isso é **especulação**.

Os filtros agem sobre reputação de IP e de domínio, autenticação,
engajamento e sinais spammy clássicos. É por isso que esta seção existe:
os três itens acima são o que de fato move o filtro.

Quando a copy homogênea for o problema, o argumento correto é
**engajamento baixo, reclamação de spam e homogeneização entre lojas**. A
homogeneização é real e observada: 20 de 20 lojas Shopify não relacionadas
na base Trendtrack mandando o mesmo texto de boas-vindas quase idêntico.
