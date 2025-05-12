from app.core.classes.jogador import Player
from app.core.classes.jogadores_por_rota import JogadoresPorRota
class AvaliadorDeJogador:
    def __init__(self):
        self.atributo_pesos = {
            "kill_rate": 0.35,       
            "assist_rate": 0.20,     
            "death_rate": - 0.25,      
            "cs_minuto": 0.05,       
            "participa_abate": 0.10, 
            "win_rate": 0.10,        
            "media_pontos": 0.10     
        }
        self.min_max = {
            "kill_rate":(0,8),
            "assist_rate":(0,10),
            "death_rate":(0,6),
            "cs_minuto":(0,10),
            "participa_abate":(0,1),
            "win_rate":(0,1),
            "media_pontos":(0,25),
        }
    def normalizar(self,campo,valor):
        min,max = self.min_max[campo]
        return (valor - min) / (max - min) if max > min else 0
    
    def calcular_score(self, jogador:Player):
        score = 0
        for atributo in self.atributo_pesos:
            valor = getattr(jogador, atributo, 0)
            valor = self.normalizar(campo=atributo,valor=valor)
            score += valor * self.atributo_pesos[atributo]
        return round(score * 100, 2)
    
    # def pontuar_confronto():