from app.Extrair.extrairDadosFantasy import extrair_dados_fantasy
from app.Extrair.extrairDadosJogadoresSul import extrair_dados
from app.Models.jogador_model import Jogador
import app.Comum.logs as logs
import json
from termcolor import colored
import requests
import os
import sys

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
                        nickname= jogador["nickname"].upper(),
                        rota= jogador["rota"].upper(),
                        jogos= estatistica["jogos"],
                        win_rate= estatistica["win_rate"],
                        kda= estatistica["kda"],
                        cs_minuto= estatistica["cs_minuto"],
                        participa_abate= estatistica["participa_abate"],
                        media_pontos= jogador["media_pontos"],
                        ultimo_ponto= jogador["ultimo_ponto"],
                        valor_atual= jogador["valor_atual"],
                        liga= estatistica["liga"]
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
        
        logs.etapas(logs.enums.Etapa.IniciandoColeta)
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
    
    