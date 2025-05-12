from fastapi import FastAPI,Query
from app.core.classes.jogadores_por_rota import JogadoresPorRota
from app.core.avalidador.avaliador_jogador import AvaliadorDeJogador
from app.core.classes.jogador import Player
from app.core.inteligencia import encontrar_melhor_time
from app.core.Enum.ligas import Ligas
import requests
import os
import requests

app = FastAPI()

def trazer_dados_api(liga:None):
    API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
    API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")

    url = f"http://{API_JAVA_HOST}:{API_JAVA_PORT}/jogadores"
    if liga: url= url + "?liga=" + liga
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
            kill_rate=jogador["kill_rate"],
            death_rate=jogador["death_rate"],
            assist_rate=jogador["assist_rate"],
            win_rate=jogador["win_rate"],
            cs_minuto=jogador["cs_minuto"],
            participa_abate=jogador["participa_abate"],
            media_pontos=jogador["media_pontos"],
            ultimo_ponto=jogador["ultimo_ponto"],
            valor_atual=jogador["valor_atual"],
            liga= jogador["liga"],
            score=0
        )
        jogador_obj.score = avaliador.calcular_score(jogador_obj)
        if jogador_obj.score == 0:
            continue
        jogador_por_rota.adicionar_jogador(jogador_obj)
    return jogador_por_rota

@app.get("/melhor-time")
def gerar_time(orcamento: float=50, Liga: Ligas=None):

    jogador_por_rota = trazer_dados_api(Liga)
    
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
def gerar_lista_jogadores(Liga: Ligas=None):
    jogador_por_rota = trazer_dados_api(Liga)
    jogador_por_rota.ordernar_por_score()
    return jogador_por_rota