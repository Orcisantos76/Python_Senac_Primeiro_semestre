"""
Fazer um algoritmo para ler duas notas, os pesos de cada nota e
mostrar a média ponderada.
                                (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
Cálculo da Média Ponderada = ------------------------------------------------------------------------
                                        soma dos pesos
"""
n1 = float(input("Digite a primeira nota: "))
pn1 = float(input("Digite o peso da primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
pn2 = float(input("Digite o peso da segunda nota: "))
media= (pn1*n1)+(pn2*n2)/pn1+pn2
print(media)

