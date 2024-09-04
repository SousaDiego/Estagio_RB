def fibonacci(limit):
    sequencia = [0, 1]
    while sequencia[-1] < limit:
        prox_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_valor)
    return sequencia

def check_fibonacci(n):
    sequencia = fibonacci(n)
    if n in sequencia:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))

resultado = check_fibonacci(numero)

print(resultado)
