import base64, html, datetime, collections, re, json
from assuntos import F as FAM, familia, estrategia, tipo
from refs import R
from plan_out import OUT
from plan_nov import NOV_A
from plan_nov_bw import NOV as NOV_OLD
from plan_dez import DEZ
from extras import X, CREDIT
NOV=NOV_A+[e for e in NOV_OLD if e['data']>='2026-11-25']
DEZ=[e for e in DEZ if e['data']!='2026-12-28']+[CREDIT]
for e in NOV+DEZ:
    if 'hero_tipo' in e: continue
    x=X.get((e['data'],e['hora']))
    if x:
        e['hero_tipo']=x['hero_tipo']; e['hv']=x['hv']; e['est']=x['est']; e['ideia']=x['ideia']
        for k in x['add']:
            if k not in e['ref']: e['ref'].append(k)
        if x['blk']: e['blocos']=[x['blk']]+e['blocos']
from historia import H, patch, patch2, patch3, patch4
patch(NOV,DEZ); patch2(OUT,NOV,DEZ); patch3(NOV); patch4(OUT,NOV,DEZ)
for e in NOV+DEZ:
    if 'historia' not in e: e['historia']=H.get((e['data'],e['hora']),'')
P=sorted(OUT+NOV+DEZ,key=lambda e:(e['data'],e['hora']))
missing=[(e['data'],e['hora']) for e in P if 'hero_tipo' not in e or not e.get('historia')]
print('faltando:',missing)
WD=["seg","ter","qua","qui","sex","sáb","dom"]
MES={10:"Outubro",11:"Novembro",12:"Dezembro"}
esc=html.escape
def b64(f): return "data:image/jpeg;base64,"+base64.b64encode(open("img/"+f,"rb").read()).decode()
def md(s): return re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",esc(s))
def dd(e): return datetime.date.fromisoformat(e['data'])
def pub(p): return " · ".join(f"<b>{k}</b> {esc(v)}" for k,v in p.items())

BANCO=json.load(open('/home/claude/cal5/banco_figma.json'))
def figtext(fig,linha):
    nomes=fig[1] if isinstance(fig[1],list) else [fig[1]]
    for o in BANCO:
        if o['mes']==fig[0] and o['nome'] in nomes and o['linha'].startswith(linha): return o
    return None
def clip(t,n=1100): return t if len(t)<=n else t[:n].rsplit(' ',1)[0]+' [...]'
def prompt(e):
    if e.get('prompt_custom'): return e['prompt_custom']
    if str(e.get('hero_tipo','')).startswith('Texto puro'):
        return 'E-mail de texto puro: não gerar imagem. Montar no editor de texto da Omnisend, fundo branco, fonte padrão, links em caixa alta com >>>, assinatura do fundador.'
    bl=[re.sub(r'\s*\((?:[^()]*?(?:tag|grava|dado real|Shopify|limite real|real da loja|versão Brasil|como o|como nas|da Black Week de 2025|do 11.11 de 2025)[^()]*)\)','',re.sub(r'\*\*','',b)) for b in e['blocos'] if not b.startswith('Hero:')]
    partes=[f'{i+3}) {b}' for i,b in enumerate(bl)]
    return ('Crie a imagem de um e-mail marketing vertical para celular, com 600 px de largura, da loja [NOME DA LOJA] ([segmento]). '
      'Use a identidade da loja: logo no topo, cor primária [cor], cor secundária [cor], títulos em caixa alta com tipografia sem serifa bold, fotos reais dos produtos, visual de e-commerce premium. '
      f'Estrutura de cima para baixo: 1) Logo centralizado. 2) Hero: {e["hv"]}. Título: "{e["hero"]}".' + (f' Subtítulo: "{e["sub"]}".' if e['sub'] else '') + ' '
      + ' '.join(partes) + f' Botão principal: "{e["cta"]}". '
      'Por último, faixa com 3 garantias (envio rápido com rastreio, pagamento seguro, qualidade nos produtos) e rodapé com a logo. '
      'Todos os textos em português do Brasil, escritos exatamente como acima, sem travessão. Onde houver colchetes, deixe o espaço marcado. Não invente números, notas ou avaliações.')
def estr_block(e):
    s=estrategia(e)
    return (f'<div class="estr"><div class="lbl">Estratégia</div><p><b>Objetivo:</b> {esc(s["objetivo"])}</p>'
            f'<p><b>Como funciona:</b> {esc(s["mecanismo"])}</p><p><b>Ação esperada:</b> {esc(s["acao"])}</p><p><b>Como medir:</b> {esc(s["medir"])}</p></div>')
