'''
2. Série Fibonacci
Exiba os primeiros N termos da série de Fibonacci.
● A série de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos
dois anteriores.
● Exemplo: 0, 1, 1, 2, 3, 5, 8, 13...
'''
N = int(input("Quantos termos da série Fibonacci você quer ver? "))

termo1 = 0
termo2 = 1
contador = 0

if N <= 0:
    print("Por favor, insira um número positivo.")
elif N == 1:
    print("Série Fibonacci até", N, "termo:")
    print(termo1)
else:
    print("Série Fibonacci:")
while contador < N:
    print(termo1)
    proximo_termo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo_termo
    contador += 1