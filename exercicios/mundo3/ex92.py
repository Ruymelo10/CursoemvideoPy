from datetime import datetime
nome = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
catra = int(input('Carteira de Trabalho (0 se não tem): '))
dados = {'nome':nome,'ano':ano,'carteira de trabalho':catra}
idade =  datetime.now().year - ano
dados['ano']=idade
if dados['carteira de trabalho']!=0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['ano de contratação']+35
print(dados)