import os, json
F="font-family:Arial,Helvetica,sans-serif;"
def page(title, body, pre="{{pre_cabecalho}}"):
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting"><title>{title}</title>
<style>body{{margin:0;padding:0;background:#ffffff}} img{{border:0;display:block}} a{{color:#000000}}
@media (max-width:620px){{.w{{width:100%!important}} .col{{display:block!important;width:100%!important}} .px{{padding-left:20px!important;padding-right:20px!important}}}}</style></head>
<body style="margin:0;background:#ffffff">
<div style="display:none;max-height:0;overflow:hidden">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#ffffff"><tr><td align="center">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" style="width:600px">
{logo()}
{body}
{rodape()}
</table></td></tr></table></body></html>"""
def logo():
    return f'<tr><td align="center" style="padding:28px 40px 20px"><img src="{{{{loja_logo}}}}" width="140" alt="{{{{loja_nome}}}}" style="width:140px;height:auto"></td></tr>'
def txt(t, size=16, w="normal", align="left", pad="0 40px 16px", color="#000000", lh=1.5):
    return f'<tr><td class="px" align="{align}" style="{F}font-size:{size}px;font-weight:{w};line-height:{lh};color:{color};padding:{pad}">{t}</td></tr>'
def btn(t="{{cta}}", href="{{link}}", pad="8px 40px 28px"):
    return f'''<tr><td class="px" align="center" style="padding:{pad}"><table role="presentation" cellpadding="0" cellspacing="0"><tr><td bgcolor="#000000" style="border-radius:4px"><a href="{href}" style="{F}display:inline-block;padding:16px 36px;font-size:16px;font-weight:bold;color:#ffffff;text-decoration:none">{t}</a></td></tr></table></td></tr>'''
def cupom(label="Cupom"):
    return f'''<tr><td class="px" align="center" style="padding:4px 40px 20px"><table role="presentation" cellpadding="0" cellspacing="0" style="border:2px dashed #000000"><tr><td align="center" style="{F}padding:14px 32px"><div style="font-size:12px;color:#555555">{label}</div><div style="font-size:26px;font-weight:bold;letter-spacing:2px;color:#000000">{{{{cupom}}}}</div></td></tr></table></td></tr>'''
def prazo():
    return txt("Válido até {{prazo}}", 14, "bold", "center", "0 40px 20px")
def grade(n=4, titulo=None):
    rows=""; 
    if titulo: rows+=txt(titulo,20,"bold","center","12px 40px 16px")
    items=[f'''<td class="col" width="50%" valign="top" style="padding:0 8px 20px"><a href="{{{{produto_{i}_link}}}}" style="text-decoration:none"><img src="{{{{produto_{i}_img}}}}" width="252" alt="{{{{produto_{i}_nome}}}}" style="width:100%;height:auto;background:#f2f2f2"><div style="{F}font-size:14px;color:#000000;padding-top:8px">{{{{produto_{i}_nome}}}}</div><div style="{F}font-size:14px;color:#000000;padding-top:4px"><span style="text-decoration:line-through;color:#777777">{{{{produto_{i}_preco_de}}}}</span> <b>{{{{produto_{i}_preco}}}}</b></div></a></td>''' for i in range(1,n+1)]
    for k in range(0,n,2):
        rows+=f'<tr><td class="px" style="padding:0 32px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{items[k]}{items[k+1] if k+1<n else "<td></td>"}</tr></table></td></tr>'
    return rows
def garantias():
    cells="".join(f'<td class="col" width="33%" align="center" style="{F}font-size:13px;color:#000000;padding:12px 6px">{g}</td>' for g in ["{{garantia_1}}","{{garantia_2}}","{{garantia_3}}"])
    return f'<tr><td class="px" style="padding:8px 40px 8px;border-top:1px solid #e5e5e5"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{cells}</tr></table></td></tr>'
def rodape():
    return f'<tr><td align="center" style="{F}font-size:12px;line-height:1.6;color:#777777;padding:24px 40px 40px;border-top:1px solid #e5e5e5">{{{{loja_nome}}}} · {{{{loja_endereco}}}}<br><a href="{{{{unsubscribe_link}}}}" style="color:#777777">Descadastrar</a></td></tr>'
def caixa(inner, borda="#000000", fundo="#ffffff"):
    return f'<tr><td class="px" style="padding:0 40px 20px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid {borda};background:{fundo}"><tr><td style="{F}padding:20px 24px;color:#000000">{inner}</td></tr></table></td></tr>'
def oferta_hero(pre="{{linha_de_contexto}}"):
    return (txt(pre,14,"normal","center","0 40px 8px","#555555")+
            txt("{{oferta_titulo}}",40,"bold","center","0 40px 8px","#000000",1.1)+
            txt("{{oferta_apoio}}",16,"normal","center","0 40px 16px"))
T={}
T["A-status-mudou"]=("Status mudou (18h do pico)",
  caixa('<div style="font-size:12px;color:#555555;padding-bottom:6px">Agora · {{loja_nome}}</div><div style="font-size:17px;line-height:1.45"><b>{{nome}}, seu status acaba de mudar.</b><br>{{oferta_titulo}} liberado até {{prazo}}.</div>', "#d9d9d9", "#f5f5f5")
  +oferta_hero("Faltam poucas horas")+cupom()+btn()+prazo()+grade(4)+cupom("Seu cupom continua ativo")+btn()+garantias())
T["A-jornal"]=("Jornal",
  f'<tr><td class="px" align="center" style="padding:0 40px 8px;border-bottom:3px double #000000"><div style="{F}font-size:34px;font-weight:bold;letter-spacing:1px;color:#000000;font-family:Georgia,serif">O Diário {{{{loja_nome}}}}</div><div style="{F}font-size:12px;color:#555555;padding:6px 0 10px">Edição de {{{{data_extenso}}}}</div></td></tr>'
  +txt("{{manchete}}",30,"bold","left","24px 40px 12px","#000000",1.15)+txt("{{linha_fina}}",17,"normal","left","0 40px 20px")
  +cupom()+btn()+prazo()+grade(4)+garantias())
T["A-figurinha"]=("Figurinha (desbloquear e revelar)",
  txt("{{nome}}, você desbloqueou",18,"normal","center","0 40px 8px")+
  caixa('<div style="text-align:center"><div style="font-size:13px;color:#555555">Figurinha dourada nº {{numero}}</div><div style="font-size:44px;font-weight:bold;padding:12px 0">{{oferta_titulo}}</div><div style="font-size:14px">Toque no botão para revelar o seu cupom</div></div>',"#000000","#ffffff")
  +btn("Revelar meu cupom")+prazo()+grade(4,"Use aqui")+garantias())
T["A-sexta-premiada"]=("Sexta premiada",
  oferta_hero("Prêmio de hoje para {{nome}}")+cupom("Seu prêmio")+btn("Resgatar meu prêmio")+txt("Vale até sábado, {{prazo}}",14,"bold","center","0 40px 20px")+grade(4)+garantias())
T["A-ligacao"]=("Ligação",
  caixa('<div style="font-size:12px;color:#555555">Chamada perdida · {{hora_envio}}</div><div style="font-size:22px;font-weight:bold;padding:6px 0">{{loja_nome}}</div><div style="font-size:15px">Deixou um recado: {{oferta_titulo}} até {{prazo}}.</div>',"#d9d9d9","#f5f5f5")
  +btn("Ouvir o recado")+oferta_hero("O recado")+cupom()+grade(4)+garantias())
T["A-favoritos"]=("Favoritos",
  txt("{{nome}}, estes foram os mais pedidos no {{evento_anterior}}",22,"bold","center","0 40px 8px",lh=1.25)+txt("Ainda com estoque, com {{oferta_titulo}} até {{prazo}}.",16,"normal","center")+grade(6)+cupom()+btn()+garantias())
T["A-curta"]=("Uma tela (00h, reenvio, última chamada)",
  txt("{{linha_de_contexto}}",14,"normal","center","8px 40px 8px","#555555")+txt("{{oferta_titulo}}",44,"bold","center","0 40px 12px",lh=1.05)+txt("Termina às {{hora_fim}}",18,"bold","center","0 40px 16px")+cupom()+btn()+grade(2))
T["B-convite"]=("Convite (D-6)",
  caixa('<div style="text-align:center"><div style="font-size:13px;color:#555555">Convite pessoal</div><div style="font-size:28px;font-weight:bold;padding:8px 0">{{nome}}, você foi convidado para o {{evento}}</div><div style="font-size:15px">{{data_evento}}, só para a lista</div></div>')
  +txt("<b>Como vai funcionar</b><br>07h: seu cupom é liberado<br>11h: lembrete para quem ainda não viu<br>18h: a última atualização do dia<br>23h59: tudo volta ao preço normal",15,pad="0 40px 20px")
  +btn("Confirmar minha presença","{{link_confirmar_tag}}")
  +txt("Status: <b>convite enviado</b> › confirmado › acesso liberado",13,"normal","center","0 40px 28px","#555555"))
T["B-agenda"]=("Agenda com FAQ (D-3)",
  txt("{{nome}}, faltam 3 dias para o {{evento}}",26,"bold","center","0 40px 16px",lh=1.2)
  +'<tr><td class="px" style="padding:0 40px 20px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="'+F+'font-size:15px;color:#000000;border-top:1px solid #000000">'+"".join(f'<tr><td style="padding:12px 0;border-bottom:1px solid #e5e5e5;width:80px"><b>{h}</b></td><td style="padding:12px 0;border-bottom:1px solid #e5e5e5">{d}</td></tr>' for h,d in [("07h","Seu cupom é liberado"),("11h","Lembrete"),("18h","Última atualização"),("23h59","Encerramento")])+'</table></td></tr>'
  +txt("<b>Perguntas frequentes</b><br><br><b>Vale para o site todo?</b> {{faq_1}}<br><b>Como uso o cupom?</b> {{faq_2}}<br><b>Tem frete grátis?</b> {{faq_3}}<br><b>Qual o prazo de entrega?</b> {{faq_4}}",15,pad="0 40px 20px")
  +txt("<b>Para não perder:</b> ative o alarme para as 7h, confira seu endereço na conta e salve os favoritos.",15,pad="0 40px 16px")+btn("Ver o que vai entrar"))
T["C-notificacao"]=("Notificação do futuro / aviso",
  caixa('<div style="font-size:13px;font-weight:bold;padding-bottom:8px">⚠️ Ação pendente</div><div style="font-size:18px;line-height:1.45">{{nome}}, falta você confirmar esse pedido.</div><div style="font-size:15px;color:#333333;padding-top:8px">{{oferta_titulo}} reservado até {{prazo}}.</div>',"#000000","#ffffff")
  +btn("Confirmar meu pedido")+cupom()+grade(2)+garantias())
T["C-ressaca"]=("Ressaca (D+2, só com estoque real)",
  caixa('<div style="font-size:13px;font-weight:bold;padding-bottom:8px">Aviso</div><div style="font-size:18px;line-height:1.45">Lamentamos informar que os itens abaixo estão com poucas unidades no preço do {{evento}}.</div>')
  +grade(4)+btn("Ver o que sobrou"))
T["C-prazo"]=("Prazo de entrega",
  caixa('<div style="text-align:center"><div style="font-size:13px;color:#555555">Para chegar antes do Natal</div><div style="font-size:36px;font-weight:bold;padding:8px 0">Peça até {{data_corte}}</div><div style="font-size:15px">{{tipo_frete}} · entrega estimada até {{data_entrega}}</div></div>')
  +btn("Escolher o presente")+grade(4)+garantias())
T["D-texto"]=("Texto com pessoa no remetente",
  txt("Oi, {{nome}},",16,pad="8px 40px 16px")+txt("{{paragrafo_1}}",16)+txt("<b>{{oferta_titulo}}</b> com o cupom <b>{{cupom}}</b>, até {{prazo}}.",16)+txt('<a href="{{link}}" style="color:#000000;font-weight:bold">{{cta}}</a>',16)+txt("{{remetente_nome}}<br>{{remetente_cargo}}, {{loja_nome}}",16,pad="8px 40px 28px")+txt("P.S. {{ps}}",15,pad="0 40px 28px",color="#333333"))
T["A-guia-presentes"]=("Guia de presentes",
  txt("Presentes separados por faixa de preço",26,"bold","center","0 40px 16px",lh=1.2)+"".join(grade(2,f"Até {{{{faixa_{i}}}}}") for i in range(1,4))+cupom()+btn()+garantias())
T["A-vale-presente"]=("Vale-presente digital",
  txt("O presente que chega em 1 minuto",30,"bold","center","0 40px 12px",lh=1.15)+txt("Perdeu o prazo de entrega? O vale-presente chega por e-mail na hora e a pessoa escolhe o que quiser.",16,"normal","center")
  +caixa('<div style="text-align:center"><div style="font-size:13px;color:#555555">Vale-presente {{loja_nome}}</div><div style="font-size:34px;font-weight:bold;padding:8px 0">{{valores}}</div></div>')+btn("Enviar um vale-presente")+garantias())
os.makedirs("html",exist_ok=True)
cards=[]
for k,(nome,body) in T.items():
    open(f"html/{k}.html","w").write(page(nome,body))
    cards.append(f'<section><h2>{nome}</h2><p><code>{k}.html</code></p><iframe src="{k}.html" loading="lazy"></iframe></section>')
open("html/index.html","w").write("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>Modelos de e-mail Convertfy</title><style>
body{font-family:Arial,Helvetica,sans-serif;margin:0;padding:32px;background:#fff;color:#000}h1{font-size:28px;margin:0 0 8px}p.i{margin:0 0 32px;color:#444;max-width:70ch}
main{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:32px}section h2{font-size:17px;margin:0 0 4px}section p{margin:0 0 8px;color:#555;font-size:13px}
iframe{width:100%;height:760px;border:1px solid #ddd}</style></head><body><h1>Modelos de e-mail da Convertfy</h1>
<p class="i">Estruturas A (notificação com oferta na primeira tela), B (convite com agenda), C (aviso de sistema) e D (texto com pessoa). Layout neutro: fundo branco, texto preto. Tudo entre chaves duplas é variável preenchida por loja.</p><main>"""+"".join(cards)+"</main></body></html>")
print(len(T))
