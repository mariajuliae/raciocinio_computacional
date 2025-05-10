"""
Maria Julia Elias (11100010563_20251_04)
Atividade Formativa (S5)
"""

#criando um sistema CRUD
lista_estudantes = []

#mostrando o menu principal conforme descriçao solicitada no exercício
def menu1():
    print("----- MENU PRINCIPAL -----")
    print("(1) Estudantes")
    print("(2) Disciplinas")
    print("(3) Professores")
    print("(4) Turmas")
    print("(5) Matrículas")
    print("(6) Sair")

    #usei while True para o programa ficar em looping até o usuário dar uma resposta válida
    while True:
        #peço para o usuário informar a opção que ele deseja
        opcaomenu1 = int(input("Informe a opção desejada do menu principal: "))
        print("Você escolheu a opção:", opcaomenu1)

        #se o usuário escolheu essa opção e vou para o menu seguinte
        if opcaomenu1 == 1:
            resposta = "Estudantes"
            menu2(opcaomenu1, resposta)
            break

        #informo que a opção (2,3,4,5) ainda não estão funcionando
        #retorno ao menu principal
        elif opcaomenu1 <= 5:
            if opcaomenu1 == 2:
                resposta = "Disciplina"
            elif opcaomenu1 == 3:
                resposta = "Professores"
            elif opcaomenu1 == 4:
                resposta = "Turmas"
            else:
                resposta = "Matrículas"
            print("Opção não está disponível")
            #menu2(opcaomenu1, resposta)

        # se o usuário escolher a opção sair do programa, eu finalizo ele aqui
        elif opcaomenu1 == 6:
            print("Finalizando o programa.")
            break
        # caso o usuario digite uma opcao que não está disponivel no menu principal
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

    # usei while True para o programa ficar em looping até o usuário dar uma resposta válida
    while True:
        # peço para o usuário informar a opção que ele deseja
        operacaomenu2 = int(input("Informe a opção desejada do menu de operações: "))
        print("Você escolheu a opção:", operacaomenu2)

        if operacaomenu2 <= 4:
            if operacaomenu2 == 1:
                #resposta_operacao = "Incluir"
                incluir()

            elif operacaomenu2 == 2:
                #resposta_operacao = "Listar"
                listar()

            elif operacaomenu2 == 3:
                #resposta_operacao = "Atualizar"
                atualizar()

            else:
                #resposta_operacao = "Excluir"
                excluir()
            break

         #opçao para caso usuário deseje sair do promama
        elif operacaomenu2 == 5:
            print("Voltando ao menu principal")
            return menu1()
            break

        #opcao para caso o usuario digite algo errado
        else:
            print("Opção inválida. Escolha uma opção válida.")

#parametros do menu de operaçoes da opção inlcuir
def incluir():
    #coloco em looping [ara ser possivel cadastrar quantos estudantes forem necessários
    while True:
        codigo = int(input("Digite o código do estudante: "))
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")

        #criando o dicionario
        estudante = {
            "codigo_estudante": codigo,
            "nome_estudante": nome,
            "cpf_estudante": cpf
        }
        #guardando o estudante cadastrado no append
        lista_estudantes.append(estudante)
        print(f"Estudante",nome,"foi incluido com sucesso!")

        #criando uma opcao para que o usuário possa parar o looping e sair do modo incluir
        incluir_novo = input("Deseja cadastrar um novo estudante? [sim/nao]: ")
        if incluir_novo == "nao":
            return menu1()
            break

#parametros do menu de operaçoes da opção listar
def listar():
    #aqui estabeleço que se a lista for diferente de 0, eu listo ela para usuário
    if len(lista_estudantes) != 0:
        print("\n----Lista de Estudantes----")
        print("CÓDIGO  |  NOME  |  CPF")

        #apresento a lista com os parametros que eu criei
        for estudante in lista_estudantes:
            print(estudante["codigo_estudante"],"|", estudante["nome_estudante"],"|", estudante["cpf_estudante"])

    #caso a lista seja igual a zero
    else:
        print("Não há estudantes cadastrados.")

    return menu1()

#parametros do menu de operaçoes da opção atualizar
def atualizar():
    codigo_para_atualizar = int(input("Qual é o código do estudante que deseja atualizar? "))
    # aqui informo que cada parametro está vazio, até ter valor dentro
    estudante_para_atualizar = None
    for estudante in lista_estudantes:
        #aqui digo que se os codigo cadastro no meu parametro estudante for iagual ao codigo a ser atualizado, eu vou salavar ele na lista estudantes_para_atualizar
        if estudante["codigo_estudante"] == codigo_para_atualizar:
            estudante_para_atualizar = estudante
            break

    #aqui informo que cada parametro está vazio, até ter valor dentro
    novo_codigo = None
    novo_nome = None
    novo_cpf = None

    #aqui crio while true para que o input fique em looping até a pessoa optar pelo nao
    #crio o input para os parametros a serem modificados
    while True:
        atualizar_estudante = input("O que você gostaria de atualizar? [codigo/nome/cpf] " )
        if atualizar_estudante == "codigo":
            novo_codigo = int(input("Digite o novo código: "))

        elif atualizar_estudante == "nome":
            novo_nome = input("Digite o novo nome: ")

        elif atualizar_estudante == "cpf":
            novo_cpf = input("Digite o novo CPF: ")

        else:
            print("Opção inválida. Tente novamente.")

        #crio opcao para caso a pessoa queira atualizar mais estudantes cadastrados
        #aqui relaciono o código antigo ao parametro novo
        continuar_atualizando = input("Deseja continuar atualizando? [sim/nao] ")
        if continuar_atualizando == "nao":
            if novo_codigo != None:
                estudante_para_atualizar["codigo_estudante"] = novo_codigo
            if novo_nome != None:
                estudante_para_atualizar["nome_estudante"] = novo_nome
            if novo_cpf != None:
                estudante_para_atualizar["cpf_estudante"] = novo_cpf
            #informo que a atualizaçao foi realizada
            print("Atualização realizada com sucesso!")
            #listo para o usuário verificar a atualizaçao
            print(estudante["codigo_estudante"],"|", estudante["nome_estudante"],"|", estudante["cpf_estudante"])
            return menu1()
            break

#parametros do menu de operaçoes da opção excluir
def excluir():
    codigo_para_excluir = int(input("Qual é o código que deseja excluir? "))
    #aqui informo que cada parametro está vazio, até ter valor dentro
    estudante_para_ser_removido = None
    #aqui digo que se os codigo cadastro no meu parametro estudante for igual ao codigo a ser excluido, eu vou salvar ele na lista estudantes_para_ser_removido
    for estudante in lista_estudantes:
        if estudante["codigo_estudante"] == codigo_para_excluir:
            estudante_para_ser_removido = estudante
            break

    #aqui crio parametros para cado o codigo nao exista no sistema e dou opcao para o usuário voltar ao menu
    if estudante_para_ser_removido is None:
        print("Código não encontrado. Nenhum estudante foi removido.")
        return excluir()

    else:
        #salvo o dado para excluir na lista criada e a removo da lista principal
        lista_estudantes.remove(estudante_para_ser_removido)
        # listo para o usuário verificar a atualizaçao
        print(estudante["codigo_estudante"],"|", estudante["nome_estudante"],"|", estudante["cpf_estudante"])
        print("Estudante removido com sucesso!")
        return menu1()

#inicio o código
def main():
    menu1()

if __name__ == "__main__":
    main()