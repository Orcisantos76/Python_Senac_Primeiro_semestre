"""
Faça uma função que receba uma string como parâmetro e
retorne a quantidade de palavras existente nesta string.
"""


x = input("Digite um testo qualquer: ")
def qt_palavras(frase):
    return len(frase.split())# return len vai contar quantos elementos tem dentro do split, que é uma lista
                                # das palavras na lista.
    pass# nao faz nada
print(qt_palavras(x)) #quero saber a quantidade de palavras de x.

#Faça um programa que receba a temperatura média de cada mês do
# ano e armazene-as em uma lista. Após isto, calcule a média anual
# das temperaturas e mostre todas as temperaturas acima da média
# anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = ["janeiro", "fevereiro", "março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

temperaturas = []
def temperatura_informada():
    for mes in range(12):
        temperaturas.append(float(input(f"Digite a temperatura do mes {meses[mes]} ")))
def media_anual():
    return sum(temperaturas)/len(meses)

def acima_media(media_anual):
    for ind, temperatura in enumerate(temperaturas): # mes é o contador , temperatura será a posição daquele contador, enumerate da a posição de cada temperatura
        if temperatura > media_anual:
            print(f" {temperatura} {meses[ind]}")

temperatura_informada()
media_anual_calculada = media_anual()
print(sum(temperaturas)/len(meses))
acima_media(media_anual_calculada)



