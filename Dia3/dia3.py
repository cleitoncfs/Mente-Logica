'''
Exercícios Práticos com Situações do Dia a Dia

1. Calculando o Troco
Você foi a uma padaria e comprou alguns itens:
● Pão: R$3.50
● Leite: R$4.20
● Café: R$2.80
Você pagou com uma nota de R$20. Calcule quanto de troco você deve receber.
'''
# Preço dos itens:
pao = 3.50
leite = 4.20
cafe = 2.80

# Total da compra:
total_compra = pao + leite + cafe

# Valor pago:
valor_pago = 20.00

# Calcular troco:
troco = valor_pago - total_compra

print("O total da compra é igual a: R$", total_compra)
print("O valor do troco é igual a: R$", troco)


'''
2. Verificando Aprovação em um Exame
Para ser aprovado em um exame, um estudante precisa ter uma nota média maior ou igual
a 7.0 e uma frequência maior ou igual a 75%.
Dados:
● Nota média: 8.5
● Frequência: 80%
Verifique se o estudante foi aprovado.
'''
# Dados do estudante
nota_media = 8.5
frequencia = 80

# Verificar aprovação
aprovado = (nota_media >= 7.0) and (frequencia >= 75)

print("O estudante foi aprovado? ", aprovado)


'''
3. Oferta Especial
Uma loja oferece um desconto se o cliente comprar mais de 10 itens ou se o valor total da
compra for superior a R$100.
Dados:
● Quantidade de itens: 8
● Valor total: R$120
Verifique se o cliente tem direito ao desconto.
'''
# Dados da compra
quantidade_itens = 8
valor_total = 120

# Verificar desconto
desconto = (quantidade_itens > 10) or (valor_total > 100)

print("O cliente tem direito ao desconto? ", desconto)


'''
4. Sistema de Acesso
Para acessar uma área restrita, o usuário deve inserir a senha correta e não pode estar
bloqueado.
Dados:
● Senha inserida: "abcd1234"
● Senha correta: "abcd1234"
● Usuário bloqueado: False
Verifique se o acesso deve ser concedido.
'''
# Dados do usuário
senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False

# Verificação de acesso
acesso_concedido = (senha_inserida == senha_correta) and (usuario_bloqueado == False)

print("Acesso concedido? ", acesso_concedido)

'''
5. Divisão de Tarefas
Três amigos vão dividir igualmente uma conta de R$150. Verifique quanto cada um deve
pagar e se a divisão é exata (sem centavos restantes).
'''
# Valor total da conta
conta = 150

# Quantidade de amigos
amigos = 3

# Valor por pessoa
valor_pessoa = conta / amigos

# Verificar se a divisão é exata
divisao_exata = (conta % amigos) == 0

print("A divisão é exata? ", divisao_exata)
print("Qual é o valor a ser pago por cada pessoa? ", valor_pessoa)


