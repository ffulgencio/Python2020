#colecciones
nota1 = 90
nota2  = 80
nota3 = 70
nota4 = 85

# lista
nombres = []
nombres.append("Juan")
nombres.append("Mario")
nombres.append("Marcos")
nombres.append("Lucas")
print(nombres)
notas = [90, 80, 70, 85]
#        0    1   2   3

print(notas[2])
notas[2] = 75
print(notas[2])


notas.append(100)
print(notas)
notas.remove(100)
print(notas)

# i = 0
# while(i < len(nombres)):
#     print(nombres[i])
#     i = i + 1

for nombre in nombres:
    print(nombre)

for nota in notas:
    print(nota)



# tuplas
nombres_tupla = ('Jhon','Mary', 'Max')

for nombre in nombres_tupla:
    print(nombre)
#nombres_tupla.append('Mark')
print(nombres_tupla[1])



# diccionarios
# clave:valor

usuario = {
        'usuario':'ffulgencio', 
        'clave':'123456'
        }
print(usuario.keys())
print(usuario.values())
print(usuario['usuario'])