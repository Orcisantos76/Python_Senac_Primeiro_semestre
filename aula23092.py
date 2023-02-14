# Faça um algoritmo que leia o nome e a idade de um conjunto
# de nadadores e, a partir da idade classifique-os em uma das
# seguintes categorias:
# infantil A = 5 - 7 anos
# infantil B = 8 - 10 anos
# juvenil A = 11 - 13 anos
# juvenil B = 14 - 17 anos
# adulto = maiores de 18 anos
# O programa deve terminar quando o nome for = “FIM”

# infantil A = 5 - 7 anos
qt_infantil_A = 0
lista_infantil_A = []
nome_infantil_a =[]
soma_infantil_a = []

# infantil B = 8-10 anos
qt_infantil_B = 0
lista_infantil_B = []
nome_infantil_b = []
soma_infantil_b = []

# juvenil A = 11-13 anos
qt_juvenil_A = 0
lista_juvenil_A = []
nome_juvenil_a = []
soma_juvenil_a = []

# juvenil B = 14-17 anos
qt_juvenil_B = 0
lista_juvenil_B = []
nome_juvenil_b = []
soma_juvenil_b = []

# adulto = maiores de 18 anos
qt_adulto = 0
lista_adulto = []
nome_adulto = []
soma_adultos = []

print ("teclar enter vazio encerra")
while True:
    nome = str(input("Digite seu nome: ")).capitalize()
    if nome == "":
        break
    idade = int(input("Digite sua idade: "))

    if idade >= 5 and idade <=  7:
        idade = idade
        qt_infantil_A = qt_infantil_A + 1
        lista_infantil_A.append(idade)
        nome_infantil_a.append(nome)
        soma_infantil_a.append(idade)

        print(str(f"{nome}, é atleta da catergoria Infantil A"))

    if idade >= 8 and idade <=  10:
        qt_infantil_B = qt_infantil_B + 1
        lista_infantil_B.append(idade)
        nome_infantil_b.append(nome)

        print(str(f"{nome}, é atleta da catergoria Infantil B"))

    if idade >= 11 and idade <=  13:
        qt_juvenil_A = qt_juvenil_A + 1
        lista_juvenil_A.append(idade)
        nome_juvenil_a.append(nome)

        print(str(f"{nome}, é atleta da categoria Juvenil A"))

    if idade >= 14 and idade <=  17:
        qt_juvenil_B = qt_juvenil_B +1
        lista_juvenil_B.append(idade)
        nome_juvenil_b.append(nome)

        print (str(f"{nome}, é atleta da categoria Juvenil B "))

    if idade >= 18:
        qt_adulto = qt_adulto +1
        lista_adulto.append(idade)
        nome_adulto.append(nome)


        print (str(f"{nome}, é atleta da categoria adulto."))

print ("Na categoria infantil A temos ",(len(lista_infantil_A)), "participantes")
print ("Na categoria infantil B temos ",(len(lista_infantil_B)), "participantes")
print ("Na categoria juvenil A temos ",(len(lista_juvenil_A)), "participantes")
print ("Na categoria juvenil B temos ",(len(lista_juvenil_B)), "participantes")
print ("Na categoria adulto temos ",(len(lista_adulto)), "participantes")

print("Na categoria infantil A os participantes são: {}".format(nome_infantil_a[0:]))
print("Na categoria infantil B os participantes são: {}".format(nome_infantil_b[0:]))
print("Na categoria juvenil A os participantes são: {}".format(nome_juvenil_a[0:]))
print("Na categoria juvenil B os participantes são: {}".format(nome_juvenil_b[0:]))
print("Na categoria adulto os participantes são: {}".format(nome_adulto[0:]))

print ("A media entre as idades da categoria Infantil A é",(sum(lista_infantil_A)/len(lista_infantil_A)))
print ("A media entre as idades da categoria Infantil B é",(sum(lista_infantil_A)/len(lista_infantil_A)))
print ("A media entre as idades da categoria Juvenil A é",(sum(lista_juvenil_A)/len(lista_juvenil_A)))
print ("A media entre as idades da categoria Juvenil B é",(sum(lista_juvenil_B)/len(lista_juvenil_B)))
print ("A media entre as idades da categoria Adulto é",(sum(lista_adulto)/len(lista_adulto)))