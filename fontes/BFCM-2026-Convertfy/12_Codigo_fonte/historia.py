H={
("2026-11-25","00:00"):"Ato 6, dia 1. A lista VIP entra antes, como prometido em 22/11.",
("2026-11-25","07:00"):"Ato 6, dia 1. O [Fundador] abre a semana para todos.",
("2026-11-25","18:00"):"Ato 6, dia 1, fechamento.",
("2026-11-26","10:00"):"Ato 6, dia 2. Oferta nova, como o calendário de 18/11 prometeu.",
("2026-11-26","18:00"):"Ato 6, dia 2. Mesma oferta em formato novo.",
("2026-11-27","07:00"):"Ato 6, dia 3: a Black Friday.",
("2026-11-27","11:00"):"Ato 6, dia 3. O brinde é a notícia nova do dia.",
("2026-11-27","18:00"):"Ato 6, dia 3, fechamento do dia mais forte do ano.",
("2026-11-28","10:00"):"Ato 6, dia 4: monte seu kit.",
("2026-11-28","18:00"):"Ato 6, dia 4. Véspera do fim.",
("2026-11-29","10:00"):"Ato 6, dia 5: último dia.",
("2026-11-29","18:00"):"Ato 6, fim da Black Week.",
("2026-11-30","07:00"):"Ato 7. A [Gerente] volta com o que os clientes pediram depois da Black: combo.",
("2026-11-30","18:00"):"Ato 7.",
("2026-12-01","10:00"):"Ato 7.",
("2026-12-02","18:00"):"Ato 7, fim da temporada de ofertas.",
("2026-12-07","10:00"):"Ato 8, capítulo 1. O último single day do ano tem um motivo: o presente chegar a tempo.",
("2026-12-09","10:00"):"Ato 8, capítulo 2. A [Gerente] ajuda a escolher.",
("2026-12-11","10:00"):"Ato 8, capítulo 3. Véspera do 12.12.",
("2026-12-12","07:00"):"Ato 8, o 12.12.",
("2026-12-12","18:00"):"Ato 8, fechamento do 12.12.",
("2026-12-15","10:00"):"Ato 8. Começa a contagem dos prazos de entrega.",
("2026-12-17","10:00"):"Ato 8. Último dia do frete padrão.",
("2026-12-18","10:00"):"Ato 8. A [Gerente] resolve para quem esqueceu alguém.",
("2026-12-19","10:00"):"Ato 8. Último prazo do expresso.",
("2026-12-21","10:00"):"Ato 8. O último dia para chegar.",
("2026-12-22","10:00"):"Ato 8. A [Gerente] resolve o presente de última hora.",
("2026-12-26","07:00"):"Trilha UK e EU.",("2026-12-26","18:00"):"Trilha UK e EU.",
("2026-12-28","10:00"):"Ato 8, epílogo. O [Fundador], que foi o rigoroso do trimestre, fecha o ano agradecendo com um crédito.",
("2026-12-30","10:00"):"Ato 8, fim do ano.",
}
def patch(NOV,DEZ):
    for e in NOV:
        if (e['data'],e['hora'])==("2026-11-30","07:00"):
            e['blocos']=["\"Oi, [nome]. Aqui é a [Gerente].\"",
             "\"Depois da Black, muita gente me escreveu pedindo a mesma coisa: combo. Então a Cyber Monday deste ano é isso: até quarta, você leva 3 e paga 2 (o de menor valor sai de graça), com frete grátis.\"",
             "\"Isso não existia na Black Week. MONTAR MEU COMBO >>>\"",
             "\"Um beijo, [Gerente]\""]
            e['cta']="MONTAR MEU COMBO >>>"; e['hero']="Texto da [Gerente]"
            e['ideia']="A [Gerente] volta à história com um pedido dos clientes: o combo."
    for e in DEZ:
        k=(e['data'],e['hora'])
        if k in (("2026-12-18","10:00"),("2026-12-22","10:00")):
            e['hero']="Texto da [Gerente]"
            e['blocos']=[b.replace('Assinatura','Assinatura: \"Um beijo, [Gerente]\"') for b in e['blocos']]
            e['blocos']=[b.replace('"Oi, [nome]. ','"Oi, [nome]. Aqui é a [Gerente]. ',1) if i==0 else b for i,b in enumerate(e['blocos'])]
            e['hv']="e-mail só de texto assinado pela gerente"
        if k==("2026-12-28","10:00"):
            e['ref']=["credit","wc_loyalty"]
            e['blocos'].append("Assinatura do [Fundador]: \"Foi um ano de muitas decisões por aqui. Obrigado por ter ficado até o fim. Este crédito é o nosso agradecimento. [Fundador]\"")
            e['conexao']=e['conexao'].replace(" Substitui a reabertura de 28/12, que já aparece em outubro.","")

