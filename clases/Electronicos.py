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
        precauciones: str,
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
            precauciones: Precauciones de seguridad
        """
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.duracion = duracion
        self.edad_minima = edad_minima
        self.estatura_minima = estatura_minima
        self.precauciones = precauciones

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
        print(f"Precauciones: {self.precauciones}")
