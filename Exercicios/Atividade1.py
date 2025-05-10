#Exercício de fixação 1: Crie um programa que pergunte a idade do usuário. Caso seja maior de idade, deve mostrar uma mensagem informando que pode se inscrever para fazer o teste para tirar a carteira de motorista.
#idade = int(input("Qual a sua idade: "))
#if idade >= 18:
    #print ("Você pode se inscrever.")


def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Estudantes")
        print("2. Disciplinas")
        print("3. Professores")
        print("4. Turmas")
        print("5. Matrículas")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_operacoes("Estudantes")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '2':
            menu_operacoes("Disciplinas")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '3':
            menu_operacoes("Professores")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '4':
            menu_operacoes("Turmas")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '5':
            menu_operacoes("Matrículas")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '6':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_operacoes(entidade):
    while True:
        print(f"\n--- Operações de {entidade} ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Escolha uma operação: ")

        if opcao == '1':
            print(f"Você escolheu: Incluir {entidade}")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '2':
            print(f"Você escolheu: Listar {entidade}")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '3':
            print(f"Você escolheu: Atualizar {entidade}")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '4':
            print(f"Você escolheu: Excluir {entidade}")
            break  # Encerra após escolher a funcionalidade
        elif opcao == '5':
            print("Voltando ao menu principal.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()