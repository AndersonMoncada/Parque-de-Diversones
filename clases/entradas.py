class Entrada:
    def __init__(self, costo: float):
        self.costo=costo

    def calcular_total(self, grupo) -> None:
        total=len(grupo) * self.costo 
        print("Numero de entradas compradas: ",len(grupo))
        print("Total a pagar: ",total)