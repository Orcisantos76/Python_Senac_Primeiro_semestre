"""
Faça uma função que receba como parâmetro uma lista.
(este parâmetro pode ter tipos de dados diferentes.)
Retorne uma lista com todos os números float existentes no
parâmetro.
Caso não exista nenhum número float no parâmetro, retorne
a seguinte mensagem: 'SEM NÚMEROS REAIS' "
"""

def valida_lista(lista): #lista não precisa ser declarada antes, como é um argumento, tudo que colocar em parenteses, sera lido
    reais = [] #criei a lista que receberá os numeros reais
    for x in lista: # para cada elemento na lista
        if type(x) == float: # se o tipo de elemento x for igual a float entao
            reais.append(x)# reais recebe x
    if not reais:
        return "SEM NÚMEROS REAIS"
    return reais

print(valida_lista(["aa", 123, True, "22", "3,5", 4.75, [], 4]))
#valida_lista(["aa", 123, True, "22", "3,5", 4.75, [], 4])

