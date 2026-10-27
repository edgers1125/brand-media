import pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path("/tmp/claude-0/-home-claude/d9907e7c-962a-55f1-92fd-0136ee14e247/scratchpad/staging")
FOREST, NAVY, NAVYD, GREEN, SAGE, TINT, CREAM, INK, SLATE, RED = (
    "#445C44", "#033F75", "#022A4F", "#7AB537", "#527354", "#E9EFE6", "#FFFDF8", "#1B161F", "#5A6470", "#C62828")

def peso(v):
    s = f"{v:,.2f}"
    return "₱" + (s[:-3] if s.endswith(".00") else s)

def pct(old, new):
    return round((1 - new / old) * 100)

PUBS = [
 dict(slug="2026-10-28-medmura-max-katinko", l1="KATINKO", l2="FAVORITES",
      sub="Ginhawa sa presyong #MedMura.", layout="rows", scheme="forest", burst=("UP TO","35%","OFF"),
      items=[("Katinko Liniment Oil", "Peppermint · 35ml", 210, 168),
             ("Katinko Liniment Oil", "Ginger + Patchouli · 35ml", 210, 168),
             ("Katinko Ointment", "Peppermint · 10g", 95, 61.75),
             ("Katinko Ointment", "Ginger + Patchouli · 10g", 95, 61.75),
             ("Katinko Ointment", "Soft White · 10g", 60, 48)]),
 dict(slug="2026-10-30-medmura-max-vitamins-otc", l1="VITAMINS", l2="& OTC PICKS",
      sub="Everyday health, month-end prices.", layout="grid2", scheme="cream", burst=("UP TO","40%","OFF"),
      items=[("Tiki Tiki Multivitamin Drops", "15ml bottle", 85, 51),
             ("Omega-3 Fish Oil", "1000mg · per capsule", 12, 7.20),
             ("Flotera Probiotic", "L. reuteri · per tablet", 28, 21),
             ("Welltrate Butamirate", "50mg · per tablet", 18, 15.30),
             ("Mucomed Diphenhydramine", "25mg · per capsule", 3, 1.95),
             None]),
 dict(slug="2026-11-02-medmura-max-clinic-supplies", l1="CLINIC", l2="SUPPLIES",
      sub="Stock up the clinic for less.", layout="grid3", scheme="navy", burst=("UP TO","35%","OFF"),
      items=[("Prohealth Auto-Disable Syringe", "0.5ml", 1324, 860.60),
             ("Simplex Auto-Disable Syringe", "0.5ml · G23 x 1in", 8, 6.40),
             ("Terumo Hypodermic Needle", "G23", 7, 5.60),
             ("Improve Multi-Sample Needle", "G22 x 1 1/2in · box of 100", 1162, 929.60),
             ("Sterilab Sodium Citrate Tube", "Blue top · 1.8ml", 10, 8),
             ("Sinocare Alcohol Pad", "per pad", 4, 2.60)]),
 dict(slug="2026-11-05-medmura-max-diagnostics-or", l1="TEST STRIPS", l2="& OR ESSENTIALS",
      sub="For home checks and the operating room.", layout="grid2big", scheme="white", burst=("UP TO","35%","OFF"),
      items=[("Easy Touch Glucose Test Strips", "25 strips", 1036, 880.60),
             ("Surgitech Urine Test Strips", "10 parameters", 1036, 777),
             ("Partners Lap Sponge", "12 x 12 · with X-ray line", 65, 42.25),
             ("Partners Endotracheal Tube", "2.0mm · uncuffed", 82, 53.30)]),
 dict(slug="2026-11-09-medmura-max-for-clinics", l1="FOR CLINICS", l2="& HOSPITALS",
      sub="Rx medicines at MedMura MAX wholesale rates.", layout="rx", scheme="tint", burst=("WHOLE","SALE","RATES"),
      items=[("Amoxicillin 500mg", "RiteMED · capsule"),
             ("Ciprofloxacin 500mg", "Cyfrox · tablet"),
             ("Losartan + HCTZ 100mg/25mg", "RiteMED · tablet"),
             ("Metformin 500mg", "RiteMED · tablet"),
             ("Atenolol 100mg", "Zenobloc · tablet"),
             ("Simvastatin 20mg", "RiteMED · tablet"),
             ("Domperidone 1mg/mL", "Accedome · 60ml suspension"),
             ("Salmeterol + Fluticasone", "Kovent SF · inhaler"),
             ("Tranexamic Acid 500mg", "Hemobas · injection"),
             ("Hyoscine Butylbromide 20mg/mL", "Hyosaph · injection")]),
]

