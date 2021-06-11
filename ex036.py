valor = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o seu salario: R$ '))
anos = float(input('Em quantos anos você ira pagar: '))
prestaçao = valor / (12 * anos)
aprovaçao = salario * 30 / 100

if prestaçao > aprovaçao:
    print('{}EMPRÉSTIMO NEGADO!!!{} O valor da prestaçao tem que ser menor que 30% do seu salário!'.format('\033[1:31m', '\033[m'))
else:
    print('{}EMPRÉSTIMO ACEITO!!!{}'.format('\033[32m', '\033[m' ))
    print('O empréstimo tera parcelas mensais de R${:.2f} por mês!'.format(prestaçao))



