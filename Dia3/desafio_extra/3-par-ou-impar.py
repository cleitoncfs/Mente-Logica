'''
3. Par ou Ímpar
Crie um programa que solicita um número inteiro ao usuário e verifica se ele é par ou ímpar.
'''
# Solicitar um número ao usuário:
numero = int(input("Informe um número inteiro: "))

# Verificar se o numero é par ou impar:
eh_par = (numero % 2) == 0

print("O número é par? ", eh_par)