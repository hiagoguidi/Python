import sympy as sp

x = sp.Symbol('x')  # Define a variável x

# Define a função a ser derivada
f = sp.sin(x**2) * sp.exp(2*x)

# Calcula a derivada da função usando todas as regras de derivação
dfdx = sp.diff(f, x)  # Derivada em relação a x
dfdx_product = sp.diff(sp.sin(x), x) * sp.exp(2*x) + sp.sin(x) * sp.diff(sp.exp(2*x), x)  # Regra do produto
dfdx_quotient = (sp.diff(x**2, x) * sp.exp(2*x) - sp.diff(2*x, x) * sp.sin(x**2)) / (x**2) ** 2  # Regra do quociente
dfdx_chain = sp.diff(sp.sin(x**2 + 1), x) * sp.diff(x**2 + 1, x)  # Regra da cadeia
dfdx_power = sp.diff(x**(3/2), x) * 3/2 * x**(1/2)  # Regra da potência
dfdx_log = sp.diff(sp.log(x), x)  # Regra do logaritmo
dfdx_exp = sp.diff(sp.exp(x), x)  # Regra da exponencial

# Imprime as derivadas da função usando todas as regras de derivação
print("Derivada de f(x):", dfdx)
print("Derivada de f(x) usando a regra do produto:", dfdx_product)
print("Derivada de f(x) usando a regra do quociente:", dfdx_quotient)
print("Derivada de f(x) usando a regra da cadeia:", dfdx_chain)
print("Derivada de f(x) usando a regra da potência:", dfdx_power)
print("Derivada de f(x) usando a regra do logaritmo:", dfdx_log)
print("Derivada de f(x) usando a regra da exponencial:", dfdx_exp)
