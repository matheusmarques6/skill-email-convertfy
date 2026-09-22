import json, os
M=json.load(open('seed/modelos.json'))['modelos']; P=json.load(open('seed/plano_q4_2026.json')); R=json.load(open('seed/regras.json'))
B="obsidian/Convertfy/calendario"
for d in ["", "/modelos", "/planos/q4-2026"]: os.makedirs(B+d, exist_ok=True)
def fm(tipo,fonte,assunto): return f"---\ntipo: {tipo}\nautor: convertfy\nfonte: \"{fonte}\"\nstatus: aprovado\nassunto: {assunto}\n---\n"
def w(path,txt): open(f"{B}/{path}","w").write(txt)
def num(v): return "-" if v in (None,"") else (f"{v:.2f}".replace(".",",") if isinstance(v,(int,float)) else str(v))
FONTE9="Estudo Base BFCM 2026, 9 lojas Omnisend, mai a set/2026"; FONTE46="omnisend_campaign_metrics do admin, 46 lojas, 15/06 a 20/09/2026"
SL={"validado":"Titular","parcial":"Titular com ressalva","revisar":"Em revisão","reserva":"Reserva","fora":"Fora do calendário","teste":"Teste"}
# modelos
usos={}
for e in P['envios']: usos.setdefault(e['modelo'],[]).append(e)
for m in M:
    a9,a46=m.get('amostra_9',{}),m.get('amostra_46',{})
    u="".join(f"| {e['data'][8:]}/{e['data'][5:7]} | {e['hora']} | {e['objetivo']} |\n" for e in usos.get(m['key'],[]))
    txt=fm("modelo-de-email",f"{FONTE9}; {FONTE46}",m['key'])+f"""
{m['nome']}. Estrutura {m['estrutura']}, papel {m['papel'].replace('_',' ')}. Situação na biblioteca: **{SL[m['status']]}**.

# O dado

| Amostra | Mediana do índice | Lojas acima da média | Pedidos | Observação |
|---|---|---|---|---|
| 9 lojas (análise a fundo) | {num(a9.get('mediana'))} | {a9.get('acima','-')} | {a9.get('pedidos','-')} | {a9.get('nota','')} |
| 46 lojas (carteira) | {num(a46.get('mediana'))} | {a46.get('acima','-')} | {a46.get('pedidos','-')} | {a46.get('nota','')} |

Índice 1 é a média da própria loja. A mediana é o valor do meio entre as lojas que receberam o e-mail.

# Assunto testado

- Português: {m['assunto'].get('pt','-')}
- Inglês: {m['assunto'].get('en','-')}

# Como produzir

- **Copiar:** {m.get('copiar') or '-'}
- **Melhorar:** {m.get('melhorar') or '-'}
- **Referência:** {m.get('referencia',{}).get('figma','-')}
- **HTML:** modelo `{ {'A':'A-status-mudou','B':'B-convite','C':'C-notificacao','D':'D-texto'}[m['estrutura']] }.html` do pacote, ou o específico do modelo.
- **Nome na Omnisend:** o evento aparece como {", ".join(f'`{x}`' for x in m.get('alias_evento',[])) or 'novo'}.

# Onde entra no Q4 2026

""" + (("| Data | Hora | Papel no dia |\n|---|---|---|\n"+u) if u else "Não entra no calendário do Q4.\n") + "\nVoltar para [[mapa-do-calendario]] · [[ranking-de-modelos]]\n"
    w(f"modelos/{m['key']}.md", txt)
