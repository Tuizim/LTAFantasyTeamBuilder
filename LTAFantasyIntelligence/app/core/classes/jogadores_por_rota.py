from app.core.classes.jogador import Player
import json
class JogadoresPorRota:
    def __init__(self):
        self.rotas = {
            "TOP": [],
            "JUNGLE": [],
            "MID": [],
            "SUPPORT": [],
            "BOTTOM": []
        }
    def adicionar_jogador(self,jogador:Player):
        if jogador.rota not in self.rotas:
            raise ValueError(f"Rota inválida: {rota}")
        self.rotas[jogador.rota].append(jogador)
    
    def get_jogadores_rota(self, rota):
        return self.rotas.get(rota, [])
    
    def get_rotas(self):
        return self.rotas.keys()
    
    def ordernar_por_score(self):
        for rota in self.rotas.values():
            rota.sort(key=lambda x: x.score, reverse= True)
    def __str__(self):
        resultado ={
            rota: [
                {
                    "nickname": player.nickname,
                    "rota": player.rota,
                    "valor_atual": player.valor_atual,
                    "score": player.score,
                    "media_pontos": player.media_pontos
                }
                for player in self.rotas[rota]
            ]
            for rota in self.rotas
        }
        return json.dumps(resultado, indent=4, ensure_ascii=False)