# Famílias de assunto com os exemplos validados (Playbook 5.1 a 5.4 e dados da carteira)
F={
"estado":dict(nome="Aviso de mudança de estado",regra="🚨 no começo + uma mudança de estado curta, sem oferta no assunto. Parece notificação de sistema. Só no disparo principal do dia de pico (18h).",
  base=["🚨 Your status has just changed · 8.8 às 18h · receita 2,13 · 5 de 5 lojas acima de 1","🚨 Your status has just changed · 9.9 às 18h · receita 1,71 · 4 de 5"]),
"convite":dict(nome="Convite com o nome",regra="[Nome] + \"seu convite chegou\" + 🎟️ (ou ✉️). Sem oferta e sem data no assunto. A oferta vai no pré-cabeçalho.",
  base=["[Nome], your invitation has arrived 🎟️ · antecipação 6.6 · receita 1,43","[Nome], you have received an invitation ✉️ · antecipação 7.7 · receita 1,34 · 4 de 5"]),
"agenda":dict(nome="Curiosidade com o nome",regra="[Nome] + pergunta sobre o que vem + 👀. Não revela a oferta nem a data.",
  base=["[Nome], have you seen what is coming? 👀 · agenda do 7.7 · receita 1,77 · 5 de 5 (o assunto de antecipação que mais vendeu em 2026)"]),
"confirmacao":dict(nome="Confirmação de algo que já é da pessoa",regra="Um benefício já concedido (cupom liberado, acesso confirmado, presente chegou) + ✅. A pessoa abre para usar algo que já é dela.",
  base=["Your coupon has been approved ✅ · 7.7 às 7h, texto · receita 1,86","[Nome], your access is confirmed ✅ · antecipação 6.6 · receita 1,48 · 3 de 3"]),
"pendencia":dict(nome="Pendência",regra="Linguagem de checkout (\"falta você confirmar\"), com reticências. Funciona no fechamento de uma oferta; na véspera de um evento o \"pendente\" não vende.",
  base=["[Nome], you still need to confirm your order... · notificação do futuro · receita 1,52","Evitar: ⚠️ Your access for tomorrow is still pending · véspera do 7.7 · receita 0,77"]),
"noticia":dict(nome="Notícia",regra="[Nome] + \"chegou a notícia que você não queria...\". A notícia é o prazo; o assunto não diz qual.",
  base=["[Nome], the news you did not want to hear has arrived... · jornal · receita 1,59 · 4 de 5"]),
"numero":dict(nome="Número dentro do e-mail",regra="Um número entre parênteses no começo, como contador de notificação: \"(1) desconto escondido\", \"(1) brinde reservado\". Pode levar 🤫 ou ⚠️.",
  base=["(1) hidden discount for [nome] inside this email 🤫 · Revele · receita 1,50 · 4 de 5"]),
"tema":dict(nome="Tema do momento com ameaça leve",regra="A linguagem do assunto que a pessoa está vendo lá fora + uma perda leve para quem não aproveitar.",
  base=["🟥 A red card for anyone who misses out on these deals... · Semana Copa 2 · receita 1,65 · 5 de 5"]),
"separei":dict(nome="Separei para você",regra="[Nome] + \"separei\" ou \"estão te esperando\" + um emoji. Pessoal, sem oferta no assunto. Nome só em convite, pendência e favoritos.",
  base=["[Nome], I've set something aside just for our special customers 🏆 · Final da Copa · receita 1,35","Favoritos do 7.7 · receita 1,12 · 3,19% de clique"]),
"lastcall":dict(nome="Última chamada",regra="🚨 + [ÚLTIMA CHAMADA] + o que expira e o horário. Só no fechamento real, nunca em prorrogação.",
  base=["Last call do 7.7 às 18h · US$ 105,3 por mil · 3,06% de clique · 1,22 na amostra ampla"]),
"sistema":dict(nome="Aviso de sistema",regra="Frase de comunicado com reticências (\"Lamentamos informar que...\"). O conteúdo é o aviso de estoque.",
  base=["We regret to inform you that... · aviso de estoque do 9.9 · 14 pedidos, US$ 77,7 por mil (a melhor campanha de setembro)"]),
"pessoa":dict(nome="Texto de pessoa",regra="Frase em primeira pessoa, como um e-mail pessoal (\"Eu decidi...\", \"Comunicado oficial...\", \"posso continuar...\"). Sem emoji.",
  base=["I decided to reopen everything for one more day · reabertura de 25/07 · 1,15 na amostra ampla · 8 pedidos","Linha de 2025: \"Comunicado\" do CEO e \"Why We're Doing EA\" (marca americana: 59% de abertura, US$ 11,8 mil)"]),
"hormozi":dict(nome="Linha do Hormozi (2025)",regra="Número, prazo ou afirmação que abre um loop (\"Faltam 3 dias e 60% das pessoas me perguntaram isso\", \"Menos de 24 horas\", \"Aqui a Black é diferente\"). Usar como variação B do teste A/B contra um assunto validado.",
  base=["Assuntos da sequência do 11.11 de 2025, o maior mês da carteira (resultado sem número por assunto)"]),
"vespera":dict(nome="Véspera",regra="\"Amanhã é [data]. Você está pronto?\" ou \"Menos de 24 horas\". Nunca \"você está na lista\" ou \"pendente\" na véspera: é a promessa repetida que derrubou o 9.9.",
  base=["Véspera com checklist do 8.8 · 10 pedidos, o melhor esquenta","Evitar: you have something scheduled for tomorrow 📅 · 9.9 · receita 0,44"]),
"catalogo":dict(nome="Catálogo com prazo",regra="\"Ignore este e-mail depois das 23h59\". Abre bem; a venda vem do conteúdo com prazo real.",
  base=["Ignore this email after 11:59 PM · catálogo fecha mês · abertura 1,09 · 2,91% de clique"]),
"chamada":dict(nome="Chamada",regra="[Nome] + \"você tem uma chamada\" + 📞. Combina com o hero de chamada recebida.",
  base=["Ligação de 24/07 · 1,17 na amostra ampla"]),
"oferta":dict(nome="Oferta direta com mecânica",regra="A mecânica em poucas palavras (\"Quanto mais você leva, maior o desconto\"). Serve quando a mecânica é a novidade.",
  base=["Progressivo de Halloween e kit da Black Week de 2025 (sequência de 2025)"]),
"jogo":dict(nome="Jogo",regra="Um convite para jogar + a regra em poucas palavras + 🔑 ou 🤫. Pode usar o padrão de número como variação A.",
  base=["What's The Discount Code (Well Copy): \"REALLY high engagement\"","(1) hidden discount for [nome] inside this email 🤫 · Revele · receita 1,50"]),
}
def familia(e):
    a=e['assunto']
    t=a.lower()
    if '🚨 seu status' in t or 'status acaba de mudar' in t or 'status has just' in t: return 'estado'
    if 'última chamada' in t: return 'lastcall'
    if 'lamentamos' in t or 'we regret' in t: return 'sistema'
    if 'notícia que você não queria' in t: return 'noticia'
    if 'falta você confirmar' in t: return 'pendencia'
    if 'você já viu o que está vindo' in t: return 'agenda'
    if 'quer jogar' in t: return 'jogo'
    if a.startswith('(1)') or '(1)' in a or 'número que você precisa' in t or '100 primeiros' in t: return 'numero'
    if 'convite' in t or '🎟️' in a: return 'convite'
    if 'chamada recebida' in t or '📞' in a: return 'chamada'
    if 'ignore este' in t: return 'catalogo'
    if 'amanhã é' in t or 'você está pronto' in t or 'amanhã começa' in t: return 'vespera'
    if 'menos de 24' in t or 'faltam' in t or 'esgotam' in t or 'aqui a black' in t or 'lista vip (e não' in t or 'última chance de halloween' in t: return 'hormozi'
    if 'quanto mais' in t: return 'oferta'
    if 'estão te esperando' in t or 'presentes que eles' in t or 'separei' in t: return 'separei'
    if '✅' in a or '🔓' in a or 'chegou 🎁' in t or 'crédito ativado' in t or 'foi liberado' in t: return 'confirmacao'
    if 'áudio' in t or 'comunicado' in t or 'eu decidi' in t or 'posso continuar' in t or 'última pergunta' in t or 'esqueceu' in t or 'última hora' in t or 'por que a nossa' in t or 'por que a black' in t: return 'pessoa'
    return 'pessoa'

