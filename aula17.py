"""
revisao, Listas
"""
lista = []
lista1 = list()
lista.append(121)
lista.insert(5,33)# precisa ter alguem na posição 5 para dar certo.
print(lista)
lista =[121,1212,123123]

##################################################
lista.remove(121) # tira o elemento 121 da lista
lista.pop(0) # retira pelo indice, se não existir o indice vai dar erro, sem referencia, vai retirar o ultimo


# ##################################################
# lista = [1,2,3,4,4,4,5,6,7,8,9]
# x = lista.index(5) # acha a posição do elemento na lista e guarda dentro do X
# print(lista.index(5))
# print(x)
# print(f"A quantidade de numeros 4 é {lista.count(4)}")
#
# ###################################################
#
# alunos = ['orci','ivo', 'pedro', 'maria', 'nei', "ana"]
# idades = [46,56,24,15,24,19]
# while True:
#     nome = input(" nome para localizar: ")
#     if nome in alunos:
#         print(f"Nome: {nome} - {idades[alunos.index(nome)]}")
#                                 # lista idades.posição aluno.index(nome é o elemento)
#

    # if nome not in alunos:
    #     print("Não ta na lista")
    #     continue
    #
    # for n in range(len(alunos)):
    #     if alunos[n] == nome:
    #         print(f"nome: {nome} - {idades[n]}")

#############################################

# #     FUNÇAO:
# print('Sou um parametro', 44)
# input()
# len()
# int()
# float()
# bool()
# str()
# range()
#
# #   COMANDOS:
#
# while
# if
# for
# break
# pass
# continue

def soma(a, b):
    #a = 5
    #b = 4
    r = a + b
    return r
    print(r)
res = soma(10,12) # recebe o return

print(soma(10,12))
soma(1,2)
soma(122,13)