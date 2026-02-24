class Acuatico:
    def __init__(
        self,
        nombre: str,
        capacidad: int,
        profundidad: float,
        propulsion: str,
        estatura_minima: float,
        edad_minima: int,
    ):
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        if profundidad <= 0:
            raise ValueError("La profundidad debe ser mayor a 0")
        if estatura_minima < 0 or edad_minima < 0:
            raise ValueError("Estatura y edad no pueden ser negativas")

        self._nombre = nombre.strip()
        self._capacidad = capacidad
        self._profundidad = profundidad
        self._propulsion = propulsion.strip()
        self._estatura_minima = estatura_minima
        self._edad_minima = edad_minima

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

    def verificar_estatura(self, estatura_persona: float) -> bool:
        if estatura_persona is None or estatura_persona <= 0:
            return False
        return estatura_persona >= self._estatura_minima

    def verificar_edad(self, edad_persona: int) -> bool:
        if edad_persona is None or edad_persona < 0:
            return False
        return edad_persona >= self._edad_minima

    def puede_acceder(self, edad: int, estatura: float, tiene_entrada: bool) -> bool:
        """Verifica todos los requisitos de acceso."""
        return (
            self.verificar_edad(edad)
            and self.verificar_estatura(estatura)
            and tiene_entrada
        )

    def registrar_visitante(self, nombre_visitante: str) -> bool:
        """Registra un visitante en la atracción."""
        if not nombre_visitante or not nombre_visitante.strip():
            return False
        nombre = nombre_visitante.strip()
        if nombre in self._visitantes:
            return False
        self._visitantes.append(nombre)
        return True

    def listar_visitantes(self) -> list[str]:
        """Retorna lista de visitantes registrados."""
        return list(self._visitantes)

    def __str__(self) -> str:
        partes = [f"Atracción: {self._nombre} ({self.__class__.__name__})"]
        partes.append(f"Capacidad: {self._capacidad}")
        partes.append(f"Edad mínima: {self._edad_minima} años")
        return " | ".join(partes)

    def mostrar_informacion(self) -> None:
        """Muestra información detallada."""
        print(f"\n{'='*50}")
        print(str(self))
        print(f"{'='*50}")
        print(f"Profundidad: {self._profundidad} m")
        print(f"Propulsión: {self._propulsion}")
        print(f"Estatura mínima: {self._estatura_minima} m")
