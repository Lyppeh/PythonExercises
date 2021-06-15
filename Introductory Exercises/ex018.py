import math
an = float(input('Digite um angulo: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))

