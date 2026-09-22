import io,contextlib,os,shutil,re,json,datetime,glob
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(open('gen.py').read().split("hc=collections")[0])
from assuntos import F as FAM, familia, estrategia, tipo
from markdownify import markdownify as mdf
V='/home/claude/vault/BFCM-2026-Convertfy'
shutil.rmtree(V,ignore_errors=True)
for d in ['00_Indice','01_Estrategia','02_Calendario_Q4/Outubro','02_Calendario_Q4/Novembro','02_Calendario_Q4/Dezembro','03_Referencias_validadas','04_Assuntos','05_Modelos_validados','06_Figma_copy_real','07_Design_Blue_Wolf','08_Skill','09_Dados','10_Documentos','assets/referencias','assets/blue_wolf','assets/estudo','assets/wellcopy','assets/2025']:
    os.makedirs(f'{V}/{d}',exist_ok=True)
def safe(s): return re.sub(r'[\\/:*?"<>|#\[\]]','',s).strip()
def nd(s): return s.replace(' — ',', ').replace('—',', ') if isinstance(s,str) else s
WD=['seg','ter','qua','qui','sex','sáb','dom']
MES={'10':'Outubro','11':'Novembro','12':'Dezembro'}
# ---------- assets ----------
for k,r in R.items():
    if r['img']:
        for d in ['/home/claude/pk/img','/tmp/e25/crops','/home/claude/cal5/img']:
            p=os.path.join(d,r['img'])
            if os.path.exists(p): shutil.copy(p,f'{V}/assets/referencias/REF_{k}.jpg'); break
for f in glob.glob('/home/claude/pk/img/*'): shutil.copy(f,f'{V}/assets/blue_wolf/')
for f in glob.glob('/tmp/e25/crops/*'): shutil.copy(f,f'{V}/assets/2025/')
for f in glob.glob('/tmp/bpe/figma-best-performing-emails/*.png'): shutil.copy(f,f'{V}/assets/wellcopy/')
shutil.copy('/tmp/bpe/figma-best-performing-emails/racionais-verbatim-29-emails.md',f'{V}/03_Referencias_validadas/Well Copy - 29 conceitos (racionais).md')
for f in glob.glob('/mnt/user-data/outputs/final/imagens/estudo/*'): shutil.copy(f,f'{V}/assets/estudo/')
for up,n in [('/mnt/user-data/uploads/1790033097187_image.png','wellcopy_credit_activated.png'),('/mnt/user-data/uploads/1790033273577_image.png','xidax_your_gpu_called.png'),('/mnt/user-data/uploads/1790031503234_image.png','pourri_halloween.png'),('/mnt/user-data/uploads/Captura_de_Tela_2026-09-21_a_s_19_50_08.png','reabertura_2507_texto.png'),('/mnt/user-data/uploads/1790031406504_image.png','marca_americana_bfcm2025_lista.png')]:
    shutil.copy(up,f'{V}/assets/referencias/{n}')
# ---------- referências ----------
refnote={}
for k,r in R.items():
    name=f'REF {k}'; refnote[k]=name
    L=['---','tipo: referencia-de-email',f'chave: {k}','---',f'# {nd(r["nome"])}','']
    if r['img']: L+=[f'![[REF_{k}.jpg|300]]','']
    L+=[f'**Estrutura e copy:** {nd(r["copy"])}','',f'**Dado:** {nd(r["dado"])}','']
    if r.get('fig'):
        en=figtext(r['fig'],'EN'); pt=figtext(r['fig'],'PT')
        if en: L+=['## Copy real em inglês (Figma)',nd(' · '.join(en['textos'])),'',f'[Abrir no Figma]({en["figma"]})','']
        if pt: L+=['## Copy real versão Brasil (Figma)',nd(' · '.join(pt['textos'])),'',f'[Abrir no Figma]({pt["figma"]})','']
    usos=[e for e in P if k in e['ref']]
    if usos: L+=['## Onde entra no Q4 2026']+[f'- [[{e["data"]} {e["hora"].replace(":","")} {safe(e["nome"])}]]' for e in usos]
    open(f'{V}/03_Referencias_validadas/{name}.md','w').write('\n'.join(L))
# ---------- assuntos ----------
for fk,f in FAM.items():
    usos=[e for e in P if familia(e)==fk]
    L=['---','tipo: familia-de-assunto','---',f'# Assunto: {f["nome"]}','',f'**Regra:** {f["regra"]}','','## Assuntos de base (validados)']+[f'- {b}' for b in f['base']]+['','## Onde é usado no Q4 2026']+[f'- {e["assunto"]} → [[{e["data"]} {e["hora"].replace(":","")} {safe(e["nome"])}]]' for e in usos]
    open(f'{V}/04_Assuntos/Assunto - {safe(f["nome"])}.md','w').write('\n'.join(L))
