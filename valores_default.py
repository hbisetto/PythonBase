import time

def imprime_nome(nome, sobrenome='Sabugosa'):
    print(f'Olá, seu nome é {nome} {sobrenome}')

imprime_nome('Henrique', 'Bisetto')
imprime_nome('Thales')
imprime_nome('Helga')

def conecta(host, timeout=10):
    print(f'Conectando com {host}')
    for i in range(1, timeout + 1):
        time.sleep(1)
        print('.' * i)
    print('Erro ao conectar')


conecta('localhost')
