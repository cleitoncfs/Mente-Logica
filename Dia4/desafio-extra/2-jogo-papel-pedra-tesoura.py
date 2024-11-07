'''
2. Jogo Pedra, Papel ou Tesoura:
Crie um programa que simula o jogo "Pedra, Papel ou Tesoura" entre o usuário e o
computador.
'''
import random

opcoes = ["pedra", "papel", "tesoura"]
usuario = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print(f"Você escolheu: {usuario}")
print(f"O computador escolheu: {computador}")

if usuario == computador:
    print("Empate!")
elif (usuario == "pedra" and computador == "tesoura") or \
     (usuario == "papel" and computador == "pedra") or \
     (usuario == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")
