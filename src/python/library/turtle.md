---
title: '"turtle" --- Turtle graphics'
source_url: https://docs.python.org/es/3
source_path: library/turtle.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4320
---

# "turtle" --- Turtle graphics

**Código fuente:** Lib/turtle.py

======================================================================

## Introducción

Los gráficos de tortuga son una implementación de the popular
geometric drawing tools introduced in Logo, desarrollado por Wally
Feurzeig, Seymour Papert y Cynthia Solomon en 1967.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

## Empezar

Imagine una tortuga robótica que comienza en (0, 0) en el plano x-y.
Después de un "import turtle", dale el comando "turtle.forward(15)" y
se moverá (¡en la pantalla!) 15 píxeles en la dirección en la que está
mirando, dibujando una línea a medida que se mueve. Dale el comando
"turtle.right(25)" y rotará en su lugar 25 grados en el sentido de las
agujas del reloj.

##### Turtle star

Turtle puede dibujar figuras intrincadas usando programas que repiten
movimientos simples.

[imagen]

En Python, los gráficos de tortuga proporcionan una representación de
una "tortuga" física (un pequeño robot con un bolígrafo) que dibuja en
una hoja de papel en el suelo.

Es una forma eficaz y probada para que los estudiantes conozcan los
conceptos de programación y la interacción con el software, ya que
proporciona una retroalimentación instantánea y visible. También
proporciona un acceso cómodo a la salida gráfica en general.

El dibujo de tortugas se creó originalmente como una herramienta
educativa para que la utilizaran los profesores en el aula. Para el
programador que necesita producir algún resultado gráfico, puede ser
una forma de hacerlo sin la sobrecarga que supone introducir
bibliotecas externas o más complejas en su trabajo.

## Tutorial

Los nuevos usuarios deberían empezar aquí. En este tutorial,
exploraremos algunos de los conceptos básicos del dibujo de tortugas.

### Iniciando un entorno para tortugas

En un shell de Python, importe todos los objetos del módulo "turtle":

   from turtle import *

Si se encuentra con un error "No module named '_tkinter'", tendrá que
instalar "Tk interface package" en su sistema.

### Dibujo básico

Envía la tortuga hacia adelante 100 pasos:

   forward(100)

Deberías ver (probablemente en una nueva ventana de tu pantalla) una
línea dibujada por la tortuga, en dirección este. Cambia la dirección
de la tortuga para que gire 120 grados hacia la izquierda (en sentido
contrario a las agujas del reloj):

   left(120)

Continuemos dibujando un triángulo:

   forward(100)
   left(120)
   forward(100)

Observa cómo la tortuga, representada por una flecha, apunta en
diferentes direcciones a medida que la diriges.

Experimente con esos comandos y también con "backward()" y "right()".

#### Control del lápiz

Intente cambiar el color (por ejemplo, "color('blue')") y el ancho de
la línea (por ejemplo, "width(3)") y luego vuelva a dibujar.

También puedes mover la tortuga sin dibujar, levantando el lápiz:
"up()" antes de moverla. Para comenzar a dibujar nuevamente, usa
"down()".

#### La posición de la tortuga

Envía a tu tortuga de regreso a su punto de partida (útil si ha
desaparecido de la pantalla):

   home()

La posición inicial está en el centro de la pantalla de la tortuga. Si
alguna vez necesitas saberlas, obtén las coordenadas x-y de la tortuga
con:

   pos()

El hogar está en "(0, 0)".

Y después de un tiempo, probablemente ayudará a limpiar la ventana
para que podamos comenzar de nuevo:

   clearscreen()

### Creando patrones algorítmicos

Utilizando bucles, es posible construir patrones geométricos:

   for steps in range(100):
       for c in ('blue', 'red', 'green'):
           color(c)
           forward(steps)
           right(30)

- ¡que, por supuesto, están limitadas únicamente por la imaginación!

Dibujemos la forma de estrella en la parte superior de esta página.
Queremos líneas rojas, rellenas con amarillo:

   color('red')
   fillcolor('yellow')

Así como "up()" y "down()" determinan si se dibujarán líneas, el
relleno se puede activar y desactivar:

   begin_fill()

A continuación crearemos un bucle:

   while True:
       forward(200)
       left(170)
       if abs(pos()) < 1:
           break

"abs(pos()) < 1" es una buena manera de saber cuándo la tortuga ha
regresado a su posición original.

Por último, completa el relleno:

   end_fill()

(Tenga en cuenta que el llenado solo se realiza cuando se da el
comando "end_fill()").

## Cómo...

Esta sección cubre algunos casos de uso y enfoques típicos de las
tortugas.

### Empiece lo antes posible

Una de las ventajas de los gráficos de tortuga es la respuesta visual
inmediata que se obtiene con comandos simples: es una forma excelente
de introducir a los niños a las ideas de programación, con un mínimo
de gastos generales (no solo para los niños, por supuesto).

El módulo Turtle hace posible esto al exponer toda su funcionalidad
básica como funciones, disponibles con "from turtle import *". turtle
graphics tutorial cubre este enfoque.

Vale la pena señalar que muchos de los comandos de la tortuga también
tienen equivalentes aún más concisos, como "fd()" para "forward()".
Estos son especialmente útiles cuando se trabaja con estudiantes para
quienes escribir a máquina no es una habilidad.

   Necesitará tener instalado "Tk interface package" en su sistema
   para que funcionen los gráficos de Turtle. Tenga en cuenta que esto
   no siempre es sencillo, por lo que debe verificar esto con
   anticipación si planea usar gráficos de Turtle con un estudiante.

### Automatically begin and end filling

Starting with Python 3.14, you can use the "fill()" *context manager*
instead of "begin_fill()" and "end_fill()" to automatically begin and
end fill. Here is an example:

   with fill():
       for i in range(4):
           forward(100)
           right(90)

   forward(200)

The code above is equivalent to:

   begin_fill()
   for i in range(4):
       forward(100)
       right(90)
   end_fill()

   forward(200)

### Utilice el espacio de nombres del módulo "turtle"

Usar "from turtle import *" es conveniente, pero tenga cuidado, ya que
importa una colección bastante grande de objetos y, si está haciendo
otra cosa que no sean gráficos de tortuga, corre el riesgo de un
conflicto de nombres (esto se vuelve aún más problemático si está
usando gráficos de tortuga en un script donde se pueden importar otros
módulos).

La solución es utilizar "import turtle": "fd()" se convierte en
"turtle.fd()", "width()" se convierte en "turtle.width()" y así
sucesivamente. (Si escribir "tortuga" una y otra vez se vuelve
tedioso, utilice, por ejemplo, "import turtle as t" en su lugar).

### Utilice gráficos de tortugas en un guión

Se recomienda utilizar el espacio de nombres del módulo "turtle" como
se describe inmediatamente arriba, por ejemplo:

   import turtle as t
   from random import random

   for i in range(100):
       steps = int(random() * 100)
       angle = int(random() * 360)
       t.right(angle)
       t.fd(steps)

Sin embargo, también se requiere otro paso: tan pronto como finalice
el script, Python también cerrará la ventana de la tortuga. Agregar:

   t.mainloop()

hasta el final del script. El script ahora esperará a que lo cierren y
no saldrá hasta que lo hagan, por ejemplo, cerrando la ventana de
gráficos de la tortuga.

### Utilice gráficos de tortuga orientados a objetos

Ver también: Explanation of the object-oriented interface

Aparte de para propósitos introductorios muy básicos o para probar
cosas lo más rápido posible, es más habitual y mucho más potente
utilizar el enfoque orientado a objetos para los gráficos de tortugas.
Por ejemplo, esto permite tener varias tortugas en la pantalla a la
vez.

En este enfoque, los distintos comandos de la tortuga son métodos de
objetos (en su mayoría objetos "Turtle"). *can* utiliza el enfoque
orientado a objetos en el shell, pero sería más típico en un script de
Python.

El ejemplo anterior se convierte entonces en:

   from turtle import Turtle
   from random import random

   t = Turtle()
   for i in range(100):
       steps = int(random() * 100)
       angle = int(random() * 360)
       t.right(angle)
       t.fd(steps)

   t.screen.mainloop()

Tenga en cuenta la última línea. "t.screen" es una instancia de
"Screen" en la que existe una instancia de Turtle; se crea
automáticamente junto con la tortuga.

La pantalla de la tortuga se puede personalizar, por ejemplo:

   t.screen.title('Object-oriented turtle demo')
   t.screen.bgcolor("orange")

## Referencia gráficos de tortugas

Nota:

  En la siguiente documentación se proporciona la listas de argumentos
  para las funciones. Los métodos, por su puesto, tienen el argumento
  principal adicional *self* que se omite aquí.

### Métodos Turtle

Movimiento de Turtle
   Mover y dibujar
         "forward()" | "fd()"
         "backward()" | "bk()" | "back()"
         "right()" | "rt()"
         "left()" | "lt()"
         "goto()" | "setpos()" | "setposition()"
         "teleport()"
         "setx()"
         "sety()"
         "setheading()" | "seth()"
         "home()"
         "circle()"
         "dot()"
         "stamp()"
         "clearstamp()"
         "clearstamps()"
         "undo()"
         "speed()"

   Mostrar el estado de la tortuga
         "position()" | "pos()"
         "towards()"
         "xcor()"
         "ycor()"
         "heading()"
         "distance()"

   Ajuste y unidades de medida
         "degrees()"
         "radians()"

Control del lápiz
   Estado de dibujo
         "pendown()" | "pd()" | "down()"
         "penup()" | "pu()" | "up()"
         "pensize()" | "width()"
         "pen()"
         "isdown()"

   Control del color
         "color()"
         "pencolor()"
         "fillcolor()"

   Relleno
         "filling()"
         "fill()"
         "begin_fill()"
         "end_fill()"

   Más controles de dibujo
         "reset()"
         "clear()"
         "write()"

Estado de la Tortuga
   Visibilidad
         "showturtle()" | "st()"
         "hideturtle()" | "ht()"
         "isvisible()"

   Apariencia
         "shape()"
         "resizemode()"
         "shapesize()" | "turtlesize()"
         "shearfactor()"
         "tiltangle()"
         "tilt()"
         "shapetransform()"
         "get_shapepoly()"

Usando eventos
      "onclick()"
      "onrelease()"
      "ondrag()"

