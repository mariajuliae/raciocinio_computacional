#criando um sistema CRUD

#mostrando o menu conforme descriçao solicitada no exercício
def menu1():
    print("----- MENU PRINCIPAL -----")
    print("(1) Estudantes")
    print("(2) Disciplinas")
    print("(3) Professores")
    print("(4) Turmas")
    print("(5) Matrículas")
    print("(6) Sair")

    #
    while True:
        # peço para o usuario informar a opcao que ele deseja
        opcaomenu1 = int(input("Informe a opção desejada do menu principal: "))

        #mostro a opção escolhida se tiver no menu principal
        if opcaomenu1 < 6:
            print("Você escolheu a opção: ", opcaomenu1)
            menu2(opcaomenu1)
            break
        elif opcaomenu1 == 6:
            print("Finalizando o programa.")
            break
        #caso o usuario digite uma opcao que não está disponivel no menu principal
        else:
            print("Opção invalida. Escolha uma opção válida no menu.")



#descriçao do menu conforme solicitado no exercício
def menu2(opcao_menu_principal):
    print("----- Opção ", opcao_menu_principal, " - MENU DE OPERAÇÕES -----")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(5) Voltar ao menu principal")

    while True:
        #peço para informar a opçao do menu de operações
        opcaomenu2 = int(input("Informe a opção desejada do menu de operações: "))

        #mostro a opção escolhida
        if opcaomenu2 < 5:
            print("Você escolheu a opção: ", opcaomenu2)
            print("Finalizando o programa.")
            break

        elif opcaomenu2 == 5:
            print("Voltando ao menu principal")
            #menu1()
            break

        else:
            print("Opção invalida. Informe uma opção válida.")

def main():
    menu1()

if __name__ == "__main__":
    main()
