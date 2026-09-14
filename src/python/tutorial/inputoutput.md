---
title: 7. Entrada y salida
source_url: https://docs.python.org/es/3
source_path: tutorial/inputoutput.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4940
---

# 7. Entrada y salida

Hay diferentes métodos de presentar la salida de un programa; los
datos pueden ser impresos de una forma legible por humanos, o escritos
a un archivo para uso futuro. Este capítulo discutirá algunas de las
posibilidades.

## 7.1. Formateo elegante de la salida

Hasta ahora encontramos dos maneras de escribir valores:
*declaraciones de expresión* y la función "print()". (Una tercera
manera es usando el método "write()" de los objetos tipo archivo; el
archivo de salida estándar puede referenciarse como "sys.stdout". Mirá
la Referencia de la Biblioteca para más información sobre esto).

A menudo se querrá tener más control sobre el formato de la salida, y
no simplemente imprimir valores separados por espacios. Para ello, hay
varias maneras de dar formato a la salida.

* Para usar literales de cadena formateados, comience una cadena con
  "f" o "F" antes de la comilla de apertura o comillas triples. Dentro
  de esta cadena,  se puede escribir una expresión de Python entre los
  caracteres "{" y "}" que pueden hacer referencia a variables o
  valores literales.

     >>> year = 2016
     >>> event = 'Referendum'
     >>> f'Results of the {year} {event}'
     'Results of the 2016 Referendum'

* The "str.format()" method of strings requires more manual effort.
  You'll still use "{" and "}" to mark where a variable will be
  substituted and can provide detailed formatting directives, but
  you'll also need to provide the information to be formatted. In the
  following code block there are two examples of how to format
  variables:

     >>> yes_votes = 42_572_654
     >>> total_votes = 85_705_149
     >>> percentage = yes_votes / total_votes
     >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
     ' 42572654 YES votes  49.67%'

  Notice how the "yes_votes" are padded with spaces and a negative
  sign only for negative numbers. The example also prints "percentage"
  multiplied by 100, with 2 decimal places and followed by a percent
  sign (see Format specification mini-language for details).

* Por último, puede realizar todo el control de cadenas usted mismo
  mediante operaciones de concatenación y segmentación de cadenas para
  crear cualquier diseño que se pueda imaginar.  El tipo de cadena
  tiene algunos métodos que realizan operaciones útiles para rellenar
  cadenas a un ancho de columna determinado.

Cuando no necesita una salida elegante, pero solo desea una
visualización rápida de algunas variables con fines de depuración,
puede convertir cualquier valor en una cadena con las funciones
"repr()" o "str()".

La función "str()" retorna representaciones de los valores que son
bastante legibles por humanos, mientras que "repr()" genera
representaciones que pueden ser leídas por el intérprete (o forzarían
un "SyntaxError" si no hay sintaxis equivalente). Para objetos que no
tienen una representación en particular para consumo humano, "str()"
retornará el mismo valor que "repr()". Muchos valores, como números o
estructuras como listas y diccionarios, tienen la misma representación
usando cualquiera de las dos funciones.  Las cadenas, en particular,
tienen dos representaciones distintas.

Algunos ejemplos:

   >>> s = 'Hello, world.'
   >>> str(s)
   'Hello, world.'
   >>> repr(s)
   "'Hello, world.'"
   >>> str(1/7)
   '0.14285714285714285'
   >>> x = 10 * 3.25
   >>> y = 200 * 200
   >>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
   >>> print(s)
   The value of x is 32.5, and y is 40000...
   >>> # The repr() of a string adds string quotes and backslashes:
   >>> hello = 'hello, world\n'
   >>> hellos = repr(hello)
   >>> print(hellos)
   'hello, world\n'
   >>> # The argument to repr() may be any Python object:
   >>> repr((x, y, ('spam', 'eggs')))
   "(32.5, 40000, ('spam', 'eggs'))"

