# Pacote Claude Design · Blue Wolf · Q4 2026

Tudo o que o Claude Design (com o Fable) precisa para desenhar a versão final dos e-mails da Blue Wolf de outubro, novembro e dezembro.

## O que tem aqui

| Arquivo | Para que serve | Quando usar |
|---|---|---|
| 01_PROMPT_MESTRE.md | Contexto, objetivo, regras e forma de trabalho | Colar no começo de toda conversa nova |
| 02_DESIGN_SYSTEM_BLUE_WOLF.md | Tipografia, cores, componentes e regras técnicas de e-mail | Anexar em toda conversa |
| 03_PALETAS_POR_MOMENTO.md | A paleta e a direção de arte de cada momento do trimestre | Anexar em toda conversa |
| 04_PROMPTS_POR_LOTE.md | O prompt pronto de cada etapa | Um por conversa |
| 05_CHECKLIST_APROVACAO.md | O que conferir em cada e-mail antes de aprovar | Na revisão |
| 06_DADOS_DA_LOJA_preencher.md | Cupons, percentuais, nomes, produtos e números reais | Preencher antes de começar |
| lotes/ | Um arquivo por sequência, com o brief de cada e-mail e a lista do que anexar | Um lote por conversa |
| referencias/ | As imagens dos e-mails validados (REF_*.jpg) | Anexar as que o lote pede |
| contexto_completo/ | O calendário completo (PDF) e os briefs de copy | Só se o Claude Design pedir mais contexto |

## Ordem de trabalho

1. Preencher o 06 (dados da loja). O que ficar sem dado vira espaço marcado entre colchetes, nunca número inventado.
2. **Conversa 1: design system.** Colar o prompt da etapa 0 do arquivo 04, anexar 01, 02, 03 e as 10 referências indicadas. Sai o sistema de componentes da Blue Wolf para o Q4. Se o Claude Design tiver a opção de salvar como design system, salvar e marcar como padrão.
3. **Conversas 2 a 9: um lote por conversa**, na ordem L1 a L8. Anexar 01, 02, 03, o arquivo do lote e as imagens listadas em `lotes/<lote>_ANEXAR.txt`. Tudo dentro do mesmo projeto, para manter a consistência.
4. Revisar cada lote com o 05 antes de passar para o próximo. Ajustes pequenos na mesma conversa; mudança de direção, avisar antes de seguir.
5. Exportar para o fatiamento. Não sei quais formatos de exportação o Claude Design oferece: se tiver PNG, exportar em 1200 px de largura (2x); se tiver HTML, conferir antes se ele passa na Omnisend.

## Números

- 67 e-mails no trimestre: **54 com design** e 13 de texto puro (vão direto no editor de texto da Omnisend; os lotes marcam quais são).
- 8 lotes, de 3 a 11 e-mails com design cada.

## Skills para habilitar na outra conta (se o Claude Design aceitar skills)

- **Sua skill própria (skill-email-convertfy)**, se já estiver instalável: é a que tira os vícios de IA de copy e design de e-mail.
- **Impeccable:** revisão de hierarquia, espaçamento, contraste e acabamento.
- **Taste (design-taste-frontend):** evita a cara de template e força uma direção visual.
- Opcional: **frontend-design**, para direção de tipografia e composição.
- Não precisa: Emil Kowalski (animação), as skills de Figma e as de documentos (pptx, docx, xlsx).
