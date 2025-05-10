#Exemplo de aplicação 3: Elabore um programa que solicite ao usuário seu ano de nascimento e calcule sua idade. Para ser mais assertivo, também deve perguntar se o usuário já fez aniversário neste ano e analisar a influência dessa informação no cálculo da idade.

ano_atual = 2025
nascimento = int(input("Qual é o seu ano de nascimento? "))
idade = ano_atual - nascimento
resp = input("Você já fez aniversário neste ano? ")

if resp == "Não":
    idade -= 1

print("Sua idade é", idade)