i = 0
j = 1

while i <= 2:
    for x in range(3):
        i = round(i, 1)
        j = round(j, 1)
        print(f"I={i:.1f} J={j:.1f}" if i % 1 > 0 else f"I={int(i)} J={int(j)}")
        j += 1
    i += 0.2
    j = 1 + i