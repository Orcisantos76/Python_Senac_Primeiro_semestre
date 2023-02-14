'''
---------------------------------
 Especificação      Código Preço
---------------------------------
Cachorro quente....100....15,20
Bauru simples......101....18,30
Bauru com ovo......102....22,50
Hambúrger..........103....17,20
Cheeseburguer......104....23,30
Refrigerante.......105....5,00'''

lst_produtos = ['100','101','102','103','104','105']
lst_precos = [15.20, 18.30, 22.50, 17.20, 23.30, 5.00]
total = 0
pedidos = []
while True:
    print('''---------------------------------
    Especificação      Código Preço
    ---------------------------------
    Cachorro quente....100....15,20
    Bauru simples......101....18,30
    Bauru com ovo......102....22,50
    Hambúrger..........103....17,20
    Cheeseburguer......104....23,30
    Refrigerante.......105....5,00
    Digitar zero encerra o pedido...''')
    pedido = int(input('Qual o seu pedido '))
    if pedido == 100:
        item0 = "Cachorro quente"
        qt = int(input(f'quantas unidades de {item0} você quer? '))
        if qt > 0:
            pedidos.append(item0)
            pedidos.append(qt)
        total += (qt*lst_precos[0])
    if pedido == 101:
        item1 = "Bauru Simples"
        qt = int(input(f'Quantas unidades de {item1} você quer? '))
        if qt > 0:
            pedidos.append(item1)
            pedidos.append(qt)
        total += (qt*lst_precos[1])
    if pedido == 102:
        item2 = "Bauru com ovo"
        qt = int(input(f"Quantas unidades de {item2} você quer? "))
        if qt > 0:
            pedidos.append(item2)
            pedidos.append(qt)
        total += (qt*lst_precos[2])
    if pedido == 103:
        item3 = "Hambúrger"
        qt = int(input(f"Quantas unidades de {item3} você quer?"))
        if qt > 0:
            pedidos.append(item3)
            pedidos.append(qt)
        total += (qt*lst_precos[3])
    if pedido == 104:
        item4 = "Cheeseburguer"
        qt = int(input(f"Quantas unidade de {item4} você quer? "))
        if qt > 0:
            pedidos.append(item4)
            pedidos.append(qt)
        total += (qt*lst_precos[4])
    if pedido == 105:
        item5 = "Refrigerante"
        qt = int(input(f"Quantas unidades de {item5} você quer? "))
        if qt > 0:
            pedidos.append(item5)
            pedidos.append(qt)
        total += (qt*lst_precos[5])

    if pedido == 0:
        break
print(f"Voce pediu {pedidos}, valor do seu pedido é R${total:.2f}")
print(pedidos)


