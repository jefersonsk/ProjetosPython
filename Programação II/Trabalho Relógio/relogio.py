class Relogio:
    def __init__(self, horas, minutos, segundos):
        self.total_segundos = horas * 3600 + minutos * 60 + segundos
        self.horas = self.total_segundos // 3600
        self.minutos = (self.total_segundos % 3600) // 60
        self.segundos = (self.total_segundos % 3600) % 60

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"

    def __repr__(self):
        return f"Classe Relogio (h={self.horas}, m={self.minutos}, s={self.segundos})"

    def __gt__(self, outra_hora):
        return self.total_segundos > outra_hora.total_segundos

    def __eq__(self, outra_hora):
        return self.total_segundos == outra_hora.total_segundos

    def __add__(self, outra_hora):
        total = self.total_segundos + outra_hora
        return Relogio(0, 0, total)

    def __sub__(self, outra_hora):
        total = self.total_segundos - outra_hora
        return Relogio(0, 0, total)

    def __int__(self):
        return self.total_segundos


r1 = Relogio(10, 30, 0)
r2 = Relogio(8, 45, 15)

print(r1)          # 10:30:00
print(repr(r1))    # Relogio(h=10, m=30, s=0)
print(r1 > r2)     # True
print(r1 == r2)    # False

r3 = r1 + 500      # soma 500 segundos
r4 = r1 - 120      # subtrai 120 segundos

print(r3)          # 10:38:20
print(r4)          # 10:28:00
print(int(r4))     # 37680 (segundos desde 00:00:00)
