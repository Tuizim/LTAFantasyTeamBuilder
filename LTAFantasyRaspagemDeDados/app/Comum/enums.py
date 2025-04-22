from enum import Enum

class Etapa(Enum):
    IniciandoColeta = "Dados de jogadores estao sendo coletados"
    ExtraindoDadosFantasy = "Coletando dados do fantasy..."
    ExtraindoDadosLiga = "Coletando estatisticas da liga..."
    MontandoObjeto = "Montando objetos..."
    EnviandoParaApi = "Enviando todos os dados para a API..."
    AtualizandoDadosDaApi = "Atualizando todos os dados da API..."
    
class RespostaFalha(Enum):
    Erro = "Erro!"
    Conexao = "Conexao falhou!"
    ForaDoAr = "Servico esta fora do ar!"
    Falhou = "Falhou!"
class RespostaSucesso(Enum):
    Sucesso = "Sucesso"
    
class timeOut(Enum):
    timeOut = "Time out na solicitacao. tentando novamente."
    timeOutFalha = "Falha ao carregar os dados após várias tentativas."