# for
# print("Antes do FOR")
# #             inicio, fim, incremento
for x in range(4,      10,    2):# 4 é o inicio, 10 é o final, 2 é o incremento
    print(x,"Lógica")
print("Depois do FOR")


print("-=-while"*6)

print("Antes do WHILE")
x = True
while x:
    nome = input("Digite seu nome: ")
    if nome == "fim":
        break  # finaliza o laço
    print(x, nome)

print("Depois do WHILE")


# Faça um algoritmo para fazera figura abaixo
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# """
print("Exemplo 1: ")
for l in range(10):# Enquanto l (linha) no range 10, contará 10 linhas
    for c in range(10):# enquanto c (contador) no range 10
        print("#",end="")# aqui ira imprimir sem quebrar a linha por causa do end=""
    print()
"""
Faça um algoritmo pqra fazera figura abaixo
#
##
###
####
#####
######
#######
########
#########
"""
qt = int(input("Digite quantas linhas voce quer (1-30): "))
if qt > 0 and qt < 30:
    for linha in range(1, qt+1):# linha é o contador, 1 é o inicio, qt=1 é o final da contagem.
        print("#"*linha)
else:
    print("valor fora do intervalo: ")



