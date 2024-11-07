'''
Desafios Extras:

1. Aprovando Empréstimo Bancário
Crie um programa para uma instituição bancária que analisa o pedido de empréstimo.
● O cliente deve informar o valor do empréstimo, a renda mensal e o número de
parcelas.
● O empréstimo será aprovado se o valor da parcela não exceder 30% da renda
mensal.
'''
valor_emprestimo = float(input("Digite o valor do empréstimo: R$"))
renda_mensal = float(input("Informe a sua renda mensal: R$"))
qtd_parcelas = int(input("Informe a quantidade de parcelas: "))

valor_parcela = valor_emprestimo / qtd_parcelas
limite_valor_parcela = renda_mensal * 0.30

if valor_parcela <= limite_valor_parcela:
    print("Empréstimo aprovado!")
    print(f"Valor da parcela: R${valor_parcela:.2f}")
else:
    print("Empréstimo negado!")
    print(f"Valor da parcela R${valor_parcela:.2f} excede 30% da renda mensal.")