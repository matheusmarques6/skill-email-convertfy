import io,contextlib,os,shutil,re,datetime,json
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(open('gen.py').read().split("hc=collections")[0])
from assuntos import F as FAM, familia, estrategia
OUT='/home/claude/cdpack/Pacote_ClaudeDesign_BlueWolf_Q4'
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT+'/referencias'); os.makedirs(OUT+'/lotes')
WD=['seg','ter','qua','qui','sex','sáb','dom']
def nd(s): return s.replace('—',',')
# ---------- paletas por momento ----------
PAL=[
 ("10.10 Perfect 10",lambda e:e['data']<='2026-10-13' and e['data']>='2026-10-01',dict(primaria="#29506D (navy Blue Wolf)",secundaria="#4588B9 (azul aço)",acento="#C9A45C (dourado de nota máxima: estrelas, selo 10/10)",fundo="gradiente #1E3A52 → #29506D; cards de avaliação em #F4F7FA",clima="Editorial e caloroso, voz de cliente. Estrelas e selos dourados, cartões de avaliação com foto real. Nada de festa: é reconhecimento de qualidade.")),
 ("Lista de espera e Pré-Black",lambda e:'2026-10-14'<=e['data']<='2026-10-24',dict(primaria="#010115 (quase preto)",secundaria="#4588B9 (azul aço, o \"ligado\")",acento="#FFFFFF",fundo="#010115 com brilho azul suave atrás do elemento principal",clima="Prévia da Black: escuro, limpo, um brilho azul marcando o que está ligado. É o primeiro contato com o tom da Black, ainda sem o amarelo.")),
 ("Halloween da gerente",lambda e:'2026-10-25'<=e['data']<='2026-11-01',dict(primaria="#121212",secundaria="#29506D",acento="#C8662B (laranja queimado, só em detalhes)",fundo="#121212 com textura sutil e luz de lua fria",clima="Halloween elegante, não infantil: noite, luz fria, um toque de laranja queimado. Nada de desenho animado.")),
 ("11.11 Black Antecipada",lambda e:'2026-11-02'<=e['data']<='2026-11-16',dict(primaria="#010115",secundaria="#4588B9",acento="#C7CED6 (prata: selo VIP, convite, cartão de membro)",fundo="#010115 com gradiente para #0E2233",clima="Exclusivo e formal: convite, lista selecionada, prata e azul. O fundador fala; o visual é de acesso restrito, não de liquidação.")),
 ("Black Week",lambda e:'2026-11-17'<=e['data']<='2026-11-29',dict(primaria="#000000",secundaria="#FFFFFF",acento="#F2C200 (amarelo de fita, só em faixas e selos) + #4588B9 em links e detalhes",fundo="#000000 chapado ou com textura de papel preto",clima="O pico do ano: alto contraste, números enormes, fitas diagonais de Black Friday (como no e-mail de 2025), energia de evento. Cada dia com um destaque diferente, mesma família visual.")),
 ("Cyber",lambda e:'2026-11-30'<=e['data']<='2026-12-02',dict(primaria="#010115",secundaria="#35C8FF (ciano elétrico)",acento="#4588B9",fundo="#010115 com grade em perspectiva sutil",clima="Tecnológico e rápido, derivado da Black mas com outra cor: é uma oferta nova (o combo), não a Black esticada.")),
 ("12.12 e Natal",lambda e:'2026-12-03'<=e['data']<='2026-12-22',dict(primaria="#14283A (navy profundo)",secundaria="#9E2B34 (vinho)",acento="#C9A45C (dourado)",fundo="#F6F1E7 (creme) nas seções de texto; #14283A nos heroes",clima="Presente e prazo: papel de presente, fita, etiqueta, rastreamento de entrega. Quente e organizado, sem clichê de Papai Noel.")),
 ("Boxing Day",lambda e:e['data']=='2026-12-26',dict(primaria="#29506D",secundaria="#FFFFFF",acento="#9E2B34",fundo="#29506D",clima="Liquidação britânica de pós-Natal: direto, limpo, vermelho só no selo.")),
 ("Fim de ano",lambda e:e['data']>='2026-12-27',dict(primaria="#0B0B0F",secundaria="#C9A45C (champanhe)",acento="#FFFFFF",fundo="#0B0B0F",clima="Encerramento e agradecimento: preto e champanhe, sóbrio.")),
]
def paleta(e):
    for n,f,p in PAL:
        if f(e): return n,p
    return PAL[0][0],PAL[0][2]
SISTEMA=("Notificação do futuro, aviso de estoque e avisos de sistema","Fundo branco #FFFFFF, texto #000000, alerta #E05252, cinza #64748B. É o visual que teve os maiores cliques do trimestre: manter, mesmo dentro de uma janela escura.")
# ---------- lotes ----------
LOTES=[("L1_Outubro_10.10","2026-10-01","2026-10-13"),("L2_Outubro_PreBlack_Halloween","2026-10-14","2026-10-31"),
 ("L3_Novembro_11.11_antecipacao","2026-11-01","2026-11-10"),("L4_Novembro_11.11_dia_e_pos","2026-11-11","2026-11-16"),
 ("L5_Novembro_BlackWeek_antecipacao","2026-11-17","2026-11-24"),("L6_Novembro_BlackWeek_dias","2026-11-25","2026-11-29"),
 ("L7_Cyber","2026-11-30","2026-12-02"),("L8_Dezembro","2026-12-03","2026-12-31")]
