#!/usr/bin/env python3
"""Toledo Digital — 合同文件 (中文版) — Song 家族"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import datetime

OUTPUT = "/data/.openclaw/workspace/propostas/Toledo_Digital_Contratos_Song_ZH.pdf"
W, H = A4
MARGEM = 2.2 * cm
AZUL = colors.HexColor('#1a2e4a')
AZUL_CLARO = colors.HexColor('#4a6fa5')
CINZA = colors.HexColor('#f5f7fa')
CINZA2 = colors.HexColor('#e8edf2')
DOURADO = colors.HexColor('#c8960c')

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
ZH = 'STSong-Light'

HOJE = datetime.date.today().strftime("%Y年%m月%d日")
ANO = datetime.date.today().year

PRESTADOR = {
    'nome': 'Luís Augusto Soares de Toledo',
    'empresa': 'Toledo Digital',
    'morada': 'Leça da Palmeira, Porto, 葡萄牙',
    'tel': '+351 931 120 429',
    'email': 'toledothelast@gmail.com',
}

def st():
    s = {}
    s['titulo'] = ParagraphStyle('titulo', fontSize=18, textColor=colors.white,
        fontName=ZH, alignment=TA_CENTER)
    s['sub'] = ParagraphStyle('sub', fontSize=10, textColor=DOURADO,
        fontName=ZH, alignment=TA_CENTER, spaceAfter=4)
    s['secao'] = ParagraphStyle('secao', fontSize=11, textColor=AZUL,
        fontName=ZH, spaceBefore=12, spaceAfter=5)
    s['corpo'] = ParagraphStyle('corpo', fontSize=9.5, textColor=colors.HexColor('#222'),
        leading=16, spaceAfter=6, alignment=TA_JUSTIFY, fontName=ZH)
    s['bold'] = ParagraphStyle('bold', parent=s['corpo'], fontName=ZH)
    s['centro'] = ParagraphStyle('centro', parent=s['corpo'], alignment=TA_CENTER)
    s['rodape'] = ParagraphStyle('rodape', fontSize=7.5, textColor=colors.grey,
        alignment=TA_CENTER, fontName=ZH)
    s['clausula'] = ParagraphStyle('clausula', fontSize=9.5, textColor=AZUL_CLARO,
        fontName=ZH, spaceBefore=8, spaceAfter=3)
    s['aviso'] = ParagraphStyle('aviso', fontSize=9, textColor=colors.HexColor('#8b0000'),
        fontName=ZH)
    return s

def hr():
    return HRFlowable(width='100%', thickness=1, color=DOURADO, spaceAfter=8, spaceBefore=4)

def tab(dados, cols, cab_cor=AZUL, zebra=True):
    t = Table(dados, colWidths=cols)
    e = [
        ('BACKGROUND', (0,0), (-1,0), cab_cor),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,-1), ZH),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#c0c8d0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]
    if zebra:
        for i in range(1, len(dados)):
            if i % 2 == 0:
                e.append(('BACKGROUND', (0,i), (-1,i), CINZA))
    t.setStyle(TableStyle(e))
    return t

def assinaturas(s):
    dados = [
        [Paragraph('服务提供方', s['centro']), Paragraph('客户', s['centro'])],
        [Paragraph(f"{PRESTADOR['empresa']}\n{PRESTADOR['nome']}", s['centro']),
         Paragraph('Song 小姐\n（Song 先生之女）', s['centro'])],
        ['', ''],
        [Paragraph('_________________________________', s['centro']),
         Paragraph('_________________________________', s['centro'])],
        [Paragraph(f'日期：_____ / _____ / {ANO}', s['centro']),
         Paragraph(f'日期：_____ / _____ / {ANO}', s['centro'])],
    ]
    t = Table(dados, colWidths=[(W-2*MARGEM)/2]*2)
    t.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('FONTNAME', (0,0), (-1,-1), ZH),
    ]))
    return t

def cab_doc(s, n, titulo, sub=''):
    bloco = Table([[Paragraph(f"文件 {n} — {titulo}", s['titulo'])]],
        colWidths=[W - 2*MARGEM])
    bloco.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
    ]))
    r = [bloco]
    if sub:
        r.append(Paragraph(sub, s['sub']))
    r.append(Spacer(1, 6))
    return r

def num_pag(canvas, doc):
    canvas.saveState()
    canvas.setFont(ZH, 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawString(MARGEM, 1.1*cm,
        f"Toledo Digital · {PRESTADOR['email']} · {PRESTADOR['tel']}")
    canvas.drawRightString(W - MARGEM, 1.1*cm, f"第 {doc.page} 页")
    canvas.restoreState()

def doc1(s):
    elems = []
    elems += cab_doc(s, "1", "服务合同", "Toledo Digital · 网站开发与数字应用")

    elems.append(Paragraph("双方信息", s['secao']))
    partes = [
        ['项目', '服务提供方', '客户'],
        ['姓名 / 公司', f"{PRESTADOR['empresa']}\n{PRESTADOR['nome']}", 'Song 小姐（Song 先生之女）'],
        ['税号 (NIF)', '_______________', '_______________'],
        ['地址', PRESTADOR['morada'], '_______________'],
        ['联系方式', f"{PRESTADOR['tel']}\n{PRESTADOR['email']}", '+351 966 599 195\njiaxinsong327@gmail.com'],
        ['服务内容', '会计事务所网站（PT+中文）\n+ QR点餐系统（Mar de Prata）', ''],
        ['合同金额', '€600 — 交付后付款（现金）', ''],
        ['合同日期', HOJE, ''],
    ]
    elems.append(tab(partes, [3.5*cm, 8*cm, 4.5*cm]))
    elems.append(Spacer(1, 10))

    clausulas = [
        ("第一条 — 合同标的",
         "本合同的标的为服务提供方向客户提供数字开发服务，具体内容以附随的商业报价及"
         "工作范围说明书（文件2）为准。服务提供方承诺以专业态度、在约定期限内、"
         "按照客户认可的规格完成项目开发。"),
        ("第二条 — 工期",
         "工期自客户提交所有必要资料（标志、文案、照片、基础设施账户）之日起计算。"
         "各套餐的预计工期见商业报价。因客户未能及时提供资料而导致的延误，"
         "不由服务提供方承担责任，工期相应顺延。"),
        ("第三条 — 价格与付款条件",
         "约定金额在项目完成交付并经客户验收后一次性付清。无需支付任何定金。"
         "例外情况：域名和服务器（VPS）费用由客户直接向 Hostinger 支付，归客户所有。"
         "本合同特别说明：由于服务提供方与客户父亲 Song 先生的长期友好关系，"
         "本次服务以优惠价提供（正常市场价格 €1.100，友情价 €600）。"),
        ("第四条 — 服务提供方的义务",
         "服务提供方承诺：(a) 按约定范围完成项目开发；(b) 及时告知客户项目进度；"
         "(c) 提供两轮修改（含于报价之内）；(d) 交付时移交全部访问权限；"
         "(e) 确保符合葡萄牙 RGPD 法规及相关法律要求。"),
        ("第五条 — 客户的义务",
         "客户承诺：(a) 及时提供所需资料（文案、图片、标志、法律信息）；"
         "(b) 自行创建并管理 Hostinger 账户（域名和服务器）；"
         "(c) 在5个工作日内对每个项目阶段进行审核和反馈；"
         "(d) 验收时按时付款；(e) 指定一名项目沟通负责人。"),
        ("第六条 — 工作范围与限制",
         "本合同的具体工作范围详见文件2（工作范围说明书）。范围外的功能需另行报价。"
         "服务提供方不对以下事项承担责任：(a) 服务器或域名故障（Hostinger 责任）；"
         "(b) 客户提供的含违法内容或第三方版权的资料；"
         "(c) 交付后客户或第三方对代码进行的修改。"),
        ("第七条 — 知识产权与访问权",
         "付款完成后，客户对所有交付成果（含源代码、数据库及相关内容）享有完整权利。"
         "服务提供方保留将本项目列入作品集的权利，除非客户明确表示反对。"),
        ("第八条 — 保密义务",
         "双方承诺对本合同框架内交换的所有信息严格保密，包括客户数据、"
         "商业策略和访问凭证。此保密义务自合同结束后持续三（3）年。"),
        ("第九条 — 交付后技术支持",
         "交付后的技术支持为可选服务，单独收费（€30/月，无最低合同期限）。"
         "支持范围包括：内容更新、小幅修改、24小时响应。"
         "不包括：项目重新设计、新功能开发或结构性变更。"),
        ("第十条 — 争议解决与适用法律",
         "如发生争议，双方承诺在30天内友好协商解决。"
         "本合同受葡萄牙法律管辖，管辖法院为服务提供方所在地法院（波尔图），"
         "双方明确放弃其他任何管辖权。"),
    ]
    for titulo, texto in clausulas:
        elems.append(KeepTogether([
            Paragraph(titulo, s['clausula']),
            Paragraph(texto, s['corpo']),
            Spacer(1, 4),
        ]))

    elems.append(Spacer(1, 14))
    elems.append(hr())
    elems.append(Paragraph(f"Leça da Palmeira，{HOJE}", s['centro']))
    elems.append(Spacer(1, 18))
    elems.append(assinaturas(s))
    return elems

def doc2(s):
    elems = [PageBreak()]
    elems += cab_doc(s, "2", "工作范围说明书（SOW）", "明确项目包含与不包含的内容")

    elems.append(Paragraph("本文件的用途", s['secao']))
    elems.append(Paragraph(
        "本文件明确规定服务提供方的交付内容、项目阶段、各方验收节点、"
        "双方责任分工，以及不在本合同范围内的事项。本文件是服务合同的组成部分。", s['corpo']))
    elems.append(Spacer(1, 6))

    elems.append(Paragraph("项目阶段 — 从构想到交付", s['secao']))
    fases = [
        ['阶段', '名称', '内容', '负责方', '时长'],
        ['1', '简报会议', '收集资料：标志、颜色、文案、照片、法律信息、域名', '双方', '1-3天'],
        ['2', '基础设施\n搭建', '客户创建 Hostinger 账户、注册域名并共享访问权限。\n服务方配置服务器和 SSL 证书。', '客户+服务方', '1-2天'],
        ['3', '开发阶段', '构建系统：后端、数据库、前端及约定功能。', '服务方', '因套餐而异'],
        ['4', '第一轮\n审核', '发送初版给客户，客户在5个工作日内审核并列出修改意见。', '双方', '3-5天'],
        ['5', '调整与\n内容整合', '整合真实内容（照片、文案）并落实第4阶段的修改意见。', '服务方', '2-4天'],
        ['6', '第二轮\n最终审核', '最终确认，最多2轮修改含于报价内，额外修改另行报价。', '双方', '2-3天'],
        ['7', '测试', '在手机、平板、电脑上测试。验证 RGPD、表单及各项功能。', '服务方', '1-2天'],
        ['8', '交付', '部署上线，操作培训（30-45分钟），移交全部账户权限，客户签署验收单。', '双方', '1天'],
    ]
    elems.append(tab(fases, [1*cm, 2.5*cm, 7*cm, 2.5*cm, 2*cm]))
    elems.append(Spacer(1, 10))

    elems.append(Paragraph("服务包含内容", s['secao']))
    inc = [
        "✓  响应式网站（适配手机、平板、电脑）",
        "✓  域名和服务器由服务方负责配置（账户归客户所有）",
        "✓  SSL/HTTPS — 从第一天起即启用安全连接",
        "✓  RGPD 合规：隐私政策、Cookie 政策及服务条款",
        "✓  客户可自主管理内容的后台管理系统",
        "✓  基础 SEO：标题、Meta 描述、Google 站长工具",
        "✓  功能性联系表单",
        "✓  报价内含两轮修改",
        "✓  操作培训（30-45分钟）",
        "✓  移交全部访问凭证",
        "✓  交付后1个月使用咨询支持（含于报价内）",
    ]
    for i in inc:
        elems.append(Paragraph(i, ParagraphStyle('inc', parent=s['corpo'], leftIndent=12)))
    elems.append(Spacer(1, 8))

    elems.append(Paragraph("服务范围之外 / 不在我们控制范围内的事项", s['secao']))
    exc = [
        "✗  Hostinger 服务器故障或维护（由 Hostinger 负责）",
        "✗  域名年度续费（由客户负责）",
        "✗  VPS 月费（由客户直接支付）",
        "✗  客户提供的错误、过时或含第三方版权的内容",
        "✗  本范围内未约定的新功能（需另行报价）",
        "✗  交付后客户或第三方对代码进行的修改",
        "✗  营销策略、社交媒体或付费广告（需另签合同）",
        "✗  内容翻译（由客户审核中文译文）",
        "✗  专业摄影或标志设计（由客户提供文件）",
        "✗  Google 搜索排名 — SEO 效果通常需3至6个月",
    ]
    for e in exc:
        elems.append(Paragraph(e, ParagraphStyle('exc', parent=s['corpo'], leftIndent=12)))
    elems.append(Spacer(1, 8))

    elems.append(Paragraph("客户需提供的资料（项目启动前）", s['secao']))
    elems.append(Paragraph("开发工作须在收到以下全部资料后方可开始：", s['corpo']))
    cont = [
        ['#', '资料', '格式', '负责方'],
        ['1', '标志', 'PNG 或 SVG，透明背景', '客户'],
        ['2', '品牌色或视觉参考', 'HEX 色码或参考图', '客户'],
        ['3', '公司介绍、服务列表等文案', 'Word / PDF / WhatsApp', '客户'],
        ['4', '照片（场所、团队、产品）', 'JPG/PNG，最小1MB', '客户'],
        ['5', '法律信息（名称、税号、地址）', '任意格式', '客户'],
        ['6', '期望域名（例：seugabinete.pt）', '文字', '客户'],
        ['7', '已创建 Hostinger 账户', '共享登录信息', '客户'],
        ['8', '指定项目沟通负责人', '电话/电子邮件', '客户'],
    ]
    elems.append(tab(cont, [0.8*cm, 7*cm, 5*cm, 3*cm]))
    elems.append(Spacer(1, 8))

    elems.append(Paragraph("沟通与审核时限", s['secao']))
    elems.append(Paragraph(
        "客户有 <b>5个工作日</b> 对每个交付阶段进行审核。逾期未回复则视为默认通过，项目继续推进。"
        "主要沟通渠道：<b>WhatsApp</b>。视频会议可安排在周四15时或晚间（21-23时）。", s['corpo']))

    elems.append(Spacer(1, 14))
    elems.append(hr())
    elems.append(Paragraph("双方声明已阅读并理解本工作范围说明书。", s['corpo']))
    elems.append(Spacer(1, 18))
    elems.append(assinaturas(s))
    return elems

def doc3(s):
    elems = [PageBreak()]
    elems += cab_doc(s, "3", "最终验收确认书（TAF）", "交付时签署 — 确认客户已收到约定的服务内容")

    elems.append(Paragraph("本文件的用途", s['secao']))
    elems.append(Paragraph(
        "最终验收确认书由客户在项目完成交付时签署，确认客户已收到、测试并认可所完成的工作，"
        "所有账户权限已移交，付款已完成。本文件正式标志项目结束，并激活交付后的技术支持服务。", s['corpo']))
    elems.append(Spacer(1, 8))

    elems.append(Paragraph("交付验收清单", s['secao']))
    checklist = [
        ['', '验收项目', '客户确认'],
        ['☐', '网站/应用已上线并可通过约定地址正常访问', '_______________'],
        ['☐', '已在手机和电脑上测试所有页面和功能', '_______________'],
        ['☐', '后台管理系统已交付并运行正常', '_______________'],
        ['☐', '后台管理账户已移交', '_______________'],
        ['☐', 'Hostinger 服务器账户（VPS）已移交', '_______________'],
        ['☐', '域名已正确指向服务器', '_______________'],
        ['☐', 'SSL/HTTPS 已启用（浏览器显示安全锁）', '_______________'],
        ['☐', '联系表单已测试并运行正常', '_______________'],
        ['☐', 'RGPD 合规内容已呈现（隐私政策、Cookie、服务条款）', '_______________'],
        ['☐', '操作培训已完成（时长：______ 分钟）', '_______________'],
        ['☐', '使用说明文件已交付（如适用）', '_______________'],
        ['☐', '套餐内的特定功能已测试并通过验收', '_______________'],
        ['☐', f'付款已完成，金额：€ ___________', '_______________'],
    ]
    t = Table(checklist, colWidths=[0.7*cm, 11*cm, 4.3*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), AZUL),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,-1), ZH),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#c0c8d0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, CINZA]),
    ]))
    elems.append(t)
    elems.append(Spacer(1, 12))

    elems.append(Paragraph("验收声明", s['secao']))
    elems.append(Paragraph("本人作为客户，特此声明：", s['corpo']))
    declaracoes = [
        "1. 已收到并测试本项目，项目内容符合服务合同及工作范围说明书的约定；",
        "2. 交付成果与约定内容一致；",
        "3. 已收到自主管理系统所需的全部账户访问凭证；",
        "4. 已了解并理解合同范围及其限制；",
        "5. 已按约定金额完成付款；",
        "6. 自本文件签署之日起，任何额外修改需另行报价；",
        "7. 交付后技术支持服务（如已订购）自本日起生效。",
    ]
    for d in declaracoes:
        elems.append(Paragraph(d, ParagraphStyle('d', parent=s['corpo'], leftIndent=12)))
    elems.append(Spacer(1, 10))

    elems.append(Paragraph("客户备注/保留意见（如有）：", s['secao']))
    elems.append(Spacer(1, 4))
    obs = Table([['']], colWidths=[W-2*MARGEM], rowHeights=[2.5*cm])
    obs.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#c0c8d0')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fafbfc')),
    ]))
    elems.append(obs)
    elems.append(Spacer(1, 16))
    elems.append(hr())
    elems.append(Paragraph(f"交付地点及日期：_________________________ ，_____ / _____ / {ANO}", s['corpo']))
    elems.append(Spacer(1, 18))
    elems.append(assinaturas(s))
    elems.append(Spacer(1, 16))
    elems.append(Paragraph(
        "⚠️  本文件须一式两份签署，双方各执一份。",
        s['aviso']))
    return elems

def gerar():
    s = st()
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
        leftMargin=MARGEM, rightMargin=MARGEM,
        topMargin=2*cm, bottomMargin=2*cm,
        title="Toledo Digital — 合同文件（中文版）")

    story = []

    # 封面
    story.append(Spacer(1, 2.5*cm))
    capa = Table([
        [Paragraph("TOLEDO DIGITAL", s['titulo'])],
        [Paragraph("网站开发 & 数字应用服务", s['sub'])],
    ], colWidths=[W - 2*MARGEM])
    capa.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL),
        ('TOPPADDING', (0,0), (-1,-1), 18),
        ('BOTTOMPADDING', (0,0), (-1,-1), 18),
    ]))
    story.append(capa)
    story.append(Spacer(1, 0.8*cm))
    story.append(Paragraph("合同文件套装（中文版）", ParagraphStyle('t2',
        fontSize=16, textColor=AZUL, fontName=ZH, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.4*cm))
    story.append(hr())
    story.append(Spacer(1, 0.4*cm))

    indice = [
        ['文件 1', '服务合同', '→ 第2页'],
        ['文件 2', '工作范围说明书（SOW）', '→ 第X页'],
        ['文件 3', '最终验收确认书（TAF）', '→ 第X页'],
    ]
    ti = Table(indice, colWidths=[3*cm, 11*cm, 2*cm])
    ti.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), ZH),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('TEXTCOLOR', (0,0), (0,-1), AZUL_CLARO),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LINEBELOW', (0,0), (-1,-2), 0.5, colors.HexColor('#e0e0e0')),
    ]))
    story.append(ti)
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph(
        f"版本 1.0 · {HOJE} · 仅供内部使用 — Toledo Digital",
        ParagraphStyle('r', fontSize=9, textColor=colors.grey, alignment=TA_CENTER, fontName=ZH)))
    story.append(PageBreak())

    story += doc1(s)
    story += doc2(s)
    story += doc3(s)

    doc.build(story, onFirstPage=num_pag, onLaterPages=num_pag)
    print(f"✅ PDF gerado: {OUTPUT}")

if __name__ == '__main__':
    gerar()
