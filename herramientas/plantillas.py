# Plantillas de Banderín para Instagram (posts 1080x1350 y portadas/historias 1080x1920).
# Uso:
#   from plantillas import *
#   S = {'1-post-algo': (feature('Kicker', 'Título', 'Texto', 'ombu-inicio.png'), 1350)}
#   render(S, 'tanda-05')
# Requiere: pip install playwright (Chromium ya instalado en el entorno).
import pathlib
from playwright.sync_api import sync_playwright

AQUI = pathlib.Path(__file__).parent
CAP = AQUI / 'capturas'
F = AQUI / 'fuentes'

FONTS = '\n'.join(
    [f"@font-face{{font-family:'Barlow Condensed';font-style:{st};font-weight:{w};src:url('file://{F}/barlow-condensed-latin-{w}-{st}.woff2')}}" for w in (600, 700, 800) for st in ('normal', 'italic')]
    + [f"@font-face{{font-family:'Figtree';font-weight:{w};src:url('file://{F}/figtree-latin-{w}-normal.woff2')}}" for w in (400, 500, 600, 700, 800)]
)

# Paleta de la marca
INK, GREEN, YELLOW, CHALK, SLATE, BLUE = '#121A24', '#1F8A4C', '#F2C230', '#F6F7F4', '#4A5560', '#1D4E9E'


def pennant(size, bar=INK, body=GREEN, band=YELLOW, cord=True):
    c = f'<path d="M30 6 L50 0 L70 6" fill="none" stroke="{bar}" stroke-width="3" stroke-linecap="round"/>' if cord else ''
    return (f'<svg width="{size}" height="{int(size*1.2)}" viewBox="0 0 100 120" aria-hidden="true">{c}'
            f'<rect x="4" y="6" width="92" height="9" rx="4.5" fill="{bar}"/>'
            f'<polygon points="11,15 89,15 50,116" fill="{body}"/>'
            f'<polygon points="11,15 89,15 81.3,35 18.7,35" fill="{band}"/>'
            f'<circle cx="50" cy="60" r="11" fill="#fff"/></svg>')


def phone(img, w=560, extra=''):
    """img: nombre de un archivo de herramientas/capturas/ (captura de la demo, 1170x2532)."""
    return f'<div class="phone" style="width:{w}px;{extra}"><img src="file://{CAP / img}" style="width:100%;display:block;border-radius:{int(w*0.075)}px"></div>'


def page(body, w=1080, h=1350, bg=CHALK, color=INK):
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{FONTS}
*{{box-sizing:border-box}} body{{margin:0}}
.s{{width:{w}px;height:{h}px;position:relative;overflow:hidden;background:{bg};color:{color};font-family:Figtree,sans-serif}}
.d{{font-family:'Barlow Condensed',sans-serif;font-style:italic;font-weight:800;line-height:1.02;letter-spacing:-.5px;margin:0}}
.k{{font-weight:800;font-size:26px;letter-spacing:2px;text-transform:uppercase}}
.p{{font-size:34px;line-height:1.4;margin:0}}
.phone{{padding:14px;background:{INK};border-radius:58px;box-shadow:0 30px 80px rgba(18,26,36,.35)}}
.sig{{position:absolute;display:flex;align-items:center;gap:12px;font-family:'Barlow Condensed',sans-serif;font-style:italic;font-weight:800;font-size:38px}}
.hl{{background:{YELLOW};color:{INK};padding:0 12px;-webkit-box-decoration-break:clone;box-decoration-break:clone;line-height:1.1}}
</style></head><body><div class="s">{body}</div></body></html>'''


def firma(color=INK, bar=INK, pos='top:56px;right:64px'):
    return f'<div class="sig" style="{pos};color:{color}">{pennant(34, bar=bar, cord=False)}Banderín</div>'


def feature(kicker, titulo, texto, img, fondo=CHALK, tinta=INK, acento=GREEN, cta=None):
    """Lámina de carrusel o post: kicker + título + texto + celular centrado abajo."""
    cta_html = f'<p class="p" style="margin-top:22px;font-weight:700;color:{acento}">{cta}</p>' if cta else ''
    return page(f'''
{firma(tinta, tinta)}
<div style="position:absolute;left:72px;top:150px;right:72px">
  <div class="k" style="color:{acento}">{kicker}</div>
  <h1 class="d" style="font-size:104px;margin-top:18px">{titulo}</h1>
  <p class="p" style="margin-top:24px;max-width:860px;color:{tinta};opacity:.85">{texto}</p>{cta_html}
</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:{'720' if cta else '660'}px">{phone(img, 540)}</div>''', bg=fondo, color=tinta)


def portada(kicker, titulo, texto, img, fondo=INK, tinta='#fff', acento=YELLOW, h=1350):
    """Portada de carrusel (h=1350) o de reel/historia (h=1920), con celular inclinado."""
    return page(f'''
{firma(tinta, '#fff')}
<div style="position:absolute;left:72px;top:{'170' if h == 1350 else '360'}px;right:72px">
  <div class="k" style="color:{acento}">{kicker}</div>
  <h1 class="d" style="font-size:{'124' if h == 1350 else '140'}px;margin-top:20px;color:{tinta}">{titulo}</h1>
  <p class="p" style="margin-top:26px;max-width:880px;color:#E6EBEF">{texto}</p>
</div>
<div style="position:absolute;left:50%;transform:translateX(-50%) rotate(-4deg);top:{'760' if h == 1350 else '1040'}px">{phone(img, 560)}</div>''', h=h, bg=fondo, color=tinta)


def frase(titulo, texto='', fondo=CHALK, tinta=INK, acento=GREEN, cta=None):
    """Post solo de texto (pregunta, dato, frase de profe), sin celular, con banderín grande."""
    cta_html = f'<p class="p" style="margin-top:22px;font-weight:800;color:{acento}">{cta}</p>' if cta else ''
    return page(f'''
{firma(tinta, tinta)}
<div style="position:absolute;left:72px;top:220px;right:72px">
  <h1 class="d" style="font-size:140px">{titulo}</h1>
  <p class="p" style="margin-top:34px;max-width:860px;color:{tinta};opacity:.8">{texto}</p>{cta_html}
</div>
<div style="position:absolute;right:90px;bottom:90px">{pennant(260, bar=tinta)}</div>
<div style="position:absolute;left:72px;bottom:110px;font-size:30px;font-weight:700;opacity:.7">@banderin.app</div>''', bg=fondo, color=tinta)


def render(laminas, carpeta):
    """laminas: {nombre: (html, alto)}. Guarda <carpeta>/<nombre>.png (ruta relativa a la raíz del repo)."""
    out = AQUI.parent / carpeta
    out.mkdir(parents=True, exist_ok=True)
    tmp = AQUI / '_tmp.html'
    with sync_playwright() as p:
        b = p.chromium.launch()
        for nombre, (html, h) in laminas.items():
            tmp.write_text(html)
            pg = b.new_page(viewport={'width': 1080, 'height': h})
            pg.goto(f'file://{tmp}')
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(out / f'{nombre}.png'))
            pg.close()
        b.close()
    tmp.unlink(missing_ok=True)
    return sorted(out.glob('*.png'))
