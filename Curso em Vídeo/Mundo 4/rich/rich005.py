# Mostra o erro de forma formatada
from rich.traceback import install
install()

def divisao(x, y):
    return x / y

print(divisao(50, 0))