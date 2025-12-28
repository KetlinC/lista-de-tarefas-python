def mostrar_menu():
    print("---------- MENU ----------\n")
    print("1. Adicionar uma tarefa")
    print("2. Listar tarefas")
    print("3. Remover uma tarefa")
    print("4. Sair do programa\n")
    print("--------------------------")


tarefas = []
def adicionar_tarefa():
    nova_tarefa = input("Digite a nova tarefa: ")
    nova_tarefa.lower()
    if nova_tarefa in tarefas:
        print("Tarefa Repetida, não incluída.")
    else:
        tarefas.append(nova_tarefa)
        print("Nova Tarefa Adicionada!")


def listar_tarefas():
    print(f"Suas tarefas são: {tarefas}")

def remover_tarefas():
    tarefa_remover = input("Digite a tarefa a ser removida: ")
    tarefa_remover

    if tarefa_remover.lower() in tarefas:
        tarefas.remove(tarefa_remover)
        print("Tarefa Removida!")
    else:
        print("Impossível remover. Nâo há esta tarefa na lista")





def main():
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        

        if opcao == "1":
            
            adicionar_tarefa()
            

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            remover_tarefas()

        elif opcao == "4":
            print("Saindo do Programa!")
            break
        
        else:
            print("Opção inválida, digite novamente um valor válido.")

main()