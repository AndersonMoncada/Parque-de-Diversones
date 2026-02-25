import time
from .Usuario import Persona


class Acuatico:
    """
    Clase base para todas las atracciones acuáticas del parque de diversiones.
    
    Maneja validaciones de acceso, registro de visitantes, capacidad limitada
    y presentaciones animadas interactivas.
    """

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
        Inicializa una atracción acuática con validación de parámetros.
        
        Args:
            nombre (str): Nombre de la atracción acuática.
            capacidad (int): Número máximo de personas simultáneas.
            profundidad (float): Profundidad del agua en metros.
            propulsion (str): Tipo de propulsión ('corriente', 'motor', etc.).
            estatura_minima (float): Estatura mínima requerida en metros.
            edad_minima (int): Edad mínima requerida en años.
        
        Raises:
            ValueError: Si capacidad <= 0, profundidad <= 0, o valores negativos.
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
        """Nombre de la atracción acuática."""
        return self._nombre

    @property
    def capacidad(self) -> int:
        """Capacidad máxima de personas simultáneas."""
        return self._capacidad

    @property
    def estatura_minima(self) -> float:
        """Estatura mínima requerida en metros."""
        return self._estatura_minima

    @property
    def edad_minima(self) -> int:
        """Edad mínima requerida en años."""
        return self._edad_minima

    @property
    def profundidad(self) -> float:
        """Profundidad del agua en metros."""
        return self._profundidad

    @property
    def propulsion(self) -> str:
        """Tipo de propulsión de la atracción."""
        return self._propulsion

    def verificar_estatura(self, persona: Persona) -> bool:
        """
        Verifica si la persona cumple el requisito de estatura mínima.
        
        Args:
            persona (Persona): Instancia de Persona a validar.
            
        Returns:
            bool: True si cumple estatura mínima, False otherwise.
        """
        if persona.estatura is None or persona.estatura <= 0:
            return False
        return persona.estatura >= self._estatura_minima

    def verificar_edad(self, persona: Persona) -> bool:
        """
        Verifica si la persona cumple el requisito de edad mínima.
        
        Args:
            persona (Persona): Instancia de Persona a validar.
            
        Returns:
            bool: True si cumple edad mínima, False otherwise.
        """
        if persona.edad is None or persona.edad < 0:
            return False
        return persona.edad >= self._edad_minima

    def puede_acceder(self, persona: Persona, tiene_entrada: bool) -> bool:
        """
        Verifica acceso completo (edad, estatura y entrada válida).
        
        Args:
            persona (Persona): Persona a validar.
            tiene_entrada (bool): Si posee entrada válida.
            
        Returns:
            bool: True si puede acceder completamente.
        """
        return (
            self.verificar_edad(persona)
            and self.verificar_estatura(persona)
            and tiene_entrada
        )

    def registrar_visitante(self, nombre_visitante: str) -> bool:
        """
        Registra un visitante si hay capacidad disponible.
        
        Args:
            nombre_visitante (str): Nombre de la persona a registrar.
            
        Returns:
            bool: True si se registró exitosamente, False si no.
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

    def listar_visitantes(self) -> list[str]:
        """
        Retorna la lista actual de visitantes registrados.
        
        Returns:
            list[str]: Copia de la lista de visitantes.
        """
        return list(self._visitantes)

    def espacios_disponibles(self) -> int:
        """
        Calcula espacios restantes disponibles.
        
        Returns:
            int: Número de espacios libres.
        """
        return self._capacidad - len(self._visitantes)

    def __str__(self) -> str:
        """
        Representación legible de la atracción para impresión.
        
        Returns:
            str: String formateado con nombre y requisitos básicos.
        """
        partes = [f"🌊 {self._nombre}"]
        partes.append(f"Capacidad: {self._capacidad}")
        partes.append(f"Edad mínima: {self._edad_minima} años")
        return " | ".join(partes)

    def mostrar_informacion(self) -> None:
        """
        Muestra información detallada con animación de carga progresiva.
        
        Presenta todos los datos técnicos de la atracción de forma visual.
        """
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
        Verifica acceso de forma interactiva con animaciones paso a paso.
        
        Args:
            persona (Persona): Persona solicitando acceso.
            tiene_entrada (bool): Si tiene entrada válida.
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
        Procesa acceso completo de un grupo con verificaciones individuales.
        
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


class RioLento(Acuatico):
    """
    Clase específica para la atracción Río Lento.
    
    Utiliza corriente natural como método de propulsión.
    """

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        profundidad: float,
        estatura_minima: float,
        edad_minima: int,
    ):
        """
        Inicializa Río Lento con propulsión por corriente natural.
        
        Args:
            nombre (str): Nombre específico del río lento.
            capacidad (int): Capacidad máxima de personas.
            profundidad (float): Profundidad del agua.
            estatura_minima (float): Estatura mínima requerida.
            edad_minima (int): Edad mínima requerida.
        """
        super().__init__(
            nombre,
            capacidad,
            profundidad,
            "Corriente natural",
            estatura_minima,
            edad_minima,
        )


class BotesChocones(Acuatico):
    """
    Clase específica para Botes Chocones.
    
    Utiliza motores eléctricos para propulsión.
    """

    def __init__(
        self,
        nombre: str,
        capacidad: int,
        profundidad: float,
        estatura_minima: float,
        edad_minima: int,
    ):
        """
        Inicializa Botes Chocones con propulsión eléctrica.
        
        Args:
            nombre (str): Nombre específico de los botes.
            capacidad (int): Capacidad máxima de personas.
            profundidad (float): Profundidad del agua.
            estatura_minima (float): Estatura mínima requerida.
            edad_minima (int): Edad mínima requerida.
        """
        super().__init__(
            nombre,
            capacidad,
            profundidad,
            "Motor eléctrico",
            estatura_minima,
            edad_minima,
        )
