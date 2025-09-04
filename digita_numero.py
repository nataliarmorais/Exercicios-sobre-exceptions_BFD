
def limpar_tela():
    print("-------------------------------")

try:
    numero = int(input("Digite um número inteiro :"))
    print(f"O numero digitado foi: {numero}")
except ValueError:
    print("Você não digitou um número inteiro válido.")

limpar_tela()
try:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero:"))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é : {resultado}")
except ValueError:
    print("Erro! Você digitou um numero invalido!")
