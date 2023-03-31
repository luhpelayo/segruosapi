class Operacion:
    def __init__(
        self, id=None, tipo=None, fecha=None,descripcion=None, ci=None
    ) -> None:
        self.id = id
        self.tipo = tipo
        self.fecha = fecha
        self.descripcion = descripcion
        self.ci = ci

    def to_JSON(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "ci": self.ci,            
        }
