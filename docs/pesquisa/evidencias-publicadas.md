# Pesquisa profunda: evidências para uma skill anti-"cara de IA" em e-mail marketing de e-commerce (Convertfy)

**A maioria das regras propostas para a skill está confirmada ou refinada pela evidência disponível; a exceção importante é a premissa de que provedores penalizam "texto com cara de IA" diretamente, para a qual não há evidência primária.** O risco real da copy homogênea é indireto (baixo engajamento, reclamação de spam, homogeneização entre lojas), e a skill deve justificar suas regras por esse caminho, não por um "detector de IA no filtro".

## Nota metodológica e de honestidade epistêmica (leia primeiro)

Este relatório foi produzido em um ambiente cujo conjunto de ferramentas **não inclui busca web de propósito geral**. Ele tem acesso direto e verificável a: (a) documentação oficial da API do Omnisend (ESP principal da Convertfy) e (b) uma base de inteligência de e-mails reais de e-commerce (Trendtrack). Todas as afirmações baseadas nessas duas fontes foram verificadas ao vivo e estão datadas (consulta em 22/09/2026).

As afirmações baseadas na **literatura publicada** (estudos acadêmicos, relatórios de ESP, documentação de Gmail/Apple/Yahoo, estatutos legais) refletem o registro público conhecido e estabelecido dessas fontes, **mas não puderam ser re-verificadas linha a linha neste ambiente** (sem web_fetch). Cada uma dessas está marcada como **[literatura publicada — reconfirmar link antes de citar na skill]**. Isto é uma limitação de ferramenta, não de disponibilidade da fonte: todas essas fontes existem publicamente e devem ser confirmadas com um clique antes de virar citação na skill. A força de evidência (forte/moderada/fraca/especulação) reflete o rigor da fonte original, não a confiança da re-verificação aqui.

## TL;DR

- A maioria das regras da skill está **confirmada ou refinada** por evidência: os marcadores linguísticos de IA são empiricamente reais e quantificados na literatura (excesso de "delve"/"delves", travessão, tríades, baixa "burstiness"); os requisitos de remetente em massa do Gmail/Yahoo de 2024 são fato documentado; e a homogeneização de copy é **observável ao vivo** (20 de 20 lojas Shopify não relacionadas enviando o mesmo texto de boas-vindas quase idêntico na base Trendtrack).
- **Nenhuma evidência primária** mostra que Gmail/Yahoo/Outlook penalizem diretamente "texto com alta similaridade de IA"; classifique isso como **especulação** e reposicione a regra em torno de engajamento e reclamação.
- As maiores **lacunas de evidência pública** são três e exigem teste A/B interno da Convertfy: (a) testes limpos de copy IA-pura vs IA-editada vs humana com receita por e-mail; (b) marcadores de IA em português brasileiro; (c) impacto quantificado de resumos de IA (Gemini/Apple Intelligence) sobre abertura/clique.

## Achados principais por pergunta

### 1. Copy de IA vs copy humana

- **Fornecedores de IA de linguagem (Persado, Phrasee/Jacquard):** publicam estudos de caso com ganhos de engajamento de copy otimizada por IA vs controle humano, tipicamente em dois dígitos percentuais de clique/conversão. Força: **moderada** — a fonte é o próprio fornecedor (viés de publicação), e a comparação é "IA otimizada por experimentação" vs "humano", **não** "IA generativa pura" vs "humano". **[literatura publicada / material de fornecedor — reconfirmar]**
- **Distinção crítica para a skill:** o ganho histórico desses fornecedores vem de **geração + teste A/B + seleção do vencedor**, não de aceitar o primeiro rascunho de um LLM generativo. Isso apoia diretamente o fluxo "estratégia humana → rascunho IA → edição humana → teste". Força: **moderada**.
- **Percepção do consumidor / aversão a IA:** o efeito "Word of Machine" (Longoni & Cian, *Journal of Marketing*) mostra que recomendações rotuladas como de IA são menos valorizadas para escolhas hedônicas/experienciais; e a linha de pesquisa sobre **divulgação (disclosure)** indica que revelar que um conteúdo foi gerado por IA tende a reduzir confiança e credibilidade percebidas. Implicação: texto que "denuncia" IA pode corroer confiança de marca. Força: **moderada a forte** (acadêmica, mas nem sempre no contexto de e-mail de e-commerce). **[literatura publicada — reconfirmar]**

