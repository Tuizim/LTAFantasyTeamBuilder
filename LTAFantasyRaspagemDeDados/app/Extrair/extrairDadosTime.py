from playwright.sync_api import sync_playwright
from app.Comum import logs

def extrair_dados_fantasy_time(cookieid):
    try:
        cookies = [
            {
                "name": "__lolfantasy_session",
                "value": cookieid,
                "domain": ".ltafantasy.com",
                "path": "/",
                "httpOnly": False,
                "secure": True,
                "sameSite": "Lax"
            }
        ]

        html = {
            "linha-times":"div.relative > div.overflow-hidden > div.flex.-ml-2",
            "slides-time":"div.relative > div.overflow-hidden > div.flex.-ml-2 > div",
            "spans-times":"span.text-sm.text-center.text-muted-foreground"
        }
        times = []
        tentativas = 3
        for tentativa in range(tentativas):
            with sync_playwright() as p:
                try:
                    browser = p.chromium.launch(headless=True)
                    context = browser.new_context(
                        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        viewport={"width": 1280, "height": 800},
                        java_script_enabled=True,
                        locale="pt-BR"
                    )
                    context.add_cookies(cookies)
                    page = context.new_page()
                    page.goto("https://ltafantasy.com/pt")
                    page.wait_for_selector(html["linha-times"], timeout=10000)
                    slides = page.query_selector_all(html["slides-time"])
                    for slide in slides:
                        imgs = slide.query_selector_all("img")
                        times_in_slide =[img.get_attribute("alt") for img in imgs if img.get_attribute("alt")]
                        for time in times_in_slide:
                            times.append(time.upper())
                    browser.close()
                    break
                except TimeoutError:
                    if tentativa==tentativas-1:
                        logs.respostas_time_out(logs.enums.timeOut.timeOutFalha)
                        break
                    else:
                        logs.respostas_time_out(logs.enums.timeOut.timeOut)
                        continue
        return times
                     
    except RuntimeError as e:
        print(f"Caught: {e}")