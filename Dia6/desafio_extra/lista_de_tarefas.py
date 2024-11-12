'''
Desafios Extras:

1. Lista de Tarefas
Crie um programa que gerencia uma lista de tarefas. O usuário deve ser capaz de:
● Adicionar uma tarefa
● Remover uma tarefa
● Listar todas as tarefas
'''
# Lista de Tarefas
tarefas = []

while True:
    print("\nMenu de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
    elif opcao == "2":
        tarefa = input("Digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso.")
        else:
            print("Tarefa não encontrada.")
    elif opcao == "3":
        print("\nLista de Tarefas:")
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"{idx}. {tarefa}")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
