from datetime import date
nascimento = int(input('Em que ano você nasceu?: '))
ano = date.today().year
if ano - nascimento <= 17:
    print('Você ainda tera que se alistar e falta {} anos'.format(18 - (ano - nascimento)))
elif ano - nascimento == 18:
    print('Ja esta na hora de você se alistar')
else:
    print('Já se passou do tempo de alistamento {} anos'.format((18 - (ano - nascimento))* -1))
