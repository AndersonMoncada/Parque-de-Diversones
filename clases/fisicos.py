class JuegosFisicos:
    def __init__ (self,nombre_juego:str,altura_juego:float,edad_minima:int,estatura_minima:float):
        self.nombre_juego=nombre_juego
        self.altura_juego=altura_juego
        self.edad_minima=edad_minima
        self.estatura_minima=estatura_minima

    def mostrarInfo (self) -> str:
        print("Nombre:",self.nombre_juego,"\n Altura del juego:",self.altura_juego,"\n Edad minima:",self.edad_minima,"\n Estatura minima:",self.estatura_minima)
    
    def validar_condiciones_entrada(self, edad: int, estatura: float) -> str:
        if edad >= self.edad_minima and estatura >= self.estatura_minima:
            return "Puedes entrar al juego"
        else:
            return "No puedes entrar al juego, lo siento"


tirolesa=JuegosFisicos("Tirolesa",29.3,14,1.60)
muro_escalar=JuegosFisicos("Muro para escalar",30, 12, 1.50)

muro_escalar.mostrarInfo()
mensaje=muro_escalar.validar_condiciones_entrada(15,1.40)

    

