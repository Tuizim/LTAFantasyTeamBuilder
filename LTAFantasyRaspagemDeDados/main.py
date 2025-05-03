from termcolor import colored
from app.atualizador import atualizar_jogadores,atualizar_times
import app.Comum.logs as logs

logs.bem_vindo()
cookie_id = logs.menu_inicial()

atualizar_times(cookieID=cookie_id)
atualizar_jogadores(cookieID=cookie_id)

