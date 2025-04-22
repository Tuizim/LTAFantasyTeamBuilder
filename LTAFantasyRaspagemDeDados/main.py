import pyfiglet
from termcolor import colored
from atualizador import atualizar_jogadores
# Título estilizado
print(pyfiglet.figlet_format("BEM VINDO!"))
print(colored("Para atualizar os dados da API,\npasse o ID do seu cookie no site do LTAFantasy.", "white"))

cookie_id = input(colored("\nDigite o ID do cookie: ", "yellow"))
atualizador = atualizar_jogadores(cookieID=cookie_id)

