def canción (cancion_favorita):
    print("Me gusta mucho, " + cancion_favorita )

#Llamada a la función con un argumento name= input("Introduce tu canción favorita: "!) canción (canción favorita)
name= input("Escribe tu canc ion favorita: ") 
canción (name)

def area_triangulo(base, altura):
    area = (base * altura) / 2
    print("El área del triángulo es:", area)


# Solicitar datos al usuario
b = float (input("Introduce la base del triangulo: "))
h = float(input("Introduce la altura del triangulo: "))
area_triangulo(b, h)
