import time
from .Usuario import Persona


class JuegoElectronico:
    """
    Clase base para todos los juegos electrónicos del parque de diversiones.
    
    Maneja validaciones de acceso, gestión de capacidad, registro de jugadores
    y presentaciones interactivas con animaciones para juegos de arcade,
    VR y shooters.
    """

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
        Inicializa un juego electrónico con validación estricta de parámetros.
        
        Args:
            nombre (str): Nombre del juego electrónico.
            tipo (str): Categoría del juego ('VR', 'Arcade', 'Shooter FPS', etc.).
            capacidad (int): Número máximo de jugadores simultáneos.
            duracion (int): Duración de la sesión en minutos.
            edad_minima (int): Edad mínima requerida en años.
            estatura_minima (float): Estatura mínima en metros.
        
        Raises:
            ValueError: Si algún parámetro tiene valores inválidos (<=0 o negativos).
        """
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")
        if estatura_minima < 0:
            raise ValueError("La estatura mínima no puede ser negativa")
        if edad_minima < 0:
            raise ValueError("La edad mínima no puede ser negativa")

        self._nombre = nombre.strip()
        self._tipo = tipo.strip()
        self._capacidad = capacidad
        self._duracion = duracion
        self._edad_minima = edad_minima
        self._estatura_minima = estatura_minima
        self._visitantes: list[str] = []

    @property
    def nombre(self) -> str:
        """Nombre del juego electrónico."""
        return self._nombre

    @property
    def tipo(self) -> str:
        """Tipo/categoría del juego (VR, Arcade, Shooter, etc.)."""
        return self._tipo

    @property
    def capacidad(self) -> int:
        """Capacidad máxima de jugadores simultáneos."""
        return self._capacidad

    @property
    def duracion(self) -> int:
        """Duración de cada sesión en minutos."""
        return self._duracion

    @property
    def edad_minima(self) -> int:
        """Edad mínima requerida en años."""
        return self._edad_minima

    @property
    def estatura_minima(self) -> float:
        """Estatura mínima requerida en metros."""
        return self._estatura_minima

    def verificar_edad(self, persona: Persona) -> bool:
        """
        Verifica si la persona cumple el requisito de edad mínima.
        
        Args:
            persona (Persona): Instancia de Persona a validar.
            
        Returns:
            bool: True si cumple edad mínima, False si es inválida o insuficiente.
        """
        if persona.edad is None or persona.edad < 0:
            return False
        return persona.edad >= self._edad_minima

    def verificar_estatura(self, persona: Persona) -> bool:
        """
        Verifica si la persona cumple el requisito de estatura mínima.
        
        Args:
            persona (Persona): Instancia de Persona a validar.
            
        Returns:
            bool: True si cumple estatura mínima, False si es inválida o insuficiente.
        """
        if persona.estatura is None or persona.estatura <= 0:
            return False
        return persona.estatura >= self._estatura_minima

    def registrar_visitante(self, nombre_visitante: str) -> bool:
        """
        Registra un jugador si hay capacidad disponible y no está duplicado.
        
        Args:
            nombre_visitante (str): Nombre del jugador a registrar.
            
        Returns:
            bool: True si se registró exitosamente, False si no (duplicado, lleno, inválido).
        """
        if not nombre_visitante or not nombre_visitante.strip():
            return False
        nombre = nombre_visitante.strip()
        if nombre in self._visitantes:
            return False
        if len(self._visitantes) >= self._capacidad:
            return False
        self._visitantes.append(nombre)
        return True

    def espacios_disponibles(self) -> int:
        """
        Calcula el número de espacios libres para nuevos jugadores.
        
        Returns:
            int: Espacios restantes (capacidad - visitantes actuales).
        """
        return self._capacidad - len(self._visitantes)

    def mostrar_informacion(self) -> None:
        """
        Muestra información técnica del juego con animación de carga progresiva.
        
        Presenta nombre, tipo, capacidad, duración y requisitos de acceso.
        """
        print(f"\n{'='*30}")
        print(f" INFORMACIÓN DEL JUEGO")
        print(f"{'='*30}")

        print("Cargando información", end="")
        for _ in range(3):
            time.sleep(0.8)
            print(".", end="", flush=True)
        print(" Si\n")

        print(f"Nombre: {self._nombre}")
        time.sleep(0.6)
        print(f"Tipo: {self._tipo}")
        time.sleep(0.5)
        print(f"Capacidad: {self._capacidad} jugadores")
        time.sleep(0.6)
        print(f"Duración: {self._duracion} minutos")
        time.sleep(0.6)
        print(f"Edad mínima: {self._edad_minima} años")
        time.sleep(0.6)
        print(f"Estatura mínima: {self._estatura_minima} m")
        time.sleep(0.7)
        print(f"Visitantes actuales: {len(self._visitantes)}/{self._capacidad}")
        print(f"{'='*30}\n")

    def verificar_acceso_interactivo(
        self, persona: Persona, tiene_entrada: bool
    ) -> None:
        """
        Verifica acceso paso a paso con animaciones interactivas.
        
        Valida entrada, edad, estatura y capacidad, mostrando feedback visual.
        
        Args:
            persona (Persona): Jugador solicitando acceso.
            tiene_entrada (bool): Si posee entrada válida al parque.
        """
        print(f"\n{'─'*30}")
        print(f"VERIFICANDO ACCESO: {persona.nombre}")
        print(f"{'─'*30}")

        # Verificación de entrada
        print("Verificando entrada", end="")
        for _ in range(2):
            time.sleep(0.4)
            print(".", end="", flush=True)
        time.sleep(0.4)

        if not tiene_entrada:
            print("No")
            print(f"\n{persona.nombre}, no tienes entrada válida.")
            print(f"{'─'*30}\n")
            return
        print("Si")

        # Verificación de edad
        print(f"Verificando edad ({persona.edad} años)", end="")
        for _ in range(2):
            time.sleep(0.6)
            print(".", end="", flush=True)
        time.sleep(0.4)

        if not self.verificar_edad(persona):
            print("No")
            print(f"\n{persona.nombre}, edad insuficiente.")
            print(f"Necesitas al menos {self._edad_minima} años.")
            print(f"{'─'*30}\n")
            return
        print("Si")

        # Verificación de estatura
        print(f"Verificando estatura ({persona.estatura} m)", end="")
        for _ in range(2):
            time.sleep(0.5)
            print(".", end="", flush=True)
        time.sleep(0.8)

        if not self.verificar_estatura(persona):
            print("No")
            print(f"\n{persona.nombre}, estatura insuficiente.")
            print(f"Necesitas al menos {self._estatura_minima} m.")
            print(f"{'─'*30}\n")
            return
        print("Si")

        # Verificación de capacidad
        print("Verificando capacidad", end="")
        for _ in range(2):
            time.sleep(0.8)
            print(".", end="", flush=True)
        time.sleep(0.8)

        if self.espacios_disponibles() <= 0:
            print("No")
            print(f"\n{persona.nombre}, el juego está lleno.")
            print(f"Capacidad: {len(self._visitantes)}/{self._capacidad}")
            print(f"{'─'*30}\n")
            return
        print("Si")

        # Acceso aprobado
        print("\n" + "=" * 30)
        print("¡ACCESO PERMITIDO!")
        print("=" * 30)
        print(f"¡Bienvenido {persona.nombre} a {self._nombre}!")

        if self.registrar_visitante(persona.nombre):
            print(f"Registrado exitosamente")
            print(f"Espacios disponibles: {self.espacios_disponibles()}")

        print(f"{'─'*30}\n")

    def iniciar_juego_grupo(
        self, grupo: list[Persona], tienen_entrada: bool = True
    ) -> None:
        """
        Procesa acceso completo de un grupo de jugadores.
        
        Verifica cada miembro individualmente y muestra resumen estadístico.
        
        Args:
            grupo (list[Persona]): Lista de personas del grupo.
            tienen_entrada (bool): Si todo el grupo tiene entrada (default: True).
        """
        print(f"\n{'='*30}")
        print(f" BIENVENIDOS A: {self._nombre.upper()}")
        print(f"{'='*30}")
        print(f" Grupo de {len(grupo)} personas")
        time.sleep(1)

        for i, persona in enumerate(grupo, 1):
            print(f"\n[{i}/{len(grupo)}] Procesando...")
            time.sleep(1.3)
            self.verificar_acceso_interactivo(persona, tienen_entrada)
            time.sleep(1.2)

        print(f" RESUMEN DE ACCESOS")
        print(f" Personas que accedieron: {len(self._visitantes)}")
        print(f" Personas rechazadas: {len(grupo) - len(self._visitantes)}")
        print(f" Capacidad restante: {self.espacios_disponibles()}")
        print(f"{'='*30}\n")


class SimuladorVR(JuegoElectronico):
    """
    Simulador de Realidad Virtual inmersiva.
    
    Diseñado para experiencias grupales intensivas como simulaciones de terror,
    vuelo o aventuras extremas.
    """

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        """
        Inicializa un simulador VR con tipo predefinido.
        
        Args:
            nombre (str): Nombre específico del simulador.
            capacidad (int): Jugadores simultáneos (típicamente 1-4).
            duracion (int): Duración de la experiencia en minutos.
            edad_minima (int): Edad mínima (generalmente >12 años).
            estatura_minima (float): Estatura mínima para el equipo VR.
        """
        super().__init__(
            nombre,
            "Realidad Virtual",
            capacidad,
            duracion,
            edad_minima,
            estatura_minima,
        )


class JuegoArcade(JuegoElectronico):
    """
    Juego arcade clásico o moderno.
    
    Perfecto para competencias rápidas y multijugador casual.
    """

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        """
        Inicializa un juego arcade con tipo predefinido.
        
        Args:
            nombre (str): Nombre del juego arcade.
            capacidad (int): Jugadores simultáneos (1-2 típicamente).
            duracion (int): Duración de las partidas.
            edad_minima (int): Edad mínima requerida.
            estatura_minima (float): Estatura mínima para controles.
        """
        super().__init__(
            nombre, "Arcade", capacidad, duracion, edad_minima, estatura_minima
        )


class ShooterFPS(JuegoElectronico):
    """
    Juego de disparos en primera persona.
    
    Experiencias intensas individuales con contenido maduro.
    """

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        """
        Inicializa un shooter FPS con tipo predefinido.
        
        Args:
            nombre (str): Nombre del shooter FPS.
            capacidad (int): Generalmente 1 jugador por máquina.
            duracion (int): Duración de sesiones intensas.
            edad_minima (int): Edad mínima elevada por violencia.
            estatura_minima (float): Estatura para controles de precisión.
        """
        super().__init__(
            nombre, "Shooter FPS", capacidad, duracion, edad_minima, estatura_minima
        )
