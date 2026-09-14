---
title: '"shlex" --- Simple lexical analysis'
source_url: https://docs.python.org/es/3
source_path: library/shlex.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3770
---

# "shlex" --- Simple lexical analysis

**Código fuente:** Lib/shlex.py

======================================================================

La clase "shlex" facilita la escritura de analizadores léxicos para
sintaxis simples que se parecen al intérprete de comandos de Unix.
Esto será a menudo útil para escribir pequeños lenguajes, (por
ejemplo, en archivos de control para aplicaciones Python) o para
analizar cadenas de texto citadas.

The "shlex" module defines the following functions:

shlex.split(s, comments=False, posix=True)

   Divide la cadena de caracteres *s* usando una sintaxis similar a la
   de un intérprete de comandos.  Si *comments* es "False" (por
   defecto), el análisis de los comentarios en la cadena de caracteres
   dada sera deshabilitada (estableciendo el atributo "commenters" de
   la instancia "shlex" a la cadena de caracteres vacía). Esta función
   trabaja en modo POSIX por defecto, pero utiliza el modo non-POSIX
   si el argumento *posix* es falso.

   Distinto en la versión 3.12: Pasar "None" para el argumento *s*
   ahora lanza una excepción, en lugar de leer "sys.stdin".

shlex.join(split_command)

   Concatena los tokens de la lista *split_command* y retorna una
   cadena. Esta función es la inversa de "split()".

   >>> from shlex import join
   >>> print(join(['echo', '-n', 'Multiple words']))
   echo -n 'Multiple words'

   El valor retornado se escapa del intérprete de comandos para
   protegerlo contra vulnerabilidades de inyección (consulte
   "quote()").

   Added in version 3.8.

shlex.quote(s)

   Retorna una versión con escape del intérprete de comandos de la
   cadena *s*.  El valor retornado es una cadena que se puede usar de
   forma segura como un token en un intérprete de línea de comandos,
   para los casos en los que no se puede usar una lista.

   Advertencia:

     El módulo "shlex" **solo está diseñado para los intérpretes de
     comandos UNIX**.No se garantiza que la función "quote()" sea
     correcta en shells no compatibles con POSIX o shells de otros
     sistemas operativos como Windows. La ejecución de comandos
     citados por este módulo en tales shells puede abrir la
     posibilidad de una vulnerabilidad de inyección de
     comandos.Considere el uso de funciones que pasen argumentos
     mediante listas tal como "subprocess.run()" con "shell=False".

   Este idioma sería inseguro:

   >>> filename = 'somefile; rm -rf ~'
   >>> command = 'ls -l {}'.format(filename)
   >>> print(command)  # executed by a shell: boom!
   ls -l somefile; rm -rf ~

   "quote()" te permite tapar el agujero de seguridad:

   >>> from shlex import quote
   >>> command = 'ls -l {}'.format(quote(filename))
   >>> print(command)
   ls -l 'somefile; rm -rf ~'
   >>> remote_command = 'ssh home {}'.format(quote(command))
   >>> print(remote_command)
   ssh home 'ls -l '"'"'somefile; rm -rf ~'"'"''

   La cita es compatible con los intérpretes de comandos UNIX y con
   "split()":

   >>> from shlex import split
   >>> remote_command = split(remote_command)
   >>> remote_command
   ['ssh', 'home', "ls -l 'somefile; rm -rf ~'"]
   >>> command = split(remote_command[-1])
   >>> command
   ['ls', '-l', 'somefile; rm -rf ~']

   Added in version 3.3.

The "shlex" module defines the following class:

class shlex.shlex(instream=None, infile=None, posix=False, punctuation_chars=False)

   Una instancia o instancia de la subclase "shlex" es un objeto de
   analizador léxico.  El argumento de inicialización, si está
   presente, especifica de dónde leer caracteres.  Debe ser un objeto
   similar a un archivo/stream con los métodos "read()" y "readline()"
   o una cadena de caracteres.  Si no se da ningún argumento, la
   entrada se tomará de "sys.stdin". El segundo argumento opcional es
   una cadena de nombre de archivo, que establece el valor inicial del
   atributo "infile".  Si el argumento *instream* es omitido o es
   igual a "sys.stdin", este segundo argumento tiene como valor
   predeterminado "stdin".  El argumento *posix* define el modo
   operativo: cuando *posix* no es true (predeterminado), la instancia
   "shlex" funcionará en modo de compatibilidad.  Cuando se opera en
   modo POSIX, "shlex" intentará estar lo más cerca posible de las
   reglas de análisis de el intérprete de comandos POSIX.  El
   argumento *punctuation_chars* proporciona una manera de hacer que
   el comportamiento sea aún más cercano a la forma en que se analizan
   los intérpretes de comandos reales.  Esto puede tomar una serie de
   valores: el valor predeterminado, "False", conserva el
   comportamiento visto en Python 3.5 y versiones anteriores.  Si se
   establece en "True", se cambia el análisis de los caracteres
   "();<>|&": cualquier ejecución de estos caracteres (caracteres
   considerados de puntuación) se retorna como un único token.  Si se
   establece en una cadena de caracteres no vacía, esos caracteres se
   utilizarán como caracteres de puntuación.  Los caracteres del
   atributo "wordchars" que aparecen en *punctuation_chars* se
   eliminarán de "wordchars".  Consulte Compatibilidad mejorada con
   intérprete de comandos para obtener más información.
   *punctuation_chars* solo se puede establecer en la creación de la
   instancia "shlex" y no se puede modificar más adelante.

   Distinto en la versión 3.6: Se añadió el parámetro
   *punctuation_chars*.