def patch2(OUT,NOV,DEZ):
    for e in OUT:
        if e['data']=='2026-10-15':
            e['oferta']="Nenhuma. Quem entra na lista de espera recebe o aviso da Black antes e tem prioridade na lista selecionada do 11.11."
    for e in NOV:
        k=(e['data'],e['hora'])
        if k==("2026-11-25","00:00"):
            e['publico']={x:"Lista VIP da Black Week (selecionados do 11.11, compradores do 11.11 e quem entrou até 24/11)" for x in "ABC"}
            e['ref']=["bw24_25","early25"]
        if k in (("2026-11-25","07:00"),("2026-11-27","07:00")):
            e['blocos']=[b.replace('"Oi, [nome]. ','"Oi, [nome]. Aqui é o [Fundador]. ',1) if i==0 else b for i,b in enumerate(e['blocos'])]
            e['blocos']=[("Assinatura: \"[Fundador]\"" if b=='Assinatura' else b.replace('Assinatura + ','Assinatura \"[Fundador]\" + ')) for b in e['blocos']]
    for e in DEZ:
        k=(e['data'],e['hora'])
        if k==("2026-12-09","10:00"): e['ref']=["favoritos77","bwcol25"]
        if k==("2026-12-18","10:00"):
            e['ref']=["reabertura","wc"]; e['est']="Texto da gerente → dois links (frete expresso e vale-presente) → assinatura"

