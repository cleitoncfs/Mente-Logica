'''Exercícios Práticos
1. Calculadora com Funções
Crie uma calculadora simples usando funções para somar, subtrair, multiplicar e dividir dois
números.'''


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"


numero1 = float(input("Digite o prmeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = somar(numero1, numero2)
elif operacao == '-':
    resultado = subtrair(numero1, numero2)
elif operacao == '*':
    resultado = multiplicar(numero1, numero2)
elif operacao == '/':
    resultado = dividir(numero1, numero2)
else:
    resultado = "Operação inválida!"

print(resultado)


'''2. Função para Verificar Número Primo
Crie uma função que verifica se um número é primo.'''


def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


num = int(input("Digite um número inteiro: "))

if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um numero primo.")


'''3. Conversor de Temperaturas
Crie funções para converter temperaturas entre Celsius, Fahrenheit e Kelvin.'''


def celsius_para_fahrenheit(c):
    return c * 9/5 + 32


def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9


def celsius_para_kelvin(c):
    return c + 273.15


def kelvin_para_celsius(k):
    return k - 273.15


temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade atual (C, K, F): ").upper()
converter_para = input("Converter para (C, K, F): ").upper()

if unidade == "C":
    if converter_para == "F":
        resultado = celsius_para_fahrenheit(temperatura)
    elif converter_para == "K":
        resultado = celsius_para_kelvin(temperatura)

elif unidade == "F":
    if converter_para == "C":
        resultado = fahrenheit_para_celsius(temperatura)
    elif converter_para == "K":
        celsius = fahrenheit_para_celsius(temperatura)
        resultado = celsius_para_kelvin(celsius)

elif unidade == "K":
    if converter_para == "C":
        resultado = kelvin_para_celsius(temperatura)
    elif converter_para == "F":
        celsius = kelvin_para_celsius(temperatura)
        resultado = celsius_para_fahrenheit(celsius)
else:
    resultado = "Unidade inválida."

print(f"Temperatura convertida: {resultado} {converter_para}")


'''4. Função Recursiva para Fatorial
Crie uma função recursiva para calcular o fatorial de um número.'''


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


num = int(input("Digite um número inteiro positivo: "))
if num >= 0:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}.")
else:
    print("Número inválido.")
