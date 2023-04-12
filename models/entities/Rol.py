class Rol:
    def __init__(self, id, nombre=None) -> None:
        self.id = id
        self.nombre = nombre

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
