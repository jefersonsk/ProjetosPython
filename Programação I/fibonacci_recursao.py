def fibonacci_recursivo(posicao:int) -> int:
    if posicao == 1:
        return 0
    elif posicao == 2:
        return 1
    else:
        return fibonacci_recursivo(posicao - 1) + fibonacci_recursivo(posicao -2)
    
print("Sequencia Fibonacci")
for x in range(1, 40):
    print(f"Posicao {x}: {fibonacci_recursivo(x)}")