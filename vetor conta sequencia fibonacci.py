n = 10  # define o número de elementos da sequência
fibonacci = [0, 1]  # cria um vetor com os dois primeiros elementos

# gera a sequência de Fibonacci e adiciona cada número ao vetor
for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

# imprime o vetor com a sequência de Fibonacci
print(fibonacci)
