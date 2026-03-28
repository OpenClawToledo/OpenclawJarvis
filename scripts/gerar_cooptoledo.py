#!/usr/bin/env python3
"""CoopToledo — Plano de Negócio PDF"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
import datetime

OUTPUT = "/data/.openclaw/workspace/propostas/CoopToledo_Plano_Negocio_2026.pdf"
W, H = A4
MARGEM = 2.2 * cm
VERDE = colors.HexColor('#1B4332')
VERDE_CLARO = colors.HexColor('#2D6A4F')
DOURADO = colors.HexColor('#D4AC0D')
CINZA = colors.HexColor('#F5F5F5')
CINZA2 = colors.HexColor('#E8F5E9')

def estilos():
    base = getSampleStyleSheet()
    s = {}
    s['titulo'] = ParagraphStyle('titulo', fontSize=22, textColor=colors.white,
        fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=6)
    s['subtitulo'] = ParagraphStyle('subtitulo', fontSize=12, textColor=DOURADO,
        fontName='Helvetica', alignment=TA_CENTER, spaceAfter=4)
    s['secao'] = ParagraphStyle('secao', fontSize=13, textColor=VERDE,
        fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=6)
    s['corpo'] = ParagraphStyle('corpo', fontSize=9.5, textColor=colors.HexColor('#222'),
        leading=15, spaceAfter=6, alignment=TA_JUSTIFY, fontName='Helvetica')
    s['lista'] = ParagraphStyle('lista', parent=s['corpo'], leftIndent=14)
    s['centro'] = ParagraphStyle('centro', parent=s['corpo'], alignment=TA_CENTER)
    s['bold'] = ParagraphStyle('bold', parent=s['corpo'], fontName='Helvetica-Bold')
    s['rodape'] = ParagraphStyle('rodape', fontSize=7.5, textColor=colors.grey,
        alignment=TA_CENTER, fontName='Helvetica')
    s['destaque'] = ParagraphStyle('destaque', fontSize=10, textColor=VERDE,
        fontName='Helvetica-Bold', alignment=TA_CENTER)
    return s

def hr():
    return HRFlowable(width='100%', thickness=1, color=DOURADO, spaceAfter=8, spaceBefore=4)

def cab(s, n, titulo, sub=''):
    dados = [[Paragraph(f"{n}. {titulo}", s['titulo'])]]
    t = Table(dados, colWidths=[W - 2*MARGEM])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), VERDE),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
    ]))
    r = [t]
    if sub:
        r.append(Paragraph(sub, s['subtitulo']))
    r.append(Spacer(1, 6))
    return r

def tabela(dados, cols, zebra=True, cab_cor=VERDE):
    t = Table(dados, colWidths=cols)
    estilo = [
        ('BACKGROUND', (0,0), (-1,0), cab_cor),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#BDBDBD')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]
    if zebra:
        for i in range(1, len(dados)):
            if i % 2 == 0:
                estilo.append(('BACKGROUND', (0,i), (-1,i), CINZA2))
    t.setStyle(TableStyle(estilo))
    return t

def numeracao(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawString(MARGEM, 1.1*cm, "CoopToledo · Governador Valadares, MG · Documento Confidencial")
    canvas.drawRightString(W - MARGEM, 1.1*cm, f"Página {doc.page}")
    canvas.restoreState()

def gerar():
    s = estilos()
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
        leftMargin=MARGEM, rightMargin=MARGEM,
        topMargin=2*cm, bottomMargin=2*cm,
        title="CoopToledo — Plano de Negócio 2026")

    story = []

    # ── CAPA ──
    story.append(Spacer(1, 2.5*cm))
    capa = Table([[Paragraph("🌱 CoopToledo", s['titulo'])],
                  [Paragraph("COOPERATIVA DE ALIMENTOS", s['subtitulo'])],
                  [Paragraph("Governador Valadares · Minas Gerais · Brasil", s['subtitulo'])]],
        colWidths=[W - 2*MARGEM])
    capa.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), VERDE),
        ('TOPPADDING', (0,0), (-1,-1), 16),
        ('BOTTOMPADDING', (0,0), (-1,-1), 16),
    ]))
    story.append(capa)
    story.append(Spacer(1, 0.8*cm))

    kpis = [
        ['20 famílias\nfundadoras', '~45%\neconomia mensal', 'R$468\npor família/mês', 'R$0\nplataforma digital'],
    ]
    kt = Table(kpis, colWidths=[(W-2*MARGEM)/4]*4)
    kt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DOURADO),
        ('TEXTCOLOR', (0,0), (-1,-1), VERDE),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ]))
    story.append(kt)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(f"Plano de Negócio · Versão 1.0 · Março de 2026", s['centro']))
    story.append(Paragraph("Documento Confidencial — Uso Interno", s['rodape']))

    # ── SUMÁRIO EXECUTIVO ──
    story.append(PageBreak())
    story += cab(s, "1", "SUMÁRIO EXECUTIVO")
    story.append(Paragraph(
        "A <b>CoopToledo</b> é uma cooperativa de consumo de alimentos sediada em Governador "
        "Valadares (MG), constituída por 20 famílias fundadoras (≈100 pessoas). O modelo "
        "combina compras coletivas directas na <b>CEASAMINAS</b> — o maior hub de distribuição "
        "de alimentos da região — com aquisição de boi vivo directo do produtor, abate em "
        "frigorífico e desossa realizada pelo próprio fundador (açougueiro desossador profissional).", s['corpo']))
    story.append(Paragraph(
        "Cada família paga <b>R$468/mês</b> e recebe uma cesta completa com hortifruti, grãos "
        "e ≈10,5kg de carne bovina de qualidade. O equivalente no varejo custa <b>R$800–900/mês</b>, "
        "representando uma <b>economia de 45%</b>. A gestão é 100% digital, com plataforma web "
        "desenvolvida internamente pela Toledo Digital, sem custo adicional.", s['corpo']))

    kpis2 = [['Indicador', 'Valor'],
             ['Famílias (fase piloto)', '20'],
             ['Pessoas beneficiadas', '≈100'],
             ['Mensalidade por família', 'R$468'],
             ['Economia vs. varejo', '~45% (≈R$400/mês)'],
             ['Investimento inicial', 'R$2.000–3.500 (abertura)'],
             ['Ponto de equilíbrio', 'Desde o 1º mês'],
             ['Horizonte de análise', '12 meses (piloto → 80 famílias)'],
    ]
    story.append(tabela(kpis2, [9*cm, 7*cm]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Diferenciais competitivos:</b> (1) Desossa própria — zero custo de mão-de-obra; "
        "(2) Plataforma digital interna — zero custo de desenvolvimento; "
        "(3) Fornecedor oficial CEASAMINAS — rastreabilidade e preço de atacado; "
        "(4) Modelo cooperativo — sem lucro, sobras distribuídas aos membros.", s['corpo']))

    # ── O NEGÓCIO ──
    story.append(PageBreak())
    story += cab(s, "2", "O NEGÓCIO", "Proposta de valor e modelo operacional")
    story.append(Paragraph(
        "A CoopToledo resolve um problema concreto: <b>o custo de alimentação de qualidade "
        "é proibitivo para famílias de classe média e trabalhadora em Governador Valadares</b>. "
        "A solução é o poder de compra colectivo — 20 famílias compram juntas como se fossem "
        "um único cliente de grande porte, acessando preços de atacado inacessíveis individualmente.", s['corpo']))

    story.append(Paragraph("Proposta de Valor", s['secao']))
    pv = [['Para o cooperado', 'Para a comunidade'],
          ['✓ Alimentos frescos a preço de custo', '✓ Fortalece economia local'],
          ['✓ Carne bovina de qualidade (origem conhecida)', '✓ Reduz intermediários'],
          ['✓ Transparência total nos gastos', '✓ Modelo replicável na região'],
          ['✓ Gestão digital simples (app/web)', '✓ Gera trabalho local (logística)'],
    ]
    story.append(tabela(pv, [(W-2*MARGEM)/2, (W-2*MARGEM)/2]))

    story.append(Paragraph("Fluxo Semanal de Operação", s['secao']))
    fluxo = [['Etapa', 'Quando', 'Responsável', 'Descrição'],
             ['1. Encomenda', 'Seg-Qua', 'Cooperado', 'Escolhe itens na plataforma web e paga via Pix'],
             ['2. Compra CEASA', 'Quinta', 'Directoria', 'Compra em atacado na CEASAMINAS GV com lista consolidada'],
             ['3. Compra boi', 'Mensal', 'Directoria', 'Negoceia boi gordo directo com produtor rural da região'],
             ['4. Abate', 'Mensal', 'Frigorífico', 'Abate em frigorífico parceiro — custo fixo negociado'],
             ['5. Desossa', 'Mensal', 'Fundador', 'Desossa profissional — sem custo de mão-de-obra'],
             ['6. Separação', 'Sexta', 'Equipa', 'Divide e embala cesta + carne por família'],
             ['7. Entrega/Retirada', 'Sábado', 'Equipa', 'Ponto de retirada central ou entrega acordada'],
             ['8. Relatório', 'Dom', 'Sistema', 'Plataforma envia resumo financeiro a todos os cooperados'],
    ]
    story.append(tabela(fluxo, [2.5*cm, 2*cm, 2.5*cm, 9*cm]))

    # ── PLANO FINANCEIRO ──
    story.append(PageBreak())
    story += cab(s, "3", "PLANO FINANCEIRO", "Custos, receitas e projecção 12 meses")

    story.append(Paragraph("Cesta Mensal por Família (5 pessoas)", s['secao']))
    cesta = [['Item', 'Qtd/mês', 'Custo CEASA', 'Equivalente varejo'],
             ['Tomate', '5kg', 'R$12', 'R$25'],
             ['Batata', '8kg', 'R$20', 'R$40'],
             ['Cebola', '3kg', 'R$7', 'R$15'],
             ['Cenoura', '3kg', 'R$5', 'R$12'],
             ['Alho', '500g', 'R$5', 'R$12'],
             ['Folhosas/Couve', 'var', 'R$5', 'R$12'],
             ['Alface', '4 un', 'R$5', 'R$10'],
             ['Banana', '5kg', 'R$11', 'R$22'],
             ['Laranja', '5kg', 'R$11', 'R$20'],
             ['Mamão', '2 un', 'R$4', 'R$10'],
             ['Arroz', '5kg', 'R$21', 'R$40'],
             ['Feijão', '3kg', 'R$19', 'R$36'],
             ['Óleo vegetal', '2L', 'R$16', 'R$28'],
             ['SUBTOTAL CEASA', '', 'R$141', 'R$282'],
             ['Carne bovina (10,5kg/boi direto)', '10,5kg', 'R$302', 'R$525'],
             ['Taxa de gestão', '', 'R$25', '—'],
             ['TOTAL POR FAMÍLIA', '', 'R$468', 'R$807'],
    ]
    story.append(tabela(cesta, [6*cm, 2.5*cm, 3*cm, 4.5*cm]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Cálculo da carne:</b> Boi médio 17@ × R$332/@ = R$5.644 + abate R$400 = R$6.044. "
        "Rendimento limpo: ≈210kg ÷ 20 famílias = 10,5kg/família. "
        "Custo unitário: R$6.044 ÷ 20 = R$302/família.", s['corpo']))

    story.append(Paragraph("Movimento Mensal — 20 Famílias (Fase Piloto)", s['secao']))
    mov = [['Descrição', 'Valor'],
           ['Arrecadação (20 × R$468)', 'R$9.360'],
           ['(-) Boi gordo + abate', '(R$6.044)'],
           ['(-) Cesta CEASA × 20 famílias', '(R$2.820)'],
           ['(=) Fundo operacional', 'R$496'],
           ['Uso: logística + embalagem + plataforma', '≈(R$400)'],
           ['Reserva cooperativa (sobras)', '≈R$96'],
    ]
    story.append(tabela(mov, [11*cm, 5*cm]))

    story.append(Paragraph("Projecção 12 Meses", s['secao']))
    proj = [['Período', 'Famílias', 'Arrecadação', 'Custo total', 'Fundo operacional'],
            ['Mês 1–3 (piloto)', '20', 'R$9.360', 'R$8.864', 'R$496'],
            ['Mês 4–6', '40', 'R$18.720', 'R$17.728', 'R$992'],
            ['Mês 7–9', '60', 'R$28.080', 'R$26.592', 'R$1.488'],
            ['Mês 10–12', '80', 'R$37.440', 'R$35.456', 'R$1.984'],
            ['Ano 1 (total)', '—', '≈R$276.480', '≈R$261.888', '≈R$14.592'],
    ]
    story.append(tabela(proj, [3.5*cm, 2.5*cm, 3.5*cm, 3.5*cm, 3*cm]))
    story.append(Spacer(1,6))
    story.append(Paragraph(
        "As sobras anuais (≈R$14.592 no Ano 1) são distribuídas proporcionalmente entre "
        "os cooperados em Assembleia, conforme a Lei 5.764/71.", s['corpo']))

    # ── ESTRUTURA JURÍDICA ──
    story.append(PageBreak())
    story += cab(s, "4", "ESTRUTURA JURÍDICA", "Passo a passo para abertura em MG")
    jur = [['Etapa', 'O que fazer', 'Custo estimado', 'Prazo'],
           ['1', 'Reunir 20 cooperados fundadores com documentação (RG + CPF)', 'R$0', 'Imediato'],
           ['2', 'Elaborar Estatuto Social (modelo no Anexo)', 'R$300–500 (advogado)', '1 semana'],
           ['3', 'Assembleia Geral de Constituição — eleger directoria + conselho fiscal', 'R$0', '1 dia'],
           ['4', 'Registar Ata + Estatuto na Junta Comercial de MG', 'R$400–600', '1–2 semanas'],
           ['5', 'CNPJ emitido automaticamente pela Receita Federal', 'R$0', 'Automático'],
           ['6', 'Registar na OCB-MG (Org. das Cooperativas de MG)', 'R$200–400', '1 semana'],
           ['7', 'Alvará de funcionamento na Prefeitura de GV', 'R$200–500', '1–3 semanas'],
           ['8', 'Licença Vigilância Sanitária (para alimentos)', 'R$300–600', '2–4 semanas'],
           ['9', 'Conta bancária PJ cooperativa (Sicoob ou Caixa)', 'R$0', '1 semana'],
           ['TOTAL', '', 'R$1.400–2.600', '6–10 semanas'],
    ]
    story.append(tabela(jur, [1*cm, 8.5*cm, 3*cm, 3*cm]))
    story.append(Spacer(1,8))

    story.append(Paragraph("Órgãos de Gestão (obrigatórios por lei)", s['secao']))
    org = [['Órgão', 'Composição', 'Função'],
           ['Assembleia Geral', 'Todos os cooperados\n(1 voto por pessoa)', 'Órgão supremo. Aprova contas, elege directoria, altera estatuto.'],
           ['Conselho de Admin.', 'Presidente + 2 membros\n(eleitos por 2 anos)', 'Gere o dia a dia. Compras, contratos, plataforma, relatórios.'],
           ['Conselho Fiscal', '3 titulares + 3 suplentes\n(eleitos por 1 ano)', 'Fiscaliza contas e operações. Garante transparência.'],
    ]
    story.append(tabela(org, [3.5*cm, 4*cm, 8.5*cm]))

    # ── PLATAFORMA DIGITAL ──
    story.append(PageBreak())
    story += cab(s, "5", "PLATAFORMA DIGITAL", "Desenvolvida internamente — custo R$0")
    story.append(Paragraph(
        "A Toledo Digital desenvolve e mantém a plataforma de gestão da CoopToledo. "
        "Por ser o próprio fundador o desenvolvedor, o custo é zero — uma vantagem "
        "competitiva única que nenhuma outra cooperativa local possui.", s['corpo']))

    func = [['Módulo', 'Funcionalidade'],
            ['Encomendas', 'Cooperado entra na plataforma, escolhe o que quer na semana e confirma pedido'],
            ['Pagamento', 'Pix integrado — a cooperativa recebe automaticamente e regista a transacção'],
            ['Gestão de compras', 'Sistema consolida todos os pedidos e gera lista de compras para CEASA + boi'],
            ['Rastreio', 'Cooperado acompanha status: "compra feita", "em separação", "pronto p/ retirada"'],
            ['Financeiro', 'Relatório mensal automático para todos: quanto entrou, quanto saiu, sobra'],
            ['Comunicação', 'Avisos, novidades e votações via plataforma + WhatsApp'],
            ['Admin', 'Painel para gestão de membros, produtos, preços e relatórios'],
    ]
    story.append(tabela(func, [3.5*cm, 12.5*cm]))
    story.append(Spacer(1,8))
    story.append(Paragraph(
        "Stack tecnológica: Spring Boot (backend) + interface web responsiva (mobile-first). "
        "Hospedagem: VPS Hostinger (~R$50/mês, já partilhado com outros projetos Toledo Digital). "
        "Pagamentos: integração Pix via API bancária (Sicoob ou Nubank PJ).", s['corpo']))

    # ── CRONOGRAMA ──
    story.append(PageBreak())
    story += cab(s, "6", "CRONOGRAMA", "Roadmap 12 meses")
    cron = [['Mês', 'Marco principal', 'Acção-chave'],
            ['1', 'Formalização legal', 'Assembleia constituinte + início registro Junta Comercial'],
            ['2', 'CNPJ + conta bancária', 'OCB-MG + conta PJ + alvará municipal'],
            ['3', 'Piloto operacional (20 famílias)', '1ª compra CEASA + 1º boi + entrega piloto'],
            ['4', 'Plataforma digital live', 'Lançamento do site de encomendas com Pix'],
            ['5', 'Primeira Assembleia de Resultados', 'Apresentar contas do trimestre + distribuir sobras'],
            ['6', 'Expansão para 40 famílias', 'Abrir inscrições para 2ª leva de cooperados'],
            ['7–8', '2 bois/mês + 2ª ronda CEASA', 'Aumentar volume, negociar preço fixo boi'],
            ['9', '60 famílias', 'Contratar ajudante de logística (remunerado pela cooperativa)'],
            ['10–11', 'Box na CEASAMINAS?', 'Avaliar viabilidade de ter espaço próprio na CEASA GV'],
            ['12', 'Assembleia anual', 'Balanço, distribuição de sobras, metas Ano 2 (150 famílias)'],
    ]
    story.append(tabela(cron, [1.5*cm, 5*cm, 9.5*cm]))

    # ── PRÓXIMOS PASSOS ──
    story.append(PageBreak())
    story += cab(s, "7", "PRÓXIMOS PASSOS", "3 acções concretas para arrancar")
    passos = [
        ("1. Ligar para a CEASAMINAS Governador Valadares",
         "Contacto: (33) 99110-0011\nPerguntar: valores mínimos de compra por caixa/saco, "
         "horário de funcionamento, como se cadastrar como comprador atacadista. "
         "Visitar pessoalmente para conhecer os boxes e negociar com fornecedores directos."),
        ("2. Reunião de fundação com os 20 interessados",
         "Apresentar este plano de negócio. Confirmar compromisso de cada família. "
         "Recolher R$100 de cada (R$2.000 total) para cobrir custos de abertura legal. "
         "Eleger informalmente quem será Presidente, Tesoureiro e Conselho Fiscal."),
        ("3. Contactar frigorífico e produtor de boi",
         "Identificar o frigorífico mais próximo de GV que aceite abate de terceiros. "
         "Negociar custo por cabeça com volume garantido (1 boi/mês). "
         "Identificar 2-3 produtores rurais locais para cotação directa sem intermediário."),
    ]
    for titulo, texto in passos:
        box = Table([[Paragraph(titulo, s['bold'])],
                     [Paragraph(texto.replace('\n', '<br/>'), s['corpo'])]],
            colWidths=[W - 2*MARGEM])
        box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), VERDE_CLARO),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('BACKGROUND', (0,1), (-1,-1), CINZA2),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('BOX', (0,0), (-1,-1), 1, VERDE),
        ]))
        story.append(KeepTogether([box, Spacer(1,8)]))

    # ── ESTATUTO MODELO ──
    story.append(PageBreak())
    story += cab(s, "ANEXO", "MODELO SIMPLIFICADO DE ESTATUTO SOCIAL")
    story.append(Paragraph(
        "<i>Este modelo é uma base orientativa. Recomenda-se revisão por advogado especializado "
        "em cooperativismo antes do registro na Junta Comercial.</i>", s['corpo']))
    story.append(Spacer(1,8))

    clausulas_estatuto = [
        ("Art. 1º — DENOMINAÇÃO E SEDE",
         "Fica constituída a COOPTOLEDO — COOPERATIVA DE CONSUMO DE ALIMENTOS DE GOVERNADOR "
         "VALADARES, com sede em Governador Valadares, Estado de Minas Gerais, República "
         "Federativa do Brasil, regendo-se pela Lei Federal n.º 5.764/71, pelo Código Civil "
         "Brasileiro e pelo presente Estatuto."),
        ("Art. 2º — OBJETIVOS",
         "A Cooperativa tem por objectivo a compra colectiva de géneros alimentícios, "
         "hortifrutigranjeiros, carnes e demais alimentos para consumo exclusivo dos seus "
         "cooperados e respectivos familiares, com vista à redução de custos e ao acesso "
         "a produtos de qualidade a preços de atacado."),
        ("Art. 3º — QUADRO SOCIAL",
         "O número mínimo de cooperados é de 20 (vinte) pessoas físicas. A admissão é "
         "voluntária, mediante aprovação do Conselho de Administração e pagamento da quota "
         "de participação. Cada cooperado tem direito a um único voto nas Assembleias Gerais, "
         "independentemente do valor de suas quotas."),
        ("Art. 4º — CAPITAL SOCIAL E QUOTAS",
         "O capital social é variável e ilimitado, constituído por quotas-partes de igual valor. "
         "Cada cooperado subscreve o mínimo de 1 (uma) quota-parte. As quotas são nominativas "
         "e intransferíveis. Em caso de saída, o cooperado recebe o valor actualizado da sua "
         "quota no prazo de 90 dias após aprovação em Assembleia."),
        ("Art. 5º — ÓRGÃOS SOCIAIS",
         "São órgãos da Cooperativa: (I) Assembleia Geral — órgão supremo de deliberação, "
         "realizada ordinariamente uma vez por ano e extraordinariamente quando necessário; "
         "(II) Conselho de Administração — composto por Presidente, Vice-Presidente e "
         "Secretário, eleitos por 2 anos; (III) Conselho Fiscal — composto por 3 membros "
         "titulares e 3 suplentes, eleitos por 1 ano."),
        ("Art. 6º — SOBRAS E PERDAS",
         "As sobras apuradas ao final de cada exercício, após as deduções legais obrigatórias "
         "(Fundo de Reserva — 10% mínimo; FATES — 5% mínimo), serão distribuídas entre os "
         "cooperados proporcionalmente às operações realizadas por cada um no período. "
         "As perdas eventualmente verificadas serão rateadas entre os cooperados na mesma proporção."),
        ("Art. 7º — DISSOLUÇÃO",
         "A Cooperativa poderá ser dissolvida por deliberação da Assembleia Geral Extraordinária, "
         "convocada especialmente para esse fim, com aprovação de 2/3 dos cooperados em pleno "
         "gozo dos seus direitos. O acervo líquido será destinado conforme deliberação da mesma "
         "Assembleia, respeitada a legislação vigente."),
    ]
    for titulo, texto in clausulas_estatuto:
        story.append(KeepTogether([
            Paragraph(titulo, s['bold']),
            Paragraph(texto, s['corpo']),
            Spacer(1,4),
        ]))

    doc.build(story, onFirstPage=numeracao, onLaterPages=numeracao)
    print(f"✅ PDF gerado: {OUTPUT}")

if __name__ == '__main__':
    gerar()
