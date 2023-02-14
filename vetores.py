# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

vetora= [4,6,8,9,7,15,26,35,24,36]
soma = 0
vetorb =[]
for item in vetora:
    soma += item * item
    vetorb.append(item * item)
print(f"A soma dos quadrados dos elementos é  {soma}")
print(vetorb)

print("-="*30)
vetorc = [1,3,5,7,9,11,13,15]
vetord = [2,4,6,8,10,12,14,16]
vetore = []
x = len(vetorc)
for indice in range(len(vetorc)):
    vetore.append(vetorc[indice])
    vetore.append(vetord[indice])
print(vetore)

print("-="*30)

"""
Faça uma função que receba uma string como parâmetro e
retorne a quantidade de palavras existente nesta string."""

frase = input("Digite uma frase: ")
print(f"A sua frase tem {len(frase.split())} palavras")
print(f"A sua frase tem {frase.count(' ')+1}")

print("-="*30)