# ---------- calendário: uma nota por e-mail ----------
for e in P:
    d=datetime.date.fromisoformat(e['data']); fam=FAM[familia(e)]; st=estrategia(e)
    fn=f'{e["data"]} {e["hora"].replace(":","")} {safe(e["nome"])}'
    fm=['---','tipo: email-q4-2026',f'data: {e["data"]}',f'hora: "{e["hora"]}"',f'janela: "{nd(e["janela"])}"',f'papel: "{nd(e["papel"]).replace(chr(34),chr(39))}"',f'categoria: {tipo(e)}',f'familia_assunto: "{fam["nome"]}"',f'hero: "{nd(e.get("hero_tipo",""))}"',f'booster: {"sim" if e.get("booster") else "não"}',f'teste_ab: {"sim" if e.get("ab") else "não"}',f'evidencia: "{e.get("evid","validado")}"','---']
    L=fm+[f'# {d.strftime("%d/%m")} ({WD[d.weekday()]}) {e["hora"]} · {nd(e["nome"])}','',
      f'**Contexto:** {nd(e["contexto"])}',f'**Na história:** {nd(e.get("historia",""))}',f'**Público:** A: {e["publico"]["A"]} · B: {e["publico"]["B"]} · C: {e["publico"]["C"]}',f'**Oferta:** {nd(e["oferta"])}','',
      '## Estratégia',f'- **Objetivo:** {nd(st["objetivo"])}',f'- **Como funciona:** {nd(st["mecanismo"])}',f'- **Ação esperada:** {st["acao"]}',f'- **Como medir:** {st["medir"]}','',
      '## Por que foi escolhido',nd(e['conexao']),'',
      '## Assunto',f'- **Família:** [[Assunto - {safe(fam["nome"])}]]',f'- **Escolhido:** {e["assunto"]}',f'- **Inglês:** {e["assunto_en"]}',f'- **Pré-cabeçalho:** {nd(e["pre"])}']
    if e.get('assuntos3'): L+=['- **Opções:**']+[f'  - {x}' for x in e['assuntos3']]
    if e.get('ab'): L+=['- **Teste A/B:** A = conservador, B = equilibrado · 20% às 08h · vence o maior clique em 2h · vencedor para 80% às 10h'+(' · só na versão de quem ainda não agiu' if e['ab']=='duplo' else '')]
    L+=['','## Estrutura',f'- **Hero:** {nd(e.get("hero_tipo",""))}: {nd(e.get("hv",""))}',f'- **Ordem dos blocos:** {nd(e.get("est",""))}','','## Copy base',f'**Título:** {nd(e["hero"])}']+([f'**Subtítulo:** {nd(e["sub"])}'] if e['sub'] else [])+['']+[f'{i+1}. {nd(x)}' for i,x in enumerate(e['blocos'])]+['',f'**Botão:** {nd(e["cta"])} · **Urgência:** {nd(e["urgencia"])}','']
    if e.get('booster'): L+=[f'**Booster:** {e["booster"]["para"]} · {e["booster"]["quando"]} · assunto: {e["booster"]["assunto"]}','']
    if e.get('canais'): L+=[f'**Canais:** {nd(e["canais"])}','']
    if e.get('teste'): L+=[f'**Teste:** {nd(e["teste"])}','']
    L+=['## Referências']+[f'- [[{refnote[k]}]]' for k in e['ref']]+['',f'## Prompt de imagem',nd(prompt(e))]
    open(f'{V}/02_Calendario_Q4/{MES[e["data"][5:7]]}/{fn}.md','w').write('\n'.join(L))
# ---------- estratégia: seções da abertura ----------
hc=collections.OrderedDict()
for e in P: hc.setdefault(e.get('hero_tipo','-'),[]).append(dd(e).strftime('%d/%m')+(' '+e['hora'] if e['hora']!='10:00' else ''))
heroes=''.join(f"<tr><td>{esc(k)}</td><td>{len(v)}</td><td>{esc(', '.join(v))}</td></tr>" for k,v in sorted(hc.items(),key=lambda kv:-len(kv[1])))
html=open('intro.html').read().replace('{{HEROES}}',heroes).replace('{{RESUMO}}',resumo)
parts=re.split(r'(?=<h2)',html)
n=0
for p in parts:
    m=re.search(r'<h2[^>]*>(.*?)</h2>',p)
    if not m: continue
    title=re.sub('<[^>]+>','',m.group(1)).strip()
    subs=re.split(r'(?=<h3)',p)
    if title.startswith('1.') and len(subs)>2:
        head=subs[0]
        open(f'{V}/01_Estrategia/{safe(title)}.md','w').write(nd(mdf(head,heading_style='ATX')))
        for s in subs[1:]:
            t=re.sub('<[^>]+>','',re.search(r'<h3[^>]*>(.*?)</h3>',s).group(1)).strip()
            open(f'{V}/01_Estrategia/{safe(t)}.md','w').write(nd(mdf(s,heading_style='ATX')))
    else:
        open(f'{V}/01_Estrategia/{safe(title)}.md','w').write(nd(mdf(p,heading_style='ATX')))
    n+=1
