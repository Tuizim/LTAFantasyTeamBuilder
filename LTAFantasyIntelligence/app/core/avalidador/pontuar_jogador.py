from app.core.avalidador.avaliador_jogador import AvaliadorDeJogador
from app.core.classes.jogador import Player
from typing import List

def pontuar_jogadores(jogadores: List[Player]):
    
    avaliador = AvaliadorDeJogador()
    for jogador in jogadores:
        jogador.score = avaliador.calcular_score(jogador=jogador)
    return jogadores