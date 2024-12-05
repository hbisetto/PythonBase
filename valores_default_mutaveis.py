# mutáveis: set, dict, list

""" Exemplos de mutáveis:
s = set()
s.add(1)

d = {}
d["key"] = "value"

l = []
l.append(0)"""

""" Os arquivos podem ser adicionados no mesmo objeto mutável por ENGANO. Tomar cuidado!"""

def adiciona_a_lista(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista

adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista([4, 3, 5]))
print(adiciona_a_lista(6))

