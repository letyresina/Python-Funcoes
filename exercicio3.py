'''
    Exercício 3:
    Crie uma função que recebe como parâmetro um número inteiro e retorna o seu dobro.
'''

def dobro(num):
    num *= 2
    return num

num = int(input("Informe um número inteiro qualquer: "))
print(f"O dobro de {num} é {dobro(num)}")