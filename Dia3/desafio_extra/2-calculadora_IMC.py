'''
2. Calculadora de IMC
O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg) pela altura (em
metros) elevada ao quadrado.
Crie um programa que calcula o IMC e verifica se a pessoa está dentro do peso ideal (IMC
entre 18.5 e 24.9).
'''
# Solicitar dados ao usuário:
peso = float(input("Por favor, digite o seu peso em kg: "))
altura = float(input("Por favor, digite a sua altura em metros: "))

# Calcular o valor do IMC
imc = peso / (altura ** 2)

#  Verificar peso ideal
peso_ideal = (imc >= 18.5) and (imc <= 24.9)

print("O seu IMC é igual: ", imc)
print("Você está no peso ideal: ", peso_ideal)