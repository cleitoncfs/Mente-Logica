'''
Desafios Extras:

1. Calculando Fatorial de um Número
Peça ao usuário um número inteiro positivo e calcule o fatorial desse número.
● Fatorial de N (N!) é o produto de todos os números inteiros positivos de 1 até N.
● Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
N = int(input("Digite um numero inteiro positivo: "))

fatorial = 1

if N < 0:
    print("Não existe fatorial de número negativo.")
elif N == 0 or N == 1:
    print(f"O fatorial de {N} é 1.")
else:
    for i in range(1, N+1):
        fatorial *= i
        
print(f"O fatorial de {N} é {fatorial}.")
