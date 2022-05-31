
import json
import os
import subprocess
    
def config():    
    col=''
    data = {}
    print("Configuração do Banco de dados: ")
    user = input("Informe o user: ")
    password = input("Informe o password: ")
    host = input("Informe o host: ")
    database = input("Informe o database: ")
    print('Informe as colunas que deseja conter no relatório: ')
    val='n'
    cont =1
    colRel = input("\n Diga a o nome da {}º- coluna * Essa sera a coluna de relacão entre as tabelas *: ".format(cont))
    while val != 'S':
        cont += 1
        col = input("Diga a o nome da {}º- coluna: ".format(cont))
        tabela = input("Diga o nome da tabela a qual a coluna pertence: ")
        if tabela in data:
            data[tabela].append(col)
        else:
            data[tabela] = [col]
        
        val = input('Finalizar colunas?\n Sim - S \n Não - ENTER \n - ')
        val = val.upper()
        print(val)
    view = input("Diga a o nome da coluna q contem a flag de exibição: ")
    flag = input("Diga qual a condição da flag para anonimização: ")
    tabela = input("Diga o nome da tabela a qual a coluna pertence: ")
    colunas = input("Diga quais as colunas a serem modificadas *(Separar por ','). ")
    colunas = colunas.replace(' ','')
    colunas = colunas.split(',')
        
    if tabela in data:
        data[tabela].append(view)
    else:
        data[tabela] = [view]
    
    for table in data:
        data[table].append(colRel)

    data['baseconfig']=[user,password,host,database]
    data['view']=[view,flag]
    data['colunas']=colunas
    
    #Configura sistema de recomendação
    apri = input('\n Deseja ter sistema de recomendação ?\n Sim - S \n Não - ENTER \n - ')
    apri = apri.upper()
    if apri == 'S':
        transaction = input(" informe a coluna de transação: ")
        item = input("informe a coluna que contem os itens para recomendação: ")
        sup = input("informe o valor de suporte: ")
        conf = input("informe o valor de confiança: ")
        data['apriori'] = True
        data['transaction'] = transaction
        data['item'] = item
        data['suporte']= sup
        data['confianca'] = conf
    else:
        data['apriori'] = False

    with open('data.json', 'w') as fp:
        json.dump(data, fp)

    print("RUN ...")
    """ for key in data:
        data[key] = pd.Series(data[key])

    df = pd.DataFrame(data=data)
    print(df)
    return user, password, host, database,df, view, flag, colunas
 """
 
 
if __name__ == '__main__':
    config()
    subprocess.call(os.getcwd() + '\API\main.py', shell=True)