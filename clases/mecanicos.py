class Mecanicas:
    def _init_(
        self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str
    ) -> None:
        self.nombre = nombre
        self.estatura_minima = estatura_minima
        self.edad_minima = edad_minima
        self.reglas = reglas
        self.precauciones = precauciones

    def validar_condiciones_entrada(self, persona) -> bool:
        if (
            persona.edad >= self.edad_minima
            and persona.estatura >= self.estatura_minima
        ):
            return True
        else:
            return False

    def verificar_entrada(self, compro_entrada: bool) -> bool:
        return compro_entrada

    def mostrar_informacion(self) -> None:
        print(f"\nAtracción: {self.nombre}")
        print(f"Estatura mínima: {self.estatura_minima} m")
        print(f"Reglas: {self.reglas}")
        print(f"Precauciones: {self.precauciones}")


class MontanaRusa(Mecanicas):
    def _init_(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, velocidad_maxima: float, inversiones: int):
        super()._init_(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.velocidad_maxima=velocidad_maxima
        self.inversiones=inversiones

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Velocidad maxima: ",self.velocidad_maxima,"km/h")
        print("Numero de inversiones: ",self.inversiones)

class RuedaDeLaFortuna(Mecanicas):
    def _init_(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, altura_maxima: float):
        super()._init_(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.altura_maxima=altura_maxima

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Altura maxima:",self.altura_maxima)


class BarcoPirata(Mecanicas):
    def _init_(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, capacidad: int):
        super()._init_(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.capacidad=capacidad

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Capacidad personas:",self.capacidad)



class TorreCaidaLibre(Mecanicas):
    def _init_(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, altura: float, velocidad_caida: float):
        super()._init_(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.altura=altura
        self.velocidad_caida=velocidad_caida

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print("Altura:",self.altura)
        print("Velocidad de caida:",self.velocidad_caida)


class CarrosChocones(Mecanicas):
    def _init_(self, nombre: str, estatura_minima: float, edad_minima: int, reglas: str, precauciones: str, numero_carros: int, duracion: float):
        super()._init_(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.numero_carros=numero_carros
        self.duracion=duracion
    def mostrar_informacion(self) -> None:
      super().mostrar_informacion()
      print("Numero de carritos: ",self.numero_carros)
      print("Duracion ronda: ",self.duracion)