def assu_block(e):
    f=FAM[familia(e)]
    base=''.join(f'<li>{esc(b)}</li>' for b in f['base'])
    return (f'<div class="assu"><div class="lbl">Assunto: como deve ser</div><p><b>Família:</b> {esc(f["nome"])}. {esc(f["regra"])}</p>'
            f'<p><b>Assuntos de base (validados):</b></p><ul>{base}</ul><p><b>Assunto escolhido:</b> {esc(e["assunto"])} · <b>Pré-cabeçalho:</b> {esc(e["pre"])}</p></div>')
def abrow(e):
    if e.get('ab')=='simples':
        return '<dt>Teste A/B</dt><dd><b>Omnisend, A/B de assunto:</b> A = conservador, B = equilibrado · 20% da lista às 08h (10% cada) · vence o maior clique em 2 horas (se a conta só tiver abertura, usar abertura) · os outros 80% recebem o vencedor às 10h · o ousado fica de reserva para o próximo teste · anotar o vencedor na planilha da conta</dd>'
    if e.get('ab')=='duplo':
        return '<dt>Teste A/B</dt><dd><b>Omnisend, A/B de assunto só na versão maior</b> (a que vai para quem ainda não agiu), com A = conservador e B = equilibrado, 20% às 08h e o vencedor às 10h. A versão de quem já confirmou sai sem teste, às 10h.</dd>'
    return ''
def card(e,uso):
    d=dd(e); refs=[R[k] for k in e['ref']]
    main=next((r for r in refs if r['img']),None)
    fig=(f'<div class="mainimg"><img src="{b64(main["img"])}"><div class="cap">{esc(main["nome"])}</div></div>' if main else
         f'<div class="mainimg"><div class="cite"><div class="ct">Referência sem imagem no pacote (anexar print)</div><div class="cn">{esc(refs[0]["nome"])}</div></div></div>')
    tags=[f'<span class="tag">{esc(e["janela"])}</span>',f'<span class="tag pap">{esc(e["papel"])}</span>']
    ev=e.get('evid','validado'); tags.append(f'<span class="tag ev">{esc(ev.capitalize())}</span>')
    if e.get('booster'): tags.append('<span class="tag bo">Booster</span>')
    if e.get('teste'): tags.append('<span class="tag te">Teste</span>')
    if e.get('trilha'): tags.append(f'<span class="tag">Trilha {esc(e["trilha"].replace("_"," e ").upper())}</span>')
    bo=e.get('booster')
    borow=f'<dt>Booster</dt><dd>Campaign Booster · <b>{esc(bo["para"])}</b> · {esc(bo["quando"])} · assunto: <b>{esc(bo["assunto"])}</b></dd>' if bo else ''
    blocos="".join(f"<li>{md(b)}</li>" for b in e['blocos'])
    extra=""
    if e.get('canais'): extra+=f'<p class="ex"><b>Canais de apoio:</b> {esc(e["canais"])}</p>'
    if e.get('teste'): extra+=f'<p class="ex"><b>Teste:</b> {esc(e["teste"])}</p>'
    rows=""
    for r in refs:
        img=f'<img class="rimg" src="{b64(r["img"])}">' if (r['img'] and r is not main) else ''
        tx=f'<p class="rc"><b>Estrutura e copy:</b> {esc(r["copy"])}</p>'
        if r.get('fig'):
            en=figtext(r['fig'],'EN'); pt=figtext(r['fig'],'PT')
            if en: tx+=f'<p class="rc"><b>Copy real, versão inglês (Figma):</b> {esc(clip(" · ".join(en["textos"])))}</p>'
            if pt: tx+=f'<p class="rc"><b>Copy real, versão Brasil (Figma):</b> {esc(clip(" · ".join(pt["textos"])))}</p>'
        tx+=f'<p class="rd"><b>Dado:</b> {esc(r["dado"])}</p>'
        rows+=f'<div class="refrow">{img}<div class="rtx"><div class="rn">{esc(r["nome"])}{" (imagem ao lado do plano)" if r is main else ""}</div>{tx}</div></div>'
    return f"""<section class="card">
<header><div class="dt"><span class="d">{d.strftime("%d/%m")}</span><span class="w">{WD[d.weekday()]}</span><span class="h">{e["hora"]}</span></div>
<div class="tt"><h3>{esc(e["nome"])}</h3><div class="ctx">{esc(e["contexto"])}</div><div class="tags">{"".join(tags)}</div></div></header>
<div class="grid"><div class="left">
<dl><dt>Público</dt><dd>{pub(e["publico"])}</dd>
<dt>Oferta</dt><dd>{md(e["oferta"])}</dd>
<dt>Assunto</dt><dd class="subj">{esc(e["assunto"])}<br><span class="en">EN: {esc(e["assunto_en"])}</span></dd>
<dt>Pré-cabeçalho</dt><dd>{esc(e["pre"])}</dd>{borow}{('<dt>Opções de assunto</dt><dd>'+'<br>'.join(esc(x) for x in e['assuntos3'])+'</dd>') if e.get('assuntos3') else ''}{abrow(e)}</dl>
<div class="copy"><div class="lbl">Copy base</div><p class="hd">{md(e["hero"])}</p>{f'<p class="sb">{md(e["sub"])}</p>' if e["sub"] else ''}<ol>{blocos}</ol>
<p class="cta">Botão: {esc(e["cta"])}{f' · <span class="urg">{esc(e["urgencia"])}</span>' if e["urgencia"] else ''}</p></div>
<div class="hist"><div class="lbl">Na história</div><p>{esc(e.get("historia",""))}</p></div>
{estr_block(e)}
<div class="est"><div class="lbl">Estrutura sugerida</div><p><b>Hero:</b> {esc(e.get("hero_tipo",""))}. {esc(e.get("est",""))}</p></div>
<div class="why"><div class="lbl">Por que foi escolhido</div><p>{esc(e["conexao"])}</p>{extra}</div>
{assu_block(e)}
</div>{fig}</div>
<div class="prm"><div class="lbl">Prompt para gerar a imagem no ChatGPT</div><p>{esc(prompt(e))}</p></div>
<div class="refs"><div class="lbl">E-mails de referência: copy real</div>{rows}</div>
</section>"""

