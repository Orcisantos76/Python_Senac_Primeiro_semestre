lista1 = [11,22,33,44]
lista2 = ["aa","bb","cc","dd"]

lista1[2] = 99# aqui mostra que posso alterar o item 2 da lista 2

txt = "Orci Santos"

for x in range (len(lista1)):
    print (lista1[x], lista2[x])

for indice in range(len(txt)):
    print(indice, end=" ")
    print(txt[indice])