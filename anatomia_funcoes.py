""" 
Este módulo serve apenas de anotação.
"""

# definição ou atribuição
## def nome_funcao
# assinatura + type hints
## o que tem entre () e os :
# documentação  /   docstring
## escrito entre '''
# codigo
# valor de retorno

def nome_funcao(a: int, b: int, c: int) -> int:
    """ 
    Documentação da Função
    O que a função faz?
    
    Use esta função quando quiser...
    [Detalhes sobre os parâmetros e suas funcionalidades]
    
    Documentation Strings (está caindo em desuso)
    :param a: Numero inteiro
    :type a: int
    :param b: Numero inteiro
    :type b: int
    :param c: Numero inteiro
    :type c: int
    :return: Retorna o resultado de a + b + c
    :rtype : int
    
    >>> nome_funcao(1, 2, 3)
    6
    """
    
    return a + b + c

print(nome_funcao(1, 2, 3))