Métodos especiales de *Turtle*
      "poly()"
      "begin_poly()"
      "end_poly()"
      "get_poly()"
      "clone()"
      "getturtle()" | "getpen()"
      "getscreen()"
      "setundobuffer()"
      "undobufferentries()"

### Métodos de TurtleScreen/Screen

Control de ventana
      "bgcolor()"
      "bgpic()"
      "clearscreen()"
      "resetscreen()"
      "screensize()"
      "setworldcoordinates()"

Control de animación
      "no_animation()"
      "delay()"
      "tracer()"
      "update()"

Usando eventos de pantalla
      "listen()"
      "onkey()" | "onkeyrelease()"
      "onkeypress()"
      "onclick()" | "onscreenclick()"
      "ontimer()"
      "mainloop()" | "done()"

Configuración y métodos especiales
      "mode()"
      "colormode()"
      "getcanvas()"
      "getshapes()"
      "register_shape()" | "addshape()"
      "turtles()"
      "window_height()"
      "window_width()"

Métodos de entrada
      "textinput()"
      "numinput()"

Métodos específicos para *Screen*
      "bye()"
      "exitonclick()"
      "save()"
      "setup()"
      "title()"

## Métodos de *RawTurtle/Turtle* Y sus correspondientes funciones

Casi todos los ejemplos de esta sección se refieren a una instancia
Turtle llamada "turtle".

### Movimiento de Turtle

turtle.forward(distance)
turtle.fd(distance)

   Parámetros:
      **distance** -- un número (entero o flotante)

   Mover hacia adelante la tortuga la *ditance* especificada, en la
   dirección en la que la tortuga apunta.

      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.forward(25)
      >>> turtle.position()
      (25.00,0.00)
      >>> turtle.forward(-75)
      >>> turtle.position()
      (-50.00,0.00)

turtle.back(distance)
turtle.bk(distance)
turtle.backward(distance)

   Parámetros:
      **distance** -- un número

   Mover hacia atrás la tortuga la *distance* especificada, opuesta a
   la dirección en que la tortuga apunta. No cambia la dirección de la
   tortuga.

      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.backward(30)
      >>> turtle.position()
      (-30.00,0.00)

turtle.right(angle)
turtle.rt(angle)

   Parámetros:
      **angle** -- un número (entero o flotante)

   Gira la tortuga a la derecha tomando los *angle* como unidad de
   medida. (La unidad de medida por defecto son los grado, pero se
   puede configurar a través de las funciones "degrees()" y
   "radians()".) La orientación de los ángulos depende del modo en que
   está la tortuga, ver "mode()".

      >>> turtle.heading()
      22.0
      >>> turtle.right(45)
      >>> turtle.heading()
      337.0

turtle.left(angle)
turtle.lt(angle)

   Parámetros:
      **angle** -- un número (entero o flotante)

   Gira la tortuga a la izquierda tomando los *ángulos* como unidad de
   medida. (La unidad de medida por defecto son los grado, pero se
   puede configurar a través de las funciones "degrees()" y
   "radians()".) La orientación de los ángulos depende del modo en que
   está la tortuga, ver "mode()".

      >>> turtle.heading()
      22.0
      >>> turtle.left(45)
      >>> turtle.heading()
      67.0

turtle.goto(x, y=None)
turtle.setpos(x, y=None)
turtle.setposition(x, y=None)

   Parámetros:
      * **x** -- un número o un par/vector de números

      * **y** -- un número o "None"

   Si *y* es "None", *x* debe ser un par de coordenadas o un "Vec2D"
   (ejemplo: según lo devuelto por "pos()").

   Mueve la tortuga a una posición absoluta. Si el lápiz está bajo,
   traza una linea. No cambia la orientación de la tortuga.

      >>> tp = turtle.pos()
      >>> tp
      (0.00,0.00)
      >>> turtle.setpos(60,30)
      >>> turtle.pos()
      (60.00,30.00)
      >>> turtle.setpos((20,80))
      >>> turtle.pos()
      (20.00,80.00)
      >>> turtle.setpos(tp)
      >>> turtle.pos()
      (0.00,0.00)

turtle.teleport(x, y=None, *, fill_gap=False)

   Parámetros:
      * **x** -- un número o "None"

      * **y** -- un número o "None"

      * **fill_gap** -- un booleano

   Mueve la tortuga a una posición absoluta. A diferencia de goto(x,
   y), no se dibujará una línea. La orientación de la tortuga no
   cambia. Si se está llenando, el polígono o polígonos desde los que
   se teletransporta se llenarán después de salir y el llenado
   comenzará nuevamente después de teletransportarse. Esto se puede
   desactivar con fill_gap=True, que hace que la línea imaginaria
   recorrida durante el teletransporte actúe como una barrera de
   relleno como en goto(x, y).

      >>> tp = turtle.pos()
      >>> tp
      (0.00,0.00)
      >>> turtle.teleport(60)
      >>> turtle.pos()
      (60.00,0.00)
      >>> turtle.teleport(y=10)
      >>> turtle.pos()
      (60.00,10.00)
      >>> turtle.teleport(20, 30)
      >>> turtle.pos()
      (20.00,30.00)

   Added in version 3.12.

turtle.setx(x)

   Parámetros:
      **x** -- un número (entero o flotante)

   Establece la primera coordenada de la tortuga a *x*, deja la
   segunda coordenada sin cambios.

      >>> turtle.position()
      (0.00,240.00)
      >>> turtle.setx(10)
      >>> turtle.position()
      (10.00,240.00)

turtle.sety(y)

   Parámetros:
      **y** -- un número (entero o flotante)

   Establece la segunda coordenada de la tortuga a *y*, deja la
   primera coordenada sin cambios.

      >>> turtle.position()
      (0.00,40.00)
      >>> turtle.sety(-10)
      >>> turtle.position()
      (0.00,-10.00)

turtle.setheading(to_angle)
turtle.seth(to_angle)

   Parámetros:
      **to_angle** -- un número (entero o flotante)

   Establece la orientación de la tortuga a *to_angle*. Aquí hay
   algunas direcciones comunes en grados:

   +---------------------+----------------------+
   | modo estándar       | modo logo            |
   |=====================|======================|
   | 0 - este            | 0 - norte            |
   +---------------------+----------------------+
   | 90 - norte          | 90 - este            |
   +---------------------+----------------------+
   | 180 - oeste         | 180 - sur            |
   +---------------------+----------------------+
   | 270 - sur           | 270 - oeste          |
   +---------------------+----------------------+

      >>> turtle.setheading(90)
      >>> turtle.heading()
      90.0

turtle.home()

   Mueve la tortuga al origen -- coordenadas (0,0) -- y establece la
   orientación a la orientación original (que depende del modo, ver
   "mode()").

      >>> turtle.heading()
      90.0
      >>> turtle.position()
      (0.00,-10.00)
      >>> turtle.home()
      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.heading()
      0.0

turtle.circle(radius, extent=None, steps=None)

   Parámetros:
      * **radius** -- un número

      * **extent** -- un número (o "None")

      * **steps** -- un entero (o "None")

   Dibuja un círculo con el *radius* (radio) dado. El centro es
   *radius* unidades a la izquierda de la tortuga; *extent* -- un
   ángulo -- determina que parte del círculo se dibuja. Si no se pasa
   *extent*, dibuja el círculo entero. Si *extent* no es un círculo
   completo, un punto final del arco es la posición actual de lápiz.
   Dibuja el arco en dirección antihorario si *radius* es positivo, si
   no en dirección horaria. Finalmente la dirección de la tortuga es
   modificada por el aumento de *extent*.

   Como el círculo se aproxima a un polígono regular inscripto,
   *steps* determina el número de pasos a usar. Si no se da, será
   calculado automáticamente. Puede ser usado para dibujar polígonos
   regulares.

      >>> turtle.home()
      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.heading()
      0.0
      >>> turtle.circle(50)
      >>> turtle.position()
      (-0.00,0.00)
      >>> turtle.heading()
      0.0
      >>> turtle.circle(120, 180)  # draw a semicircle
      >>> turtle.position()
      (0.00,240.00)
      >>> turtle.heading()
      180.0

turtle.dot()
turtle.dot(size)
turtle.dot(color, /)
turtle.dot(size, color, /)
turtle.dot(size, r, g, b, /)

   Parámetros:
      * **size** -- un entero >= 1 (si se da)

      * **color** -- un *colorstring* o una tupla numérica de color

   Draw a circular dot with diameter *size*, using *color*.  If *size*
   is not given, the maximum of "pensize+4" and "2*pensize" is used.

      >>> turtle.home()
      >>> turtle.dot()
      >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
      >>> turtle.position()
      (100.00,-0.00)
      >>> turtle.heading()
      0.0

turtle.stamp()

   Estampa una copia de la forma de la tortuga en el lienzo en la
   posición actual. Devuelve un stamp_id por cada estampa, que puede
   ser usado para borrarlo al llamar "clearstamp(stamp_id)".

      >>> turtle.color("blue")
      >>> stamp_id = turtle.stamp()
      >>> turtle.fd(50)

turtle.clearstamp(stampid)

   Parámetros:
      **stampid** -- un entero, debe devolver el valor de la llamada
      previa de la función "stamp()" call

   Borra la estampa con el *stampid* dado.

      >>> turtle.position()
      (150.00,-0.00)
      >>> turtle.color("blue")
      >>> astamp = turtle.stamp()
      >>> turtle.fd(50)
      >>> turtle.position()
      (200.00,-0.00)
      >>> turtle.clearstamp(astamp)
      >>> turtle.position()
      (200.00,-0.00)

turtle.clearstamps(n=None)

   Parámetros:
      **n** -- un entero (o "None")

   Borra todas o las primeros/últimos *n* estampas de la tortuga. Si
   *n* es "None" , borra todas las estampas, Si *n* *> 0* borra la
   primera estampa *n*, sino y *n* *< 0* borra la última estampa *n*.

      >>> for i in range(8):
      ...     unused_stamp_id = turtle.stamp()
      ...     turtle.fd(30)
      >>> turtle.clearstamps(2)
      >>> turtle.clearstamps(-2)
      >>> turtle.clearstamps()

turtle.undo()

   Deshace (repetidamente) la(s) última(s) acción(es) de la tortuga.
   El número de acciones a deshacer es determinado por el tamaño del
   *undobuffer*.

      >>> for i in range(4):
      ...     turtle.fd(50); turtle.lt(80)
      ...
      >>> for i in range(8):
      ...     turtle.undo()

