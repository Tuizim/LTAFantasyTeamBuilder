from playwright.sync_api import sync_playwright
import util

def extrair_dados_liga_sul():
    try:
        html={
            "linhas":"table.wikitable > tbody > tr:has(td.spstats-player)",
            "nickname":"td.spstats-player",
            "team":"td.spstats-team a",
            "jogos":"td:nth-child(3)",
            "win_rate":"td:nth-child(6)",
            "kda":"td:nth-child(10)",
            "cs_minuto":"td:nth-child(12)",
            "participa_abate":"td:nth-child(17)"
        }

        jogadores = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://lol.fandom.com/wiki/LTA_South/2025_Season/Split_2/Player_Statistics")

            page.wait_for_selector(html["linhas"])
            linhas = page.locator(html["linhas"])
            
            for i in range(linhas.count()):
                linha = linhas.nth(i)
                
                nickname = linha.locator(html["nickname"]).inner_text()
                time = linha.locator(html["team"]).first.get_attribute("title")
                jogos = linha.locator(html["jogos"]).inner_text()
                win_rate = linha.locator(html["win_rate"]).inner_text()
                kda = linha.locator(html["kda"]).inner_text()
                cs_minuto = linha.locator(html["cs_minuto"]).inner_text()
                participa_abate = linha.locator(html["participa_abate"]).inner_text()
                
                jogadores.append(
                {
                    "nickname":nickname,
                    "time": time,
                    "jogos":util.normalizar_int(jogos),
                    "win_rate":util.normalizar_porc(win_rate),
                    "kda":util.normalizar_float(kda),
                    "cs_minuto": util.normalizar_float(cs_minuto),
                    "participa_abate":util.normalizar_porc(participa_abate),
                } 
                )
            browser.close()
            return jogadores
    except RuntimeError as e:
        print(f"Caught: {e}")