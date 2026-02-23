class JuegosElectronicos:
    """Clase base para atracciones de juegos electrónicos."""

    def __init__(
        self,
        nombre: str,
        tipo: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        """
        Inicializa una atracción de juegos electrónicos.

        Args:
            nombre: Nombre de la atracción
            tipo: Tipo de juego (arcade, VR, shooter, etc.)
            capacidad: Número máximo de jugadores
            duracion: Duración del juego en minutos
            edad_minima: Edad mínima requerida
            estatura_minima: Estatura mínima en metros

        """
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.duracion = duracion
        self.edad_minima = edad_minima
        self.estatura_minima = estatura_minima

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @property
    def estatura_minima(self) -> float:
        return self._estatura_minima

    @property
    def edad_minima(self) -> int:
        return self._edad_minima

    def verificar_edad(self, edad_persona: int) -> bool:
        """Verifica si la persona cumple con la edad mínima."""
        return edad_persona >= self.edad_minima

    def verificar_estatura(self, estatura_persona: float) -> bool:
        """Verifica si la persona cumple con la estatura mínima."""
        return estatura_persona >= self.estatura_minima

    def verificar_entrada(self, compro_entrada: bool) -> bool:
        """Verifica si la persona compró entrada."""
        return compro_entrada

    def mostrar_informacion(self) -> None:
        """Muestra toda la información de la atracción."""
        print(f"\n{'='*50}")
        print(f"Atracción Electrónica: {self.nombre}")
        print(f"{'='*50}")
        print(f"Tipo: {self.tipo}")
        print(f"Capacidad: {self.capacidad} jugadores")
        print(f"Duración: {self.duracion} minutos")
        print(f"Edad mínima: {self.edad_minima} años")
        print(f"Estatura mínima: {self.estatura_minima} m")


class SimuladorVR(JuegosElectronicos):
    """Representa un simulador de realidad virtual."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        """Inicializa un simulador VR."""
        super().__init__(
            nombre,
            "Realidad Virtual",
            capacidad,
            duracion,
            edad_minima,
            estatura_minima,
        )

    def tipo_experiencia(self) -> str:
        """Retorna el tipo de experiencia VR."""
        return "Experiencia inmersiva 360° con sonido envolvente"

    def equipo_necesario(self) -> str:
        """Retorna el equipo necesario."""
        return "Visor VR Oculus Quest 2 y controladores"

    def nivel_intensidad(self) -> str:
        """Retorna el nivel de intensidad."""
        return "Alta intensidad - puede causar mareo"


class JuegoArcade(JuegosElectronicos):
    """Representa un juego arcade clásico o moderno."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        """Inicializa un juego arcade."""
        super().__init__(
            nombre,
            "Arcade",
            capacidad,
            duracion,
            edad_minima,
            estatura_minima,
        )

    def tipo_controles(self) -> str:
        """Retorna el tipo de controles."""
        return "Joystick clásico y botones táctiles"

    def dificultad(self) -> str:
        """Retorna el nivel de dificultad."""
        return "Dificultad: Media - Progresiva"

    def puntuacion_maxima(self) -> str:
        """Retorna información sobre la puntuación."""
        return "Puntuación máxima histórica: 999,999 puntos"


class ShooterFPS(JuegosElectronicos):
    """Representa un juego shooter en primera persona."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        """Inicializa un shooter FPS."""
        super().__init__(
            nombre,
            "Shooter FPS",
            capacidad,
            duracion,
            edad_minima,
            estatura_minima,
        )

    def tipo_armas(self) -> str:
        """Retorna los tipos de armas disponibles."""
        return "Pistola láser, rifle de asalto y escopeta"

    def modo_juego(self) -> str:
        """Retorna el modo de juego."""
        return "Modo: Supervivencia - Oleadas de enemigos"

    def clasificacion(self) -> str:
        """Retorna la clasificación del juego."""
        return "Clasificación: +15 años - Contenido de acción intensa"


if __name__ == "__main__":

    simulacion_zombies = SimuladorVR(
        nombre="Simulación Apocalipsis Zombie",
        capacidad=4,
        duracion=10,
        edad_minima=12,
        estatura_minima=1.30,
    )

    simulacion_zombies.mostrar_informacion()
    print(simulacion_zombies.tipo_experiencia())
    print(simulacion_zombies.equipo_necesario())
    print(simulacion_zombies.nivel_intensidad())

    doom = ShooterFPS(
        nombre="Doom Arcade",
        capacidad=1,
        duracion=15,
        edad_minima=15,
        estatura_minima=1.40,
    )

    doom.mostrar_informacion()
    print(doom.tipo_armas())
    print(doom.modo_juego())
    print(doom.clasificacion())

    tetris = JuegoArcade(
        nombre="Tetris Versus",
        capacidad=2,
        duracion=20,
        edad_minima=5,
        estatura_minima=1.20,
    )

    tetris.mostrar_informacion()
    print(tetris.tipo_controles())
    print(tetris.dificultad())
    print(tetris.puntuacion_maxima())

    print("\n" + "=" * 50)
    print("VERIFICACIÓN DE ACCESO")
    print("=" * 50)

    persona_edad = 14
    persona_estatura = 1.35
    compro_entrada = True

    print(f"\nVerificando acceso a {doom.nombre}:")
    print(f"Edad de la persona: {persona_edad} años")
    print(f"Estatura de la persona: {persona_estatura} m")
    print(f"¿Cumple edad mínima? {'Si' if doom.verificar_edad(persona_edad) else 'No'}")
    print(
        f"¿Cumple estatura mínima? {'Si' if doom.verificar_estatura(persona_estatura) else 'No'}"
    )
    print(
        f"¿Compró entrada? {' Si' if doom.verificar_entrada(compro_entrada) else 'No'}"
    )

    if (
        doom.verificar_edad(persona_edad)
        and doom.verificar_estatura(persona_estatura)
        and doom.verificar_entrada(compro_entrada)
    ):
        print("\n Acceso permitido!! Bienvenido al juego.")
    else:
        print("\n Acceso Denegado!! No cumple con los requisitos.")
