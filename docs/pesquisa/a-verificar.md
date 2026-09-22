# A verificar antes de virar citação

Itens que aparecem na pesquisa mas **não foram reconfirmados na fonte** neste
ambiente (sem busca web de propósito geral). Enquanto estiverem aqui, valem como
orientação interna e **não podem ser citados como fato** em skill, em SKILL.md,
em proposta para cliente nem em eval.

Origem: `docs/pesquisa/evidencias-publicadas.md`, nota metodológica e seção
"Correções e itens explicitamente não confirmados".

Como usar a tabela: cada item diz **o que reconfirmar**, **por que importa** e
**o que muda na regra se cair**. Item resolvido sai daqui e entra na regra com a
fonte no lugar.

---

## 1. Estudo de estética de IA atribuído a Adrian Krebs (abril de 2026)

- **Estado:** parcialmente apurado. O repositório `ravidsrk/slop-detect`
  **existe** (está clonado em `vendor/slop-detect`, licença MIT) e **de fato cita
  Krebs**. Isso resolve a dúvida sobre o repositório.
- **O que continua não verificado:** se o estudo de Adrian Krebs existe de
  verdade, quem o publicou, o que foi medido, com que amostra e com que método.
  A citação dentro de um repositório não é prova do estudo.
- **Por que importa:** os pesos e limiares dos 27 padrões de design do
  slop-detect (F8) alimentam D01 a D14. Se o estudo não existir, os pesos viram
  heurística de autor, não medida.
- **Se cair:** D01 a D14 continuam válidos por outro caminho (renderização,
  contraste, convenção do arsenal), mas a suite perde o direito de falar em
  "peso 7" ou "peso 8" e deve descrever os padrões sem número.

## 2. Figuras exatas de excesso de vocabulário ("delve" e afins)

- **O que reconfirmar:** Gray (2024) sobre "delve"; Kobak et al. sobre excesso de
  vocabulário em resumos do PubMed. Números exatos de sobrerrepresentação.
- **Por que importa:** é a evidência mais forte de C21 (vocabulário de IA).
- **Se cair:** improvável que caia o fenômeno; o que pode cair é o número. A
  regra C21 sobrevive sem número. **Nunca escreva o multiplicador sem o link.**

## 3. Percentuais do relatório do Email Markup Consortium (EMC)

- **O que reconfirmar:** a proporção exata de e-mails com falha de
  acessibilidade (alt ausente, contraste, idioma, semântica).
- **Por que importa:** sustenta D17 e D04/D05 como problema de mercado, não como
  preferência da agência.
- **Se cair:** D17 e D04/D05 continuam de pé por WCAG e por observação direta
  (previews de e-mail só imagem saem como OCR ilegível na Trendtrack). Só não dá
  para dizer "X% dos e-mails falham".

## 4. Limite de 102 KB do clipping do Gmail

- **O que reconfirmar:** o valor exato e se ainda é o corte atual.
- **Por que importa:** é o limiar codificado em `scripts/lint_email.py`
  (`LIMITE_CLIPPING`) com severidade B.
- **Se cair:** trocar a constante. A regra de manter a peça pequena não depende
  do dígito, mas um linter que bloqueia entrega precisa de número defensável.

## 5. Benchmarks de tamanho de assunto

- **O que reconfirmar:** a faixa recomendada por relatórios de ESP (citada como
  algo entre 30 e 50 caracteres, ou 6 a 10 palavras) e a metodologia de cada um.
- **Por que importa:** C40 usa 40 caracteres como alvo, 25 como ideal e 60 como
  corte para severidade A. O veredito da evidência é **refinada**: curto sim,
  limite exato via teste.
- **Se cair ou divergir:** os limiares de C40 mudam por teste A/B na base da
  Convertfy, não por benchmark de fornecedor. Até lá, C40 acima de 40 caracteres
  é severidade M de propósito.

## 6. Requisitos de remetente em massa do Gmail e do Yahoo (2024)

- **O que reconfirmar:** SPF, DKIM, DMARC, reclamação abaixo de 0,3% com meta
  prática abaixo de 0,1%, one-click unsubscribe (RFC 8058).
