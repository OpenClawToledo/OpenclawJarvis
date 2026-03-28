#!/usr/bin/env python3
"""Gera card do padrão Porta-Copos Tartaruga em PT-BR estilo Pinterest."""

from PIL import Image, ImageDraw, ImageFont
import textwrap, os

# ── Cores ──────────────────────────────────────
BG        = (253, 248, 242)   # cream
DARK      = (61,  32,  16)    # castanho escuro
ROSE      = (139, 74,  68)    # dusty rose
GOLD      = (196, 149, 106)   # dourado
WHITE     = (255, 255, 255)
LIGHT     = (232, 213, 190)   # lace

W, H = 900, 1200
img = Image.new("RGB", (W, H), BG)
d   = ImageDraw.Draw(img)

# ── Fontes (usa padrão do sistema) ─────────────
def font(size, bold=False):
    paths = [
        "/home/linuxbrew/.linuxbrew/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else
        "/home/linuxbrew/.linuxbrew/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

f_title  = font(52, bold=True)
f_sub    = font(32, bold=True)
f_body   = font(26)
f_small  = font(22)
f_badge  = font(20, bold=True)

# ── Borda decorativa ───────────────────────────
for i in range(3):
    d.rectangle([i*4, i*4, W-i*4-1, H-i*4-1], outline=LIGHT, width=2)

# ── Cabeçalho ──────────────────────────────────
d.rectangle([0, 0, W, 130], fill=ROSE)
d.text((W//2, 42), "🐢 Porta-Copos Tartaruga", font=f_title, fill=WHITE, anchor="mt")
d.text((W//2, 100), "Padrão de Crochê  •  Fios MJ", font=f_small, fill=LIGHT, anchor="mt")

# ── Linha dourada ──────────────────────────────
d.rectangle([40, 140, W-40, 144], fill=GOLD)

y = 165

def section(title, lines):
    global y
    # Fundo da secção
    d.rectangle([30, y-4, W-30, y+42], fill=ROSE, outline=ROSE)
    d.text((50, y+4), title, font=f_sub, fill=WHITE)
    y += 52
    for line in lines:
        d.text((60, y), line, font=f_body, fill=DARK)
        y += 34
    y += 10

section("🐚 Carapaça  (alças traseiras)", [
    "R1: Anel mágico, 11 F",
    "R2: (FV) × 11",
    "R3: (F, FV) × 11",
    "R4: (F, FV, F) × 11",
    "R5: 44 pb — ponto de caranguejo",
])

section("🐢 Cabeça  (Ponto Cruz)", [
    "R1: Anel mágico, 6 pb",
    "R2: 6 aum (12)   R3: (pb, aum) × 6 (18)",
    "R4: (pb, aum, pb) × 6 (24)   R5–7: 24 pb",
    "R8: (pb, dim, pb) × 6",
    "R9: (pb, dim) × 6  — Rechear",
    "R10–13: 12 pb",
    "R14–15: Dobrar e 6 pb pelas duas camadas",
])

section("🌀 Rabo", [
    "R1: Anel mágico, 4 pb",
    "R2: (pb, aum) × 2 (6)   R3: (pb, aum) × 3 (9)",
    "R4: 9 pb",
])

section("🦾 Braços  (× 2)", [
    "R1: Anel mágico, 6 pb   R2: 6 aum (12)",
    "R3: (pb, aum) × 6 (18)",
    "Dobrar e 9 pb pelas duas camadas",
])

section("🦵 Pernas  (× 2)", [
    "R1: Anel mágico, 6 pb   R2: 6 aum (12)",
    "Dobrar e 6 pb pelas duas camadas",
])

# ── Rodapé abreviações ─────────────────────────
d.rectangle([0, H-110, W, H], fill=DARK)
d.text((W//2, H-95), "ABREVIAÇÕES", font=f_badge, fill=GOLD, anchor="lt")

abbr = "pb = ponto baixo  |  aum = aumento  |  dim = diminuição  |  F = ponto cruz  |  FV = ponto cruz c/ aumento"
for i, line in enumerate(textwrap.wrap(abbr, 70)):
    d.text((W//2, H-70 + i*24), line, font=f_small, fill=LIGHT, anchor="mt")

# ── Rodapé Fios MJ ────────────────────────────
d.rectangle([0, H-28, W, H], fill=ROSE)
d.text((W//2, H-22), "fiosmj.com  •  @fiosmjcroche", font=font(18), fill=WHITE, anchor="mt")

# ── Guardar ────────────────────────────────────
out = "/data/.openclaw/workspace/fiosmj-app/uploads/porta-copos-tartaruga-ptbr.jpg"
img.save(out, "JPEG", quality=95)
print(f"Guardado: {out}")