SCHEMES = {
 # bg, logo, kicker colour, title l1, title l2, band(bg,text), card(bg,ink,muted), footer(bg,text)
 "forest": dict(bg="#fff", logo="white", t1="#fff", t2="#fff", rule=GREEN, card=TINT, cink=INK, cmut=SLATE, cnew=FOREST, foot=NAVY, sub="#E9EFE6"),
 "cream":  dict(bg="#fff", logo="color", t1=INK, t2=NAVY, rule=GREEN, card=NAVY, cink="#fff", cmut="#C9D6E3", cnew=GREEN, foot=FOREST, sub=SLATE),
 "navy":   dict(bg="#fff", logo="color", t1=INK, t2=NAVY, rule=GREEN, card=FOREST, cink="#fff", cmut="#D7E3D5", cnew="#fff", foot=NAVY, sub=SLATE),
 "white":  dict(bg="#fff", logo="color", t1=INK, t2=SAGE, rule=GREEN, card="#F3F5F1", cink=INK, cmut=SLATE, cnew=NAVY, foot=FOREST, sub=SLATE),
 "tint":   dict(bg="#F3F5F1", logo="color", t1=INK, t2=FOREST, rule=GREEN, card="#fff", cink=INK, cmut=SLATE, cnew=FOREST, foot=FOREST, sub=SLATE),
}

HEAD = """<!doctype html><html><head><meta charset="utf-8"><title>MedSource post</title><style>
@font-face{font-family:Poppins;font-weight:400;src:url(../../../brand/fonts/poppins/Poppins-Regular.ttf)}
@font-face{font-family:Poppins;font-weight:500;src:url(../../../brand/fonts/poppins/Poppins-Medium.ttf)}
@font-face{font-family:Poppins;font-weight:600;src:url(../../../brand/fonts/poppins/Poppins-SemiBold.ttf)}
@font-face{font-family:Poppins;font-weight:700;src:url(../../../brand/fonts/poppins/Poppins-Bold.ttf)}
@font-face{font-family:Poppins;font-weight:800;src:url(../../../brand/fonts/poppins/Poppins-ExtraBold.ttf)}
@font-face{font-family:Poppins;font-weight:900;src:url(../../../brand/fonts/poppins/Poppins-Black.ttf)}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:Poppins,sans-serif;overflow:hidden;width:1080px;height:%dpx}
.root{width:1080px;height:%dpx;display:flex;flex-direction:column;background:%s}
.old{text-decoration:line-through;text-decoration-thickness:3px}
.off{background:%s;color:#fff;font-weight:800;border-radius:8px;display:inline-block}
</style></head><body><div class="root">"""

def badge(s, big):
    f = 40 if big else 34
    dark = s["bg"] in (FOREST, NAVYD)
    c1 = "#fff" if dark else NAVY
    return (f'<div style="display:flex;align-items:center;gap:8px;font-weight:700;font-size:{f}px;line-height:1">'
            f'<span style="color:{c1}">#Med</span>'
            f'<span style="background:{GREEN};color:#fff;border-radius:9999px;padding:6px 20px 10px">Mura</span>'
            f'<span style="color:{c1};letter-spacing:.04em">MAX</span></div>')

def card(item, s, size, story):
    if item is None:
        return f'<div style="border-radius:16px;border:3px dashed {s["rule"]};display:flex;align-items:center;justify-content:center;text-align:center;padding:20px;color:{s["t2"]};font-weight:700;font-size:{30 if story else 26}px;line-height:1.25">Plus more<br>in store!</div>'
    n, d, old, new = item
    p = pct(old, new)
    k = {"rows": 1.0, "grid2": 1.0, "grid3": 0.86, "grid2big": 1.15}[size] * (1.12 if story else 1)
    return (f'<div style="background:{s["card"]};border-radius:16px;padding:{int(22*k)}px {int(26*k)}px;display:flex;flex-direction:column;justify-content:space-between;position:relative">'
            f'<span class="off" style="position:absolute;top:{int(18*k)}px;right:{int(18*k)}px;font-size:{int(28*k)}px;padding:2px 14px">-{p}%</span>'
            f'<div style="padding-right:{int(90*k)}px"><div style="font-weight:700;font-size:{int(28*k)}px;line-height:1.2;color:{s["cink"]}">{n}</div>'
            f'<div style="font-size:{int(20*k)}px;color:{s["cmut"]};margin-top:4px">{d}</div></div>'
            f'<div style="display:flex;align-items:baseline;gap:14px;margin-top:{int(10*k)}px"><span style="font-weight:700;font-size:{int(54*k)}px;color:{s["cnew"]};line-height:1">{peso(new)}</span>'
            f'<span class="old" style="font-size:{int(22*k)}px;color:{s["cmut"]}">{peso(old)}</span></div></div>')

