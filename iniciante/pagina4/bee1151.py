def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]

        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)

        return sequence


num = int(input())

fib_sequence = fibonacci(num)

saida = " ".join(map(str, fib_sequence))
print(saida)
