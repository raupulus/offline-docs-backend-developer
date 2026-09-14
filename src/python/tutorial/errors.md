---
title: 8. Errores y excepciones
source_url: https://docs.python.org/es/3
source_path: tutorial/errors.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4910
---

# 8. Errores y excepciones

Hasta ahora los mensajes de error apenas habían sido mencionados, pero
si has probado los ejemplos anteriores probablemente hayas visto
algunos.  Hay (al menos) dos tipos diferentes de errores: *errores de
sintaxis* y *excepciones*.

## 8.1. Errores de sintaxis

Los errores de sintaxis, también conocidos como errores de
interpretación, son quizás el tipo de queja más común que tenés cuando
todavía estás aprendiendo Python:

   >>> while True print('Hello world')
     File "<stdin>", line 1
       while True print('Hello world')
                  ^^^^^
   SyntaxError: invalid syntax

The parser repeats the offending line and displays little arrows
pointing at the place where the error was detected.  Note that this is
not always the place that needs to be fixed.  In the example, the
error is detected at the function "print()", since a colon ("':'") is
missing just before it.

The file name ("<stdin>" in our example) and line number are printed
so you know where to look in case the input came from a file.

## 8.2. Excepciones

Incluso si una declaración o expresión es sintácticamente correcta,
puede generar un error cuando se intenta ejecutar.  Los errores
detectados durante la ejecución se llaman *excepciones*, y no son
incondicionalmente fatales: pronto aprenderás a gestionarlos en
programas Python.  Sin embargo, la mayoría de las excepciones no son
gestionadas por el código, y resultan en mensajes de error como los
mostrados aquí:

   >>> 10 * (1/0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       10 * (1/0)
             ~^~
   ZeroDivisionError: division by zero
   >>> 4 + spam*3
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       4 + spam*3
           ^^^^
   NameError: name 'spam' is not defined
   >>> '2' + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       '2' + 2
       ~~~~^~~
   TypeError: can only concatenate str (not "int") to str

La última línea de los mensajes de error indica qué ha sucedido.  Hay
excepciones de diferentes tipos, y el tipo se imprime como parte del
mensaje: los tipos en el ejemplo son: "ZeroDivisionError", "NameError"
y "TypeError".  La cadena mostrada como tipo de la excepción es el
nombre de la excepción predefinida que ha ocurrido.  Esto es válido
para todas las excepciones predefinidas del intérprete, pero no tiene
por que ser así para excepciones definidas por el usuario (aunque es
una convención útil).  Los nombres de las excepciones estándar son
identificadores incorporados al intérprete (no son palabras clave
reservadas).

El resto de la línea provee información basado en el tipo de la
excepción y qué la causó.

La parte anterior del mensaje de error muestra el contexto donde
ocurrió la excepción, en forma de seguimiento de pila. En general,
contiene un seguimiento de pila que enumera las líneas de origen; sin
embargo, no mostrará las líneas leídas desde la entrada estándar.

Excepciones incorporadas lista las excepciones predefinidas y sus
significados.

## 8.3. Gestionando excepciones

Es posible escribir programas que gestionen determinadas excepciones.
Véase el siguiente ejemplo, que le pide al usuario una entrada hasta
que ingrese un entero válido, pero permite al usuario interrumpir el
programa (usando "Control"-"C" o lo que soporte el sistema operativo);
nótese que una interrupción generada por el usuario es señalizada
generando la excepción "KeyboardInterrupt".

   >>> while True:
   ...     try:
   ...         x = int(input("Please enter a number: "))
   ...         break
   ...     except ValueError:
   ...         print("Oops!  That was no valid number.  Try again...")
   ...

La sentencia "try" funciona de la siguiente manera.

* Primero, se ejecuta la cláusula *try* (la(s) linea(s) entre las
  palabras reservadas "try" y la "except").

* Si no ocurre ninguna excepción, la cláusula *except* se omite y la
  ejecución de la cláusula "try" finaliza.

* Si ocurre una excepción durante la ejecución de la cláusula "try",
  se omite el resto de la cláusula. Luego, si su tipo coincide con la
  excepción nombrada después de la palabra clave "except", se ejecuta
  la *cláusula except*, y luego la ejecución continúa después del
  bloque try/except.

* If an exception occurs which does not match the exception named in
  the *except clause*, it is passed on to outer "try" statements; if
  no handler is found, it is an *unhandled exception* and execution
  stops with an error message.

A "try" statement may have more than one *except clause*, to specify
handlers for different exceptions.  At most one handler will be
executed. Handlers only handle exceptions that occur in the
corresponding *try clause*, not in other handlers of the same "try"
statement.  An *except clause* may name multiple exceptions, for
example:

   ... except RuntimeError, TypeError, NameError:
   ...     pass

A class in an "except" clause matches exceptions which are instances
of the class itself or one of its derived classes (but not the other
way around --- an *except clause* listing a derived class does not
match instances of its base classes). For example, the following code
will print B, C, D in that order:

   class B(Exception):
       pass

   class C(B):
       pass

   class D(C):
       pass

   for cls in [B, C, D]:
       try:
           raise cls()
       except D:
           print("D")
       except C:
           print("C")
       except B:
           print("B")

Nótese que si las *cláusulas except* estuvieran invertidas (con
"except B" primero), habría impreso B, B, B --- se usa la primera
*cláusula except* coincidente.

Cuando ocurre una excepción, puede tener un valor asociado, también
conocido como el *argumento* de la excepción.  La presencia y el tipo
de argumento depende del tipo de excepción.

La *cláusula except* puede especificar una variable después del nombre
de la excepción. La variable está ligada a la instancia de la
excepción, que normalmente tiene un atributo "args" que almacena los
argumentos. Por conveniencia, los tipos de excepción incorporados
definen "__str__()" para imprimir todos los argumentos sin acceder
explícitamente a ".args".

   >>> try:
   ...     raise Exception('spam', 'eggs')
   ... except Exception as inst:
   ...     print(type(inst))    # the exception type
   ...     print(inst.args)     # arguments stored in .args
   ...     print(inst)          # __str__ allows args to be printed directly,
   ...                          # but may be overridden in exception subclasses
   ...     x, y = inst.args     # unpack args
   ...     print('x =', x)
   ...     print('y =', y)
   ...
   <class 'Exception'>
   ('spam', 'eggs')
   ('spam', 'eggs')
   x = spam
   y = eggs

La salida "__str__()" de la excepción se imprime como la última parte
('detalle') del mensaje para las excepciones no gestionadas.

"BaseException" es la clase base común de todas las excepciones. Una
de sus subclases, "Exception", es la clase base de todas las
excepciones no fatales. Las excepciones que no son subclases de
"Exception" no se suelen manejar, porque se utilizan para indicar que
el programa debe terminar. Entre ellas se incluyen "SystemExit", que
es lanzada por "sys.exit()" y "KeyboardInterrupt", que se lanza cuando
un usuario desea interrumpir el programa.

"Exception" se puede utilizar como un comodín que atrapa (casi) todo.
Sin embargo, es una buena práctica ser lo más específico posible con
los tipos de excepciones que pretendemos manejar, y permitir que
cualquier excepción inesperada se propague.

El patrón más común para gestionar "Exception" es imprimir o registrar
la excepción y luego volver a re-lanzarla (permitiendo a un llamador
manejar la excepción también):

   import sys

   try:
       f = open('myfile.txt')
       s = f.readline()
       i = int(s.strip())
   except OSError as err:
       print("OS error:", err)
   except ValueError:
       print("Could not convert data to an integer.")
   except Exception as err:
       print(f"Unexpected {err=}, {type(err)=}")
       raise

La declaración "try" ... "except" tiene una *cláusula else* opcional,
que, cuando está presente, debe seguir todas las *cláusulas except*.
Es útil para el código que debe ejecutarse si la *cláusula try* no
lanza una excepción. Por ejemplo:

   for arg in sys.argv[1:]:
       try:
           f = open(arg, 'r')
       except OSError:
           print('cannot open', arg)
       else:
           print(arg, 'has', len(f.readlines()), 'lines')
           f.close()

El uso de la cláusula "else" es mejor que agregar código adicional en
la cláusula "try" porque evita capturar accidentalmente una excepción
que no fue generada por el código que está protegido por la
declaración "try" ... "except".

Los gestores de excepciones no sólo gestionan excepciones que ocurren
inmediatamente en la *cláusula try*, sino también aquellas que ocurren
dentro de funciones que son llamadas (incluso indirectamente) en la
*cláusula try*. Por ejemplo:

   >>> def this_fails():
   ...     x = 1/0
   ...
   >>> try:
   ...     this_fails()
   ... except ZeroDivisionError as err:
   ...     print('Handling run-time error:', err)
   ...
   Handling run-time error: division by zero

## 8.4. Lanzando excepciones

La declaración "raise" permite al programador forzar a que ocurra una
excepción específica.  Por ejemplo:

   >>> raise NameError('HiThere')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       raise NameError('HiThere')
   NameError: HiThere

El único argumento de "raise" indica la excepción a lanzar. Debe ser
una instancia de excepción o una clase de excepción (una clase que
derive de "BaseException", como "Exception" o una de sus subclases).
Si se pasa una clase de excepción, se instanciará implícitamente
llamando a su constructor sin argumentos:

   raise ValueError  # shorthand for 'raise ValueError()'

Si es necesario determinar si una excepción fue lanzada pero sin
intención de gestionarla, una versión simplificada de la instrucción
"raise" te permite relanzarla:

   >>> try:
   ...     raise NameError('HiThere')
   ... except NameError:
   ...     print('An exception flew by!')
   ...     raise
   ...
   An exception flew by!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise NameError('HiThere')
   NameError: HiThere

## 8.5. Encadenamiento de excepciones

Si se produce una excepción no gestionada dentro de una sección
"except", se le adjuntará la excepción que se está gestionando y se
incluirá en el mensaje de error:

   >>> try:
   ...     open("database.sqlite")
   ... except OSError:
   ...     raise RuntimeError("unable to handle error")
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       open("database.sqlite")
       ~~~~^^^^^^^^^^^^^^^^^^^
   FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError("unable to handle error")
   RuntimeError: unable to handle error

Para indicar que una excepción es consecuencia directa de otra, la
sentencia "raise" permite una cláusula opcional "from":

   # exc must be exception instance or None.
   raise RuntimeError from exc

Esto puede resultar útil cuando está transformando excepciones. Por
ejemplo:

   >>> def func():
   ...     raise ConnectionError
   ...
   >>> try:
   ...     func()
   ... except ConnectionError as exc:
   ...     raise RuntimeError('Failed to open database') from exc
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       func()
       ~~~~^^
     File "<stdin>", line 2, in func
   ConnectionError

   The above exception was the direct cause of the following exception:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError('Failed to open database') from exc
   RuntimeError: Failed to open database

También permite deshabilitar el encadenamiento automático de
excepciones utilizando el modismo "from None":

   >>> try:
   ...     open('database.sqlite')
   ... except OSError:
   ...     raise RuntimeError from None
   ...
   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError from None
   RuntimeError

Para obtener más información sobre la mecánica del encadenamiento,
consulte Excepciones incorporadas.

## 8.6. Excepciones definidas por el usuario

Los programas pueden nombrar sus propias excepciones creando una nueva
clase excepción (mirá Clases para más información sobre las clases de
Python).  Las excepciones, típicamente, deberán derivar de la clase
"Exception", directa o indirectamente.

Las clases de Excepción pueden ser definidas de la misma forma que
cualquier otra clase, pero es habitual mantenerlas lo más simples
posible, a menudo ofreciendo solo un número de atributos con
información sobre el error que leerán los gestores de la excepción.

La mayoría de las excepciones se definen con nombres acabados en
"Error", de manera similar a la nomenclatura de las excepciones
estándar.

Muchos módulos estándar definen sus propias excepciones para reportar
errores que pueden ocurrir en funciones propias.

## 8.7. Definiendo acciones de limpieza

La declaración "try" tiene otra cláusula opcional cuyo propósito es
definir acciones de limpieza que serán ejecutadas bajo ciertas
circunstancias. Por ejemplo:

   >>> try:
   ...     raise KeyboardInterrupt
   ... finally:
   ...     print('Goodbye, world!')
   ...
   Goodbye, world!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise KeyboardInterrupt
   KeyboardInterrupt

Si una cláusula "finally" está presente, el bloque "finally" se
ejecutará al final antes de que todo el bloque "try" se complete. La
cláusula "finally" se ejecuta independientemente de que la cláusula
"try" produzca o no una excepción. Los siguientes puntos explican
casos más complejos en los que se produce una excepción:

* Si ocurre una excepción durante la ejecución de la cláusula "try",
  la excepción podría ser gestionada por una cláusula "except". Si la
  excepción no es gestionada por una cláusula "except", la excepción
  es relanzada después de que se ejecute el bloque de la cláusula
  "finally".

* Podría aparecer una excepción durante la ejecución de una cláusula
  "except" o "else". De nuevo, la excepción será relanzada después de
  que el bloque de la cláusula "finally" se ejecute.

* If the "finally" clause executes a "break", "continue" or "return"
  statement, exceptions are not re-raised. This can be confusing and
  is therefore discouraged. From version 3.14 the compiler emits a
  "SyntaxWarning" for it (see **PEP 765**).

* Si el bloque "try" llega a una sentencia "break", "continue" o
  "return", la cláusula "finally" se ejecutará justo antes de la
  ejecución de dicha sentencia.

* If a "finally" clause includes a "return" statement, the returned
  value will be the one from the "finally" clause's "return"
  statement, not the value from the "try" clause's "return" statement.
  This can be confusing and is therefore discouraged. From version
  3.14 the compiler emits a "SyntaxWarning" for it (see **PEP 765**).

Por ejemplo:

   >>> def bool_return():
   ...     try:
   ...         return True
   ...     finally:
   ...         return False
   ...
   >>> bool_return()
   False

Un ejemplo más complicado:

   >>> def divide(x, y):
   ...     try:
   ...         result = x / y
   ...     except ZeroDivisionError:
   ...         print("division by zero!")
   ...     else:
   ...         print("result is", result)
   ...     finally:
   ...         print("executing finally clause")
   ...
   >>> divide(2, 1)
   result is 2.0
   executing finally clause
   >>> divide(2, 0)
   division by zero!
   executing finally clause
   >>> divide("2", "1")
   executing finally clause
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       divide("2", "1")
       ~~~~~~^^^^^^^^^^
     File "<stdin>", line 3, in divide
       result = x / y
                ~~^~~
   TypeError: unsupported operand type(s) for /: 'str' and 'str'

Como se puede ver, la cláusula "finally" siempre se ejecuta.  La
excepción "TypeError" lanzada al dividir dos cadenas de texto no es
gestionado por la cláusula "except" y por lo tanto es relanzada luego
de que se ejecuta la cláusula "finally".

En aplicaciones reales, la cláusula "finally" es útil para liberar
recursos externos (como archivos o conexiones de red), sin importar si
el uso del recurso fue exitoso.

## 8.8. Acciones predefinidas de limpieza

Algunos objetos definen acciones de limpieza estándar para llevar a
cabo cuando el objeto ya no necesario, independientemente de que las
operaciones sobre el objeto hayan sido exitosas o no. Véase el
siguiente ejemplo, que intenta abrir un archivo e imprimir su
contenido en la pantalla.

   for line in open("myfile.txt"):
       print(line, end="")

El problema con este código es que deja el archivo abierto por un
periodo de tiempo indeterminado luego de que esta parte termine de
ejecutarse.  Esto no es un problema en *scripts* simples, pero puede
ser un problema en aplicaciones más grandes.  La declaración "with"
permite que los objetos como archivos sean usados de una forma que
asegure que siempre se los libera rápido y en forma correcta.:

   with open("myfile.txt") as f:
       for line in f:
           print(line, end="")

Una vez que la declaración se ejecuta, el fichero *f* siempre se
cierra, incluso si aparece algún error durante el procesado de las
líneas.  Los objetos que, como los ficheros, posean acciones
predefinidas de limpieza lo indicarán en su documentación.

## 8.9. Lanzando y gestionando múltiples excepciones no relacionadas

Hay situaciones en las que es necesario informar de varias excepciones
que se han producido. Este es a menudo el caso en los marcos de
concurrencia, cuando varias tareas pueden haber fallado en paralelo,
pero también hay otros casos de uso en los que es deseable continuar
la ejecución y recoger múltiples errores en lugar de lanzar la primera
excepción.

El incorporado "ExceptionGroup" envuelve una lista de instancias de
excepción para que puedan ser lanzadas juntas. Es una excepción en sí
misma, por lo que puede capturarse como cualquier otra excepción.

   >>> def f():
   ...     excs = [OSError('error 1'), SystemError('error 2')]
   ...     raise ExceptionGroup('there were problems', excs)
   ...
   >>> f()
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 1, in <module>
     |     f()
     |     ~^^
     |   File "<stdin>", line 3, in f
     |     raise ExceptionGroup('there were problems', excs)
     | ExceptionGroup: there were problems (2 sub-exceptions)
     +-+---------------- 1 ----------------
       | OSError: error 1
       +---------------- 2 ----------------
       | SystemError: error 2
       +------------------------------------
   >>> try:
   ...     f()
   ... except Exception as e:
   ...     print(f'caught {type(e)}: {e}')
   ...
   caught <class 'ExceptionGroup'>: there were problems (2 sub-exceptions)
   >>>

Utilizando "except*" en lugar de "except", podemos manejar
selectivamente sólo las excepciones del grupo que coincidan con un
determinado tipo. En el siguiente ejemplo, que muestra un grupo de
excepciones anidado, cada cláusula "except*" extrae del grupo las
excepciones de un tipo determinado, mientras que deja que el resto de
excepciones se propaguen a otras cláusulas y, finalmente, se vuelvan a
lanzar.

   >>> def f():
   ...     raise ExceptionGroup(
   ...         "group1",
   ...         [
   ...             OSError(1),
   ...             SystemError(2),
   ...             ExceptionGroup(
   ...                 "group2",
   ...                 [
   ...                     OSError(3),
   ...                     RecursionError(4)
   ...                 ]
   ...             )
   ...         ]
   ...     )
   ...
   >>> try:
   ...     f()
   ... except* OSError as e:
   ...     print("There were OSErrors")
   ... except* SystemError as e:
   ...     print("There were SystemErrors")
   ...
   There were OSErrors
   There were SystemErrors
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 2, in <module>
     |     f()
     |     ~^^
     |   File "<stdin>", line 2, in f
     |     raise ExceptionGroup(
     |     ...<12 lines>...
     |     )
     | ExceptionGroup: group1 (1 sub-exception)
     +-+---------------- 1 ----------------
       | ExceptionGroup: group2 (1 sub-exception)
       +-+---------------- 1 ----------------
         | RecursionError: 4
         +------------------------------------
   >>>

Tenga en cuenta que las excepciones anidadas en un grupo de
excepciones deben ser instancias, no tipos. Esto se debe a que en la
práctica las excepciones serían típicamente las que ya han sido
planteadas y capturadas por el programa, siguiendo el siguiente
patrón:

   >>> excs = []
   ... for test in tests:
   ...     try:
   ...         test.run()
   ...     except Exception as e:
   ...         excs.append(e)
   ...
   >>> if excs:
   ...    raise ExceptionGroup("Test Failures", excs)
   ...

## 8.10. Enriqueciendo excepciones con notas

Cuando se crea una excepción para ser lanzada, normalmente se
inicializa con información que describe el error que se ha producido.
Hay casos en los que es útil añadir información después de que la
excepción haya sido capturada. Para este propósito, las excepciones
tienen un método "add_note(note)" que acepta una cadena y la añade a
la lista de notas de la excepción. La representación estándar del
rastreo incluye todas las notas, en el orden en que fueron añadidas,
después de la excepción.

   >>> try:
   ...     raise TypeError('bad type')
   ... except Exception as e:
   ...     e.add_note('Add some information')
   ...     e.add_note('Add some more information')
   ...     raise
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise TypeError('bad type')
   TypeError: bad type
   Add some information
   Add some more information
   >>>

Por ejemplo, al recopilar excepciones en un grupo de excepciones, es
posible que queramos añadir información de contexto para los errores
individuales. A continuación, cada excepción del grupo tiene una nota
que indica cuándo se ha producido ese error.

   >>> def f():
   ...     raise OSError('operation failed')
   ...
   >>> excs = []
   >>> for i in range(3):
   ...     try:
   ...         f()
   ...     except Exception as e:
   ...         e.add_note(f'Happened in Iteration {i+1}')
   ...         excs.append(e)
   ...
   >>> raise ExceptionGroup('We have some problems', excs)
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 1, in <module>
     |     raise ExceptionGroup('We have some problems', excs)
     | ExceptionGroup: We have some problems (3 sub-exceptions)
     +-+---------------- 1 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operation failed')
       | OSError: operation failed
       | Happened in Iteration 1
       +---------------- 2 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operation failed')
       | OSError: operation failed
       | Happened in Iteration 2
       +---------------- 3 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operation failed')
       | OSError: operation failed
       | Happened in Iteration 3
       +------------------------------------
   >>>
