class Player:
    def __init__(self,
                 nickname,
                 rota,
                 jogos,
                 win_rate,
                 kda,
                 kill_rate,
                 death_rate,
                 assist_rate,
                 cs_minuto,
                 participa_abate,
                 media_pontos,
                 ultimo_ponto,
                 valor_atual,
                 score,
                 liga):
        self.nickname = nickname
        self.rota = rota
        self.jogos = round(jogos,2)
        self.win_rate= round(win_rate,2)
        self.kda = round(kda,2)
        self.kill_rate = round(kill_rate,2)
        self.death_rate = round(death_rate,2)
        self.assist_rate = round(assist_rate,2)
        self.cs_minuto = round(cs_minuto,2)
        self.participa_abate = round(participa_abate,2)
        self.media_pontos = round(media_pontos,2)
        self.ultimo_ponto = round(ultimo_ponto,2)
        self.valor_atual = round(valor_atual,2)
        self.score = round(score,2)
        self.liga = liga
        pass
    def __str__(self):
        return f"Player(nickname={self.nickname}, lane={self.rota}, value={self.valor_atual}, score={self.score}, media de pontos={self.media_pontos} )"