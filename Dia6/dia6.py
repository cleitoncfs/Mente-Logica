# Lista para Tupla
lista_frutas = ["maçã", "banana", "laranja"]
tupla_frutas = tuple(lista_frutas)
print(tupla_frutas)  # Saída: ('maçã', 'banana', 'laranja')

# Tupla para Lista
tupla_cores = ("vermelho", "azul", "verde")
lista_cores = list(tupla_cores)
print(lista_cores)  # Saída: ['vermelho', 'azul', 'verde']


'''
Exercícios Práticos:

1. Lista de Convidados
Crie uma lista com nomes de convidados para uma festa. Exiba uma mensagem
personalizada para cada convidado.
'''
convidados = ["ana", "Bruno", "Carlos", "Diana"]
for convidado in convidados:
    print(f"Olá convidado {convidado}! Você está convdado para o evento...")

'''
2. Estatísticas de Números
Peça ao usuário para inserir uma lista de números (separados por espaço) e calcule:
● O maior número
● O menor número
● A soma dos números
● A média dos números
'''
entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print(f'Maior número: {maior_numero:.0f}')
print(f'Menor número: {menor_numero:.0f}')
print(f'Soma dos numeros: {soma_numeros:.0f}')
print(f'Média dos números: {media_numeros:.0f}')


'''
3. Contagem de Caracteres em uma String
Peça ao usuário para inserir uma frase e conte quantas vezes cada letra aparece.
'''
frase = input("Digite uma frase: ").lower()
letras = {}

for caractere in frase:
    if caractere.isalpha():
        if caractere in letras:
            letras[caractere] += 1
        else:
            letras[caractere] = 1
for letra, contagem in letras.items():
    print(f"A letra '{letra}' aparece {contagem} vez (es).")


'''4. Ordenando uma Lista
Peça ao usuário para inserir uma lista de números (separados por espaço) e exiba a lista
em ordem crescente e decrescente.
'''
# Ordenando uma Lista
entrada = input("Digite uma lista de números separados por espaços: ")
numeros = [float(num) for num in entrada.split()]

# Números em ordem crescente:
numeros_crescente = sorted(numeros)
numeros_crescente_int = [int(num) for num in numeros_crescente]
print(f"Números em ordem crescente: {numeros_crescente_int}")

# Números em ordem decrescente:
numeros_decrescente = sorted(numeros, reverse=True)
numeros_decrescente_int = [int(num) for num in numeros_decrescente]
print(f"Números em ordem decrescente: {numeros_decrescente_int}")


'''
5. Trabalhando com Tuplas
Crie uma tupla com nomes de meses do ano. Peça ao usuário um número entre 1 e 12 e
exiba o nome do mês correspondente.
'''
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
         "Setembro", "Outubro", "Novembro", "Dezembro")

numero_mes = int(input("Digite um número entre 1 e 12: "))
if 1 <= numero_mes <= 12:
    print(f"O mês correspondente é {meses[numero_mes - 1]}.")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 12.")