# ---------- figma copy real ----------
for o in json.load(open('banco_figma.json')):
    fn=safe(f'{o["mes"]} - {o["linha"]} - {o["nome"]} - {o["node_id"].replace(":","-")}')
    L=['---','tipo: email-figma-copy-real',f'mes: {o["mes"]}',f'linha: "{o["linha"]}"',f'node: "{o["node_id"]}"','---',f'# {o["nome"]} ({o["linha"]}, {o["mes"]})','',f'[Abrir no Figma]({o["figma"]}) · altura {o["altura"]} px','','## Textos na ordem de leitura']+[f'- {nd(t)}' for t in o['textos']]
    open(f'{V}/06_Figma_copy_real/{fn}.md','w').write('\n'.join(L))
# ---------- modelos validados (biblioteca anterior) ----------
for f in glob.glob('/mnt/user-data/outputs/planejamento-campanhas/obsidian/Convertfy/calendario/modelos/*.md'): shutil.copy(f,f'{V}/05_Modelos_validados/')
for f in ['principio-80-10-10.md','ranking-de-modelos.md','regras-de-copy-de-campanha.md','segmentacao-e-freios.md','convencao-de-nome-de-campanha.md','fontes-do-estudo.md','lojas-analisadas.md']:
    shutil.copy(f'/mnt/user-data/outputs/planejamento-campanhas/obsidian/Convertfy/calendario/{f}',f'{V}/05_Modelos_validados/')
# ---------- design Blue Wolf ----------
cd='/home/claude/cdpack/Pacote_ClaudeDesign_BlueWolf_Q4'
for f in glob.glob(cd+'/*.md'): shutil.copy(f,f'{V}/07_Design_Blue_Wolf/')
os.makedirs(f'{V}/07_Design_Blue_Wolf/lotes',exist_ok=True)
for f in glob.glob(cd+'/lotes/*'): shutil.copy(f,f'{V}/07_Design_Blue_Wolf/lotes/')
# ---------- dados ----------
shutil.copy('banco_figma.json',f'{V}/09_Dados/emails_figma_agosto_setembro.json')
shutil.copy('/home/claude/banco/emails_figma_agosto_setembro.csv',f'{V}/09_Dados/')
shutil.copy('/home/claude/banco/banco_referencias.json',f'{V}/09_Dados/')
shutil.copy('/mnt/user-data/outputs/Briefs_Q4_2026_Convertfy.json',f'{V}/09_Dados/')
shutil.copy('/mnt/user-data/outputs/planejamento-campanhas/dados/base_campanhas_convertfy.csv',f'{V}/09_Dados/base_campanhas_525_9_lojas.csv')
shutil.copy('/mnt/user-data/outputs/planejamento-campanhas/dados/base_campanhas_convertfy.xlsx',f'{V}/09_Dados/base_campanhas_525_9_lojas.xlsx')
shutil.copy('/mnt/user-data/outputs/planejamento-campanhas/dados/ranking_46_lojas_2026-09-21.csv',f'{V}/09_Dados/')
shutil.copy('/mnt/user-data/outputs/final/Base_de_dados (texto).md',f'{V}/09_Dados/Base de dados do estudo (dicionario e metodo).md')
# ---------- documentos ----------
shutil.copy('/mnt/user-data/outputs/Calendario_Q4_2026_Convertfy.pdf',f'{V}/10_Documentos/')
shutil.copy('/mnt/user-data/outputs/Briefs_Q4_2026_Convertfy.md',f'{V}/10_Documentos/')
shutil.copy('/mnt/user-data/uploads/Estudo_Base_BFCM_2026_Convertfy_completo.pdf',f'{V}/10_Documentos/')
shutil.copy('/mnt/user-data/uploads/Playbook_Q4_2026_Convertfy.pdf',f'{V}/10_Documentos/')
shutil.copy('/mnt/user-data/outputs/final/Estudo_Base_BFCM_2026 (texto).md',f'{V}/10_Documentos/Estudo Base BFCM 2026 (texto).md')
open(f'{V}/10_Documentos/Playbook Q4 2026 (texto).md','w').write('# Playbook Q4 2026 Convertfy (texto extraído do PDF)\n\n'+open('/tmp/pb.txt').read())
print('ok',n)
