from app.core.classes.jogadores_por_rota import JogadoresPorRota
from app.core.classes.jogador import Player
from typing import List

def jsonToJogador(jogadores: List[Player]):
    jogadores_obj = []
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
        jogadores_obj.append(jogador_obj)
    return jogadores_obj

def jogadorToRota(jogadores: List[Player]):
    jogador_por_rota = JogadoresPorRota()
    for jogador in jogadores:
        jogador_por_rota.adicionar_jogador(jogador)
    return jogador_por_rota