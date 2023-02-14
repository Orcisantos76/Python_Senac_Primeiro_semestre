x = float("2.3")
r = x * 2/3
if r > 5:
    print = (round(r) , 2)
else:
    print("valor não é maior que 5. ")
nome= input("Digite seu nome: ").strip()
email = input("Digite seu email: ").strip()

if nome and email:
    pos_a = email.find("@")
    if pos_a != -1: # se o caracter não for encontrado ele aparece como -1
        print("Cadastro concluido")
    print(nome)
else:
    print("Digite seu nome e email corretamente.")
