class Carro:
    def __init__(self, fabricante, modelo, placa="SEM PLACA"):
        self.fabricante = fabricante
        self.modelo =  modelo
        self.placa = placa

    def Info(self):
        print(f"{self.fabricante} - {self.modelo} - {self.placa}")

    def Emplacamento(self, novaPlaca):
        self.placa = novaPlaca

    def Emplacamento(self):
        self.placa =input("Qual a nova placa do veículo: ")

if __name__ == '__main__':
    c1 = Carro(fabricante="Honda", modelo="Civic", placa="TYC0909")
    c1.Info()
    c1.Emplacamento("EUI9098")
    c1.Info()