# ranking
ordem=sorted(M,key=lambda m:-(m.get('amostra_46',{}).get('mediana') or -1))
rk=fm("ranking",f"{FONTE9}; {FONTE46}","ranking-de-modelos")+"""
Ranking dos modelos de campanha da Convertfy pela amostra ampla (46 lojas), com a amostra de 9 lojas ao lado. Quando as duas discordam, a decisão segue a amostra ampla e o modelo fica marcado. Recalcular todo mês pela view de índice do admin.

| Modelo | 46 lojas | Acima de 1 | 9 lojas | Situação |
|---|---|---|---|---|
""" + "".join(f"| [[{m['key']}]] | {num(m.get('amostra_46',{}).get('mediana'))} | {m.get('amostra_46',{}).get('acima','-')} | {num(m.get('amostra_9',{}).get('mediana'))} | {SL[m['status']]} |\n" for m in ordem) + """
# O que mudou com a amostra ampla (21/09/2026)

| Modelo | 9 lojas | 46 lojas | Decisão |
|---|---|---|---|
| Revele seu desconto | 1,22 | 0,00 (13 de 29) | Rebaixado para reserva. Saiu de 4 datas do Q4 |
| Tema do momento | 1,27 | 0,00 (1 de 21) | Reserva. O tema vira ângulo dentro de modelo validado |
| Ligação | 0,91 | 1,17 (15 de 28) | Promovido a titular |
| Reabertura | 1,11 | 1,15 (17 de 28) | Titular |
| Favoritos | top 6 soft | 1,12 (16 de 29) | Titular |
| Agenda D-3 | 1,21 | 0,37 (10 de 28) | Em revisão. Só para VIP e E30 |
| Catálogo fecha mês | 1,13 | 0,79 (18 de 40) | Complemento |
| Convite D-6 | 1,55 | 0,98 (14 de 28) | Titular com ressalva. Spam de 0,26 por mil, o dobro do 18h |

Voltar para [[mapa-do-calendario]]
"""
w("ranking-de-modelos.md", rk)
# regras
pp=R['principio_decisao']
w("principio-80-10-10.md", fm("doutrina","Decisão do Bruno, 21/09/2026","principio-80-10-10")+f"""
Toda decisão de calendário da Convertfy segue a mesma proporção: **pelo menos {pp['validado_min_pct']}% dos envios de um plano usam modelos validados pela carteira**, até {pp['inspiracao_max_pct']}% vêm de inspiração externa que vem dando certo, e o restante complementa o desenvolvimento.

| Categoria | O que é |
|---|---|
| Validado | {pp['definicoes']['validado']} |
| Inspiração | {pp['definicoes']['inspiracao']} |
| Complemento | {pp['definicoes']['complemento']} |

{pp['regra']}

O plano Q4 2026 fecha em {P['composicao'].get('validado')} validado, {P['composicao'].get('inspiracao')} inspiração e {P['composicao'].get('complemento')} complemento.

Ver [[ranking-de-modelos]] · [[mapa-do-calendario]]
""")
sq="".join(f"| D{p['offset']:+d} | {p['hora']} | {('[['+p['modelo']+']]') if p.get('modelo') else p.get('texto','')} | {p.get('publico') if isinstance(p.get('publico'),str) else json.dumps(p.get('publico'),ensure_ascii=False) if p.get('publico') else '-'} | {p.get('condicao','')} |\n" for p in R['sequencia_de_pico']['passos'])
w("sequencia-de-pico.md", fm("especificacao",FONTE9+"; "+FONTE46,"sequencia-de-pico")+"""
O molde de toda data dupla (6.6, 7.7, 10.10, 11.11) e de todo pico de temporada. É a parte mais validada da operação: o 18h com status mudou ficou acima da média em 8 de 9 lojas no 9.9 e em 25 de 33 no 8.8.

| Dia | Hora | E-mail | Público | Condição |
|---|---|---|---|---|
"""+sq+"""
Esquenta de 3 ou 4 e-mails e véspera por e-mail estão fora: ficaram abaixo da média nas duas amostras.

Ver [[segmentacao-e-freios]] · [[mapa-do-calendario]]
""")
cam="".join(f"| {c['key']} | {c['def']} |\n" for c in R['camadas']); niv="".join(f"| {n['key']} | {n['criterio']} | {n.get('lista_toda_por_trimestre',n.get('regra',''))} |\n" for n in R['niveis_conta']); fr="".join(f"| {f['sinal']} | {f['acao']} |\n" for f in R['freios'])
w("segmentacao-e-freios.md", fm("doutrina",FONTE9,"segmentacao-e-freios")+f"""
Segmento pesa mais que o modelo. Na Donaris, engajados de 90 dias renderam R$ 92,5 por mil envios contra R$ 17,5 da lista toda. Na Brinque Mais, R$ 176,0 contra R$ 41,4. No pico da Brinque Mais, engajados fizeram 44 pedidos com 40 mil envios e a lista toda fez 24 com 99 mil.

# Camadas

| Camada | Definição |
|---|---|
{cam}
# Nível da conta

| Nível | Critério | Lista toda no trimestre |
|---|---|---|
{niv}
# Freios

| Sinal | Ação |
|---|---|
{fr}
Métrica de decisão: clique, pedidos e receita por mil envios, e spam. Abertura é sinal auxiliar por causa do Apple Mail.

Ver [[sequencia-de-pico]] · [[mapa-do-calendario]]
""")
w("regras-de-copy-de-campanha.md", fm("doutrina","Estudo Base BFCM 2026, seção 16.9 e Playbook 2.4","regras-de-copy")+"\nRegras que valem para todo e-mail de campanha, vindas dos erros encontrados nos e-mails de 2025 e nas contas analisadas.\n\n"+"".join(f"- {r}\n" for r in R['copy'])+"\n# Checklist antes de agendar\n\n"+"".join(f"- [ ] {c}\n" for c in R['checklist_envio'])+"\nVer [[mapa-do-calendario]]\n")
nm=R['nome_da_campanha']
w("convencao-de-nome-de-campanha.md", fm("especificacao","Padrão das contas Omnisend da Convertfy","nome-de-campanha")+f"""
Toda campanha na Omnisend segue o padrão `{nm['padrao']}`. Exemplo: `{nm['exemplo']}`.

{nm['motivo']}. O admin lê o quarto campo (evento) e liga à nota do modelo pelos aliases de cada modelo em [[ranking-de-modelos]].

Erro já encontrado: campanha com 18:00 no nome agendada para 11h (Brinque Mais, 7.7). O nome e o horário precisam bater.
""")
te="".join(f"| {t['id']} | {t['pergunta']} | {t.get('desenho','')} | {t['metrica']} | {t.get('decisao','')} |\n" for t in R['testes'])
w("testes-q4-2026.md", fm("plano-de-teste","Calendário Q4 2026","testes-q4-2026")+"\n| Teste | Pergunta | Desenho | Métrica | Decisão |\n|---|---|---|---|---|\n"+te+"\nVer [[plano-q4-2026]]\n")
# planos por janela
nomes={"preparacao":"Preparação","outubro":"Outubro","10.10":"10.10","11.11":"11.11","intervalo":"Intervalo 14 a 24/11","bf":"Black Friday","cm":"Cyber Monday","dezembro":"Dezembro"}
jan={}
for e in P['envios']: jan.setdefault(e['janela'],[]).append(e)
def pub(p): return " / ".join(f"{k}: {v}" for k,v in p.items())
links=[]
for j,es in jan.items():
    slug="janela-"+j.replace(".","-")
    links.append(f"- [[{slug}]] ({len(es)} envios)")
    rows="".join(f"| {e['data'][8:]}/{e['data'][5:7]} | {e['hora']} | [[{e['modelo']}]] | {e['estrutura']} | {e['assunto_pt'] or '-'} | {pub(e['publico'])} | {'sim' if e['lista_pequena'] else ''} | {e['evidencia']} | {e['porque'] or e['objetivo']} |\n" for e in es)
    w(f"planos/q4-2026/{slug}.md", fm("plano","Calendário Q4 2026 | Convertfy",slug)+f"\nEnvios da janela {nomes.get(j,j)} no plano [[plano-q4-2026]].\n\n| Data | Hora | Modelo | Estrutura | Assunto | Público | Lista pequena | Evidência | Por quê |\n|---|---|---|---|---|---|---|---|---|\n"+rows)
