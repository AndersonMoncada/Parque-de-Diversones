import time
import random
from .Usuario import Persona


class JuegosFisicos:
    """
    Clase base para todos los juegos físicos del parque de diversiones.
    
    Define las propiedades y métodos comunes para validar acceso
    y mostrar información de juegos físicos.
    """

    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
    ):
        """
        Inicializa un juego físico con sus requisitos básicos de acceso.
        
        Args:
            nombre_juego (str): Nombre del juego físico.
            altura_juego (float): Altura del juego en metros.
            edad_minima (int): Edad mínima requerida para participar.
            estatura_minima (float): Estatura mínima requerida en metros.
        """
        self._nombre_juego = nombre_juego
        self._altura_juego = altura_juego
        self._edad_minima = edad_minima
        self._estatura_minima = estatura_minima

    @property
    def nombre_juego(self) -> str:
        """Nombre del juego físico."""
        return self._nombre_juego

    @property
    def altura_juego(self) -> float:
        """Altura del juego en metros."""
        return self._altura_juego

    @property
    def edad_minima(self) -> int:
        """Edad mínima requerida para participar."""
        return self._edad_minima

    @property
    def estatura_minima(self) -> float:
        """Estatura mínima requerida en metros."""
        return self._estatura_minima

    def mostrar_info(self) -> None:
        """
        Muestra la información básica del juego físico en consola.
        
        Imprime nombre, altura, edad mínima y estatura mínima requerida.
        """
        print(
            "Nombre:", self.nombre_juego,
            "\n Altura del juego:", self.altura_juego,
            "\n Edad minima:", self.edad_minima,
            "\n Estatura minima:", self.estatura_minima,
        )

    def validar_condiciones_entrada(self, persona: Persona) -> bool:
        """
        Valida si una persona cumple los requisitos básicos del juego.
        
        Args:
            persona (Persona): Instancia de Persona a validar.
            
        Returns:
            bool: True si cumple requisitos de edad y estatura, False otherwise.
        """
        if (
            persona.edad >= self.edad_minima
            and persona.estatura >= self.estatura_minima
        ):
            return True
        else:
            return False


class Tirolesa(JuegosFisicos):
    """
    Clase para la atracción de tirolesa.
    
    Extiende JuegosFisicos con validación de peso máximo y simulación de recorrido.
    """

    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
        velocidad: float,
        peso_maximo: float,
    ):
        """
        Inicializa la tirolesa con todos sus requisitos de seguridad.
        
        Args:
            nombre_juego (str): Nombre de la tirolesa.
            altura_juego (float): Altura de la tirolesa en metros.
            edad_minima (int): Edad mínima requerida.
            estatura_minima (float): Estatura mínima en metros.
            velocidad (float): Velocidad máxima en km/h.
            peso_maximo (float): Peso máximo permitido en kg.
        """
        super().__init__(
            nombre_juego,
            altura_juego,
            edad_minima,
            estatura_minima,
        )
        self._velocidad = velocidad
        self._peso_maximo = peso_maximo

    @property
    def velocidad(self) -> float:
        """Velocidad máxima de la tirolesa en km/h."""
        return self._velocidad

    @property
    def peso_maximo(self) -> float:
        """Peso máximo permitido en kg."""
        return self._peso_maximo

    def mostrar_info(self) -> None:
        """
        Muestra información completa de la tirolesa incluyendo velocidad y peso máximo.
        """
        super().mostrar_info()
        print("Velocidad: ", self.velocidad, "km/h")
        print("Peso maximo: ", self.peso_maximo)

    def validar_condiciones_entrada(self, persona: Persona) -> bool:
        """
        Valida todas las condiciones específicas de la tirolesa.
        
        Args:
            persona (Persona): Persona a validar.
            
        Returns:
            bool: True si cumple todos los requisitos, False otherwise.
        """
        condiciones = super().validar_condiciones_entrada(persona)
        if not condiciones:
            return False
        if persona.peso <= self.peso_maximo:
            return True
        else:
            return False

    def entrar_tirolesa(self, grupo: list[Persona]) -> None:
        """
        Procesa la entrada de un grupo completo a la tirolesa.
        
        Valida cada persona y ejecuta el recorrido si es apta.
        
        Args:
            grupo (list[Persona]): Lista de personas del grupo.
        """
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print(persona.nombre, " Puedes entraaaar!! 😁")
                self.iniciar_recorrido(persona)
            else:
                print("Lo siento, ", persona.nombre, " no puedes entrar :(")
            print("=" * 40)

    def iniciar_recorrido(self, persona: Persona) -> None:
        """
        Simula el recorrido de tirolesa para una persona.
        
        Muestra animación de árboles pasando durante 4 segundos.
        
        Args:
            persona (Persona): Persona que realiza el recorrido.
        """
        print("Iniciando recorrido para ", persona.nombre)
        for i in range(0, 4):
            time.sleep(1)
            print("🌳")
        print("Recorrido terminado, ", persona.nombre)


