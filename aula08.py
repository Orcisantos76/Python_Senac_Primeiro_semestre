# Faça um algoritmo que leia um conjunto indeterminado de
# números inteiros e mostre uma mensagem indicando se este
# número é par ou ímpar, e se é positivo ou negativo.
# Terminar o programa quando o numero lido for 0 (Zero).

# x = 0
# while x != 0:
#     n = int(input("Digite um numero: "))

num1030= []
num5070= []
impares= []
percentual = []
percentualimpares = []

while True:
    n = int(input("Digite um número: "))
    if n == 0: break
    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n}, é impar")
    print (n)
    if n > 0:
        print("número positivo")
    else:
        print("O número é negativo")
    if n > 10 and n < 30 and n % 2 == 0:
        num1030.append(n)
    if n > 50 and n < 70 and n % 2 == 0:
        num5070.append(n)


    if n > 25 and n < 60 and n % 2 ==0:
        percentual.append(n)
    if n > 25 and n < 60 and n % 2 ==1:
        impares.append(n)
print("os numeros pares entre 10 e 30 são:",(num1030))
print("Ha um total de",(len(num1030))," números nesta lista.")
print (num5070)
print (len(num5070))
print(impares)
print (percentual)
print(percentualimpares)