### 2. Entregabilidade e IA

- **Requisitos de remetente em massa Gmail/Yahoo (a partir de fevereiro de 2024):** para remetentes de mais de 5.000 mensagens/dia ao Gmail, exigência de SPF + DKIM + DMARC; taxa de reclamação de spam **abaixo de 0,3%** (com meta prática **abaixo de 0,1%**, medida no Google Postmaster Tools); e **one-click unsubscribe** (RFC 8058) processado em poucos dias. Força: **forte** (documentação oficial Google/Yahoo). É o pano de fundo regulatório obrigatório da skill. **[documentação de plataforma — reconfirmar link oficial]**
- **Filtragem por "similaridade de IA":** **não há evidência primária** de que Gmail, Yahoo ou Outlook detectem e penalizem texto por "parecer gerado por IA". Filtros agem sobre reputação de IP/domínio, autenticação, engajamento e sinais spammy clássicos. Veredito: **especulação**. Reposicione a regra: o risco da copy homogênea é engajamento baixo e reclamação, não um filtro anti-IA. Força do fato negativo: **moderada**.
- **Homogeneização de copy (evidência direta ao vivo):** na base Trendtrack, a busca por "we're só happy you're here" (intenção welcome, últimos 90 dias) retornou **20 de 20 resultados com o mesmo template verbatim**, em lojas Shopify totalmente não relacionadas: Long Studio Design, For Little Kiwis, Chemo-Hats, Bijouterie Classique, Thorness, Jonny's Place, BuckedOff, Zombie Sport Co (ID 9669270, 27/07/2026), Flawn Seed Kits (floweringlawn.com, ID 10697749, 02/09/2026), Gretachic, EVERSINCE, Matty's Crafting Joy, Prisa Enterprises, Uncle Keith's Red Sauce (ID 10750831, 04/09/2026), DCVOLTAGE, Kristen's Book Boutique, SheltonShirts. Copy recorrente: *"Welcome / Hey, we're só happy you're here! Enjoy this discount on your first purchase. / SPECIAL OFFER / Apply discount / Bestsellers."* Isto demonstra que a "cara de template" já é epidêmica **antes mesmo** de IA generativa; a IA generativa amplifica o problema. Força: **forte** (observação empírica direta, Trendtrack, 22/09/2026). Ressalva: não há medição publicada do impacto disso em inbox placement.

### 3. Resumos de IA na caixa de entrada

- **Gemini (Gmail) e Apple Intelligence (iOS 18):** ambos resumem a partir de **texto** (corpo HTML vivo, com peso alto de assunto e preheader). E-mails majoritariamente de imagem oferecem pouco texto para o resumo, deixando-o pobre ou dependente só de preheader/alt. Força: **moderada** (comportamento documentado em termos gerais; falta dado público de impacto em abertura/clique). **[literatura publicada / relatórios de ESP — reconfirmar]**
- Apple Intelligence enfrentou problemas públicos de precisão em resumos no início de 2025, reforçando: não confie no resumo automático; controle a primeira linha de texto vivo e o preheader. Força: **moderada**. **[literatura publicada — reconfirmar]**
- **Recomendação prática:** todo e-mail deve ter (a) preheader específico com a oferta em texto, (b) uma primeira seção em HTML de texto vivo com proposta e condição da oferta, (c) alt text descritivo em cada imagem-chave. Serve simultaneamente a resumidores de IA, acessibilidade, dark mode e clipping.

### 4. Padrões linguísticos de IA (evidência empírica)

