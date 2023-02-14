"""
Faça um algoritmo que leia um valor para saque em Reais,
e diga quantas notas de cada são necessárias para
para formar o valor lido.
Considerar notas de 200, 100, 50, 20, 10, 5 e 2 Reais.

Exemplo:
Digite o valor em Reais: 380
Para esse valor precisamos de:
1 nota de 200
1 nota de 100
1 nota de 50
1 nota de 20
1 nota de 10
"""

valor = int(input('Digite um valor:'))
if valor % 2 == 0:
    print("Não é possivel sacar ")

qt200 = valor//200
valor = valor%200
qt100 = valor//100
valor = valor%100
qt50 = valor//50
valor = valor%50
qt20 = valor//20
valor = valor%20
qt10 = valor//10
valor = valor%10
qt5 = valor//5
valor = valor%5
qt2 = valor//2
valor = valor%2
print (f'teremos {qt200} notas de R$ 200,00')
print (f'teremos {qt100} notas de R$ 100,00')
print (f'teremos {qt50} notas de R$ 50,00')
print (f'teremos {qt20} notas de R$ 20,00')
print (f'teremos {qt10} notas de R$ 10,00')
print (f'teremos {qt5} notas de R$ 5,00')
print (f'teremos {qt2} notas de R$ 2,00')



valor1 = int(input("Qual valor para saque: "))
if valor1 % 2 == 1:
    print("Não é possivel sacar ")
    

print = ("É necessario: ")
qt_notas = valor//200
if qt_notas > 0:
    print("->",qt_notas, "de R$ 200,00")
valor = valor % 200