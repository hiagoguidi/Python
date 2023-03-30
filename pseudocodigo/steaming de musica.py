# Função de adição
def add(x, y):
   return x + y

# Função de subtração
def subtract(x, y):
   return x - y

# Função de multiplicação
def multiply(x, y):
   return x * y

# Função de divisão
def divide(x, y):
   return x / y

# Função de exponenciação
def exponentiation(x, y):
   return x ** y

# Função de raiz quadrada
def square_root(x):
   return x ** 0.5

# Função de fatorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

# Menu principal
print("Selecione a operação.")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponenciação")
print("6 - Raiz Quadrada")
print("7 - Fatorial")

# Pega a escolha do usuário
choice = input("Digite sua opção (1/2/3/4/5/6/7): ")

# Verifica se a escolha é válida
if choice in ('1', '2', '3', '4', '5', '6', '7'):

   # Pega os números do usuário
   if choice == '6' or choice == '7':
      num1 = int(input("Digite um número: "))
   else:
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))

   # Realiza a operação
   if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))

   elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

   elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

   elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

   elif choice == '5':
      print(num1, "^", num2, "=", exponentiation(num1, num2))

   elif choice == '6':
      print("Raiz Quadrada de", num1, "=", square_root(num1))

   elif choice == '7':
      print("Fatorial de", num1, "=", factorial(num1))

else:
   print("Opção Inválida")

