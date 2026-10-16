from playwright.sync_api import sync_playwright
import pathlib
d = pathlib.Path(__file__).parent
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for name, w, h, out in [("feed.html", 1080, 1350, "../feed-1080x1350.png"), ("story.html", 1080, 1920, "../story-1080x1920.png")]:
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg.goto((d / name).as_uri()); pg.wait_for_timeout(800)
        pg.screenshot(path=str(d / out)); pg.close()
    b.close()
