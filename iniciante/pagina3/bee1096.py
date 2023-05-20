i = 1
j = 7

for t in range(15):
    print(f"I={i} J={j}")
    j -= 1
    if j < 5:
        i += 2
        j = 7
