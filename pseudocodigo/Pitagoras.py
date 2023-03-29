import math

def calcular_hipotenusa(cateto_a, cateto_b):
    """
    Esta função calcula a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras,
    onde cateto_a e cateto_b são os comprimentos dos catetos do triângulo.
    """
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa

# Exemplo de uso
cateto1 = 3
cateto2 = 4
hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print(f"Para um triângulo retângulo com catetos {cateto1} e {cateto2}, a hipotenusa é {hipotenusa:.2f}.")
