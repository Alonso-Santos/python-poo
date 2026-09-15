tarefas = []


def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"nome": tarefa, "concluida": False})
    print("✅ Tarefa adicionada!")


def listar_tarefas():
    print("\n📋 LISTA DE TAREFAS")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {status} {tarefa['nome']}")


def concluir_tarefa():
    listar_tarefas()

    if tarefas:
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            print("✅ Tarefa concluída!")


def remover_tarefa():
    listar_tarefas()

    if tarefas:
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            print(f"🗑️ Tarefa '{removida['nome']}' removida!")


while True:
    print("""
========================
   CONTROLE DE TAREFAS
========================

1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        concluir_tarefa()

    elif opcao == "4":
        remover_tarefa()

    elif opcao == "5":
        print("👋 Programa encerrado!")
        break

    else:
        print("❌ Opção inválida!")
