#Exercício de fixação 7: Crie um programa que pergunte o tamanho de três lados de um triângulo e informe o tipo de triângulo, a saber:
print("Informe os três lados de um triângulo: ")
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado3 + lado1 < lado2:
    print("Estes lados não formam um triângulo.")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("é um triângulo equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")