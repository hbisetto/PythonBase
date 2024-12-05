contador = 0

def funcao():
    global contador  # Não é recomendável utilizar global com frequência
    contador += 1

    subcontador = 0

    def funcao_interna():
        global contador
        contador += 1

        nonlocal subcontador  # pouco utilizado
        subcontador += 1

    funcao_interna()

funcao()
funcao()

print(contador)
    