def row(item, s, story):
    n, d, old, new = item
    k = 1.15 if story else 1
    return (f'<div style="background:{s["card"]};border-radius:16px;padding:{int(18*k)}px {int(28*k)}px;display:flex;align-items:center;gap:20px">'
            f'<div style="flex:1"><div style="font-weight:700;font-size:{int(30*k)}px;line-height:1.15;color:{s["cink"]}">{n}</div>'
            f'<div style="font-size:{int(21*k)}px;color:{s["cmut"]}">{d}</div></div>'
            f'<span class="off" style="font-size:{int(28*k)}px;padding:2px 14px">-{pct(old,new)}%</span>'
            f'<div style="text-align:right;min-width:{int(190*k)}px"><div class="old" style="font-size:{int(21*k)}px;color:{s["cmut"]}">{peso(old)}</div>'
            f'<div style="font-weight:700;font-size:{int(52*k)}px;color:{s["cnew"]};line-height:1">{peso(new)}</div></div></div>')

def rxrow(item, s, story):
    n, d = item
    k = 1.12 if story else 1
    return (f'<div style="background:#fff;border-radius:12px;padding:{int(12*k)}px {int(20*k)}px;display:flex;flex-direction:column;justify-content:center">'
            f'<div style="font-weight:700;font-size:{int(25*k)}px;line-height:1.2;color:{INK}">{n}</div>'
            f'<div style="font-size:{int(19*k)}px;color:{SLATE}">{d}</div></div>')

