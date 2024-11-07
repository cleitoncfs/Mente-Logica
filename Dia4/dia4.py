'''
Exemplos com Analogias do Mundo Real:
1. Decidindo o Que Vestir
Situação: Você olha pela janela para ver o clima e decide o que vestir.
'''
clima = 'chuvoso'

if clima == 'ensolarado':
    print('Vista um short e uma camiseta.')
elif clima == 'nublado':
    print('Leve um casaco.')
elif clima == 'chuvoso':
    print('Não se esqueça de levar um guarda-chuva')
else:
    print('Verifique a previsão do tempo')
'''
Análise:
● O programa verifica a variável clima.
● Dependendo do valor, ele sugere o que vestir.
● Se o clima não corresponder a nenhuma condição, ele sugere verificar a previsão.
===================================================================================
'''

'''
2. Semáforo
Situação: Ao dirigir, você reage de acordo com a cor do semáforo.
'''
semaforo = 'amarelo'

if semaforo == 'verde':
    print('Siga em frente...')
elif semaforo == 'Amarelo':
    print('Atenção, se prepare para parar.')
elif semaforo == 'vermelho':
    print("Pare o carro.")
else:
    print('Sinal desconhecido, tenha cautela.')
'''
Análise:
● O programa verifica a cor do semáforo.
● Executa a ação correspondente a cada cor.
● Se encontrar um sinal desconhecido, alerta o motorista.
==================================================================================
'''

'''
3. Calculando Descontos em Compras
Situação: Uma loja oferece descontos com base no valor da compra.
● Se o valor for maior ou igual a R$1000, o desconto é de 10%.
● Se for entre R$500 e R$999, o desconto é de 5%.
● Caso contrário, não há desconto.
'''
valor_compra = 1200

if valor_compra >= 1000:
    desconto = valor_compra * 0.10
    print(f'Você recebeu um desconto de 10%, o valor do desconto foi de R$ , {desconto:.2f}')
elif valor_compra >= 500:
    desconto = valor_compra * 0.05
    print(f"Você recebeu um desconto de 5%, no valor de R$ , {desconto:.f2}")
else:
    print('Infelizmente você não recebeu nenhum desconto nesta compra.')
'''
Análise:
● O programa calcula o desconto com base no valor da compra.
● Aplica o desconto adequado.
● Calcula e exibe o valor final.
==================================================================================
'''

'''
4. Planejando um Passeio
Situação: Você quer fazer um passeio ao parque, mas depende do clima e do dia da
semana.
● Se for fim de semana (sábado ou domingo) e não estiver chovendo, você vai ao
parque.
● Caso contrário, fica em casa e assiste a um filme.
'''
dia_da_semana = 'sabado'
chovendo = False

if (dia_da_semana == 'sabado' or dia_da_semana == 'domingo') and not chovendo:
    print('Hoje é um ótimo dia para ir ao parque!')
else:
    print('Fique em casa e assista a um bom filme.')
'''
Análise:
● Usa operadores lógicos para combinar condições.
● Verifica se é fim de semana e se não está chovendo.
● Toma a decisão com base nas condições.
'''

'''
Exercícios Práticos:
1. Verificando Se um Número é Positivo, Negativo ou Zero
Crie um programa que solicita um número ao usuário e verifica se ele é positivo, negativo
ou zero.
'''
numero = int(input('Por favor digite um número: '))

if numero > 0:
    print("O número é postivo.")
elif numero < 0:
    print("O número é negativo")
else:
    print("Você digitou zéro")
'''
Análise:
● O programa lê um número do usuário.
● Verifica se o número é maior que zero, menor que zero ou igual a zero.
● Exibe a mensagem correspondente.
'''

