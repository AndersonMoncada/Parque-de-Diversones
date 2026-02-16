class JuegosFisicos:
    def __init__ (self,nombre_juego:str,altura_juego:float,edad_minima:int,estatura_minima:float):
        self.nombre_juego=nombre_juego
        self.altura_juego=altura_juego
        self.edad_minima=edad_minima
        self.estatura_minima=estatura_minima
    def mostrarInfo (self):
        print("Nombre:",self.nombre_juego,"\n Altura del juego:",self.altura_juego,"\n Edad minima:",self.edad_minima,"\n Estatura minima:",self.estatura_minima)

tiroleza=JuegosFisicos("tiroleza",29.3,14,1.60)    
tiroleza.mostrarInfo()