- **Vocabulário superrepresentado:** análises de frequência em textos científicos pós-ChatGPT mostram salto abrupto de certas palavras. O trabalho de Andrew Gray (2024) sobre "delve" e o estudo de Kobak et al. sobre "excesso de vocabulário" em resumos do PubMed quantificam termos como *delve/delves/delving, showcasing, underscores, crucial, pivotal, realm, intricate, boasts, leveraging, notably*. Força: **forte** (acadêmica, grandes corpora). **[literatura publicada — reconfirmar figuras exatas de excesso antes de citar]**
- **Travessão (em dash):** uso pesado é marcador amplamente relatado de texto de LLM. Força: **moderada** (muitos relatos e algumas análises de frequência; menos rigor que a lista de "delve").
- **"Not X but Y", tríades (rule of three), uniformidade de frase, baixa burstiness/perplexity:** LLMs tendem a frases de comprimento uniforme e baixa perplexidade, e abusam de paralelismos e listas de três. "Slop scores" e forense de slop (trabalho associado a Sam Paech / EQ-Bench) medem esse excesso. Força: **moderada a forte**. **[literatura publicada / repositórios — reconfirmar]**
- **Estudo de estética de IA (Adrian Krebs, abril de 2026) e repo ravidsrk/slop-detect:** **NÃO VERIFICÁVEL neste ambiente** (sem busca web). Trate como **a verificar** e não cite na skill até confirmar (i) que o estudo de Adrian Krebs existe, (ii) seus achados sobre padrões de landing pages geradas por IA, e (iii) que o repositório ravidsrk/slop-detect de fato o referência. Força: **a verificar / não confirmada**.
- **Português brasileiro:** **nenhuma pesquisa acadêmica localizável** sobre marcadores de IA em pt-BR neste ambiente. Sinais anedóticos/de blog conhecidos: gerundismo excessivo ("vamos estar enviando"), conectivos superusados ("além disso", "portanto", "no entanto", "dessa forma"), fórmulas ("vale ressaltar", "em suma", "em um mundo cada vez mais", "não é apenas... é"), e tradução literal do inglês. Força: **fraca** (secundária/anedótica). Lacuna clara para teste interno.

### 5. Boas práticas de copy com dados

- **Tamanho de assunto:** benchmarks de ESP recomendam assuntos curtos (faixa frequentemente citada de ~30 a 50 caracteres, ou ~6 a 10 palavras) por truncamento em mobile. Força: **moderada** (metodologias variam). A regra da skill de ≤25 a 40 caracteres é agressiva mas defensável para mobile. **[relatórios de ESP — reconfirmar]**
- **Especificidade vs genérico:** números reais, nome de produto e condição concreta da oferta superam superlativos vagos. Força: **moderada** (princípio bem estabelecido de copywriting + testes de ESP).
- **Urgência real vs falsa:** urgência genuína (prazo/estoque reais) aumenta conversão; urgência falsa recorrente corrói confiança e eleva reclamação/descadastro ao longo do tempo. Força: **moderada**.
- **Assuntos enganosos ("RE:", "Seu pedido foi aprovado"):** geram abertura de curto prazo mas aumentam reclamação de spam e são risco legal. **CAN-SPAM (EUA) proíbe linhas de assunto enganosas e cabeçalhos falsos**, com multa civil por e-mail em violação; a FTC fiscaliza. No Brasil, o **CDC proíbe publicidade enganosa (art. 37)**. Força: **forte** (estatutária). **[estatutos — reconfirmar seção/artigo exato]**
- **Emojis, exclamação, caixa alta, personalização por nome:** dados de ESP são mistos; personalização por nome no assunto tem efeito pequeno e às vezes negativo; excesso de exclamação/caixa alta correlaciona com aparência spammy. Força: **fraca a moderada**.
- **Número de CTAs:** um CTA principal por e-mail tende a superar múltiplos CTAs competindo. Força: **moderada** (forte suporte de UX; menos testes de e-mail publicados limpos).
- **Copy curta vs longa / storytelling vs oferta direta:** depende do tipo e da fase do fluxo; oferta direta vence em promocional/carrinho, storytelling ajuda em welcome/brand. Força: **fraca a moderada**.

### 6. Design e "cara de IA"

