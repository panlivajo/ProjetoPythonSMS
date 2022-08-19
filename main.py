import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "acount Sid twilio"
# Your Auth Token from twilio.com/console
auth_token = "token twilio"
#conexão com o servidor twilio
client = Client(account_sid, auth_token)

#Projeto ler 6 arquivos excel contidos na mesma pasta do projeto
# #localizar venda maior que 55000 e enviar SMS com nome do vendedor e total de vendas

# Abrir os 6 arquivos Excel

#criação de lista
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
#percorrer listas metodo for
for mes in lista_meses:
    #print(mes)
    #metodo pd.read
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
     #print(tabela_vendas)
#condição para isolar venda maior que 55000
    if (tabela_vendas['Vendas'] > 55000).any():
#variaveis para receber a celula da tabela desejada + .values para isolar o conteudo apenas
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} a meta foi batida, vendedor {vendedor} vendeu {vendas}')
#metodo twilio envio de SMS
        message = client.messages.create(
            to="+numero de celular",
            from_="++14256003421",
            body=f'No mes de {mes} a meta foi batida, vendedor {vendedor} vendeu {vendas}')
        print(message.sid)


