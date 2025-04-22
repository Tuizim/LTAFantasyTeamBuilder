from termcolor import colored
from app.atualizador import atualizar_jogadores
import app.Comum.logs as logs

logs.bem_vindo()
cookie_id = logs.menu_inicial()

atualizador = atualizar_jogadores(cookieID=cookie_id)