Ver también:

  Módulo "configparser"
     Analizador de archivos de configuración similares a los archivos
     ".ini" de Windows.

## objetos "shlex"

Una instancia "shlex" tiene los siguientes métodos:

shlex.get_token()

   Retorna un token.  Si los tokens han sido apiladas usando
   "push_token()", saca una ficha de la pila.  De lo contrario, lee
   uno de la secuencia de entrada.  Si la lectura encuentra un fin de
   archivo inmediato, "eof" se retorna (la cadena de caracteres vacía
   ("''") en modo no-POSIX, y "None" en modo POSIX).

shlex.push_token(str)

   Coloca el argumento en la pila de tokens.

shlex.read_token()

   Lee un token sin procesar. Ignora la pila de retroceso y no
   interpreta las peticiones de la fuente.  (Este no es normalmente un
   punto de entrada útil, y está documentado aquí sólo para
   completarlo.)

shlex.sourcehook(filename)

   Cuando "shlex" detecta una petición de fuente (ver "source" abajo)
   este método recibe el siguiente token como argumento, y se espera
   que retorne una tupla que consista en un nombre de archivo y un
   archivo abierto como objeto.

   Normalmente, este método primero elimina las comillas del
   argumento.  Si el resultado es un nombre de ruta absoluto, o no
   había ninguna solicitud de origen anterior en vigor, o el origen
   anterior era una secuencia (como "sys.stdin"), el resultado se deja
   solo.  De lo contrario, si el resultado es un nombre de ruta
   relativo, la parte del directorio del nombre del archivo se pone
   inmediatamente antes en la pila de inclusión de origen (este
   comportamiento es similar a la forma en que el preprocesador de C
   controla "#include "file.h"").

   El resultado de las manipulaciones se trata como un nombre de
   archivo y se retorna como el primer componente de la tupla, con
   "open()" llamado en él para producir el segundo componente. (Nota:
   esto es lo contrario del orden de los argumentos en la
   inicialización de instancia!)

   Este enlace se expone para que pueda usarlo para implementar rutas
   de búsqueda de directorios, adición de extensiones de archivo y
   otros trucos de espacios de nombres. No hay ningún enlace 'close'
   correspondiente, pero una instancia de "shlex" llamará el método
   "close()" de la secuencia de entrada de origen cuando retorna EOF.

   Para un control más explícito del apilamiento de código fuente,
   utilice los métodos "push_source()" y "pop_source()".

shlex.push_source(newstream, newfile=None)

   Inserta una secuencia de fuente de entrada en la pila de entrada.
   Si se especifica el argumento de nombre de archivo, más adelante
   estará disponible para su uso en mensajes de error.  Este es el
   mismo método utilizado internamente por el método "sourcehook()".

shlex.pop_source()

   Saca la última fuente de entrada de la pila de entrada. Este es el
   mismo método que el analizador léxico utiliza cuando llega al EOF
   en una secuencia de entrada apilada.

shlex.error_leader(infile=None, lineno=None)

   Este método genera un mensaje de error líder en el formato de una
   etiqueta de error del compilador de Unix C; el formato es "'"%s",
   line %d: '", donde el "%s" es reemplazado con el nombre del archivo
   fuente actual y el "%d" con el número de línea de entrada actual
   (los argumentos opcionales pueden ser usado para sobrescribir
   estos).

   This convenience is provided to encourage "shlex" users to generate
   error messages in the standard, parseable format understood by
   Emacs and other Unix tools.

Las instancias de las subclases "shlex" tienen algunas variables de
instancia pública que controlan el análisis léxico o pueden ser usadas
para la depuración:

shlex.commenters

   La cadena de caracteres que son reconocidos como comentarios de
   principiantes. Todos los caracteres desde el comentario
   principiante hasta el final de la línea son ignorados. Incluye sólo
   "'#'" por defecto.

