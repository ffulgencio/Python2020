# pasos para trabajar con una db
# 1-  importar el modulo con el que trabajaremos
import sqlite3
# 2 - crear una connexion a la base de datos
conn = sqlite3.connect("mydb.db")
# 3 - crear una variable intermedia que nos permita enviar consultas
cursor = conn.cursor()

query1 = """
CREATE TABLE Estudiantes (nombre text, apellido text);
"""

query2 = """
INSERT INTO Estudiantes VALUES ('Maria','Martinez');
"""

query3 = """
SELECT nombre, apellido FROM Estudiantes;
"""
#cursor.execute(query2) #
cursor.execute(query3)
result = cursor.fetchall()
for res in result:
    print(res[0])


# 4-  validar los cambios
conn.commit()
# 5 - cerrar la connexion
conn.close()

