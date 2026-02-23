import time

from Usuario import Persona


class JuegosFisicos:
    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
    ):
        self.nombre_juego = nombre_juego
        self.altura_juego = altura_juego
        self.edad_minima = edad_minima
        self.estatura_minima = estatura_minima

    def mostrarInfo(self) -> None:
        print(
            "Nombre:",
            self.nombre_juego,
            "\n Altura del juego:",
            self.altura_juego,
            "\n Edad minima:",
            self.edad_minima,
            "\n Estatura minima:",
            self.estatura_minima,
        )

    def validar_condiciones_entrada(self, persona) -> bool:
        if (
            persona.edad >= self.edad_minima
            and persona.estatura >= self.estatura_minima
        ):
            return True
        else:
            return False


class Tirolesa(JuegosFisicos):
    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
        velocidad: float,
        peso_maximo: float,
    ):
        super().__init__(
            nombre_juego,
            altura_juego,
            edad_minima,
            estatura_minima,
        )
        self.velocidad = velocidad
        self.peso_maximo = peso_maximo

    def mostrarInfo(self) -> None:
        super().mostrarInfo()
        print("Velocidad: ", self.velocidad, "km/h")
        print("Peso maximo: ", self.peso_maximo)

    def validar_condiciones_entrada(self, persona) -> bool:
        condiciones = super().validar_condiciones_entrada(persona)
        if not condiciones:
            return False
        if persona.peso <= self.peso_maximo:
            return True
        else:
            return False

    def entrar_tirolesa(self, grupo) -> None:
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print(persona.nombre, " Puedes entraaaar!! 😁")
                self.iniciar_recorrido(persona)
            else:
                print("Lo siento, ", persona.nombre, " no puedes entrar :(")
            print("=" * 40)

    def iniciar_recorrido(self, persona) -> None:
        print("Iniciando recorrido para ", persona.nombre)
        for i in range(0, 4):
            time.sleep(1)
            print("🌳")
        print("Recorrido terminado, ", persona.nombre)


class MuroEscalada(JuegosFisicos):
    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
        dificultad: str,
    ):
        super().__init__(
            nombre_juego,
            altura_juego,
            edad_minima,
            estatura_minima,
        )
        self.dificultad = dificultad

    def mostrarInfo(self) -> None:
        super().mostrarInfo()
        print("dificultad: ", self.dificultad)

    def entrar_muro(self, grupo) -> None:
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entraaar ", persona.nombre, "😁")
                self.iniciar_escalada_muro(persona)
            else:
                print("Lo siento, no puedes entrar ", persona.nombre, " :c")
            print("=" * 40)

    def iniciar_escalada_muro(self, persona) -> None:
        print("Iniciando turno para: ", persona.nombre)
        for i in range(0, 4):
            time.sleep(1)
            print("🧗🏼‍♂️")
        print("Turno terminado, ", persona.nombre)
