class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
        self.participantes = 0
        self.cupos = 5

    def agregarParticipante(self):
        if self.participantes < self.cupos:
            self.participantes += 1
        else:
            print("No hay cupos")

    def display(self):
        print(f"{self.titulo} cupos: {self.cupos} participantes inscritos: {self.participantes} Quedan {self.cupos - self.participantes}")


class Carro:
    def __init__(self):
        self.marca = None
        self.cantidad_ruedas = None
        self.cantidad_puertas = None
        self.tipo_combustible = None
        self.galones_combustible = None
        self.color = None
        self.encendido = False

    def enciende(self):
        pass

    def apagar(self):
        pass

    def acelera(self):
        pass

    def frena(self):
        pass

class Persona:
    def __init__(self):
        self.nombre =""
        self.apellido =""
        self.cedula = ""
        self.telefono = ""
class Cliente(Persona):
    pass

class Empleado(Persona):
    def cobrar(self):
        pass

    def pasarInventario(self):
        pass

class Suplidor(Persona):
    pass

e1 = Empleado()
e1.cobrar()
e1.pasarInventario()

class Corolla(Carro):
    pass



class Civic(Carro):
    pass

crojo = Corolla()
cazul = Corolla()

sql = Curso("Gestion de bases de datos sql")


sql.display()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()

sql.display()
sql.cupos = 40
sql.display()