The "string" module contains support for a simple templating approach
based upon regular expressions, via "string.Template". This offers yet
another way to substitute values into strings, using placeholders like
"$x" and replacing them with values from a dictionary. This syntax is
easy to use, although it offers much less control for formatting.

### 7.1.1. Formatear cadenas literales

Literales de cadena formateados (también llamados f-strings para
abreviar) le permiten incluir el valor de las expresiones de Python
dentro de una cadena prefijando la cadena con "f" o "F" y escribiendo
expresiones como "{expresion}".

La expresión puede ir seguida de un especificador de formato opcional
. Esto permite un mayor control sobre cómo se formatea el valor. En el
ejemplo siguiente se redondea pi a tres lugares después del decimal:

   >>> import math
   >>> print(f'The value of pi is approximately {math.pi:.3f}.')
   The value of pi is approximately 3.142.

Pasar un entero después de "':'" hará que ese campo sea un número
mínimo de caracteres de ancho. Esto es útil para hacer que las
columnas se alineen.

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
   >>> for name, phone in table.items():
   ...     print(f'{name:10} ==> {phone:10d}')
   ...
   Sjoerd     ==>       4127
   Jack       ==>       4098
   Dcab       ==>       7678

Se pueden utilizar otros modificadores para convertir el valor antes
de formatearlo. "'!a'" se aplica "ascii()", "'!s'" se aplica "str()",
y "'!r'" se aplica "repr()":

   >>> animals = 'eels'
   >>> print(f'My hovercraft is full of {animals}.')
   My hovercraft is full of eels.
   >>> print(f'My hovercraft is full of {animals!r}.')
   My hovercraft is full of 'eels'.

El especificador "=" puede utilizarse para expandir una expresión al
texto de la expresión, un signo igual y, a continuación, la
representación de la expresión evaluada:

>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'

Véase expresiones auto-documentadas para más información en el
especificador "=". Para obtener una referencia sobre estas
especificaciones de formato, consulte la guía de referencia para
Format specification mini-language.

### 7.1.2. El método format() de cadenas

El uso básico del método "str.format()" es como esto:

   >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
   We are the knights who say "Ni!"

Las llaves y caracteres dentro de las mismas (llamados campos de
formato) son reemplazadas con los objetos pasados en el método
"str.format()".  Un número en las llaves se refiere a la posición del
objeto pasado en el método "str.format()".

   >>> print('{0} and {1}'.format('spam', 'eggs'))
   spam and eggs
   >>> print('{1} and {0}'.format('spam', 'eggs'))
   eggs and spam

Si se usan argumentos nombrados en el método "str.format()", sus
valores se referencian usando el nombre del argumento.

   >>> print('This {food} is {adjective}.'.format(
   ...       food='spam', adjective='absolutely horrible'))
   This spam is absolutely horrible.

Se pueden combinar arbitrariamente argumentos posicionales y
nombrados:

   >>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
   ...                                                    other='Georg'))
   The story of Bill, Manfred, and Georg.

Si tiene una cadena de caracteres de formato realmente larga que no
desea dividir, sería bueno si pudiera hacer referencia a las variables
que se formatearán por nombre en lugar de por posición. Esto se puede
hacer simplemente pasando el diccionario y usando corchetes "'[]'"
para acceder a las claves.

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
   ...       'Dcab: {0[Dcab]:d}'.format(table))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

Esto se podría hacer, también, pasando el diccionario "table" como
argumentos por palabra clave con la notación '**'.

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

This is particularly useful in combination with the built-in function
"vars()", which returns a dictionary containing all local variables:

   >>> table = {k: str(v) for k, v in vars().items()}
   >>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
   >>> print(message.format(**table))
   __name__: __main__; __doc__: None; __package__: None; __loader__: ...

Como ejemplo, las siguientes líneas producen un conjunto ordenado de
columnas que dan enteros y sus cuadrados y cubos:

   >>> for x in range(1, 11):
   ...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

Para una completa descripción del formateo de cadenas con
"str.format()", ver Custom string formatting.

