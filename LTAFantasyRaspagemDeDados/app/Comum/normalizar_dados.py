def normalizar_float(valor):
    try:
        valor = float(valor)
    except:
        valor = 0
    return round(valor,2)

def normalizar_int(valor):
    try:
        valor = int(valor)
    except:
        valor = 0
    return round(valor,2)

def normalizar_porc(valor):
    try:
        valor = float(valor.strip('%')) / 100
    except:
        valor = 0
    return round(valor,2)

def normalizar_texto(texto: str) -> str:
    import unicodedata
    import re
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r'[^A-Za-z0-9 ]+', '', texto)
    return texto.upper()  