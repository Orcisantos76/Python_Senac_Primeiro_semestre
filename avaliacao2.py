# Avaliação 02 individual
# Autor: Seu Nome Aqui

# Quando finalizar a tarefa, salve o arquivo com o seu
# nome_completo

# Esta avaliação deverá ser individual.
# Competências observadas:
#   - Saber interpretar o que foi solicitado;
#   - Conhecer os comando básicos da linguagem python;
#   - Saber utilizar a estrutura de lista da linguagem;
#   - Desenvolver uma solução viável para o problema
#     proposto.
#   PROVAS IGUAS. 'D'



'''
Faça um algoritmo que implemente o menu abaixo.

MENU
1- Cadastrar Login e Senha
2- Aumento de 10%
3- Relatório
4- Cadastrar Funcionário
Escolha:

Para implementar seu código você deverá utilizar
as seguintes listas:
login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]


Descrição:
Na opção 1 - Você deverá ler o nome do funcionário e verificar
            se este na lista de funcionarios.
            Se existir, cadastrar login e senha nas listas
               correspondentes.
            Critério: login não poderá se repetir.

Para executar as opções 2 e 3, você deverá validar o
   login e senha cadastrados.

Na opção 2 - Após validar login e senha, seu código deverá
                 aumentar o salário dos funcionários em 10%. Mas somente
             Se o funcionário ganhar abaixo da média em
                 relação a lista de salarios.

Na opção 3 - Após confirmar login e senha, você deverá fazer
                 um relatório mostrando o nome e o salario,
                 conforme exemplo:

                 Maria Clara  - 7450.23
                 João Antonio - 5677.33
                 Carlos       - 3970.34
                 Pedro        - 3470.00
                 Ana          - 2200.00

Na opção 4 - Você deverá cadastrar o nome e o salário de um
             novo funcionário.
             (Não precisa validar login e senha)

'''

login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]


while True:
    try:
        menu = int(input("MENU:\n1- Cadastrar Login e Senha\n2- Aumento de 10%\n3- Relatório\n4- Cadastrar Funcionário\nEscolha: "))
    except:
        print("Você deve escolher uma das opções do menu.")
        continue
    if menu > 4 or menu < 1:
        print("Você deve escolher uma das opções do menu.")
        pass
    elif menu == 1:
        usuario = input("Digite seu nome de usuario: ").capitalize()
        if usuario in funcionarios:
            print("Seu login será seu nome")
            if usuario in login:
                print("Login ja cadastrado")
                pass
            else:
                login.append(usuario)
                senha_usuario = int(input("Digite uma senha: "))
                senha.append(senha_usuario)
        else:
            print("Seu nome não consta na lista de funcionarios")
            continue
    elif menu == 2:
        print("Vamos validar seu usuario:")
        x = input("Digite seu nome de usuario: ").capitalize()
        if x in login:
            cod = int(input("Digite sua senha: "))
            if cod != senha[login.index(x)]:
                print("Senha invalida")
                pass
            else:
                aumento = input("Isso aumentará o salário de quem estiver abaixo da media em 10%: S/N ")
                if aumento in "Ss":
                    #print(aumento)
                    media = (sum(salarios)) / len(salarios)
                    for i in range(len(salarios)):
                        if salarios[i] < media:
                            #print(f"{salarios[i]}")
                            if salarios[i] < media:
                                salarios[i] = salarios[i] * 1.1
                else:
                    print("Ninguem recebeu aumento, os salarios continuam iguais")

        else:
            print("Seu nome não consta na lista de funcionarios autorizados")
            continue
    elif menu == 3:
        print("Vamos validar seu usuario:")
        x = input("Digite seu nome de usuario: ").capitalize()
        if x in login:
            cod = int(input("Digite sua senha: "))
            if cod != senha[login.index(x)]:
                print("Senha invalida")
                pass
            else:
                print("-="*30)
                print("Aqui temos o nosso relatório: ")
                for r in range(len(funcionarios)):

                    print(f"{funcionarios[r]:.<18}", end="")
                    print(f"R$ {salarios[r]:.2f}")
                print("-=" * 30)
        else:
            print("Seu nome não consta na lista de funcionarios autorizados")
            print("-=" * 30)
            continue
    elif menu == 4:
        print("Vamos validar seu usuario:")
        x = input("Digite seu nome de usuario: ").capitalize()
        if x in login:
            cod = int(input("Digite sua senha: "))
            if cod != senha[login.index(x)]:
                print("Senha invalida")
                pass
            else:
                print("Vamos cadastrar novo funcionário:")
                func = input("Digite o nome do funcionário: ").capitalize()
                funcionarios.append(func)
                sal = float(input("Digite o salario do novo funcionario, Rs: "))
                salarios.append(sal)
                print("-="*30)
        else:
            print("Seu nome não consta na lista de funcionarios autorizados")
            continue

