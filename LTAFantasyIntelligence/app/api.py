from fastapi import FastAPI,Query
from app.core.classes.jogadores_por_rota import JogadoresPorRota
from app.core.classes.avaliador_jogador import AvaliadorDeJogador
from app.core.classes.jogador import Player
from app.core.inteligencia import encontrar_melhor_time
import requests
import os
import requests

app = FastAPI()

def trazer_dados_api():
    API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
    API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")

    url = f"http://{API_JAVA_HOST}:{API_JAVA_PORT}/jogadores"
    response = requests.get(url)
    jogadores = response.json()
    
    jogador_por_rota = JogadoresPorRota()
    avaliador = AvaliadorDeJogador()
    
    for jogador in jogadores:
        jogador_obj = Player(
            nickname=jogador["nickname"],
            rota=jogador["rota"],
            jogos=jogador["jogos"],
            kda=jogador["kda"],
            win_rate=jogador["win_rate"],
            cs_minuto=jogador["cs_minuto"],
            participa_abate=jogador["participa_abate"],
            media_pontos=jogador["media_pontos"],
            ultimo_ponto=jogador["ultimo_ponto"],
            valor_atual=jogador["valor_atual"],
            score=0
        )
        jogador_obj.score = avaliador.calcular_score(jogador_obj)
        if jogador_obj.score == 0:
            continue
        jogador_por_rota.adicionar_jogador(jogador_obj)
    return jogador_por_rota

@app.get("/melhor-time")
def gerar_time(orcamento: float=50):

    jogador_por_rota = trazer_dados_api()
    
    resultado = encontrar_melhor_time(jogador_por_rota,orcamento)
    return {
        "score": resultado.score,
        "custo": resultado.custo,
        "media_pontos": resultado.media_pontos,
        "time": [
            {
                "nickname": j.nickname,
                "rota": j.rota,
                "valor_atual": j.valor_atual,
                "score": j.score,
                "media_pontos": j.media_pontos
            }
            for j in resultado.time
        ]
    }
    
@app.get("/melhores-jogadores-por-rota")
def gerar_lista_jogadores():
    jogador_por_rota = trazer_dados_api()
    jogador_por_rota.ordernar_por_score()
    return jogador_por_rota