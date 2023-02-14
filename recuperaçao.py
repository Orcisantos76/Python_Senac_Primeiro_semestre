"""
O cardápio de uma lancheria é o seguinte:
---------------------------------
 Especificação      Código Preço
---------------------------------
 Cachorro quente....100....15,20
 Bauru simples......101....18,30
 Bauru com ovo......102....22,50
 Hambúrger..........103....17,20
 Cheeseburguer......104....23,30
 Refrigerante.......105....5,00


Escrever um algoritmo que leia o código do item pedido,
a quantidade e calcule o valor a ser pago por aquele lanche.
Considere que o cliente pode pedir mais de um item.
Ao digitar 0 (zero) finalize o pedido mostrando o
    Total a ser pago.

Utilize as seguintes listas:
lst_produtos = ['100','101','102','103','104','105']
lst_precos = [15.20, 18.30, 22.50, 17.20, 23.30, 5.00]
"""

cardapio = """
---------------------------------
 Especificação      Código Preço
---------------------------------
 Cachorro quente....100....15,20
 Bauru simples......101....18,30
 Bauru com ovo......102....22,50
 Hambúrger..........103....17,20
 Cheeseburguer......104....23,30
 Refrigerante.......105....5,00"""


lst_produtos = ['100','101','102','103','104','105']
lst_precos = [15.20, 18.30, 22.50, 17.20, 23.30, 5.00]
pedido = []

total_pedido = 0
quantidade = 0
while True:
    print(cardapio)
    print("\n>>>Digite 0 para finalizar o pedido<<<")
    escolha = int(input(">>Digite o código do produto: "))
    unidades = int(input(f'quantas unidades de {escolha} vai querer? '))
    for p, i in enumerate(lst_produtos):
        if escolha == i:
            pass
    print(lst_precos[p])
    print(p, i, escolha)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in "Nn":
        break
