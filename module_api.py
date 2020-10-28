from prettytable import PrettyTable
import requests
import locale
import time
from colors import*

#Informações 
def infos():
    color_blue()
    print("Author: Gabriel Alves (Nalpalm Death fan)")
    print("Inspiration: Gilfoyle - Silicon Valley")
    print("Song: You Soufer - Nalpalm Death")
    print("\nUpdate a cada 5 minutos")
    


def value_bitcoin():
    #Consumindo API da cointrader
    chamada_api = requests.get('https://cointradermonitor.com/api/pbb/v1/ticker') 
    valor = chamada_api.json()
    valor_BR = (valor["last"])
    volume = (valor["volume24h"])
    
    #hora da execução, para apresentar o horario do check 
    hora = time.strftime("%H:%M", time.localtime())
    data = time.strftime("%Y-%m-%d")
    valor = valor_BR
   
    #Locale utilizado para formatar os valores
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    valor = locale.currency(valor, grouping=True, symbol=None)
    volume = locale.currency(volume, grouping=True, symbol=None)
   
    #Prettytable, uma biblioteca para apresentar dados em forma de tabela no terminal
    table = PrettyTable()
    color_green()
    table.field_names = (["Valor atual:", "Volume/24h", "Hora do check","Data"])
    table.add_row([f'R$ {valor}', volume, hora, data])
   
    return print(table)

