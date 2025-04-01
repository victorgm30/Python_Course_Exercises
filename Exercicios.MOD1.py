#
# ? Exercício 1
# * Desenvolva um algoritmo que solicite ao usuário dois números inteiros.
# * Imprima a soma destes dois números na tela

#x = int(input('Digite um número inteiro:'))
#y = int(input('Digite um segundo número inteiro:'))

#res = f'O resultado da soma de {x} com {y} será {x + y}.'
#print(res)

# ? Exercício 2
# * Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos.
# * Cálcule o total de segundos resultante e imprima na tela para o usuário.

# #d = int(input('Quantos dias?'))
# h = int(input('Quantas horas?'))
# m = int(input('Quantos minutos?'))
# s = int(input('Quantos segundos?'))
#
# total = s + (m * 60) + (h * 3600) + (d * 24 * 60 * 60)
#
# print(f'O total de segundos calculado é de {total}.')

# ? Exercício 3
# * Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# * Cálcule e exiba o valor do desconto e o preço final do produto.

# preco = float(input('Digite o preço do produto:'))
# p = float(input('Digite o percentual de desconto (0-100%):'))
#
# desconto = preco * (p/100)
# final = preco - desconto
#
# print(f'O preço do produto é R$ {preco}. Desconto aplicado de {p}%')
# print(f'Valor do desconto calculado: R$ {desconto}.')
# print(f'Valor final do produto: R$ {final}.')

# ? Exercício 4
# * Desenvolva um algoritmo que converta uma temperatura em C para F.
# * A equação de conversão é: 9 x c, tudo dividido por 5, somando 32.

# c = float(input('Digite um temperatura em Celsius (C):'))
# f = (9 * c) / 5 + 32
#
# print(f'Celsius: {c}. Fahrenheit: {f}')

# ? Exercício 5
# * Desenvolva um algoritmo que seja capaz de cálcular a soma e a subtração entre 2 valores com vírgula.
# * Crie duas variáveis de teste. Uma que testa se a soma é maior do que 10.
# * Outra que teste se a subtração é menor do que 0. Imprima tudo na tela.

x = float(input('Digite um número:'))
y = float(input('Digite um segundo número:'))

soma = x + y
sub = x - y
testeA = soma > 10
testeB = sub < 0


print(f'Soma: {soma:.2f}. Subtração: {sub:.1f}.')
print(f'A soma é maior do que 10? {testeA}. ')
print(f'A subtração é menor do que 0? {testeB}. ')








