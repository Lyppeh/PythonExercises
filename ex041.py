from datetime import date
nasc = int(input('Qual a sua data de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('Esse atleta tem {} anos e ele é MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Esse atleta tem {} anos e ele é INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Esse atleta tem {} anos e ele é JUNIOR'.format(idade))
elif idade > 19 and idade <=25:
    print('Esse atleta tem {} anos e ele é SÊNIOR'.format(idade))
else:
    print('Esse atleta tem {} anos e ele é MASTER'.format(idade))
