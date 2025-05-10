#Exercício de fixação 3: Crie um programa que solicite um número ao usuário e informe se é par ou ímpar. Dica: para saber se um número é par ou ímpar, calcular o resto da divisão desse número por 2 (operador %). Se o resultado for 0, o número será par; se for 1, será ímpar.
numero = int(input("Digite um número: "))
if numero %2 == 0:
    print("O número é par.")
else:
    print("O número é impar")