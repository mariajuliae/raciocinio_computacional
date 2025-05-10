"""
Maria Julia Elias (11100010563_20251_04)
Atividade Somativa (S8)
"""

#carrego a biblioteca json
import json

#crio lista para cada uma das opções do menu principal
lista_estudantes = []
lista_disciplinas = []
lista_professores = []
lista_turmas= []
lista_matriculas = []


#carrega o conteudo do arquivo json recebido pra a variavel lista recebida
#caso nao exista um arquivo criado ela cria um
def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except:
        with open(nome_arquivo, "w") as arquivo:
            json.dump([], arquivo)
        return []


#defino uma funçao para iniciar o menu principal
def iniciar_menu_principal():
    # apresento o menu
    print("----- MENU PRINCIPAL -----")
    print("(1) Estudantes\n(2) Disciplinas\n(3) Professores\n(4) Turmas\n(5) Matrículas\n(6) Sair")
    # peço para o usuário informar a opção que ele deseja e retorno aqui apos cada inserção
    try:
        return int(input("Informe a opção desejada do menu principal: "))
    except:
        print("Você deve digitar um número")
        return


#defino uma funçao para iniciar o menu de operações
def iniciar_menu_operacoes(opcaomenu, resposta):
    print("----- Opção", opcaomenu, ":", resposta, "- MENU DE OPERAÇÕES -----")
    print("(1) Incluir\n(2) Listar\n(3) Atualizar\n(4) Excluir\n(5) Voltar ao menu principal")
    try:
        return int(input("Informe a opção desejada do menu de operações: "))
    except:
        print("Você deve digitar um número")
        return


#defino uma funçao para iniciar o incluir do menu de operações

def incluir(tipo):
    try:
        if tipo == "Estudantes":
            codigo = int(input("Digite o código do estudante: "))
            nome = input("Digite o nome do estudante: ")
            cpf = input("Digite o cpf do estudante: ")

            #crio um dicionário para salvar as informações dos estudantes
            dicionario_estudante = {
                "codigo": codigo,
                "nome": nome,
                "cpf": cpf
            }
            #adiciono na minha lista de estudantes o dicionário do estudante
            lista_estudantes.append(dicionario_estudante)
            #chamo a função salvar_arquivo para que os estudantes incluidos sejam salvos no arquivo
            salvar_arquivo("lista_estudante.json", lista_estudantes)

        elif tipo == "Disciplinas":
            codigo = int(input("Digite o código da disciplina: "))
            nome = input("Digite o nome da disciplina ")

            # crio um dicionário para salvar as informações dos estudantes
            dicionario_disciplina = {
                "codigo": codigo,
                "nome": nome

            }
            # adiciono na minha lista de estudantes o dicionário do estudante
            lista_disciplinas.append(dicionario_disciplina)
            # chamo a função salvar_arquivo para que os estudantes incluidos sejam salvos no arquivo
            salvar_arquivo("lista_disciplinas.json", lista_disciplinas)

        elif tipo == "Professores":
            codigo = int(input("Digite o código do professor: "))
            nome = input("Digite o nome do professor: ")
            cpf = input("Digite o cpf do professor: ")

            # crio um dicionário para salvar as informações dos estudantes
            dicionario_professor = {
                "codigo": codigo,
                "nome": nome,
                "cpf": cpf
            }
            # adiciono na minha lista de estudantes o dicionário do estudante
            lista_professores.append(dicionario_professor)
            # chamo a função salvar_arquivo para que os estudantes incluidos sejam salvos no arquivo
            salvar_arquivo("lista_professores.json", lista_professores)

        elif tipo == "Turmas":
            codigo = int(input("Digite o código da turma: "))
            codigo_professor = int(input("Digite o código do professor: "))
            codigo_disciplina = int(input("Digite o código da turma: "))

            # crio um dicionário para salvar as informações dos estudantes
            dicionario_turmas = {
                "codigo": codigo,
                "codigo_professor": codigo_professor,
                "codigo_disciplina": codigo_disciplina
            }

            # adiciono na minha lista de estudantes o dicionário do estudante
            lista_turmas.append(dicionario_turmas)
            # chamo a função salvar_arquivo para que os estudantes incluidos sejam salvos no arquivo
            salvar_arquivo("lista_turmas.json", lista_turmas)

        elif tipo == "Matrículas":
            codigo_turma = int(input("Digite o código da turma: "))
            codigo_estudante = int(input("Digite o código do estudante: "))

            # crio um dicionário para salvar as informações dos estudantes
            dicionario_matriculas = {
                "codigo_turma": codigo_turma,
                "codigo_estudante": codigo_estudante
            }

            # adiciono na minha lista de estudantes o dicionário do estudante
            lista_matriculas.append(dicionario_matriculas)
            # chamo a função salvar_arquivo para que os estudantes incluidos sejam salvos no arquivo
            salvar_arquivo("lista_matriculas.json", lista_matriculas)
        else:
            print("Dados não encontrados")

    except:
        print("Erro ao incluir. Verifique os dados.")


