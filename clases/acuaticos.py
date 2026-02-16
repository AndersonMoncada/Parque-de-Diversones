class Acuatico:
    def __init__(
        self,
        nombre: str,
        capacidad: int,
        profundidad: float,
        propulsion: str,
        estatura_minima: float,
        edad_minima: int,
    ):
        self.nombrenombre = nombre
        self.capacidad = capacidad
        self.profundidad = profundidad
        self.propulsion = propulsion
        self.estatura_minima = estatura_minima
        self.edad_minima = edad_minima

    def imprimir_data(self):
        print(
            f"La capacidad de la atraccion acuatica es de {self.capacidad} personas, su profundidad es {self.profundidad} metros, y su tipo de propulsion es : {self.propulsion}"
        )

    def verificar_estatura(self, estatura_persona: float) -> bool:
        return estatura_persona >= self.estatura_minima

    def verificar_entrada(self, compro_entrada: bool) -> bool:
        return compro_entrada

    def mostrar_informacion(self) -> None:
        print(f"\nAtracción Acuática: {self.nombre}")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"Profundidad: {self.profundidad} metros")
        print(f"Tipo de propulsión: {self.propulsion}")
        print(f"Estatura mínima: {self.estatura_minima} m")
        print(f"Precauciones: {self.precauciones}")
        print(f"Edad minima es:{self.edad_minima}")


class Tobogan(Acuatico):
    def velocidad_descenso(self) -> str:
        return "La velocidad de descenso es 43km/h"

    def longitud_Tobogan(self) -> str:
        return "La longitud es de 90 metros"


class Piscina(Acuatico):

    def temperatura(self) -> str:
        return "Es de 25°C"

    def longitud(self) -> str:
        return "8.20 metros"


class RioLento(Acuatico):

    def longitud_recorrido(self) -> str:
        return "Longitud del recorrido: 300 metros"

    def velocidad_corriente(self) -> str:
        return "Velocidad de corriente 5 km/h ¿)"

    def tiempo_recorrido(self) -> str:
        return "Tiempo promedio del recorrido: 15 minutos"


if __name__ == "__main__":
    tobogan = Tobogan(
        nombre="Tobogán del Dragon",
        capacidad=2,
        profundidad=1.70,
        propulsion="Tobogán",
        estatura_minima=1.40,
        edad_minima=11,
    )
