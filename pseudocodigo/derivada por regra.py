import sympy as sp

x = sp.Symbol('x')  # Define a variável x

# Solicita ao usuário a função a ser derivada
f = sp.sympify(input("Digite a função a ser derivada: "))

# Solicita ao usuário a regra de derivação a ser utilizada
opcao = int(input("Escolha a regra de derivação:\n1 - Regra do produto\n2 - Regra do quociente\n3 - Regra da cadeia\n4 - Regra da potência\n5 - Regra do logaritmo\n6 - Regra da exponencial\n"))

# Aplica a regra de derivação escolhida pelo usuário
if opcao == 1:
    dfdx = sp.diff(f, x)  # Derivada em relação a x
    dfdx_product = sp.diff(sp.sin(x), x) * sp.exp(2*x) + sp.sin(x) * sp.diff(sp.exp(2*x), x)  # Regra do produto
    print("Derivada de f(x) usando a regra do produto:", dfdx_product)
elif opcao == 2:
    dfdx = sp.diff(f, x)  # Derivada em relação a x
    dfdx_quotient = (sp.diff(x**2, x) * sp.exp(2*x) - sp.diff(2*x, x) * sp.sin(x**2)) / (x**2) ** 2  # Regra do quociente
    print("Derivada de f(x) usando a regra do quociente:", dfdx_quotient)
elif opcao == 3:
    dfdx = sp.diff(f.subs(x, x**2 + 1), x) * sp.diff(x**2 + 1, x)  # Regra da cadeia
    print("Derivada de f(x) usando a regra da cadeia:", dfdx)
elif opcao == 4:
    dfdx = sp.diff(f, x)  # Derivada em relação a x
    dfdx_power = sp.diff(x**(3/2), x) * 3/2 * x**(1/2)  # Regra da potência
    print("Derivada de f(x) usando a regra da potência:", dfdx_power)
elif opcao == 5:
    dfdx = sp.diff(f, x)  # Derivada em relação a x
    dfdx_log = sp.diff(sp.log(x), x)  # Regra do logaritmo
    print("Derivada de f(x) usando a regra do logaritmo:", dfdx_log)
elif opcao == 6:
    dfdx = sp.diff(f, x)  # Derivada em relação a x
    dfdx_exp = sp.diff(sp.exp(x), x)  # Regra da exponencial
    print("Derivada de f(x) usando a regra da exponencial:", dfdx_exp)
else:
    print("Opção inválida")

