# Faça um algoritmo que leia, para  8 pessoas, seus nomes e idades.
# Após, mostre o nome e a idade da pessoa mais nova.
# obs. Não utilizar listas.



# idademenor = 0
# nome_mais_novo = ""
# for qt in range (3):
#     nome = str(input("Digite seu nome: "))
#     idade = int(input("Digite sua idade: "))
#
#
#     if idade < idademenor or qt == 0:
#         idademenor = idade
#         nome_mais_novo = nome
# print (f"Nome da pessoa mais nova : {nome_mais_novo}"
#         f"com a idade de {idademenor}")
#

   ### Lista
lista_nomes=["orci","andré", "ana","juliano","Arthur"]
lista_idade=[46, 10, 43, 42, 10]
'''
Faça um algoritmo que leia, para  8 pessoas, seus
nomes e idades.
Após, mostre o nome e a idade da pessoa mais nova.
obs. Não utilizar listas.
'''

# Ler 8 nomes e idades
# Mostrar o nome e a idade de quem é mais novo
#
# idade_mais_novo = 0
# nome_mais_novo = ""
#
# for qt in range(8):
#     nome = input("Digite o nome: ")
#     idade = int(input("Digite a idade: "))
#
#     if idade < idade_mais_novo or qt == 0 :
#         idade_mais_novo = idade
#         nome_mais_novo = nome
#
# print(f"Nome da Pessoa mais nova: {nome_mais_novo} "
#       f"com a idade de {idade_mais_novo}")
#

lista_nomes = []
lista_idades = []
lista_nomes = ["ana","maria", "joao", "Pedro", "Luiz", "Juca"]
#                0      1       2       3        4       5
lista_idades = [18,    22,      45,     27,      18,    32]


# for qt in range(8):
#     nome = input("Digite o nome: ")
#     idade = int(input("Digite a idade: "))
#
#     lista_nomes.append(nome)
#     lista_idades.append(idade)


print(lista_nomes)
print(lista_idades)
# como saber quem é o mais novo?

idade_mais_novo = min(lista_idades)
for indice, elemento in enumerate(lista_idades):
    if idade_mais_novo == elemento:
        print(f"Nome: {lista_nomes[indice]} - {elemento}")



# idade_mais_novo = 999
# for elemento in lista_idades:
#     if elemento < idade_mais_novo:
#         idade_mais_novo = elemento
#
# print("Idade Mais Novo:", idade_mais_novo)
#
# for indice in range(len(lista_idades)):
#     if idade_mais_novo == lista_idades[indice]:
#         print(f"Nome: {lista_nomes[indice]} - {lista_idades[indice]}")
#