turtle.speed(speed=None)

   Parámetros:
      **speed** -- un entero en el rango 0..10 o un *speedstring* (ver
      abajo)

   Establecer la velocidad de la tortuga a un valor entero en el rango
   0..10. Si no se pasa ningún argumento, vuelve a la velocidad
   actual.

   Si el parámetro de entrada es un número mayor que 10 o menor que
   0.5, la velocidad se establece a 0. La frase acerca de la velocidad
   es mapeada a valores de velocidad de la siguiente manera:

   * "fastest":  0

   * "fast":  10

   * "normal":  6

   * "slow":  3

   * "slowest":  1

   Velocidades de 1 a 10 generan una animación cada vez más rápida al
   dibujar las líneas y en el giro de la tortuga.

   Atención: *speed* = 0 implica que *no* habrá ninguna animación. Los
   métodos *fordward/back* harán que la tortuga salte, de la misma
   manera que *left/right* hará que la tortuga gire instantáneamente.

      >>> turtle.speed()
      3
      >>> turtle.speed('normal')
      >>> turtle.speed()
      6
      >>> turtle.speed(9)
      >>> turtle.speed()
      9

### Mostrar el estado de la tortuga

turtle.position()
turtle.pos()

   Devuelve la posición actual de la tortuga (x,y) (como un vector
   "Vec2D")

      >>> turtle.pos()
      (440.00,-0.00)

turtle.towards(x, y=None)

   Parámetros:
      * **x** -- un número o par de vectores numéricos o una instancia
        de la tortuga

      * **y** -- un número si *x* es un número, si no "None"

   Retorna el ángulo entre la línea en la posición de la tortuga a la
   posición especificada en (x, y), el vector o la otra tortuga. Esto
   depende de la posición inicial de la tortuga, que depende del modo
   - "standard"/"world" o "logo".

      >>> turtle.goto(10, 10)
      >>> turtle.towards(0,0)
      225.0

turtle.xcor()

   Devuelve la coordinada *x* de la tortuga.

      >>> turtle.home()
      >>> turtle.left(50)
      >>> turtle.forward(100)
      >>> turtle.pos()
      (64.28,76.60)
      >>> print(round(turtle.xcor(), 5))
      64.27876

turtle.ycor()

   Devuelve la coordenada *y* de la tortuga.

      >>> turtle.home()
      >>> turtle.left(60)
      >>> turtle.forward(100)
      >>> print(turtle.pos())
      (50.00,86.60)
      >>> print(round(turtle.ycor(), 5))
      86.60254

turtle.heading()

   Devuelve la orientación actual de la tortuga (el valor depende del
   modo de la tortuga, ver "mode()").

      >>> turtle.home()
      >>> turtle.left(67)
      >>> turtle.heading()
      67.0

turtle.distance(x, y=None)

   Parámetros:
      * **x** -- un número o par de vectores numéricos o una instancia
        de la tortuga

      * **y** -- un número si *x* es un número, si no "None"

   Devuelve la distancia desde la tortuga al vector (x,y) dado, otra
   instancia de la tortuga, el valor es unidad pasos de tortuga.

      >>> turtle.home()
      >>> turtle.distance(30,40)
      50.0
      >>> turtle.distance((30,40))
      50.0
      >>> joe = Turtle()
      >>> joe.forward(77)
      >>> turtle.distance(joe)
      77.0

### Configuración de las medidas

turtle.degrees(fullcircle=360.0)

   Parámetros:
      **fullcircle** -- un número

   Establece la unidad de medida del ángulo, por ejemplo establece el
   número de "grados" para un círculo completo. El valor por defecto
   es 36 grados.

      >>> turtle.home()
      >>> turtle.left(90)
      >>> turtle.heading()
      90.0

      >>> # Change angle measurement unit to grad (also known as gon,
      >>> # grade, or gradian and equals 1/100-th of the right angle.)
      >>> turtle.degrees(400.0)
      >>> turtle.heading()
      100.0
      >>> turtle.degrees(360)
      >>> turtle.heading()
      90.0

turtle.radians()

   Establece la unidad de medida del ángulo a radianes. Equivalente a
   "degrees(2*math.pi)".

      >>> turtle.home()
      >>> turtle.left(90)
      >>> turtle.heading()
      90.0
      >>> turtle.radians()
      >>> turtle.heading()
      1.5707963267948966

### Control del lápiz

#### Estado de dibujo

turtle.pendown()
turtle.pd()
turtle.down()

   Baja el lápiz -- dibuja mientras se mueve.

turtle.penup()
turtle.pu()
turtle.up()

   Levanta el lápiz -- no dibuja mientras se mueve.

turtle.pensize(width=None)
turtle.width(width=None)

   Parámetros:
      **width** -- un número positivo

   Establece el grosos de la línea a *width* o lo devuelve. Si
   *resizemode* se establece a "auto" y turtleshape es un polígono,
   ese polígono es dibujado con el mismo grosor de línea. Si no se dan
   argumentos, devuelve el grosor del lápiz actual.

      >>> turtle.pensize()
      1
      >>> turtle.pensize(10)   # de aquí en adelante se dibujan líneas con ancho 10

turtle.pen(pen=None, **pendict)

   Parámetros:
      * **pen** -- un diccionario con algunos o todos las claves
        listadas debajo

      * **pendict** -- uno o más argumentos-palabras claves con las
        claves listadas debajo como palabras claves

   Devuelve o establece los atributos del lápiz en un "diccionario-
   lápiz" con el siguiente para de valores/claves:

   * "shown": True/False

   * "pendown": True/False

   * "pencolor": color-string or color-tuple

   * "fillcolor": color-string or color-tuple

   * "pensize": número positivo

   * "speed": número en el rango 0..10

   * "resizemode": "auto" or "user" or "noresize"

   * "stretchfactor": (número positivo, número positivo)

   * "outline": número positivo

   * "tilt": número

   Este diccionario puede usarse como argumento de una llamada
   subsecuente a la función "pen()" para restaurar el estado anterior
   del lápiz. Más aún, uno o más de estos atributos pueden darse como
   argumentos  claves. Esto puede usarse para establecer diferentes
   atributos del lápiz en una sola definición.

      >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
      >>> sorted(turtle.pen().items())
      [('fillcolor', 'black'), ('outline', 1), ('pencolor', 'red'),
       ('pendown', True), ('pensize', 10), ('resizemode', 'noresize'),
       ('shearfactor', 0.0), ('shown', True), ('speed', 9),
       ('stretchfactor', (1.0, 1.0)), ('tilt', 0.0)]
      >>> penstate=turtle.pen()
      >>> turtle.color("yellow", "")
      >>> turtle.penup()
      >>> sorted(turtle.pen().items())[:3]
      [('fillcolor', ''), ('outline', 1), ('pencolor', 'yellow')]
      >>> turtle.pen(penstate, fillcolor="green")
      >>> sorted(turtle.pen().items())[:3]
      [('fillcolor', 'green'), ('outline', 1), ('pencolor', 'red')]

turtle.isdown()

   Devuelve "True" si el lápiz está abajo, si está arriba "False".

      >>> turtle.penup()
      >>> turtle.isdown()
      False
      >>> turtle.pendown()
      >>> turtle.isdown()
      True

#### Control del color

turtle.pencolor()
turtle.pencolor(color, /)
turtle.pencolor(r, g, b, /)

   Devuelve o establece el color del lápiz.

   Se permiten cuatro formatos de entrada:

   "pencolor()"
      Return the current pencolor as color specification string or as
      a tuple (see example).  May be used as input to another
      color/pencolor/fillcolor/bgcolor call.

   "pencolor(colorstring)"
      Establece el color del lápiz a *colorstring*, que es una palabra
      que especifica un color *Tk*, tales como ""red"", ""yellow"", o
      ""#33cc8c"".

   "pencolor((r, g, b))"
      Establece el color del lápiz representado como una tupla de *r*,
      *g*, y *b*.  Cada valor *r*, *g*, y *b* debe ser un valor entero
      en el rango 0..colormode, donde colormode es 1.0 o 255 (ver
      "colormode()").

   "pencolor(r, g, b)"
      Establece el color del lápiz al color RGB representado por *r*,
      *g*, y *b*. Cada valor *r*, *g*, y *b* debe estar en el rango
      0..colormode.

   Si *turtleshape* es un polígono, la línea del polígono es dibujado
   con el muevo color de lápiz elegido.

      >>> colormode()
      1.0
      >>> turtle.pencolor()
      'red'
      >>> turtle.pencolor("brown")
      >>> turtle.pencolor()
      'brown'
      >>> tup = (0.2, 0.8, 0.55)
      >>> turtle.pencolor(tup)
      >>> turtle.pencolor()
      (0.2, 0.8, 0.5490196078431373)
      >>> colormode(255)
      >>> turtle.pencolor()
      (51.0, 204.0, 140.0)
      >>> turtle.pencolor('#32c18f')
      >>> turtle.pencolor()
      (50.0, 193.0, 143.0)

turtle.fillcolor()
turtle.fillcolor(color, /)
turtle.fillcolor(r, g, b, /)

   Return or set the fillcolor.

   Se permiten cuatro formatos de entrada:

   "fillcolor()"
      Return the current fillcolor as color specification string,
      possibly in tuple format (see example).  May be used as input to
      another color/pencolor/fillcolor/bgcolor call.

   "fillcolor(colorstring)"
      Establece *fillcolor* a *colorstring*, que es un color TK
      especificado como una palabra (en inglés), tales como *"red"*,
      *"yellow"*, o ""#33cc8c"".

   "fillcolor((r, g, b))"
      Establece *fillcolor* al color RGB representado por la tupla
      *r*, *g*, y *b*. Cada uno de los valores *r*, *g*, y *b* debe
      estar en el rango 0..colormode, donde *colormode* es 1.0 o 255
      (ver "colormode()").

   "fillcolor(r, g, b)"
      Establece *fillcolor* al color RGB representado por *r*, *g*, y
      *b*. Cada uno de los valores *r*, *g* y *b* debe ser un valor en
      el rango 0..colormode.

   Si *turtleshape* es un polígono, el interior de ese polígono es
   dibujado con el color establecido en *fillcolor*.

      >>> turtle.fillcolor("violet")
      >>> turtle.fillcolor()
      'violet'
      >>> turtle.pencolor()
      (50.0, 193.0, 143.0)
      >>> turtle.fillcolor((50, 193, 143))  # Integers, not floats
      >>> turtle.fillcolor()
      (50.0, 193.0, 143.0)
      >>> turtle.fillcolor('#ffffff')
      >>> turtle.fillcolor()
      (255.0, 255.0, 255.0)

