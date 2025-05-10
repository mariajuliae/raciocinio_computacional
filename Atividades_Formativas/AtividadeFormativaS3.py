"""
Maria Julia Elias (11100010563_20251_04)
Atividade Formativa (S3)
"""

#criando um sistema CRUD

#mostrando o menu principal conforme descriçao solicitada no exercício
def menu1():
    print("----- MENU PRINCIPAL -----")
    print("(1) Estudantes")
    print("(2) Disciplinas")
    print("(3) Professores")
    print("(4) Turmas")
    print("(5) Matrículas")
    print("(6) Sair")

    #usei while True para o programa ficar em looping até o usuário dar uma resposta valida
    while True:
        # peço para o usuario informar a opcao que ele deseja
        opcaomenu1 = int(input("Informe a opção desejada do menu principal: "))

        #mostro a opção escolhida para usuário. uso a resposta dele em formato int e mudo para string
        if opcaomenu1 < 6:
            if opcaomenu1 == 1:
                resposta = "Estudantes"
            elif opcaomenu1 == 2:
                resposta = "Disciplina"
            elif opcaomenu1 == 3:
                resposta = "Professores"
            elif opcaomenu1 == 4:
                resposta = "Turmas"
            else:
                resposta = "Matrículas"
            print("Você escolheu a opção:", resposta)
            #se o usuário der uma resposta válida, eu paro o looping e vou para o menu seguinte
            menu2(opcaomenu1, resposta)
            break
        #se o usuário escolher a opção sair do programa, eu finalizo ele aqui
        elif opcaomenu1 == 6:
            print("Finalizando o programa.")
            break
        #caso o usuario digite uma opcao que não está disponivel no menu principal
        else:
            print("Opção invalida. Escolha uma opção válida no menu.")

#descriçao do menu de operações conforme solicitado no exercício
#aqui achei melhor utilizar dois parametros: um para apresentar a opção escolhida em formato int e outro com a string.
def menu2(opcao_menu_principal, resposta_menu_principal):
    print("----- Opção ",opcao_menu_principal,":",resposta_menu_principal,"- MENU DE OPERAÇÕES -----")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(5) Voltar ao menu principal")

    # usei while True para o programa ficar em looping até o usuário dar uma resposta valida
    while True:
        #peço para informar a opçao do menu de operações
        opcaomenu2 = int(input("Informe a opção desejada do menu de operações: "))

        #mostro a opção escolhida
        #aqui como ainda não vamos para segunda parte, resolvi fazer de forma mais direta, para ser mais simples
        if opcaomenu2 < 5:
            print("Você escolheu a opção: ", opcaomenu2)
            #aqui deixei o break comentado para o while True ficar em looping até o usuário escolher a opção 5
            print("Escolha outra opção do menu de operações.")
            #break

        #crio a opção de voltar ao menu principal como solicitado
        elif opcaomenu2 == 5:
            print("Voltando ao menu principal")
            menu1()
            break

        # caso o usuario digite uma opcao que não está disponivel no menu de operações
        else:
            print("Opção invalida. Informe uma opção válida.")

def main():
    menu1()

if __name__ == "__main__":
    main()








# função para incluir estudantes
def incluir_estudante():
    nome = input("Digite o nome do estudante: ")
    estudantes.append(nome)
    print("Estudante -", nome, "- incluído com sucesso!")

# função para listar estudantes
def listar_estudantes():
    if estudantes:
        print("----- Lista de Estudantes -----")
        for estudante in estudantes:
            print(f"- {estudante}")
    else:
        print("Nenhum estudante cadastrado.")

# função principal que controla o fluxo
def main():
    # uso while True para manter o programa funcionando até o usuário escolher sair
    while True:
        opcao = menu1()

        if opcao == 1:
            # enquanto o usuário estiver no menu de estudantes
            while True:
                operacao = menu2()

                if operacao == 1:
                    incluir_estudante()

                elif operacao == 2:
                    listar_estudantes()

                elif 3 >= operacao <= 4:
                    print("Menu em desenvolvimento. Escolha outra opção.")

                elif operacao == 5:
                    # volto ao menu principal
                    break

        elif 2 >= opcao <= 5:
            print("Menu em desenvolvimento. Escolha outra opção.")

        elif opcao == 6:
            print("Finalizando o programa.")
            break

# aqui defino o ponto de partida da execução
if __name__ == "__main__":
    main()
