"""
Programa que repete as vogais das palavras escritas pelo usuário.
Ex.:
'Digite uma palavra (ou enter para sair): ' Python
> Pythoon

"""

lista = []
lista_por_palavra = []
nova_lista = []
situacao = True
vogais = ('a', 'e', 'i', 'o', 'u')

while situacao:
    palavra = input('Digite uma palavra (o enter para sair): ')

    if palavra:
        lista.append(palavra)
    else:
        situacao = False

    print(lista)

for item in lista:      
    tamanho = len(item)
    n = 0
    lista_por_letra = []
    for n in range(tamanho):
        lista_por_letra.append(item[n])
    print(lista_por_letra)
    lista_para_add = lista_por_letra
    lista_por_palavra.append(lista_para_add)

palavra_vogal_adicionada = ""
for item in lista_por_palavra:
    palavra_vogal_adicionada = item
    tamanho = len(item)
    for n in range(tamanho):
            provisorio = palavra_vogal_adicionada[n:tamanho]
            comeco = palavra_vogal_adicionada[0:n]
            if palavra_vogal_adicionada[n] in vogais:
                nova_palavra = split(palavra_vogal_adicionada)
    
    print(nova_palavra)                
                

    
