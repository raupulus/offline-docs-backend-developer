---
title: El tutorial de Python
source_url: https://docs.python.org/es/3
source_path: tutorial/index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4930
---

# El tutorial de Python

Truco:

  This tutorial is designed for *programmers* that are new to the
  Python language, **not** *beginners* who are new to programming.

Python es un lenguaje de programación potente y fácil de aprender.
Tiene estructuras de datos de alto nivel eficientes y un simple pero
efectivo sistema de programación orientado a objetos. La elegante
sintaxis de Python y su tipado dinámico, junto a su naturaleza
interpretada lo convierten en un lenguaje ideal para scripting y
desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de
plataformas.

The Python interpreter and the extensive standard library are freely
available in source or binary form for all major platforms from the
Python website, https://www.python.org/, and may be freely
distributed. The same site also contains distributions of and pointers
to many free third party Python modules, programs and tools, and
additional documentation.

El intérprete de Python es fácilmente extensible con funciones y tipos
de datos implementados en C o C++ (u otros lenguajes que permitan ser
llamados desde C). Python también es apropiado como un lenguaje para
extender aplicaciones modificables.

This tutorial introduces the reader informally to the basic concepts
and features of the Python language and system. Be aware that it
expects you to have a basic understanding of programming in general.
It helps to have a Python interpreter handy for hands-on experience,
but all examples are self-contained, so the tutorial can be read off-
line as well.

Para una descripción de los objetos estándar y de los módulos, ver La
biblioteca estándar de Python. Referencia del Lenguaje Python dónde se
ofrece una definición más formal del lenguaje. Para escribir
extensiones en C o C++, leer Ampliación e incrustación del intérprete
de Python y Python/C API reference manual. Existen diversos libros que
cubren Python en detalle.

Este tutorial no pretende ser exhaustivo ni cubrir cada una de las
características del lenguaje, ni siquiera las más utilizadas. En vez
de eso, pretende introducir muchas de las funcionalidades más notables
y brindar una idea clara acerca del estilo y el tipo de lenguaje que
es Python. Después de leerlo podrás leer y escribir módulos y
programas en Python, y estarás listo para aprender más acerca de las
diversas librerías y módulos descritos en La biblioteca estándar de
Python.

Es interesante leer el Glosario.

* 1. Abriendo el apetito

* 2. Usando el intérprete de Python

  * 2.1. Invocar el intérprete

    * 2.1.1. Paso de argumentos

    * 2.1.2. Modo interactivo

  * 2.2. El intérprete y su entorno

    * 2.2.1. Codificación del código fuente

* 3. Una introducción informal a Python

  * 3.1. Usando Python como una calculadora

    * 3.1.1. Números

    * 3.1.2. Texto

    * 3.1.3. Listas

  * 3.2. Primeros pasos hacia la programación

* 4. Más herramientas para control de flujo

  * 4.1. La sentencia "if"

  * 4.2. La sentencia "for"

  * 4.3. La función "range()"

  * 4.4. Las sentencias "break" y "continue"

  * 4.5. Cláusulas "else" en bucles

  * 4.6. La sentencia "pass"

  * 4.7. La sentencia "match"

  * 4.8. Definir funciones

  * 4.9. Más sobre definición de funciones

    * 4.9.1. Argumentos con valores por omisión

    * 4.9.2. Palabras claves como argumentos

    * 4.9.3. Parámetros especiales

      * 4.9.3.1. Argumentos posicionales o de palabras claves

      * 4.9.3.2. Parámetros únicamente posicionales

      * 4.9.3.3. Argumentos únicamente de palabras clave

      * 4.9.3.4. Ejemplos de Funciones

      * 4.9.3.5. Resumen

    * 4.9.4. Listas de argumentos arbitrarios

    * 4.9.5. Desempaquetando una lista de argumentos

    * 4.9.6. Expresiones lambda

    * 4.9.7. Cadenas de texto de documentación

    * 4.9.8. Anotación de funciones

  * 4.10. Intermezzo: Estilo de programación

