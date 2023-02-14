"""
Faça um
 algoritmo que leia vários números inteiros de 2 digitos.
Se o número lido estiver no intervalor entre 20 e 70, adicione em uma lista.
"""

intervalo = []
print("Digite nada para encerrar. ")
while True:
    n = (input("Digite um numero: "))
    if len(n) == 0:# conta o numero de caracteres dentro da variavel recebida.
            break
    n = int(n) # transforma o imput recebido em inteiro
    if n >= 100:
        print("Os números digitados não podem ter mais que dois digitos")

    if n > 20 and n < 70:
        intervalo.append(n)
print(f"os números no intervalo são {intervalo}")

