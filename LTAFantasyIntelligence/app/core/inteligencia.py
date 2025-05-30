import itertools
from app.core.classes.resultado_time import ResultadoTime
from app.core.classes.jogadores_por_rota import JogadoresPorRota

def encontrar_melhor_time(rotas:JogadoresPorRota,orcamento) -> ResultadoTime:
    jogadores_por_rota = [rotas.get_jogadores(rota) for rota in rotas.get_rotas()]
    todas_combinacoes = itertools.product(*jogadores_por_rota)
    
    melhor_time = None
    melhor_score = 0
    custo_equipe = 0
    melhor_media_pontos= 0
    
    for combinacao in todas_combinacoes:
        custo_total = sum(jogador.valor_atual for jogador in combinacao)
        score_total = sum(jogador.score for jogador in combinacao)
        media_pontos = sum(jogador.media_pontos for jogador in combinacao)
        
        if custo_total <= orcamento and score_total > melhor_score:
            custo_equipe = custo_total
            melhor_score = score_total
            melhor_time = combinacao
            melhor_media_pontos = media_pontos
        
    return ResultadoTime(
            round(score_total,2),
            melhor_time,
            round(custo_equipe,2),
            round(melhor_media_pontos,2)
            )
