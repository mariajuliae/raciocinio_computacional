"""
Maria Julia Elias (11100010563_20251_04)
Atividade Formativa (S7)
"""

#carrego a biblioteca json
import json

#crio lista para cada uma das opções do menu principal
lista_estudantes = []
lista_disciplinas = []
lista_professores = []
lista_turmas= []
lista_matriculas = []


def carregar_arquivo(nome_arquivo, lista):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = json.load(arquivo)
    except:
        with open(nome_arquivo, "w") as arquivo:
            json.dump(lista, arquivo)

#ESTUDANTES
#carrega o conteudo do arquivo json pra a variavel lista_estudantes
#caso nao exista um arquivo criado ela cria um
def carregar_arquivo_estudantes():
    global lista_estudantes
    try:
        with open("lista_estudantes.json", "r") as arquivo:
            lista_estudantes = json.load(arquivo)
    except:
        with open("lista_estudantes.json", "w") as arquivo:
            json.dump(lista_estudantes, arquivo)


#carrega o conteudo do arquivo json pra a variavel lista_estudantes
#caso nao exista um arquivo criado ela cria um
def carregar_arquivo_disciplinas():
    global lista_disciplinas
    try:
        with open("lista_disciplinas.json", "r") as arquivo:
            lista_disciplinas = json.load(arquivo)
    except:
        with open("lista_disciplinas.json", "w") as arquivo:
            json.dump(lista_disciplinas, arquivo)


#carrega o conteudo do arquivo json pra a variavel lista_estudantes
#caso nao exista um arquivo criado ela cria um
def carregar_arquivo_professores():
    global lista_professores
    try:
        with open("lista_professores.json", "r") as arquivo:
            lista_professores = json.load(arquivo)
    except:
        with open("lista_professores.json", "w") as arquivo:
            json.dump(lista_professores, arquivo)


#carrega o conteudo do arquivo json pra a variavel lista_estudantes
#caso nao exista um arquivo criado ela cria um
def carregar_arquivo_turmas():
    global lista_turmas
    try:
        with open("lista_turmas.json", "r") as arquivo:
            lista_turmas = json.load(arquivo)
    except:
        with open("lista_turmas.json", "w") as arquivo:
            json.dump(lista_turmas, arquivo)


#carrega o conteudo do arquivo json pra a variavel lista_estudantes
#caso nao exista um arquivo criado ela cria um
def carregar_arquivo_matriculas():
    global lista_matriculas
    try:
        with open("lista_matriculas.json", "r") as arquivo:
            lista_matriculas = json.load(arquivo)
    except:
        with open("lista_matriculas.json", "w") as arquivo:
            json.dump(lista_matriculas, arquivo)


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
def incluir_estudante():
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
    salvar_arquivo()


def incluir_professor():
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
    salvar_arquivo()

#vincular salvar arquivo ao salvar arquivo do professor


def incluir_turma():
    codigo_turma = int(input("Digite o código da turma: "))
    codigo_professor = int(input("Digite o código do professor: "))
    codigo_disciplina = int(input("Digite o código da turma: "))

    # crio um dicionário para salvar as informações dos estudantes
    dicionario_turma = {
       # "codigo": codigo,
       # "nome": nome,
        #"cpf": cpf
    }
    # adiciono na minha lista de estudantes o dicionário do estudante
    lista_estudantes.append(dicionario_turma)
    # chamo a função salvar_arquivo para que os estudantes incluidos sejam salvos no arquivo
    salvar_arquivo()

#defino uma funçao para iniciar o listar do menu de operações
def listar_estudantes():
    if len(lista_estudantes) == 0:
        print("Não existe estudante cadastrado.")
    else:
        print("\nCÓDIGO | NOME | CPF")
        for dicionario_estudante in lista_estudantes:
            print(dicionario_estudante["codigo"],"|", dicionario_estudante["nome"],"|", dicionario_estudante["cpf"])
        print()


