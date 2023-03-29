# Definir os dados de entrada
idade = int(input("Qual a sua idade? "))
salario = float(input("Qual o seu salário? "))
emprego = input("Você está empregado ou desempregado? ")
autonomo = input("Você é autônomo ou CLT? ")
tempo_trabalho = int(input("Há quanto tempo trabalha na atual empresa? "))
divida = input("Você possui alguma dívida atrasada ou está negativado? ")
estado_civil = input("Qual é o seu estado civil? ")

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
