# Função utilitária
def limpar_tela():
    print("-------------------------------")

# 1 - Ler número inteiro
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"O número digitado foi: {numero}")
except ValueError:
    print("Você não digitou um número inteiro válido.")
limpar_tela()

# 2 - Multiplicação de dois números
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
except ValueError:
    print("Erro! Você digitou um número inválido!")
limpar_tela()

# 3 - Número inteiro com else
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro! Você não digitou um número inteiro válido.")
else:
    print(f"Você digitou o número inteiro: {numero}")
finally:
    limpar_tela()

# 4 - Abrir arquivo com finally
try:
    arquivo = open("dados.txt", "r")
    print("Arquivo aberto com sucesso.")
    print(arquivo.read())
except FileNotFoundError:
    print("Erro! Arquivo não encontrado.")
finally:
    print("Encerrando programa")
limpar_tela()

# 5 - Função dividir
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro! Divisão por zero não é permitida.")
    return a / b

try:
    print("Resultado:", dividir(10, 2))
    print("Resultado:", dividir(10, 5))
except ZeroDivisionError as e:
    print("Erro:", e)
limpar_tela()

# 6 - Exceção personalizada IdadeInvalidaError
class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError
    print(f"Idade {idade} cadastrada com sucesso.")

try:
    cadastrar_idade(25)
    cadastrar_idade(-5)
except IdadeInvalidaError:
    print("A idade não pode ser negativa!")
limpar_tela()

# 7 - Divisão com tratamento de ValueError e ZeroDivisionError
def divisao_usuario():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ValueError:
        print("Erro: Você precisa digitar apenas números!")
    except ZeroDivisionError:
        print("Erro: O número não pode ser dividido por zero!")
    finally:
        limpar_tela()

divisao_usuario()

# 8 - Verificar se número é par ou ímpar
def verificar_par():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Você precisa digitar um número inteiro válido!")
    finally:
        limpar_tela()

verificar_par()

# 9 - Função sacar com exceção personalizada
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente!")
    return saldo - valor

try:
    saldo_atual = 100
    saldo_atual = sacar(saldo_atual, 50)
    print("Saldo após saque:", saldo_atual)
    saldo_atual = sacar(saldo_atual, 100)  # Vai disparar SaldoInsuficienteError
except ValueError as ve:
    print("Erro:", ve)
except SaldoInsuficienteError as sie:
    print("Erro:", sie)
finally:
    limpar_tela()
