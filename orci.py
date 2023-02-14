"""
Questão 1:
Faça um algoritmo que leia 2 números inteiros e verifique:
Se o primeiro número for menor que o segundo número, mostre
    todos os números inteiros entre o primeiro e o segundo de
    forma decrescente. (Não incluir os números digitados)
    Caso a diferença entre eles seja apenas
    1, mostre a mensagem:
    "NÃO HÁ NÚMEROS INTEIROS ENTRE O INTERVALO DIGITADO!"

Se o primeiro número for maior que o segundo número, mostre
    a diferença entre eles (primeiro - segundo).

Se os números forem iguais mostre a seguinte mensagem:
    "NÚMEROS NÃO PODEM SER IGUAIS", e leia novamente os 2 números.
"""

n1 = 0
n2 = 0
cont = 0
iguais = 0
while True:
    print("-=-"*30)
    print("Digitar um número negativo ira encerrar.")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    if n1 == n2:
        iguais += 1
        print("NÚMEROS NÃO PODEM SER IGUAIS.")
        if iguais == 3:
            break
    if n1 < 0 or n2 < 0:
        break
    listax = []
    listainv = []
    cont = 0
    if n2 < n1:
        for c in range(n1 - 1, n2, -1):
            listainv.append(c)
            cont += 1
        print((f"Os números inteiros entre {n1} e {n2} são {listainv}"))
    if n1 < n2:
        for x in range(n1+1,n2):
            listax.append(x)
        print(f"Os números inteiros entre {n1} e {n2} são {listax}")
    if n2 == n1+1:
        print("NÃO HÁ NÚMEROS INTEIROS ENTRE O INTERVALO DIGITADO!.")
    if n1 == n2+1:
        print("NÃO HÁ NÚMEROS INTEIROS ENTRE O INTERVALO DIGITADO!.")