turtle.color()
turtle.color(color, /)
turtle.color(r, g, b, /)
turtle.color(pencolor, fillcolor, /)

   Retorna o establece *pencolor* (el color del lápiz) y *fillcolor*
   (el color de relleno).

   Se permiten varios formatos de entrada. Usan de 0 a 3 argumentos
   como se muestra a continuación:

   "color()"
      Devuelve el valor actual de *pencolor* y el valor actual de
      *fillcolor* como un par de colores especificados como palabras o
      tuplas, como devuelven las funciones "pencolor()" y
      "fillcolor()".

   "color(colorstring)", "color((r,g,b))", "color(r,g,b)"
      Entradas como en  "pencolor()", establece al valor dado tanto,
      *fillcolor* como *pencolor*.

   "color(colorstring1, colorstring2)", "color((r1,g1,b1),
   (r2,g2,b2))"
      Equivalente a "pencolor(colorstring1)" y
      "fillcolor(colorstring2)" y análogamente si se usa el otro
      formato de entrada.

   Si *turtleshape* es un polígono, la línea y el interior de ese
   polígono e dibujado con los nuevos colores que se establecieron.

      >>> turtle.color("red", "green")
      >>> turtle.color()
      ('red', 'green')
      >>> color("#285078", "#a0c8f0")
      >>> color()
      ((40.0, 80.0, 120.0), (160.0, 200.0, 240.0))

Ver también: Método *Screeen* "colormode()".

#### Relleno

turtle.filling()

   Devuelve *fillstate* ("True" si está lleno, sino "False").

      >>> turtle.begin_fill()
      >>> if turtle.filling():
      ...    turtle.pensize(5)
      ... else:
      ...    turtle.pensize(3)

turtle.fill()

   Fill the shape drawn in the "with turtle.fill():" block.

      >>> turtle.color("black", "red")
      >>> with turtle.fill():
      ...     turtle.circle(80)

   Using "fill()" is equivalent to adding the "begin_fill()" before
   the fill-block and "end_fill()" after the fill-block:

      >>> turtle.color("black", "red")
      >>> turtle.begin_fill()
      >>> turtle.circle(80)
      >>> turtle.end_fill()

   Added in version 3.14.

turtle.begin_fill()

   Para ser llamada justo antes de dibujar una forma a rellenar.

turtle.end_fill()

   Rellena la forma dibujada después de última llamada a la función
   "begin_fill()".

   Superponer o no, regiones de polígonos auto-intersectados o
   múltiples formas, estas son rellenadas dependiendo de los gráficos
   del sistema operativo, tipo de superposición y número de
   superposiciones. Por ejemplo, la flecha de la tortuga de arriba,
   puede ser toda amarilla o tener algunas regiones blancas.

      >>> turtle.color("black", "red")
      >>> turtle.begin_fill()
      >>> turtle.circle(80)
      >>> turtle.end_fill()

#### Más controles de dibujo

turtle.reset()

   Borra el dibujo de la tortuga de la pantalla, centra la tortuga y
   establece las variables a los valores por defecto.

      >>> turtle.goto(0,-22)
      >>> turtle.left(100)
      >>> turtle.position()
      (0.00,-22.00)
      >>> turtle.heading()
      100.0
      >>> turtle.reset()
      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.heading()
      0.0

turtle.clear()

   Borra el dibujo de la tortuga de la pantalla. No mueve la tortuga.
   El estado y posición de la tortuga así como los todos los dibujos
   de las otras tortugas no son afectados.

turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))

   Parámetros:
      * **arg** -- objeto que se escribirá en *TurtleScreen*

      * **move** -- True/False

      * **align** -- una de las frases "*left*", "*center*" o
        "*right*"

      * **font** -- un trio (nombre de fuente, tamaño de fuente, tipo
        de fuente)

   Escribe texto - la representación de cadena de caracteres de *arg*
   - en la posición actual de la tortuga de acuerdo con *align*
   ("izquierda", "centro" o "derecha") y con la fuente dada. Si *mov*
   es verdadero, el lápiz se mueve a la esquina inferior derecha del
   texto. De forma predeterminada, *move* es "False".

   >>> turtle.write("Home = ", True, align="center")
   >>> turtle.write((0,0), True)

### Estado de la Tortuga

#### Visibilidad

turtle.hideturtle()
turtle.ht()

   Hace invisible a la tortuga, Es una buena idea hacer eso mientras
   está haciendo dibujos complejos, ya que esconder a la tortuga
   acelera dibujo de manera observable.

      >>> turtle.hideturtle()

turtle.showturtle()
turtle.st()

   Hace visible la tortuga.

      >>> turtle.showturtle()

turtle.isvisible()

   Devuelve "True" si la tortuga se muestra, "False" si está oculta.

   >>> turtle.hideturtle()
   >>> turtle.isvisible()
   False
   >>> turtle.showturtle()
   >>> turtle.isvisible()
   True

#### Apariencia

turtle.shape(name=None)

   Parámetros:
      **name** -- una cadena de caracteres que es un nombre de forma
      válido

   Establece la forma de la tortuga al *name* que se establece o, si
   no se establece un nombre, devuelve el nombre actual de su forma.
   La forma *name* debe existir en el diccionario de formas de
   *TurtleScreen*. Inicialmente están las siguientes formas
   poligonales: "*arrow*", "*turtle*", "*circle*", "*square*",
   "*triangle*", "*classic*". Para aprender como trabajar con estas
   formas ver los métodos de Screen "register_shape()".

      >>> turtle.shape()
      'classic'
      >>> turtle.shape("turtle")
      >>> turtle.shape()
      'turtle'

turtle.resizemode(rmode=None)

   Parámetros:
      **rmode** -- una de las cadenas "*auto*", "*user*", "*noresize*"

   Establece *resizemode* a alguno de los valores: "*auto*", "*user*",
   "*noresize*". Si *mode* no se aporta, devuelve el actual
   *resizemode*. Distintos *resizemode* tienen los siguientes efectos:

   * "*auto*": adapta la apariencia de la tortuga al correspondiente
     valor del lápiz.

   * "*user*": adapta la apariencia de la tortuga de acuerdo a los
     valores de *sretchfactor* y *outlinewidth* (contorno), que se
     establece con la función "shapesize()".

   * "*noresize*": no se adapta la apariencia de la tortuga.

   "resizemode("user")" es llamado por la función "shapesize()" cuando
   se usa con argumentos.

      >>> turtle.resizemode()
      'noresize'
      >>> turtle.resizemode("auto")
      >>> turtle.resizemode()
      'auto'

turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
turtle.turtlesize(stretch_wid=None, stretch_len=None, outline=None)

   Parámetros:
      * **stretch_wid** -- número positivo

      * **stretch_len** -- número positivo

      * **outline** -- número positivo

   Devuelve o establece los atributos x/y-stretchfactors y/o outline
   del lápiz. Establece resizemode en "user". Si y solo si resizemode
   está establecido en "user", la tortuga se mostrará estirada de
   acuerdo con sus factores de estiramiento: *stretch_wid* es el
   factor de estiramiento perpendicular a su orientación,
   *stretch_len* es el factor de estiramiento en la dirección de su
   orientación, *outline* determina el ancho del contorno de la forma.

      >>> turtle.shapesize()
      (1.0, 1.0, 1)
      >>> turtle.resizemode("user")
      >>> turtle.shapesize(5, 5, 12)
      >>> turtle.shapesize()
      (5, 5, 12)
      >>> turtle.shapesize(outline=8)
      >>> turtle.shapesize()
      (5, 5, 8)

turtle.shearfactor(shear=None)

   Parámetros:
      **shear** -- número (opcional)

   Establece o devuelve el valor actual del estiramiento. Estira la
   forma de la tortuga de acuerdo a la inclinación del factor de
   corte, que es la tangente del ángulo de corte. No cambia el rumbo
   de la tortuga (dirección del movimiento). Si no de da un valor de
   inclinación: devuelve el factor actual, por ejemplo la tangente del
   ángulo de inclinación, por el cual se cortan la líneas paralelas al
   rumbo de la tortuga.

      >>> turtle.shape("circle")
      >>> turtle.shapesize(5,2)
      >>> turtle.shearfactor(0.5)
      >>> turtle.shearfactor()
      0.5

turtle.tilt(angle)

   Parámetros:
      **angle** -- un número

   Rota la forma de la tortuga en *ángulo* desde su ángulo de
   inclinación actual, pero no cambia el rumbo de la tortuga
   (dirección del movimiento).

      >>> turtle.reset()
      >>> turtle.shape("circle")
      >>> turtle.shapesize(5,2)
      >>> turtle.tilt(30)
      >>> turtle.fd(50)
      >>> turtle.tilt(30)
      >>> turtle.fd(50)

turtle.tiltangle(angle=None)

   Parámetros:
      **angle** -- un número (opcional)

   Establece o devuelve el ángulo de inclinación actual. Si se otorga
   un ángulo, rota la forma de la tortuga para apuntar en la dirección
   del ángulo especificado, independientemente de su actual ángulo de
   inclinación. No cambia el rumbo de la tortuga (dirección del
   movimiento). Si no se da el ángulo: devuelve el ángulo de
   inclinación actual, por ejemplo: el ángulo entre la orientación de
   la forma de la tortuga y el rumbo de la tortuga (su dirección de
   movimiento).

      >>> turtle.reset()
      >>> turtle.shape("circle")
      >>> turtle.shapesize(5,2)
      >>> turtle.tilt(45)
      >>> turtle.tiltangle()
      45.0

turtle.shapetransform(t11=None, t12=None, t21=None, t22=None)

   Parámetros:
      * **t11** -- un número (opcional)

      * **t12** -- un número (opcional)

      * **t21** -- un número (opcional)

      * **t12** -- un número (opcional)

   Establece o devuelve la matriz de transformación actual de la forma
   de la tortuga.

   Si no se proporciona ninguno de los elementos de la matriz, retorna
   la matriz de transformación como una tupla de 4 elementos. De lo
   contrario, establezca los elementos dados y transforme la forma de
   tortuga de acuerdo con la matriz que consta de la primera fila t11,
   t12 y la segunda fila t21, t22. El determinante t11 * t22 - t12 *
   t21 no debe ser cero, de lo contrario se genera un error. Modifique
   el factor de estiramiento, el factor de corte y el ángulo de
   inclinación de acuerdo con la matriz dada.

      >>> turtle = Turtle()
      >>> turtle.shape("square")
      >>> turtle.shapesize(4,2)
      >>> turtle.shearfactor(-0.5)
      >>> turtle.shapetransform()
      (4.0, -1.0, -0.0, 2.0)

