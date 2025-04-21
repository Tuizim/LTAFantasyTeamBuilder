from app.core.classes.jogador import Player
class AvaliadorDeJogador:
    def __init__(self):
        self.atributo_pesos = {
            "kda": 0.50,
            "cs_minuto": 0.05,
            "participa_abate": 0.10,
            "win_rate": 0.20,
            "media_pontos": 0.15
        }

    def calcular_score(self, jogador:Player):
        score = 0
        for atributo in self.atributo_pesos:
            valor = getattr(jogador, atributo, 0)
            score += valor * self.atributo_pesos[atributo]
            
        return round(score, 2)