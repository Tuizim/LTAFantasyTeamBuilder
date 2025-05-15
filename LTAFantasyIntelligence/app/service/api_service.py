from app.core.avalidador.pontuar_jogador import pontuar_jogadores
from app.repository.api_repository import trazer_dados_api
from app.converter.jogador_converter import jsonToJogador,jogadorToRota
from app.core.inteligencia import encontrar_melhor_time
from app.core.Enum.ligas import Ligas


def gerar_melhor_time(orcamento: float=50, Liga: Ligas=None):

    jogadores = trazer_dados_api(Liga)
    jogadores = jsonToJogador(jogadores)
    jogadores = pontuar_jogadores(jogadores=jogadores)
    jogador_por_rota = jogadorToRota(jogadores=jogadores)
    
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
    
def gerar_lista_jogadores_pontuados(Liga: Ligas=None):
    jogadores = trazer_dados_api(Liga)
    jogadores = jsonToJogador(jogadores)
    jogadores = pontuar_jogadores(jogadores)
    jogador_por_rota = jogadorToRota(jogadores)
    jogador_por_rota.ordernar_por_score()
    return jogador_por_rota