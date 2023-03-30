import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Solicitação de Empréstimo")

# Adicionando os widgets para coletar as informações do usuário
label_idade = tk.Label(janela, text="Qual a sua idade?")
entry_idade = tk.Entry(janela)

label_salario = tk.Label(janela, text="Qual o seu salário?")
entry_salario = tk.Entry(janela)

label_emprego = tk.Label(janela, text="Você está empregado ou desempregado?")
entry_emprego = tk.Entry(janela)

label_autonomo = tk.Label(janela, text="Você é autônomo ou CLT?")
entry_autonomo = tk.Entry(janela)

label_tempo_trabalho = tk.Label(janela, text="Há quanto tempo trabalha na atual empresa?")
entry_tempo_trabalho = tk.Entry(janela)

label_divida = tk.Label(janela, text="Você possui alguma dívida atrasada ou está negativado?")
entry_divida = tk.Entry(janela)

label_estado_civil = tk.Label(janela, text="Qual é o seu estado civil?")
entry_estado_civil = tk.Entry(janela)

label_idade.grid(row=0, column=0)
entry_idade.grid(row=0, column=1)
label_salario.grid(row=1, column=0)
entry_salario.grid(row=1, column=1)
label_emprego.grid(row=2, column=0)
entry_emprego.grid(row=2, column=1)
label_autonomo.grid(row=3, column=0)
entry_autonomo.grid(row=3, column=1)
label_tempo_trabalho.grid(row=4, column=0)
entry_tempo_trabalho.grid(row=4, column=1)
label_divida.grid(row=5, column=0)
entry_divida.grid(row=5, column=1)
label_estado_civil.grid(row=6, column=0)
entry_estado_civil.grid(row=6, column=1)

# Adicionando um botão para calcular o score
def calcular_score():
    # Obter as informações do usuário
    idade = int(entry_idade.get())
    salario = float(entry_salario.get())
    emprego = entry_emprego.get()
    autonomo = entry_autonomo.get()
    tempo_trabalho = int(entry_tempo_trabalho.get())
    divida = entry_divida.get()
    estado_civil = entry_estado_civil.get()

    # Calcular o score
    score_idade = 3 * (idade - 25)
    score_salario = 150 if salario > 5000 else 10
    score_empregado = -50 if emprego == "desempregado" else 0
    score_clt = 150 if autonomo == "CLT" else 0
    score_tempo_trabalho = 150 if tempo_trabalho > 2 else 0
    score_tem_divida = -400 if divida == "sim" else 0
    score_estado_civil = -50 if estado_civil == "solteiro" else 100 if estado_civil == "casado" else 0

    score_final = score_idade + score_salario + score_empregado + score_clt + score_tempo_trabalho + score_tem_divida + score_estado_civil

    if score_final < 200:
        resultado_label.config(text="Crédito reprovado")
    elif 200 <= score_final < 400:
        valor_emprestimo = salario * 0.7 * 12
        valor_parcela = valor_emprestimo / 12 * 1.06
        custo_juros = valor_emprestimo * 0.06
        juros_anual = custo_juros / valor_emprestimo * 100
        resultado_label.config(text=f"Crédito aprovado em 12 parcelas de 70% do salário, a 6% de juros ao mês\nValor total do empréstimo: R${valor_emprestimo:.2f}\nValor da parcela: R${valor_parcela:.2f}\nCusto dos juros: R${custo_juros:.2f}\nJuros anual: {juros_anual:.2f}%")
    elif score_final >= 500:
        valor_emprestimo = salario * 0.8 * 24
        valor_parcela = valor_emprestimo / 24 * 1.03
        custo_juros = valor_emprestimo * 0.03
        juros_anual = custo_juros / valor_emprestimo * 100
        resultado_label.config(text=f"Crédito aprovado em 24 parcelas de 80% do salário, a 3% de juros ao mês\nValor total do empréstimo: R${valor_emprestimo:.2f}\nValor da parcela: R${valor_parcela:.2f}\nCusto dos juros: R${custo_juros:.2f}\nJuros anual:{juros_anual:.2f}%")
    elif idade > 60:
        valor_emprestimo = salario * 0.8 * 6
