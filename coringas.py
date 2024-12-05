""" Recaptulação das possibilidades de passar parâmetro para a função:
def soma(a, b):
    return a + b

soma(1, 3)
soma(1, b=3)

def hello(nome, sobrenome='Sabugosa'):
    print(f'Hello {nome} {sobrenome}')

hello('Helga', 'Peres')
hello('Helga')
hello('Helga', sobrenome='Peres')
hello(sobrenome='Peres', nome='Helga')
"""

# Utilizando argumentos coringas

def funcao(*args, timeout=10): # a convenção é o nome *args com os argumentos empacotados
    for item in args:
        print(item)

    print(f'timeout {timeout}')

def funcao2(*args, timeout=5, **kwargs): # keywords arguments, convenção; usar 2 *
    for item in args:
            print(item)

    print(kwargs) 
    
    print(f'timeout {timeout}')

funcao('Henrique', 1, True, [])
print('-' * 30)
funcao('Thales', 12, False, timeout=30)
print('-' * 30)
funcao2('Henrique', 1, True, timeout=40, nome='Helga', cidade='Capivari', data='hoje')
print('-' * 30)




