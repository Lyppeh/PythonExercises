peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Diite sua altura: (M) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal')
elif imc >= 18.5 and imc < 25:
    print('Você está NO PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está ACIMA DO PESO ideal')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MORBITA! Cuidado')


