---
title: 1. Abriendo el apetito
source_url: https://docs.python.org/es/3
source_path: tutorial/appetite.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4870
---

# 1. Abriendo el apetito

Si trabajas mucho con ordenadores, en algún momento encontrarás que
hay alguna tarea que quieres automatizar. Por ejemplo, quizás quieres
buscar y remplazar un texto en muchos ficheros o renombrar y reordenar
un montón de imágenes de forma complicada. Quizás lo que quieres es
escribir una pequeña base de datos personalizada, una interfaz gráfica
o un juego simple.

Si eres un desarrollador profesional, quizás quieres trabajar con
varias librerías de C/C++/Java pero encuentras el ciclo de
escribir/compilar/probar/recompilar bastante lento. Quizás estás
escribiendo una serie de pruebas para éstas librerías y te parece
tedioso escribir el código de pruebas. O quizás has escrito un
programa que puede utilizar un lenguaje como extensión y no quieres
diseñar e implementar un lenguaje entero para tu aplicación.

Python es justo el lenguaje para ti.

Puedes escribir un script de shell de Unix o archivos por lotes de
Windows para algunas de estas tareas. Los scripts de shell son mejores
para mover archivos y cambiar datos de texto, pero no son adecuados
para juegos o aplicaciones GUI. Podrías escribir un programa C / C ++
/ Java, pero llevaría mucho tiempo de desarrollo obtener incluso un
primer programa de borrador. Python es más fácil de usar, está
disponible en los sistemas operativos Windows, macOS y Unix, y te
ayudará a hacer el trabajo más rápidamente.

Python es fácil de utilizar y es un verdadero lenguaje de programación
ofreciendo mucha más estructura y soporte para programas grandes que
la que ofrecen scripts de shell o archivos por lotes. Por otro lado,
Python también ofrece mayor comprobación de errores que C y siendo un
*lenguaje de muy alto nivel* tiene tipos de datos de alto nivel
incorporados como listas flexibles y diccionarios. Debido a sus tipos
de datos más generales, Python es aplicable a más dominios que Awk o
Perl, aunque hay muchas cosas que son tan sencillas en Python como en
esos lenguajes.

Python te permite dividir tu programa en módulos que pueden
reutilizarse en otros programas de Python. Tiene una gran colección de
módulos estándar que puedes utilizar como la base de tus programas o
como ejemplos para empezar a aprender Python. Algunos de estos módulos
proporcionan cosas como entrada/salida de ficheros, llamadas a
sistema, sockets e incluso interfaces a herramientas de interfaz
gráfica como Tk.

Python es un lenguaje interpretado, lo cual puede ahorrarte mucho
tiempo durante el desarrollo ya que no es necesario compilar ni
enlazar. El intérprete puede usarse interactivamente, lo que facilita
experimentar con características del lenguaje, escribir programas
desechables o probar funciones cuando se hace desarrollo de programas
de abajo hacia arriba. Es también una calculadora de escritorio
práctica.

Python permite escribir programas compactos y legibles. Los programas
en Python son típicamente más cortos que sus programas equivalentes en
C, C++ o Java por varios motivos:

* los tipos de datos de alto nivel permiten expresar operaciones
  complejas en una sola instrucción;

* la agrupación de instrucciones se hace mediante indentación en vez
  de llaves de apertura y cierre;

* no es necesario declarar variables ni argumentos.

Python es *extensible*: si ya sabes programar en C es fácil añadir
nuevas funciones o módulos al intérprete, ya sea para realizar
operaciones críticas a velocidad máxima, o para enlazar programas de
Python con bibliotecas que tal vez sólo estén disponibles de forma
binaria (por ejemplo bibliotecas gráficas específicas de un
fabricante). Una vez estés realmente entusiasmado, puedes enlazar el
intérprete Python en una aplicación hecha en C y usarlo como lenguaje
de extensión o de comando para esa aplicación.

Por cierto, el lenguaje recibe su nombre del programa de televisión de
la BBC "Monty Python's Flying Circus" y no tiene nada que ver con
reptiles. Hacer referencias sobre Monty Python en la documentación no
sólo esta permitido, ¡sino que también está bien visto!

Ahora que estás emocionado con Python, querrás verlo en más detalle.
Como la mejor forma de aprender un lenguaje es usarlo, el tutorial te
invita a que juegues con el intérprete de Python a medida que vas
leyendo.

En el próximo capítulo se explicará la mecánica de uso del intérprete.
Esta es información bastante mundana, pero es esencial para poder
probar los ejemplos que aparecerán más adelante.

El resto del tutorial introduce varias características del lenguaje y
el sistema Python a través de ejemplos, empezando con expresiones,
instrucciones y tipos de datos simples, pasando por funciones y
módulos, y finalmente tocando conceptos avanzados como excepciones y
clases definidas por el usuario.