shlex.wordchars

   La cadena de caracteres que se acumulará en tokens de varios
   caracteres.  Por defecto, incluye todos los alfanuméricos ASCII y
   el subrayado.  En el modo POSIX, los caracteres acentuados del
   conjunto Latin-1 también están incluidos.  Si "punctuation_chars"
   no está vacío, los caracteres "~-./*?=", que pueden aparecer en las
   especificaciones del nombre de archivo y en los parámetros de la
   línea de comandos, también se incluirán en este atributo, y
   cualquier carácter que aparezca en "punctuation_chars" será
   eliminado de "wordchars" si están presentes allí. Si
   "whitespace_split" se establece en "True", esto no tendrá ningún
   efecto.

shlex.whitespace

   Caracteres que serán considerados como espacio en blanco y
   salteados.  El espacio blanco limita los tokens.  Por defecto,
   incluye espacio, tabulación, salto de línea y retorno de carro.

shlex.escape

   Caracteres que serán considerados como de escape. Esto sólo se
   usará en el modo POSIX, e incluye sólo "'\'" por defecto.

shlex.quotes

   Los caracteres que serán considerados como citas de la cadena.  El
   token se acumula hasta que la misma cita se encuentra de nuevo
   (así, los diferentes tipos de citas se protegen entre sí como en el
   intérprete de comandos.) Por defecto, incluye ASCII comillas
   simples y dobles.

shlex.escapedquotes

   Caracteres en "quotes" que interpretarán los caracteres de escape
   definidos en "escape".  Esto sólo se usa en el modo POSIX, e
   incluye sólo "'"'" por defecto.

shlex.whitespace_split

   Si es "True", los tokens sólo se dividirán en espacios en blanco.
   Esto es útil, por ejemplo, para analizar las líneas de comando con
   "shlex", obteniendo los tokens de forma similar a los argumentos de
   el intérprete de comandos.  Cuando se utiliza en combinación con
   "puntuation_chars", los tokens se dividirán en espacios en blanco
   además de esos caracteres.

   Distinto en la versión 3.8: El atributo "puntuation_chars" se hizo
   compatible con el atributo "whitespace_split".

shlex.infile

   El nombre del archivo de entrada actual, como se estableció
   inicialmente al momento de la instanciación de la clase o apilado
   por solicitudes de fuente posteriores.  Puede ser útil examinar
   esto cuando se construyan mensajes de error.

shlex.instream

   El flujo de entrada del cual esta instancia "shlex" está leyendo
   caracteres.

shlex.source

   Este atributo es "None" por defecto.  Si le asignas una cadena, esa
   cadena será reconocida como una solicitud de inclusión a nivel
   léxico similar a la palabra clave "source" en varios intérpretes de
   comandos.  Es decir, el token inmediatamente siguiente se abrirá
   como un nombre de archivo y la entrada se tomará de ese flujo hasta
   EOF, en cuyo momento se llamará al método "close()" de ese flujo y
   la fuente de entrada se convertirá de nuevo en el flujo de entrada
   original.  Las peticiones de origen pueden ser apiladas a cualquier
   número de niveles de profundidad.

shlex.debug

   Si este atributo es numérico y "1" o más, una instancia "shlex"
   imprimirá una salida de progreso verboso en su comportamiento.  Si
   necesitas usar esto, puedes leer el código fuente del módulo para
   conocer los detalles.

shlex.lineno

   Numero de linea de fuente (conteo de las nuevas lineas vistas hasta
   ahora mas uno).

shlex.token

   El buffer de tokens.  Puede ser útil examinarlo cuando se capturan
   excepciones.

shlex.eof

   Token usado para determinar el final del archivo. Esto se ajustará
   a la cadena de caracteres vacía ("''"), en el modo no-POSIX, y a
   "None" en el modo POSIX.

shlex.punctuation_chars

   Una propiedad de sólo lectura. Caracteres que serán considerados
   como puntuación. Las series de caracteres de puntuación se
   retornarán como un único token. Sin embargo, tenga en cuenta que no
   se realizará ninguna comprobación de validez semántica: por
   ejemplo, '>>>' podría ser retornado como un token, aunque no sea
   reconocido como tal por los intérpretes de comandos.

   Added in version 3.6.

## Reglas de análisis

When operating in non-POSIX mode, "shlex" will try to obey the
following rules.

* Los caracteres entre comillas no son reconocidos dentro de las
  palabras ("Do"Not"Separate" es analizado como la única palabra
  "Do"Not"Separate");

* Los caracteres de escape no son reconocidos;

* El encerrar los caracteres entre comillas preserva el valor literal
  de todos los caracteres dentro de las comillas;

