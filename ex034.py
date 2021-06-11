salario = float(input('Digite seu salário para saber o aumento: R$  '))
if salario > 1250:
    aumento = (salario*10/100)
    salario = aumento + salario
    print('O aumento no seu salario será de R${:.2f}, e você irá passar a receber R${:.2f}'.format(aumento, salario ))
else:
    aumento = (salario*15/100)
    salario = aumento + salario
    print('O aumento no seu salário será de R${}, e você irá passar a receber R${}'.format(aumento, salario))