- **E-mail só imagem vs HTML com texto vivo:** prejudica entregabilidade (razão texto/imagem ruim é sinal spammy), acessibilidade (leitor de tela não lê imagem sem alt), dark mode e a experiência quando imagens estão bloqueadas. **Evidência direta ao vivo:** previews de e-mails só imagem na base Trendtrack aparecem como OCR ilegível — "FCTSFEXTRAWSPGJ RTSWGHJLBSLKMSF..." (GANDAIA, ID 11016601, 13/09/2026) e o welcome da AMANI YANI (ID 10962147, 11/09/2026) — exatamente o que um resumidor de IA e um leitor de tela "veem" quando a copy está assada dentro da imagem sem alt. Força: **forte** (observação direta Trendtrack 22/09/2026 + princípio estabelecido).
- **Clipping do Gmail:** o Gmail corta ("clips") mensagens acima de ~102 KB, escondendo conteúdo e potencialmente o link de descadastro abaixo do corte, prejudicando conformidade e conversão. Força: **forte** (documentado há anos). **[documentação/literatura — reconfirmar o limite exato de 102 KB]**
- **Acessibilidade:** relatórios do Email Markup Consortium (EMC) indicam que a grande maioria dos e-mails tem falhas de acessibilidade (alt ausente, contraste insuficiente, ausência de atributo de idioma/estrutura semântica). Força: **moderada a forte** (relatório de consórcio da indústria). **[relatório EMC/Litmus — reconfirmar percentuais exatos]**

### 7. Fluxo humano + IA que funciona

- **LLM-como-juiz / critic loop / linters:** um segundo passo automatizado que critica e reescreve o rascunho (revisor separado) melhora consistência; listas de palavras proibidas e guias de estilo aplicados por linter reduzem "slop". Força: **moderada** (prática documentada em engenharia de LLM; poucos estudos formais no marketing de e-mail especificamente).
- **Combinação vencedora documentada:** humano define estratégia e oferta → IA gera variações → linter/critic remove marcadores de IA e valida regras → humano edita e aprova → A/B testa (o Omnisend suporta A/B nativo por openRate/clickRate, com seleção automática ou manual de vencedor — útil para operacionalizar a etapa de teste). Força: **moderada**.

## Tabela: Regra da skill → evidência → veredito

| Regra da skill | Evidência | Força | Veredito |
|---|---|---|---|
| Proibir travessão (em dash) | Marcador de LLM amplamente relatado e medido | Moderada | **Refinada** (proibir como default; permitir uso humano ocasional) |
| Proibir número inventado | Veracidade + risco legal (CDC art. 37, CAN-SPAM) | Forte | **Confirmada** |
| Proibir urgência falsa | Corrói confiança, eleva reclamação; risco legal | Moderada a forte | **Confirmada** |
| Proibir assunto que simula transação | CAN-SPAM proíbe assunto enganoso; CDC; + reclamação | Forte | **Confirmada** |
| Assunto curto (≤25 a 40 caracteres) | Benchmarks de ESP recomendam assunto curto p/ mobile | Moderada | **Refinada** (curto sim; limite exato via teste) |
| Corpo curto por tipo de e-mail | Depende do tipo (promo/carrinho curto; welcome/brand pode ser +longo) | Fraca a moderada | **Refinada** |
| 1 CTA principal | UX e testes apoiam foco em uma ação | Moderada | **Confirmada** |
| Oferta em texto vivo + alt descritivo | Entregabilidade, acessibilidade, resumos de IA, clipping | Forte | **Confirmada** |
| Evitar superlativos e vocabulário de IA | Lista de excesso de vocabulário (delve etc.) quantificada | Forte | **Confirmada** |
| Evitar "não é X, é Y" e tríades | Marcadores de LLM medidos | Moderada | **Confirmada** |
| Limitar emoji e exclamação | Dados mistos; excesso é spammy | Fraca a moderada | **Refinada** |
| Fluxo estratégia humana → rascunho IA → edição humana | Persado/Phrasee: ganho vem de geração + teste + seleção | Moderada | **Confirmada** |
| Revisor separado (critic loop) | Prática de engenharia de LLM; melhora consistência | Moderada | **Confirmada** |
| Provedor penaliza "texto de IA" diretamente | Sem evidência primária | Especulação | **Sem evidência / contrariada** (reposicionar) |

