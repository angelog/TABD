from ast import arg
import mysql.connector
from numpy import insert
import pandas as pd
import apriori as apr
class database:
    def __init__(self,user = 'root',password ='97855818',host='127.0.0.1',database='tabd'):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

    def insertData(self,data):
        args = '{},'
        args = args * len(data)
        args = '({})'.format(args[:-1])
        val = '%s,'
        val = val * len(data)
        val = '({})'.format(val[:-1])
        cursor = self.cnx.cursor()
        query = ("INSERT INTO Relatorio {} "
                 "VALUES {}").format(self.workdata, args, val)

        cursor.executemany(query, list(data.to_records(index=False)))
        self.cnx.commit()
        
    def relatorio(self, df, view, flag, colunas, apri=False, transaction= '', item='', sup=0, conf=0):
        #print(df)
        result={}
        #cursor = self.cnx.cursor()
        for table in df:
            col = ''
            for c in df[table]:
                c = str(c)
                if c == 'nan':
                    pass
                else:
                    col = col + c +','
            result[table] = pd.read_sql_query('''select {} from {}'''.format(col[:-1], table), self.cnx)

        cont = 0
        for df in result:
            if cont == 0:
                relatorio  = result[df]
            else:
                relatorio = pd.merge(relatorio, result[df], how='outer')
            
            cont += 1
        for row in relatorio.index:
            if relatorio[view][row] == flag:
                for col in colunas:
                    relatorio.loc[row,col] = 'XXXXXXXXXX'
        
        relatorio = relatorio.drop(columns=['view'])
        relatorio.to_csv('relatorio.csv',index=False)
        if apri:
            rules =  apr.apriori(relatorio, transaction, item, sup, conf)
            if rules == []:
                rules =  '<h4>... Sem Recomendação...</h4>'
        else:
            rules = '<h4>... Sem Recomendação...</h4>'

        args = "{} varchar(20),"
        args = args * len(relatorio)
        query = """create table if not exists Relatorio({})""".format(args[:-1])
        cursor = self.cnx.cursor()
        cursor.execute(query)
        self.insertData(relatorio)
        return relatorio, rules

    def update(self,id,colum,perm,cond):
        cursor = self.cnx.cursor()
        query = "update clients set {} = '{}' where {} = {}".format(colum,perm,cond,id)
        cursor.execute(query)
        self.cnx.commit()