def patch3(NOV):
    for e in NOV:
        k=(e['data'],e['hora'])
        if k==("2026-11-27","11:00"):
            e.update(dict(nome="Black Friday premiada",papel="Black Friday: disparo 2 (sexta premiada + brinde surpresa)",
             oferta="25% extra com o cupom BLACK + a chave: aplicar o cupom no checkout revela o desconto final de cada produto e destrava o brinde surpresa em todo pedido de hoje.",
             assunto="Seu presente de Black Friday chegou 🎁",assunto_en="Your Black Friday gift has arrived 🎁",
             assuntos3=["Conservador: Seu presente de Black Friday chegou 🎁","Equilibrado: Black Friday premiada: sua chave está aqui 🔑","Ousado: Tem um presente no seu carrinho (e a gente não vai dizer o que é)"],
             pre="Aplique a chave no checkout e descubra o desconto e o brinde.",
             hero="Black Friday premiada",sub="A chave dourada destrava o desconto final de cada produto e um brinde surpresa em todo pedido de hoje.",
             blocos=["Hero (da sexta premiada de 31/07): \"BLACK FRIDAY PREMIADA\" + chave dourada + \"use a chave e descubra\"",
              "Cupom BLACK em caixa + \"Aplique o cupom no checkout para descobrir o desconto em cada produto. Válido até 23h59.\" + botão \"USAR MINHA CHAVE\"",
              "Caixa de presente com \"?\" (Black Friday de 2025): \"Todo pedido de hoje leva um brinde surpresa. Não vamos dizer o que é.\"",
              "\"Destrave com a chave\": grade 2x2 de produtos com \"aplique BLACK no checkout para ver o preço final\"",
              "\"Black Friday exclusiva por e-mail\""],
             cta="USAR MINHA CHAVE",urgencia="Só hoje.",
             hero_tipo="Sexta premiada (chave dourada)",hv="hero \"Black Friday premiada\" com uma chave dourada grande e, mais abaixo, uma caixa de presente com um ponto de interrogação",
             est="Hero da chave dourada → cupom e regra do checkout → brinde surpresa → grade \"destrave com a chave\" → faixa exclusiva por e-mail → garantias",
             ideia="A Black Friday cai numa sexta: é o dia da sexta premiada (1,22 nas 9 lojas), agora com o brinde surpresa da Black Friday de 2025 dentro.",
             ref=["sexta","bf2_25"],conexao="A sexta premiada foi a campanha de sexta que mais vendeu no trimestre (9 pedidos, US$ 50,2 por mil na Blue Wolf; 1,17 em 46 lojas; 1,22 nas 9 lojas) e a copy real das duas versões está na ficha. O brinde surpresa é o segundo disparo da Black Friday de 2025.",
             historia="Ato 6, dia 3. A Black Friday numa sexta: a sexta premiada, com o brinde dentro."))
        if k==("2026-11-30","07:00"):
            e['ref']=["reabertura","cupom99"]
            e['conexao']="Texto assinado no formato da reabertura de 25/07 (1,15 na amostra ampla) e do 07h com cupom (1,66 nas 9 lojas). A Cyber tem oferta própria, não é extensão da Black: a Cyber VIP de 2025 (extensão) foi o ponto fraco daquela sequência."

