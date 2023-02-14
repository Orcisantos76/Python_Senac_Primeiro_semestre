'''
Faça um algoritmo que leia, para  8 pessoas, seus
nomes e idades.
Após, mostre o nome e a idade da pessoa mais nova.
obs. Não utilizar listas.
'''
"""
idade_mais_novo = 0
nome_mais_novo = ""
for pessoas in range (3):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    if idade < idade_mais_novo or pessoas == 0:
        idade_mais_novo = idade
        nome_mais_novo = nome
print(f"O nome da pessoa mais nova é {nome_mais_novo} e essa pessoa tem {idade_mais_novo} anos.")

lista_nomes = []
lista_idades = []
for qt in range (3):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    lista_nomes.append(nome)
    lista_idades.append(idade)
print(lista_nomes)
print(lista_idades)
idade_m_novo = min(lista_idades)# menor da lista idades
for indice, elemento in enumerate(lista_idades):
    if idade_m_novo == elemento:
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
"""

dados = dict()
cadastro = ()
for pessoas in range(3):
    dados["nome"] = (str(input("Digite seu nome: ")))
    dados['idade'] = (int(input('Digite sua idade: ')))
    cadastro.append(dados)
print(dados)
print(cadastro)