turtle.get_shapepoly()

   Devuelve el polígono de la forma actual como tupla de pares de
   coordenadas. Esto puede ser usado para definir una nueva forma o
   componentes de una forma compuesta.

      >>> turtle.shape("square")
      >>> turtle.shapetransform(4, -1, 0, 2)
      >>> turtle.get_shapepoly()
      ((50, -20), (30, 20), (-50, 20), (-30, -20))

### Usando eventos

turtle.onclick(fun, btn=1, add=None)

   Parámetros:
      * **fun** -- una función con dos argumentos que se invocará con
        las coordenadas del punto en el que se hizo clic en el lienzo

      * **btn** -- número del botón del mouse, el valor predeterminado
        es 1 (botón izquierdo del mouse)

      * **add** -- "True" o "False" -- si es "True", se agrega un
        nuevo enlace, de lo contrario reemplazará el enlace anterior

   Enlaza *acciones divertidas* a eventos de click en la tortuga. Si
   la *accion* es "None", las acciones asociadas son borradas. Ejemplo
   para la tortuga anónima, en la forma procedimental:

      >>> def turn(x, y):
      ...     left(180)
      ...
      >>> onclick(turn)  # Now clicking into the turtle will turn it.
      >>> onclick(None)  # event-binding will be removed

turtle.onrelease(fun, btn=1, add=None)

   Parámetros:
      * **fun** -- una función con dos argumentos que se invocará con
        las coordenadas del punto en el que se hizo clic en el lienzo

      * **btn** -- número del botón del mouse, el valor predeterminado
        es 1 (botón izquierdo del mouse)

      * **add** -- "True" o "False" -- si es "True", se agrega un
        nuevo enlace, de lo contrario reemplazará el enlace anterior

   Enlaza *acciones divertidas* a eventos del tipo soltar botón del
   mouse en la tortuga. SI la *acción* es "None", las acciones
   asociadas son borradas.

      >>> class MyTurtle(Turtle):
      ...     def glow(self,x,y):
      ...         self.fillcolor("red")
      ...     def unglow(self,x,y):
      ...         self.fillcolor("")
      ...
      >>> turtle = MyTurtle()
      >>> turtle.onclick(turtle.glow)     # clicking on turtle turns fillcolor red,
      >>> turtle.onrelease(turtle.unglow) # releasing turns it to transparent.

turtle.ondrag(fun, btn=1, add=None)

   Parámetros:
      * **fun** -- una función con dos argumentos que se invocará con
        las coordenadas del punto en el que se hizo clic en el lienzo

      * **btn** -- número del botón del mouse, el valor predeterminado
        es 1 (botón izquierdo del mouse)

      * **add** -- "True" o "False" -- si es "True", se agrega un
        nuevo enlace, de lo contrario reemplazará el enlace anterior

   Enlaza *acciones divertidas* a eventos en los movimientos del
   mouse. Si la *acción* es "None", las acciones asociadas son
   borradas.

   Observación: cada secuencia de los eventos de movimiento del mouse
   en una tortuga es precedida por un evento de click del mouse en esa
   tortuga.

      >>> turtle.ondrag(turtle.goto)

   Subsecuentemente, clickear y arrastrar la Tortuga la moverá a
   través de la pantalla produciendo dibujos a mano alzada (si el
   lápiz está abajo).

### Métodos especiales de *Turtle*

turtle.poly()

   Record the vertices of a polygon drawn in the "with turtle.poly():"
   block. The first and last vertices will be connected.

      >>> with turtle.poly():
      ...     turtle.forward(100)
      ...     turtle.right(60)
      ...     turtle.forward(100)

   Added in version 3.14.

turtle.begin_poly()

   Comienza a grabar los vértices de un polígono. La posición actual
   de la tortuga es el primer vértice del polígono.

turtle.end_poly()

   Deja de grabar los vértices de un polígono. La posición actual de
   la tortuga es el último vértice del polígono. Esto se conectará con
   el primer vértice.

turtle.get_poly()

   Devuelve el último polígono grabado.

      >>> turtle.home()
      >>> turtle.begin_poly()
      >>> turtle.fd(100)
      >>> turtle.left(20)
      >>> turtle.fd(30)
      >>> turtle.left(60)
      >>> turtle.fd(50)
      >>> turtle.end_poly()
      >>> p = turtle.get_poly()
      >>> register_shape("myFavouriteShape", p)

turtle.clone()

   Crea y devuelve un clon de la tortuga con la misma posición,
   dirección y propiedades de la tortuga.

      >>> mick = Turtle()
      >>> joe = mick.clone()

turtle.getturtle()
turtle.getpen()

   Devuelve el objeto Tortuga en si. El único uso razonable: es como
   una función para devolver la "tortuga anónima":

      >>> pet = getturtle()
      >>> pet.fd(50)
      >>> pet
      <turtle.Turtle object at 0x...>

turtle.getscreen()

   Devuelve el objeto "TurtleScreen" sobre el cual la tortuga está
   dibujando. Los métodos *TurtleScreen* luego pueden ser llamados
   para ese objeto.

      >>> ts = turtle.getscreen()
      >>> ts
      <turtle._Screen object at 0x...>
      >>> ts.bgcolor("pink")

turtle.setundobuffer(size)

   Parámetros:
      **size** -- un entero o "None"

   Establecer o deshabilitar deshacer búfer. Si *size* es un número
   entero, se instala un búfer de deshacer vacío de un tamaño
   determinado. *size* da el número máximo de acciones de tortuga que
   se pueden deshacer mediante el método/función "undo()". Si *size*
   es "None", el búfer para deshacer está deshabilitado.

      >>> turtle.setundobuffer(42)

turtle.undobufferentries()

   Devuelve el número de entradas en el buffer para deshacer acciones.

      >>> while undobufferentries():
      ...     undo()

### Formas compuestas

Para usar formas complejas con la tortuga, que consiste en varios
polígonos de diferentes colores, deberá usar la clase de ayuda "Shape"
explícitamente como se describe debajo:

1. Crear una objeto de forma vacía del tipo *compound*.

2. Agregue tantos componentes a este objeto como desee, utilizando el
   método "addcomponent()".

   Por ejemplo:

      >>> s = Shape("compound")
      >>> poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
      >>> s.addcomponent(poly1, "red", "blue")
      >>> poly2 = ((0,0),(10,-5),(-10,-5))
      >>> s.addcomponent(poly2, "blue", "red")

3. Ahora agregar la forma a la lista de formas de la pantalla y úsela:

      >>> register_shape("myshape", s)
      >>> shape("myshape")

Nota:

  La clase "Shape" es usada internamente por el método
  "register_shape()" en maneras diferentes. El programador deberá
  lidiar con la clase *Shape* ¡solo cuando use formas compuestas como
  las que se mostraron arriba!

## Métodos de *TurtleScreen/Screen* y sus correspondientes funciones

La mayoría de los ejemplos en esta sección se refieren a la instancia
de *TurtleScreen* llamada "screen".

### Control de ventana

turtle.bgcolor()
turtle.bgcolor(color, /)
turtle.bgcolor(r, g, b, /)

   Return or set the background color of the TurtleScreen.

   Se permiten cuatro formatos de entrada:

   "bgcolor()"
      Return the current background color as color specification
      string or as a tuple (see example).  May be used as input to
      another color/pencolor/fillcolor/bgcolor call.

   "bgcolor(colorstring)"
      Set the background color to *colorstring*, which is a Tk color
      specification string, such as ""red"", ""yellow"", or
      ""#33cc8c"".

   "bgcolor((r, g, b))"
      Set the background color to the RGB color represented by the
      tuple of *r*, *g*, and *b*. Each of *r*, *g*, and *b* must be in
      the range 0..colormode, where colormode is either 1.0 or 255
      (see "colormode()").

   "bgcolor(r, g, b)"
      Set the background color to the RGB color represented by *r*,
      *g*, and *b*.  Each of *r*, *g*, and *b* must be in the range
      0..colormode.

      >>> screen.bgcolor("orange")
      >>> screen.bgcolor()
      'orange'
      >>> screen.bgcolor("#800080")
      >>> screen.bgcolor()
      (128.0, 0.0, 128.0)

turtle.bgpic(picname=None)

   Parámetros:
      **picname** -- a string, name of an image file (PNG, GIF, PGM,
      and PPM) or ""nopic"", or "None"

   Establece la imagen de fondo o devuelve el nombre de la imagen de
   fondo actual. Si *picname* es un nombre de archivo, establece la
   imagen correspondiente como fondo. Si *picname* es ""nopic"", borra
   la imagen de fondo, si hay alguna presente. Si *picname* es "None",
   devuelve el nombre de archivo de la imagen de fondo actual.

      >>> screen.bgpic()
      'nopic'
      >>> screen.bgpic("landscape.gif")
      >>> screen.bgpic()
      "landscape.gif"

turtle.clear()

   Nota:

     Este método de *TurtleScreen* está disponible como una función
     global solo bajo el nombre "clearscreen". La función global
     "clear" es otra, derivada del método de *Turtle* "clear".

turtle.clearscreen()

   Borra todos los dibujos y todas las tortugas del la pantalla de la
   tortuga. Reinicia la ahora vacía pantalla de la tortuga a su estado
   inicial: fondo blanco, sin imagen de fondo, sin enlaces a eventos o
   seguimientos.

turtle.reset()

   Nota:

     Este método *TurtleScreen* esta disponible como una función
     global solo bajo el nombre "resetscreen". La función global
     "reset" es otra, derivada del método *Turtle* "reset".

turtle.resetscreen()

   Reinicia todas las tortugas de la pantalla a su estado inicial.

