'''
2. Analisador de Notas
Crie um programa que recebe as notas dos alunos em uma lista e:
● Exibe a maior e a menor nota.
● Calcula a média da turma.
● Exibe as notas acima da média.
'''
# Analisador de Notas
notas = []

while True:
    entrada = input("Digite uma nota (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    else:
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if notas:
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)
    notas_acima_media = [nota for nota in notas if nota > media]

    print("\nResultados:")
    print("Maior nota:", maior_nota)
    print("Menor nota:", menor_nota)
    print("Média da turma:", media)
    print("Notas acima da média:", notas_acima_media)
else:
    print("Nenhuma nota foi inserida.")
