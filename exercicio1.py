''' 
    Exercício 1:
    Escreva  um  programa  para solicitar as  notas  de  duas provas.  Faça  uma função que  receba
    as  duas notas por parâmetro e exibe a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”. 
    Considere 6.0 a média mínima para aprovação.
'''


def realizaMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6.0:
        print(f"Você foi aprovado com {media}!")
    else:
        print(f"Você foi reprovado com {media}")


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
realizaMedia(nota1, nota2)