turtle.screensize(canvwidth=None, canvheight=None, bg=None)

   Parámetros:
      * **canvwidth** -- entero positivo, nueva anchura del lienzo en
        pixeles

      * **canvheight** -- entero positivo, nueva altura del lienzo en
        pixeles

      * **bg** -- *colorstrng* o tupla de color, muevo color de fondo

   Si no se dan argumentos, devuelve el actual (ancho y alto del
   lienzo). Sino redimensiona el lienzo en el que la tortuga está
   dibujando. No altera la ventana de dibujo. Para ver las partes
   ocultas del lienzo, use la barra de desplazamiento. Con este
   método, se pueden hacer visibles aquellas partes de un dibujo que
   antes estaban fuera del lienzo.

   >>> screen.screensize()
   (400, 300)
   >>> screen.screensize(2000,1500)
   >>> screen.screensize()
   (2000, 1500)

   ej. buscar una tortuga que se escapó por error ;-)

turtle.setworldcoordinates(llx, lly, urx, ury)

   Parámetros:
      * **llx** -- un número, coordenada x de la esquina inferior
        izquierda del lienzo

      * **lly** -- un número, coordenada y de la esquina inferior
        izquierda del lienzo

      * **urx** -- un número, coordenada x de la esquina superior
        derecha del lienzo

      * **ury** -- un número, coordenada z de la esquina superior
        derecha del lienzo

   Configura coordenadas definidas por el usuario y cambia al modo
   *world* si es necesario. Esto realiza un "screen.reset()". Si el
   modo *world* ya está activo, todos los dibujos se re dibujan de
   acuerdo a las nuevas coordenadas.

   **ATENCIÓN**: en los sistemas de coordenadas definidos por el
   usuario, los ángulos pueden aparecer distorsionados.

      >>> screen.reset()
      >>> screen.setworldcoordinates(-50,-7.5,50,7.5)
      >>> for _ in range(72):
      ...     left(10)
      ...
      >>> for _ in range(8):
      ...     left(45); fd(2)   # a regular octagon

### Control de animación

turtle.no_animation()

   Temporarily disable turtle animation. The code written inside the
   "no_animation" block will not be animated; once the code block is
   exited, the drawing will appear.

      >>> with screen.no_animation():
      ...     for dist in range(2, 400, 2):
      ...         fd(dist)
      ...         rt(90)

   Added in version 3.14.

turtle.delay(delay=None)

   Parámetros:
      **delay** -- entero positivo

   Establece o retorna el *retraso* del dibujo en mili segundos. (
   Este es aproximadamente, el tiempo de intervalo entre dos
   actualizaciones consecutivas del lienzo). Mientras más largo sea el
   retraso, más lenta la animación.

   Argumento opcional:

      >>> screen.delay()
      10
      >>> screen.delay(5)
      >>> screen.delay()
      5

turtle.tracer(n=None, delay=None)

   Parámetros:
      * **n** -- entero no negativo

      * **delay** -- entero no negativo

   Activa o desactiva la animación de la tortuga y establece el
   retraso para la actualización de los dibujos. Si se da *n*, solo
   cada enésima actualización regular de pantalla se realiza
   realmente. (Puede usarse para acelerar los dibujos de gráficos
   complejos). Cuando es llamada sin argumentos, devuelve el valor de
   *n* guardado actualmente. El segundo argumento establece el valor
   de retraso (ver "delay()").

      >>> screen.tracer(8, 25)
      >>> dist = 2
      >>> for i in range(200):
      ...     fd(dist)
      ...     rt(90)
      ...     dist += 2

turtle.update()

   Realiza una actualización de la pantalla de la tortuga. Para ser
   usada cuando *tracer* está deshabilitada.

Ver también el método *RawTurtle/Turtle* "speed()".

### Usando eventos de pantalla

turtle.listen(xdummy=None, ydummy=None)

   Establece el foco en la pantalla de la tortuga (para recoger
   eventos de teclado). Los argumentos *dummy* se proveen en orden de
   ser capaces de pasar "listen()" a los métodos *onclick*.

turtle.onkey(fun, key)
turtle.onkeyrelease(fun, key)

   Parámetros:
      * **fun** -- una función sin argumentos o "None"

      * **key** -- una cadena de caracteres: tecla (por ejemplo, "a")
        o una acción del teclado (por ejemplo, "space")

   Vincula *fun* a un evento de liberación de una tecla. Si *fun* es
   "None", los eventos vinculados son removidos. Aclaración: para
   poder registrar eventos de teclado, *TurtleScreen* tiene que tener
   el foco. (ver el método "listen()".)

      >>> def f():
      ...     fd(50)
      ...     lt(60)
      ...
      >>> screen.onkey(f, "Up")
      >>> screen.listen()

turtle.onkeypress(fun, key=None)

   Parámetros:
      * **fun** -- una función sin argumentos o "None"

      * **key** -- una cadena de caracteres: tecla (por ejemplo, "a")
        o una acción del teclado (por ejemplo, "space")

   Vincula *fun* a un evento de pulsado de una tecla, o a cualquier
   evento de pulsado de tecla si no se da una. Aclaración: para poder
   registrar eventos de teclado, *TurtleScreen* tiene que tener el
   foco. (ver el método "listen()".)

      >>> def f():
      ...     fd(50)
      ...
      >>> screen.onkey(f, "Up")
      >>> screen.listen()

turtle.onclick(fun, btn=1, add=None)
turtle.onscreenclick(fun, btn=1, add=None)

   Parámetros:
      * **fun** -- una función con dos argumentos que se invocará con
        las coordenadas del punto en el que se hizo clic en el lienzo

      * **btn** -- número del botón del mouse, el valor predeterminado
        es 1 (botón izquierdo del mouse)

      * **add** -- "True" o "False" -- si es "True", se agrega un
        nuevo enlace, de lo contrario reemplazará el enlace anterior

   Vincula *fun* a eventos de click del mouse en esta pantalla. Si
   *fun* es "None", los vínculos existentes son removidos.

   Ejemplo de una instancia TurtleScreen llamada "screen" y una
   instancia Turtle llamada "turtle":

      >>> screen.onclick(turtle.goto) # Subsequently clicking into the TurtleScreen will
      >>>                             # make the turtle move to the clicked point.
      >>> screen.onclick(None)        # remove event binding again

   Nota:

     Este método *TurtleScreen* está disponible como una función
     global solo bajo el nombre "onscreenclick". La función global
     "onclick" es otra derivada del método Turtle "onclick".

turtle.ontimer(fun, t=0)

   Parámetros:
      * **fun** -- una función sin argumentos

      * **t** -- un número >= 0

   Instala un temporizador que llama a *fun* cada *t* milisegundos.

      >>> running = True
      >>> def f():
      ...     if running:
      ...         fd(50)
      ...         lt(60)
      ...         screen.ontimer(f, 250)
      >>> f()   ### makes the turtle march around
      >>> running = False

turtle.mainloop()
turtle.done()

   Comienza un bucle de evento - llamando a la función *mainloop* del
   *Tkinter*. Debe ser la última declaración en un programa gráfico de
   turtle. *No* debe ser usado si algún script es corrido dentro del
   IDLE en modo -n (Sin subproceso) - para uso interactivo de gráficos
   turtle.:

      >>> screen.mainloop()

### Métodos de entrada

turtle.textinput(title, prompt)

   Parámetros:
      * **title** -- cadena de caracteres

      * **prompt** -- cadena de caracteres

   Abre una ventana de diálogo para ingresar una cadena de caracteres.
   El parámetro *title* es el título de la ventana de diálogo,
   *prompt* es un texto que usualmente describe que información se
   debe ingresar. Devuelve la cadena ingresada. Si el diálogo es
   cancelado, devuelve "None".

      >>> screen.textinput("NIM", "Name of first player:")

turtle.numinput(title, prompt, default=None, minval=None, maxval=None)

   Parámetros:
      * **title** -- cadena de caracteres

      * **prompt** -- cadena de caracteres

      * **default** -- número (opcional)

      * **minval** -- número (opcional)

      * **maxval** -- número (opcional)

   Abre una ventana de diálogo para ingresar un número. El título es
   el título de la ventana de diálogo, el mensaje es un texto que
   describe principalmente qué información numérica ingresar.
   predeterminado: valor predeterminado, minval: valor mínimo para la
   entrada, maxval: valor máximo para la entrada. El número ingresado
   debe estar en el rango minval... maxval si se proporcionan estos.
   Si no, se emite una pista y el diálogo permanece abierto para su
   corrección. Devuelve el número ingresado. Si se cancela el diálogo,
   devuelve "None".

      >>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

### Configuración y métodos especiales

turtle.mode(mode=None)

   Parámetros:
      **mode** -- una de las cadenas *"standard"*, *"logo*" o
      *"world*"

   Establece el mode de la tortuga  (*"standard"*, *"logo"* o
   *"world"*) y realiza un reinicio. Si no se da "*mode*", retorna el
   modo actual.

   Mode "standard" is compatible with old "turtle".  Mode "logo" is
   compatible with most Logo turtle graphics.  Mode "world" uses user-
   defined "world coordinates". **Attention**: in this mode angles
   appear distorted if "x/y" unit-ratio doesn't equal 1.

   +--------------+---------------------------+---------------------+
   | Modo         | Rumbo inicial de la       | ángulos positivos   |
   |              | tortuga                   |                     |
   |==============|===========================|=====================|
   | *"standard"* | hacia la derecha (este)   | sentido antihorario |
   +--------------+---------------------------+---------------------+
   | *"logo"*     | hacia arriba (norte)      | sentido horario     |
   +--------------+---------------------------+---------------------+

      >>> mode("logo")   # reinicia la tortuga hacia el norte
      >>> mode()
      'logo'

turtle.colormode(cmode=None)

   Parámetros:
      **cmode** -- uno de los valores 1.0 o 255

   Devuelve el modo de color o configúrelo en 1.0 o 255.
   Posteriormente, los valores *r*, *g*, *b* de los triples de color
   deben estar en el rango 0..*cmode*.

      >>> screen.colormode(1)
      >>> turtle.pencolor(240, 160, 80)
      Traceback (most recent call last):
           ...
      TurtleGraphicsError: bad color sequence: (240, 160, 80)
      >>> screen.colormode()
      1.0
      >>> screen.colormode(255)
      >>> screen.colormode()
      255
      >>> turtle.pencolor(240,160,80)

turtle.getcanvas()

   Devuelve el lienzo de este *TurtleScreen*. Útil para conocedores
   que saben que hace con un *TKinter* *Canvas*.

      >>> cv = screen.getcanvas()
      >>> cv
      <turtle.ScrolledCanvas object ...>

turtle.getshapes()

   Devuelve la lista de nombres de todas las formas de la tortuga
   actualmente disponibles.

      >>> screen.getshapes()
      ['arrow', 'blank', 'circle', ..., 'turtle']