#defino uma funçao para iniciar o listar do menu de operações
def listar(lista):
    if len(lista) == 0:
        print("Não existem dados cadastrados.")
    else:
        for dicionario_geral in lista:
            if lista == lista_estudantes:
                print("\nCÓDIGO | NOME | CPF")
                print(dicionario_geral["codigo"],"|", dicionario_geral["nome"],"|", dicionario_geral["cpf"])
                print()

            elif lista == lista_disciplinas:
                print("\nCÓDIGO | NOME")
                print(dicionario_geral["codigo"],"|", dicionario_geral["nome"])
                print()

            elif lista == lista_professores:
                print("\nCÓDIGO | NOME | CPF")
                print(dicionario_geral["codigo"],"|", dicionario_geral["nome"],"|", dicionario_geral["cpf"])
                print()

            elif lista == lista_turmas:
                print("\nCOD. TURMA | COD. PROFESSOR | COD. DISCIPLINA")
                print(dicionario_geral["codigo"],"|", dicionario_geral["codigo_professor"],"|", dicionario_geral["codigo_disciplina"])
                print()

            else:
                print("\nCOD. TURMA | COD. ESTUDANTE")
                print(dicionario_geral["codigo"],"|", dicionario_geral["codigo_estudante"])
                print()

#defino uma funçao para iniciar o atualizar do menu de operações
def atualizar(codigo_para_editar, nome_arquivo):
    try:
        for estudante in lista_estudantes:
            if estudante["codigo"] == codigo_para_editar:
                estudante["nome"] = input("Digite o novo nome: ")
                estudante["cpf"] = input("Digite o novo CPF: ")
                print("Atualizado com sucesso!")
                salvar_arquivo(nome_arquivo, lista_estudantes)
                return

        for disciplina in lista_disciplinas:
            if disciplina["codigo"] == codigo_para_editar:
                disciplina["nome"] = input("Digite o novo nome: ")
                print("Atualizado com sucesso!")
                salvar_arquivo(nome_arquivo, lista_disciplinas)
                return

        for professor in lista_professores:
            if professor["codigo"] == codigo_para_editar:
                professor["nome"] = input("Digite o novo nome: ")
                professor["cpf"] = input("Digite o novo CPF: ")
                print("Atualizado com sucesso!")
                salvar_arquivo(nome_arquivo, lista_professores)
                return

        for turma in lista_turmas:
            if turma["codigo"] == codigo_para_editar:
                turma["codigo_professor"] = int(input("Digite o novo códido do professor: "))
                turma["codigo_disciplina"] = int(input("Digite o novo código da disciplina: "))
                print("Atualizado com sucesso!")
                salvar_arquivo(nome_arquivo, lista_turmas)
                return

        for matricula in lista_matriculas:
            if matricula["codigo"] == codigo_para_editar:
                matricula["codigo_estudante"] = input("Digite o novo código: ")
                print("Atualizado com sucesso!")
                salvar_arquivo(nome_arquivo, lista_matriculas)
                return
        print("Código não encontrado.")
    except:
        print("Erro ao atualizar. Verifique os dados.")

