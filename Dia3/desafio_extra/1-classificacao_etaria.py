'''
1. Classificação Etária
Crie um programa que verifica se uma pessoa pode assistir a um filme classificado como
"maiores de 16 anos".
Dados:
● Idade da pessoa: Pergunte ao usuário# Solicitar idade
'''
# Perguntar a idade do usuário
idade = int(input("Por favor, informe a sua idade: "))

# Verificar a autorização para assistir ao filme
autorizado = idade >= 16

print("Você está autorizado a assistir ao filme: ", autorizado)