turtle.register_shape(name, shape=None)
turtle.addshape(name, shape=None)

   There are four different ways to call this function:

   1. *name* is the name of an image file (PNG, GIF, PGM, and PPM) and
      *shape* is "None": Install the corresponding image shape.

         >>> screen.register_shape("turtle.gif")

      Nota:

        Las imágenes de tipo *shapes* no rotan cuando la tortuga gira,
        así que ellas ¡no muestran el rumbo de la tortuga!

   2. *name* is an arbitrary string and *shape* is the name of an
      image file (PNG, GIF, PGM, and PPM): Install the corresponding
      image shape.

         >>> screen.register_shape("turtle", "turtle.gif")

      Nota:

        Las imágenes de tipo *shapes* no rotan cuando la tortuga gira,
        así que ellas ¡no muestran el rumbo de la tortuga!

   3. *name* es una cadena de caracteres arbitraria y *shape* es una
      tupla de pares de coordenadas: Instala la forma poligonal
      correspondiente.

         >>> screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))

   4. *name* es una cadena arbitraria y *shape* es un objeto "Shape"
      (compuesto): instala la forma compuesta correspondiente.

   Agregar una forma de tortuga a la lista  de formas de
   *TurtleScreen*. Solo las formas registradas de esta manera pueden
   ser usadas invocando el comando "shape(shapename)".

   Distinto en la versión 3.14: Added support for PNG, PGM, and PPM
   image formats. Both a shape name and an image file name can be
   specified.

turtle.turtles()

   Devuelve la lista de tortugas en la pantalla.

      >>> for turtle in screen.turtles():
      ...     turtle.color("red")

turtle.window_height()

   Devuelve la altura de la ventana de la tortuga.

      >>> screen.window_height()
      480

turtle.window_width()

   Devuelve el ancho de la ventana de la tortuga.

      >>> screen.window_width()
      640

### Métodos específicos de *Screen*, no heredados de *TurtleScreen*

turtle.bye()

   Apaga la ventana gráfica de la tortuga.

turtle.exitonclick()

   Ata el método "bye()" al click del ratón sobre la pantalla.

   Si el valor *"using_IDLE"* en la configuración del diccionario es
   "False" (valor por defecto), también ingresa *mainloop*.
   Observaciones: si se usa la *IDLE* con el modificador (no
   subproceso) "-n", este valor debe establecerse a "True" en
   "turtle.cfg". En este caso el propio *mainloop* de la *IDLE* está
   activa también para script cliente.

turtle.save(filename, overwrite=False)

   Save the current turtle drawing (and turtles) as a PostScript file.

   Parámetros:
      * **filename** -- the path of the saved PostScript file

      * **overwrite** -- if "False" and there already exists a file
        with the given filename, then the function will raise a
        "FileExistsError". If it is "True", the file will be
        overwritten.

      >>> screen.save("my_drawing.ps")
      >>> screen.save("my_drawing.ps", overwrite=True)

   Added in version 3.14.

turtle.setup(width=_CFG['width'], height=_CFG['height'], startx=_CFG['leftright'], starty=_CFG['topbottom'])

   Establece el tamaño y la posición de la ventana principal. Los
   valores por defecto de los argumentos son guardados en el
   diccionario de configuración y puede ser cambiado a través del
   archivo  "turtle.cfg".

   Parámetros:
      * **width** -- si es un entero, el tamaño en pixeles, si es un
        número flotante, una fracción de la pantalla; el valor por
        defecto es 50% de la pantalla

      * **height** -- si es un entero, la altura en pixeles, si es un
        número flotante, una fracción de la pantalla; el valor por
        defecto es 75% de la pantalla

      * **startx** -- si es positivo, punto de inicio en pixeles desde
        la esquina izquierda de la pantalla, si es negativo desde la
        esquina derecha de la pantalla, si es "None", centra la
        ventana horizontalmente

      * **starty** -- si es positivo, punto de inicio en pixeles desde
        la parte superior de la pantalla, si es negativo desde la
        parte inferior de la pantalla, si es "None", centra la ventana
        verticalmente

      >>> screen.setup (width=200, height=200, startx=0, starty=0)
      >>>              # sets window to 200x200 pixels, in upper left of screen
      >>> screen.setup(width=.75, height=0.5, startx=None, starty=None)
      >>>              # sets window to 75% of screen by 50% of screen and centers

turtle.title(titlestring)

   Parámetros:
      **titlestring** -- una cadena de caracteres que se muestra en la
      barra de título de la ventana gráfica de la tortuga

   Establece el título de la ventana de la tortuga a *titlestring*.

      >>> screen.title("Welcome to the turtle zoo!")

## Clases públicas

class turtle.RawTurtle(canvas)
class turtle.RawPen(canvas)

   Parámetros:
      **canvas** -- un "tkinter.Canvas", un "ScrolledCanvas" o un
      "TurtleScreen"

   Crea una tortuga. La tortuga tiene todos los métodos descriptos
   anteriormente como "métodos de *"Turtle/RawTurtle"*.

class turtle.Turtle

   Subclase de *RawTurtle*, tiene la misma interface pero dibuja sobre
   una objeto por defecto "Screen" creado automáticamente cuando es
   necesario por primera vez.

class turtle.TurtleScreen(cv)

   Parámetros:
      **cv** -- un "tkinter.Canvas"

   Proporciona métodos orientados a la pantalla como "bgcolor()",
   etc., que se describen anteriormente.

class turtle.Screen

   Subclase de *TurtleScreen*, con cuatro métodos agregados.

class turtle.ScrolledCanvas(master)

   Parámetros:
      **master** -- algunos *widgets* *TKinter* para contener el
      *ScrollCanvas*, por ejemplo un lienzo *Tkinter* con barras de
      desplazamiento agregadas

   Usado por la clase *Screen*, que proporciona automáticamente un
   *ScrolledCanvas* como espacio de trabajo para las tortugas.

class turtle.Shape(type_, data)

   Parámetros:
      **type_** -- una de las cadenas de caracteres *"polygon"*,
      *"image"*, *"compound"*

   Estructura de datos que modela las formas. El par "(type_, data)"
   debe seguir estas especificaciones:

   +-------------+------------------------------------------------------------+
   | *type_*     | *data*                                                     |
   |=============|============================================================|
   | *"polygon"* | una tupla para el polígono, por ejemplo: una tupla de par  |
   |             | de coordenadas                                             |
   +-------------+------------------------------------------------------------+
   | *"image"*   | una imagen (en esta forma solo se usa ¡internamente!)      |
   +-------------+------------------------------------------------------------+
   | *"compound  | "None" (una forma compuesta tiene que ser construida       |
   | "*          | usando el método "addcomponent()")                         |
   +-------------+------------------------------------------------------------+

   addcomponent(poly, fill, outline=None)

      Parámetros:
         * **poly** -- un polígono, por ejemplo una tupla de pares de
           números

         * **fill** -- un color con el que el polígono será llenado

         * **outline** -- un color con el que se delineará el polígono
           (se de ingresa)

      Ejemplo:

         >>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
         >>> s = Shape("compound")
         >>> s.addcomponent(poly, "red", "blue")
         >>> # ... add more components and then use register_shape()

      Ver Formas compuestas.

class turtle.Vec2D(x, y)

   Una clase de vectores bidimensionales, usado como clase de ayuda
   para implementar gráficos de tortuga. Puede ser útil para los
   programas de gráficos de tortugas también. Derivado de la tupla,
   ¡por lo que un vector es una tupla!

   Proporciona (para *a*, *b* vectores, *k* números)

   * "a + b" suma de vectores

   * "a - b" resta de vectores

   * "a * b" producto interno

   * "k * a" y "a * k" multiplicación con escalar

   * "abs(a)" valor absoluto de a

   * "a.rotate(angle)" rotación

## Explicación

Un objeto tortuga se dibuja en un objeto de pantalla, y hay una serie
de clases clave en la interfaz orientada a objetos tortuga que se
pueden usar para crearlos y relacionarlos entre sí.

Una instancia "Turtle" creará automáticamente una instancia "Screen"
si aún no hay una presente.

"Turtle" es una subclase de "RawTurtle", que crea automáticamente una
superficie de dibujo. Para ello, será necesario proporcionar o crear
una *canvas*. La *canvas* puede ser una "tkinter.Canvas", una
"ScrolledCanvas" o una "TurtleScreen".

"TurtleScreen" es la superficie de dibujo básica de una tortuga.
"Screen" es una subclase de "TurtleScreen" e incluye some additional
methods para gestionar su apariencia (incluido el tamaño y el título)
y su comportamiento. El constructor de "TurtleScreen" necesita un
"tkinter.Canvas" o un "ScrolledCanvas" como argumento.

La interfaz funcional para gráficos de tortugas utiliza los distintos
métodos de "Turtle" y "TurtleScreen"/"Screen". En segundo plano, se
crea automáticamente un objeto de pantalla cada vez que se llama a una
función derivada de un método "Screen". De manera similar, se crea
automáticamente un objeto de tortuga cada vez que se llama a
cualquiera de las funciones derivadas de un método de Turtle.

Para utilizar varias tortugas en una pantalla, se debe utilizar la
interfaz orientada a objetos.

## Ayuda y configuración

### Cómo usar la ayuda

Los métodos públicos de las clases Screen y Turtle están ampliamente
documentados a través de cadenas de documentación. Por lo tanto, estos
se pueden usar como ayuda en línea a través de las instalaciones de
ayuda de Python:

* Cuando se usa IDLE, la información sobre herramientas muestra las
  firmas y las primeras líneas de las cadenas de documentos de las
  llamadas de función/método escritas.

* Llamar a "help()" en métodos o funciones muestra los docstrings:

     >>> help(Screen.bgcolor)
     Help on method bgcolor in module turtle:

     bgcolor(self, *args) unbound turtle.Screen method
         Set or return backgroundcolor of the TurtleScreen.

         Arguments (if given): a color string or three numbers
         in the range 0..colormode or a 3-tuple of such numbers.

         >>> screen.bgcolor("orange")
         >>> screen.bgcolor()
         "orange"
         >>> screen.bgcolor(0.5,0,0.5)
         >>> screen.bgcolor()
         "#800080"

     >>> help(Turtle.penup)
     Help on method penup in module turtle:

     penup(self) unbound turtle.Turtle method
         Pull the pen up -- no drawing when moving.

         Aliases: penup | pu | up

         No argument

         >>> turtle.penup()