### 7.1.3. Formateo manual de cadenas

Aquí está la misma tabla de cuadrados y cubos, formateados
manualmente:

   >>> for x in range(1, 11):
   ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
   ...     # Note use of 'end' on previous line
   ...     print(repr(x*x*x).rjust(4))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

(Nótese que el espacio existente entre cada columna es añadido debido
a como funciona "print()": siempre añade espacios entre sus
argumentos.)

El método "str.rjust()" de los objetos cadena justifica a la derecha
en un campo de anchura predeterminada rellenando con espacios a la
izquierda. Métodos similares a este son "str.ljust()" y
"str.center()". Estos métodos no escriben nada, simplemente retornan
una nueva cadena. Si la cadena de entrada es demasiado larga no la
truncarán sino que la retornarán sin cambios; esto desordenará la
disposición de la columna que es, normalmente, mejor que la
alternativa, la cual podría falsear un valor. (Si realmente deseas
truncar siempre puedes añadir una operación de rebanado, como en
"x.ljust(n)[:n]".)

Hay otro método, "str.zfill()", el cual rellena una cadena numérica a
la izquierda con ceros. Entiende signos positivos y negativos:

   >>> '12'.zfill(5)
   '00012'
   >>> '-3.14'.zfill(7)
   '-003.14'
   >>> '3.14159265359'.zfill(5)
   '3.14159265359'

### 7.1.4. Viejo formateo de cadenas

The % operator (modulo) can also be used for string formatting. Given
"format % values" (where *format* is a string), "%" conversion
specifications in *format* are replaced with zero or more elements of
*values*. This operation is commonly known as string interpolation.
For example:

   >>> import math
   >>> print('The value of pi is approximately %5.3f.' % math.pi)
   The value of pi is approximately 3.142.

Podés encontrar más información en la sección Formateo de cadenas al
estilo *printf*.

## 7.2. Leyendo y escribiendo archivos

La función "open()" retorna un *file object*, y se usa normalmente con
dos argumentos posicionales y un argumento nombrado:
"open(nombre_de_archivo, modo, encoding=None)"

   >>> f = open('workfile', 'w', encoding="utf-8")

El primer argumento es una cadena que contiene el nombre del fichero.
El segundo argumento es otra cadena que contiene unos pocos caracteres
describiendo la forma en que el fichero será usado. *mode* puede ser
"'r'" cuando el fichero solo se leerá, "'w'" para solo escritura (un
fichero existente con el mismo nombre se borrará) y "'a'" abre el
fichero para agregar; cualquier dato que se escribe en el fichero se
añade automáticamente al final. "'r+'" abre el fichero tanto para
lectura como para escritura. El argumento *mode* es opcional; se asume
que se usará "'r'" si se omite.

Normalmente, los ficheros se abren en *modo texto*, es decir, se leen
y escriben cadenas desde y hacia el fichero, que están codificadas en
una *codificación* específica. Si no se especifica *codificación*, el
valor por defecto depende de la plataforma (véase "open()"). Dado que
UTF-8 es el estándar moderno de facto, se recomienda
"encoding="utf-8"" a menos que sepa que necesita usar una codificación
diferente. Añadiendo "'b'" al modo se abre el fichero en *modo
binario*. Los datos en modo binario se leen y escriben como objetos
"bytes". No se puede especificar *codificación* al abrir un fichero en
modo binario.

Cuando se lee en modo texto, por defecto se convierten los fin de
lineas que son específicos a las plataformas ("\n" en Unix, "\r\n" en
Windows) a solamente "\n". Cuando se escribe en modo texto, por
defecto se convierten los "\n" a los fin de linea específicos de la
plataforma. Este cambio automático está bien para archivos de texto,
pero corrompería datos binarios como los de archivos "JPEG" o "EXE".
Asegúrese de usar modo binario cuando lea y escriba tales archivos.

