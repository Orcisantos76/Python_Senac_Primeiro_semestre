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
# ler até 5 frases

cont = 0
while cont < 5:
    frase = input("[fim]Encerra. Digite uma frase: ")
    print(frase.lower())
    if frase == "fim":
        break
    cont = cont + 1
    print (f"A frase tem {len(frase)} caracteres")
    print (f" temos {frase.count('a')} a,temos {frase.count('e')} e,temos {frase.count('i')} i,temos {frase.count('o')} o,temos {frase.count('u')} u")
    a = frase.count("a")
    e = frase.count("e")
    i = frase.count("i")
    o = frase.count("o")
    u = frase.count("u")
    soma = a + e + i + o + u
    print (f"A soma das vogais é {soma}")


print ("sai do while")
# # mostrar quantos caracteres tem a frase
print(len(frase))
#     qt_caracter = 0
#     for caracter in frase:
#         qt_caracter = qt_caracter + 1
#     print(qt_caracter)
qt_vogais = 0
for caracter in frase:
    if caracter == "a": qt_vogais = qt_vogais + 1
    print (f"A quantidade de vogais 'a' é {qt_vogais}")
    if caracter == "e": qt_vogais = qt_vogais + 1
    print (f"A quantidade de vogais 'e' é {qt_vogais}")
    if caracter == "i": qt_vogais = qt_vogais + 1
    print (f"A quantidade de vogais 'i' é {qt_vogais}")
    if caracter == "o": qt_vogais = qt_vogais + 1
    print (f"A quantidade de vogais 'o' é {qt_vogais}")
    if caracter == "u": qt_vogais = qt_vogais + 1
    print (f"A quantidade de vogais 'u' é {qt_vogais}")
        

# mostrar quantas vogais


# mostrar o percentua de A,s