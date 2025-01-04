'''3. Verificador de Palíndromo
Crie uma função que verifica se uma palavra ou frase é um palíndromo (lê-se da mesma
forma de trás para frente, desconsiderando espaços e pontuação).'''


def eh_palindromo(texto):
    texto = ''.join(char.lower() for char in texto if char.isalnum())
    return texto == texto[::-1]


frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
