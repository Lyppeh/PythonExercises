print('-='*25)
print('ANALIZADOR DE TRIÂNGULOS')
print('-='*25)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar uma TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM formar uma TRIÂNGULO')