## Recomendações (escalonadas)

1. **Adote agora (evidência forte):** banir número inventado, urgência falsa e assunto que simula transação (justificativa legal CDC/CAN-SPAM + reputação); exigir oferta e condição em **texto vivo com alt descritivo**; manter e-mails **abaixo de ~102 KB**; manter reclamação de spam **abaixo de 0,1%** no Postmaster Tools e one-click unsubscribe ativo. Estas não precisam de teste — são conformidade e higiene.
2. **Adote com A/B de confirmação (evidência moderada):** limite de travessão, tríades e "não é X, é Y"; lista de vocabulário de IA proibido; assunto curto; 1 CTA principal; limite de emoji/exclamação. Meça **abertura, clique, conversão, descadastro e reclamação** por variante usando o A/B nativo do Omnisend (winningMetric = openRate/clickRate).
3. **Trate como hipótese e teste internamente (evidência fraca/ausente):** marcadores de IA em pt-BR; impacto de resumos Gemini/Apple; tamanho ótimo de assunto/corpo por tipo para a base brasileira.
4. **Reposicione a regra de entregabilidade na skill:** **não** afirme que filtros penalizam "texto de IA". Justifique por engajamento, reclamação de spam e homogeneização entre lojas (que é real e observável).
5. **Antes de publicar a skill, reconfirme com um clique** cada fonte marcada **[literatura publicada — reconfirmar]** e resolva os itens "a verificar" (estudo Adrian Krebs abr/2026 e repo ravidsrk/slop-detect; figuras exatas de excesso de "delve"; percentuais do relatório EMC; limite de 102 KB).
6. **Benchmarks que mudariam a recomendação:** se um A/B interno mostrar que travessão/tríade não afeta engajamento, rebaixe de "proibir" para "preferência de estilo"; se a reclamação de spam de uma conta passar de 0,1%, acione revisão imediata de copy/urgência; se resumos de IA se mostrarem sem impacto em abertura, relaxe a exigência de texto vivo apenas para os e-mails onde a imagem converte melhor (mantendo alt por acessibilidade).

## Lacunas de evidência pública (exigem teste A/B interno Convertfy)

- **IA-pura vs IA-editada vs humana** com receita por e-mail e reclamação, em e-commerce brasileiro — não há teste público limpo.
- **Marcadores de IA em português brasileiro** validados empiricamente — inexistentes; construa um corpus interno (e-mails aprovados vs rejeitados) e meça gerundismo, conectivos e fórmulas.
- **Impacto de resumos de IA** (Gemini/Apple Intelligence) em abertura/clique de e-mail de marketing — sem dado público de impacto.
- **Impacto medido da homogeneização de copy** em inbox placement — a homogeneização é comprovada (20/20 na Trendtrack), mas o efeito em entregabilidade não.
- **Tamanho ótimo de assunto/preheader/corpo por tipo** para a base da Convertfy. Nota de correção: a documentação da API do Omnisend define subject, senderName e templateID como obrigatórios e preheader como opcional em post_campaigns, mas **não** documenta um limite de 250 caracteres para assunto/preheader (afirmação anterior removida por não ser verificável na doc oficial). O ótimo prático de assunto é muito menor que qualquer limite técnico e deve vir de teste.

## Correções e itens explicitamente não confirmados neste ambiente

- Removida a afirmação não verificada de "até 250 caracteres em assunto e preheader" no Omnisend (não consta na referência oficial da API consultada em 22/09/2026).
- Estudo Adrian Krebs (abr/2026) e repo ravidsrk/slop-detect: **não confirmados**; verificar antes de qualquer citação.
- Todas as citações da literatura publicada (Gray 2024; Kobak et al.; Longoni & Cian; requisitos Gmail/Yahoo; CAN-SPAM; CDC art. 37; EMC; clipping 102 KB; benchmarks de assunto) refletem o registro público estabelecido mas **devem ter o link reconfirmado** antes de entrar na skill, pois não houve web_fetch neste ambiente.