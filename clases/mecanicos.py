import time
from Usuario import Persona
class Mecanicas:
    def __init__(
        self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str
    ) -> None:
        self.nombre = nombre
        self.estatura_minima = estatura_minima
        self.edad_minima = edad_minima
        self.reglas = reglas
        self.precauciones = precauciones

    def validar_condiciones_entrada(self, persona) -> bool:
        if (
            persona.edad >= self.edad_minima
            and persona.estatura >= self.estatura_minima
        ):
            return True
        else:
            return False

    def verificar_entrada(self, compro_entrada: bool) -> bool:
        return compro_entrada

    def mostrar_informacion(self) -> None:
        print(f"\nAtracción: {self.nombre}")
        print(f"Estatura mínima: {self.estatura_minima} m")
        print(f"Reglas: {self.reglas}")
        print(f"Precauciones: {self.precauciones}")


class MontanaRusa(Mecanicas):
    def __init__(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, velocidad_maxima: float, inversiones: int):
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.velocidad_maxima = velocidad_maxima
        self.inversiones = inversiones

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Velocidad maxima: ", self.velocidad_maxima, "km/h")
        print("Numero de inversiones: ", self.inversiones)
    
    def entrar_montana(self, grupo) -> None:
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar ", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar ", persona.nombre, " :c")
            print("=" * 40)
        if personas_abordo:
            self.iniciar_recorrido(personas_abordo)
        else:
            print("No hay personas que puedan subir")

    def iniciar_recorrido(self, lista_personas) -> None:
        print("Personas abordo: ")
        for persona in lista_personas:
            print(persona.nombre)
            time.sleep(1)
        print("Iniciando recorrido 🎢")
        for i in range(0,4):
            print("🎢")
            time.sleep(1)
        print("Recorrido finalizado")
        

class RuedaDeLaFortuna(Mecanicas):
    def __init__(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, altura_maxima: float):
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.altura_maxima = altura_maxima

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Altura maxima:", self.altura_maxima)

    def entrar_rueda(self, grupo) -> None:
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar", persona.nombre, ":c")
            print("=" * 40)
        if personas_abordo:
            self.iniciar_vuelta()
        else:
            print("No hay personas que puedan subir")

    def iniciar_vuelta(self) -> None:
        print("Iniciando vuelta 🎡")
        for i in range(0,4):
            print("🎡")
            time.sleep(1)
            print("⛅")
        print("Vuelta finalizada")


class BarcoPirata(Mecanicas):
    def __init__(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, capacidad: int):
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.capacidad = capacidad

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Capacidad personas:", self.capacidad)

    def entrar_barco(self, grupo) -> None:
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar", persona.nombre, ":c")
            print("=" * 40)
        if personas_abordo:
            self.iniciar_barco()
        else:
            print("No hay personas que puedan subir")

    def iniciar_barco(self) -> None:
        print("Iniciando juego ⚓")
        for i in range(0,5):
            print("🚢")
            time.sleep(1)
        print("Juego finalizado")


class CarrosChocones(Mecanicas):
    def __init__(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, numero_carros: int, duracion: float):
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.numero_carros = numero_carros
        self.duracion = duracion

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Numero de carritos: ", self.numero_carros)
        print("Duracion ronda: ", self.duracion)

    def entrar_carros(self, grupo) -> None:
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar", persona.nombre, ":c")
            print("=" * 40)
        if len(personas_abordo)>=2:
            self.iniciar_carros()
        else:
            print("No hay personas suficientes para iniciar el juego")

    def iniciar_carros(self) -> None:
        print("Iniciando juego 🏎")
        for i in range(0,5):
            print("🏎")
            time.sleep(1)
            print("💥")
        print("Juego finalizado")