# ---------- intro sections ----------
INTRO=open("intro.html").read()
# overview table
rows=""; cur=None
for e in P:
    d=dd(e)
    bo=" + booster "+e['booster']['quando'].split(' ')[0] if e.get('booster') else ""
    rows+=f"<tr><td>{d.strftime('%d/%m')} {WD[d.weekday()]}</td><td>{e['hora']}{bo}</td><td>{esc(e['janela'])}</td><td>{esc(e['nome'])}</td><td>{esc(e['assunto'])}</td><td>{esc(e['oferta'][:90])}{'...' if len(e['oferta'])>90 else ''}</td></tr>"
cnt=collections.Counter(dd(e).month for e in P); nb=sum(1 for e in P if e.get('booster'))
resumo=f"<p>{len(P)} e-mails desenhados ({cnt[10]} em outubro, {cnt[11]} em novembro, {cnt[12]} em dezembro) e {nb} boosters da Omnisend para quem não abriu.</p>"
cards=[]; cm=None
TOT=collections.Counter(e['nome'].split(' (')[0] for e in P)
seen=collections.Counter()
for e in P:
    d=dd(e)
    if d.month!=cm:
        cm=d.month; cards.append(f'<h1 class="mes">{MES[cm]}</h1>')
    k=e['ref'][0]; seen[k]+=1
    uso=""
    cards.append(card(e,uso))
hc=collections.OrderedDict()
for e in P: hc.setdefault(e.get('hero_tipo','-'),[]).append(dd(e).strftime('%d/%m')+(' '+e['hora'] if e['hora']!='10:00' else ''))
heroes=''.join(f"<tr><td>{esc(k)}</td><td>{len(v)}</td><td>{esc(', '.join(v))}</td></tr>" for k,v in sorted(hc.items(),key=lambda kv:-len(kv[1])))
CSS=open("style.css").read()
doc=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>Calendário Q4 2026 | Convertfy</title><style>{CSS}</style></head><body>
{INTRO.replace("{{RESUMO}}",resumo).replace("{{HEROES}}",heroes)}
<h2 class="pb">10. Visão geral dos envios</h2><table class="ov"><tr><th>Data</th><th>Hora</th><th>Janela</th><th>E-mail</th><th>Assunto</th><th>Oferta</th></tr>{rows}</table>
{"".join(cards)}</body></html>'''
open("calendario.html","w").write(doc); print(len(P),cnt,nb)
