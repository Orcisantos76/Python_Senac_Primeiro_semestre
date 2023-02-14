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
while True:
    try:
        escolha = int(input("faça a sua MENU\n 1- Cadastrar Login e Senha\n 2- Aumento de 10%\n 3- Relatório\n 4- Cadastrar Funcionário\n Escolha: "))
    except:

if escolha == 1:



login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]
