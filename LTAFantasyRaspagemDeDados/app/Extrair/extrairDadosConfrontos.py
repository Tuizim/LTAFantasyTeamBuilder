from playwright.sync_api import sync_playwright
from app.Comum import logs
from datetime import datetime
from app.Models.times import Confronto,Time
from app.Comum.util import normalizar_texto

meses = {
    'jan': '01',
    'fev': '02',
    'mar': '03',
    'abr': '04',
    'mai': '05',
    'jun': '06',
    'jul': '07',
    'ago': '08',
    'set': '09',
    'out': '10',
    'nov': '11',
    'dez': '12'
}
def converter_data(data_str, ano=datetime.now().year):
    partes = data_str.split(",")[-1].strip().split(".")
    mes_abrev = partes[0].strip()
    dia = partes[1].strip().zfill(2)
    mes = meses[mes_abrev]
    data_formatada = f"{ano}-{mes}-{dia}"
    return data_formatada

def extrair_dados_fantasy_confrontos(cookieid):
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
            "spans-times":"span.text-sm.text-center.text-muted-foreground",
            "data":"div.w-full.flex.flex-row.items-center.justify-between > span"
        }
        confrontos = []
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
                        if (len(imgs)==0):
                            break
                        datas = slide.query_selector_all(html["data"])
                        if (len(datas)==0):
                            break
                        data = converter_data(datas[0].inner_text())
                        confronto =[img.get_attribute("alt").upper() for img in imgs if img.get_attribute("alt").upper()]
                        time1 = normalizar_texto(confronto[0])
                        time2 = normalizar_texto(confronto[1])
                        confronto_obj = Confronto(
                            time1=Time(nome= time1),
                            time2=Time(nome= time2),
                            data_confronto=data )
                        confrontos.append(confronto_obj)
                    browser.close()
                    break
                except RuntimeError as e:
                    print(e)
                    if tentativa==tentativas-1:
                        logs.respostas_time_out(logs.enums.timeOut.timeOutFalha)
                        break
                    else:
                        logs.respostas_time_out(logs.enums.timeOut.timeOut)
                        continue
        return confrontos
                        
            
                      
    except RuntimeError as e:
        print(f"Caught: {e}")
        
