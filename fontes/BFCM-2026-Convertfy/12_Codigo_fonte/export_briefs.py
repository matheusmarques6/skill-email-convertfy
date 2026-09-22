import io,contextlib,json,re
buf=io.StringIO()
src=open('gen.py').read()
with contextlib.redirect_stdout(buf):
    exec(src.split("hc=collections")[0])
from assuntos import F as FAM, familia, estrategia
REGRAS=["Português do Brasil (e a versão em inglês para lojas globais, a partir do assunto_en).",
 "Frases curtas e diretas. Nada de floreio: a história aparece só na assinatura (a [Gerente] ou o [Fundador]) e nos ganchos entre e-mails.",
 "Nunca usar travessão. Usar ponto, vírgula ou dois-pontos. (Nas transcrições de copy real, o travessão original foi trocado por vírgula.)",
 "Um botão principal por e-mail, com o texto do campo cta. O cupom sempre visível perto do botão.",
 "Oferta, cupom e prazo na primeira tela nos e-mails de venda.",
 "Nada de número inventado: o que está entre colchetes ([N], [valor], [produto], [prazo]) vem da loja. Se não tiver o dado real, o bloco sai.",
 "O assunto segue a família indicada. O pré-cabeçalho completa o assunto com a oferta ou o prazo, sem repetir o assunto.",
 "Nenhum assunto repete a promessa do e-mail anterior da mesma sequência.",
 "Usar a copy real das referências como modelo de tom e tamanho, não como texto a copiar."]
out=[]
for e in P:
    refs=[]
    for k in e['ref']:
        r=R[k]; d=dict(nome=r['nome'],estrutura_e_copy=r['copy'],dado=r['dado'])
        if r.get('fig'):
            en=figtext(r['fig'],'EN'); pt=figtext(r['fig'],'PT')
            if en: d['copy_real_en']=' · '.join(en['textos']).replace(' — ',', ').replace('—',', ')
            if pt: d['copy_real_pt']=' · '.join(pt['textos']).replace(' — ',', ').replace('—',', ')
        refs.append(d)
    f=FAM[familia(e)]
    out.append(dict(
      data=e['data'],hora=e['hora'],nome=e['nome'],janela=e['janela'],papel=e['papel'],contexto=e['contexto'],
      na_historia=e.get('historia',''),publico=e['publico'],oferta=e['oferta'],
      estrategia=estrategia(e),por_que_foi_escolhido=e['conexao'],
      assunto=dict(familia=f['nome'],regra=f['regra'],assuntos_de_base=f['base'],escolhido=e['assunto'],en=e['assunto_en'],opcoes=e.get('assuntos3',[]),teste_ab=e.get('ab') or None,pre_cabecalho=e['pre']),
      estrutura=dict(hero_tipo=e.get('hero_tipo'),hero_visual=e.get('hv'),ordem_dos_blocos=e.get('est')),
      copy_base=dict(hero=e['hero'],subtitulo=e['sub'],blocos=e['blocos'],botao=e['cta'],urgencia=e['urgencia']),
      referencias=refs,booster=e.get('booster'),canais=e.get('canais'),teste=e.get('teste'),prompt_imagem=prompt(e)))
json.dump(dict(regras_de_copy=REGRAS,emails=out),open('/mnt/user-data/outputs/Briefs_Q4_2026_Convertfy.json','w'),ensure_ascii=False,indent=1)
L=["# Briefs de copy · Q4 2026 · Convertfy","","Um bloco por e-mail, na ordem do calendário. Cada bloco tem tudo o que a IA de copy precisa: estratégia, por que o e-mail foi escolhido, regra do assunto com os assuntos validados, estrutura, copy base e a copy real das referências.","","## Regras de copy (valem para todos os e-mails)",""]+[f"- {x}" for x in REGRAS]+[""]
WD=['seg','ter','qua','qui','sex','sáb','dom']
import datetime
for o in out:
    d=datetime.date.fromisoformat(o['data'])
    L+=[f"---",f"## {d.strftime('%d/%m')} ({WD[d.weekday()]}) {o['hora']} · {o['nome']}","",
        f"**Janela:** {o['janela']} · **Papel:** {o['papel']}",f"**Contexto:** {o['contexto']}",f"**Na história:** {o['na_historia']}",
        f"**Público:** A: {o['publico']['A']} · B: {o['publico']['B']} · C: {o['publico']['C']}",f"**Oferta:** {o['oferta']}","",
        "### Estratégia",f"- **Objetivo:** {o['estrategia']['objetivo']}",f"- **Como funciona:** {o['estrategia']['mecanismo']}",f"- **Ação esperada:** {o['estrategia']['acao']}",f"- **Como medir:** {o['estrategia']['medir']}","",
        "### Por que foi escolhido",o['por_que_foi_escolhido'],"",
        "### Assunto",f"- **Família:** {o['assunto']['familia']}. {o['assunto']['regra']}","- **Assuntos de base (validados):**"]+[f"  - {b}" for b in o['assunto']['assuntos_de_base']]+[
        f"- **Assunto escolhido:** {o['assunto']['escolhido']}",f"- **Em inglês:** {o['assunto']['en']}",f"- **Pré-cabeçalho:** {o['assunto']['pre_cabecalho']}"]
    if o['assunto']['opcoes']: L+=["- **Opções:**"]+[f"  - {x}" for x in o['assunto']['opcoes']]
    if o['assunto']['teste_ab']: L+=[f"- **Teste A/B:** A = conservador, B = equilibrado, 20% às 08h, vence o maior clique em 2h, vencedor para os 80% às 10h" + (" (só na versão de quem ainda não agiu)" if o['assunto']['teste_ab']=='duplo' else "")]
    L+=["","### Estrutura",f"- **Hero:** {o['estrutura']['hero_tipo']}: {o['estrutura']['hero_visual']}",f"- **Ordem dos blocos:** {o['estrutura']['ordem_dos_blocos']}","",
        "### Copy base",f"- **Hero:** {o['copy_base']['hero']}"]+([f"- **Subtítulo:** {o['copy_base']['subtitulo']}"] if o['copy_base']['subtitulo'] else [])+[f"{i+1}. {b}" for i,b in enumerate(o['copy_base']['blocos'])]+[
        f"- **Botão:** {o['copy_base']['botao']} · **Urgência:** {o['copy_base']['urgencia']}",""]
    if o['booster']: L+=[f"**Booster:** {o['booster']['para']} · {o['booster']['quando']} · assunto: {o['booster']['assunto']}",""]
    if o['canais']: L+=[f"**Canais:** {o['canais']}",""]
    L+=["### Referências (copy real)"]
    for r in o['referencias']:
        L+=[f"- **{r['nome']}**",f"  - Estrutura e copy: {r['estrutura_e_copy']}",f"  - Dado: {r['dado']}"]
        if r.get('copy_real_en'): L+=[f"  - Copy real (inglês): {r['copy_real_en']}"]
        if r.get('copy_real_pt'): L+=[f"  - Copy real (Brasil): {r['copy_real_pt']}"]
    L+=["",f"**Prompt de imagem:** {o['prompt_imagem']}",""]
open('/mnt/user-data/outputs/Briefs_Q4_2026_Convertfy.md','w').write('\n'.join(L))
print(len(out),'e-mails')
