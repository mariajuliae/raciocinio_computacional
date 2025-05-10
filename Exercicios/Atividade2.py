#Exercício de fixação 2: Crie um programa que pergunte o nome do cliente para ser inserido em um cartão de crédito, com espaço máximo de 20 caracteres. Caso o usuário informe um nome maior, deve mostrar uma mensagem informando que o nome é extenso demais e deve ser abreviado. Dica: para saber o tamanho de uma string, usar a função len. Exemplo: len(nome)
nome = input("Qual o seu nome?")
if len(nome) > 20:
    print ("O nome é extenso demais e deve ser abreviado")