#!/usr/bin/env python3
"""Toledo Digital — Ordem de Serviço Nº 001 — Família Song"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
import datetime

OUTPUT = "/data/.openclaw/workspace/propostas/OS-001-ToledoDigital-Song.pdf"
W, H = A4
MARGEM = 2.2 * cm
AZUL = colors.HexColor('#1a2e4a')
AZUL_CLARO = colors.HexColor('#4a6fa5')
CINZA = colors.HexColor('#f5f7fa')
CINZA2 = colors.HexColor('#e8edf2')
DOURADO = colors.HexColor('#c8960c')

def s():
    base = getSampleStyleSheet()
    st = {}
    st['titulo'] = ParagraphStyle('titulo', fontSize=18, textColor=colors.white,
        fontName='Helvetica-Bold', alignment=TA_CENTER)
    st['sub'] = ParagraphStyle('sub', fontSize=10, textColor=AZUL_CLARO,
        fontName='Helvetica', alignment=TA_CENTER, spaceAfter=4)
    st['secao'] = ParagraphStyle('secao', fontSize=11, textColor=AZUL,
        fontName='Helvetica-Bold', spaceBefore=12, spaceAfter=5)
    st['corpo'] = ParagraphStyle('corpo', fontSize=9.5, textColor=colors.HexColor('#222'),
        leading=15, spaceAfter=5, alignment=TA_JUSTIFY, fontName='Helvetica')
    st['bold'] = ParagraphStyle('bold', parent=st['corpo'], fontName='Helvetica-Bold')
    st['centro'] = ParagraphStyle('centro', parent=st['corpo'], alignment=TA_CENTER)
    st['rodape'] = ParagraphStyle('rodape', fontSize=7.5, textColor=colors.grey,
        alignment=TA_CENTER, fontName='Helvetica')
    st['campo'] = ParagraphStyle('campo', fontSize=9, textColor=colors.HexColor('#444'),
        fontName='Helvetica', leading=14)
    st['aviso'] = ParagraphStyle('aviso', fontSize=9, textColor=DOURADO,
        fontName='Helvetica-Bold', alignment=TA_CENTER)
    return st

def hr(cor=AZUL):
    return HRFlowable(width='100%', thickness=1, color=cor, spaceAfter=6, spaceBefore=4)

def tab(dados, cols, cab_cor=AZUL, zebra=True):
    t = Table(dados, colWidths=cols)
    est = [
        ('BACKGROUND', (0,0), (-1,0), cab_cor),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#c0c8d0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
    ]
    if zebra:
        for i in range(1, len(dados)):
            if i % 2 == 0:
                est.append(('BACKGROUND', (0,i), (-1,i), CINZA))
    t.setStyle(TableStyle(est))
    return t

def num_pag(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawString(MARGEM, 1.1*cm,
        "Toledo Digital · Luís Toledo · +351 931 120 429 · toledothelast@gmail.com")
    canvas.drawRightString(W - MARGEM, 1.1*cm, f"OS Nº 001 · Página {doc.page}")
    canvas.restoreState()

def gerar():
    st = s()
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
        leftMargin=MARGEM, rightMargin=MARGEM,
        topMargin=2*cm, bottomMargin=2*cm,
        title="OS-001 Toledo Digital — Família Song")

    story = []

    # ── CABEÇALHO ──
    cab = Table([
        [Paragraph("TOLEDO DIGITAL", st['titulo'])],
        [Paragraph("ORDEM DE SERVIÇO Nº 001", ParagraphStyle('os',
            fontSize=13, textColor=DOURADO, fontName='Helvetica-Bold', alignment=TA_CENTER))],
        [Paragraph("Desenvolvimento Web & Aplicações Digitais", st['sub'])],
    ], colWidths=[W - 2*MARGEM])
    cab.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(cab)
    story.append(Spacer(1, 10))

    # Data + estado
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    info = [['Data de abertura', hoje, 'Estado', 'EM CURSO — A INICIAR'],
            ['Responsável', 'Luís Augusto Soares de Toledo', 'Referência', 'OS-001-SONG-2026']]
    ti = Table(info, colWidths=[3.5*cm, 7*cm, 2.5*cm, 3*cm])
    ti.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('BACKGROUND', (0,0), (-1,-1), CINZA),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#c0c8d0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('BACKGROUND', (3,0), (3,0), colors.HexColor('#e8f5e9')),
        ('TEXTCOLOR', (3,0), (3,0), colors.HexColor('#1B4332')),
        ('FONTNAME', (3,0), (3,0), 'Helvetica-Bold'),
    ]))
    story.append(ti)
    story.append(Spacer(1, 10))

    # ── PARTES ──
    story.append(Paragraph("1. IDENTIFICAÇÃO DAS PARTES", st['secao']))
    partes = [
        ['', 'PRESTADOR DE SERVIÇOS', 'CLIENTE'],
        ['Nome', 'Luís Augusto Soares de Toledo\nToledo Digital', 'Jiaxin Song\n(Filha do Sr. Song)'],
        ['NIF', '_________________', '_________________'],
        ['Morada', 'Leça da Palmeira, Porto, Portugal', '_________________________________'],
        ['Telefone', '+351 931 120 429', '+351 966 599 195'],
        ['Email', 'toledothelast@gmail.com', 'jiaxinsong327@gmail.com'],
        ['Função', 'Desenvolvedor / Gestor de Projeto', 'Cliente — Decisora'],
    ]
    story.append(tab(partes, [3*cm, 8*cm, 5*cm]))
    story.append(Spacer(1, 8))

    # ── PROJETOS ──
    story.append(Paragraph("2. PROJETOS CONTRATADOS", st['secao']))

    # Projeto A
    pA = Table([[Paragraph("PROJETO A — App de Pedidos QR Code · Mar de Prata 🍽️",
        ParagraphStyle('pA', fontSize=10, textColor=colors.white, fontName='Helvetica-Bold'))],],
        colWidths=[W - 2*MARGEM])
    pA.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),AZUL_CLARO),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),10)]))
    story.append(pA)

    dadosA = [
        ['Campo', 'Detalhe'],
        ['Descrição', 'Sistema de pedidos por QR Code nas mesas → pedido chega em tempo real à cozinha'],
        ['Inclui', '• QR Code por mesa (sem instalar app)\n• Menu digital com categorias e preços\n• 14 alergénios por prato (obrigatório por lei)\n• Painel da cozinha em tempo real\n• Histórico e estatísticas de pedidos\n• SSL/HTTPS + conformidade RGPD\n• Painel admin para gestão de menu'],
        ['Prazo estimado', '15 a 20 dias úteis após briefing e entrega de conteúdos'],
        ['Valor acordado', '€450 — pago integralmente na entrega'],
        ['Pagamento', 'Em numerário, no momento da entrega e validação'],
        ['Infra (cliente)', 'Domínio ~€10/ano + VPS ~€6-12/mês — conta Hostinger do cliente'],
        ['Domínio pretendido', '_________________________________'],
        ['Nº de mesas', '_________________________________'],
        ['Painel cozinha em', '☐ Tablet  ☐ TV  ☐ PC fixo  ☐ Telemóvel'],
        ['Estado', '✅ Proposta aceite — aguarda briefing e conteúdos'],
    ]
    story.append(tab(dadosA, [4*cm, 12*cm]))
    story.append(Spacer(1, 10))

    # Projeto B
    pB = Table([[Paragraph("PROJETO B — Website Gabinete de Contabilidade 👩‍💼",
        ParagraphStyle('pB', fontSize=10, textColor=colors.white, fontName='Helvetica-Bold'))],],
        colWidths=[W - 2*MARGEM])
    pB.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),AZUL),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),10)]))
    story.append(pB)

    dadosB = [
        ['Campo', 'Detalhe'],
        ['Descrição', 'Website profissional bilingue (Português + 中文) com presença digital completa'],
        ['Inclui', '• Site PT + 中文: serviços, sobre, equipa, contacto\n• SEO local — "contabilista [zona]", "gabinete contabilístico"\n• Google Meu Negócio — no mapa, avaliações, contacto directo\n• WeChat integrado (QR Code de contacto)\n• Formulário de marcação de consulta\n• SSL/HTTPS + conformidade RGPD\n• Painel admin para edição autónoma\n• 12 meses de suporte incluídos'],
        ['Referências visuais', 'agendapadrao.com · teru.pt'],
        ['Prazo estimado', '18 a 22 dias úteis após briefing e entrega de conteúdos'],
        ['Valor acordado', '€600 — pago integralmente na entrega (em numerário)'],
        ['Pagamento', 'Em numerário, no momento da entrega e validação'],
        ['Infra (cliente)', 'Domínio ~€10/ano + VPS ~€6-12/mês — conta Hostinger do cliente'],
        ['Nome do gabinete', '_________________________________'],
        ['Nome em chinês', '_________________________________'],
        ['Domínio pretendido', '_________________________________'],
        ['WeChat profissional', '☐ Sim (ID: ______________________)  ☐ Não'],
        ['Estado', '✅ Proposta aceite — aguarda briefing e conteúdos'],
    ]
    story.append(tab(dadosB, [4*cm, 12*cm]))
    story.append(Spacer(1, 10))

    # ── RESUMO FINANCEIRO ──
    story.append(Paragraph("3. RESUMO FINANCEIRO", st['secao']))
    fin = [
        ['Projeto', 'Valor', 'Pagamento', 'Estado'],
        ['App QR Mar de Prata', '€450', 'Na entrega · Numerário', '⏳ Aguarda entrega'],
        ['Website Gabinete Contabilidade', '€600', 'Na entrega · Numerário', '⏳ Aguarda entrega'],
        ['TOTAL', '€1.050', '—', '—'],
    ]
    tf = Table(fin, colWidths=[7*cm, 2.5*cm, 4.5*cm, 3*cm])
    tf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), AZUL),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#e8f5e9')),
        ('TEXTCOLOR', (0,-1), (-1,-1), colors.HexColor('#1B4332')),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#c0c8d0')),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, CINZA]),
    ]))
    story.append(tf)
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "⚠️  Nota: Os custos de infraestrutura (domínio e servidor VPS Hostinger) são da "
        "responsabilidade do Cliente e pagos diretamente à Hostinger. Ficam em nome do Cliente.",
        st['campo']))

    # ── FASES DO PROJETO ──
    story.append(PageBreak())
    story.append(Paragraph("4. FASES DO PROJETO — DA VISÃO À ENTREGA", st['secao']))
    fases = [
        ['Fase', 'Nome', 'Descrição', 'Prazo'],
        ['0', 'Briefing', 'Reunião para recolher: logo, cores, textos, fotos, NIF, domínio, nº mesas', '1 sessão (~30 min)'],
        ['1', 'Setup de Infra', 'Cliente cria conta Hostinger. Prestador configura VPS, domínio e SSL.', 'Dias 1–2'],
        ['2', 'Desenvolvimento', 'Backend, base de dados, frontend, funcionalidades acordadas.', 'Dias 3–14'],
        ['3', '1ª Revisão', '1º protótipo enviado. Cliente valida em até 5 dias úteis e lista ajustes.', 'Dias 15–17'],
        ['4', 'Ajustes e conteúdo', 'Integração de fotos e textos reais. Aplicação das revisões.', 'Dias 18–20'],
        ['5', '2ª Revisão final', 'Validação final. Máx. 2 rondas incluídas. Extras são orçamentados.', 'Dias 21–22'],
        ['6', 'Testes', 'Testes em mobile, tablet e desktop. RGPD, formulários, funcionalidades.', 'Dias 23–24'],
        ['7', 'Entrega', 'Deploy, formação de utilização (30 min), entrega de credenciais, pagamento.', 'Dia 25'],
    ]
    story.append(tab(fases, [1*cm, 2.5*cm, 10.5*cm, 3*cm]))
    story.append(Spacer(1, 8))

    # ── O QUE PRECISO DO CLIENTE ──
    story.append(Paragraph("5. CONTEÚDOS NECESSÁRIOS DO CLIENTE", st['secao']))
    story.append(Paragraph(
        "Por favor, vá reunindo os seguintes elementos. Pode enviar por WhatsApp ou email "
        "à medida que tiver disponível — não precisa de tudo de uma vez.", st['corpo']))

    cont = [
        ['#', 'Item', 'Projeto', 'Formato', 'Estado'],
        ['1', 'Logótipo do gabinete', 'Gabinete', 'PNG ou SVG, fundo transparente', '☐'],
        ['2', 'Nome do gabinete (PT + 中文)', 'Gabinete', 'Texto', '☐'],
        ['3', 'NIF do gabinete', 'Gabinete', 'Texto', '☐'],
        ['4', 'Morada e horário de atendimento', 'Gabinete', 'Texto', '☐'],
        ['5', 'Foto profissional (sua ou da equipa)', 'Gabinete', 'JPG/PNG mín. 1MB', '☐'],
        ['6', 'WeChat profissional (QR ou ID)', 'Gabinete', 'Imagem/texto', '☐'],
        ['7', 'Serviços a destacar no site', 'Gabinete', 'Lista', '☐'],
        ['8', 'Domínio pretendido (gabinete)', 'Gabinete', 'Ex: seugabinete.pt', '☐'],
        ['9', 'Logótipo do restaurante Mar de Prata', 'Mar de Prata', 'PNG ou SVG', '☐'],
        ['10', 'Nome legal + NIF do restaurante', 'Mar de Prata', 'Texto', '☐'],
        ['11', 'Morada e horários do restaurante', 'Mar de Prata', 'Texto', '☐'],
        ['12', 'Menu completo (pratos, preços, categorias)', 'Mar de Prata', 'Excel/Word/PDF', '☐'],
        ['13', 'Alergénios por prato (tabela)', 'Mar de Prata', 'Tabela (envio modelo)', '☐'],
        ['14', 'Fotos do espaço e dos pratos (mín. 10)', 'Mar de Prata', 'JPG/PNG mín. 1MB', '☐'],
        ['15', 'Nº de mesas e onde fica o painel da cozinha', 'Mar de Prata', 'Texto', '☐'],
        ['16', 'Domínio pretendido (restaurante)', 'Mar de Prata', 'Ex: mardeprata.pt', '☐'],
        ['17', 'Conta Hostinger criada (ambos)', 'Ambos', 'Credenciais partilhadas', '☐'],
    ]
    story.append(tab(cont, [0.7*cm, 6*cm, 2.5*cm, 4.5*cm, 1.5*cm]))
    story.append(Spacer(1, 8))

    # ── O QUE ESTÁ FORA DO ÂMBITO ──
    story.append(Paragraph("6. O QUE ESTÁ FORA DO ÂMBITO DESTE CONTRATO", st['secao']))
    fora = [
        "✗  Falhas ou manutenção do servidor Hostinger (responsabilidade da Hostinger/cliente)",
        "✗  Renovação anual do domínio (responsabilidade do cliente)",
        "✗  Novas funcionalidades não acordadas nesta OS (orçamentadas à parte)",
        "✗  Alterações ao código feitas pelo cliente ou terceiros após a entrega",
        "✗  Estratégia de marketing ou redes sociais (salvo contrato adicional)",
        "✗  Fotografias profissionais ou design de logótipo (cliente fornece os ficheiros)",
        "✗  Posicionamento no Google — o SEO demora 3 a 6 meses de resultados orgânicos",
        "✗  Tradução de conteúdos — cliente valida as traduções para mandarim",
    ]
    for f in fora:
        story.append(Paragraph(f, ParagraphStyle('fora', parent=st['corpo'], leftIndent=10)))
    story.append(Spacer(1, 10))

    # ── ASSINATURAS ──
    story.append(hr())
    story.append(Paragraph(
        "Ambas as partes declaram ter lido e concordado com os termos desta Ordem de Serviço.",
        st['centro']))
    story.append(Spacer(1, 20))

    assin = [
        [Paragraph('PRESTADOR DE SERVIÇOS', st['centro']),
         Paragraph('CLIENTE', st['centro'])],
        [Paragraph('Luís Augusto Soares de Toledo\nToledo Digital', st['centro']),
         Paragraph('Jiaxin Song', st['centro'])],
        ['', ''],
        [Paragraph('_________________________________', st['centro']),
         Paragraph('_________________________________', st['centro'])],
        [Paragraph(f'Data: _____ / _____ / {datetime.date.today().year}', st['centro']),
         Paragraph(f'Data: _____ / _____ / {datetime.date.today().year}', st['centro'])],
    ]
    ta = Table(assin, colWidths=[(W-2*MARGEM)/2]*2)
    ta.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(ta)

    doc.build(story, onFirstPage=num_pag, onLaterPages=num_pag)
    print(f"✅ PDF gerado: {OUTPUT}")

if __name__ == '__main__':
    gerar()