used=set()
def is_text(e): return str(e.get('hero_tipo','')).startswith('Texto puro') and not e.get('prompt_custom')
def slug(s): 
    s=re.sub(r'[^a-z0-9]+','-',s.lower().encode('ascii','ignore').decode()); return s.strip('-')[:40]
for nome,a,b in LOTES:
    es=[e for e in P if a<=e['data']<=b]
    L=[f"# Lote {nome.replace('_',' ')}","",
       "Cole o prompt do lote (arquivo 04) e anexe as imagens da lista \"Referências para anexar\" de cada e-mail. Os e-mails de texto puro deste lote não precisam de design: vão direto no editor de texto da Omnisend.",""]
    refs_lote=[]
    for e in es:
        d=datetime.date.fromisoformat(e['data']); pid=f"BW_{e['data']}_{e['hora'].replace(':','')}_{slug(e['nome'])}"
        L+=["---",f"## {pid}",f"**{d.strftime('%d/%m')} ({WD[d.weekday()]}) às {e['hora']} · {nd(e['nome'])}**",""]
        if is_text(e):
            L+=["**TEXTO PURO: não desenhar.** Vai no editor de texto da Omnisend.",f"- Assunto (EN): {e['assunto_en']}",f"- Copy base: "+" / ".join(nd(x) for x in e['blocos']),""]
            continue
        pn,p=paleta(e)
        sysl = e.get('hero_tipo','') in ('Aviso de sistema','Notificação de pedido','Notificação de sistema (pedido)','Notificação de entrega')
        L+=[f"- **Papel na sequência:** {nd(e['papel'])}",f"- **Na história:** {nd(e.get('historia',''))}",f"- **Contexto:** {nd(e['contexto'])}",
            f"- **Estratégia:** {nd(estrategia(e)['mecanismo'])}",
            f"- **Oferta:** {nd(e['oferta'])}",
            f"- **Assunto (EN):** {e['assunto_en']} · família \"{FAM[familia(e)]['nome']}\"",
            f"- **Momento e paleta:** {pn} · cor primária {p['primaria']} · cor secundária {p['secundaria']} · acento {p['acento']} · fundo {p['fundo']}"+(f" · **exceção:** {SISTEMA[1]}" if sysl else ""),
            f"- **Direção de arte do momento:** {p['clima']}",
            f"- **Hero:** {nd(e.get('hero_tipo',''))}: {nd(e.get('hv',''))}",
            f"- **Ordem dos blocos:** {nd(e.get('est',''))}",
            "- **Copy base (em português; escrever a versão final em inglês com o mesmo sentido e tamanho):**",
            f"  - Título: {nd(e['hero'])}"]+([f"  - Subtítulo: {nd(e['sub'])}"] if e['sub'] else [])+[f"  - {i+1}. {nd(x)}" for i,x in enumerate(e['blocos'])]+[
            f"  - Botão: {nd(e['cta'])} · Urgência: {nd(e['urgencia'])}"]
        L+=["- **Referências para anexar:**"]
        for k in e['ref']:
            r=R[k]
            if not r['img']: L+=[f"  - (sem imagem) {nd(r['nome'])}: {nd(r['copy'])[:300]}"]; continue
            fn=f"REF_{k}.jpg"; used.add(k); refs_lote.append(fn)
            en=figtext(r['fig'],'EN') if r.get('fig') else None
            L+=[f"  - `{fn}` · {nd(r['nome'])} · o que aproveitar: {nd(r['copy'])[:260]} · dado: {nd(r['dado'])[:160]}"]
            if en: L+=[f"    - Copy real em inglês (tom e tamanho de referência): {nd(' · '.join(en['textos']))[:700]}"]
        L+=[""]
    open(f"{OUT}/lotes/{nome}.md",'w').write('\n'.join(L))
    open(f"{OUT}/lotes/{nome}_ANEXAR.txt",'w').write('\n'.join(sorted(set(refs_lote))))
# ---------- imagens ----------
import glob
src_dirs=['/home/claude/pk/img','/tmp/e25/crops','/home/claude/cal5/img']
for k in used:
    img=R[k]['img']
    for d in src_dirs:
        pth=os.path.join(d,img)
        if os.path.exists(pth): shutil.copy(pth,f"{OUT}/referencias/REF_{k}.jpg"); break
# originais em alta das peças novas e da Well Copy
for up,n in [('/mnt/user-data/uploads/1790033097187_image.png','REF_credit_ORIGINAL.png'),('/mnt/user-data/uploads/1790033273577_image.png','REF_xidax_ORIGINAL.png')]:
    shutil.copy(up,f"{OUT}/referencias/{n}")
print(len(used),'referências', len(os.listdir(OUT+'/referencias')))
