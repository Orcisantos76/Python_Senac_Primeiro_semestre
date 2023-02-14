'''
Competências:
- Atividade é individual. :)
- Saber interpretar o que foi solicitado;
- Desenvolver uma solução viável para o problema proposto;
- Utilizar os comandos de forma adequada para a solução;

Tarefa:
-------
Perguntar a 4 alunos a resposta de 10 questoes de uma prova de múltipla escolha.
Comparar essas respostas com o gabarito da prova.
Calcular o total de acertos de cada aluno.

No final informar:
Aluno(s) com Maior acerto(s)
Aluno(s) com Menor acerto(s)
A média das notas da turma


lista_gabarito = ["A","B","C","D","E","E","D","C","B","A"]
Aceitar como respostas apenas A,B,C,D,E.

'''

lista_gabarito = ["", "A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
lista_acertos = ["", 0, 0, 0, 0]

for aluno in range(1, 5):
    print(f"Aluno {aluno}:")

    for pergunta in range(1, 11):
        print(f"  Questão {pergunta}: ")
        while True:
            resposta = input("...Resposta: A,B,C,D,E? ")
            if resposta.upper() in ['A', 'B', 'C', 'D', 'E']:
                break
        if resposta == lista_gabarito[pergunta]:
            lista_acertos[aluno] += 1

for aluno in range(1,5):
    print(f"Total de acertos do aluno{aluno}: {lista_acertos[aluno]}")

print(f"Aluno(s) com mais acertos: ", end="")
for posicao, acerto in enumerate(lista_acertos):
    if acerto == max(lista_acertos[1:]):
        print(f"{posicao} ", end="")

print(f"\nAluno(s) com menos acertos: ", end="")
for posicao, acerto in enumerate(lista_acertos):
    if acerto == min(lista_acertos[1:]):
        print(f"{posicao} ", end="")

media = sum(lista_acertos[1:]) / 4

print(f"\nMédia de notas da turma: {media}")

