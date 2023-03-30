import PySimpleGUI as sg

# Definir a janela
layout = [
    [sg.Text("Qual a sua idade?"), sg.InputText()],
    [sg.Text("Qual o seu salário?"), sg.InputText()],
    [sg.Text("Você está empregado ou desempregado?"), sg.InputText()],
    [sg.Text("Você é autônomo ou CLT?"), sg.InputText()],
    [sg.Text("Há quanto tempo trabalha na atual empresa?"), sg.InputText()],
    [sg.Text("Você possui alguma dívida atrasada ou está negativado?"), sg.InputText()],
    [sg.Text("Qual é o seu estado civil?"), sg.InputText()],
    [sg.Button("Calcular score")],
    [sg.Output(size=(60, 10))]
]

window = sg.Window("Análise de crédito", layout)

# Definir os dados de entrada
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    idade = int(values[0])
    salario = float(values[1])
    emprego = values[2]
    autonomo = values[3]
    tempo_trabalho = int(values[4])
    divida = values[5]
    estado_civil = values[6]

    # Calculando os scores
    score_idade = 3 * (idade - 25)
    score_salario = 150 if salario > 5000 else 10
    score_empregado = -50 if emprego == "desempregado" else 0
    score_clt = 150 if autonomo == "CLT" else 0
    score_tempo_trabalho = 150 if tempo_trabalho > 2 else 0
    score_tem_divida = -400 if divida == "sim" else 0
    score_estado_civil = -50 if estado_civil == "solteiro" else 100 if estado_civil == "casado" else 0

    # Calculando o score final
    score_final = score_idade + score_salario + score_empregado + score_clt + score_tempo_trabalho + score_tem_divida + score_estado_civil

    # Aplicando as políticas de crédito
    if score_final < 200:
        print("Crédito reprovado")
    elif 200 <= score_final < 400:
        valor_emprestimo = salario * 0.7 * 12
        valor_parcela = valor_emprestimo / 12 * 1.06
        custo_juros = valor_emprestimo * 0.06
        juros_anual = custo_juros / valor_emprestimo * 100
        print("Crédito aprovado em 12 parcelas de 70% do salário, a 6% de juros ao mês")
        print(f"Valor total do empréstimo: R${valor_emprestimo:.2f}")
        print(f"Valor da parcela: R${valor_parcela:.2f}")
        print(f"Custo dos juros: R${custo_juros:.2f}")
        print(f"Juros anual: {juros_anual:.2f}%")
    elif score_final >= 500:
       valor_emprestimo = salario * 0.8 * 24
       valor_parcela = valor_emprestimo / 24 * 1.03
       custo_juros = valor_emprestimo * 0.03
       juros_anual = custo_juros / valor_emprestimo * 100
       print("Crédito aprovado em 24 parcelas de 80% do salário, a 3% de juros ao mês")
       print(f"Valor total do empréstimo: R${valor_emprestimo:.2f}")
       print(f"Valor da parcela: R${valor_parcela:.2f}")
       print(f"Custo dos juros: R${custo_juros:.2f}")
       print(f"Juros anual: {juros_anual:.2f}%")
    elif idade > 60:
       valor_emprestimo = salario * 0.8 * 6