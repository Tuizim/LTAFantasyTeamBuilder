from pydantic import BaseModel, Field
from typing import Optional

class Time(BaseModel):
    nome: str = Field(..., description="Nome do time")
    
    def to_dict(self):
        return self.dict()