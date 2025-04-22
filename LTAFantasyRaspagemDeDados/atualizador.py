from extrairDadosFantasy import extrair_dados_fantasy
from extrairDadosJogadoresSul import extrair_dados
from jogador_model import Jogador
import json
from termcolor import colored
import requests
import os
import sys

def montar_dados_jogadores(cookieID):
    try:        
        print(colored("Coletando dados do fantasy...", "white"))
        dadosFantasy = extrair_dados_fantasy(cookieID)
        if (dadosFantasy==None):
            print(colored("Falhou!", "red"))
            sys.exit()
        elif (len(dadosFantasy)==0):
            print(colored("Servico LTAFantasy esta fora do ar!", "red"))
            sys.exit()
        else: print(colored("Sucesso!", "green"))
        
        print(colored("Coletando estatisticas da liga...", "white"))
        dadosLtaSul = extrair_dados()
        print(colored("Sucesso!", "green"))
        
        print(colored("Montando objetos...", "white"))
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
                        media_ponto= jogador["media_pontos"],
                        ultimo_ponto= jogador["ultimo_ponto"],
                        valor_atual= jogador["valor_atual"],
                        liga= jogador["liga"]
                    )
                    jogadores.append(jogador_obj.to_dict())
        jogadores_json = json.dumps(jogadores, indent=4, ensure_ascii=False)
        if (len(jogadores_json)>0):
            print(colored("Sucesso!", "green"))
            return jogadores_json
    except RuntimeError as e: 
        print(colored("ERRO!", "red"))
        print(e)

def atualizar_jogadores(cookieID):
    try:
        API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
        API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")
        url_api = f"http://{API_JAVA_HOST}:{API_JAVA_PORT}/jogadores/lote"
        headers = {'Content-Type': 'application/json'}
        
        
        print(colored("\nDados de jogadores estao sendo coletados", "white"))    
        jogadores_json = montar_dados_jogadores(cookieID)
        
        
        print(colored("\nEnviando todos os dados para a API...", "white"))   
        try: 
            response = requests.post(url_api,data=jogadores_json,headers=headers)
            if (response.status_code==200):
                print(colored("Sucesso", "green"))
            else:
                print(colored("Falhou!", "red")) 
        except:
            print(colored("conexao falhou!", "red"))
        
        print(colored("Atualizando todos os dados da API...", "white"))
        try:
            response = requests.patch(url_api,data=jogadores_json, headers=headers)
            if (response.status_code==200):
                print(colored("Sucesso", "green"))
            else:
                print(colored("Falhou!", "red"))
        except:
            print(colored("conexao falhou!", "red"))
            
    except RuntimeError as e:
        print(colored("ERRO!", "red"))
        print(e)
    
    