#defino uma funçao para iniciar o atualizar do menu de operações
def atualizar_estudante(codigo_para_editar):
    for dicionario_estudante in lista_estudantes:
        if dicionario_estudante["codigo"] == codigo_para_editar:
            dicionario_estudante["nome"] = input("Digite o novo nome: ")
            dicionario_estudante["cpf"] = input("Digite o novo CPF: ")
            print(f"O estudante", dicionario_estudante["codigo"], "foi atualizado com sucesso!")
            salvar_arquivo()
            return

    print("Código não encontrado. Tente novamente")


#defino uma funçao para iniciar o excluir do menu de operações
def excluir_estudante(codigo_para_excluir):
    excluir_estudante_da_lista = None
    for dicionario_estudante in lista_estudantes:
        if dicionario_estudante["codigo"] == codigo_para_excluir:
            excluir_estudante_da_lista = dicionario_estudante
            break

    if excluir_estudante_da_lista is None:
        print("Código não encontrado. Tente novamente")

    else:
        lista_estudantes.remove(excluir_estudante_da_lista)
        print(f"O estudante", excluir_estudante_da_lista["codigo"], "foi removido com sucesso!")
        salvar_arquivo()


#defino uma funçao para salvar os dados no arquivo
#ela vai criar ou abrir arquivo
def salvar_arquivo():
    with open("lista_estudantes.json", "w") as arquivo:
        json.dump(lista_estudantes, arquivo)


#defino uma funçao para ler os dados do arquivo
#mostra os dados já cadastrados no arquivo
def ler_arquivo():
    with open("lista_estudantes.json", "r") as arquivo:
        arquivo_lido = json.load(arquivo)
        print(arquivo_lido)


#defino uma funçao para mostrar a navegação interna dos menus e para chamar as funções
def main():
    #inicio a funçao carregar, para carregar os dados existentes no arquivo
    carregar_arquivo("lista_estudantes.json", lista_estudantes)
    carregar_arquivo("lista_professores.json", lista_professores)
    carregar_arquivo("lista_disciplinas.json", lista_disciplinas)
    carregar_arquivo("lista_turmas.json", lista_turmas)
    carregar_arquivo("lista_matriculas.json", lista_matriculas)
    #usei while True para o programa ficar em looping enquanto o usuário navega pelo menu principal
    # defino no elif e else o que cada comando vai fazer no menu principal
    while True:
        opcaomenu = iniciar_menu_principal()

        # se o usuário escolheu essa opção e vou para o menu seguinte
        if opcaomenu == 1:
            resposta = "Estudantes"
            print("Você escolheu a opção:", resposta)

            # usei while True para o programa ficar em looping enquanto o usuário navega pelo menu de operaçoes
            #defino no if, elif, else o que cada comando vai fazer no menu de operações
            while True:
                operacaomenu2 = iniciar_menu_operacoes(opcaomenu, resposta)
                print("Você escolheu a opção:", operacaomenu2)

                if operacaomenu2 == 1:
                    incluir_estudante()
                    print("Usuário cadastrado com sucesso!")

                elif operacaomenu2 == 2:
                    listar_estudantes()

                elif operacaomenu2 == 3:
                    codigo_estudante_para_editar = int(input("Digite o código do estudante para atualizar: "))
                    atualizar_estudante(codigo_estudante_para_editar)

                elif operacaomenu2 == 4:
                    codigo_estudante_para_excluir = int(input("Digite o código do estudante para excluir: "))
                    excluir_estudante(codigo_estudante_para_excluir)

                elif operacaomenu2 == 5:
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif 2 <= opcaomenu <= 5:
            print("Você escolheu a opção:", opcaomenu)
            print("Opção em desenvolvimento")

        # se o usuário escolher a opção sair do programa, eu finalizo ele aqui
        elif opcaomenu == 6:
            print("Finalizando o programa.")
            break

        # caso o usuario digite uma opcao que não está disponivel no menu principal
        else:
            print("Opção inválida. Escolha uma opção válida no menu.")
            # return

if __name__ == "__main__":
    main()