- **Por que importa:** é o pano de fundo de conformidade de toda a suite e a
  justificativa correta no lugar do mito do "filtro anti-IA".
- **Se cair:** improvável (documentação oficial), mas os números de reclamação
  aparecem em relatório e em eval, então precisam de link antes de virar meta
  contratual com cliente.

## 7. CAN-SPAM e CDC art. 37

- **O que reconfirmar:** a seção exata do CAN-SPAM que proíbe assunto enganoso e
  cabeçalho falso, e o texto do art. 37 do Código de Defesa do Consumidor sobre
  publicidade enganosa.
- **Por que importa:** é a justificativa legal de C03 (assunto que simula
  transação) e de C02 e C06. Regra severidade B citando lei precisa citar a lei
  certa.
- **Se cair a citação (não a lei):** C03, C02 e C06 continuam B por reclamação de
  spam e por confiança, mas a redação perde a menção ao artigo.

## 8. Longoni e Cian, "Word of Machine"

- **O que reconfirmar:** o artigo no Journal of Marketing e o escopo do efeito
  (escolha hedônica versus utilitária), além da linha de pesquisa sobre
  divulgação de conteúdo gerado por IA.
- **Por que importa:** é o argumento de que copy que "denuncia" IA corrói
  confiança de marca, que é uma das justificativas da suite inteira.
- **Se cair:** a suite passa a se justificar só por homogeneização observada e
  por engajamento, que já bastam.

## 9. Estudos de caso de Persado e Phrasee/Jacquard

- **O que reconfirmar:** os ganhos publicados e, principalmente, o desenho do
  teste.
- **Por que importa:** sustenta o fluxo "estratégia humana, rascunho de IA,
  edição humana, teste A/B". Atenção: o ganho vem de gerar mais testar mais
  selecionar vencedor, **não** de aceitar o primeiro rascunho do modelo.
- **Se cair:** o fluxo continua por prática de engenharia, mas some a afirmação
  de ganho percentual.

## 10. Impacto de resumos de IA na caixa de entrada

- **O que reconfirmar:** comportamento documentado do Gemini no Gmail e do Apple
  Intelligence quanto ao peso de assunto, preheader e texto vivo, e qualquer dado
  público de impacto em abertura e clique.
- **Por que importa:** é uma das quatro justificativas de C42 e D17.
- **Se cair:** C42 e D17 continuam por acessibilidade, entregabilidade e imagem
  bloqueada. Perde só um dos quatro pés.

---

## Não é item a verificar: é mito a não repetir

**"Provedor penaliza texto com alta similaridade de IA."** Não há evidência
primária e a afirmação está contrariada. Filtro age sobre reputação de IP e
domínio, autenticação, engajamento e sinal spammy clássico. Não coloque isso em
nenhuma skill, nem como hipótese. O risco real da copy homogênea é engajamento
baixo, reclamação de spam e homogeneização entre lojas, esta última observada ao
vivo: 20 de 20 lojas Shopify não relacionadas mandando o mesmo texto de
boas-vindas na Trendtrack (consulta de 22/09/2026).

## Lacunas que só teste interno resolve

Não são itens a reconfirmar, são coisas que a literatura pública não tem:

- copy de IA pura contra IA editada contra humana, com receita por e-mail, em
  e-commerce brasileiro;
- marcadores de IA em português do Brasil validados empiricamente (o léxico
  `shared/lexico/pt-br.txt` é hoje a melhor hipótese disponível, montada a partir
  de fonte secundária e anedótica, mais as rejeições reais da Convertfy);
- impacto medido da homogeneização em inbox placement;
- tamanho ótimo de assunto, preheader e corpo por tipo, na base da Convertfy.

Caminho para fechar: construir corpus interno de peças aprovadas contra
rejeitadas e medir gerundismo, conectivos e fórmulas; rodar A/B no Omnisend com
`winningMetric` em openRate ou clickRate, medindo abertura, clique, conversão,
descadastro e reclamação por variante.
