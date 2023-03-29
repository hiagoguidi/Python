import math

def solve_quadratic(a, b, c):
    """
    Esta função resolve a equação do segundo grau ax^2 + bx + c = 0,
    retornando as raízes da equação, se houverem.
    """
    delta = b**2 - 4*a*c

    # Se o discriminante é negativo, não há raízes reais
    if delta < 0:
        return None, None

    # Se o discriminante é zero, há uma única raiz real
    elif delta == 0:
        x = -b / (2*a)
        return x, None

    # Se o discriminante é positivo, há duas raízes reais distintas
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

# Exemplo de uso
a = 2
b = -8
c = 6
x1, x2 = solve_quadratic(a, b, c)

if x1 and x2:
    print(f"As raízes da equação {a}x^2 + {b}x + {c} são {x1} e {x2}.")
elif x1:
    print(f"A única raiz da equação {a}x^2 + {b}x + {c} é {x1}.")
else:
    print(f"A equação {a}x^2 + {b}x + {c} não possui raízes reais.")
