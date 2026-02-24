import time
from .Usuario import Persona


class JuegoElectronico:
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

    def verificar_edad(self, persona: Persona) -> bool:
        if persona.edad is None or persona.edad < 0:
            return False
        return persona.edad >= self._edad_minima

    def verificar_estatura(self, persona: Persona) -> bool:
        if persona.estatura is None or persona.estatura <= 0:
            return False
        return persona.estatura >= self._estatura_minima

    def registrar_visitante(self, nombre_visitante: str) -> bool:
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
        return self._capacidad - len(self._visitantes)

    def mostrar_informacion(self) -> None:
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
        print(f"\n{'─'*30}")
        print(f"VERIFICANDO ACCESO: {persona.nombre}")
        print(f"{'─'*30}")

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
    """Simulador de realidad virtual."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        super().__init__(
            nombre,
            "Realidad Virtual",
            capacidad,
            duracion,
            edad_minima,
            estatura_minima,
        )


class JuegoArcade(JuegoElectronico):
    """Juego arcade clásico o moderno."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        super().__init__(
            nombre, "Arcade", capacidad, duracion, edad_minima, estatura_minima
        )


class ShooterFPS(JuegoElectronico):
    """Juego shooter en primera persona."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        duracion: int,
        edad_minima: int,
        estatura_minima: float,
    ):
        super().__init__(
            nombre, "Shooter FPS", capacidad, duracion, edad_minima, estatura_minima
        )
