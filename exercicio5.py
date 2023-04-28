'''
    Exercício 5:
    Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada 
    área que  calcula  e  retorna  a  área  do  círculo  e  outra  função  chamada perimetro que
    calcula  e  retorna  o perímetro do círculo. Utilize as fórmulas abaixo 
    Área = π * r ** 2
    Perímetro = π * 2 * r
'''

pi = 3.14

def area (raio):
    areaCirculo = pi * raio ** 2
    return areaCirculo

def perimetro(raio):
    perimetroCirculo = pi * 2 * raio
    return perimetro