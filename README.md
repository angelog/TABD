# **Tópicos Avançados de Banco de Dados.**
 ## Anonimização
 ### O que é anonimização de dados?
- A anonimização é um método de preservação de informações privadas ou confidenciais por meio da exclusão ou codificação de identificadores que vinculam indivíduos aos dados armazenados. Sua finalidade é garantir a privacidade de uma pessoa ou empresa, preservando a credibilidade dos dados coletados e eventualmente repassados.
- Lei Geral de Proteção de Dados brasileira, a LGPD, no inciso XI do art. 5º, anonimização é: 
“utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo”.

**Objetivo** : Desenvolver uma API para anonimalização de dados, na intenção de gerar relatórios sem nenhum perigo de violar a segurança dos dados pessoais do cliente.
## Para Execução da API
- Bibliotecas necessárias para a execução:
```
pip install flask
pip install pandas
pip install mysql-connector-python
```

## Sistema de recomendação
- Para o uso do sistema de recomendação, recomenda-se usar para relatório de vendas, pois mesmo com a anonimização, ira conseguir ter recomendações de produtos pelas transações feitas.

## Execução
1. Execute o arquivo config.py para iniciar a configuração da sua API
   - Nele ira informar os dados do banco de dados que será usado e ira conter a estrutura do relatório que será exportado.
2. Após a configuração a API já estará operando
   - Usando a rota **"/relatorio"**, retornara o relatório.
   - Caso tenha optado pelo uso do sistema de recomendação, retornara recomendaçãos de acordo com os parametros definidos
   - Cada chamada de relatório e feito a inserção do mesmo no banco de dados para histórico de chamadas
