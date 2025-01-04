'''Desafios Extras
1. Gerador de Senhas Aleatórias
Crie uma função que gera uma senha aleatória com tamanho especificado, contendo letras
maiúsculas, minúsculas, números e símbolos.'''

import random
import string


def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada:", senha_gerada)
