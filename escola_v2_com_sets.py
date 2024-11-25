#! usr/bin/env python3
"""
Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Henrique Bisetto"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), # tupla -> texto + lista
    ("Música", aula_musica),
    ("Dança", aula_danca),
]
# Acima foi usado uma tupla com nome e identificação [que é uma outra lista]

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
                
    # sala1 que tem interseção com a atividade
            
        
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)
    
    print("Sala 1", atividade_sala1)
    print("Sala 2", atividade_sala2)

    print("#" * 40)

