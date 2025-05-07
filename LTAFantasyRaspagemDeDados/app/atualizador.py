from app.Extrair.extrairDadosFantasy import extrair_dados_fantasy
from app.Extrair.extrairDadosJogadoresLiga import extrair_dados
from app.Extrair.extrairDadosTime import extrair_dados_fantasy_time
from app.Extrair.extrairDadosConfrontos import extrair_dados_fantasy_confrontos
from app.Models.jogador_model import Jogador
from app.Models.times import Time,Confronto
import app.Comum.logs as logs
from app.Comum.util import normalizar_texto
import json
import requests
import os
import sys

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

def montar_dados_jogadores(cookieID):
    try:        
        logs.etapas(logs.enums.Etapa.ExtraindoDadosFantasy)
        dadosFantasy = extrair_dados_fantasy(cookieID)
        if (dadosFantasy==None):
            logs.respostas_falha(logs.enums.RespostaFalha)
            sys.exit()
        elif (len(dadosFantasy)==0):
            logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
            sys.exit()
        else:
            logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
        
        logs.etapas(logs.enums.Etapa.ExtraindoDadosLiga)
        dadosLtaSul = extrair_dados()
        logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
        
        logs.etapas(logs.enums.Etapa.MontandoObjeto)
        jogadores = []
        for jogador in dadosFantasy:
            for estatistica in dadosLtaSul:
                if estatistica["nickname"].upper() == jogador["nickname"].upper():
                    jogador_obj = Jogador(
                        **extrai_jogador_estatisticas(estatisticas=estatistica),
                        **extrai_jogador_fantasy(jogador=jogador)
                    )
                    jogadores.append(jogador_obj.to_dict())
        jogadores_json = json.dumps(jogadores, indent=4, ensure_ascii=False)
        if (len(jogadores_json)>0):
            logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
            return jogadores_json
    except RuntimeError as e: 
        logs.respostas_falha(logs.enums.RespostaFalha.Erro)
        print(e)

def atualizar_jogadores(cookieID):
    try:
        API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
        API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")
        url_api = f"http://{API_JAVA_HOST}:{API_JAVA_PORT}/jogadores/lote"
        headers = {'Content-Type': 'application/json'}
        
        logs.etapas(logs.enums.Etapa.IniciandoColetaJogadores)
        jogadores_json = montar_dados_jogadores(cookieID)
        
        
        logs.etapas(logs.enums.Etapa.EnviandoParaApi)  
        try: 
            response = requests.post(url_api,data=jogadores_json,headers=headers)
            if (response.status_code==200):
                logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
            else:
                logs.respostas_falha(logs.enums.RespostaFalha.Falhou) 
        except:
            logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
        
        logs.etapas(logs.enums.Etapa.AtualizandoDadosDaApi)  
        try:
            response = requests.put(url_api,data=jogadores_json, headers=headers)
            if (response.status_code==200):
                logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
            else:
                logs.respostas_falha(logs.enums.RespostaFalha.Falhou)
        except:
            logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
            
    except RuntimeError as e:
        logs.respostas_falha(logs.enums.RespostaFalha.Erro)
        print(e)

def montar_times(cookieId):
    try:
        logs.etapas(logs.enums.Etapa.ColetandoTimes)
        nome_times = extrair_dados_fantasy_time(cookieid=cookieId)
        if (nome_times==None):
            logs.respostas_falha(logs.enums.RespostaFalha)
            sys.exit()
        elif (len(nome_times)==0):
            logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
            sys.exit()
        else:
            logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
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
    try:
        API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
        API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")
        url_api = f"http://{API_JAVA_HOST}:{API_JAVA_PORT}/times/lote"
        headers = {'Content-Type': 'application/json'}
        
        logs.etapas(logs.enums.Etapa.IniciandoColetaTimes)
        json_times = montar_times(cookieID)
        
        logs.etapas(logs.enums.Etapa.EnviandoParaApi)  
        try: 
            response = requests.post(url_api,data=json_times,headers=headers)
            if (response.status_code==200):
                logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
            else:
                logs.respostas_falha(logs.enums.RespostaFalha.Falhou) 
        except:
            logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
        
    except RuntimeError as e:
        logs.respostas_falha(logs.enums.RespostaFalha.Erro)
        print(e)

def montar_confrontos(cookieId):
    confrontos = extrair_dados_fantasy_confrontos(cookieid=cookieId)
    if (confrontos==None):
        logs.respostas_falha(logs.enums.RespostaFalha)
        sys.exit()
    elif (len(confrontos)==0):
        logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
        sys.exit()
    else:
        logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
    confrontos_json=[]
    for confronto in confrontos:
        confrontos_json.append(confronto.to_dict())
    return json.dumps(confrontos_json, indent=4, ensure_ascii=False)

def atualizar_confrontos(cookieID):
    try:
        API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
        API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")
        url_api = f"http://{API_JAVA_HOST}:{API_JAVA_PORT}/confrontos/lote"
        headers = {'Content-Type': 'application/json'}
        
        logs.etapas(logs.enums.Etapa.IniciandoColetaConfrontos)
        json_confrontos = montar_confrontos(cookieID)
        
        logs.etapas(logs.enums.Etapa.EnviandoParaApi)  
        try: 
            response = requests.post(url_api,data=json_confrontos,headers=headers)
            if (response.status_code==200):
                logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
            else:
                logs.respostas_falha(logs.enums.RespostaFalha.Falhou) 
        except:
            logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
        
    except RuntimeError as e:
        logs.respostas_falha(logs.enums.RespostaFalha.Erro)
        print(e)