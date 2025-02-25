# ? Exercício 5 2
# * Desenvolva um algoritmo que seja capaz de cálcular a soma e a subtração entre 2 valores com vírgula.
# * Crie duas variáveis de teste. Uma que testa se a soma é maior do que 10.
# * Outra que teste se a subtração é menor do que 0. Imprima tudo na tela.

# x = float(input('Digite um número:'))
# y = float(input('Digite um segundo número:'))
#
# soma = x + y
# sub = x - y
# print(f'Soma: {soma:.2f}. Subtração: {sub:.1f}.')
#
# if (soma > 10):
#     print(f'A soma é maior do que 10.')
#
# if (sub < 0):
#     print(f'A subtração é menor do que 0.')

# ? Exercício 1
# * Desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Cálcule a sua idade e apresente na tela.
# * Para fins de simplificação, despreze o dia e o mês do ano.
# * Após o cálculo, verifique se a idade é maior ou igual a 18 e apresente na tela uma mensagem.
# * Informando que já é possível tirar a carteira de motorista.

# nasc = int(input('Digite seu ano de nascimento?'))
# ano = int(input('Em qual ano estamos?'))
#
# idade = ano - nasc
#
# print(f'Sua idade é: {idade:.2f}.')
#
# if (idade >= 18):
#     print(f'Você é de maior. Parabéns, você já pode tirar sua carteira de motorista.')

# ? Exercício 2
# * Uma empresa concedeu um bônus de 20% para todos os funcionários com mais de 5 anos de empresa.
# * Todos que não se enquadram nesta categoria, receberam um bônus de 10%, somente.
# * Escreve um algoritmo que leia o salário do funcionário e seu tempo de empresa.
# * e apresente a bonificação de cada funcionário na tela.

# salario = float(input('Qual seu salário?'))
# ano_admissao = int(input('Qual seu ano de admissão?'))
# ano_atual = int(input('Qual o ano atual?'))
#
# tempo = ano_atual - ano_admissao
# if (tempo > 5):
#    bonus = salario * 0.2
# else:
#     bonus = salario * 0.1
#
# print(f'Você tem {tempo} anos dentro da empresa.')
# print(f'Seu salário é de {salario}.')
# print(f'Sua bonificação será de {bonus}.')
# print(f'Salário final:{salario + bonus}.')

# ? Exercício 4
# * Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que ele está cursando.
# * Assuma que a média de aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
# * Escreva um algoritmo que Leia a nota final do aluno em cada matéria e informe na tela se ele passou de ano.

# m1 = float(input('Digite a nota da matéria 1: '))
# m2 = float(input('Digite a nota da matéria 2: '))
# m3 = float(input('Digite a nota da matéria 3: '))
#
# if (m1 >= 7) and (m2 >= 7) and (m3 >= 7):
#     print('Aluno aprovado!')
# else:
#     print('Aluno reprovado!')

# ? Exercício 5
# * Escreva um algoritmo que lê um número inteiro.
# * Após verifique se este valor está contido dentro dos seguintes intervalos: -100 < x < -1 ou 1 < x < 100.
# * Imprima na tela.

# x = int(input('Digite um valor inteiro: '))
# if (x > 1) and (x < 100) or (x < -1) and (x > -100):
#     print('Atende o critério de intervalo!')

# ? Exercício 6
# * Uma empresa concedeu um bônus de 20% para todos os funcionários com mais de 5 anos de empresa.
# * Concedeu também um bônus de 30% para todos os funcionários com mais de 10 anos de empresa.
# * Todos que não se enquadram nesta categoria, receberam um bônus de 10%, somente.
# * Escreve um algoritmo que leia o salário do funcionário e seu tempo de empresa.
# * e apresente a bonificação de cada funcionário na tela.

salario = float(input('Qual seu salário?'))
ano_admissao = int(input('Qual seu ano de admissão?'))
ano_atual = int(input('Qual o ano atual?'))

tempo = ano_atual - ano_admissao
if tempo > 10:
    bonus = salario * 0.3
else:
    if tempo > 5:
        bonus = salario * 0.2
    else:
        bonus = salario * 0.1

print(f'Você tem {tempo} anos dentro da empresa.')
print(f'Seu salário é de {salario}.')
print(f'Sua bonificação será de {bonus}.')
print(f'Salário final:{salario + bonus}.')