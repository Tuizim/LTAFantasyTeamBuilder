from enum import Enum
from pydantic import BaseModel, Field
import json

class Jogador(BaseModel):
    nickname: str = Field(..., unique=True, min_length=1, description="Apelido do jogador")
    rota: str
    jogos: int = Field(default=0, description="Número de jogos")
    win_rate: float = Field(default=0.0, description="Taxa de vitórias (%)")
    kda: float = Field(default=0.0, description="Kill/Death/Assist ratio")
    cs_minuto: float = Field(default=0.0, description="Farm por minuto")
    participa_abate: float = Field(default=0.0, description="Participação em abates (%)")
    media_ponto: float = Field(default=0.0, description="Média de pontos")
    ultimo_ponto: float = Field(default=0.0, description="Última pontuação obtida")
    valor_atual: float = Field(default=0.0, description="Valor de mercado atual")
    liga: str
    
    def to_dict(self):
        return self.dict()
