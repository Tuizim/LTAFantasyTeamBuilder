import app.Comum.logs as logs
import requests
import requests
import os

class Gateway():
    API_JAVA_HOST = os.getenv("API_JAVA_HOST", "localhost")
    API_JAVA_PORT = os.getenv("API_JAVA_PORT", "8080")
    headers = {'Content-Type': 'application/json'}

    def adicionar_banco(self,endpoint,json):
        try:
            url_api = f"http://{self.API_JAVA_HOST}:{self.API_JAVA_PORT}/{endpoint}"
            logs.etapas(logs.enums.Etapa.EnviandoParaApi)  
            try: 
                response = requests.post(url_api,data=json,headers=self.headers)
                if (response.status_code==200):
                    logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
                else:
                    logs.respostas_falha(logs.enums.RespostaFalha.Falhou) 
            except:
                logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
            
        except RuntimeError as e:
            logs.respostas_falha(logs.enums.RespostaFalha.Erro)
            print(e)

    def atualizar_banco(self,endpoint,json):
        try:
            url_api = f"http://{self.API_JAVA_HOST}:{self.API_JAVA_PORT}/{endpoint}"
            logs.etapas(logs.enums.Etapa.AtualizandoDadosDaApi)  
            try: 
                response = requests.put(url_api,data=json,headers=self.headers)
                if (response.status_code==200):
                    logs.respostas_sucesso(logs.enums.RespostaSucesso.Sucesso)
                else:
                    logs.respostas_falha(logs.enums.RespostaFalha.Falhou) 
            except:
                logs.respostas_falha(logs.enums.RespostaFalha.Conexao)
        except RuntimeError as e:
            logs.respostas_falha(logs.enums.RespostaFalha.Erro)
            print(e)