* Las comillas finales separan las palabras (""Do"Separate" es
  analizado como ""Do"" y "Separate");

* Si "whitepace_split" es "False", cualquier carácter que no sea
  declarado como un carácter de palabra, espacio en blanco, o una cita
  será retornado como un token de un solo carácter. Si es "True",
  "shlex" sólo dividirá las palabras en espacios en blanco;

* EOF es señalado con una cadena de caracteres vacía ("''");

* No es posible analizar cadenas de caracteres vacías, incluso si se
  citan.

When operating in POSIX mode, "shlex" will try to obey the following
parsing rules.

* Las comillas se eliminan y no separan las palabras
  (""Do"Not"Separate"" se analiza como la sola palabra
  "DoNotSeparate");

* Los caracteres de escape no citados (por ejemplo "'\'") conservan el
  valor literal del siguiente carácter que continua;

* Encerrar caracteres entre comillas que no forman parte de
  "escapedquotes" (por ejemplo, """") conservan el valor literal de
  todos los caracteres dentro de las comillas;

* Enclosing characters in quotes which are part of "escapedquotes"
  (e.g. "'"'") preserves the literal value of all characters within
  the quotes, with the exception of the characters mentioned in
  "escape".  The escape characters retain their special meaning only
  when followed by the quote in use, or the escape character itself.
  Otherwise the escape character will be considered a normal
  character.

* EOF es señalado con un valor "None";

* Se permiten cadenas de caracteres vacías entrecomilladas ("''").

## Compatibilidad mejorada con intérprete de comandos

Added in version 3.6.

La clase "shlex" provee compatibilidad con el análisis realizado por
los intérprete de comandos comunes de Unix como "bash", "dash" y "sh".
Para aprovechar esta compatibilidad, especifica el argumento
"punctuation_chars" en el constructor.  Esto por defecto es "False",
el cual conserva el comportamiento pre-3.6. Sin embargo, si se
establece como "True", entonces se cambia el análisis de los
caracteres "();<>|&": cualquier ejecución de estos caracteres se
retorna como un único token.  Mientras que esto se queda corto en un
analizador completo para los intérprete de comandos (que estaría fuera
del alcance de la biblioteca estándar, dada la multiplicidad de
intérpretes de comandos que hay), te permite realizar el procesamiento
de las líneas de comandos más fácilmente de lo que podrías hacerlo de
otra manera.  Para ilustrarlo, puede ver la diferencia en el siguiente
fragmento:

   >>> import shlex
   >>> text = "a && b; c && d || e; f >'abc'; (def \"ghi\")"
   >>> s = shlex.shlex(text, posix=True)
   >>> s.whitespace_split = True
   >>> list(s)
   ['a', '&&', 'b;', 'c', '&&', 'd', '||', 'e;', 'f', '>abc;', '(def', 'ghi)']
   >>> s = shlex.shlex(text, posix=True, punctuation_chars=True)
   >>> s.whitespace_split = True
   >>> list(s)
   ['a', '&&', 'b', ';', 'c', '&&', 'd', '||', 'e', ';', 'f', '>', 'abc', ';',
   '(', 'def', 'ghi', ')']

Por supuesto, se retornarán tokens que no son válidos para los
intérpretes de comandos y deberá implementar sus propias
comprobaciones de errores en los tokens retornados.

En lugar de pasar "True" como valor para el parámetro
punctuation_chars, puede pasar una cadena con caracteres específicos,
que se usará para determinar qué caracteres constituyen puntuación.
Por ejemplo:

   >>> import shlex
   >>> s = shlex.shlex("a && b || c", punctuation_chars="|")
   >>> list(s)
   ['a', '&', '&', 'b', '||', 'c']

Nota:

  Cuando es especificado "punctuation_chars", el atributo "wordchars"
  se aumenta con los caracteres "~-./*?=".  Esto se debe a que estos
  caracteres pueden aparecer en los nombres de archivo (incluidos los
  comodines) y en los argumentos de la línea de comandos (por ejemplo,
  "--color=auto"). Por lo tanto:

     >>> import shlex
     >>> s = shlex.shlex('~/a && b-c --color=auto || d *.py?',
     ...                 punctuation_chars=True)
     >>> list(s)
     ['~/a', '&&', 'b-c', '--color=auto', '||', 'd', '*.py?']

  Sin embargo, para que coincida con el intérprete de comandos lo más
  cerca posible, se recomienda utilizar siempre "posix" y
  "whitespace_split" cuando se utiliza "punctuation_chars", el cual
  negará por completo "wordchars".

Para obtener el mejor efecto, "punctuation_chars" debe establecerse
junto con "posix=True". (Tenga en cuenta que "posix=False" es el valor
predeterminado para "shlex".)
