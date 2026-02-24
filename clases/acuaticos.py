import time
from .Usuario import Persona


class Acuatico:
    """Representa una atracción acuática del parque."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        profundidad: float,
        propulsion: str,
        estatura_minima: float,
        edad_minima: int,
    ):
        """
        Inicializa una atracción acuática.

        Args:
            nombre: Nombre de la atracción
            capacidad: Número máximo de personas
            profundidad: Profundidad del agua en metros
            propulsion: Tipo de propulsión
            estatura_minima: Estatura mínima en metros
            edad_minima: Edad mínima requerida

        Raises:
            ValueError: Si algún parámetro no es válido
        """

        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        if profundidad <= 0:
            raise ValueError("La profundidad debe ser mayor a 0")
        if estatura_minima < 0:
            raise ValueError("La estatura mínima no puede ser negativa")
        if edad_minima < 0:
            raise ValueError("La edad mínima no puede ser negativa")

        self._nombre = nombre.strip()
        self._capacidad = capacidad
        self._profundidad = profundidad
        self._propulsion = propulsion.strip()
        self._estatura_minima = estatura_minima
        self._edad_minima = edad_minima
        self._visitantes: list[str] = []

    @property
    def nombre(self) -> str:
        """Retorna el nombre de la atracción."""
        return self._nombre

    @property
    def capacidad(self) -> int:
        """Retorna la capacidad máxima."""
        return self._capacidad

    @property
    def estatura_minima(self) -> float:
        """Retorna la estatura mínima."""
        return self._estatura_minima

    @property
    def edad_minima(self) -> int:
        """Retorna la edad mínima."""
        return self._edad_minima

    def verificar_estatura(self, persona: Persona) -> bool:
        """Verifica si la persona cumple con la estatura mínima."""
        if persona.estatura is None or persona.estatura <= 0:
            return False
        return persona.estatura >= self._estatura_minima

    def verificar_edad(self, persona: Persona) -> bool:
        """Verifica si la persona cumple con la edad mínima."""
        if persona.edad is None or persona.edad < 0:
            return False
        return persona.edad >= self._edad_minima

    def puede_acceder(self, persona: Persona, tiene_entrada: bool) -> bool:
        """
        Verifica si una persona puede acceder a la atracción.

        Args:
            persona: Objeto Persona a verificar
            tiene_entrada: Si tiene entrada válida

        Returns:
            True si cumple todos los requisitos
        """
        return (
            self.verificar_edad(persona)
            and self.verificar_estatura(persona)
            and tiene_entrada
        )

    def registrar_visitante(self, nombre_visitante: str) -> bool:
        """Registra un visitante en la atracción."""
        if not nombre_visitante or not nombre_visitante.strip():
            return False
        nombre = nombre_visitante.strip()
        if nombre in self._visitantes:
            return False
        if len(self._visitantes) >= self._capacidad:
            return False
        self._visitantes.append(nombre)
        return True

    def listar_visitantes(self) -> list[str]:
        """Retorna lista de visitantes registrados."""
        return list(self._visitantes)

    def espacios_disponibles(self) -> int:
        """Retorna espacios disponibles."""
        return self._capacidad - len(self._visitantes)

    def __str__(self) -> str:
        """Representación en texto de la atracción."""
        partes = [f"🌊 {self._nombre}"]
        partes.append(f"Capacidad: {self._capacidad}")
        partes.append(f"Edad mínima: {self._edad_minima} años")
        return " | ".join(partes)

    def mostrar_informacion(self) -> None:
        """Muestra información detallada de forma animada."""
        print(f"\n{'='*30}")
        print(f" INFORMACIÓN DE LA ATRACCIÓN")
        print(f"{'='*30}")

        print("Cargando información", end="")
        for _ in range(3):
            time.sleep(0.8)
            print(".", end="", flush=True)
        print(" Si\n")

        print(f"Nombre: {self._nombre}")
        time.sleep(0.6)
        print(f"Capacidad: {self._capacidad} personas")
        time.sleep(0.5)
        print(f"Profundidad: {self._profundidad} m")
        time.sleep(0.7)
        print(f"Propulsión: {self._propulsion}")
        time.sleep(0.6)
        print(f"Estatura mínima: {self._estatura_minima} m")
        time.sleep(0.6)
        print(f"Edad mínima: {self._edad_minima} años")
        time.sleep(0.7)
        print(f"Visitantes actuales: {len(self._visitantes)}/{self._capacidad}")
        print(f"{'='*30}\n")

    def verificar_acceso_interactivo(
        self, persona: Persona, tiene_entrada: bool
    ) -> None:
        """
        Verifica el acceso de forma interactiva y animada.

        Args:
            persona: Persona que quiere acceder
            tiene_entrada: Si tiene entrada
        """
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
            print(f"{'─'*20}\n")
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
            print(f" Necesitas al menos {self._edad_minima} años.")
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
            print(f"   Necesitas al menos {self._estatura_minima} m.")
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
            print(f"\n{persona.nombre}, la atracción está llena.")
            print(f"   Capacidad: {len(self._visitantes)}/{self._capacidad}")
            print(f"{'─'*60}\n")
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

    def iniciar_atraccion_grupo(
        self, grupo: list[Persona], tienen_entrada: bool = True
    ) -> None:
        """
        Procesa un grupo de personas para la atracción.

        Args:
            grupo: Lista de personas
            tienen_entrada: Si tienen entrada (por defecto True)
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


class RioLento(Acuatico):
    """Representa el juego acuático Río Lento."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        profundidad: float,
        estatura_minima: float,
        edad_minima: int,
    ):
        super().__init__(
            nombre,
            capacidad,
            profundidad,
            "Corriente natural",
            estatura_minima,
            edad_minima,
        )


class BotesChocones(Acuatico):
    """Representa el juego acuático Botes Chocones."""

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        profundidad: float,
        estatura_minima: float,
        edad_minima: int,
    ):
        super().__init__(
            nombre,
            capacidad,
            profundidad,
            "Motor eléctrico",
            estatura_minima,
            edad_minima,
        )
