n = 10  # define o número de linhas da matriz
m = 20  # define o número de colunas da matriz
matriz = []  # cria uma matriz vazia

# preenche a matriz com os números de 1 a n*m
for i in range(n):
    linha = []  # cria uma linha vazia
    for j in range(m):
        numero = i*m + j + 1
        linha.append(numero)
    matriz.append(linha)

# imprime a matriz
for linha in matriz:
    print(linha)
