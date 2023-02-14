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
for x in range (2):
    frase= str(input("Digite uma frase:"))
    if len(frase)<5 and len(frase)<200:
        print("A frase tem que ter mais de 5 caracteres e menos de 200.")
        break
    print(len(frase))
    a = (frase.count("a"))
    print(f"temos {a} letras a")
    e = (frase.count("e"))
    print(f"temos {e} letras e")
    i = (frase.count("i"))
    print(f"temos {i} letras i")
    o = (frase.count("o"))
    print(f"temos {o} letras o")
    u = (frase.count("u"))
    print(f"temos {u} letras u")
    print("um total de ",(a+e+i+o+u)," vogais")
    print(f"O percentual de letras (a) desta frase é {a/len(frase)*100:.2f}%")


