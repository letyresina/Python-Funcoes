'''
    Exercício 6:
    Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) e o sexo 
    ('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal, sendo que:
    Peso Ideal (para homens) = (72.7 * altura) - 58
    Peso Ideal (para mulheres) = (62.1 * altura) - 44.7
'''

def pesoIdeal(altura, sexo):
    if (sexo == "f" or sexo == "F"):
        pesoIdeialF = (62.1 * altura) - 44.7
        return pesoIdeialF
    elif (sexo == "m" or sexo == "M"):
        pesoIdealM = (72.7 * altura) - 58
        return pesoIdealM


sexo = input("Informe seu sexo baseado no menu abaixo \n M para masculino \n F para feminino \n")
altura = float(input("Agora informe sua altura em metros: "))
print(f"Seu peso ideal deve ser de {round(pesoIdeal(altura, sexo), 2)}")
