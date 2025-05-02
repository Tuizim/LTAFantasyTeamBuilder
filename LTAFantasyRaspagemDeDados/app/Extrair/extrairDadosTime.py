from playwright.sync_api import sync_playwright
def extrair_dados_fantasy(cookieid):
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
        tentativas = 3
        for tentativa in range(tentativas):
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                context = browser.new_context()
                context.add_cookies(cookies)
                page = context.new_page()
                page.goto("https://ltafantasy.com/pt")
                page.wait_for_selector(html["linha-times"], timeout=10000)

                jogador_divs = page.locator(html["linha-times"])
                slides = page.query_selector_all(html["slides-time"])
                times = []
                for slide in slides:
                    imgs = slide.query_selector_all("img")
                    times_in_slide =[img.get_attribute("alt") for img in imgs if img.get_attribute("alt")]
                    for time in times_in_slide:
                        times.append(time)
                browser.close()
                      
    except RuntimeError as e:
        print(f"Caught: {e}")
        

extrair_dados_fantasy("Fe26.2*1*1f1c27a64ac0aae0fb69d4018bce573ea250ea3ea4d2201f5614bd3853f5a442*O93sbrMGkSzd4YyviRcWcg*-cRZN79BmmQGWzvfEDku2-w7KkDIqQ6H9g_hLjZoXtSuZQYhd9jJ8iph5yWW_stkisNHrz-3Nl3zvSfPGnN0FXJjN7YBZpa6DDC3YkRcTfPvKh3y3v4fyKqZcKXCHvpyXcJ0RUByuFSEidcrY_6o9fpJWc0qOGJy4Ml3ssd58u3k9F7y1bIxo1XNuS4ihx4_*1746575832753*270c018440f5a34c3d5e78982ed7ab57395b28b288c13ca5633d9eeccb01510d*94-yghVRJnB8dtzDPF_Wq80jSxIZhnCAuZ46PoKY1eg~2")