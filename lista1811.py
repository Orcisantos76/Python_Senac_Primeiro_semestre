"""faca um algoritmo que leia o nome e a idade de 10 pessoas."""
nomes=[]
idades=[]
def lista_nomes():
    for x in range(2):
        nome = input("Digite seu nome: ")
        nomes.append(nome)
        idade = int(input("Digite sua idade: "))
    idades.append(idade)
print(nomes, idades)
lista_nomes()
print(nomes)
print(idades)


nome =["orci", "Joao", "pedro", "adao"]
print(nome)

for palavra in nome:
    vogais = []
    for letra in palavra:
        if letra.lower() in "aeiou":
            vogais.append(letra)

    print(f"Na palavra {palavra} temos as seguintes vogais {vogais}")