#defino uma funçao para iniciar o excluir do menu de operações
def excluir(codigo, lista, nome_arquivo):
    try:
        for item in lista:
            if "codigo" in item and item["codigo"] == codigo:
                lista.remove(item)
                salvar_arquivo(nome_arquivo, lista)
                print("Removido com sucesso!")
                return
            elif "codigo_turma" in item and item["codigo_turma"] == codigo:
                lista.remove(item)
                salvar_arquivo(nome_arquivo, lista)
                print("Removido com sucesso!")
                return
        print("Código não encontrado.")
    except:
        print("Erro ao excluir. Verifique os dados.")


#defino uma funçao para salvar os dados no arquivo
#ela vai criar ou abrir arquivo
def salvar_arquivo(nome_arquivo, lista):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo)


#defino uma funçao para ler os dados do arquivo
#mostra os dados já cadastrados no arquivo
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        arquivo_lido = json.load(arquivo)
        print(arquivo_lido)


#defino uma funçao para mostrar a navegação interna dos menus e para chamar as funções
def main():

    #inicio a funçao carregar, para carregar os dados existentes no arquivo
    global lista_estudantes, lista_disciplinas, lista_professores, lista_turmas, lista_matriculas
    lista_estudantes = carregar_arquivo("lista_estudantes.json")
    lista_disciplinas = carregar_arquivo("lista_disciplinas.json")
    lista_professores = carregar_arquivo("lista_professores.json")
    lista_turmas = carregar_arquivo("lista_turmas.json")
    lista_matriculas = carregar_arquivo("lista_matriculas.json")

    #usei while True para o programa ficar em looping enquanto o usuário navega pelo menu principal
    # defino no elif e else o que cada comando vai fazer no menu principal
    while True:
        opcaomenu = iniciar_menu_principal()

        # se o usuário escolheu essa opção e vou para o menu seguinte
        lista = None
        if opcaomenu < 6 :
            if opcaomenu == 1:
                escolha_menu_principal = "Estudantes"
                lista = lista_estudantes
                nome_arquivo = "lista_estudantes.json"

            elif opcaomenu == 2:
                escolha_menu_principal = "Disciplinas"
                lista = lista_disciplinas
                nome_arquivo = "lista_disciplinas.json"

            elif opcaomenu == 3:
                escolha_menu_principal = "Professores"
                lista = lista_professores
                nome_arquivo = "lista_professores.json"

            elif opcaomenu == 4:
                escolha_menu_principal = "Turmas"
                lista = lista_turmas
                nome_arquivo = "lista_turmas.json"

            elif opcaomenu == 5:
                escolha_menu_principal = "Matrículas"
                lista = lista_matriculas
                nome_arquivo = "lista_matriculas.json"

            #usei while True para o programa ficar em looping enquanto o usuário navega pelo menu de operaçoes
            #defino no if, elif, else o que cada comando vai fazer no menu de operações
            while True:
                operacaomenu2 = iniciar_menu_operacoes(opcaomenu, escolha_menu_principal)
                #print("Você escolheu a opção:", operacaomenu2)

                if operacaomenu2 == 1:
                    incluir(escolha_menu_principal)

                elif operacaomenu2 == 2:
                    listar(lista)

                elif operacaomenu2 == 3:
                    codigo_para_editar = int(input("Digite o código para atualizar: "))
                    atualizar(codigo_para_editar, nome_arquivo)

                elif operacaomenu2 == 4:
                    codigo_para_excluir = int(input("Digite o código para excluir: "))
                    excluir(codigo_para_excluir, lista, nome_arquivo)

                elif operacaomenu2 == 5:
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        # se o usuário escolher a opção sair do programa, eu finalizo ele aqui
        elif opcaomenu == 6:
            print("Finalizando o programa.")
            break

        # caso o usuario digite uma opcao que não está disponivel no menu principal
        else:
            print("Opção inválida. Escolha uma opção válida no menu.")


if __name__ == "__main__":
    main()