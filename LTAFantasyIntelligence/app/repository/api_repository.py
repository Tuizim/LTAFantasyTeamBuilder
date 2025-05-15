import requests
import os

def trazer_dados_api(liga:None):
    try:
        API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
        API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")

        url = f"http://{API_JAVA_HOST}:{API_JAVA_PORT}/jogadores"
        if liga:
            url += f"?liga={liga}"

        response = requests.get(url)
        response.raise_for_status()  # Levanta erro se resposta não for 200
        return response.json()

    except requests.exceptions.RequestException as e:
        raise RuntimeError("Serviço está fora do ar") from e