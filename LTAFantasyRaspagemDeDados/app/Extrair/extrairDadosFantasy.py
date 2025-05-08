from playwright.sync_api import sync_playwright
import app.Comum.normalizar_dados as normalizar_dados
import app.Comum.logs as logs
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
            "jogador_div" : "div.grid.grid-cols-12.flex-1.h-24.justify-start",
            "nickname":"span.font-kurdis-extra-bold.uppercase.text-xl.text-lta-gold.truncate",
            "lane":'img[src*="/public/role/"]',
            "media_pontos":"div.flex.flex-row.gap-1.sm\\:gap-2.items-end div:nth-child(1) span.font-kurdis-extra-bold",
            "ultimo_ponto":"div.flex.flex-row.gap-1.sm\\:gap-2.items-end div:nth-child(2) span.font-kurdis-extra-bold",
            "valor_atual": "div.flex.text-sm.items-center.font-kurdis.text-right.justify-end span.font-kurdis-extra-bold",
            "flutuacao": "div.flex.text-sm.items-center.font-kurdis.text-right.justify-end span.font-red-hat-display-semi-bold"
        }

        jogadores =[]
        tentativas = 3
        for tentativa in range(tentativas):
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    viewport={"width": 1280, "height": 800},
                    java_script_enabled=True,
                    locale="pt-BR"
                )
                context.add_cookies(cookies)
                page = context.new_page()
                try:
                    page.goto("https://ltafantasy.com/pt/market")
                    page.wait_for_selector(html["jogador_div"], timeout=10000)

                    jogador_divs = page.locator(html["jogador_div"])

                    for i in range(jogador_divs.count()):
                        card = jogador_divs.nth(i)
                        
                        nick = card.locator(html["nickname"]).inner_text()
                        lane = card.locator(html["lane"]).first.get_attribute("alt")
                        media_pontos = card.locator(html["media_pontos"]).inner_text()
                        ultimo_ponto = card.locator(html["ultimo_ponto"]).inner_text()
                        valor_atual = card.locator(html["valor_atual"]).inner_text()
                        flutuacao = card.locator(html["flutuacao"]).inner_text() if card.locator(html["flutuacao"]).count()>0 else 0

                        jogadores.append(
                            {
                                "nickname":nick,
                                "rota":lane,
                                "media_pontos": normalizar_dados.normalizar_float(media_pontos),
                                "ultimo_ponto":normalizar_dados.normalizar_float(ultimo_ponto),
                                "valor_atual":normalizar_dados.normalizar_float(valor_atual),
                                "flutuacao_mercado":normalizar_dados.normalizar_float(flutuacao)
                            }
                        )
                    browser.close()
                    break
                except TimeoutError:
                    if (tentativa == tentativas-1):
                        logs.respostas_time_out(logs.enums.timeOut.timeOutFalha)
                        break
                    else:
                        logs.respostas_time_out(logs.enums.timeOut.timeOut)
                        continue
        return jogadores
            
    except RuntimeError as e:
        print(f"Caught: {e}")