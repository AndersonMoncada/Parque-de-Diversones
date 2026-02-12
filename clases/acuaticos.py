class Acuatico:
    def __init__(self, capacidad: int, profundidad: float, propulsion: str):
        self.capacidad = capacidad
        self.profundidad = profundidad
        self.propulsion = propulsion

    def imprimir_data(self):
        print(
            f"La capacidad de la atraccion acuatica es {self.capacidad} personas, su profundidad es {self.profundidad} metros, y su tipo de propulsion es : {self.propulsion}"
        )


Tobogan = Acuatico(20, 1.70, " Tobogan")
Tobogan.imprimir_data()

Piscina = Acuatico(50, 1.90, "Pasiva")
