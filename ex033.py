a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite um terceiro valor: '))
#Verficando quem e o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verficando quem e o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


