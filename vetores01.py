#Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão
# ser compostos pelos elementos
# intercalados dos dois outros vetores.
# considerando os vetores já inicializados
# se preferir, pode digitá-los também
vetorA = [11, 22, 33, 44, 55, 66, 77, 88, 99, 55]
vetorB = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetorC = []
for elemento in range (10):
    vetorC.append(vetorA[elemento])
    vetorC.append(vetorB[elemento])
print(vetorC)

print("-="*30)

"""
Faça uma função que receba uma string como parâmetro e
retorne a quantidade de palavras existente nesta string.
"""
texto = ("Orci santos") #str(input("Digite uma frase: ")).lower()
def qt_palavras(frase):
    return len(frase.split())
print(qt_palavras(texto))

print("-="*30)

"""
Faça uma função que receba um número e retone True, caso o 
número seja inteiro e False caso não seja um inteiro.
"""
n = float(input("Digite um valor: "))
def inteitro():
    if n % 1 == 0:
        print('Numero inteiro')
        return True
    else:
        print('Numero flutuante')


inteiro()