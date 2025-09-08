
<<<<<<< HEAD
=======
# 1 - Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

>>>>>>> dd73772 (Primeiro commit)
def limpar_tela():
    print("-------------------------------")

try:
    numero = int(input("Digite um número inteiro :"))
    print(f"O numero digitado foi: {numero}")
except ValueError:
    print("Você não digitou um número inteiro válido.")

limpar_tela()
<<<<<<< HEAD
try:
=======

#2 - Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

def limpar_tela():
    print("-------------------------------")
try:
    
>>>>>>> dd73772 (Primeiro commit)
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero:"))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é : {resultado}")
except ValueError:
    print("Erro! Você digitou um numero invalido!")
<<<<<<< HEAD
=======
    
limpar_tela()

# 3 - Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
def limpar_tela():
    print("-------------------------------")
try :
    numero = int(input ("Digite um numero inteiro : "))
except ValueError:
    print("Erro! Você não digitou um número inteiro válido.")
else :
    print(f"Você digitou o número inteiro: {numero}")
finally:
    limpar_tela()
    
# 4 - Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

def limpar_tela ():
    print("-------------------------------")
try: 
        arquivo = open ("dados.txt", "r")  
        print ("Arquivo aberto com sucesso.")
        conteudo = arquivo.read()
        print (conteudo)
except FileNotFoundError:
        print("Erro! Arquivo não encontrado.")
finally :
        print("Encerrando programa")
limpar_tela()  


# 5 - Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

def limpar_tela():
    print("-------------------------------")

def dividir (a,b):
    if b ==0:
        raise ZeroDivisionError("Erro! Divisão por zero não é permitida.")
    return (a/b)
try:
    resultado = dividir (10,2)
    print ("Resultado", resultado)
    
    resultado = dividir (10,5)
    print ("Resultado", resultado)
except ZeroDivisionError as e:
    print ("Erro:", e)

limpar_tela()

# 6 - Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

def limpar_tela():
    print ("-----------------------")
class IdadeInvalidaError(Exception):
    pass
def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError
    print (f'Idade {idade} cadastrada com sucesso.')
try:
    cadastrar_idade(25)
    cadastrar_idade(-5)
    
except IdadeInvalidaError:

 print( "A idade não pode ser negativa !")
 
 limpar_tela()

# 7 -Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
#ValueError se o usuário digitar algo inválido
#ZeroDivisionError se tentar dividir por zero
def limpar_tela():
    print ("--------------------")
    
def numero ():
    
    try:
     num1 = float(input("Digita o primeiro numero:"))
     num2 = float(input("Digita o segundo numero:"))
     resultado =num1/num2
     print (f" O resultado da divisão é : {resultado}")
     
    except ValueError:
     print ("Erro: Você precisa digitar apenas números!")
     
    except ZeroDivisionError:
        print("Erro: O número não pode ser dividido por zero!")
        
    limpar_tela ()
numero()

# 8 - Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
#try para a conversão,
#else para verificar se é par ou ímpar,
#finally para exibir "Fim do programa".

def limpar_tela():
    print ("------------------------")

def verificar_par ():
    try:
         numero = int(input("Digite um número inteiro :"))
         if numero % 2 == 0:
            print(f" O numero {numero} é par.")
         else:
            print(f" O numero {numero} é impar.")
        
    except ValueError:

        print ("Você pecisa digitar um número inteiro válido!")
    
verificar_par()
limpar_tela()

# 9 - Crie uma função sacar(saldo, valor) que:
#Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
#Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.
    
def limpar_tela():
    
    class SaldoInsuficienteError(Exception):
        pass
    
    def sacar(saldo,valor):
        try:
            if valor <=0:
                raise ValueError( "O valor deve ser maior que o saldo")
    
    
    def sacar(saldo,valor):
        try:
            if valor <=0:
    raise
    
    if valor > saldo:
        return 
        
     
    

    
    
    
    
>>>>>>> dd73772 (Primeiro commit)
