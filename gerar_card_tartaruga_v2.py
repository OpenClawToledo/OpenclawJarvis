#!/usr/bin/env python3
"""
Recria o card Turtle Coaster em PT-BR, fiel ao original.
Abre a imagem original, extrai o card (sem chrome do Pinterest),
pinta sobre o texto em inglês e redesenha em português.
"""
from PIL import Image, ImageDraw, ImageFont
import os

SRC  = '/data/.openclaw/media/inbound/b17b7d7b-afb4-47ec-a8d2-8e927ec4c771.jpg'
OUT  = '/data/.openclaw/workspace/fiosmj-app/uploads/porta-copos-tartaruga-ptbr.jpg'

# Cores extraídas do original
BG    = (245, 240, 232)   # creme/bege
DARK  = (59,  47,  47)    # castanho escuro
LINE  = (180, 160, 130)   # linha bege-acastanhada

# ── Abrir original e cortar só o card (sem UI do Pinterest) ──
orig = Image.open(SRC).convert('RGB')
W, H = orig.size   # 720 × 1612

# O card começa ~y=225 (depois do header Pinterest) e vai até ~y=1260
card = orig.crop((0, 225, W, 1260))
CW, CH = card.size   # 720 × 1035

img = card.copy()
d   = ImageDraw.Draw(img)

# ── Cobrir TODA a zona de texto com o BG (preserva só a foto da tartaruga) ──
# Foto da tartaruga está à direita, ~x:340 a x:710, y:50 a y:460
# Cobrir zona esquerda (título + texto geral) e zona inferior
d.rectangle([0,   0,  340, CH], fill=BG)   # coluna esquerda
d.rectangle([0, 460, CW,  CH], fill=BG)   # tudo abaixo da foto

# ── Fontes ──────────────────────────────────────────────────
def fnt(size, bold=False):
    candidates = [
        f"/home/linuxbrew/.linuxbrew/share/fonts/truetype/liberation/LiberationSerif-{'Bold' if bold else 'Regular'}.ttf",
        f"/usr/share/fonts/truetype/liberation/LiberationSerif-{'Bold' if bold else 'Regular'}.ttf",
        f"/home/linuxbrew/.linuxbrew/share/fonts/truetype/dejavu/DejaVuSerif{'-Bold' if bold else ''}.ttf",
        f"/usr/share/fonts/truetype/dejavu/DejaVuSerif{'-Bold' if bold else ''}.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

f_title  = fnt(44, bold=True)
f_title2 = fnt(28, bold=False)
f_section= fnt(20, bold=True)
f_note   = fnt(15, bold=False)
f_body   = fnt(14, bold=False)

# ── TÍTULO (canto superior esquerdo) ────────────────────────
d.text((22,  18), "Porta-Copos",    font=f_title,  fill=DARK)
d.text((22,  70), "Tartaruga",      font=f_title,  fill=DARK)
d.text((22, 122), "Padrão de Crochê", font=f_title2, fill=DARK)

# ── Função para secção ──────────────────────────────────────
def section(x, y, title, note, lines):
    """Desenha cabeçalho + lista de passos."""
    # mini tartaruga + linha
    d.text((x, y), "🐢", font=f_note, fill=DARK)
    lx = x + 26
    d.line([(lx, y+10), (lx+280, y+10)], fill=LINE, width=1)
    y += 18
    d.text((x, y), title, font=f_section, fill=DARK)
    if note:
        d.text((x+len(title)*11, y+3), f"  {note}", font=f_note, fill=DARK)
    y += 24
    for line in lines:
        d.text((x+8, y), f"• {line}", font=f_body, fill=DARK)
        y += 18
    return y + 8

# ── CARAPAÇA (esquerda, abaixo do título) ───────────────────
y = section(14, 165,
    "Carapaça", "(Somente alças traseiras)",
    [
        "R1: Anel mágico, 11 F",
        "R2: (FV) × 11",
        "R3: (F, FV) × 11",
        "R4: (F, FV, F) × 11",
        "R5: 44 pb — ponto de caranguejo",
        "     (ponto reverso)",
    ])

# ── CABEÇA (esquerda) ───────────────────────────────────────
y = section(14, y,
    "Cabeça", "(Ponto Cruz Simples)",
    [
        "R1: Anel mágico, 6 pb",
        "R2: 6 aum (12)",
        "R3: (pb, aum) ×6 (18)",
        "R4: (pb, aum, pb) ×6 (24)",
        "R5–7: 24 pb",
        "R8: (pb, dim, pb) ×6",
        "R9: (pb, dim) ×6 — Rechear",
        "R10–13: 12 pb",
        "R14–15: Dobrar e 6 pb",
        "         pelas duas camadas",
    ])

# ── RABO (esquerda) ─────────────────────────────────────────
y = section(14, y,
    "Rabo", "",
    [
        "R1: Anel mágico, 4 pb",
        "R2: (pb, aum) ×2 (6)",
        "R3: (pb, aum) ×3 (9)",
        "R4: 9 pb",
    ])

# ── BRAÇOS (direita) ────────────────────────────────────────
yr = section(370, 460,
    "Braços", "(Fazer 2)",
    [
        "R1: Anel mágico, 6 pb",
        "R2: 6 aum (12)",
        "R3: (pb, aum) ×6 (18)",
        "Dobrar e 9 pb pelas",
        "duas camadas",
    ])

# ── PERNAS (direita) ────────────────────────────────────────
yr = section(370, yr,
    "Pernas", "(Fazer 2)",
    [
        "R1: Anel mágico, 6 pb",
        "R2: 6 aum (12)",
        "R3: Dobrar e 6 pb pelas",
        "     duas camadas",
    ])

# ── ABREVIAÇÕES (direita) ───────────────────────────────────
section(370, yr,
    "Abreviações:", "",
    [
        "pb = ponto baixo",
        "aum = aumento",
        "dim = diminuição",
        "F = ponto cruz simples",
        "FV = ponto cruz c/ aumento",
    ])

# ── Guardar ─────────────────────────────────────────────────
img.save(OUT, "JPEG", quality=96)
print(f"Guardado: {OUT}  ({CW}×{CH}px)")
