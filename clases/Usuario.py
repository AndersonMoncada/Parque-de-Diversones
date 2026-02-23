class Persona:
    def __init__(self, nombre: str, edad: int, estatura: float, peso: float):
        self._nombre = nombre
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    @property
    def estatura(self) -> float:
        return self._estatura

    @property
    def peso(self) -> float:
        return self._peso