ca="".join(f"| {c['data'][8:]}/{c['data'][5:7]} | {c['hora']} | {c['canal']} | {c['texto']} |\n" for c in R['canais_q4'])
pz="".join(f"| {x['ate'][8:]}/{x['ate'][5:7]} | {x['o_que']} |\n" for x in R['prazos_producao_q4'])
w("planos/q4-2026/plano-q4-2026.md", fm("plano","Calendário Q4 2026 | Convertfy","plano-q4-2026")+f"""
Plano de outubro a dezembro de 2026: {len(P['envios'])} envios de e-mail por loja, composição {P['composicao'].get('validado')} validado, {P['composicao'].get('inspiracao')} inspiração e {P['composicao'].get('complemento')} complemento ([[principio-80-10-10]]).

Decisões: 10.10 com teste da madrugada; 11.11 é a Black antecipada e o acesso antecipado, com 5 disparos (00h se aprovado, 07h, 11h, 18h, 21h30) e fechamento real às 23h59; sem Early Access separado de 17 a 24/11; BF de quarta 25 a domingo 29/11; Cyber Monday de 30/11 a 03/12 com oferta nova; dezembro com presentes, prazos e vale-presente; datas locais em trilha separada.

# Janelas

"""+"\n".join(links)+"""

# Canais de apoio

| Data | Hora | Canal | Mensagem |
|---|---|---|---|
"""+ca+"""
# Prazos de produção

| Até | O que |
|---|---|
"""+pz+"\nVer [[testes-q4-2026]] · [[sequencia-de-pico]] · [[segmentacao-e-freios]]\n")
lojas=[("Emyerre","Global, USD","25 campanhas, primeira análise, protocolo de coleta"),("Blue Wolf","Global, USD","46 campanhas, 742 mil envios, 389 pedidos, US$ 43,58 por mil. Fonte das peças de referência"),("Clube Rock","Brasil, BRL","55 campanhas, 2,5 mi envios, 1.950 pedidos, R$ 112,80 por mil. Texto das 7h com o Henrique"),("Azzurro Milano","Europa, EUR","57 campanhas, 194 pedidos, € 39,14 por mil"),("Feratto","Reino Unido, GBP","57 campanhas, 282 pedidos, £ 56,24 por mil"),("LensEVO","Reino Unido, GBP","57 campanhas, 103 pedidos, £ 22,53 por mil"),("Vorttexia","França, EUR","63 campanhas, 995 mil envios, € 7,42 por mil. Fadiga de frequência"),("Donaris","Brasil, BRL","62 campanhas, R$ 26,07 por mil. Teste de segmento: engajados 5,3x"),("Moisfine","Global, USD","65 campanhas, lista de 2 mil, US$ 103,66 por mil. Regra da lista pequena"),("Brinque Mais","Brasil, BRL","63 campanhas, 427 pedidos, R$ 54,28 por mil. Segmento em 3 fases e erro de horário")]
w("lojas-analisadas.md", fm("indice",FONTE9,"lojas-analisadas")+"\nAs 10 lojas analisadas a fundo no estudo base. Detalhe completo no Estudo Base BFCM 2026 (seções 17 a 32).\n\n| Loja | Mercado | Resumo |\n|---|---|---|\n"+"".join(f"| {a} | {b} | {c} |\n" for a,b,c in lojas))
w("fontes-do-estudo.md", fm("indice","Estudo Base BFCM 2026","fontes")+"""
| Fonte | Peso | Onde |
|---|---|---|
| Carteira, 46 lojas | Maior | omnisend_campaign_metrics, view de índice do admin |
| Carteira, 9 lojas a fundo | Maior | Estudo Base BFCM 2026, seções 17 a 32; base_campanhas_convertfy.csv |
| 11.11 de 2025 | Alto no 11.11 | Estudo Base, seções 15 e 16 |
| Wellcopy e Max | Médio, só onde a carteira não tem dado | Advisors/Max no vault; Estudo Base, seções 3 a 9 |
| Trendtrack | Apoio | Estudo Base, seção 10 |

Documentos: Estudo Base (https://claude.ai/code/artifact/e3da050a-9dbb-42dc-9b30-987f7cf02ad7), Playbook (https://claude.ai/code/artifact/7f25e035-cf35-4336-858b-a2cd0fdadc91), Calendário Q4 (https://claude.ai/code/artifact/d2398783-1e9c-4de4-b580-b98d5826f0d2).
""")
w("mapa-do-calendario.md", fm("indice","Convertfy","mapa-do-calendario")+"""
Porta de entrada do planejamento de campanhas da Convertfy: como o calendário mensal é montado, quais e-mails entram, para quem e por quê. Vale para todo mês, e o Q4 2026 é o primeiro plano completo.

# Como decidir

- [[principio-80-10-10]]: pelo menos 80% validado pela carteira
- [[ranking-de-modelos]]: o índice de cada modelo em 46 lojas e em 9
- [[sequencia-de-pico]]: o molde de toda data dupla e de todo pico
- [[segmentacao-e-freios]]: quem recebe cada envio e quando parar
- [[regras-de-copy-de-campanha]]: o que nunca pode sair num e-mail
- [[convencao-de-nome-de-campanha]]: a chave que liga Omnisend, admin e vault

# Planos

- [[plano-q4-2026]] e [[testes-q4-2026]]

# Contexto

- [[lojas-analisadas]] · [[fontes-do-estudo]]
""")
print(sum(len(f) for _,_,f in os.walk("obsidian")))
