va = int(input("Digite um número "))
vb = int(input("Digite um segundo númreo "))

print(f"Os números foram digitados na seguinte ordem {va} e depois {vb}")

n = vb
vb = va
vb = n
soma = vb + va
print(f"A ordem inversa é {vb} vb e {va} va")

print(f"A soma dos valores digitado é {soma}")
print(f"A media é de {soma/2}")
numeros = [4,2,6,1,3]
numeros_ordenados = sorted(numeros)

print (numeros )
print (numeros_ordenados)
lista = []
soma = 0
for x in range(3):
    num = int(input("Digite um número"))
    x = x+1
    lista.append(num)
    soma = soma + num
print(f"Foram digitados {x} numeros, sua soma foi de {soma} e a media foi de {soma/x:.2f}")
print(f"Colocando em ordem crescente os numeros digitados {sorted(lista)} ")