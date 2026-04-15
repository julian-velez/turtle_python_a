# Importa todas las funciones de turtle (para dibujar)
from turtle import *

# Importa la función hsv_to_rgb para manejar colores dinámicos
from colorsys import *

# Acelera la animación (entre más alto, más rápido)
tracer(200)

# Fondo negro para resaltar los colores
bgcolor('black')

# Oculta la tortuga (cursor)
hideturtle()

# Grosor de la línea
pensize(3)


# Levanta el lápiz para mover la tortuga sin dibujar
penup()

# Mueve la tortuga hacia abajo para centrar mejor el diseño
goto(0, -190)  # puedes ajustar este valor

# Apunta hacia la derecha (0 grados)
setheading(0)

# Baja el lápiz para empezar a dibujar
pendown()


# Bucle principal que repite el patrón 400 veces
for i in range(400):

    # Cambia el color usando HSV → RGB
    # i/400 genera un degradado de colores (tipo arcoíris)
    color(hsv_to_rgb(i / 400, 1, 1))

    # Dibuja un arco grande (casi círculo)
    circle(180, 190)

    # Gira 60 grados a la derecha
    right(60)

    # Dibuja un arco más pequeño
    circle(80, 90)

    # Gira mucho a la izquierda (efecto espiral)
    left(340)

    # Avanza dependiendo del valor de i (crece poco a poco)
    forward(i * 0.5)

    # Dibuja otro arco pequeño
    circle(40, 60)

    # Regresa al punto anterior (mantiene el patrón centrado)
    backward(i * 0.5)


# Mantiene la ventana abierta al final
done()