import tkinter as tk

# Funções para cálculos
def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    label_result.config(text="Resultado: " + str(result))

def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    label_result.config(text="Resultado: " + str(result))

def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    label_result.config(text="Resultado: " + str(result))

def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 / num2
    label_result.config(text="Resultado: " + str(result))

def exponentiation():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 ** num2
    label_result.config(text="Resultado: " + str(result))

def square_root():
    num1 = float(entry_num1.get())
    result = num1 ** 0.5
    label_result.config(text="Resultado: " + str(result))

def factorial():
    num1 = int(entry_num1.get())
    result = 1
    for i in range(1,num1+1):
        result *= i
    label_result.config(text="Resultado: " + str(result))

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Widgets da janela principal
label_num1 = tk.Label(root, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

button_add = tk.Button(root, text="+", command=add)
button_add.pack()

button_subtract = tk.Button(root, text="-", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(root, text="*", command=multiply)
button_multiply.pack()

button_divide = tk.Button(root, text="/", command=divide)
button_divide.pack()

button_exponentiation = tk.Button(root, text="^", command=exponentiation)
button_exponentiation.pack()

button_square_root = tk.Button(root, text="Raiz Quadrada", command=square_root)
button_square_root.pack()

button_factorial = tk.Button(root, text="Fatorial", command=factorial)
button_factorial.pack()

label_result = tk.Label(root, text="Resultado:")
label_result.pack()

# Loop principal da janela
root.mainloop()
