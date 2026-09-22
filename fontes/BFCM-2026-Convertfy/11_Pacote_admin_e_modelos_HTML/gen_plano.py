import json
M={m['key']:m for m in json.load(open('seed/modelos.json'))['modelos']}
E90={"A":"E90","B":"E90","C":"E90"}
P18={"A":"E180","B":"E180","C":"E90"}
BFD={"A":"E180","B":"E90","C":"E90"}
S=[]
def s(data,hora,janela,modelo,obj,publico,lp=False,trilha="todas",teste=None,assunto_pt=None,assunto_en=None,porque="",notas=""):
    m=M[modelo]
    S.append(dict(id=f"{data}-{hora.replace(':','')}-{modelo}",data=data,hora=hora,canal="email",janela=janela,modelo=modelo,
      estrutura=m['estrutura'],objetivo=obj,assunto_pt=assunto_pt or m['assunto'].get('pt'),assunto_en=assunto_en or m['assunto'].get('en'),
      publico=publico,lista_pequena=lp,trilha=trilha,teste=teste,porque=porque,notas=notas,status_modelo=m['status']))
# OUTUBRO
s("2026-10-01","10:00","outubro","notificacao-do-futuro","Abre o mês com o e-mail de maior índice fora de pico",E90,True,porque="O melhor e-mail fora de pico da carteira: 1,67 em 39 lojas (24 acima da média) e 1,43 nas 9 lojas")
s("2026-10-02","10:00","preparacao","reativacao","Limpar a lista antes da BF. Botão 'quero continuar' grava tag",{"A":"INATIVO_180_365","B":"INATIVO_180_365","C":"COMPRADOR_ANTIGO_LOTE"},porque="Brinque Mais: lista limpa abriu 25% contra 14%")
s("2026-10-04","10:00","10.10","convite","Convite do 10.10 (D-6). Botão confirma e grava VIP-1010",E90,True)
s("2026-10-06","10:00","preparacao","reativacao","Reativação 2, só quem não abriu a 1",{"A":"NA_REATIVACAO_1","B":"NA_REATIVACAO_1","C":"NA_REATIVACAO_1"},assunto_pt="Última pergunta antes da Black, [nome]",assunto_en="One last question before Black Friday, [nome]")
s("2026-10-07","10:00","10.10","agenda","Acesso confirmado e agenda (D-3), só para quem confirmou",{"A":"VIP+E30","B":"VIP+E30","C":"VIP+E30"},True,assunto_pt="[Nome], seu acesso está confirmado ✅",assunto_en="[Nome], your access is confirmed ✅")
s("2026-10-10","00:00","10.10","acesso-liberado-00h","Acesso liberado para metade da lista VIP",{"A":"VIP_GRUPO_A","B":"VIP_GRUPO_A","C":"VIP_GRUPO_A"},teste="T1-madrugada",assunto_pt="🔓 Seu acesso ao 10.10 foi liberado",assunto_en="🔓 Your 10.10 access has been granted")
s("2026-10-10","07:00","10.10","cupom-liberado-7h","Cupom liberado, texto com pessoa",E90,True)
s("2026-10-10","11:00","10.10","reenvio-11h","Reenvio para quem não abriu o 07h",{"A":"NA_07H","B":"NA_07H","C":"NA_07H"})
s("2026-10-10","18:00","10.10","status-mudou-18h","Disparo principal do dia, formato conversa",P18,True,notas="execucao:conversa")
s("2026-10-10","21:30","10.10","ultima-chamada-2130","Última chamada, fecha 23h59",{"A":"CNC","B":"CNC","C":"CNC"},True,teste="T2-2130")
s("2026-10-12","10:00","10.10","ressaca","Ressaca só com estoque real",{"A":"E90","B":"E90","C":"E30"},trilha="todas_exceto_br_infantil")
s("2026-10-12","10:00","10.10","ultima-chamada-2130","Última chance do Dia das Crianças (lojas BR infantis)",E90,trilha="br_infantil",assunto_pt="Última chance para o Dia das Crianças",assunto_en=None)
s("2026-10-14","10:00","outubro","jornal","Jornal de outubro",E90)
s("2026-10-16","10:00","outubro","sexta-premiada","Sexta premiada",E90)
s("2026-10-19","10:00","outubro","favoritos","Os mais pedidos no 10.10 (D+9)",E90,porque="O pós que funciona é a vitrine uma semana depois, não a ressaca: favoritos do 7.7 (D+8) fez 1,11 na amostra ampla; as ressacas do 8.8 e do 9.9, 0,50 e 0,56")
s("2026-10-21","10:00","outubro","ligacao","Ligação com oferta de outubro",E90)
s("2026-10-23","10:00","outubro","figurinha","Figurinha adaptada ao mês. No global, Halloween",E90)
s("2026-10-30","10:00","outubro","sexta-premiada","Última sexta de outubro, fecha o mês",E90,True,assunto_pt="Você foi premiado: último dia de outubro 🎁",porque="Sexta premiada (1,17) no lugar do catálogo fecha mês (0,79 na amostra ampla)")
# NOVEMBRO 1
s("2026-11-03","10:00","11.11","jornal","Jornal de novembro",E90)
s("2026-11-05","10:00","11.11","convite","Convite do 11.11 assinado por pessoa, grava VIP-1111",E90,True)
s("2026-11-08","10:00","11.11","agenda","Acesso confirmado e agenda do 11.11, com 3 tarefas",{"A":"VIP+E30","B":"VIP+E30","C":"VIP+E30"},True,assunto_pt="[Nome], seu acesso está confirmado ✅",assunto_en="[Nome], your access is confirmed ✅")
s("2026-11-11","00:00","11.11","acesso-liberado-00h","Black antecipada liberada para a lista VIP, se o T1 aprovar",{"A":"VIP","B":"VIP","C":"VIP"},teste="depende-T1",assunto_pt="🔓 Sua Black começou antes, [nome]",assunto_en="🔓 Your Black Friday started early, [nome]")
s("2026-11-11","07:00","11.11","cupom-liberado-7h","Cupom liberado",E90,True)
s("2026-11-11","11:00","11.11","reenvio-11h","Reenvio para não abridores",{"A":"NA_00H_07H","B":"NA_00H_07H","C":"NA_00H_07H"})
s("2026-11-11","18:00","11.11","status-mudou-18h","Status mudou. Nível A na lista toda (1 de 2)",{"A":"LT","B":"E180","C":"E90"},True,notas="execucao:conversa")
s("2026-11-11","21:30","11.11","ultima-chamada-2130","Última chamada, fechamento real",{"A":"CNC","B":"CNC","C":"CNC"},True,teste="T2-2130")
s("2026-11-13","10:00","11.11","ressaca","Ressaca só com estoque real",{"A":"E90","B":"E90","C":"E30"})
# NOVEMBRO 2
s("2026-11-16","10:00","intervalo","notificacao-do-futuro","Notificação com brinde ou frete grátis, sem gastar a oferta da BF",E90,True,porque="Nova campanha de novembro com o modelo de maior índice fora de pico")
s("2026-11-17","10:00","intervalo","favoritos","Os mais pedidos no 11.11 (D+6)",E90)
s("2026-11-19","10:00","bf","convite","Convite da BF. Compradores do 11.11 já entram",{"A":"E90+COMPRADOR-1111","B":"E90+COMPRADOR-1111","C":"E90+COMPRADOR-1111"},True,assunto_pt="[Nome], seu convite para a Black chegou 🎟️",assunto_en="[Nome], your Black Friday invitation has arrived 🎟️")
s("2026-11-20","10:00","intervalo","sexta-premiada","Sexta premiada com brinde",E90,porque="Nova campanha de novembro. 1,22 nas 9 lojas (7 de 8) e 1,17 na amostra ampla")
s("2026-11-22","10:00","bf","agenda","Acesso confirmado e agenda dos 5 dias da BF",{"A":"VIP+E30","B":"VIP+E30","C":"VIP+E30"},True,assunto_pt="[Nome], seu acesso à Black está confirmado ✅",assunto_en="[Nome], your Black Friday access is confirmed ✅")
# BF
s("2026-11-25","00:00","bf","acesso-liberado-00h","BF liberada para VIP, se o T1 aprovar",{"A":"VIP-BF","B":"VIP-BF","C":"VIP-BF"},teste="depende-T1",assunto_pt="🔓 Sua Black foi liberada, [nome]",assunto_en="🔓 Your Black Friday is unlocked, [nome]")
s("2026-11-25","07:00","bf","cupom-liberado-7h","A oferta do ano começou",BFD,True,assunto_pt="A oferta do ano começou ✅",assunto_en="Our offer of the year has started ✅")
s("2026-11-25","18:00","bf","status-mudou-18h","Status mudou",BFD,True,notas="execucao:conversa")
s("2026-11-26","10:00","bf","figurinha","Figurinha dourada da Black",BFD,assunto_pt="🏆 Você desbloqueou a figurinha dourada da Black",assunto_en="🏆 You've unlocked the golden Black Friday sticker")
s("2026-11-26","19:00","bf","reenvio-11h","Reenvio do 18h de 25/11 para não abridores",{"A":"NA_18H_2511","B":"NA_18H_2511","C":"NA_18H_2511"},assunto_pt="A Black está no ar e você ainda não viu, [nome]",assunto_en="Black Friday is live and you haven't seen it yet, [nome]")
s("2026-11-27","07:00","bf","cupom-liberado-7h","Hoje é o dia",BFD,True,assunto_pt="[Nome], hoje é o dia",assunto_en="[Nome], today is the day")
s("2026-11-27","11:00","bf","reenvio-11h","Para quem não abriu o 07h",{"A":"NA_07H","B":"NA_07H","C":"NA_07H"})
s("2026-11-27","18:00","bf","status-mudou-18h","Status mudou. Lista toda A e B (única do nível B)",{"A":"LT","B":"LT","C":"E90"},True,notas="execucao:conversa")
s("2026-11-28","10:00","bf","notificacao-do-futuro","Notificação com a oferta da BF",BFD,teste="T3-fim-de-semana")
s("2026-11-28","18:00","bf","ligacao","A Black está te ligando",BFD,teste="T3-fim-de-semana",assunto_pt="[Nome], a Black está te ligando 📞",assunto_en="[Nome], Black Friday is calling 📞",porque="A referência validada (24/07) é uma liquidação ligando para o cliente, com a oferta na tela")
s("2026-11-29","10:00","bf","cupom-liberado-7h","A Black termina hoje, texto",BFD,True,teste="T3-fim-de-semana",assunto_pt="A Black termina hoje, [nome]",assunto_en="Black Friday ends today, [nome]")
s("2026-11-29","18:00","bf","status-mudou-18h","Status mudou, termina 23h59",BFD,True,notas="execucao:conversa")
s("2026-11-29","21:30","bf","ultima-chamada-2130","Fecha a BF",{"A":"CNC","B":"CNC","C":"CNC"},True,teste="T2-2130")
# CM
s("2026-11-30","07:00","cm","cupom-liberado-7h","Cyber Monday com oferta nova",E90,True,assunto_pt="Cyber Monday: tem novidade para você",assunto_en="Cyber Monday: something new for you",porque="A CM vem colada na BF. O VIP Day, 6 dias depois do 9.9, rendeu metade do 9.9 por envio (0,38 contra 0,79 pedidos por mil). Por isso a CM é mais curta e só para E90")
s("2026-11-30","11:00","cm","reenvio-11h","Reenvio",{"A":"NA_07H","B":"NA_07H","C":"NA_07H"})
s("2026-11-30","18:00","cm","status-mudou-18h","Status mudou",{"A":"E180","B":"E90","C":"E90"},True,notas="execucao:conversa")
s("2026-12-01","10:00","cm","jornal","Jornal da Cyber: termina quinta",E90)
s("2026-12-03","18:00","cm","status-mudou-18h","Último dia da CM",E90,True,notas="execucao:conversa")
s("2026-12-03","21:30","cm","ultima-chamada-2130","Fecha a temporada",{"A":"CNC","B":"CNC","C":"CNC"},True,teste="T2-2130")
# DEZEMBRO
s("2026-12-07","10:00","dezembro","favoritos","Os mais pedidos da Black, como guia de presentes (D+8)",E90)
s("2026-12-09","10:00","dezembro","ligacao","Recado: os presentes que mais saíram",E90,assunto_pt="[Nome], você recebeu uma ligação 📞",assunto_en="[Nome], you've received a call 📞")
s("2026-12-11","10:00","dezembro","sexta-premiada","Sexta premiada com nível de gasto",E90)
s("2026-12-12","18:00","dezembro","status-mudou-18h","12.12 opcional, lojas BR com histórico",E90,trilha="br_opcional",teste="T7-1212",notas="execucao:conversa")
s("2026-12-14","10:00","dezembro","jornal","Jornal: prazo de entrega na manchete",E90,True)
s("2026-12-15","10:00","dezembro","notificacao-do-futuro","Prazo 1: pedido para chegar antes do Natal",P18,True,porque="O prazo de entrega entra no melhor modelo fora de pico, no lugar de um e-mail de prazo sem dado")
s("2026-12-16","10:00","dezembro","reabertura","Reabri o frete padrão por mais um dia",E90,assunto_pt="Eu decidi reabrir o frete padrão por mais um dia",assunto_en="I've decided to reopen standard shipping for one more day",porque="Reabertura: 1,15 na amostra ampla (17 de 28). Só se a transportadora ainda entregar a tempo")
s("2026-12-17","10:00","dezembro","figurinha","Presente dourado",E90,assunto_pt="🎄 Você desbloqueou o presente dourado",assunto_en="🎄 You've unlocked the golden gift")
s("2026-12-19","10:00","dezembro","ligacao","Prazo 2: frete expresso ainda chega",P18,assunto_pt="[Nome], recado: o expresso ainda chega antes do Natal 📞",assunto_en="[Nome], message: express shipping still arrives before Christmas 📞")
s("2026-12-20","10:00","dezembro","cupom-liberado-7h","Segunda parcela do 13º, texto com pessoa",E90,trilha="br",assunto_pt="O 13º caiu. Seus presentes estão aqui",assunto_en=None)
s("2026-12-21","10:00","dezembro","ultima-chamada-2130","Último dia para chegar antes do Natal",P18,True,assunto_pt="🚨 [ÚLTIMA CHAMADA] Último dia para chegar antes do Natal",assunto_en="🚨 [FINAL CALL] Last day for delivery by Christmas")
s("2026-12-22","10:00","dezembro","notificacao-do-futuro","O presente que chega em 1 minuto (vale-presente)",E90,True,assunto_pt="[Nome], seu presente já foi entregue...",assunto_en="[Nome], your gift has already been delivered...")
s("2026-12-23","10:00","dezembro","cupom-liberado-7h","Vale-presente de última hora, texto com pessoa",E90,assunto_pt="Ainda dá tempo, [nome]",assunto_en="There's still time, [nome]")
s("2026-12-26","07:00","dezembro","cupom-liberado-7h","Boxing Day",E90,trilha="uk_eu",assunto_pt=None,assunto_en="Boxing Day starts now")
s("2026-12-26","18:00","dezembro","status-mudou-18h","Boxing Day 18h",P18,trilha="uk_eu",assunto_pt=None,notas="execucao:conversa")
s("2026-12-28","10:00","dezembro","ligacao","Pós-Natal: recado com crédito de loja até 31/12",E90,assunto_pt="[Nome], você tem um recado: crédito até 31/12 📞",assunto_en="[Nome], you have a message: credit until 31/12 📞")
s("2026-12-30","10:00","dezembro","notificacao-do-futuro","Notificação de 2027: o crédito que você esqueceu",E90,True,assunto_pt="[Nome], uma notificação de 2027 chegou...",assunto_en="[Nome], a notification from 2027 has arrived...")
nivel={"validado":"validado","parcial":"validado","revisar":"validado","reserva":"complemento","teste":"validado","fora":"fora"}
insp={"guia-presentes","prazo-entrega","vale-presente","texto-pessoa"}
teste_ok={"revele"}
for x in S:
    st=x['status_modelo']
    x['evidencia']= "inspiracao" if x['modelo'] in insp else ("complemento" if x['modelo'] in teste_ok else ("complemento" if x['modelo'] in ("reativacao","acesso-liberado-00h") else nivel[st]))
from collections import Counter
c=Counter(x['evidencia'] for x in S); n=len(S)
print(n,c,{k:round(100*v/n) for k,v in c.items()})
json.dump({"plano":"Q4 2026","inicio":"2026-10-01","fim":"2026-12-31","principio":"80% validado, 5 a 10% inspiração, restante complemento",
 "composicao":{k:f"{round(100*v/n)}%" for k,v in c.items()},"envios":S},open('seed/plano_q4_2026.json','w'),ensure_ascii=False,indent=1)
