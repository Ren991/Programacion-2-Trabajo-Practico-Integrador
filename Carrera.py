class Carrera():
    def __init__(self, nombre, cant_anios) -> None:
        self.__nombre: nombre
        self.__cant_anios: cant_anios
        

    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cant_anios(self):
        return self.__cant_anios
    
    def get_cantidad_materias(self) -> int:
        return None
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Cantidad de años : {self.cant_anios}"
    
    
        
        