Es una buena práctica usar la declaración "with" cuando manejamos
objetos archivo. Tiene la ventaja de que el archivo es cerrado
apropiadamente luego de que el bloque termina, incluso si se generó
una excepción. También es mucho más corto que escribir los
equivalentes bloques "try"-"finally"

   >>> with open('workfile', encoding="utf-8") as f:
   ...     read_data = f.read()

   >>> # We can check that the file has been automatically closed.
   >>> f.closed
   True

Si no está utilizando la palabra clave "with", entonces debe llamar a
"f.close()" para cerrar el archivo y liberar inmediatamente los
recursos del sistema utilizados por él.

Advertencia:

  Llamar a "f.write()" sin usar la palabra clave "with" o sin llamar a
  "f.close()" **podría** dar como resultado que los argumentos de
  "f.write()" no se escriban completamente en disco, incluso si el
  programa se termina correctamente.

Después de que un objeto de archivo es cerrado, ya sea por "with" o
llamando a "f.close()", intentar volver a utilizarlo fallará
automáticamente:

   >>> f.close()
   >>> f.read()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: I/O operation on closed file.

### 7.2.1. Métodos de los objetos Archivo

El resto de los ejemplos en esta sección asumirán que ya se creó un
objeto archivo llamado "f".

Para leer el contenido de una archivo utiliza "f.read(size)", el cual
lee alguna cantidad de datos y los retorna como una cadena (en modo
texto) o un objeto de bytes (en modo binario). *size* es un argumento
numérico opcional. Cuando se omite *size* o es negativo, el contenido
entero del archivo será leído y retornado; es tu problema si el
archivo es el doble de grande que la memoria de tu máquina. De otra
manera, son leídos y retornados como máximo *size* caracteres (en modo
texto) o *size* bytes (en modo binario). Si se alcanzó el fin del
archivo, "f.read()" retornará una cadena vacía ("''").

   >>> f.read()
   'This is the entire file.\n'
   >>> f.read()
   ''

"f.readline()" lee una sola linea del archivo; el carácter de fin de
linea ("\n") se deja al final de la cadena, y sólo se omite en la
última linea del archivo si el mismo no termina en un fin de linea.
Esto hace que el valor de retorno no sea ambiguo; si "f.readline()"
retorna una cadena vacía, es que se alcanzó el fin del archivo,
mientras que una linea en blanco es representada por "'\n'", una
cadena conteniendo sólo un único fin de linea.

   >>> f.readline()
   'This is the first line of the file.\n'
   >>> f.readline()
   'Second line of the file\n'
   >>> f.readline()
   ''

Para leer líneas de un archivo, puedes iterar sobre el objeto archivo.
Esto es eficiente en memoria, rápido, y conduce a un código más
simple:

   >>> for line in f:
   ...     print(line, end='')
   ...
   This is the first line of the file.
   Second line of the file

Si querés leer todas las líneas de un archivo en una lista también
podés usar "list(f)" o "f.readlines()".

"f.write(cadena)" escribe el contenido de la *cadena* al archivo,
retornando la cantidad de caracteres escritos.

   >>> f.write('This is a test\n')
   15

Otros tipos de objetos necesitan ser convertidos -- tanto a una cadena
(en modo texto) o a un objeto de bytes (en modo binario) -- antes de
escribirlos:

   >>> value = ('the answer', 42)
   >>> s = str(value)  # convert the tuple to string
   >>> f.write(s)
   18

"f.tell()" retorna un entero que indica la posición actual en el
archivo representada como número de bytes desde el comienzo del
archivo en modo binario y un número opaco en modo texto.

