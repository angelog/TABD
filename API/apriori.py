import pandas as pd 
from apriori_2 import apriori_2
#basket_data = pd.read_csv(r'C:\Users\angel\OneDrive\Documentos\Fatec\IA\artificial_intelligence-master\artificial_intelligence-master\unsupervised_learning\apriori\relatorio.csv')

def apriori(df,transaction, item, sup, conf):
    item_by_transaction = df.groupby(transaction)[item].apply(list)
    print(item_by_transaction)
    itemset = df[transaction].unique()
    rules = apriori_2(itemset, item_by_transaction, sup, conf)

    print(rules[1])
    return rules[1]