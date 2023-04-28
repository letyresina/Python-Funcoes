'''
    Exercício 4:
    Faça uma função que recebe um número inteiro por parâmetro e retorna True se for par e False se
    for ímpar.
'''

def parImpar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Informe um número inteiro qualquer: "))
print(f"{parImpar(num)}")