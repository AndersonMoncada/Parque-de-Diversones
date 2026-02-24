import time
import random
from Usuario import Persona


class JuegosFisicos:
    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
    ):
        self._nombre_juego = nombre_juego
        self._altura_juego = altura_juego
        self._edad_minima = edad_minima
        self._estatura_minima = estatura_minima

    @property
    def nombre_juego(self):
        return self._nombre_juego

    @property
    def altura_juego(self):
        return self._altura_juego

    @property
    def edad_minima(self):
        return self._edad_minima

    @property
    def estatura_minima(self):
        return self._estatura_minima

    def mostrar_info(self) -> None:
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
        self._velocidad = velocidad
        self._peso_maximo = peso_maximo

    @property
    def velocidad(self):
        return self._velocidad

    @property
    def peso_maximo(self):
        return self._peso_maximo

    def mostrar_info(self) -> None:
        super().mostrar_info()
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
        self._dificultad = dificultad

    @property
    def dificultad(self):
        return self._dificultad

    def mostrar_info(self) -> None:
        super().mostrar_info()
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


class SaltoBungee(JuegosFisicos):

    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
    ):
        super().__init__(
            nombre_juego,
            altura_juego,
            edad_minima,
            estatura_minima,
        )

    def entrar_salto(self, grupo) -> None:
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes tirarte ", persona.nombre, "😁")
                self.iniciar_salto(persona)
            else:
                print("Lo siento, no puedes tirarte ", persona.nombre, " :c")
            print("=" * 40)

    def iniciar_salto(self, persona) -> None:
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        print("Saltando: ", persona.nombre)

        for i in range(0, 4):
            time.sleep(1)
            print("🧍🏼‍♂️")

        print("Salto terminado, ", persona.nombre)


class TiroConArco(JuegosFisicos):

    def __init__(
        self,
        nombre_juego: str,
        edad_minima: int,
        estatura_minima: float,
    ):
        super().__init__(
            nombre_juego,
            0.0,
            edad_minima,
            estatura_minima,
        )

    def entrar_tiro_arco(self, grupo) -> None:
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entraaar", persona.nombre, "😁")
                self.iniciar_tiro_arco(persona)
            else:
                print("Lo siento, no puedes entrar ", persona.nombre)
            print("=" * 40)

    def iniciar_tiro_arco(self, persona) -> None:
        totalpuntos = 0

        for ronda in range(1, 4):
            puntuacion = random.randint(0, 10)

            print("Ronda: ", ronda)
            print("Disparando...🏹")

            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)

            print("Puntuación: ", puntuacion, " 🎯")
            totalpuntos += puntuacion

        print(persona.nombre, ", has obtenido ", totalpuntos, " puntos")
        print("Fin del turno para ", persona.nombre)