Para cambiar la posición del objeto archivo, utiliza "f.seek(offset,
whence)". La posición es calculada agregando el *offset* a un punto de
referencia; el punto de referencia se selecciona del argumento
*whence*. Un valor *whence* de 0 mide desde el comienzo del archivo, 1
usa la posición actual del archivo, y 2 usa el fin del archivo como
punto de referencia.  *whence* puede omitirse, el valor por defecto es
0, usando el comienzo del archivo como punto de referencia.

   >>> f = open('workfile', 'rb+')
   >>> f.write(b'0123456789abcdef')
   16
   >>> f.seek(5)      # Go to the 6th byte in the file
   5
   >>> f.read(1)
   b'5'
   >>> f.seek(-3, 2)  # Go to the 3rd byte before the end
   13
   >>> f.read(1)
   b'd'

En los archivos de texto (aquellos que se abrieron sin una "b" en el
modo), se permiten solamente desplazamientos con "seek" relativos al
comienzo (con la excepción de ir justo al final con "seek(0, 2)") y
los únicos valores de *desplazamiento* válidos son aquellos retornados
por "f.tell()", o cero. Cualquier otro valor de *desplazamiento*
produce un comportamiento indefinido.

Los objetos archivo tienen algunos métodos más, como "isatty()" y
"truncate()" que son usados menos frecuentemente; consultá la
Referencia de la Biblioteca para una guía completa sobre los objetos
archivo.

### 7.2.2. Guardar datos estructurados con "json"

Las cadenas pueden fácilmente escribirse y leerse de un archivo. Los
números toman algo más de esfuerzo, ya que el método "read()" sólo
retorna cadenas, que tendrán que ser pasadas a una función como
"int()", que toma una cadena como "'123'" y retorna su valor numérico
123. Sin embargo, cuando querés guardar tipos de datos más complejos
como listas, diccionarios, o instancias de clases, las cosas se ponen
más complicadas.

En lugar de tener a los usuarios constantemente escribiendo y
debugueando código para guardar tipos de datos complicados, Python te
permite usar el popular formato intercambiable de datos llamado JSON
(JavaScript Object Notation). El módulo estándar llamado "json" puede
tomar datos de Python con una jerarquía, y convertirlo a
representaciones de cadena de caracteres; este proceso es llamado
*serialización*. Reconstruir los datos desde la representación de
cadena de caracteres es llamado *deserialización*. Entre serialización
y deserialización, la cadena de caracteres representando el objeto
quizás haya sido guardado en un archivo o datos, o enviado a una
máquina distante por una conexión de red.

Nota:

  El formato JSON es comúnmente usado por aplicaciones modernas para
  permitir el intercambio de datos. Muchos programadores ya están
  familiarizados con él, lo cual lo convierte en una buena opción para
  la interoperabilidad.

Si tienes un objeto "x", puedes ver su representación JSON con una
simple línea de código:

   >>> import json
   >>> x = [1, 'simple', 'list']
   >>> json.dumps(x)
   '[1, "simple", "list"]'

Otra variante de la función "dumps()", llamada "dump()", simplemente
serializa el objeto a un *archivo de texto*. Así que, si "f" es un
objeto *archivo de texto* abierto para escritura, podemos hacer:

   json.dump(x, f)

Para decodificar un objeto nuevamente, si "f" es un objeto *binary
file* o *text file* que fue abierto para lectura:

   x = json.load(f)

Nota:

  Los archivos JSON deben estar codificados en UTF-8. Utilice
  "encoding="utf-8"" al abrir un archivo JSON como *text file* tanto
  para lectura como para escritura.

La simple técnica de serialización puede manejar listas y
diccionarios, pero serializar instancias de clases arbitrarias en JSON
requiere un poco de esfuerzo extra. La referencia del módulo "json"
contiene una explicación de esto.

Ver también:

  "pickle" - El módulo *pickle*

  Contrariamente a JSON, *pickle* es un protocolo que permite la
  serialización de objetos Python arbitrariamente complejos. Como tal,
  es específico de Python y no se puede utilizar para comunicarse con
  aplicaciones escritas en otros lenguajes. También es inseguro de
  forma predeterminada: deserializar los datos de *pickle* procedentes
  de un origen que no es de confianza puede ejecutar código
  arbitrario, si los datos fueron creados por un atacante experto.
