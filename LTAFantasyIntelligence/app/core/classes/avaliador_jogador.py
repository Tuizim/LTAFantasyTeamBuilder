from app.core.classes.jogador import Player
from app.core.classes.jogadores_por_rota import JogadoresPorRota
class AvaliadorDeJogador:
    def __init__(self):
        self.atributo_pesos = {
            "kda": 0.40,
            "cs_minuto": 0.10,
            "participa_abate": 0.20,
            "win_rate": 0.10,
            "media_pontos": 0.20
        }
        self.faixa_conservadora = {
            "kda":{"min":2.0 , "max":10.0},
            "cs_minuto":{"min":6.5 , "max":10.0},
            "participa_abate":{"min":0.0 , "max":0.9},
            "win_rate":{"min":0 , "max":85},
            "media_pontos":{"min":0.0 , "max":25.0}
        }
     
    def calcular_score(self, jogador:Player):
        def normalizar(valor,minimo,maximo):
            return (valor-minimo) / (maximo-minimo)
        score = 0
        for atributo in self.atributo_pesos:
            valor = getattr(jogador, atributo, 0)
            minimo= self.faixa_conservadora[atributo]["min"]
            maximo= self.faixa_conservadora[atributo]["max"]
            valor = normalizar(valor,minimo,maximo)
            score += valor * self.atributo_pesos[atributo]
            
        return round(score, 2)
    
    def ajustar_score_jogadores(jogadores:JogadoresPorRota):
        soma_score=0
        quantidade_jogadores = 0    
        normalizador= 10
        
        for rota in jogadores.rotas:
            quantidade_jogadores += len(jogadores.rotas[rota])
            for jogador in jogadores.rotas[rota]:
                soma_score+=jogador.score
        
        media_score = soma_score/quantidade_jogadores
        for rota in jogadores.rotas:
            for jogador in jogadores.rotas[rota]:
                jogador.score = (jogador.jogos/(jogador.jogos + normalizador)) * jogador.score + (normalizador / (jogador.jogos + normalizador)) * media_score
                jogador.score = round(jogador.score,3)

    # def pontuar_confronto():