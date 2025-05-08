from app.Extrair.extrairDadosFantasy import extrair_dados_fantasy
from app.Extrair.extrairDadosJogadoresLiga import extrair_dados
from app.Extrair.extrairDadosTime import extrair_dados_fantasy_time
from app.Extrair.extrairDadosConfrontos import extrair_dados_fantasy_confrontos
from app.Models.jogador_model import Jogador
from app.Models.times import Time
import app.Comum.logs as logs
from app.Comum.normalizar_dados import normalizar_texto
from app.Comum.api_gateway import Gateway
import json
import sys

gateway = Gateway()

def montar_dados_jogadores(cookieID):
    def extrai_jogador_fantasy(jogador):
        return {
            "nickname": jogador["nickname"].upper(),
            "rota": jogador["rota"].upper(),
            "media_pontos": jogador["media_pontos"],
            "ultimo_ponto": jogador["ultimo_ponto"],
            "valor_atual": jogador["valor_atual"]
        }
    
    def extrai_jogador_estatisticas(estatisticas):
        time_nome = normalizar_texto(estatisticas["time"])
        de_para = {
            "RED CANIDS":"RED KALUNGA",
            "TEAM LIQUID":"TEAM LIQUID HONDA",
            "CLOUD9":"CLOUD9 KIA",
            "LYON 2024 AMERICAN TEAM":"LYON",
            "LEVIATAN":"LEVIATAN ESPORTS"
        }
        time= de_para.get(time_nome,time_nome)
        return {
            "jogos": estatisticas["jogos"],
            "win_rate": estatisticas["win_rate"],
            "kda": estatisticas["kda"],
            "kill_rate": estatisticas["kill_rate"],
            "death_rate": estatisticas["death_rate"],
            "assist_rate": estatisticas["assist_rate"],
            "cs_minuto": estatisticas["cs_minuto"],
            "participa_abate": estatisticas["participa_abate"],
            "liga": estatisticas["liga"],
            "time": Time(nome=time)
        }
    
    try:  
        logs.etapas(logs.enums.Etapa.ExtraindoDadosFantasy)
        dadosFantasy = extrair_dados_fantasy(cookieID)
        validar_dados_extraidos(dadosFantasy)
        
        logs.etapas(logs.enums.Etapa.ExtraindoDadosLiga)
        dadosLtaSul = extrair_dados()
        validar_dados_extraidos(dadosLtaSul)
        
        jogadores = []
        for jogador in dadosFantasy:
            for estatistica in dadosLtaSul:
                if estatistica["nickname"].upper() == jogador["nickname"].upper():
                    jogador_obj = Jogador(
                        **extrai_jogador_estatisticas(estatisticas=estatistica),
                        **extrai_jogador_fantasy(jogador=jogador)
                    )
                    jogadores.append(jogador_obj.to_dict())
        return json.dumps(jogadores, indent=4, ensure_ascii=False)
    except RuntimeError as e: 
        logs.respostas_falha(logs.enums.RespostaFalha.Erro)
        print(e)

def atualizar_jogadores(cookieID):
    logs.etapas(logs.enums.Etapa.IniciandoColetaJogadores)
    jogadores_json = montar_dados_jogadores(cookieID)
    gateway.adicionar_banco(endpoint="jogadores/lote",json=jogadores_json)
    gateway.atualizar_banco(endpoint="jogadores/lote",json=jogadores_json)
    
def montar_times(cookieId):
    try:
        logs.etapas(logs.enums.Etapa.ColetandoTimes)
        nome_times = extrair_dados_fantasy_time(cookieid=cookieId)
        validar_dados_extraidos(nome_times)
        
        times=[]
        for time in nome_times:
            time = normalizar_texto(time)
            time_obj = Time(nome=time)
            times.append(time_obj.to_dict())
        return json.dumps(times, indent=4, ensure_ascii=False)
    
    except RuntimeError as e:
        logs.respostas_falha(logs.enums.RespostaFalha.Erro)
        print(e)
           
def atualizar_times(cookieID):
    logs.etapas(logs.enums.Etapa.IniciandoColetaTimes)
    json_times = montar_times(cookieID)
    gateway.adicionar_banco(endpoint="times/lote",json=json_times)

def montar_confrontos(cookieId):
    confrontos = extrair_dados_fantasy_confrontos(cookieid=cookieId)
    validar_dados_extraidos(confrontos)
    
    confrontos_json=[]
    for confronto in confrontos:
        confrontos_json.append(confronto.to_dict())
    return json.dumps(confrontos_json, indent=4, ensure_ascii=False)

def atualizar_confrontos(cookieID):        
    logs.etapas(logs.enums.Etapa.IniciandoColetaConfrontos)
    json_confrontos = montar_confrontos(cookieID)
    gateway.adicionar_banco(endpoint="confrontos/lote",json=json_confrontos)

def validar_dados_extraidos(json):
    if (json==None):
        logs.respostas_falha(logs.enums.RespostaFalha)
        sys.exit()
    elif (len(json)==0):
        logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
        sys.exit()
    else:
        logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)