def build(pub, story):
    s = SCHEMES[pub["scheme"]]
    H = 1920 if story else 1350
    top = 120 if story else 56
    logo = "medsource-landscape-white.svg" if s["logo"] == "white" else "medsource-landscape.svg"
    h = [HEAD % (H, H, s["bg"], RED)]
    # MAX hero, house structure: white top, forest band, double green stripe, navy label bar
    k = 1.18 if story else 1
    a, bb, c = pub["burst"]
    small = len(bb) > 3
    h.append(f'<div style="background:#fff;padding:{top}px 64px {int(18*k)}px;display:flex;justify-content:space-between;align-items:center">'
             f'<img src="../../../brand/logos/medsource/medsource-landscape.svg" style="height:{int(84*k)}px">'
             f'<div style="display:flex;align-items:center;gap:{int(16*k)}px">'
             f'<div style="border:3px solid {GREEN};color:{NAVY};font-weight:700;font-size:{int(22*k)}px;letter-spacing:.2em;padding:6px 18px;border-radius:6px">MONTH-END SALE</div>'
             f'</div></div>'

             f'<div style="height:{int(8*k)}px;background:{GREEN}"></div><div style="height:{int(6*k)}px;background:#fff"></div>'
             f'<div style="background:{NAVY};padding:{int(18*k)}px 64px {int(22*k)}px;display:flex;justify-content:space-between;align-items:center"><div>'
             f'<div style="color:#fff;font-weight:800;font-size:{int(54*k)}px;line-height:1;letter-spacing:-.01em">#Med<span style="color:{GREEN}">Mura</span></div>'
             f'<div style="display:flex;align-items:center;gap:{int(18*k)}px;margin-top:{int(2*k)}px">'
             f'<span style="color:{GREEN};font-weight:900;font-size:{int(150*k)}px;line-height:.86;letter-spacing:-.04em">MAX</span>'
             f'<span style="color:#AFD176;font-weight:900;font-size:{int(84*k)}px;line-height:.8;letter-spacing:-.06em">&#8250;&#8250;&#8250;</span></div></div>'
             f'<div style="width:{int(210*k)}px;height:{int(210*k)}px;border-radius:50%;background:{RED};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1;flex:none;box-shadow:0 0 0 {int(7*k)}px {NAVY},0 0 0 {int(11*k)}px {RED}">'
             f'<div style="font-weight:700;font-size:{int(22*k)}px">{a}</div><div style="font-weight:800;font-size:{int((52 if small else 70)*k)}px;margin:4px 0;letter-spacing:-.02em">{bb}</div><div style="font-weight:700;font-size:{int(22*k)}px">{c}</div></div></div>'
             f'<div style="height:{int(6*k)}px;background:#fff"></div><div style="height:{int(8*k)}px;background:{GREEN}"></div>'
             f'<div style="background:{FOREST};padding:{int(10*k)}px 64px"><span style="color:#fff;font-weight:700;font-size:{int(32*k)}px;letter-spacing:.06em">{pub["l1"]} {pub["l2"]}</span></div>')
    # items
    gap = 22 if story else 16
    L = pub["layout"]
    body = f'<div style="flex:1;padding:{48 if story else 16}px 64px {40 if story else 14}px;display:'
    if L == "rows":
        body += f'flex;flex-direction:column;gap:{gap}px;justify-content:center">' + "".join(row(i, s, story) for i in pub["items"])
    elif L == "grid2":
        body += f'grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:{gap}px">' + "".join(card(i, s, "grid2", story) for i in pub["items"])
    elif L == "grid3":
        cols = "1fr 1fr" if story else "1fr 1fr 1fr"
        body += f'grid;grid-template-columns:{cols};grid-auto-rows:1fr;gap:{gap}px">' + "".join(card(i, s, "grid3", story) for i in pub["items"])
    elif L == "grid2big":
        cols = "1fr 1fr"
        body += f'grid;grid-template-columns:{cols};grid-auto-rows:1fr;gap:{gap}px">' + "".join(card(i, s, "grid2big", story) for i in pub["items"])
    elif L == "rx":
        body += (f'flex;flex-direction:column;gap:{gap}px"><div style="display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:{12 if not story else 16}px;flex:1">'
                 + "".join(rxrow(i, s, story) for i in pub["items"]) + '</div>'
                 f'<div style="background:{NAVY};color:#fff;border-radius:16px;padding:{26 if story else 20}px 28px;font-size:{30 if story else 26}px;line-height:1.3">'
                 f'<b>Clinics, hospitals and pharmacies:</b> message us for MedMura MAX wholesale rates.'
                 f'<div style="font-size:{22 if story else 19}px;color:#C9D6E3;margin-top:6px">Prescription medicines are dispensed with a valid prescription.</div></div>')
    body += '</div>'
    h.append(body)
    # footer
    fine = "Promo valid while stocks last." if L != "rx" else "Limited stocks only."
    h.append(f'<div style="height:10px;background:{GREEN}"></div>'
             f'<div style="background:{s["foot"]};color:#fff;padding:{26 if story else 22}px 64px {120 if story else 28}px;display:flex;justify-content:space-between;align-items:center">'
             f'<div><div style="font-size:{30 if story else 28}px;font-weight:700">0906 299 3555</div>'
             f'<div style="font-size:{21 if story else 19}px">sales.quotations@medsource.com.ph</div>'
             f'<div style="font-size:{18 if story else 16}px;opacity:.8;margin-top:4px">{fine}</div></div>'
             f'<div style="text-align:right;font-weight:700;font-size:{32 if story else 28}px;line-height:1.1">'
             f'<span style="font-weight:400;font-size:.62em">Certified</span><br>#Med<span style="color:{GREEN}">Mura</span></div></div>')
    h.append('</div></body></html>')
    return "".join(h)

with sync_playwright() as pw:
    b = pw.chromium.launch()
    for pub in PUBS:
        src = ROOT / pub["slug"] / "source"
        src.mkdir(parents=True, exist_ok=True)
        for story, name, W, H, out in [(False, "feed.html", 1080, 1350, "feed-1080x1350.png"), (True, "story.html", 1080, 1920, "story-1080x1920.png")]:
            (src / name).write_text(build(pub, story))
            pg = b.new_page(viewport={"width": W, "height": H})
            pg.goto((src / name).as_uri()); pg.wait_for_timeout(600)
            # overflow check
            ov = pg.evaluate("document.querySelector('.root').scrollHeight")
            if ov > H: print("OVERFLOW", pub["slug"], name, ov)
            pg.screenshot(path=str(src.parent / out)); pg.close()
    b.close()
print("done")
