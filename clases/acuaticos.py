class Acuatico:
    def __init__(self, capacidad: int, profundidad: int, propulsion: str):
        self.capacidad = capacidad
        self.profundidad = profundidad
        self.propulsion = propulsion

    def imprimir_data(self):
        print(
            f"La capacidad de la atraccion acuatica es {self.capacidad}, su profundidad es {self.profundidad}, y su tipo de propulsion es : {self.propulsion}"
        )


Tobogan = Acuatico("20 Personas", "20 metros", " Tobogan")
Tobogan.imprimir_data()
