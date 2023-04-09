def fibonacci(n):
    # Casos base da recursão
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso geral da recursão
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def verifica_fibonacci(n):
    # Verifica se o número n está na sequência de Fibonacci
    i = 0
    while fibonacci(i) <= n:
        if fibonacci(i) == n:
            print(n, "pertence a sequencia de Fibonacci.")
            return
        i += 1
    print(n, "nao pertence a sequencia de Fibonacci.")

# Solicita que o usuário digite um número
n = int(input("Digite um numero: "))

verifica_fibonacci(n)
