# EXER. 1 - CONTAGEM REGRESSIVA

# contador = 10
# while contador >= 0:
#     print(contador)
#     contador = contador - 1
# print('Fogo!')

# EXER. 2 - INTERVALO DE PARES

# inicial = int(input('Qual é o número inicial da contagem?'))
# final = int(input('Qual é o número final da contagem?'))
#
# i = inicial
# while (i <= final):
#     if (i % 2 == 0):
#         print(i)
#     i = i + 1

# EXER. 3 - TABUADA

# num = int(input('Digite um número para cálcular a tabuada:'))
#
# print(f'TABUADA DO {num}:')
# i = 1
# while i <= 10:
#     print(f'{i} x {num} = {i * num}')
#     i = i + 1

# EXER. 4 - SOMA E MÉDIA DE INTEIROS
# soma = 0
# i = 1
# while i <= 5:
#     x = int(input(f'Digite o valor {i}: '))
#     soma = soma + x
#     i = i + 1
#
# print(f'Somatória: {soma}')
# media = soma / 5
# print(f'Média Final: {media}')

# EXER. 5 - MULTIPLICAÇÃO DE VALORES

# x = int(input(f'Digite um valor: '))
# y = int(input(f'Digite um segundo valor: '))
#
# multi = 0
# i = 1
# while i <= x:
#     multi = multi + y
#     i = i + 1
# print(f'Resultado da multiplicação: {x} x {y} = {multi}')

# EXER. 6 - QUANTIDADES E MEDIA

#variável

qtd_positivo = 0
soma_positivo = 0
qtd_par = 0
soma_par = 0
qtd_impar = 0
soma_impar = 0

inicial = int(input('Qual é o número inicial da contagem?'))
final = int(input('Qual é o número final da contagem?'))

i = inicial
if (inicial < final):
    while i <= final:
        if i > 0:
            qtd_positivo = qtd_positivo + 1
            soma_positivo = soma_positivo + i
        if i % 2 == 0:
            qtd_par = qtd_par + 1
            soma_par = soma_par + i
        else:
            qtd_impar = qtd_impar + 1
            soma_impar = soma_impar + i
        i = i + 1

    media_positivo = soma_positivo / qtd_positivo
    media_par      = soma_par      / qtd_par
    media_impar    = soma_impar    / qtd_impar
    print(f'Quantidade de valores positivos: {qtd_positivo}')
    print(f'Quantidade de valores pares: {qtd_par}')
    print(f'Quantidade de valores impares: {qtd_impar}')
    print(f'Média dos valores positivos: {media_positivo}')
    print(f'Média dos valores pares: {media_par}')
    print(f'Média dos valores impares: {media_impar}')
else:
    print('Você digitou um valor inicial menor do que o valor final.')
