# Funções:
''' Para definir uma função em Python, usamos a palavra-chave def, seguida do nome da
função e parênteses (). O código da função é indentado.

● def: Indica que estamos definindo uma função.
● nome_da_funcao: Nome que escolhemos para a função.
● ():: Parênteses que podem conter parâmetros (explicaremos em breve).
● pass: Palavra-chave usada como placeholder quando não há código dentro da
função.

Exemplo Simples
Vamos criar uma função que imprime uma mensagem de saudação'''


def saudacao():
    print("Olá! Seja bem vindo-a.")


# Para chamar (executar) a função, simplesmente usamos seu nome seguido de parênteses:
saudacao()


'''Parâmetros são variáveis que permitem que você passe informações para dentro de uma
função. Eles são definidos entre os parênteses na declaração da função.'''


def saudacao(nome):
    print(f"Olá!{nome} seja bem vindo-a.")


# Para chamar (executar) a função, simplesmente usamos seu nome seguido de parênteses:
saudacao("Cleiton")


# Podemos definir funções com vários parâmetros.
def apresentar_pessoa(nome, idade):
    print(f"Este é {nome} e sua idade é {idade} anos.")


apresentar_pessoa("Cleiton", 41)


# Exemplo de Função com Retorno
def soma(a, b):
    resultado = a + b
    return resultado


total = soma(5, 3)
print("O total é: ", total)


# Se uma função não possui a instrução return, ela retorna None por padrão.
def multiplicar(a, b):
    produto = a * b
    # não há return


resultado = multiplicar(4, 5)
print("Resultado é igual a: ", resultado)

# Para corrigir adicionamos o return


def multiplicar(a, b):
    produto = a * b
    return produto


resultado = multiplicar(4, 5)
print("Resultado é igual a: ", resultado)
