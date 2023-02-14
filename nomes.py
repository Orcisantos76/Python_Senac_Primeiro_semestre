lista_nomes = []

for x in range(5):
    nome = input("Digite seu nome: ")
    if nome in lista_nomes:
        #lista_nomes.remove(nome) # se o nome ja existir na lista remove o nome.
        for x in nome:
            print(x)
        continue# continua o programa, break pararia aqui, e o pass passaria o programa e adicionaria o nome na lista
    lista_nomes.append(nome)
print(lista_nomes)

if x in lista_nomes:
    print(x)