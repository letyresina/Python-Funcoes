'''
    Exercício 5:
    Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada 
    área que  calcula  e  retorna  a  área  do  círculo  e  outra  função  chamada perimetro que
    calcula  e  retorna  o perímetro do círculo. Utilize as fórmulas abaixo 
    Área = π * r ** 2
    Perímetro = π * 2 * r
'''
import math
pi = math.pi

def area(raio):
    areaCirculo = pi * raio ** 2
    return areaCirculo

def perimetro(raio):
    perimetroCirculo = pi * 2 * raio
    return perimetroCirculo

raio = float(input("Informe o valor do raio: "))
print(f"A área do círculo é {round(area(raio), 2)} e o perímetro é {round(perimetro(raio), 2)}")