'''
2. Calculadora Simples
Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e realiza
o cálculo correspondente.
'''
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
operacao = input("Informe qual operação deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(f"O resultado da operação é: {int(numero1 + numero2)}")
elif operacao == '-':
    print(f"O resultado da operação é: {int(numero1 - numero2)}")
elif operacao == '*':
    print(f"O resultado da operação é: {int(numero1 * numero2)}")
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2  # Mantém como float para precisão
        print(f"O resultado da operação é: {resultado:.2f}")
    else:
        print("Erro: Divisão por ZERO!")
else:
    print("Erro: Operação inválida!")


'''
Análise:
● O programa solicita dois números e a operação desejada.
● Utiliza estruturas condicionais para realizar a operação correta.
● Verifica se a divisão por zero está sendo evitada.
'''

'''3. Classificação de Idade
Crie um programa que classifica a idade de uma pessoa em:
● Criança: 0 a 12 anos
● Adolescente: 13 a 17 anos
● Adulto: 18 a 59 anos
● Idoso: 60 anos ou mais
'''
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto.")
elif idade >= 60:
    print("Você é um idoso.")
else:
    print("Idade inválida.")

'''Análise:
● O programa lê a idade do usuário.
● Utiliza estruturas condicionais para classificar a idade.
● Inclui uma verificação para idades inválidas (números negativos).  
'''

'''
4. Verificando Ano Bissexto
Crie um programa que verifica se um ano é bissexto.
● Um ano é bissexto se for divisível por 4.
● Mas não é bissexto se for divisível por 100, exceto se for divisível por 400.
'''
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
'''
Análise:
● O programa verifica as condições específicas para um ano ser bissexto.
● Utiliza operadores lógicos para combinar as condições.
'''

'''
5. Simulador de Caixa Eletrônico
Crie um programa que simula um caixa eletrônico. O usuário deve informar o valor do saque
(apenas valores inteiros) e o programa deve informar quantas cédulas de cada valor serão
fornecidas.
● Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.
'''
valor_saque = int(input("Informe o valor do saque: R$"))

if valor_saque <= 0:
    print("Valor inválido!")
else:
    cedulas_100 = valor_saque // 100
    valor_saque %= 100
    cedulas_50 = valor_saque // 50
    valor_saque %= 50
    cedulas_20 = valor_saque // 20
    valor_saque %= 20
    cedulas_10 = valor_saque // 10
    valor_saque %= 10
    cedulas_5 = valor_saque // 5
    valor_saque %= 5
    cedulas_2 = valor_saque // 2
    valor_saque %= 2

    if valor_saque != 0:
        print("Não é possível sacar o valor especificado com as cédulas disponíveis.")
    else:
        print("Cédulas entregues:")
        if cedulas_100 > 0:
            print(f"{cedulas_100} x R$100")
        if cedulas_50 > 0:
            print(f"{cedulas_50} x R$50")
        if cedulas_20 > 0:
            print(f"{cedulas_20} x R$20")
        if cedulas_10 > 0:
            print(f"{cedulas_10} x R$10")
        if cedulas_5 > 0:
            print(f"{cedulas_5} x R$5")
        if cedulas_2 > 0:
            print(f"{cedulas_2} x R$2")
'''
Análise:

Divisões Inteiras e Operador Módulo:
O programa usa divisões inteiras (//) para determinar quantas cédulas de cada valor 
são necessárias.
O operador módulo (%) é utilizado para calcular o restante do valor após a retirada das 
cédulas de maior valor. Isso permite que o programa continue a calcular as cédulas necessárias 
para o valor restante.

Verificação de Disponibilidade das Cédulas:
Após calcular a quantidade de cédulas para cada denominação, o programa verifica se o valor 
restante é zero. Se o valor restante não for zero, significa que não é possível fornecer o 
valor exato com as cédulas disponíveis, e o programa informa ao usuário.
Esses dois pontos garantem que o programa funcione corretamente e informe ao usuário a 
quantidade de cédulas necessárias ou a impossibilidade de realizar o saque com as cédulas 
disponíveis.
'''