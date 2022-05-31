from flask import Flask, request
import bd
import pandas as pd 
import json
    
class API():
    def __init__(self):
        with open('data.json', 'r') as fp:
            data = json.load(fp)

        self.user=data['baseconfig'][0] 
        self.password=data['baseconfig'][1] 
        self.host=data['baseconfig'][2]
        self.database=data['baseconfig'][3]
        del data['baseconfig']
        self.view=data['view'][0] 
        self.flag=data['view'][1]
        del data['view']
        self.colunas =data['colunas'] 
        del data['colunas']
        self.apri = data['apriori']
        del data['apriori']
        if self.apri is True:
            self.transaction = data['transaction']
            self.item = data['item']
            self.sup = float(data['suporte'])
            self.conf = float(data['confianca'])
            del data['transaction']
            del data['item']
            del data['suporte']
            del data['confianca']

        for key in data:
            data[key] = pd.Series(data[key])

        self.df = pd.DataFrame(data=data)
        self.run()


    def run(self):   
        app = Flask('API')

        @app.route('/update',methods=['POST'])
        def update():
            vars = request.get_json()
            bd.database(self.user, self.password, self.host, self.database).update(vars['clientsID'],vars['coluna'],vars['update'],vars['cond'])
            return '<h1> clientsID: {}, {} atualizado para => {} </h1>'.format(vars['clientsID'],vars['coluna'],vars['update'])

        @app.route('/relatorio',methods=['GET'])
        def getRelatorio():
            if not self.apri:
                result, rules = bd.database(self.user, self.password, self.host, self.database).relatorio(self.df,self.view,self.flag,self.colunas)
            else:
                result, rules = bd.database(self.user, self.password, self.host, self.database).relatorio(self.df,self.view,self.flag,self.colunas,
                 self.apri, self.transaction, self.item, self.sup, self.conf)
            linhas = ''
            colunas =''
            for i ,row in result.iterrows():
                linhas = linhas + '<tr>'
                for line in row:
                    linhas = linhas + '<td>{}</td>'.format(line)
                linhas = linhas +'</tr>'

            for col in result.columns.tolist():
                colunas = colunas + '<th>{}</th>'.format(col)
            return "<table> <tr> {}</tr> {} </table><br><p>{}</p>".format(colunas,linhas,rules)

        app.run(debug=True)

if __name__ == '__main__':
    API()
