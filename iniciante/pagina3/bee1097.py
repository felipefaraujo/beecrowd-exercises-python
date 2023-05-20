i = 1
j = 7

while i <= 9:
    print(f"I={i} J={j}")
    j -= 1
    if j - i < 4:
        i += 2
        j += 5
