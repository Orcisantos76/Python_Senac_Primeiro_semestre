lista = []# [] significa que ali tem uma lista
for x in range(2):# enquanto x dentro do range(4)--range = intervalor -- x é a vez que esta contando, tipo 0, 1, 2
    n = input("Digite algo: ") # n recebe um input(entrada
    lista.append(n) # lista receberá o que está em .append(n)
print (lista)


nome = []
idade = []

for x in range(4):
    n = input("digite o nome:")
    nome.append(n)
    i = int(input("Digite sua idade"))
    idade.append(i)
    x = x + 1

print(nome)
print(idade)
print (x)
