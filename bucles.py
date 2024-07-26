for n in range(8):
    print (n)

for n in range(1,13):
    print (n)

for n in range(3,100, 3):
    print (n)

for count in range(10,0,-1):
    print (count)
print("¡Despegue!")

import turtle

# Configuración de la ventana
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Bandera de Colombia")

# Crear una tortuga
bandera = turtle.Turtle()
bandera.speed(2)
bandera.penup()

# Función para dibujar un rectángulo con un color de relleno
def dibujar_rectangulo(tortuga, ancho, alto, color):
    tortuga.begin_fill()
    tortuga.color(color)
    for _ in range(2):
        tortuga.forward(ancho)
        tortuga.left(90)
        tortuga.forward(alto)
        tortuga.left(90)
    tortuga.end_fill()

# Dimensiones de la bandera
ancho_bandera = 300
alto_bandera = 180

# Dibujar la franja amarilla (superior)
bandera.goto(-ancho_bandera/2, alto_bandera/2)
bandera.pendown()
dibujar_rectangulo(bandera, ancho_bandera, alto_bandera * 0.5, "yellow")

# Dibujar la franja azul (media)
bandera.penup()
bandera.goto(-ancho_bandera/2, alto_bandera/2 - alto_bandera * 0.5)
bandera.pendown()
dibujar_rectangulo(bandera, ancho_bandera, alto_bandera * 0.25, "blue")

# Dibujar la franja roja (inferior)
bandera.penup()
bandera.goto(-ancho_bandera/2, alto_bandera/2 - alto_bandera * 0.75)
bandera.pendown()
dibujar_rectangulo(bandera, ancho_bandera, alto_bandera * 0.25, "red")

# Finalizar
bandera.hideturtle()
wn.mainloop()
