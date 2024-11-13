'''
Projeto: Jogo de Adivinhação com Pontuação
Descrição do Projeto
Vamos criar um jogo interativo de adivinhação em que:

● O computador escolhe um número aleatório entre 1 e 100.
● O jogador tem um número limitado de tentativas para adivinhar o número.
● A cada palpite, o programa fornece dicas, informando se o número é maior ou
menor.
● O jogador acumula pontos com base no número de tentativas.
● O jogo armazena as pontuações em uma lista e exibe o placar ao final.
'''
import random

# Lista para armazenar pontuações
pontuacoes = []

print("Bem-vindo ao Jogo da Adivinhação!")

# Escolha do nível de dificuldade
print("Escolha o nível de dificuldade:")
print("1. Fácil (10 tentativas)")
print("2. Médio (7 tentativas)")
print("3. Difícil (5 tentativas)")

while True:
    dificuldade = input("Digite o número da dificuldade desejada: ")
    if dificuldade == "1":
        tentativas_totais = 10
        break
    elif dificuldade == "2":
        tentativas_totais = 7
        break
    elif dificuldade == "3":
        tentativas_totais = 5
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

while True:
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = tentativas_totais
    tentativas = 0
    palpites_feitos = []

    print("\nEu pensei em um número entre 1 e 100")
    print(f"Você tem {tentativas_totais} tentativas para adivinhar")

    # Loop de tentativas
    while tentativas_restantes > 0:
        palpite = input("\nDigite o seu palpite: ")

        # Verificando se o input é um número válido
        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        palpite = int(palpite)

        # Verificando se o palpite está dentro do intervalo permitido
        if palpite < 1 or palpite > 100:
            print("Entrada inválida! Por favor, digite um número inteiro entre 1 e 100.")
            continue

        # Verificando se o palpite já foi feito
        if palpite in palpites_feitos:
            print("Você já tentou esse número. Tente outro.")
            continue
        else:
            palpites_feitos.append(palpite)

        tentativas += 1
        tentativas_restantes -= 1

        if palpite == numero_secreto:
            print(
                f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            pontuacao = tentativas_restantes * 10 * int(dificuldade)
            pontuacoes.append(pontuacao)
            print(f"Sua pontuação nesta partida: {pontuacao} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior que esse.")
        else:
            print("O número secreto é menor que esse.")

        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Palpites já feitos: {palpites_feitos}")

    else:
        print(
            f"Que pena, você não conseguiu adivinhar. O número era {numero_secreto}.")
        pontuacoes.append(0)

    # Exibindo o placar
    print("\nPlacar:")
    for idx, pontos in enumerate(pontuacoes, start=1):
        print(f"Partida {idx}: {pontos} pontos")

    # Perguntar se o jogador deseja jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar. Até a próxima!")
        break


'''
Explicação do Código:

Importação do Random: Para gerar o numero_secreto.
Variáveis de Controle:
tentativas_restantes: Começa com um valor baseado no nível de dificuldade escolhido e diminui a cada palpite.
tentativas: Conta o número de palpites feitos.
Loop Principal: Mantém o jogo em execução até o jogador decidir sair.
Loop de Tentativas: O jogador faz palpites até acertar ou acabar as tentativas.
Feedback ao Jogador:
Se o palpite está correto.
Se o número secreto é maior ou menor.
Quantas tentativas restam.
Palpites já feitos.
Pontuação:
O jogador ganha pontos com base nas tentativas restantes e no nível de dificuldade.
Pontuação é calculada como tentativas_restantes * 10 * int(dificuldade).
Armazenamos as pontuações na lista pontuacoes.
Placar: Após cada partida, exibimos o histórico de pontuações.
Opção de Jogar Novamente: Permite que o jogador decida continuar ou sair.
Nível de Dificuldade: O jogador pode escolher entre fácil, médio e difícil, o que altera o número de tentativas disponíveis.


Este projeto demonstra como os conceitos individuais se combinam para criar um programa
completo e funcional. A prática de desenvolver projetos é essencial para solidificar seu
entendimento e habilidades em programação.
'''