AB3={
("2026-10-04","10:00"):["Conservador: [Nome], seu convite para o 10.10 chegou 🎟️","Equilibrado: Você foi convidado (e vai ajudar a escolher um desconto) 🎟️","Ousado: Dez é a nota máxima. Dia 10 você vai entender."],
("2026-10-06","10:00"):["Conservador: [Nome], você já viu o que está vindo? 👀","Equilibrado: [Nome], você decide qual fica mais barato 🗳️","Ousado: Seu voto vale um desconto"],
("2026-10-09","10:00"):["Conservador: Amanhã é 10.10. Você está pronto?","Equilibrado: Menos de 24 horas","Ousado: Deu [produto]"],
("2026-11-18","10:00"):["Conservador: [Nome], seu convite para a Black Week chegou 🎟️","Equilibrado: Por que a Black este ano tem 5 dias","Ousado: No 11.11 muita gente ficou de fora. Por isso, 5 dias."],
("2026-11-20","10:00"):["Conservador: O número que você precisa lembrar: [N] 👀","Equilibrado: [N] pessoas viram \"esgotado\" no 11.11","Ousado: Não seja uma delas"],
("2026-11-24","10:00"):["Conservador: Amanhã começa a Black Week. Você está pronto?","Equilibrado: Menos de 24 horas para a Black Week","Ousado: Amanhã, 24 produtos por 24 horas"],
("2026-12-07","10:00"):["Conservador: [Nome], seu convite para o Natal Antecipado chegou 🎟️","Equilibrado: O presente que chega antes do Natal (com o frete por nossa conta)","Ousado: 12.12: 24 horas de frete prioritário grátis"],
("2026-12-11","10:00"):["Conservador: Amanhã é 12.12. Seus presentes estão prontos?","Equilibrado: Menos de 24 horas para o frete grátis de Natal","Ousado: Amanhã, o frete é por nossa conta"],
}
AB_KEYS=set(AB3)|{("2026-11-02","10:00"),("2026-11-04","10:00"),("2026-11-06","10:00"),("2026-11-10","10:00")}
AB_DUAL={("2026-11-08","10:00"),("2026-10-08","10:00"),("2026-11-22","10:00")}
SMS={
("2026-11-11","07:00"):"SMS/WhatsApp de venda às 07h05, para toda a base de SMS: \"[Loja]: a Black Antecipada começou. 22% extra com 1111 nos 24 mais vendidos, só hoje. [link]\"",
("2026-11-11","18:00"):"SMS/WhatsApp de venda às 18h05, para quem tem telefone e clicou ou abriu hoje, sem comprar: \"[Loja]: faltam 6 horas. Tem uma surpresa no seu carrinho. [link]\". Nos EUA, MMS com a foto do produto mais vendido do dia.",
("2026-11-25","07:00"):"SMS/WhatsApp de venda às 07h05, para toda a base de SMS: \"[Loja]: Black Week no ar. Só hoje, 25% nos 24 mais vendidos. [link]\"",
("2026-11-25","18:00"):"SMS/WhatsApp de venda às 18h05, para quem clicou hoje e não comprou: \"[Loja]: os 24 mudam de preço à meia-noite. [link]\"",
("2026-11-27","07:00"):"SMS/WhatsApp de venda às 07h05, para toda a base de SMS: \"[Loja]: é hoje. Até 60% + 25% extra com BLACK e um brinde surpresa em todo pedido. [link]\". Nos EUA, MMS com a foto do brinde (no teste do Max, o MMS fez US$ 2.000 contra US$ 534).",
("2026-11-27","18:00"):"SMS/WhatsApp de venda às 18h05, para quem clicou hoje e não comprou: \"[Loja]: a Black Friday acaba às 23h59. Sua chave ainda funciona. [link]\"",
("2026-11-30","07:00"):"SMS/WhatsApp de venda às 07h05, para toda a base de SMS: \"[Loja]: Cyber Monday. Leve 3, pague 2 até quarta. [link]\"",
("2026-11-30","18:00"):"SMS/WhatsApp de venda às 18h05, para quem clicou hoje e não comprou: \"[Loja]: seu combo ainda está no carrinho. Leve 3, pague 2. [link]\"",
}
def patch4(OUT,NOV,DEZ):
    for e in OUT+NOV+DEZ:
        k=(e['data'],e['hora'])
        if k in AB3: e['assuntos3']=AB3[k]
        if k in AB_KEYS and e.get('assuntos3'): e['ab']="simples"
        if k in AB_DUAL: e['ab']="duplo"
        if k in SMS: e['canais']=SMS[k]
        if k==("2026-10-31","10:00"):
            e['booster']=dict(quando="17h (delay de 7h)",para="nonOpeners",assunto="⏳ O progressivo de Halloween acaba à meia-noite")
        if k==("2026-12-17","10:00"):
            e['booster']=dict(quando="17h (delay de 7h)",para="nonOpeners",assunto="⏳ Hoje é o último dia do frete padrão para o Natal")
        if e['data'] in ("2026-11-18","2026-11-20","2026-11-22","2026-11-24") and e['hora']=="10:00":
            if 'condição especial' not in e['oferta']:
                of=e['oferta']
                for pre in ("Nenhuma no e-mail. ","Nenhuma. "):
                    if of.startswith(pre): of=of[len(pre):]
                if of.strip()=="Nenhuma nova.": of="Sem oferta nova da Black Week."
                e['oferta']=of.rstrip('.')+". No site, condição especial ativa em produtos selecionados: até 30%, sem cupom, até 24/11 às 23h59."
                bl=[b for b in e['blocos']]
                bl.insert(len(bl)-1 if len(bl)>2 else len(bl),"\"Já com condição especial no site\": 4 produtos com preço de antes e de agora (até 30%, sem cupom, até 24/11) + \"VER TODOS\"")
                e['blocos']=bl
                if e.get('est') and 'condição especial' not in e['est']:
                    e['est']=e['est'].replace(' → garantias',' → já com condição especial no site → garantias')
