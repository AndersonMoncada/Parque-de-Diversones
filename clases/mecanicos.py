class Mecanicas:
    nombre: str
    estatura_minima: float
    reglas: str
    precauciones: str

    def _init_(
        self, nombre: str, estatura_minima: float, reglas: str, precauciones: str
    ) -> None:
        self.nombre = nombre
        self.estatura_minima = estatura_minima
        self.reglas = reglas
        self.precauciones = precauciones

    def verificar_estatura(self, estatura_persona: float) -> bool:
        return estatura_persona >= self.estatura_minima

    def verificar_entrada(self, compro_entrada: bool) -> bool:
        return compro_entrada

    def mostrar_informacion(self) -> None:
        print(f"\nAtracción: {self.nombre}")
        print(f"Estatura mínima: {self.estatura_minima} m")
        print(f"Reglas: {self.reglas}")
        print(f"Precauciones: {self.precauciones}")


class MontanaRusa:

    def velocidad_maxima(self) -> str:
        return "Velocidad máxima: 120 km/h"

    def numero_inversiones(self) -> str:
        return "Tiene 3 inversiones (vueltas de cabeza)"


class RuedaDeLaFortuna:

    def altura_maxima(self) -> str:
        return "Altura máxima: 50 metros"

    def vista(self) -> str:
        return "Ofrece vista panorámica de todo el parque"


class BarcoPirata:

    def angulo_inclinacion(self) -> str:
        return "Ángulo máximo de inclinación: 75 grados"

    def capacidad(self) -> str:
        return "Capacidad: 40 personas por viaje"


class TorreCaidaLibre:

    def altura(self) -> str:
        return "Altura: 60 metros"

    def velocidad_caida(self) -> str:
        return "Velocidad de caída: 100 km/h"


class CarrosChocones:

    def numero_carros(self) -> str:
        return "Cuenta con 20 carros eléctricos"

    def duracion(self) -> str:
        return "Duración del juego: 5 minutos"
