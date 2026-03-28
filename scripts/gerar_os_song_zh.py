#!/usr/bin/env python3
"""Toledo Digital — 服务单 Nº 001 — Song 家族 (中文版)"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import datetime

OUTPUT = "/data/.openclaw/workspace/propostas/OS-001-ToledoDigital-Song-ZH.pdf"
W, H = A4
MARGEM = 2.2 * cm
AZUL = colors.HexColor('#1a2e4a')
AZUL_CLARO = colors.HexColor('#4a6fa5')
CINZA = colors.HexColor('#f5f7fa')
DOURADO = colors.HexColor('#c8960c')

# Registar fonte CID para suporte a caracteres chineses
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
FONTE_ZH = 'STSong-Light'

def s():
    st = {}
    st['titulo'] = ParagraphStyle('titulo', fontSize=18, textColor=colors.white,
        fontName=FONTE_ZH, alignment=TA_CENTER)
    st['sub'] = ParagraphStyle('sub', fontSize=10, textColor=AZUL_CLARO,
        fontName=FONTE_ZH, alignment=TA_CENTER, spaceAfter=4)
    st['secao'] = ParagraphStyle('secao', fontSize=11, textColor=AZUL,
        fontName=FONTE_ZH, spaceBefore=12, spaceAfter=5)
    st['corpo'] = ParagraphStyle('corpo', fontSize=9.5, textColor=colors.HexColor('#222'),
        leading=16, spaceAfter=5, alignment=TA_JUSTIFY, fontName=FONTE_ZH)
    st['bold'] = ParagraphStyle('bold', parent=st['corpo'], fontName=FONTE_ZH)
    st['centro'] = ParagraphStyle('centro', parent=st['corpo'], alignment=TA_CENTER)
    st['rodape'] = ParagraphStyle('rodape', fontSize=7.5, textColor=colors.grey,
        alignment=TA_CENTER, fontName=FONTE_ZH)
    st['campo'] = ParagraphStyle('campo', fontSize=9, textColor=colors.HexColor('#444'),
        fontName=FONTE_ZH, leading=14)
    return st

def hr():
    return HRFlowable(width='100%', thickness=1, color=AZUL, spaceAfter=6, spaceBefore=4)

def tab(dados, cols, cab_cor=AZUL, zebra=True):
    t = Table(dados, colWidths=cols)
    est = [
        ('BACKGROUND', (0,0), (-1,0), cab_cor),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,-1), FONTE_ZH),
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
    canvas.setFont(FONTE_ZH, 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawString(MARGEM, 1.1*cm,
        "Toledo Digital · Luís Toledo · +351 931 120 429 · toledothelast@gmail.com")
    canvas.drawRightString(W - MARGEM, 1.1*cm, f"服务单 Nº 001 · 第 {doc.page} 页")
    canvas.restoreState()

def gerar():
    st = s()
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
        leftMargin=MARGEM, rightMargin=MARGEM,
        topMargin=2*cm, bottomMargin=2*cm,
        title="服务单 OS-001 Toledo Digital — Song 家族")

    story = []
    hoje = datetime.date.today().strftime("%Y年%m月%d日")

    # ── 页眉 ──
    cab = Table([
        [Paragraph("TOLEDO DIGITAL", st['titulo'])],
        [Paragraph("服务单 Nº 001", ParagraphStyle('os',
            fontSize=13, textColor=DOURADO, fontName=FONTE_ZH, alignment=TA_CENTER))],
        [Paragraph("网站开发 & 数字应用服务", st['sub'])],
    ], colWidths=[W - 2*MARGEM])
    cab.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(cab)
    story.append(Spacer(1, 10))

    info = [['开单日期', hoje, '状态', '进行中 — 待启动'],
            ['负责人', 'Luís Augusto Soares de Toledo', '参考编号', 'OS-001-SONG-2026']]
    ti = Table(info, colWidths=[3.5*cm, 7*cm, 2.5*cm, 3*cm])
    ti.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), FONTE_ZH),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('BACKGROUND', (0,0), (-1,-1), CINZA),
        ('FONTNAME', (0,0), (0,-1), FONTE_ZH),
        ('FONTNAME', (2,0), (2,-1), FONTE_ZH),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#c0c8d0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('BACKGROUND', (3,0), (3,0), colors.HexColor('#e8f5e9')),
        ('TEXTCOLOR', (3,0), (3,0), colors.HexColor('#1B4332')),
    ]))
    story.append(ti)
    story.append(Spacer(1, 10))

    # ── 1. 双方信息 ──
    story.append(Paragraph("1. 双方信息", st['secao']))
    partes = [
        ['', '服务提供方', '客户'],
        ['姓名', 'Luís Augusto Soares de Toledo\nToledo Digital', 'Song 小姐 (Song 先生之女)'],
        ['税号 (NIF)', '_________________', '_________________'],
        ['地址', 'Leça da Palmeira, Porto, 葡萄牙', '_________________________________'],
        ['电话', '+351 931 120 429', '+351 966 599 195'],
        ['电子邮件', 'toledothelast@gmail.com', 'jiaxinsong327@gmail.com'],
        ['身份', '开发者 / 项目经理', '客户 — 决策人'],
    ]
    story.append(tab(partes, [3*cm, 8*cm, 5*cm]))
    story.append(Spacer(1, 8))

    # ── 2. 项目内容 ──
    story.append(Paragraph("2. 合同项目", st['secao']))

    # 项目 A
    pA = Table([[Paragraph("项目 A — 二维码点餐系统 · Mar de Prata 餐厅 🍽️  🎁 免费赠送",
        ParagraphStyle('pA', fontSize=10, textColor=colors.white, fontName=FONTE_ZH))],],
        colWidths=[W - 2*MARGEM])
    pA.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#2D6A4F')),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),10)]))
    story.append(pA)

    dadosA = [
        ['项目', '详情'],
        ['说明', '餐桌二维码点餐系统 → 订单实时传送至厨房，无需安装 App'],
        ['包含内容', '• 每桌二维码（顾客用手机扫码即可）\n• 含分类和价格的数字菜单\n• 每道菜14种过敏原标注（葡萄牙法律要求）\n• 厨房实时订单看板\n• 订单历史记录与统计\n• SSL/HTTPS + RGPD 合规\n• 菜单管理后台'],
        ['预计工期', '简报会议及资料提交后 15 至 20 个工作日'],
        ['费用', '🎁 免费赠送 — 随会计事务所网站项目一并交付'],
        ['付款方式', '无需付款，作为礼物赠送'],
        ['客户基础设施', '域名约 €10/年 + VPS 约 €6-12/月（客户自行在 Hostinger 购买）'],
        ['期望域名', '_________________________________'],
        ['餐桌数量', '_________________________________'],
        ['厨房看板位置', '☐ 平板电脑  ☐ 电视  ☐ 台式电脑  ☐ 手机'],
        ['状态', '✅ 提案已接受 — 待简报会议'],
    ]
    story.append(tab(dadosA, [4*cm, 12*cm]))
    story.append(Spacer(1, 10))

    # 项目 B
    pB = Table([[Paragraph("项目 B — 会计事务所网站 👩‍💼",
        ParagraphStyle('pB', fontSize=10, textColor=colors.white, fontName=FONTE_ZH))],],
        colWidths=[W - 2*MARGEM])
    pB.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),AZUL),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),10)]))
    story.append(pB)

    dadosB = [
        ['项目', '详情'],
        ['说明', '葡中双语专业网站，提供完整数字化形象'],
        ['包含内容', '• 葡萄牙语 + 中文双语网站：服务、关于、团队、联系\n• 本地 SEO — "会计师[地区]"等关键词优化\n• Google My Business — 地图展示、评价、直接联系\n• 微信联系集成（专业微信二维码）\n• 预约咨询表单\n• SSL/HTTPS + RGPD 合规\n• 自主编辑管理后台\n• 12 个月技术支持'],
        ['参考网站', 'agendapadrao.com · teru.pt'],
        ['预计工期', '简报会议及资料提交后 18 至 22 个工作日'],
        ['费用', '€600 — 交付验收后付款'],
        ['付款方式', '现金，交付时付款'],
        ['客户基础设施', '域名约 €10/年 + VPS 约 €6-12/月（客户自行在 Hostinger 购买）'],
        ['事务所名称', '_________________________________'],
        ['中文名称', '_________________________________'],
        ['期望域名', '_________________________________'],
        ['专业微信', '☐ 有（微信号：____________________）  ☐ 没有'],
        ['状态', '✅ 提案已接受 — 待简报会议'],
    ]
    story.append(tab(dadosB, [4*cm, 12*cm]))
    story.append(Spacer(1, 10))

    # ── 3. 费用汇总 ──
    story.append(Paragraph("3. 费用汇总", st['secao']))

    # Nota introdutória
    story.append(Paragraph(
        "以下为本服务单的正式报价记录，包含各项目市场价格及最终成交价格。"
        "由于服务提供方与 Song 先生（Mar de Prata 餐厅负责人）相识多年，基于长期友好关系，"
        "特别给予优惠价格，作为对老朋友的诚意与支持。",
        st['corpo']))
    story.append(Spacer(1, 6))

    fin = [
        ['项目', '市场正常价格', '朋友优惠价', '付款方式', '状态'],
        ['二维码点餐系统\n(Mar de Prata 餐厅)', '€450', '🎁 免费赠送', '—', '⏳ 待交付'],
        ['会计事务所网站\n(葡中双语)', '€650', '€600', '现金 · 交付时付款', '⏳ 待交付'],
        ['正常价格合计', '€1.100', '—', '—', '—'],
        ['实际成交价格', '—', '€600', '现金 · 交付时付款', '—'],
        ['客户节省金额', '—', '€500 (45%)', '—', '—'],
    ]
    tf = Table(fin, colWidths=[4.5*cm, 3*cm, 3*cm, 3.5*cm, 2*cm])
    tf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), AZUL),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,-1), FONTE_ZH),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#c0c8d0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, CINZA]),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor('#e8f5e9')),
        ('TEXTCOLOR', (0,4), (-1,4), colors.HexColor('#1B4332')),
        ('FONTNAME', (0,4), (-1,4), FONTE_ZH),
        ('BACKGROUND', (0,5), (-1,5), colors.HexColor('#fff8e1')),
        ('TEXTCOLOR', (0,5), (-1,5), colors.HexColor('#7B5800')),
    ]))
    story.append(tf)
    story.append(Spacer(1, 8))

    # Caixa de destaque — razão do desconto
    desc_box = Table([[Paragraph(
        "🤝  友情说明\n\n"
        "Toledo Digital 与 Song 先生相识已久，彼此建立了深厚的信任与友谊。"
        "本次报价充分体现了这份情谊：餐厅二维码系统免费赠送，"
        "会计事务所网站以友情价交付。\n\n"
        "本服务单中记录的市场价格仅作为正式文件登记之用，"
        "实际收费以双方口头约定的友情价为准（€600，交付时以现金支付）。",
        ParagraphStyle('desc', fontSize=9, fontName=FONTE_ZH, leading=15,
            textColor=colors.HexColor('#1a2e4a')))
    ]], colWidths=[W - 2*MARGEM])
    desc_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1, AZUL_CLARO),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ]))
    story.append(desc_box)
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "⚠️  注意：域名和服务器（VPS Hostinger）费用由客户承担，直接向 Hostinger 支付，归客户所有。",
        st['campo']))

    # ── 4. 项目阶段 ──
    story.append(PageBreak())
    story.append(Paragraph("4. 项目阶段 — 从构想到交付", st['secao']))
    fases = [
        ['阶段', '名称', '说明', '时间'],
        ['0', '简报会议', '收集：标志、颜色、文案、照片、税号、域名、餐桌数量等', '1次会议（约30分钟）'],
        ['1', '基础设施搭建', '客户创建 Hostinger 账户，服务方配置 VPS、域名和 SSL', '第1-2天'],
        ['2', '开发阶段', '后端、数据库、前端及约定功能开发', '第3-14天'],
        ['3', '第一轮审核', '发送初版给客户，客户在5个工作日内反馈修改意见', '第15-17天'],
        ['4', '调整与内容整合', '整合真实照片和文案，应用修改意见', '第18-20天'],
        ['5', '最终审核', '最终确认。最多2轮修改，额外修改另行报价', '第21-22天'],
        ['6', '测试', '手机、平板、电脑测试，RGPD合规，表单功能验证', '第23-24天'],
        ['7', '交付', '部署上线，操作培训（30分钟），移交所有账户权限，收款', '第25天'],
    ]
    story.append(tab(fases, [1*cm, 2.5*cm, 9.5*cm, 3*cm]))
    story.append(Spacer(1, 8))

    # ── 5. 客户需提供的资料 ──
    story.append(Paragraph("5. 客户需提供的资料清单", st['secao']))
    story.append(Paragraph(
        "请逐步准备以下资料，可通过 WhatsApp 或电子邮件发送，无需一次性全部提供。",
        st['corpo']))

    cont = [
        ['#', '资料', '项目', '格式', '状态'],
        ['1', '事务所标志', '会计网站', 'PNG 或 SVG，透明背景', '☐'],
        ['2', '事务所名称（葡文 + 中文）', '会计网站', '文字', '☐'],
        ['3', '事务所税号 (NIF)', '会计网站', '文字', '☐'],
        ['4', '办公地址及接待时间', '会计网站', '文字', '☐'],
        ['5', '专业照片（本人或团队）', '会计网站', 'JPG/PNG 最小1MB', '☐'],
        ['6', '专业微信（二维码或微信号）', '会计网站', '图片/文字', '☐'],
        ['7', '网站重点推广的服务列表', '会计网站', '列表', '☐'],
        ['8', '期望域名（会计网站）', '会计网站', '例：seugabinete.pt', '☐'],
        ['9', 'Mar de Prata 餐厅标志', 'QR点餐', 'PNG 或 SVG', '☐'],
        ['10', '餐厅全称 + 税号', 'QR点餐', '文字', '☐'],
        ['11', '餐厅地址及营业时间', 'QR点餐', '文字', '☐'],
        ['12', '完整菜单（菜名、价格、分类）', 'QR点餐', 'Excel/Word/PDF', '☐'],
        ['13', '每道菜过敏原信息表', 'QR点餐', '表格（可提供模板）', '☐'],
        ['14', '餐厅及菜品照片（最少10张）', 'QR点餐', 'JPG/PNG 最小1MB', '☐'],
        ['15', '餐桌数量及厨房看板位置', 'QR点餐', '文字', '☐'],
        ['16', '期望域名（餐厅）', 'QR点餐', '例：mardeprata.pt', '☐'],
        ['17', '创建 Hostinger 账户（双项目）', '双项目', '共享登录信息', '☐'],
    ]
    story.append(tab(cont, [0.7*cm, 5.5*cm, 2.5*cm, 4.5*cm, 1.5*cm]))
    story.append(Spacer(1, 8))

    # ── 6. 服务范围外 ──
    story.append(Paragraph("6. 服务范围之外", st['secao']))
    fora = [
        "✗  Hostinger 服务器故障或维护（由 Hostinger/客户负责）",
        "✗  域名年度续费（由客户负责）",
        "✗  本服务单未约定的新功能（需另行报价）",
        "✗  交付后客户或第三方对代码进行的修改",
        "✗  营销策略或社交媒体管理（需另签合同）",
        "✗  专业摄影或标志设计（由客户提供文件）",
        "✗  Google 排名 — SEO 效果通常需要3至6个月显现",
        "✗  中文内容翻译 — 客户负责审核中文译文",
    ]
    for f in fora:
        story.append(Paragraph(f, ParagraphStyle('fora', parent=st['corpo'], leftIndent=10)))
    story.append(Spacer(1, 10))

    # ── 签字 ──
    story.append(hr())
    story.append(Paragraph("双方声明已阅读并同意本服务单的所有条款。", st['centro']))
    story.append(Spacer(1, 20))

    assin = [
        [Paragraph('服务提供方', st['centro']), Paragraph('客户', st['centro'])],
        [Paragraph('Luís Augusto Soares de Toledo\nToledo Digital', st['centro']),
         Paragraph('Song 小姐', st['centro'])],
        ['', ''],
        [Paragraph('_________________________________', st['centro']),
         Paragraph('_________________________________', st['centro'])],
        [Paragraph(f'日期：_____ / _____ / {datetime.date.today().year}', st['centro']),
         Paragraph(f'日期：_____ / _____ / {datetime.date.today().year}', st['centro'])],
    ]
    ta = Table(assin, colWidths=[(W-2*MARGEM)/2]*2)
    ta.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('FONTNAME', (0,0), (-1,-1), FONTE_ZH),
    ]))
    story.append(ta)

    doc.build(story, onFirstPage=num_pag, onLaterPages=num_pag)
    print(f"✅ PDF gerado: {OUTPUT}")

if __name__ == '__main__':
    gerar()
