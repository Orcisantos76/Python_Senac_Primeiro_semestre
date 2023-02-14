"""
Faça um algoritmos que leia até 5 frases.
Para cada frase digitada você deverá:
   - mostrar quantos caracteres existem na frase digitada. (inclusive os espaços em branco)
   - mostrar quantas vogais existem na frase.
   - mostrar qual o percentual de letras 'a' ou 'A' existem na frase.

Critérios:
- Não aceitar frase com menos de 5 caracteres, nem mais que 200 caracteres.
- Não aceitar frase que contenha "0,1,2,3,4,5,6,7,8 ou 9"
"""
# # for vai repetir tudo que estiver identado dentro dele.
# x = 0
# while x < 5:
#     w = x * 4
#     print (w)
#     x = x +1
contador = 0
while True:
    w = input("Digite algo: ")
    contador = contador + 1
    if w == "fim":
              break
    print("Você digitou: ",w)
    print("jeito 1: Você digitou ", contador, "vezes")
    print("jeito 2: Voce digitou {} vezes".format(contador))
    print(f" jeito 3: Voce digitou {contador} vezes")


# for x in range(5):
#     w = x * 4
#     print (w)
#
# print (range(7))
# Exemplo de programa em python
# print("Olá Pessoal")
# print("Este é outro exemplo de fluxo de execução do programa.")
# print("------------------------------------------------------")
# print("Digite um número no teclado e aperte o enter: ")
# numero_lido = input()
# if int(numero_lido) >= 10:
#     print("Este número é maior que 10.")
#     if int(numero_lido) < 100:
#         print("Posso afirmar que:")
#         print("  Esse número também é menor que 100.")
#     if int(numero_lido) == 10:
#         print("Bacana. Entendi.")
#         print("  Esse número é o próprio 10.")
# elif int(numero_lido) >= 0:
#     print("Ok. O número digitado está entre 0 e 9.")
#
# else:
#     print("Entendi. Você digitou um número negativo.")
#
# print("Fim do Exemplo.")


"""
Fazer um algoritmo para ler dois números e mostrar o maior deles.
"""

qt = int(input("Quantas vezes? "))
for x in range(qt):
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))

    if num1 > num2:
        print("O maior é num1:", num1)
    elif num2 > num1:
        print("O maior é num2:", num2)
    else:
        print("São iguais.")





# if num1 > num2:
#     print("O maior é num1:", num1)
# else:
#     if num2 > num1:
#         print("O maior é num2:", num2)
#     else:
#         print("São iguais.")

# if num1 > num2:
#     print("O maior é num1:", num1)
# if num2 > num1:
#     print("O maior é num2:", num2)
# if num1 == num2:
#     print("São iguais.")





#Item
#exercício 7 feito em aula
"""
Ler 3 números e imprimi-los em ordem crescente.
"""
n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
n3 = int(input("Digite n3: "))

if n1 > n2 and n1 > n3 and n2 >  n3:
            print(n3,n2,n1)
if n1 > n2 and n1 > n3 and n3 >  n2:
            print(n2,n3,n1)
if n2 > n1 and n2 > n3 and n1 > n2:
            print(n3,n1,n2)
if n2 > n1 and n2 > n3 and n3 > n1:
            print(n1,n3,n2)
if n3 > n1 and n3 > n2 and n2 > n1:
            print(n1,n2,n3)
if n3 > n1 and n3 > n2 and n1 > n2:
            print(n2,n1,n3)

# if n1 > n2 and n1 > n3:
#         if n2 >  n3:
#             print(n3,n2,n1)
#         else:
#             print(n2,n3,n1)
#
# elif n2 > n1 and n2 > n3:
#         if n1 > n2:
#             print(n3,n1,n2)
#         else:
#             print(n1,n3,n2)
#
# else:
#         if n2 > n1:
#             print(n1,n2,n3)
#         else:
#             print(n2,n1,n3)
#

