"""
Maria quer saber quantos litros de gasolina precisa colocar em
seu carro e quanto vai gastar para fazer
uma viagem até a casa de sua irmã.
Dados extras:
- Distância da casa de Maria até sua irmã : 520 km
- Seu carro consome 12 Km/litro de combustível.
- Ela abastece sempre no mesmo posto, onde o preço da gasolina
é R$ 4,50 o litro.
Desenvolva um algoritmo onde o usuário digite a distância, o
consumo e o valor do litro de
combustível, com estes dados o algoritmo deverá calcular a
quantidade de litros de combustível para a
viagem e o custo da viagem.

"""
dist= float(input("Digite a distancia a percorrer: "))
cons = float(input("Digite quantos km o carro percorre com um litro de combustivel: "))
comb = float(input("Digite o valor do combustivel: "))
totcomb = dist/cons
valorgasto = totcomb*comb
print(f"Maria vai gastar {totcomb:.2f}litros, com o valor de "
      f"R${comb:.2f} o litro, ela gastará um total de R${valorgasto:.2f}")