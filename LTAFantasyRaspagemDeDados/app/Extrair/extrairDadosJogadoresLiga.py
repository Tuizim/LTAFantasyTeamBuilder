from playwright.sync_api import sync_playwright
import app.Comum.normalizar_dados as normalizar_dados

def extrair_dados_por_liga(liga,endpoint_liga):
    try:
        html={
            "linhas":"table.wikitable > tbody > tr:has(td.spstats-player)",
            "nickname":"td.spstats-player",
            "team":"td.spstats-team a",
            "jogos":"td:nth-child(3)",
            "win_rate":"td:nth-child(6)",
            "kda":"td:nth-child(10)",
            "kill_rate":"td:nth-child(7)",
            "death_rate":"td:nth-child(8)",
            "assist_rate":"td:nth-child(9)",
            "cs_minuto":"td:nth-child(12)",
            "participa_abate":"td:nth-child(17)"
        }

        jogadores = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://lol.fandom.com/wiki"+endpoint_liga)

            page.wait_for_selector(html["linhas"])
            linhas = page.locator(html["linhas"])
            
            for i in range(linhas.count()):
                linha = linhas.nth(i)
                
                nickname = linha.locator(html["nickname"]).inner_text()
                time = linha.locator(html["team"]).first.get_attribute("title")
                jogos = linha.locator(html["jogos"]).inner_text()
                win_rate = linha.locator(html["win_rate"]).inner_text()
                kda = linha.locator(html["kda"]).inner_text()
                kill_rate = linha.locator(html["kill_rate"]).inner_text()
                death_rate = linha.locator(html["death_rate"]).inner_text()
                assist_rate = linha.locator(html["assist_rate"]).inner_text()
                
                cs_minuto = linha.locator(html["cs_minuto"]).inner_text()
                participa_abate = linha.locator(html["participa_abate"]).inner_text()
                
                jogadores.append(
                {
                    "nickname":nickname,
                    "time": time,
                    "jogos":normalizar_dados.normalizar_int(jogos),
                    "win_rate":normalizar_dados.normalizar_porc(win_rate),
                    "kda":normalizar_dados.normalizar_float(kda),
                    "kill_rate":normalizar_dados.normalizar_float(kill_rate),
                    "death_rate":normalizar_dados.normalizar_float(death_rate),
                    "assist_rate":normalizar_dados.normalizar_float(assist_rate),
                    "cs_minuto": normalizar_dados.normalizar_float(cs_minuto),
                    "participa_abate":normalizar_dados.normalizar_porc(participa_abate),
                    "liga":liga
                } 
                )
            browser.close()
            return jogadores
    except RuntimeError as e:
        print(f"Caught: {e}")
        
def extrair_dados():
    endpoint_liga = {
        "LTANorte":"/LTA_North/2025_Season/Split_2/Player_Statistics",
        "LTASul":"/LTA_South/2025_Season/Split_2/Player_Statistics"
    }
    jogadores =  []
    for liga,endpoint in endpoint_liga.items():
        jogadores_por_liga = extrair_dados_por_liga(liga,endpoint)
        for jogador in jogadores_por_liga:
            jogadores.append(jogador)
    return jogadores
        