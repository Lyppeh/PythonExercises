sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('DADO INVALIDO. Por favor, informe seu sexo [M/F]: '))
print('Sexo {} registrado com suscesso!'.format(sexo))
