from termcolor import colored
import pyfiglet
import app.Comum.enums as enums



def bem_vindo():
    print(pyfiglet.figlet_format("BEM VINDO!"))

def menu_inicial():
    print(colored("Para atualizar os dados da API,\npasse o ID do seu cookie no site do LTAFantasy.", "white"))
    print()
    return input(colored("Digite o ID do cookie: ", "yellow"))

def etapas(enum:enums.Etapa):
    print()
    print(colored(enum.value, "white"))

def respostas_falha(enum: enums.RespostaFalha):
    print(colored(enum.value, "red"))

def respostas_sucesso(enum: enums.RespostaSucesso):
    print(colored(enum.value, "green"))

def respostas_time_out(enum: enums.timeOut):
    print(enum.value)