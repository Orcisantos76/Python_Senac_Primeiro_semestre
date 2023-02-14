"""

Faça um algoritmo que leia o nome e a idade
de 10 pessoas.
lista_nomes
lista_idades

# Crie uma função para cada lista
"""

# lista_nomes = []
# lista_idades = []
#
# while True:
#     nome = input("Nome: ")
#     if not nome: break
#
#     idade = input("Idade: ")
#     lista_nomes.append(nome)
#     lista_idades.append(idade)


lista_nomes = []
lista_idades = []

def adiciona_nome(nome):
    lista_nomes.append(nome)

def adiciona_idade(idade):
    lista_idades.append(idade)

def adicionar_dados(nome, idade):
    adiciona_nome(nome)
    adiciona_idade(idade)

def ler_teclado(mensagem):
    return input(mensagem+">>>: ")

while True:
    print('Digitar 999 encerra: ')
    nome = ler_teclado("Nome")
    if nome == 999:
        break
    idade = ler_teclado("Idade")
    if idade == 999:
        break

    adicionar_dados(nome, idade)



# lista_nomes = []
#
# for x in range(5):
#     nome = input("Nome: ")
#     # Se o nome existir, imprima as letras do nome uma
#     # em baixo da outra
#     if nome in lista_nomes:
#         for letra in nome:
#             print(letra)
#         # lista_nomes.remove(nome)
#         continue
#     lista_nomes.append(nome)
#
# print(lista_nomes)

lista_nomes = []

for x in range(5):
    nome = input("Nome: ")
    # Se o nome existir:
    # imprima o nome substituindo as vogais por '*'

    novo_nome = ""
    if nome.lower() in lista_nomes or \
       nome.upper() in lista_nomes:
        for letra in nome:
            if letra in "aeiouAEIOU":
                novo_nome += "*"
            else:
                novo_nome += letra
        print(novo_nome)
        input()
        continue

    # OU assim

    if nome.lower() in lista_nomes or \
       nome.upper() in lista_nomes:
        for vogal in 'aeiouAEIOU':
            nome = nome.replace(vogal,'*')
        print(nome)
        continue
    lista_nomes.append(nome)

print(lista_nomes)