class MuroEscalada(JuegosFisicos):
    """
    Clase para el muro de escalada.
    
    Incluye nivel de dificultad y simulación de escalada.
    """

    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
        dificultad: str,
    ):
        """
        Inicializa el muro de escalada con su nivel de dificultad.
        
        Args:
            nombre_juego (str): Nombre del muro.
            altura_juego (float): Altura del muro en metros.
            edad_minima (int): Edad mínima requerida.
            estatura_minima (float): Estatura mínima en metros.
            dificultad (str): Nivel de dificultad ('fácil', 'medio', 'difícil').
        """
        super().__init__(
            nombre_juego,
            altura_juego,
            edad_minima,
            estatura_minima,
        )
        self._dificultad = dificultad

    @property
    def dificultad(self) -> str:
        """Nivel de dificultad del muro de escalada."""
        return self._dificultad

    def mostrar_info(self) -> None:
        """
        Muestra información del muro incluyendo su dificultad.
        """
        super().mostrar_info()
        print("dificultad: ", self.dificultad)

    def entrar_muro(self, grupo: list[Persona]) -> None:
        """
        Procesa la entrada de un grupo al muro de escalada.
        
        Args:
            grupo (list[Persona]): Lista de personas del grupo.
        """
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entraaar ", persona.nombre, "😁")
                self.iniciar_escalada_muro(persona)
            else:
                print("Lo siento, no puedes entrar ", persona.nombre, " :c")
            print("=" * 40)

    def iniciar_escalada_muro(self, persona: Persona) -> None:
        """
        Simula la escalada del muro durante 4 segundos.
        
        Args:
            persona (Persona): Persona que escala el muro.
        """
        print("Iniciando turno para: ", persona.nombre)
        for i in range(0, 4):
            time.sleep(1)
            print("🧗🏼‍♂️")
        print("Turno terminado, ", persona.nombre)


class SaltoBungee(JuegosFisicos):
    """
    Clase para el salto en bungee.
    
    Simula cuenta regresiva y animación de salto.
    """

    def __init__(
        self,
        nombre_juego: str,
        altura_juego: float,
        edad_minima: int,
        estatura_minima: float,
    ):
        """
        Inicializa el salto en bungee con requisitos básicos.
        
        Args:
            nombre_juego (str): Nombre del salto bungee.
            altura_juego (float): Altura de salto en metros.
            edad_minima (int): Edad mínima requerida.
            estatura_minima (float): Estatura mínima en metros.
        """
        super().__init__(
            nombre_juego,
            altura_juego,
            edad_minima,
            estatura_minima,
        )

    def entrar_salto(self, grupo: list[Persona]) -> None:
        """
        Procesa la entrada de un grupo al salto bungee.
        
        Args:
            grupo (list[Persona]): Lista de personas del grupo.
        """
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes tirarte ", persona.nombre, "😁")
                self.iniciar_salto(persona)
            else:
                print("Lo siento, no puedes tirarte ", persona.nombre, " :c")
            print("=" * 40)

    def iniciar_salto(self, persona: Persona) -> None:
        """
        Simula el salto en bungee con cuenta regresiva.
        
        Incluye cuenta regresiva de 3 segundos y animación de caída.
        
        Args:
            persona (Persona): Persona que realiza el salto.
        """
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        print("Saltando: ", persona.nombre)

        for i in range(0, 4):
            time.sleep(1)
            print("🧍🏼‍♂️")

        print("Salto terminado, ", persona.nombre)


class TiroConArco(JuegosFisicos):
    """
    Clase para el tiro con arco.
    
    Simula 3 rondas de disparos con puntuación aleatoria.
    """

    def __init__(
        self,
        nombre_juego: str,
        edad_minima: int,
        estatura_minima: float,
    ):
        """
        Inicializa el tiro con arco (altura por defecto 0.0).
        
        Args:
            nombre_juego (str): Nombre del stand de tiro con arco.
            edad_minima (int): Edad mínima requerida.
            estatura_minima (float): Estatura mínima en metros.
        """
        super().__init__(
            nombre_juego,
            0.0,
            edad_minima,
            estatura_minima,
        )

    def entrar_tiro_arco(self, grupo: list[Persona]) -> None:
        """
        Procesa la entrada de un grupo al tiro con arco.
        
        Args:
            grupo (list[Persona]): Lista de personas del grupo.
        """
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entraaar", persona.nombre, "😁")
                self.iniciar_tiro_arco(persona)
            else:
                print("Lo siento, no puedes entrar ", persona.nombre)
            print("=" * 40)

    def iniciar_tiro_arco(self, persona: Persona) -> None:
        """
        Simula 3 rondas de tiro con arco con puntuación aleatoria.
        
        Cada ronda genera una puntuación de 0-10 puntos y muestra cuenta regresiva.
        
        Args:
            persona (Persona): Persona que realiza el tiro con arco.
        """
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
