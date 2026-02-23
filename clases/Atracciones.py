def __init__(
    self,
    capacidad: int,
    duracion: int,
    edad_minima: int,
    estatura_minima: float,
):

    if capacidad <= 0:
        raise ValueError("La capacidad debe ser mayor a 0")
    if duracion <= 0:
        raise ValueError("La duracion debe ser mayor a")
    if estatura_minima < 0 or edad_minima < 0:
        raise ValueError("Estatura y edad no pueden ser negativas")
    if edad_minima < 0:
        raise ValueError("La edad mínima no puede ser negativa")

    self._capacidad = capacidad
    self._duracion = duracion
    self._edad_minima = edad_minima
    self._estatura_minima = estatura_minima
    self._visitantes: list[str] = []

    @property
    def capacidad(self) -> int:
        """Retorna la capacidad máxima."""
        return self._capacidad

    @property
    def duracion(self) -> int:
        """Retorna la duración en minutos."""
        return self._duracion

    @property
    def edad_minima(self) -> int:
        """Retorna la edad mínima."""
        return self._edad_minima

    @property
    def estatura_minima(self) -> float:
        """Retorna la estatura mínima."""
        return self._estatura_minima
