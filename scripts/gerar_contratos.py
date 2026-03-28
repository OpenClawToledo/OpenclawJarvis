#!/usr/bin/env python3
"""
SolutionSoftware — Gerador de Documentos Contratuais
Gera 3 documentos num único PDF:
  1. Contrato de Prestação de Serviços
  2. Declaração de Âmbito (SOW)
  3. Termo de Aceite Final (TAF)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Flowable
import datetime

# ─── CONFIGURAÇÃO ──────────────────────────────────────────────────────────────
OUTPUT = "/data/.openclaw/workspace/propostas/Toledo_Digital_Contratos_2026.pdf"

PRESTADOR = {
    "nome": "Luís Augusto Soares de Toledo",
    "nif": "_______________",   # preencher quando abrir atividade
    "morada": "Leça da Palmeira, Porto, Portugal",
    "telefone": "+351 931 120 429",
    "email": "toledothelast@gmail.com",
    "designacao": "SolutionSoftware",
}

DATA_HOJE = datetime.date.today().strftime("%d de %B de %Y").replace(
    "January","janeiro").replace("February","fevereiro").replace("March","março"
    ).replace("April","abril").replace("May","maio").replace("June","junho"
    ).replace("July","julho").replace("August","agosto").replace("September","setembro"
    ).replace("October","outubro").replace("November","novembro").replace("December","dezembro")

# ─── ESTILOS ───────────────────────────────────────────────────────────────────
W, H = A4
MARGEM = 2.2 * cm

def build_styles():
    base = getSampleStyleSheet()
    s = {}
    s['titulo_doc'] = ParagraphStyle('titulo_doc', parent=base['Title'],
        fontSize=20, textColor=colors.HexColor('#1a2e4a'), spaceAfter=4,
        alignment=TA_CENTER, fontName='Helvetica-Bold')
    s['subtitulo'] = ParagraphStyle('subtitulo', parent=base['Normal'],
        fontSize=11, textColor=colors.HexColor('#4a6fa5'), spaceAfter=12,
        alignment=TA_CENTER, fontName='Helvetica')
    s['secao'] = ParagraphStyle('secao', parent=base['Normal'],
        fontSize=12, textColor=colors.HexColor('#1a2e4a'), spaceBefore=14,
        spaceAfter=6, fontName='Helvetica-Bold', borderPad=4)
    s['corpo'] = ParagraphStyle('corpo', parent=base['Normal'],
        fontSize=9.5, textColor=colors.HexColor('#2d2d2d'), leading=15,
        spaceAfter=6, alignment=TA_JUSTIFY, fontName='Helvetica')
    s['corpo_bold'] = ParagraphStyle('corpo_bold', parent=s['corpo'],
        fontName='Helvetica-Bold')
    s['lista'] = ParagraphStyle('lista', parent=s['corpo'],
        leftIndent=14, bulletIndent=4)
    s['rodape'] = ParagraphStyle('rodape', parent=base['Normal'],
        fontSize=8, textColor=colors.grey, alignment=TA_CENTER)
    s['assinatura'] = ParagraphStyle('assinatura', parent=base['Normal'],
        fontSize=9, textColor=colors.HexColor('#2d2d2d'), alignment=TA_CENTER)
    s['numero_clausula'] = ParagraphStyle('numero_clausula', parent=s['corpo'],
        fontName='Helvetica-Bold', textColor=colors.HexColor('#4a6fa5'))
    s['aviso'] = ParagraphStyle('aviso', parent=s['corpo'],
        textColor=colors.HexColor('#8b0000'), fontName='Helvetica-Oblique')
    s['centro'] = ParagraphStyle('centro', parent=s['corpo'], alignment=TA_CENTER)
    return s

def linha_divisora(cor='#4a6fa5', espessura=1):
    return HRFlowable(width='100%', thickness=espessura,
                      color=colors.HexColor(cor), spaceAfter=8, spaceBefore=4)

def cabecalho_doc(s, numero, titulo, subtitulo_txt):
    """Retorna bloco de cabeçalho de cada documento"""
    # Fundo azul simulado via tabela
    dados = [[Paragraph(f"DOCUMENTO {numero} — {titulo}", ParagraphStyle('h',
        parent=s['titulo_doc'], fontSize=16, textColor=colors.white))]]
    t = Table(dados, colWidths=[W - 2*MARGEM])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1a2e4a')),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ]))
    return [t, Spacer(1, 8),
            Paragraph(subtitulo_txt, s['subtitulo']),
            linha_divisora()]

def tabela_partes(s, cliente_nome="[NOME DO CLIENTE]", cliente_nif="[NIF]",
                  cliente_morada="[MORADA]", servico="[SERVIÇO]", valor="[VALOR]"):
    dados = [
        ['CAMPO', 'PRESTADOR DE SERVIÇOS', 'CLIENTE'],
        ['Nome / Designação', PRESTADOR['designacao'] + '\n' + PRESTADOR['nome'],
         cliente_nome],
        ['NIF', PRESTADOR['nif'], cliente_nif],
        ['Morada', PRESTADOR['morada'], cliente_morada],
        ['Contacto', PRESTADOR['telefone'] + '\n' + PRESTADOR['email'], ''],
        ['Serviço contratado', servico, ''],
        ['Valor acordado', valor, ''],
        ['Data do contrato', DATA_HOJE, ''],
    ]
    t = Table(dados, colWidths=[3.5*cm, 8*cm, 6.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a2e4a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f0f4f8')),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#c0c8d0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('WORDWRAP', (0,0), (-1,-1), True),
    ]))
    return t

def bloco_assinaturas(s):
    dados = [
        [Paragraph('PRESTADOR DE SERVIÇOS', s['assinatura']),
         Paragraph('CLIENTE', s['assinatura'])],
        [Paragraph(PRESTADOR['nome'], s['assinatura']),
         Paragraph('[Nome do Cliente]', s['assinatura'])],
        ['', ''],
        [Paragraph('_________________________________', s['assinatura']),
         Paragraph('_________________________________', s['assinatura'])],
        [Paragraph('Data: _____ / _____ / _______', s['assinatura']),
         Paragraph('Data: _____ / _____ / _______', s['assinatura'])],
    ]
    t = Table(dados, colWidths=[(W-2*MARGEM)/2, (W-2*MARGEM)/2])
    t.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('FONTSIZE', (0,0), (-1,-1), 9),
    ]))
    return t

# ─── DOCUMENTO 1 — CONTRATO DE PRESTAÇÃO DE SERVIÇOS ──────────────────────────
def doc1_contrato(s):
    elems = []
    elems += cabecalho_doc(s, "1", "CONTRATO DE PRESTAÇÃO DE SERVIÇOS",
        "SolutionSoftware · Desenvolvimento Web & Aplicações · toledothelast@gmail.com")

    elems.append(Paragraph("IDENTIFICAÇÃO DAS PARTES", s['secao']))
    elems.append(tabela_partes(s,
        cliente_nome="[Nome do Cliente]",
        cliente_nif="[NIF do Cliente]",
        cliente_morada="[Morada do Cliente]",
        servico="[Descrição do serviço — ex: Website + App QR Code]",
        valor="€ [Valor] — pago na entrega"))
    elems.append(Spacer(1, 12))

    clausulas = [
        ("CLÁUSULA 1ª — OBJETO DO CONTRATO",
         """O presente contrato tem por objeto a prestação de serviços de desenvolvimento digital
         pelo Prestador ao Cliente, conforme descrição acordada na proposta comercial anexa e
         detalhada na Declaração de Âmbito (Documento 2). O Prestador obriga-se a desenvolver
         a solução acordada de forma profissional, dentro do prazo estipulado e segundo as
         especificações aprovadas pelo Cliente."""),

        ("CLÁUSULA 2ª — PRAZO DE EXECUÇÃO",
         """O prazo de execução inicia-se na data de receção de todos os conteúdos e informações
         necessários fornecidos pelo Cliente (logótipo, textos, fotografias, credenciais de
         infraestrutura). O prazo estimado por pacote é o indicado na proposta comercial.
         Atrasos causados por falta de fornecimento de conteúdos pelo Cliente não são
         imputáveis ao Prestador e suspendem o prazo acordado."""),

        ("CLÁUSULA 3ª — PREÇO E CONDIÇÕES DE PAGAMENTO",
         """O valor acordado é pago <b>na entrega</b> do serviço concluído e após validação pelo
         Cliente. Não é exigido qualquer adiantamento para início do trabalho. Excepção: custos
         de infraestrutura (domínio e servidor VPS), que são contratados diretamente pelo Cliente
         junto à Hostinger e são da sua responsabilidade e propriedade exclusiva."""),

        ("CLÁUSULA 4ª — OBRIGAÇÕES DO PRESTADOR",
         """O Prestador compromete-se a: (a) desenvolver a solução conforme o âmbito acordado;
         (b) manter o Cliente informado do progresso; (c) realizar até 2 (duas) rondas de
         revisões incluídas no preço; (d) entregar credenciais de acesso completas ao Cliente
         na conclusão; (e) garantir conformidade com o RGPD e legislação aplicável em Portugal."""),

        ("CLÁUSULA 5ª — OBRIGAÇÕES DO CLIENTE",
         """O Cliente compromete-se a: (a) fornecer todos os conteúdos necessários em tempo útil
         (textos, imagens, logótipo, dados legais); (b) criar e gerir a sua conta Hostinger para
         domínio e servidor; (c) validar e aprovar cada fase do projeto em até 5 (cinco) dias
         úteis; (d) efetuar o pagamento no momento da entrega; (e) designar um interlocutor
         responsável para comunicação durante o projeto."""),

        ("CLÁUSULA 6ª — ÂMBITO E LIMITAÇÕES",
         """O âmbito do presente contrato está detalhado no Documento 2 (Declaração de Âmbito).
         Qualquer funcionalidade não prevista nesse documento será considerada trabalho adicional,
         sujeito a orçamentação separada. O Prestador não é responsável por: (a) falhas de
         infraestrutura do servidor ou domínio (responsabilidade do Cliente/Hostinger); (b)
         conteúdos ilegais ou com direitos de terceiros fornecidos pelo Cliente; (c) alterações
         feitas pelo Cliente ao código após a entrega."""),

        ("CLÁUSULA 7ª — PROPRIEDADE INTELECTUAL E ACESSO",
         """Após o pagamento integral, o Cliente é titular de todos os direitos sobre o trabalho
         entregue, incluindo código-fonte, base de dados e conteúdos desenvolvidos. O Prestador
         retém o direito de mencionar o projeto no seu portfólio, salvo indicação em contrário
         do Cliente. O Prestador poderá utilizar frameworks, bibliotecas e componentes de
         código aberto (open source) licenciados para uso comercial."""),

        ("CLÁUSULA 8ª — CONFIDENCIALIDADE",
         """Ambas as partes comprometem-se a manter confidenciais todas as informações trocadas
         no âmbito deste contrato, incluindo dados de clientes, estratégias comerciais e
         credenciais de acesso. Esta obrigação mantém-se por 3 (três) anos após a conclusão
         do contrato."""),

        ("CLÁUSULA 9ª — SUPORTE PÓS-ENTREGA",
         """O suporte técnico após entrega é opcional e cobrado separadamente (€30/mês, sem
         permanência mínima). O suporte inclui: atualizações de conteúdo, pequenas alterações,
         resposta em 24h úteis. Não inclui: redesenho do projeto, novas funcionalidades ou
         alterações estruturais."""),

        ("CLÁUSULA 10ª — RESOLUÇÃO DE CONFLITOS E LEI APLICÁVEL",
         """Em caso de litígio, as partes comprometem-se a resolver a situação amigavelmente
         num prazo de 30 (trinta) dias. Caso não seja possível, o presente contrato rege-se
         pela lei portuguesa e o foro competente é o da comarca do prestador (Porto), com
         expressa renúncia a qualquer outro."""),
    ]

    for titulo, texto in clausulas:
        elems.append(KeepTogether([
            Paragraph(titulo, s['numero_clausula']),
            Paragraph(texto.replace('\n', ' ').replace('         ', ''), s['corpo']),
            Spacer(1, 4),
        ]))

    elems.append(Spacer(1, 16))
    elems.append(linha_divisora())
    elems.append(Paragraph(f"Leça da Palmeira, {DATA_HOJE}", s['centro']))
    elems.append(Spacer(1, 20))
    elems.append(bloco_assinaturas(s))
    return elems

# ─── DOCUMENTO 2 — DECLARAÇÃO DE ÂMBITO (SOW) ─────────────────────────────────
def doc2_sow(s):
    elems = [PageBreak()]
    elems += cabecalho_doc(s, "2", "DECLARAÇÃO DE ÂMBITO",
        "Statement of Work (SOW) · Define o que está e o que não está incluído no projeto")

    elems.append(Paragraph("O QUE É ESTE DOCUMENTO?", s['secao']))
    elems.append(Paragraph(
        """Este documento define com precisão o que o Prestador vai entregar, as fases do projeto,
        os marcos de validação, as responsabilidades de cada parte e o que está fora do âmbito
        contratado. É parte integrante do Contrato de Prestação de Serviços.""", s['corpo']))
    elems.append(Spacer(1, 8))

    # Fases do projeto
    elems.append(Paragraph("FASES DO PROJETO — DA VISÃO À ENTREGA", s['secao']))
    fases = [
        ['Fase', 'Nome', 'O que acontece', 'Responsável', 'Duração'],
        ['1', 'Briefing', 'Reunião/troca de informações: logótipo, cores, textos, dados, fotos, domínio', 'Ambas', '1-3 dias'],
        ['2', 'Configuração\nde Infra', 'Cliente cria conta Hostinger, regista domínio e partilha acesso. Prestador configura servidor e SSL.', 'Cliente + Prestador', '1-2 dias'],
        ['3', 'Desenvolvimento', 'Construção do sistema: backend, base de dados, frontend, funcionalidades acordadas.', 'Prestador', 'Variável por pacote'],
        ['4', 'Revisão\n(1ª ronda)', '1º protótipo funcional enviado ao Cliente. Cliente valida em até 5 dias úteis e lista ajustes.', 'Ambas', '3-5 dias'],
        ['5', 'Ajustes\ne conteúdo', 'Prestador integra conteúdos reais (fotos, textos) e aplica revisões da fase 4.', 'Prestador', '2-4 dias'],
        ['6', 'Revisão\n(2ª ronda)', '2ª validação final. Máximo 2 rondas incluídas. Alterações adicionais são orçamentadas.', 'Ambas', '2-3 dias'],
        ['7', 'Testes\nfinais', 'Testes em mobile, tablet e desktop. Teste de velocidade, RGPD, formulários e funcionalidades.', 'Prestador', '1-2 dias'],
        ['8', 'Entrega\nfinal', 'Deploy no servidor do cliente. Formação de utilização (30-45 min). Entrega de credenciais. Assinatura do TAF.', 'Ambas', '1 dia'],
    ]
    t = Table(fases, colWidths=[1*cm, 2.5*cm, 7*cm, 2.5*cm, 2.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a2e4a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#c0c8d0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f5f7fa')]),
    ]))
    elems.append(t)
    elems.append(Spacer(1, 14))

    # O que está incluído
    elems.append(Paragraph("O QUE ESTÁ INCLUÍDO — PACOTE STANDARD", s['secao']))
    incluido = [
        "✓  Website responsivo (mobile, tablet, desktop)",
        "✓  Domínio e servidor configurados pelo Prestador (conta do Cliente)",
        "✓  SSL/HTTPS — conexão segura desde o primeiro dia",
        "✓  Conformidade RGPD: Política de Privacidade, Cookies e Termos e Condições",
        "✓  Painel de administração para o Cliente gerir conteúdos de forma autónoma",
        "✓  SEO básico: títulos, meta-descrições, Google Search Console",
        "✓  Formulário de contacto funcional",
        "✓  2 rondas de revisão incluídas no preço",
        "✓  Formação de utilização (30-45 minutos)",
        "✓  Entrega de todas as credenciais de acesso",
        "✓  1 mês de suporte pós-entrega incluído (dúvidas de utilização)",
    ]
    for item in incluido:
        elems.append(Paragraph(item, s['lista']))
    elems.append(Spacer(1, 10))

    # O que NÃO está incluído
    elems.append(Paragraph("O QUE NÃO ESTÁ SOB O NOSSO CONTROLO / FORA DO ÂMBITO", s['secao']))
    nao_incluido = [
        "✗  Falhas ou manutenção do servidor da Hostinger (responsabilidade da Hostinger)",
        "✗  Renovação anual do domínio (responsabilidade do Cliente)",
        "✗  Pagamento da fatura mensal do VPS (responsabilidade do Cliente)",
        "✗  Conteúdos fornecidos com erro, desatualizados ou com direitos de terceiros",
        "✗  Novas funcionalidades não acordadas neste âmbito (orçamentadas à parte)",
        "✗  Alterações ao código feitas pelo Cliente ou por terceiros após a entrega",
        "✗  Estratégia de marketing, redes sociais ou publicidade paga (salvo contrato adicional)",
        "✗  Tradução de conteúdos (o Cliente valida as traduções se solicitadas)",
        "✗  Fotografias profissionais ou design de logótipo (o Cliente fornece os ficheiros)",
        "✗  Sistemas externos de terceiros (pagamentos, ERPs, etc.) não especificados",
        "✗  Posicionamento no Google — o SEO demora 3 a 6 meses de resultados orgânicos",
    ]
    for item in nao_incluido:
        elems.append(Paragraph(item, s['lista']))
    elems.append(Spacer(1, 10))

    # Conteúdos necessários do cliente
    elems.append(Paragraph("CONTEÚDOS NECESSÁRIOS DO CLIENTE (para início do projeto)", s['secao']))
    elems.append(Paragraph(
        "O desenvolvimento só pode começar após receção dos seguintes elementos:", s['corpo']))
    conteudos = [
        ['#', 'Item', 'Formato', 'Quem fornece'],
        ['1', 'Logótipo', 'PNG ou SVG, fundo transparente', 'Cliente'],
        ['2', 'Cores e identidade visual', 'Código HEX ou referência visual', 'Cliente'],
        ['3', 'Textos da empresa (quem somos, serviços, etc.)', 'Word / PDF / WhatsApp', 'Cliente'],
        ['4', 'Fotografias (espaço, equipa, produtos)', 'JPG/PNG, mín. 1MB cada', 'Cliente'],
        ['5', 'Dados legais (nome, NIF, morada)', 'Qualquer formato', 'Cliente'],
        ['6', 'Domínio pretendido (ex: mardeprata.pt)', 'Texto', 'Cliente'],
        ['7', 'Conta Hostinger criada', 'Credenciais partilhadas', 'Cliente'],
        ['8', 'Interlocutor disponível para validações', 'Telefone/email', 'Cliente'],
    ]
    t = Table(conteudos, colWidths=[0.8*cm, 7*cm, 5*cm, 3*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a2e4a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#c0c8d0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f5f7fa')]),
    ]))
    elems.append(t)
    elems.append(Spacer(1, 10))

    # Comunicação e validação
    elems.append(Paragraph("COMUNICAÇÃO E PRAZOS DE VALIDAÇÃO", s['secao']))
    elems.append(Paragraph(
        """O Cliente tem até <b>5 (cinco) dias úteis</b> para validar cada fase entregue.
        Após esse prazo sem resposta, considera-se aprovação tácita e o projeto avança.
        Canal de comunicação principal: <b>WhatsApp</b>. Reuniões por videochamada disponíveis
        às quintas-feiras às 15h ou à noite (21h-23h) conforme disponibilidade.""", s['corpo']))

    elems.append(Spacer(1, 16))
    elems.append(linha_divisora())
    elems.append(Paragraph("Ambas as partes declaram ter lido e compreendido a presente Declaração de Âmbito.", s['corpo']))
    elems.append(Spacer(1, 16))
    elems.append(bloco_assinaturas(s))
    return elems

# ─── DOCUMENTO 3 — TERMO DE ACEITE FINAL (TAF) ────────────────────────────────
def doc3_taf(s):
    elems = [PageBreak()]
    elems += cabecalho_doc(s, "3", "TERMO DE ACEITE FINAL (TAF)",
        "Confirmação de entrega e receção — Assinado no momento da entrega do projeto")

    elems.append(Paragraph("O QUE É ESTE DOCUMENTO?", s['secao']))
    elems.append(Paragraph(
        """O Termo de Aceite Final é assinado pelo Cliente no momento da entrega do projeto concluído.
        Confirma que o Cliente recebeu, testou e aprovou o trabalho contratado, que todas as
        credenciais foram entregues e que o pagamento foi efetuado. É o documento que encerra
        formalmente o projeto e activa o suporte pós-entrega.""", s['corpo']))
    elems.append(Spacer(1, 10))

    # Checklist de entrega
    elems.append(Paragraph("CHECKLIST DE ENTREGA", s['secao']))
    checklist = [
        ['', 'Item a verificar na entrega', 'Validado pelo Cliente'],
        ['☐', 'Website/aplicação disponível e acessível no endereço acordado', '_______________'],
        ['☐', 'Todas as páginas e funcionalidades testadas em mobile e desktop', '_______________'],
        ['☐', 'Painel de administração entregue e funcional', '_______________'],
        ['☐', 'Credenciais de acesso ao painel admin entregues', '_______________'],
        ['☐', 'Credenciais do servidor VPS (Hostinger) entregues', '_______________'],
        ['☐', 'Domínio a apontar corretamente para o servidor', '_______________'],
        ['☐', 'SSL/HTTPS activo (cadeado verde no browser)', '_______________'],
        ['☐', 'Formulário de contacto testado e funcional', '_______________'],
        ['☐', 'RGPD: Política de Privacidade, Cookies e Termos visíveis', '_______________'],
        ['☐', 'Formação de utilização realizada (duração: ______ minutos)', '_______________'],
        ['☐', 'Manual de utilização básico entregue (se aplicável)', '_______________'],
        ['☐', 'Funcionalidades específicas do pacote testadas e aprovadas', '_______________'],
        ['☐', 'Pagamento efectuado no valor de € ___________', '_______________'],
    ]
    t = Table(checklist, colWidths=[0.7*cm, 11*cm, 4.3*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a2e4a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#c0c8d0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f5f7fa')]),
    ]))
    elems.append(t)
    elems.append(Spacer(1, 14))

    # Declaração de aceitação
    elems.append(Paragraph("DECLARAÇÃO DE ACEITAÇÃO", s['secao']))
    elems.append(Paragraph(
        """Eu, abaixo assinado, na qualidade de Cliente, declaro que:""", s['corpo']))
    declaracoes = [
        "1. Recebi e testei o projeto conforme descrito no Contrato de Prestação de Serviços e na Declaração de Âmbito;",
        "2. O trabalho entregue corresponde ao que foi acordado e contratado;",
        "3. Recebi todas as credenciais de acesso necessárias para gerir o sistema de forma autónoma;",
        "4. Fui informado e compreendi os limites do âmbito contratado e o que está fora do mesmo;",
        "5. Efectuei o pagamento integral do valor acordado;",
        "6. A partir desta data, quaisquer alterações adicionais ao projeto serão orçamentadas separadamente;",
        "7. O suporte pós-entrega (se contratado) inicia-se nesta data.",
    ]
    for d in declaracoes:
        elems.append(Paragraph(d, s['lista']))
    elems.append(Spacer(1, 10))

    # Observações
    elems.append(Paragraph("OBSERVAÇÕES / RESSALVAS DO CLIENTE (se aplicável):", s['secao']))
    elems.append(Spacer(1, 6))
    linhas_obs = Table([['']], colWidths=[W-2*MARGEM], rowHeights=[2.5*cm])
    linhas_obs.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#c0c8d0')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fafbfc')),
    ]))
    elems.append(linhas_obs)
    elems.append(Spacer(1, 16))
    elems.append(linha_divisora())
    elems.append(Paragraph(f"Local e data de entrega: _________________________ , _____ / _____ / _______", s['corpo']))
    elems.append(Spacer(1, 20))
    elems.append(bloco_assinaturas(s))
    elems.append(Spacer(1, 20))
    elems.append(Paragraph(
        "⚠️  Este documento deve ser assinado em 2 (dois) exemplares — um para cada parte.",
        s['aviso']))
    return elems

# ─── NUMERAÇÃO DE PÁGINAS ──────────────────────────────────────────────────────
class NumeracaoPaginas:
    def __init__(self):
        self.paginas = []

    def __call__(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.grey)
        canvas.drawString(MARGEM, 1.2*cm,
            f"SolutionSoftware · {PRESTADOR['email']} · {PRESTADOR['telefone']}")
        canvas.drawRightString(W - MARGEM, 1.2*cm, f"Página {doc.page}")
        canvas.restoreState()

# ─── MAIN ───────────────────────────────────────────────────────────────────────
def gerar():
    s = build_styles()
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
        leftMargin=MARGEM, rightMargin=MARGEM,
        topMargin=2*cm, bottomMargin=2*cm,
        title="SolutionSoftware — Contratos",
        author="SolutionSoftware",
        subject="Documentos Contratuais")

    numeracao = NumeracaoPaginas()
    story = []

    # Capa
    story.append(Spacer(1, 3*cm))
    capa = Table([[Paragraph("TOLEDO DIGITAL", ParagraphStyle('cap',
        fontSize=28, textColor=colors.white, fontName='Helvetica-Bold',
        alignment=TA_CENTER))],
        [Paragraph("Desenvolvimento Web & Aplicações", ParagraphStyle('cap2',
        fontSize=14, textColor=colors.HexColor('#a8c0e0'), fontName='Helvetica',
        alignment=TA_CENTER))]],
        colWidths=[W - 2*MARGEM])
    capa.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1a2e4a')),
        ('TOPPADDING', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(capa)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("DOCUMENTOS CONTRATUAIS", ParagraphStyle('s',
        fontSize=18, textColor=colors.HexColor('#1a2e4a'), fontName='Helvetica-Bold',
        alignment=TA_CENTER)))
    story.append(Spacer(1, 0.4*cm))
    story.append(linha_divisora())
    story.append(Spacer(1, 0.4*cm))

    indice = [
        ['Documento 1', 'Contrato de Prestação de Serviços', '→ p.2'],
        ['Documento 2', 'Declaração de Âmbito (SOW — Statement of Work)', '→ p.X'],
        ['Documento 3', 'Termo de Aceite Final (TAF)', '→ p.X'],
    ]
    t = Table(indice, colWidths=[3*cm, 11*cm, 2*cm])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('TEXTCOLOR', (0,0), (0,-1), colors.HexColor('#4a6fa5')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LINEBELOW', (0,0), (-1,-2), 0.5, colors.HexColor('#e0e0e0')),
    ]))
    story.append(t)
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph(
        f"Versão 1.0 · {DATA_HOJE} · Documento de uso interno SolutionSoftware",
        ParagraphStyle('r', fontSize=9, textColor=colors.grey, alignment=TA_CENTER)))
    story.append(PageBreak())

    # Documentos
    story += doc1_contrato(s)
    story += doc2_sow(s)
    story += doc3_taf(s)

    doc.build(story, onFirstPage=numeracao, onLaterPages=numeracao)
    print(f"✅ PDF gerado: {OUTPUT}")

if __name__ == '__main__':
    gerar()