* 5. Estructuras de datos

  * 5.1. Más sobre listas

    * 5.1.1. Usar listas como pilas

    * 5.1.2. Usar listas como colas

    * 5.1.3. Comprensión de listas

    * 5.1.4. Listas por comprensión anidadas

  * 5.2. La instrucción "del"

  * 5.3. Tuplas y secuencias

  * 5.4. Conjuntos

  * 5.5. Diccionarios

  * 5.6. Técnicas de iteración

  * 5.7. Más acerca de condiciones

  * 5.8. Comparando secuencias y otros tipos

* 6. Módulos

  * 6.1. Más sobre los módulos

    * 6.1.1. Ejecutar módulos como scripts

    * 6.1.2. El camino de búsqueda de los módulos

    * 6.1.3. Archivos "compilados" de Python

  * 6.2. Módulos estándar

  * 6.3. La función "dir()"

  * 6.4. Paquetes

    * 6.4.1. Importar * desde un paquete

    * 6.4.2. Referencias internas en paquetes

    * 6.4.3. Paquetes en múltiples directorios

* 7. Entrada y salida

  * 7.1. Formateo elegante de la salida

    * 7.1.1. Formatear cadenas literales

    * 7.1.2. El método format() de cadenas

    * 7.1.3. Formateo manual de cadenas

    * 7.1.4. Viejo formateo de cadenas

  * 7.2. Leyendo y escribiendo archivos

    * 7.2.1. Métodos de los objetos Archivo

    * 7.2.2. Guardar datos estructurados con "json"

* 8. Errores y excepciones

  * 8.1. Errores de sintaxis

  * 8.2. Excepciones

  * 8.3. Gestionando excepciones

  * 8.4. Lanzando excepciones

  * 8.5. Encadenamiento de excepciones

  * 8.6. Excepciones definidas por el usuario

  * 8.7. Definiendo acciones de limpieza

  * 8.8. Acciones predefinidas de limpieza

  * 8.9. Lanzando y gestionando múltiples excepciones no relacionadas

  * 8.10. Enriqueciendo excepciones con notas

* 9. Clases

  * 9.1. Unas palabras sobre nombres y objetos

  * 9.2. Ámbitos y espacios de nombres en Python

    * 9.2.1. Ejemplo de ámbitos y espacios de nombre

  * 9.3. Un primer vistazo a las clases

    * 9.3.1. Sintaxis de definición de clases

    * 9.3.2. Objetos clase

    * 9.3.3. Objetos instancia

    * 9.3.4. Objetos método

    * 9.3.5. Variables de clase y de instancia

  * 9.4. Algunas observaciones

  * 9.5. Herencia

    * 9.5.1. Herencia múltiple

  * 9.6. Variables privadas

  * 9.7. Detalles y Cuestiones Varias

  * 9.8. Iteradores

  * 9.9. Generadores

  * 9.10. Expresiones generadoras

* 10. Brief tour of the standard library

  * 10.1. Operating system interface

  * 10.2. File wildcards

  * 10.3. Command-line arguments

  * 10.4. Error output redirection and program termination

  * 10.5. String pattern matching

  * 10.6. Matemáticas

  * 10.7. Internet access

  * 10.8. Dates and times

  * 10.9. Data compression

  * 10.10. Performance measurement

  * 10.11. Quality control

  * 10.12. Batteries included

* 11. Brief tour of the standard library --- part II

  * 11.1. Output formatting

  * 11.2. Plantillas

  * 11.3. Working with binary data record layouts

  * 11.4. Multi-hilos

  * 11.5. Registrando

  * 11.6. Weak references

  * 11.7. Tools for working with lists

  * 11.8. Decimal floating-point arithmetic

* 12. Entornos virtuales y paquetes

  * 12.1. Introducción

  * 12.2. Creando entornos virtuales

  * 12.3. Manejando paquetes con pip

* 13. ¿Y ahora qué?

* 14. Edición de entrada interactiva y sustitución de historial

  * 14.1. Autocompletado con tab e historial de edición

  * 14.2. Alternativas al intérprete interactivo

* 15. Floating-Point Arithmetic:  Issues and Limitations

  * 15.1. Error de Representación

* 16. Apéndice

  * 16.1. Modo interactivo

    * 16.1.1. Manejo de errores

    * 16.1.2. Programas ejecutables de Python

    * 16.1.3. El archivo de inicio interactivo

    * 16.1.4. Los módulos de customización
