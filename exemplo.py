# Função que verifica se um número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é Ímpar')


# Função que calcula a área de um triângulo (exibe o resultado)
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f'Área do triângulo: {area}')


# Função que calcula a área de um retângulo (retorna o resultado)
def calcular_area_retangulo(base, altura):
    area = base * altura
    return area # Para a execução (se não printar, não vai mostrar o resultado)

while True:     # loop infinito
    print('1 - Verificar se um numero é Par ou Impar')
    print('2 - Calcular a area de um triangulo')
    print('3 - Calcular a area de um retângulo')
    print('4 - Finalizar')
    opcao = int(input('Escolha um opção: '))

    if opcao == 1:
        n = int(input('Informe um numero: '))
        par_ou_impar(n)     # chama função
    elif opcao == 2:
        base = float(input('Informe a base: '))
        altura = float(input('Informe a altura: '))
        calcular_area_triangulo(base, altura)   # chama função
    elif opcao == 3:
        base = float(input('Informe a base: '))
        altura = float(input('Informe a altura: '))
        area = calcular_area_retangulo(base, altura)    # chama função
        print(f'Área do retângulo: {area}')
    elif opcao == 4:
        print('Final da Execução')
        break       # finaliza as repetições do while
    else:
        print('Opção inválida')