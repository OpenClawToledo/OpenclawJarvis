#!/usr/bin/env python3
"""Gera PDF de proposta comercial — Toledo Dev"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import PageBreak
import datetime

OUTPUT = "/data/.openclaw/workspace/projetos/Proposta_ToledoDev_MarDePrata_Gabinete.pdf"

# ── Cores ──────────────────────────────────────────────────────────────────
PINK       = colors.HexColor("#e91e7b")
PINK_LIGHT = colors.HexColor("#fce4f0")
DARK       = colors.HexColor("#1a1a2e")
GRAY       = colors.HexColor("#555555")
GRAY_LIGHT = colors.HexColor("#f5f5f5")
WHITE      = colors.white

# ── Estilos ────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def style(name, **kw):
    s = ParagraphStyle(name, **kw)
    return s

S_TITLE    = style("Title2",    fontSize=22, textColor=DARK,  fontName="Helvetica-Bold",  spaceAfter=4,  leading=26)
S_SUBTITLE = style("Subtitle2", fontSize=11, textColor=PINK,  fontName="Helvetica-Bold",  spaceAfter=2)
S_BODY     = style("Body2",     fontSize=9,  textColor=GRAY,  fontName="Helvetica",       spaceAfter=3,  leading=14)
S_LABEL    = style("Label2",    fontSize=8,  textColor=GRAY,  fontName="Helvetica",       spaceAfter=2)
S_SMALL    = style("Small2",    fontSize=8,  textColor=GRAY,  fontName="Helvetica-Oblique", spaceAfter=2)
S_CENTER   = style("Center2",   fontSize=9,  textColor=WHITE, fontName="Helvetica-Bold",  alignment=TA_CENTER, leading=14)
S_HERO     = style("Hero2",     fontSize=28, textColor=WHITE, fontName="Helvetica-Bold",  alignment=TA_CENTER, leading=34)
S_HERO_SUB = style("HeroSub2",  fontSize=12, textColor=PINK_LIGHT, fontName="Helvetica", alignment=TA_CENTER, leading=18)
S_SECTION  = style("Sec2",      fontSize=13, textColor=WHITE, fontName="Helvetica-Bold",  alignment=TA_LEFT, leading=16)
S_NOTE     = style("Note2",     fontSize=8,  textColor=GRAY,  fontName="Helvetica-Oblique", leading=12, spaceAfter=2)
S_BOLD     = style("Bold2",     fontSize=9,  textColor=DARK,  fontName="Helvetica-Bold",  spaceAfter=2)
S_FOOTER   = style("Footer2",   fontSize=8,  textColor=GRAY,  fontName="Helvetica",       alignment=TA_CENTER)

W, H = A4
DATE = datetime.date.today().strftime("%d/%m/%Y")

# ── Helpers ────────────────────────────────────────────────────────────────
def section_header(text):
    t = Table([[Paragraph(text, S_SECTION)]], colWidths=[W - 4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), PINK),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("ROUNDEDCORNERS", [4,4,4,4]),
    ]))
    return t

def pkg_table(rows, highlight=False):
    col = [W - 4*cm - 3.5*cm, 3.5*cm]
    data = []
    for label, val in rows:
        data.append([Paragraph(label, S_BODY), Paragraph(val, S_BOLD)])
    t = Table(data, colWidths=col)
    bg = PINK_LIGHT if highlight else GRAY_LIGHT
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, bg]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#e0e0e0")),
        ("ALIGN",         (1,0), (1,-1), "RIGHT"),
    ]))
    return t

def price_banner(label, price, desc=""):
    inner = f'<font color="#e91e7b"><b>{price}</b></font>'
    data = [[
        Paragraph(f"<b>{label}</b>", S_BOLD),
        Paragraph(inner, style("P2", fontSize=14, fontName="Helvetica-Bold", alignment=TA_RIGHT, textColor=PINK)),
    ]]
    if desc:
        data.append([Paragraph(desc, S_NOTE), Paragraph("", S_NOTE)])
    t = Table(data, colWidths=[W - 4*cm - 5*cm, 5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), GRAY_LIGHT),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
        ("LINEBELOW",     (0,-1), (-1,-1), 1.5, PINK),
    ]))
    return t

def hr(): return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e0e0e0"), spaceAfter=8, spaceBefore=4)

def sp(n=0.3): return Spacer(1, n*cm)

# ── Cover Page ─────────────────────────────────────────────────────────────
def cover_page():
    elems = []

    # Fundo rosa no topo via tabela
    cover = Table(
        [[Paragraph("Toledo Dev", S_HERO)],
         [Paragraph("Soluções Digitais Profissionais", S_HERO_SUB)],
         [Paragraph(f"Proposta Comercial — {DATE}", S_HERO_SUB)]],
        colWidths=[W - 4*cm]
    )
    cover.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), DARK),
        ("TOPPADDING",    (0,0), (-1,-1), 40),
        ("BOTTOMPADDING", (0,0), (0,0),  8),
        ("BOTTOMPADDING", (0,1), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 20),
        ("RIGHTPADDING",  (0,0), (-1,-1), 20),
        ("BOTTOMPADDING", (0,2), (-1,-1), 40),
    ]))
    elems.append(cover)
    elems.append(sp(1))

    # Destaque: dois projectos
    card = Table([
        [Paragraph("  Restaurante Mar de Prata", S_SUBTITLE),
         Paragraph("  Gabinete de Contabilidade", S_SUBTITLE)],
        [Paragraph("Website + App de Pedidos QR Code", S_BODY),
         Paragraph("Website Bilingue (Mandarim) + Portal de Cliente", S_BODY)],
        [Paragraph("€550 · €850 · €1.300", style("PK", fontSize=11, fontName="Helvetica-Bold", textColor=PINK)),
         Paragraph("€650 · €950", style("PK2", fontSize=11, fontName="Helvetica-Bold", textColor=PINK))],
    ], colWidths=[(W-4*cm)/2, (W-4*cm)/2])
    card.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), PINK_LIGHT),
        ("TOPPADDING",    (0,0), (-1,-1), 12),
        ("BOTTOMPADDING", (0,0), (-1,-1), 12),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#f0a0c8")),
        ("LINEAFTER",     (0,0), (0,-1),  1, PINK),
    ]))
    elems.append(card)
    elems.append(sp(0.5))

    elems.append(Paragraph(
        "Proposta preparada por <b>Luís Augusto Soares de Toledo</b> — todos os pacotes incluem "
        "conformidade RGPD completa, SSL/HTTPS e infra­estrutura a cargo do cliente.",
        S_NOTE))

    elems.append(PageBreak())
    return elems

# ── Projecto 1 — Mar de Prata ───────────────────────────────────────────────
def projeto_restaurante():
    e = []
    e.append(section_header("  PROJECTO 1 — Restaurante Mar de Prata"))
    e.append(sp(0.4))
    e.append(Paragraph(
        "Sistema digital completo para restaurante — não apenas um website, mas uma solução que funciona, "
        "é segura e cumpre todas as obrigações legais em vigor em Portugal.", S_BODY))
    e.append(sp(0.5))

    # Pacote Essencial
    e.append(KeepTogether([
        price_banner("PACOTE ESSENCIAL", "€ 550", "Prazo: 7 a 10 dias úteis"),
        sp(0.2),
        pkg_table([
            ("Website completo: menu, reservas, horários, localização", "v"),
            ("Adaptado a telemóvel, tablet e computador", "v"),
            ("Conformidade RGPD: Privacidade, Cookies, Termos", "v"),
            ("14 Alergénios por prato (obrigatório — Reg. EU 1169/2011)", "v"),
            ("Certificado SSL/HTTPS", "v"),
        ]),
        sp(0.4),
    ]))

    # Pacote Standard
    e.append(KeepTogether([
        price_banner("PACOTE STANDARD", "€ 850", "Prazo: 15 a 20 dias úteis"),
        sp(0.2),
        pkg_table([
            ("Tudo do Pacote Essencial", "v"),
            ("App de pedidos via QR Code por mesa (sem instalar nada)", "v"),
            ("Painel da cozinha em tempo real", "v"),
            ("Histórico e estatísticas de pedidos", "v"),
            ("Preços com IVA e identificação legal conforme Decreto-Lei 24/2014", "v"),
        ], highlight=True),
        sp(0.4),
    ]))

    # Pacote Premium
    e.append(KeepTogether([
        price_banner("PACOTE PREMIUM", "€ 1.300", "Prazo: 25 a 30 dias úteis"),
        sp(0.2),
        pkg_table([
            ("Tudo do Pacote Standard", "v"),
            ("Servidor local — funciona mesmo sem internet", "v"),
            ("Duas bases de dados sincronizadas (local + nuvem)", "v"),
            ("Pedidos chegam à cozinha sem interrupção", "v"),
            ("Recuperação automática quando a ligação é restabelecida", "v"),
            ("Nota: requer Raspberry Pi (~€70) ou PC disponível", "*"),
        ]),
        sp(0.5),
    ]))

    e.append(hr())
    e.append(Paragraph("<b>Conformidade Legal — incluída em todos os pacotes</b>", S_BOLD))
    e.append(Paragraph(
        "Sujeito ao RGPD e Decreto-Lei 24/2014. Incumprimento pode resultar em coimas até "
        "<b>€20 milhões ou 4% do volume de negócios</b>. Política de Privacidade, banner de cookies, "
        "SSL, alergénios e identificação legal incluídos desde o primeiro dia.", S_BODY))

    e.append(sp(0.4))
    e.append(Paragraph("<b>Infra­estrutura — custo do cliente (Hostinger)</b>", S_BOLD))
    infra = Table([
        [Paragraph("Domínio (.pt ou .com)", S_BODY), Paragraph("~€10/ano", S_BOLD)],
        [Paragraph("Servidor VPS", S_BODY),           Paragraph("~€6–12/mês", S_BOLD)],
    ], colWidths=[W-4*cm-3.5*cm, 3.5*cm])
    infra.setStyle(TableStyle([
        ("GRID", (0,0),(-1,-1), 0.3, colors.HexColor("#e0e0e0")),
        ("BACKGROUND", (0,0),(-1,-1), GRAY_LIGHT),
        ("TOPPADDING", (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING", (0,0),(-1,-1), 10),
        ("ALIGN", (1,0),(1,-1), "RIGHT"),
    ]))
    e.append(infra)
    e.append(PageBreak())
    return e

# ── Projecto 2 — Gabinete ──────────────────────────────────────────────────
def projeto_gabinete():
    e = []
    e.append(section_header("  PROJECTO 2 — Gabinete de Contabilidade"))
    e.append(sp(0.4))
    e.append(Paragraph(
        "Website profissional bilingue (Português + (Mandarim)) para gabinete de contabilidade a servir "
        "a comunidade empresarial chinesa em Portugal — um posicionamento com muito pouca concorrência "
        "e grande potencial de diferenciação.", S_BODY))
    e.append(sp(0.5))

    # Pacote Essencial
    e.append(KeepTogether([
        price_banner("PACOTE ESSENCIAL", "€ 650", "Prazo: 10 a 14 dias úteis"),
        sp(0.2),
        pkg_table([
            ("Website profissional em português e mandarim (Mandarim)", "v"),
            ("Serviços: contabilidade, fiscalidade, abertura de empresa, RH, vistos", "v"),
            ("Calendário fiscal integrado", "v"),
            ("Formulário de contacto em português e mandarim", "v"),
            ("Integração com WeChat (QR Code de contacto directo)", "v"),
            ("Conformidade RGPD reforçada — dados fiscais sensíveis", "v"),
            ("SSL/HTTPS incluído", "v"),
        ]),
        sp(0.4),
    ]))

    # Pacote Standard
    e.append(KeepTogether([
        price_banner("PACOTE STANDARD", "€ 950", "Prazo: 18 a 22 dias úteis"),
        sp(0.2),
        pkg_table([
            ("Tudo do Pacote Essencial", "v"),
            ("Portal privado de cliente com login individual", "v"),
            ("Partilha segura de documentos: balancetes, declarações, recibos", "v"),
            ("Notificações de prazos fiscais e obrigações por cliente", "v"),
            ("Histórico de documentos organizado por ano", "v"),
        ], highlight=True),
        sp(0.5),
    ]))

    e.append(hr())
    e.append(Paragraph("<b>Conformidade Legal — incluída em todos os pacotes</b>", S_BOLD))
    e.append(Paragraph(
        "Gabinetes de contabilidade lidam com dados fiscais e financeiros — uma das categorias mais "
        "sensíveis ao abrigo do RGPD. O incumprimento pode resultar em coimas até <b>€20 milhões</b> e "
        "em responsabilidade profissional perante a OCC. Todos os pacotes incluem Política de Privacidade, "
        "Termos e Condições, consentimento de cookies e arquitectura de segurança adequada ao sector.", S_BODY))

    e.append(sp(0.4))
    e.append(Paragraph("<b>Diferencial competitivo — website bilingue</b>", S_BOLD))
    e.append(Paragraph(
        "Há muito poucos gabinetes em Portugal que servem a comunidade empresarial chinesa com "
        "proximidade linguística e cultural. Um website em mandarim transmite confiança imediata "
        "e diferencia o gabinete de forma clara e sustentável.", S_BODY))

    e.append(sp(0.4))
    e.append(Paragraph("<b>Infra­estrutura — custo do cliente (Hostinger)</b>", S_BOLD))
    infra = Table([
        [Paragraph("Domínio (.pt ou .com)", S_BODY), Paragraph("~€10/ano", S_BOLD)],
        [Paragraph("Servidor VPS", S_BODY),           Paragraph("~€6–12/mês", S_BOLD)],
    ], colWidths=[W-4*cm-3.5*cm, 3.5*cm])
    infra.setStyle(TableStyle([
        ("GRID", (0,0),(-1,-1), 0.3, colors.HexColor("#e0e0e0")),
        ("BACKGROUND", (0,0),(-1,-1), GRAY_LIGHT),
        ("TOPPADDING", (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING", (0,0),(-1,-1), 10),
        ("ALIGN", (1,0),(1,-1), "RIGHT"),
    ]))
    e.append(KeepTogether([infra]))
    e.append(sp(0.5))
    return e

# ── Resumo Final ───────────────────────────────────────────────────────────
def resumo():
    e = []
    e.append(section_header("  RESUMO — Ambos os Projectos"))
    e.append(sp(0.5))

    resumo_data = [
        [Paragraph("<b>Projecto</b>", S_BOLD), Paragraph("<b>Pacote</b>", S_BOLD),
         Paragraph("<b>Valor</b>", S_BOLD), Paragraph("<b>Prazo</b>", S_BOLD)],
        [Paragraph("Restaurante Mar de Prata", S_BODY), Paragraph("Essencial", S_BODY),
         Paragraph("€550", S_BOLD), Paragraph("7–10 dias", S_BODY)],
        [Paragraph("Restaurante Mar de Prata", S_BODY), Paragraph("Standard", S_BODY),
         Paragraph("€850", S_BOLD), Paragraph("15–20 dias", S_BODY)],
        [Paragraph("Restaurante Mar de Prata", S_BODY), Paragraph("Premium", S_BODY),
         Paragraph("€1.300", S_BOLD), Paragraph("25–30 dias", S_BODY)],
        [Paragraph("Gabinete de Contabilidade", S_BODY), Paragraph("Essencial", S_BODY),
         Paragraph("€650", S_BOLD), Paragraph("10–14 dias", S_BODY)],
        [Paragraph("Gabinete de Contabilidade", S_BODY), Paragraph("Standard", S_BODY),
         Paragraph("€950", S_BOLD), Paragraph("18–22 dias", S_BODY)],
        [Paragraph("Suporte mensal (qualquer pacote)", S_BODY), Paragraph("—", S_BODY),
         Paragraph("€30/mês", S_BOLD), Paragraph("Contínuo", S_BODY)],
    ]
    cols = [(W-4*cm)*0.38, (W-4*cm)*0.22, (W-4*cm)*0.18, (W-4*cm)*0.22]
    t = Table(resumo_data, colWidths=cols)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  DARK),
        ("TEXTCOLOR",     (0,0), (-1,0),  WHITE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, GRAY_LIGHT]),
        ("GRID",          (0,0),(-1,-1),  0.3, colors.HexColor("#e0e0e0")),
        ("TOPPADDING",    (0,0),(-1,-1),  7),
        ("BOTTOMPADDING", (0,0),(-1,-1),  7),
        ("LEFTPADDING",   (0,0),(-1,-1),  10),
        ("ALIGN",         (2,0),(2,-1),   "RIGHT"),
        ("ALIGN",         (3,0),(3,-1),   "CENTER"),
        ("LINEBELOW",     (0,0),(-1,0),   1, PINK),
    ]))
    e.append(t)
    e.append(sp(0.5))

    e.append(Paragraph(
        "Os dois projectos podem ser desenvolvidos <b>em simultâneo ou por fases</b> — conforme a preferência do cliente. "
        "Os custos de infra­estrutura (domínio e servidor VPS) ficam sempre em nome e propriedade do cliente, "
        "pagos directamente à Hostinger.", S_BODY))

    e.append(sp(0.8))
    e.append(hr())
    e.append(sp(0.3))

    # Footer de contacto
    contact = Table([[
        Paragraph("<b>Luís Augusto Soares de Toledo</b>", S_BOLD),
        Paragraph("+351 931 120 429", S_BODY),
    ]], colWidths=[(W-4*cm)/2, (W-4*cm)/2])
    contact.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), PINK_LIGHT),
        ("TOPPADDING",    (0,0),(-1,-1), 12),
        ("BOTTOMPADDING", (0,0),(-1,-1), 12),
        ("LEFTPADDING",   (0,0),(-1,-1), 14),
        ("ALIGN",         (1,0),(1,-1),  "RIGHT"),
        ("RIGHTPADDING",  (0,0),(-1,-1), 14),
    ]))
    e.append(contact)
    e.append(sp(0.3))
    e.append(Paragraph(f"Proposta válida por 30 dias a contar de {DATE}. Preços sem IVA.", S_NOTE))
    return e

# ── Gerar PDF ──────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm,
    title="Proposta Comercial — Toledo Dev",
    author="Luís Augusto Soares de Toledo",
)

story = []
story += cover_page()
story += projeto_restaurante()
story += projeto_gabinete()
story += resumo()

doc.build(story)
print(f"PDF gerado: {OUTPUT}")
