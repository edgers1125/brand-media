from playwright.sync_api import sync_playwright
import pathlib
p=pathlib.Path(__file__).parent/"cover.html"
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1640,"height":624},device_scale_factor=1)
    pg.goto(p.as_uri()); pg.wait_for_timeout(800)
    pg.screenshot(path=str(p.parent/"../facebook-cover-1640x624.png")); b.close()
