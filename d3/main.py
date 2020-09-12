class Curso:
    def __init__(self, titulo, cupos):
        self.titulo = titulo
        self.participantes = 0
        self.cupos = cupos

    def agregarParticipante(self):
        if self.participantes < self.cupos:
            self.participantes += 1

    def display(self):
        print(f"{self.titulo} cupos: {self.cupos} participantes inscritos: {self.participantes}")


class Corolla:
    def __init__(self, galones, color):
        self.marca = "Toyota"
        self.cantidad_ruedas = 4
        self.cantidad_puertas = 4
        self.tipo_combustible = "gasolina"
        self.galones_combustible = galones
        self.color = color

    def encender(self):
        if self.galones_combustible > 0:
            print("El corolla enciende")

    def apagar(self):
        pass

    def acelerar(self):
        pass

    def frenar(self):
        pass


crojo = Corolla(5, "rojo")
cazul = Corolla(6, "Azul")

sql = Curso("Gestion de bases de datos sql", 20)
python = Curso("POO python", 30)

sql.display()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()
sql.agregarParticipante()
sql.display()
sql.cupos = 40
sql.display()


