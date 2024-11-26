""" Exemplos de funções """

"""
Funções matemáticas. Exemplo:
f(x) = 5 * (x / 2)
"""
from math import sqrt

def f(x): # assinatura da função
    return 5 * (x / 2)

def double(x):
    return x * 2

valor = double (f(10))
print(valor)
print(f(10) == 25)

###

# Procedimentos / Procedures -- Não tem retorno
def print_in_upper(text):
    print(text.upper())

print_in_upper('henrique')

###

def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return sqrt(area) # ou area ** 0.5

# area_triangulo = heron(3, 4, 5)
# print(area_triangulo)

def heron2(params):
   return heron(*params) #  a, b, c = params

 
triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (34, 35, 42)
]

print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron(*t) # = heron(t[0], t[1], t[2])
    print(f'A area do triangulo é: {area}')

for t in triangulos:
    area = heron2(t)
    print(f'A area do triangulo é: {area}')
