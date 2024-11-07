'''
3. Calculadora de Tarifas de Táxi:
Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro
rodado. Crie um programa que calcula o valor total da corrida com base na distância
percorrida.
'''
distancia = float(input("Informe a distância percorrida em km: "))

tarifa_basica = 4.00
taxa_km = 0.25

total = tarifa_basica + (distancia * taxa_km)
print(f"O valor da corrida é: {total:.2f}")