def tipo(e):
    p=e.get('papel','').lower(); n=e['nome'].lower()
    if 'reativa' in p: return 'reengajamento'
    if 'fase 7' in p or 'fechar' in p or 'fechamento' in p or 'last call' in n or 'last call' in p: return 'fechamento'
    if 'fase 6' in p or 'pico' in p or 'disparo' in p or 'envio' in p: return 'pico'
    if 'pós' in p or 'aviso de estoque' in p or 'vitrine' in p or 'epílogo' in p: return 'pos'
    if 'antecipa' in p or 'fase ' in p or 'captação' in p or 'abertura do mês' in p or 'véspera' in p: return 'antecipacao'
    return 'oferta'
MEDIR={
'antecipacao':"Clique e ação pedida (confirmação de vaga, voto, favoritos, resposta), mais os pedidos que vierem do catálogo com condição especial. Não se mede pela receita do dia.",
'pico':"Pedidos e receita por mil envios. Comparar com o mesmo horário dos single days de 2026.",
'fechamento':"Pedidos entre o envio e as 23h59, e a receita do booster ou do SMS de quem clicou e não comprou.",
'pos':"Receita por mil sem cupom novo, e quantos produtos zeraram o estoque.",
'reengajamento':"Cliques no botão de continuar (tag) e, depois, queda de bounce e spam nos envios grandes.",
'oferta':"Receita por mil e pedidos da janela da oferta.",
}
def estrategia(e):
    papel=e.get('papel','')
    obj=papel.split(':',1)[-1].strip() if ':' in papel else papel
    acao=e.get('cta','').replace('>>>','').strip()
    return dict(objetivo=f"{papel}. {e.get('historia','')}".strip(),
                mecanismo=e.get('ideia',''),
                acao=f"Levar a pessoa a clicar em \"{acao}\"." if acao else "",
                medir=MEDIR[tipo(e)])
