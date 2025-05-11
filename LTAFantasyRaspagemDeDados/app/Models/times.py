from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Time(BaseModel):
    nome: str = Field(..., description="Nome do time")
    
    def to_dict(self):
        return self.dict()

class Confronto(BaseModel):
    time1: Time = Field(..., description="Time1")
    time2: Time = Field(..., description="Time2")
    data_confronto: str = Field(..., description="data dd-mm-yyyy")
    
    def to_dict(self):
        return self.dict()