* Los docstrings de las funciones que se derivan de los métodos tienen
  una forma modificada:

     >>> help(bgcolor)
     Help on function bgcolor in module turtle:

     bgcolor(*args)
         Set or return backgroundcolor of the TurtleScreen.

         Arguments (if given): a color string or three numbers
         in the range 0..colormode or a 3-tuple of such numbers.

         Example::

           >>> bgcolor("orange")
           >>> bgcolor()
           "orange"
           >>> bgcolor(0.5,0,0.5)
           >>> bgcolor()
           "#800080"

     >>> help(penup)
     Help on function penup in module turtle:

     penup()
         Pull the pen up -- no drawing when moving.

         Aliases: penup | pu | up

         No argument

         Example:
         >>> penup()

Estos docstrings modificados se crean automáticamente junto con las
definiciones de función que se derivan de los métodos en el momento de
la importación.

### Traducción de cadenas de documentos a diferentes idiomas

Existe una utilidad para crear un diccionario cuyas claves son los
nombres de los métodos y cuyos valores son los docstrings de los
métodos públicos de las clases Screen y Turtle.

turtle.write_docstringdict(filename='turtle_docstringdict')

   Parámetros:
      **filename** -- una cadena de caracteres, utilizada como nombre
      de archivo

   Crea y escribe un diccionario-docstring en un script de Python con
   el nombre de archivo dado. Esta función tiene que ser llamada
   explícitamente (no es utilizada por las clases de gráficos de
   tortugas). El diccionario de docstrings se escribirá en el script
   de Python "*filename*.py". Está destinado a servir como plantilla
   para la traducción de las cadenas de documentos a diferentes
   idiomas.

If you (or your students) want to use "turtle" with online help in
your native language, you have to translate the docstrings and save
the resulting file as e.g. "turtle_docstringdict_german.py".

Si tiene una entrada adecuada en su archivo "turtle.cfg", este
diccionario se leerá en el momento de la importación y reemplazará los
docstrings originales en inglés.

En el momento de escribir este artículo, existen diccionarios de
docstrings en alemán e italiano. (Solicitudes por favor a
glingl@aon.at.)

### Cómo configurar Screen and Turtles

La configuración predeterminada incorporada imita la apariencia y el
comportamiento del antiguo módulo de tortuga para mantener la mejor
compatibilidad posible con él.

Si desea utilizar una configuración diferente que refleje mejor las
características de este módulo o que se adapte mejor a sus
necesidades, por ejemplo, para su uso en un aula, puede preparar un
archivo de configuración "turtle.cfg" que se leerá en el momento de la
importación y modificará la configuración de acuerdo con su
configuración.

La configuración incorporada correspondería al siguiente "turtle.cfg":

   width = 0.5
   height = 0.75
   leftright = None
   topbottom = None
   canvwidth = 400
   canvheight = 300
   mode = standard
   colormode = 1.0
   delay = 10
   undobuffersize = 1000
   shape = classic
   pencolor = black
   fillcolor = black
   resizemode = noresize
   visible = True
   language = english
   exampleturtle = turtle
   examplescreen = screen
   title = Python Turtle Graphics
   using_IDLE = False

Breve explicación de las entradas seleccionadas:

* Las primeras cuatro líneas corresponden a los argumentos del método
  "Screen.setup".

* Las líneas 5 y 6 corresponden a los argumentos del método
  "Screen.screensize".

* *shape* puede ser cualquiera de las formas integradas, por ejemplo:
  arrow, turtle, etc. Para obtener más información, pruebe con
  "help(shape)".

* Si no desea utilizar ningún color de relleno (es decir, hacer que la
  tortuga sea transparente), debe escribir "fillcolor = """ (pero
  todas las cadenas no vacías no deben tener comillas en el archivo
  cfg).

* Si desea reflejar el estado de la tortuga, debe usar "resizemode =
  auto".

* If you set e.g. "language = italian" the docstringdict
  "turtle_docstringdict_italian.py" will be loaded at import time (if
  present on the import path, e.g. in the same directory as "turtle").

* Las entradas *exampleturtle* y *examplescreen* definen los nombres
  de estos objetos a medida que aparecen en las cadenas de documentos.
  La transformación de método-docstrings en función-docstrings
  eliminará estos nombres de las docstrings.

* *using_IDLE*: Establezca esta opción en "True" si trabaja
  habitualmente con IDLE y su opción "-n" ("sin subproceso"). Esto
  evitará que "exitonclick()" ingrese al bucle principal.

There can be a "turtle.cfg" file in the directory where "turtle" is
stored and an additional one in the current working directory.  The
latter will override the settings of the first one.

El directorio "Lib/turtledemo" contiene un archivo "turtle.cfg". Puede
estudiarlo como un ejemplo y ver sus efectos al ejecutar las
demostraciones (preferiblemente no desde el visor de demostraciones).

## "turtledemo" --- Demo scripts

The "turtledemo" package includes a set of demo scripts.  These
scripts can be run and viewed using the supplied demo viewer as
follows:

   python -m turtledemo

Alternativamente, puede ejecutar los scripts de demostración
individualmente. Por ejemplo,

   python -m turtledemo.bytedesign

The "turtledemo" package directory contains:

* Un visor de demostración "__main__.py" que se puede utilizar para
  ver el código fuente de los scripts y ejecutarlos al mismo tiempo.

* Multiple scripts demonstrating different features of the "turtle"
  module.  Examples can be accessed via the Examples menu.  They can
  also be run standalone.

* Un archivo "turtle.cfg" que sirve como ejemplo de cómo escribir y
  usar dichos archivos.

Los scripts de demostración son:

+--------------------------+--------------------------------+----------------------------------------+
| Nombre                   | Descripción                    | Características                        |
|==========================|================================|========================================|
| "bytedesign"             | patrón de gráficos de tortuga  | "tracer()", "delay()", "update()"      |
## |                          | clásica compleja               |                                        |

| "chaos"                  | gráficos dinámicos de          | coordenadas mundiales                  |
|                          | Verhulst, muestra que los      |                                        |
|                          | cálculos de la computadora     |                                        |
|                          | pueden generar resultados a    |                                        |
|                          | veces contra las expectativas  |                                        |
## |                          | del sentido común              |                                        |

| "clock"                  | reloj analógico que muestra la | turtles as clock's hands, "ontimer()"  |
## |                          | hora de su computadora         |                                        |

## | "colormixer"             | experimento con r, g, b        | "ondrag()"                             |

## | "forest"                 | 3 árboles de ancho primero     | aleatorización                         |

## | "fractalcurves"          | Curvas Hilbert & Koch          | recursión                              |

| "lindenmayer"            | etnomatemáticas (kolams        | Sistema-L                              |
## |                          | indios)                        |                                        |

| "minimal_hanoi"          | Torres de Hanoi                | Rectangular Turtles as Hanoi discs     |
## |                          |                                | ("shape()", "shapesize()")             |

| "nim"                    | juega el clásico juego de nim  | tortugas como nimsticks, impulsado por |
|                          | con tres montones de palos     | eventos (mouse, teclado)               |
## |                          | contra la computadora.         |                                        |

| "paint"                  | programa de dibujo super       | "onclick()"                            |
## |                          | minimalista                    |                                        |

## | "peace"                  | elemental                      | turtle: apariencia y animación         |

| "penrose"                | embaldosado aperiódico con     | "stamp()"                              |
## |                          | cometas y dardos               |                                        |

| "planet_and_moon"        | simulación de sistema          | formas compuestas, "Vec2D"             |
## |                          | gravitacional                  |                                        |

| "rosette"                | un patrón del artículo de      | "clone()", "undo()"                    |
|                          | wikipedia sobre gráficos de    |                                        |
## |                          | tortuga (*turtle*)             |                                        |

| "round_dance"            | tortugas bailarinas que giran  | compound shapes, "clone()"             |
|                          | por parejas en dirección       | "shapesize()", "tilt()",               |
## |                          | opuesta                        | "get_shapepoly()", "update()"          |

| "sorting_animate"        | demostración visual de         | alineación simple, aleatorización      |
|                          | diferentes métodos de          |                                        |
## |                          | ordenamiento                   |                                        |

| "tree"                   | un primer árbol de amplitud    | "clone()"                              |
## |                          | (gráfico, usando generadores)  |                                        |

| "two_canvases"           | diseño simple                  | tortugas en dos lienzos                |
## |                          |                                | (*two_canvases*)                       |

## | "yinyang"                | otro ejemplo elemental         | "circle()"                             |

¡Diviértete!

## Cambios desde Python 2.6

* Se han eliminado los métodos "Turtle.tracer", "Turtle.window_width"
  y "Turtle.window_height". Los métodos con estos nombres y
  funcionalidades ahora solo están disponibles como métodos de
  "Screen". Las funciones derivadas de estos siguen estando
  disponibles. (De hecho, ya en Python 2.6 estos métodos eran meras
  duplicaciones de los métodos "TurtleScreen"/"Screen"
  correspondientes).

* Se ha eliminado el método "Turtle.fill()". El comportamiento de
  "begin_fill()" y "end_fill()" ha cambiado ligeramente: ahora cada
  proceso de llenado debe completarse con una llamada a "end_fill()".

* Se ha añadido un método "Turtle.filling". Devuelve un valor
  booleano: "True" si se está realizando un proceso de llenado,
  "False" en caso contrario. Este comportamiento corresponde a una
  llamada "fill()" sin argumentos en Python 2.6.

## Cambios desde Python 3.0

* Se han añadido los métodos "shearfactor()", "shapetransform()" y
  "get_shapepoly()" de "Turtle". De esta forma, ahora está disponible
  toda la gama de transformaciones lineales regulares para transformar
  formas de tortugas. Se ha mejorado la funcionalidad de
  "tiltangle()": ahora se puede utilizar para obtener o establecer el
  ángulo de inclinación.

* Se ha añadido el método "Screen" "onkeypress()" como complemento de
  "onkey()". Como este último vincula acciones al evento de liberación
  de la tecla, también se le ha añadido un alias: "onkeyrelease()".

* Se ha agregado el método "Screen.mainloop", por lo que ya no es
  necesario utilizar la función independiente "mainloop()" al trabajar
  con objetos "Screen" y "Turtle".

* Se han añadido dos métodos de entrada: "Screen.textinput" y
  "Screen.numinput". Estos abren cuadros de diálogo de entrada y
  devuelven cadenas y números respectivamente.