# =========== usando lista
# n1 = int(input("Digite n1: "))
# n2 = int(input("Digite n2: "))
# n3 = int(input("Digite n3: "))
#
# lista = [n1, n2, n3]
# #        0 , 1 , 2
#
# lista.sort()
# print("Elementos individuais: ")
# for x in range(3):
#     print(">>", lista[x])
#
# print("\nlista completa:")
# print(lista)
# """
# Faça um algoritmo que leia valores para as variáveis a, b e c e
# mostre o resultado da seguinte
# expressão:
# ( a – b ) * c
# """
#
# a = int(input("Digite a: "))
# b = int(input("Digite b: "))
# c = int(input("Digite c: "))
#
# resultado = (a - b) * c
#
# print(f"Resultado= {resultado}")
# Item
# Exercício feiro em aula - 09
# """
# Fazer um algoritmo para ler duas notas, os pesos de cada nota e
# mostrar a média ponderada.
#                                 (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
# Cálculo da Média Ponderada = ------------------------------------------------------------------------
#                                         soma dos pesos
# """
# nota1 = float(input("Digite nota1: "))
# peso1 = float(input("Digite peso1: "))
#
# nota2 = float(input("Digite nota2: "))
# peso2 = float(input("Digite peso2: "))
#
# media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1+peso2)
#
# print(f"Média Ponderada = {round( media_ponderada, 2 )}")
# print("Média Ponderada = {round( media_ponderada, 2 )}")
# print("Média Ponderada = {}".format(round( media_ponderada, 2 )))
# Item
# Exercício feito em aula - 12
# """
# Maria quer saber quantos litros de gasolina precisa colocar em
# seu carro e quanto vai gastar para fazer
# uma viagem até a casa de sua irmã.
# Dados extras:
# - Distância da casa de Maria até sua irmã : 520 km
# - Seu carro consome 12 Km/litro de combustível.
# - Ela abastece sempre no mesmo posto, onde o preço da gasolina
# é R$ 4,50 o litro.
# Desenvolva um algoritmo onde o usuário digite a distância, o
# consumo e o valor do litro de
# combustível, com estes dados o algoritmo deverá calcular a
# quantidade de litros de combustível para a
# viagem e o custo da viagem.
#
# """
# # quantos_litros = ???
# # quanto_gastar = ???
# #
# distancia = int(input("Digite a distância a percorrer: "))
# consumo = float(input("Digite quantos km/l: "))
# preco_gasolina = 4.5
#
# qt_litros = distancia / consumo
# qt_gastar = qt_litros * preco_gasolina
#
# print(f"Maria vai gastar {round(qt_litros,2)} de combustivel gastando {round(qt_gastar,2)}")
# Item
# Dúvidas sobre FOR e WHILE
# # for
# # print("Antes do FOR")
# # #             inicio, fim, incremento
# # for x in range(4,      10,    2):
# #     print(x,"Lógica")
# # print("Depois do FOR")
#
#
# # while
#
# print("Antes do WHILE")
# x = True
# while x:
#     nome = input("Digite seu nome: ")
#     if nome == "fim":
#         break  # finaliza o laço
#     print(x, nome)
#
# print("Depois do WHILE")
#
# Item
# Exercícios Figuras 1 e 2
# # """
# # Faça um algoritmo pqra fazera figura abaixo
# # ##########
# # ##########
# # ##########
# # ##########
# # ##########
# # ##########
# # ##########
# # ##########
# # ##########
# # ##########
# # """
# #
# # print("Exemplo 1:")
# # for l in range(10):
# #     for c in range(10):
# #         print("#",end="")
# #     print()
# #
# # print("\n==================\nExemplo 2:")
# # for l in range(10):
# #     print("#"*10)
# #
#
# """
# Faça um algoritmo pqra fazera figura abaixo
# #
# ##
# ###
# ####
# #####
# ######
# #######
# ########
# #########
# """
# qt = int(input("Digite quantas linhas você quer (1-30): "))
# if qt > 0 and qt <= 30:
#     for linha in range(1, qt+1):
#         print("#"*linha)
# else:
#     print("Valor fora do intervalo desejado")
#
#
# if qt <= 0 or qt > 30:
#     print("Valor fora do intervalo desejado")
# else:
#     for linha in range(1, qt+1):
#         print("#"*linha)