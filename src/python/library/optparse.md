---
title: '"optparse" --- Parser for command line options'
source_url: https://docs.python.org/es/3
source_path: library/optparse.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3370
---

# "optparse" --- Parser for command line options

**Source code:** Lib/optparse.py

======================================================================

## Choosing an argument parsing library

The standard library includes three argument parsing libraries:

* "getopt": a module that closely mirrors the procedural C "getopt"
  API. Included in the standard library since before the initial
  Python 1.0 release.

* "optparse": a declarative replacement for "getopt" that provides
  equivalent functionality without requiring each application to
  implement its own procedural option parsing logic. Included in the
  standard library since the Python 2.3 release.

* "argparse": a more opinionated alternative to "optparse" that
  provides more functionality by default, at the expense of reduced
  application flexibility in controlling exactly how arguments are
  processed. Included in the standard library since the Python 2.7 and
  Python 3.2 releases.

In the absence of more specific argument parsing design constraints,
"argparse" is the recommended choice for implementing command line
applications, as it offers the highest level of baseline functionality
with the least application level code.

"getopt" is retained almost entirely for backwards compatibility
reasons. However, it also serves a niche use case as a tool for
prototyping and testing command line argument handling in
"getopt"-based C applications.

"optparse" should be considered as an alternative to "argparse" in the
following cases:

* an application is already using "optparse" and doesn't want to risk
  the subtle behavioural changes that may arise when migrating to
  "argparse"

* the application requires additional control over the way options and
  positional parameters are interleaved on the command line (including
  the ability to disable the interleaving feature completely)

* the application requires additional control over the incremental
  parsing of command line elements (while "argparse" does support
  this, the exact way it works in practice is undesirable for some use
  cases)

* the application requires additional control over the handling of
  options which accept parameter values that may start with "-" (such
  as delegated options to be passed to invoked subprocesses)

* the application requires some other command line parameter
  processing behavior which "argparse" does not support, but which can
  be implemented in terms of the lower level interface offered by
  "optparse"

These considerations also mean that "optparse" is likely to provide a
better foundation for library authors writing third party command line
argument processing libraries.

As a concrete example, consider the following two command line
argument parsing configurations, the first using "optparse", and the
second using "argparse":

   import optparse

   if __name__ == '__main__':
       parser = optparse.OptionParser()
       parser.add_option('-o', '--output')
       parser.add_option('-v', dest='verbose', action='store_true')
       opts, args = parser.parse_args()
       process(args, output=opts.output, verbose=opts.verbose)

   import argparse

   if __name__ == '__main__':
       parser = argparse.ArgumentParser()
       parser.add_argument('-o', '--output')
       parser.add_argument('-v', dest='verbose', action='store_true')
       parser.add_argument('rest', nargs='*')
       args = parser.parse_args()
       process(args.rest, output=args.output, verbose=args.verbose)

The most obvious difference is that in the "optparse" version, the
non-option arguments are processed separately by the application after
the option processing is complete. In the "argparse" version,
positional arguments are declared and processed in the same way as the
named options.

However, the "argparse" version will also handle some parameter
combination differently from the way the "optparse" version would
handle them. For example (amongst other differences):

* supplying "-o -v" gives "output="-v"" and "verbose=False" when using
  "optparse", but a usage error with "argparse" (complaining that no
  value has been supplied for "-o/--output", since "-v" is interpreted
  as meaning the verbosity flag)

* similarly, supplying "-o --" gives "output="--"" and "args=()" when
  using "optparse", but a usage error with "argparse" (also
  complaining that no value has been supplied for "-o/--output", since
  "--" is interpreted as terminating the option processing and
  treating all remaining values as positional arguments)

* supplying "-o=foo" gives "output="=foo"" when using "optparse", but
  gives "output="foo"" with "argparse" (since "=" is special cased as
  an alternative separator for option parameter values)

Whether these differing behaviors in the "argparse" version are
considered desirable or a problem will depend on the specific command
line application use case.

Ver también:

  click is a third party argument processing library (originally based
  on "optparse"), which allows command line applications to be
  developed as a set of decorated command implementation functions.

  Other third party libraries, such as typer or msgspec-click, allow
  command line interfaces to be specified in ways that more
  effectively integrate with static checking of Python type
  annotations.

## Introduction

"optparse" is a more convenient, flexible, and powerful library for
parsing command-line options than the minimalist "getopt" module.
"optparse" uses a more declarative style of command-line parsing: you
create an instance of "OptionParser", populate it with options, and
parse the command line. "optparse" allows users to specify options in
the conventional GNU/POSIX syntax, and additionally generates usage
and help messages for you.

Here's an example of using "optparse" in a simple script:

   from optparse import OptionParser
   ...
   parser = OptionParser()
   parser.add_option("-f", "--file", dest="filename",
                     help="write report to FILE", metavar="FILE")
   parser.add_option("-q", "--quiet",
                     action="store_false", dest="verbose", default=True,
                     help="don't print status messages to stdout")

   (options, args) = parser.parse_args()

Con estas pocas líneas de código, los usuarios de tu script ahora
pueden hacer un uso "normal" del mismo mediante la línea de comandos,
por ejemplo:

   <yourscript> --file=outfile -q

As it parses the command line, "optparse" sets attributes of the
"options" object returned by "parse_args()" based on user-supplied
command-line values.  When "parse_args()" returns from parsing this
command line, "options.filename" will be ""outfile"" and
"options.verbose" will be "False".  "optparse" supports both long and
short options, allows short options to be merged together, and allows
options to be associated with their arguments in a variety of ways.
Thus, the following command lines are all equivalent to the above
example:

   <yourscript> -f outfile --quiet
   <yourscript> --quiet --file outfile
   <yourscript> -q -foutfile
   <yourscript> -qfoutfile

Además, los usuarios pueden ejecutar uno de los siguientes:

   <yourscript> -h
   <yourscript> --help

and "optparse" will print out a brief summary of your script's
options:

   Usage: <yourscript> [options]

   Options:
     -h, --help            show this help message and exit
     -f FILE, --file=FILE  write report to FILE
     -q, --quiet           don't print status messages to stdout

donde el valor de *yourscript* se determina en tiempo de ejecución
(normalmente a partir de "sys.argv [0]").

## Contexto

"optparse" was explicitly designed to encourage the creation of
programs with straightforward command-line interfaces that follow the
conventions established by the "getopt()" family of functions
available to C developers. To that end, it supports only the most
common command-line syntax and semantics conventionally used under
Unix.  If you are unfamiliar with these conventions, reading this
section will allow you to acquaint yourself with them.

### Terminología

argumento
   una cadena de caracteres ingresada en la línea de comandos y pasada
   mediante la shell a "execl()" o "execv()". En Python, los
   argumentos son elementos de "sys.argv[1:]" (dado que "sys.argv[0]"
   es el propio nombre del programa que se está ejecutando). Las
   shells de Unix también usan el término "*word*" ('palabra') para
   referirse a ellos.

   En ocasiones es deseable proporcionar una lista de argumentos que
   no sea "sys.argv[1:]", por lo que deberías considerar un
   'argumento' como 'un elemento de "sys.argv[1:]" o de alguna otra
   lista proporcionada como sustituto de "sys.argv[1:]"'.

opción
   an argument used to supply extra information to guide or customize
   the execution of a program.  There are many different syntaxes for
   options; the traditional Unix syntax is a hyphen ("-") followed by
   a single letter, e.g. "-x" or "-F".  Also, traditional Unix syntax
   allows multiple options to be merged into a single argument, e.g.
   "-x -F" is equivalent to "-xF".  The GNU project introduced "--"
   followed by a series of hyphen-separated words, e.g. "--file" or "
   --dry-run".  These are the only two option syntaxes provided by
   "optparse".

   Algunas de las otras sintaxis para opciones que el mundo ha visto
   son:

   * un guion seguido de algunas letras, por ejemplo "-pf" (esto *no*
     es lo mismo que múltiples opciones fusionadas en un solo
     argumento)

   * un guion seguido de una palabra completa, por ejemplo "-file"
     (esto es técnicamente equivalente a la sintaxis anterior, pero
     generalmente no se ven ambas en un mismo programa)

   * un signo más seguido de una sola letra, unas pocas letras o una
     palabra, por ejemplo "+f" o "+rgb"

   * una barra seguida de una letra, de unas pocas letras o de una
     palabra, por ejemplo "/f" o "/file"

   These option syntaxes are not supported by "optparse", and they
   never will be.  This is deliberate: the first three are non-
   standard on any environment, and the last only makes sense if
   you're exclusively targeting Windows or certain legacy platforms
   (e.g. VMS, MS-DOS).

argumento de opción
   an argument that follows an option, is closely associated with that
   option, and is consumed from the argument list when that option is.
   With "optparse", option arguments may either be in a separate
   argument from their option:

      -f foo
      --file foo

   o incluidos en el mismo argumento:

      -ffoo
      --file=foo

   Typically, a given option either takes an argument or it doesn't.
   Lots of people want an "optional option arguments" feature, meaning
   that some options will take an argument if they see it, and won't
   if they don't.  This is somewhat controversial, because it makes
   parsing ambiguous: if "-a" takes an optional argument and "-b" is
   another option entirely, how do we interpret "-ab"?  Because of
   this ambiguity, "optparse" does not support this feature.

argumento posicional
   es algo que queda en la lista de argumentos después de que las
   opciones hayan sido analizadas sintácticamente, es decir, después
   de que las opciones y sus argumentos hayan sido analizados y
   eliminados de la lista de argumentos.

opción requerida
   an option that must be supplied on the command-line; note that the
   phrase "required option" is self-contradictory in English.
   "optparse" doesn't prevent you from implementing required options,
   but doesn't give you much help at it either.

Por ejemplo, considera esta hipotética linea de comandos:

   prog -v --report report.txt foo bar

"-v" y "--report" son ambas opciones. "report.txt" es un argumento de
opción, suponiendo que "--report" toma un argumento. En cambio, "foo"
y "bar" son ambos argumentos posicionales.

### ¿Qué finalidad tienen las opciones?

Las opciones se utilizan para poder proporcionar información adicional
con el fin de ajustar o personalizar la ejecución de un programa. Por
si aún no ha quedado claro, las opciones suelen ser *opcionales*. Un
programa debería poder ejecutarse sin problemas sin ninguna opción.
(Elija un programa aleatorio del conjunto de herramientas de Unix o
GNU. ¿Puede ejecutarse sin ninguna opción y aún así tener sentido? Las
principales excepciones son "find", "tar" y "dd"---los cuales son
todos bichos raros mutantes que han sido apropiadamente criticados por
su sintaxis no estándar y por tener interfaces confusas).

Como se ha comentado, mucha gente quiere que sus programas tengan
"opciones requeridas". Pero pensemos en ello detenidamente. ¡Si es
necesario, entonces *no es opcional*! Si hay una pieza de información
absolutamente requerida para que tu programa pueda ejecutarse
correctamente no uses opciones, para eso están los argumentos
posicionales.

Como ejemplo de un buen diseño de una interfaz de línea de comandos,
considera la humilde herramienta "cp" para copiar archivos. No tiene
mucho sentido intentar copiar archivos sin proporcionar un destino y
al menos una fuente de origen. Por lo tanto, "cp" falla si lo ejecutas
sin argumentos. Sin embargo, tiene una sintaxis flexible y útil que no
requiere ninguna opción:

   cp SOURCE DEST
   cp SOURCE ... DEST-DIR

Puedes hacer mucho simplemente con eso. La mayoría de las
implementaciones de "cp" proporcionan un montón de opciones para
modificar exactamente cómo se copian los archivos: se puede preservar
el modo y la fecha de modificación, evitar que se sigan enlaces
simbólicos, preguntar antes de sobrescribir el contenido de archivos
existentes, etc. Pero nada de esto distrae de la misión principal de
"cp", que consiste en copiar uno o varios archivos en otro directorio.

### ¿Qué finalidad tienen los argumentos posicionales?

Los argumentos posicionales son adecuados para aquellas piezas de
información que tu programa, absolutamente y sin duda alguna, requiere
para funcionar.

Una buena interfaz de usuario debería tener la menor cantidad de
requisitos absolutos posibles. Si tu programa requiere 17 piezas
distintas de información para ejecutarse correctamente, no importa
mucho *cómo* obtengas esa información del usuario; la mayoría de ellos
se rendirán y se irán antes de ejecutar con éxito el programa. Esto se
aplica tanto si la interfaz de usuario es una línea de comandos, un
archivo de configuración o una GUI: si hace demasiadas demandas a sus
usuarios, la mayoría simplemente se rendirá.

En resumen, trata de minimizar la cantidad de información que los
usuarios están absolutamente obligados a proporcionar, utiliza valores
predeterminados sensatos siempre que sea posible. Como es natural,
también deseas que tus programas sean razonablemente flexibles, para
eso están las opciones. De nuevo, no importa si son entradas en un
archivo de configuración, widgets en un cuadro de diálogo de
"Preferencias" de una GUI u opciones en la línea de comandos; cuantas
más opciones implementes, más flexible será tu programa y más
complicada se vuelve su implementación. Una excesiva flexibilidad
evidentemente también tiene inconvenientes, demasiadas opciones pueden
abrumar a los usuarios y hacer que tu código sea mucho más difícil de
mantener.

## Tutorial

While "optparse" is quite flexible and powerful, it's also
straightforward to use in most cases.  This section covers the code
patterns that are common to any "optparse"-based program.

En primer lugar, necesitas importar la clase OptionParser y luego, al
comienzo del programa principal, crear una instancia de ella:

   from optparse import OptionParser
   ...
   parser = OptionParser()

Ahora ya puedes comenzar a definir opciones. La sintaxis básica es:

   parser.add_option(opt_str, ...,
                     attr=value, ...)

Each option has one or more option strings, such as "-f" or "--file",
and several option attributes that tell "optparse" what to expect and
what to do when it encounters that option on the command line.

Normalmente, cada opción tendrá una cadena de opción corta y una
cadena de opción larga, por ejemplo:

   parser.add_option("-f", "--file", ...)

Puedes definir tantas cadenas de opción cortas y tantas largas como
desees (incluso ninguna), siempre que haya al menos una cadena de
opción en total.

The option strings passed to "OptionParser.add_option()" are
effectively labels for the option defined by that call.  For brevity,
we will frequently refer to *encountering an option* on the command
line; in reality, "optparse" encounters *option strings* and looks up
options from them.

Once all of your options are defined, instruct "optparse" to parse
your program's command line:

   (options, args) = parser.parse_args()

(Si lo deseas, puedes pasar una lista de argumentos personalizada a
"parse_args()", pero eso rara vez es necesario: por defecto se usa
"sys.argv [1:]".)

"parse_args()" retorna dos valores:

* "options", un objeto que contiene valores para todas tus opciones.
  Por ejemplo, si "--file" toma un argumento de una sola cadena de
  caracteres, entonces "options.file" será el nombre del archivo
  proporcionado por el usuario o "None" si el usuario no proporcionó
  esa opción en la linea de comandos

* "args", la lista de argumentos posicionales que quedan después de
  analizar las opciones

Este tutorial solo cubre los cuatro atributos de opción más
importantes: "action", "type", "dest" (destino) y "help". De todos
ellos, "action" es el fundamental.

### Comprendiendo las acciones de opción

Actions tell "optparse" what to do when it encounters an option on the
command line.  There is a fixed set of actions hard-coded into
"optparse"; adding new actions is an advanced topic covered in section
Extending optparse.  Most actions tell "optparse" to store a value in
some variable---for example, take a string from the command line and
store it in an attribute of "options".

If you don't specify an option action, "optparse" defaults to "store".

### La acción store

The most common option action is "store", which tells "optparse" to
take the next argument (or the remainder of the current argument),
ensure that it is of the correct type, and store it to your chosen
destination.

Por ejemplo:

   parser.add_option("-f", "--file",
                     action="store", type="string", dest="filename")

Now let's make up a fake command line and ask "optparse" to parse it:

   args = ["-f", "foo.txt"]
   (options, args) = parser.parse_args(args)

When "optparse" sees the option string "-f", it consumes the next
argument, "foo.txt", and stores it in "options.filename".  So, after
this call to "parse_args()", "options.filename" is ""foo.txt"".

Some other option types supported by "optparse" are "int" and "float".
Here's an option that expects an integer argument:

   parser.add_option("-n", type="int", dest="num")

Ten en cuenta que esta opción no tiene una cadena de opción larga, lo
cual es perfectamente aceptable. Además, no hay ninguna acción
explícita, ya que el valor predeterminado es "store".

Analicemos otra línea de comandos simulada. En esta ocasión, vamos a
proporcionar el argumento de la opción pegado junto a la misma, sin
separación entre ambos: dado que "-n42" (un argumento) es equivalente
a "-n 42" (dos argumentos), el código:

   (options, args) = parser.parse_args(["-n42"])
   print(options.num)

imprimirá "42".

If you don't specify a type, "optparse" assumes "string".  Combined
with the fact that the default action is "store", that means our first
example can be a lot shorter:

   parser.add_option("-f", "--file", dest="filename")

If you don't supply a destination, "optparse" figures out a sensible
default from the option strings: if the first long option string is "
--foo-bar", then the default destination is "foo_bar".  If there are
no long option strings, "optparse" looks at the first short option
string: the default destination for "-f" is "f".

"optparse" also includes the built-in "complex" type.  Adding types is
covered in section Extending optparse.

### Manejo de opciones booleanas (flags)

Flag options---set a variable to true or false when a particular
option is seen---are quite common.  "optparse" supports them with two
separate actions, "store_true" and "store_false".  For example, you
might have a "verbose" flag that is turned on with "-v" and off with
"-q":

   parser.add_option("-v", action="store_true", dest="verbose")
   parser.add_option("-q", action="store_false", dest="verbose")

Aquí tenemos dos opciones diferentes con el mismo destino, lo cual es
totalmente correcto. Solo significa que debes tener un poco de cuidado
al establecer los valores predeterminados, lo veremos a continuación.

When "optparse" encounters "-v" on the command line, it sets
"options.verbose" to "True"; when it encounters "-q",
"options.verbose" is set to "False".

### Otras acciones

Some other actions supported by "optparse" are:

""store_const""
   almacena un valor de constante, preestablecida vía "Option.const"

""append""
   agrega el argumento de esta opción a una lista

""count""
   incrementa un contador en uno

""callback""
   llama a una función específica

Estas acciones se tratan en la sección Guía de referencia y en la
sección Retrollamadas de opción.

### Valores por defecto

All of the above examples involve setting some variable (the
"destination") when certain command-line options are seen.  What
happens if those options are never seen?  Since we didn't supply any
defaults, they are all set to "None".  This is usually fine, but
sometimes you want more control.  "optparse" lets you supply a default
value for each destination, which is assigned before the command line
is parsed.

First, consider the verbose/quiet example.  If we want "optparse" to
set "verbose" to "True" unless "-q" is seen, then we can do this:

   parser.add_option("-v", action="store_true", dest="verbose", default=True)
   parser.add_option("-q", action="store_false", dest="verbose")

Dado que los valores predeterminados se aplican a *destination* en
lugar de a cualquier opción en particular y que estas dos opciones
tienen el mismo destino, lo anterior es exactamente equivalente a:

   parser.add_option("-v", action="store_true", dest="verbose")
   parser.add_option("-q", action="store_false", dest="verbose", default=True)

Considera lo siguiente:

   parser.add_option("-v", action="store_true", dest="verbose", default=False)
   parser.add_option("-q", action="store_false", dest="verbose", default=True)

Nuevamente, el valor predeterminado para "verbose" será "True": el
último valor predeterminado proporcionado para cualquier destino en
particular es el único que se tendrá en cuenta.

Una forma más clara de especificar valores predeterminados es el
método "set_defaults()" de OptionParser, al que puedes llamar en
cualquier momento antes de llamar a "parse_args()":

   parser.set_defaults(verbose=True)
   parser.add_option(...)
   (options, args) = parser.parse_args()

Como vimos antes, el último valor especificado para un destino de
opción dado es el que cuenta. Para mayor claridad, intenta utilizar un
método u otro para establecer valores predeterminados, no ambos.

### Generando ayuda

"optparse"'s ability to generate help and usage text automatically is
useful for creating user-friendly command-line interfaces.  All you
have to do is supply a "help" value for each option, and optionally a
short usage message for your whole program.  Here's an OptionParser
populated with user-friendly (documented) options:

   usage = "usage: %prog [options] arg1 arg2"
   parser = OptionParser(usage=usage)
   parser.add_option("-v", "--verbose",
                     action="store_true", dest="verbose", default=True,
                     help="make lots of noise [default]")
   parser.add_option("-q", "--quiet",
                     action="store_false", dest="verbose",
                     help="be vewwy quiet (I'm hunting wabbits)")
   parser.add_option("-f", "--filename",
                     metavar="FILE", help="write output to FILE")
   parser.add_option("-m", "--mode",
                     default="intermediate",
                     help="interaction mode: novice, intermediate, "
                          "or expert [default: %default]")

If "optparse" encounters either "-h" or "--help" on the command-line,
or if you just call "parser.print_help()", it prints the following to
standard output:

   Usage: <yourscript> [options] arg1 arg2

   Options:
     -h, --help            show this help message and exit
     -v, --verbose         make lots of noise [default]
     -q, --quiet           be vewwy quiet (I'm hunting wabbits)
     -f FILE, --filename=FILE
                           write output to FILE
     -m MODE, --mode=MODE  interaction mode: novice, intermediate, or
                           expert [default: intermediate]

(If the help output is triggered by a help option, "optparse" exits
after printing the help text.)

There's a lot going on here to help "optparse" generate the best
possible help message:

* el script define su propio mensaje de uso:

     usage = "usage: %prog [options] arg1 arg2"

  "optparse" expands "%prog" in the usage string to the name of the
  current program, i.e. "os.path.basename(sys.argv[0])".  The expanded
  string is then printed before the detailed option help.

  If you don't supply a usage string, "optparse" uses a bland but
  sensible default: ""Usage: %prog [options]"", which is fine if your
  script doesn't take any positional arguments.

* every option defines a help string, and doesn't worry about line-
  wrapping---"optparse" takes care of wrapping lines and making the
  help output look good.

* las opciones que toman un valor indican este hecho en su mensaje de
  ayuda generado automáticamente, por ejemplo, para la opción "mode":

     -m MODE, --mode=MODE

  Here, "MODE" is called the meta-variable: it stands for the argument
  that the user is expected to supply to "-m"/"--mode".  By default,
  "optparse" converts the destination variable name to uppercase and
  uses that for the meta-variable.  Sometimes, that's not what you
  want---for example, the "--filename" option explicitly sets
  "metavar="FILE"", resulting in this automatically generated option
  description:

     -f FILE, --filename=FILE

  Sin embargo, esto es importante para algo más que para ahorrar
  espacio: el texto de ayuda escrito manualmente utiliza la
  metavariable "FILE" para indicarle al usuario que hay una conexión
  entre la sintaxis semiformal "-f FILE" y la descripción semántica
  informal "escribir la salida en FILE". Esta es una manera simple
  pero efectiva de hacer que tu texto de ayuda sea mucho más claro y
  útil para los usuarios finales.

* options that have a default value can include "%default" in the help
  string---"optparse" will replace it with "str()" of the option's
  default value.  If an option has no default value (or the default
  value is "None"), "%default" expands to "none".

#### Agrupando opciones

Cuando se trabaja con muchas opciones, suele ser conveniente
agruparlas para obtener una mejor salida de ayuda. La clase
"OptionParser" puede contener varios grupos de opciones, cada uno de
los cuales puede contener múltiples opciones.

Podemos obtener un grupo de opciones usando la clase "OptionGroup":

class optparse.OptionGroup(parser, title, description=None)

   donde

   * *parser* es la instancia de "OptionParser" en la que se insertará
     el grupo

   * *title* es el título dado al grupo

   * *description*, opcional, es la descripción larga del grupo

la clase "OptionGroup" hereda de "OptionContainer" (al igual que
"OptionParser"), por lo que el método "add_option()" se puede usar
para agregar una opción al grupo.

Una vez que se han declarado todas las opciones, usando el método
"add_option_group()" de la clase "OptionParser" el grupo se agrega al
analizador sintáctico previamente definido.

Agregar un "OptionGroup" a un analizador es fácil, continuando con el
analizador definido en la sección anterior:

   group = OptionGroup(parser, "Dangerous Options",
                       "Caution: use these options at your own risk.  "
                       "It is believed that some of them bite.")
   group.add_option("-g", action="store_true", help="Group option.")
   parser.add_option_group(group)

Esto daría como resultado la siguiente salida de ayuda:

   Usage: <yourscript> [options] arg1 arg2

   Options:
     -h, --help            show this help message and exit
     -v, --verbose         make lots of noise [default]
     -q, --quiet           be vewwy quiet (I'm hunting wabbits)
     -f FILE, --filename=FILE
                           write output to FILE
     -m MODE, --mode=MODE  interaction mode: novice, intermediate, or
                           expert [default: intermediate]

     Dangerous Options:
       Caution: use these options at your own risk.  It is believed that some
       of them bite.

       -g                  Group option.

Un ejemplo un poco más completo podría implicar el uso de más de un
grupo, ampliando el ejemplo anterior:

   group = OptionGroup(parser, "Dangerous Options",
                       "Caution: use these options at your own risk.  "
                       "It is believed that some of them bite.")
   group.add_option("-g", action="store_true", help="Group option.")
   parser.add_option_group(group)

   group = OptionGroup(parser, "Debug Options")
   group.add_option("-d", "--debug", action="store_true",
                    help="Print debug information")
   group.add_option("-s", "--sql", action="store_true",
                    help="Print all SQL statements executed")
   group.add_option("-e", action="store_true", help="Print every action done")
   parser.add_option_group(group)

lo que da como resultado la siguiente salida:

   Usage: <yourscript> [options] arg1 arg2

   Options:
     -h, --help            show this help message and exit
     -v, --verbose         make lots of noise [default]
     -q, --quiet           be vewwy quiet (I'm hunting wabbits)
     -f FILE, --filename=FILE
                           write output to FILE
     -m MODE, --mode=MODE  interaction mode: novice, intermediate, or expert
                           [default: intermediate]

     Dangerous Options:
       Caution: use these options at your own risk.  It is believed that some
       of them bite.

       -g                  Group option.

     Debug Options:
       -d, --debug         Print debug information
       -s, --sql           Print all SQL statements executed
       -e                  Print every action done

Otro método interesante, particularmente cuando se trabaja
programáticamente con grupos de opciones, es:

OptionParser.get_option_group(opt_str)

   Retorna el "OptionGroup" al que pertenece la cadena de opción corta
   o larga *opt_str* (por ejemplo, "'-o'" o "' --option'"). Si no
   existe dicho "OptionGroup", el método retorna "None".

### Imprimir una cadena de caracteres con la versión del programa

Similar to the brief usage string, "optparse" can also print a version
string for your program.  You have to supply the string as the
"version" argument to OptionParser:

   parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")

"%prog" is expanded just like it is in "usage".  Apart from that,
"version" can contain anything you like.  When you supply it,
"optparse" automatically adds a "--version" option to your parser. If
it encounters this option on the command line, it expands your
"version" string (by replacing "%prog"), prints it to stdout, and
exits.

Por ejemplo, si tu script se llama "/usr/bin/foo":

   $ /usr/bin/foo --version
   foo 1.0

Para imprimir y obtener la cadena de caracteres "version", se pueden
utilizar cualquiera de los siguientes métodos:

OptionParser.print_version(file=None)

   Imprime el mensaje con la versión del programa actual
   ("self.version") en *file* (por defecto, la salida estándar). Al
   igual que con "print_usage()", cualquier aparición de "%prog" en
   "self.version" se reemplaza con el nombre del programa actual. El
   método no hace nada si "self.version" está vacío o no está
   definido.

OptionParser.get_version()

   Igual que "print_version()", pero retorna la cadena de versión en
   lugar de imprimirla.

### How "optparse" handles errors

There are two broad classes of errors that "optparse" has to worry
about: programmer errors and user errors.  Programmer errors are
usually erroneous calls to "OptionParser.add_option()", e.g. invalid
option strings, unknown option attributes, missing option attributes,
etc.  These are dealt with in the usual way: raise an exception
(either "optparse.OptionError" or "TypeError") and let the program
crash.

Handling user errors is much more important, since they are guaranteed
to happen no matter how stable your code is.  "optparse" can
automatically detect some user errors, such as bad option arguments
(passing "-n 4x" where "-n" takes an integer argument), missing
arguments ("-n" at the end of the command line, where "-n" takes an
argument of any type).  Also, you can call "OptionParser.error()" to
signal an application-defined error condition:

   (options, args) = parser.parse_args()
   ...
   if options.a and options.b:
       parser.error("options -a and -b are mutually exclusive")

In either case, "optparse" handles the error the same way: it prints
the program's usage message and an error message to standard error and
exits with error status 2.

Considera el primero de los dos ejemplos anteriores, donde el usuario
pasa "4x" a una opción que toma un número entero:

   $ /usr/bin/foo -n 4x
   Usage: foo [options]

   foo: error: option -n: invalid integer value: '4x'

O, en el caso en el que el usuario definitivamente no pase ningún
valor:

   $ /usr/bin/foo -n
   Usage: foo [options]

   foo: error: -n option requires an argument

"optparse"-generated error messages take care always to mention the
option involved in the error; be sure to do the same when calling
"OptionParser.error()" from your application code.

If "optparse"'s default error-handling behaviour does not suit your
needs, you'll need to subclass OptionParser and override its "exit()"
and/or "error()" methods.

### Reuniendo todas las piezas

Here's what "optparse"-based scripts usually look like:

   from optparse import OptionParser
   ...
   def main():
       usage = "usage: %prog [options] arg"
       parser = OptionParser(usage)
       parser.add_option("-f", "--file", dest="filename",
                         help="read data from FILENAME")
       parser.add_option("-v", "--verbose",
                         action="store_true", dest="verbose")
       parser.add_option("-q", "--quiet",
                         action="store_false", dest="verbose")
       ...
       (options, args) = parser.parse_args()
       if len(args) != 1:
           parser.error("incorrect number of arguments")
       if options.verbose:
           print("reading %s..." % options.filename)
       ...

   if __name__ == "__main__":
       main()

## Guía de referencia

### Creando el analizador sintáctico (parser)

The first step in using "optparse" is to create an OptionParser
instance.

class optparse.OptionParser(...)

   El constructor de la clase OptionParser no tiene argumentos
   obligatorios, pero sí varios argumentos opcionales por palabra
   clave. Siempre deben pasarse como argumentos por palabras clave, es
   decir, no se debe confiar nunca en el orden en que se declaran los
   argumentos.

   "usage" (por defecto: ""%prog [options]"")
      The usage summary to print when your program is run incorrectly
      or with a help option.  When "optparse" prints the usage string,
      it expands "%prog" to "os.path.basename(sys.argv[0])" (or to
      "prog" if you passed that keyword argument).  To suppress a
      usage message, pass the special value "optparse.SUPPRESS_USAGE".

   "option_list" (por defecto: "[]")
      Una lista de objetos Option con los que poblar el analizador.
      Las opciones en "option_list" se agregan después de cualquier
      opción en "standard_option_list" (un atributo de clase que puede
      ser establecido por las subclases de OptionParser), pero antes
      de cualquier versión u opción de ayuda. Obsoleto: usar en su
      lugar el método "add_option()", una vez creado el analizador.

   "option_class" (por defecto: *optparse.Option*)
      Clase usada por el método "add_option()" para añadir opciones al
      analizador.

   "version" (por defecto: "None")
      A version string to print when the user supplies a version
      option. If you supply a true value for "version", "optparse"
      automatically adds a version option with the single option
      string "--version".  The substring "%prog" is expanded the same
      as for "usage".

   "conflict_handler" (por defecto: ""error"")
      Especifica qué hacer cuando se agregan al analizador opciones
      con cadenas de opción en conflicto entre si. Ver sección
      Conflictos entre opciones.

   "description" (por defecto: "None")
      A paragraph of text giving a brief overview of your program.
      "optparse" reformats this paragraph to fit the current terminal
      width and prints it when the user requests help (after "usage",
      but before the list of options).

   "formatter" (por defecto: una nueva instancia de la clase
   "IndentedHelpFormatter")
      An instance of optparse.HelpFormatter that will be used for
      printing help text.  "optparse" provides two concrete classes
      for this purpose: IndentedHelpFormatter and TitledHelpFormatter.

   "add_help_option" (por defecto: "True")
      If true, "optparse" will add a help option (with option strings
      "-h" and "--help") to the parser.

   "prog"
      La cadena de caracteres a usar como substituta de
      "os.path.basename(sys.argv[0])" cuando se expanda "%prog" en
      "usage" y en "version".

   "epilog" (por defecto: "None")
      Un párrafo con texto de ayuda que se imprimirá después de la
      opción de ayuda.

### Completando el analizador con opciones

Hay varias formas de agregar las opciones al analizador. La forma
preferida es mediante el método "OptionParser.add_option()", tal como
se muestra en la sección del Tutorial. El método "add_option()" se
puede llamar de dos formas diferentes:

* pasándole una instancia de Option (como la que retorna
  "make_option()")

* pasándole cualquier combinación de argumentos posicionales y por
  palabra clave que sean aceptables para "make_option()" (es decir,
  para el constructor de la clase Option), lo que creará la instancia
  Option automáticamente

La otra alternativa es pasar una lista de instancias de Option
previamente construidas al constructor OptionParser, como en el
siguiente ejemplo:

   option_list = [
       make_option("-f", "--filename",
                   action="store", type="string", dest="filename"),
       make_option("-q", "--quiet",
                   action="store_false", dest="verbose"),
       ]
   parser = OptionParser(option_list=option_list)

("make_option()" is a factory function for creating Option instances;
currently it is an alias for the Option constructor.  A future version
of "optparse" may split Option into several classes, and
"make_option()" will pick the right class to instantiate.  Do not
instantiate Option directly.)

### Definiendo las opciones

Cada instancia de Option representa un conjunto de cadenas de opción
sinónimas para la línea de comandos, por ejemplo "-f" y "--file". Se
puede especificar cualquier número de cadenas de opción cortas o
largas, pero se debe proporcionar al menos una cadena de opción en
total.

La forma canónica de crear una instancia de "Option" es mediante el
método "add_option()" de la clase "OptionParser".

OptionParser.add_option(option)
OptionParser.add_option(*opt_str, attr=value, ...)

   Para definir una opción con solo una cadena de opción corta:

      parser.add_option("-f", attr=value, ...)

   Y para definir una opción con solo una cadena de opción larga:

      parser.add_option("--foo", attr=value, ...)

   The keyword arguments define attributes of the new Option object.
   The most important option attribute is "action", and it largely
   determines which other attributes are relevant or required.  If you
   pass irrelevant option attributes, or fail to pass required ones,
   "optparse" raises an "OptionError" exception explaining your
   mistake.

   An option's *action* determines what "optparse" does when it
   encounters this option on the command-line.  The standard option
   actions hard-coded into "optparse" are:

   ""store""
      almacena el argumento de esta opción (por defecto)

   ""store_const""
      almacena un valor de constante, preestablecida vía
      "Option.const"

   ""store_true""
      almacena "True"

   ""store_false""
      almacena "False"

   ""append""
      agrega el argumento de esta opción a una lista

   ""append_const""
      agrega un valor constante a una lista, preestablecido vía
      "Option.const"

   ""count""
      incrementa un contador en uno

   ""callback""
      llama a una función específica

   ""help""
      imprime un mensaje de uso que incluye todas las opciones y la
      documentación correspondiente

   (Si no se proporciona una acción, el valor predeterminado es
   ""store"". Para esta acción en concreto, también se pueden
   proporcionar los atributos de opción "type" y "dest". Consultar
   Acciones de opción estándares para más información.)

As you can see, most actions involve storing or updating a value
somewhere. "optparse" always creates a special object for this,
conventionally called "options", which is an instance of
"optparse.Values".

class optparse.Values

   Un objeto que mantiene como atributos a los nombres de los
   argumentos y los valores analizados. Normalmente se crean por
   invocación cuando llamamos "OptionParser.parse_args()", y pueden
   ser sobreescritos por una subclase personalizada pasada al
   argumento *values* de "OptionParser.parse_args()" (como se describe
   en Analizando los argumentos).

Los argumentos de opción (y algunos otros valores) se almacenan como
atributos de este objeto, de acuerdo con el atributo de opción "dest"
(destino) establecido.

Por ejemplo, cuando se llama a:

   parser.parse_args()

one of the first things "optparse" does is create the "options"
object:

   options = Values()

Si una de las opciones de este analizador es definida con:

   parser.add_option("-f", "--file", action="store", type="string", dest="filename")

y la línea de comandos que se analiza incluye cualquiera de las
siguientes variantes:

   -ffoo
   -f foo
   --file=foo
   --file foo

then "optparse", on seeing this option, will do the equivalent of

   options.filename = "foo"

Los atributos de opción "type" y "dest" son casi tan importantes como
"action", pero "action" es el único de ellos que es apropiado para
*todas* las opciones.

### Atributos de opción

class optparse.Option

   Un único argumento de línea de comando, con varios atributos
   pasados como palabras clave al constructor. Normalmente se crea con
   "OptionParser.add_option()" en lugar de directamente, y puede ser
   sobrescrito por una clase personalizada mediante el argumento
   *option_class* de "OptionParser".

The following option attributes may be passed as keyword arguments to
"OptionParser.add_option()".  If you pass an option attribute that is
not relevant to a particular option, or fail to pass a required option
attribute, "optparse" raises "OptionError".

Option.action

   (por defecto: ""store"")

   Determines "optparse"'s behaviour when this option is seen on the
   command line; the available options are documented here.

Option.type

   (por defecto: ""string"")

   El tipo de argumento esperado para esta opción (por ejemplo,
   ""string"" o ""int""). Los tipos de opción disponibles están
   documentados aquí.

Option.dest

   (por defecto: derivado de las cadenas de opción)

   If the option's action implies writing or modifying a value
   somewhere, this tells "optparse" where to write it: "dest" names an
   attribute of the "options" object that "optparse" builds as it
   parses the command line.

Option.default

   El valor que se utilizará como destino de esta opción si la opción
   no aparece en la línea de comandos. Ver también
   "OptionParser.set_defaults()".

Option.nargs

   (por defecto: 1)

   How many arguments of type "type" should be consumed when this
   option is seen.  If > 1, "optparse" will store a tuple of values to
   "dest".

Option.const

   Para acciones que almacenan un valor constante, el valor constante
   a almacenar.

Option.choices

   Para opciones de tipo ""choice"", la lista con las cadenas que el
   usuario puede elegir.

Option.callback

   Para las opciones con la acción ""callback"" asignada, el objeto
   invocable a llamar cuando se encuentra esta opción. Consultar la
   sección Retrollamadas de opción para obtener más detalles sobre los
   argumentos que son pasados al objeto invocable.

Option.callback_args
Option.callback_kwargs

   Argumentos posicionales y por palabra clave adicionales para ser
   pasados a "callback" después de los cuatro argumentos pasados a la
   retrollamada estándar.

Option.help

   Texto de ayuda a imprimir para esta opción cuando se enumeran todas
   las opciones disponibles, después de que el usuario proporcione una
   opción "help" (como "--help"). Si no se proporciona ningún texto de
   ayuda, la opción seguirá apareciendo, solo que sin texto de ayuda.
   Para ocultar esta opción completamente, se debe asignar al atributo
   el valor especial "optparse.SUPPRESS_HELP".

Option.metavar

   (por defecto: derivado de las cadenas de opción)

   Reemplazo para los argumentos de opción que se utilizará al
   imprimir el texto de ayuda. Consultar la sección Tutorial para ver
   un ejemplo.

### Acciones de opción estándares

The various option actions all have slightly different requirements
and effects. Most actions have several relevant option attributes
which you may specify to guide "optparse"'s behaviour; a few have
required attributes, which you must specify for any option using that
action.

* ""store"" [atributos relacionados: "type", "dest", "nargs",
  "choices"]

  La opción debe ir seguida de un argumento, que se convierte en un
  valor de acuerdo a "type" y se almacena en "dest". Si "nargs" es
  mayor que 1, se consumirán varios argumentos de la línea de
  comandos. Todos ellos se convertirán de acuerdo a "type" y se
  almacenarán en "dest" como una tupla. Consultar la sección Tipos de
  opción estándares para más información.

  Si se proporciona "choices" (una lista o tupla de cadenas de
  caracteres), el tipo por defecto es ""choice"".

  Si no se proporciona "type", el tipo por defecto es ""string"".

  If "dest" is not supplied, "optparse" derives a destination from the
  first long option string (e.g., "--foo-bar" implies "foo_bar"). If
  there are no long option strings, "optparse" derives a destination
  from the first short option string (e.g., "-f" implies "f").

  Ejemplo:

     parser.add_option("-f")
     parser.add_option("-p", type="float", nargs=3, dest="point")

  Mientras analiza la línea de comandos:

     -f foo.txt -p 1 -3.5 4 -fbar.txt

  "optparse" will set

     options.f = "foo.txt"
     options.point = (1.0, -3.5, 4.0)
     options.f = "bar.txt"

* ""store_const"" [atributo requerido: "const"; atributo relacionado:
  "dest"]

  El valor "const" es almacenado en "dest".

  Ejemplo:

     parser.add_option("-q", "--quiet",
                       action="store_const", const=0, dest="verbose")
     parser.add_option("-v", "--verbose",
                       action="store_const", const=1, dest="verbose")
     parser.add_option("--noisy",
                       action="store_const", const=2, dest="verbose")

  If "--noisy" is seen, "optparse" will set

     options.verbose = 2

* ""store_true"" [atributo relacionado: "dest"]

  Un caso especial de ""store_const"" que almacena "True" en "dest".

* ""store_false"" [atributo relacionado: "dest"]

  Como ""store_true"", pero almacena "False".

  Ejemplo:

     parser.add_option("--clobber", action="store_true", dest="clobber")
     parser.add_option("--no-clobber", action="store_false", dest="clobber")

* ""append"" [atributos relacionados: "type", "dest", "nargs",
  "choices"]

  The option must be followed by an argument, which is appended to the
  list in "dest".  If no default value for "dest" is supplied, an
  empty list is automatically created when "optparse" first encounters
  this option on the command-line.  If "nargs" > 1, multiple arguments
  are consumed, and a tuple of length "nargs" is appended to "dest".

  Los valores por defecto para los atributos "type" y "dest" son los
  mismos que para la acción ""store"".

  Ejemplo:

     parser.add_option("-t", "--tracks", action="append", type="int")

  If "-t3" is seen on the command-line, "optparse" does the equivalent
  of:

     options.tracks = []
     options.tracks.append(int("3"))

  Si, un poco más adelante, se encuentra "--tracks=4", procede así:

     options.tracks.append(int("4"))

  La acción "append" llama al método "append" con el valor actual de
  la opción. Esto significa que cualquier valor por defecto
  especificado debe tener un método "append". También significa que si
  existe un valor por defecto, los elementos por defecto estarán
  presentes en el valor analizado para la opción, con todos los
  valores de la línea de comandos agregados a la lista a continuación
  de ellos:

     >>> parser.add_option("--files", action="append", default=['~/.mypkg/defaults'])
     >>> opts, args = parser.parse_args(['--files', 'overrides.mypkg'])
     >>> opts.files
     ['~/.mypkg/defaults', 'overrides.mypkg']

* ""append_const"" [atributo requerido: "const"; atributo relacionado:
  "dest"]

  Igual que ""store_const"", pero el valor "const" se agrega a "dest".
  Como ocurre con ""append"", "dest" por defecto es "None" y se crea
  automáticamente una lista vacía la primera vez que se encuentra la
  opción en la linea de comandos.

* ""count"" [atributo relacionado: "dest"]

  Incrementa el entero almacenado en "dest". Si no se proporciona un
  valor por defecto, "dest" se establece en cero antes de
  incrementarse por primera vez.

  Ejemplo:

     parser.add_option("-v", action="count", dest="verbosity")

  The first time "-v" is seen on the command line, "optparse" does the
  equivalent of:

     options.verbosity = 0
     options.verbosity += 1

  Cada aparición posterior de "-v" da como resultado:

     options.verbosity += 1

* ""callback"" [atributo requerido: "callback"; atributos
  relacionados: "type", "nargs", "callback_args", "callback_kwargs"]

  Llama a la función especificada por "callback", que es llamada como:

     func(option, opt_str, value, parser, *args, **kwargs)

  Ver sección Retrollamadas de opción para más detalles.

* ""help""

  Imprime un mensaje de ayuda completo para todas las opciones
  presentes en el analizador de opciones actual. El mensaje de ayuda
  se construye a partir de la cadena "usage", pasada al constructor de
  OptionParser, y la cadena "help", pasada a cada opción.

  Si no se proporciona una cadena "help" para una opción, dicha opción
  seguirá apareciendo en el mensaje de ayuda. Para omitir una opción
  por completo, debe usarse el valor especial
  "optparse.SUPPRESS_HELP".

  "optparse" automatically adds a "help" option to all OptionParsers,
  so you do not normally need to create one.

  Ejemplo:

     from optparse import OptionParser, SUPPRESS_HELP

     # usually, a help option is added automatically, but that can
     # be suppressed using the add_help_option argument
     parser = OptionParser(add_help_option=False)

     parser.add_option("-h", "--help", action="help")
     parser.add_option("-v", action="store_true", dest="verbose",
                       help="Be moderately verbose")
     parser.add_option("--file", dest="filename",
                       help="Input file to read data from")
     parser.add_option("--secret", help=SUPPRESS_HELP)

  If "optparse" sees either "-h" or "--help" on the command line, it
  will print something like the following help message to stdout
  (assuming "sys.argv[0]" is ""foo.py""):

     Usage: foo.py [options]

     Options:
       -h, --help        Show this help message and exit
       -v                Be moderately verbose
       --file=FILENAME   Input file to read data from

  After printing the help message, "optparse" terminates your process
  with "sys.exit(0)".

* ""version""

  Prints the version number supplied to the OptionParser to stdout and
  exits. The version number is actually formatted and printed by the
  "print_version()" method of OptionParser.  Generally only relevant
  if the "version" argument is supplied to the OptionParser
  constructor.  As with "help" options, you will rarely create
  "version" options, since "optparse" automatically adds them when
  needed.

### Tipos de opción estándares

"optparse" has five built-in option types: ""string"", ""int"",
""choice"", ""float"" and ""complex"".  If you need to add new option
types, see section Extending optparse.

Los argumentos de las opciones en la cadena ingresada no se verifican
ni se convierten de ninguna manera: el texto de la línea de comandos
se almacena en el destino (o se pasa a la retrollamada) tal cual.

Los argumentos enteros (tipo ""int"") se analizan de la siguiente
manera:

* si el número comienza con "0x", se analiza como un número
  hexadecimal

* si el número comienza con "0", se analiza como un número octal

* si el número comienza con "0b", se analiza como un número binario

* en cualquier otro caso, el número se analiza como un número decimal

The conversion is done by calling "int()" with the appropriate base
(2, 8, 10, or 16).  If this fails, so will "optparse", although with a
more useful error message.

Los argumentos de las opciones de tipo ""float"" y ""complex"" se
convierten directamente usando "float()" y "complex()"
respectivamente, con un manejo de errores similar.

Las opciones de tipo ""choice"" son un subtipo de las opciones
""string"". El atributo de opción "choices" (que es una secuencia de
cadenas) define el conjunto de argumentos de opción permitidos.
Posteriormente, "optparse.check_choice()" comparará los argumentos de
las opciones proporcionadas por el usuario con esta lista maestra y
lanzará una excepción "OptionValueError" si se proporciona una cadena
no válida.

### Analizando los argumentos

El objetivo primario de crear y agregar opciones a un OptionParser es
llamar a su método "parse_args()".

OptionParser.parse_args(args=None, values=None)

   Analiza las opciones de la línea de comando encontradas en *args*.

   Los parámetros de entrada son

   "args"
      la lista de argumentos a procesar (por defecto: "sys.argv [1:]")

   "values"
      a "Values" object to store option arguments in (default: a new
      instance of "Values") -- if you give an existing object, the
      option defaults will not be initialized on it

   y los valores de retorno es un par "(options, args)" donde

   "options"
      the same object that was passed in as *values*, or the
      "optparse.Values" instance created by "optparse"

   "args"
      los argumentos posicionales que quedan en la linea de comandos
      después de que se hayan procesado todas las opciones

El uso más habitual es no proporcionar ningún argumento por palabra
clave. Si se proporciona "values", dicho argumento será modificado
mediante llamadas repetidas a "setattr()" (aproximadamente una por
cada argumento de opción a almacenar en un destino de opción) y
finalmente será retornado por el método "parse_args()".

Si el método "parse_args()" encuentra algún error en la lista de
argumentos, llama al método "error()" de OptionParser con un mensaje
de error apropiado para el usuario final. Esto causa que el proceso
termine con un estado de salida de 2 (el estado de salida tradicional
en Unix para errores en la línea de comandos).

### Consultar y manipular el analizador de opciones

El comportamiento predeterminado del analizador de opciones se puede
personalizar ligeramente. También se puede indagar en el analizador de
opciones y ver qué hay en él. OptionParser proporciona varios métodos
para ayudar con éstos propósitos:

OptionParser.disable_interspersed_args()

   Set parsing to stop on the first non-option.  For example, if "-a"
   and "-b" are both simple options that take no arguments, "optparse"
   normally accepts this syntax:

      prog -a arg1 -b arg2

   y la trata de forma equivalente a:

      prog -a -b arg1 arg2

   Para deshabilitar esta funcionalidad, se debe llamar al método
   "disable_interspersed_args()". Esto restaura la sintaxis
   tradicional usada en Unix, donde el análisis de opción se detiene
   con el primer argumento que no es una opción.

   Se debe usar este método si se dispone de un procesador de comandos
   que ejecuta otro comando con sus propias opciones y se desea
   asegurarse de que estas opciones no se confunden entre si. Lo que
   puede ocurrir si, por ejemplo, cada comando tiene un conjunto
   diferente de opciones.

OptionParser.enable_interspersed_args()

   Configura el análisis para que no se detenga si encuentra un
   argumento que no sea una opción, lo que permite intercalar
   modificadores con argumentos de linea de comandos. Este es el
   comportamiento por defecto.

OptionParser.get_option(opt_str)

   Retorna la instancia de Option con la cadena de opción *opt_str*, o
   "None" si ninguna opción tiene esa cadena de opción.

OptionParser.has_option(opt_str)

   Retorna "True" si OptionParser tiene una opción con la cadena de
   opción *opt_str* (por ejemplo, "-q" o "--verbose").

OptionParser.remove_option(opt_str)

   Si "OptionParser" tiene una opción correspondiente a *opt_str*, esa
   opción es eliminada. Si esa opción proporcionó cualquier otra
   cadena de opción, todas esas cadenas de opción quedan invalidadas.
   Si *opt_str* no aparece en ninguna opción que pertenezca a este
   "OptionParser", se lanza una excepción "ValueError".

### Conflictos entre opciones

Si no se tiene cuidado, es fácil definir opciones con cadenas de
opción en conflicto entre si:

   parser.add_option("-n", "--dry-run", ...)
   ...
   parser.add_option("-n", "--noisy", ...)

(Esto es particularmente cierto si se ha definido una subclase propia
de OptionParser con algunas opciones estándar.)

Every time you add an option, "optparse" checks for conflicts with
existing options.  If it finds any, it invokes the current conflict-
handling mechanism. You can set the conflict-handling mechanism either
in the constructor:

   parser = OptionParser(..., conflict_handler=handler)

o mediante una llamada separada:

   parser.set_conflict_handler(handler)

Los administradores de conflictos disponibles son:

   ""error"" (por defecto)
      se asume que los conflictos entre opciones son un error de
      programación y, por tanto, generarán una excepción
      "OptionConflictError"

   ""resolve""
      resuelve conflictos de opciones de forma inteligente (ver más
      abajo)

Como ejemplo, vamos a definir un "OptionParser" que resuelva
conflictos de manera inteligente y agregaremos algunas opciones
conflictivas:

   parser = OptionParser(conflict_handler="resolve")
   parser.add_option("-n", "--dry-run", ..., help="do no harm")
   parser.add_option("-n", "--noisy", ..., help="be noisy")

At this point, "optparse" detects that a previously added option is
already using the "-n" option string.  Since "conflict_handler" is
""resolve"", it resolves the situation by removing "-n" from the
earlier option's list of option strings.  Now "--dry-run" is the only
way for the user to activate that option.  If the user asks for help,
the help message will reflect that:

   Options:
     --dry-run     do no harm
     ...
     -n, --noisy   be noisy

It's possible to whittle away the option strings for a previously
added option until there are none left, and the user has no way of
invoking that option from the command-line.  In that case, "optparse"
removes that option completely, so it doesn't show up in help text or
anywhere else. Carrying on with our existing OptionParser:

   parser.add_option("--dry-run", ..., help="new dry-run option")

At this point, the original "-n"/"--dry-run" option is no longer
accessible, so "optparse" removes it, leaving this help text:

   Options:
     ...
     -n, --noisy   be noisy
     --dry-run     new dry-run option

### Limpieza

Las instancias de OptionParser tienen varias referencias cíclicas.
Esto no debería ser un problema para el recolector de basura de
Python, pero es posible que se desee romper las referencias cíclicas
explícitamente llamando al método "destroy()" de la instancia
OptionParser una vez que se haya terminado. Esto es particularmente
útil en aplicaciones de larga ejecución en las que OptionParser puede
terminar accediendo a grafos de objetos considerablemente grandes.

### Otros métodos

OptionParser admite varios métodos públicos más:

OptionParser.set_usage(usage)

   Establece la cadena de caracteres de uso de acuerdo a las reglas
   descritas anteriormente para el argumento por palabra clave "usage"
   del constructor. Pasando "None" se establece la cadena de uso por
   defecto; use el valor especial "optparse.SUPPRESS_USAGE" para
   suprimir el mensaje de uso.

OptionParser.print_usage(file=None)

   Imprime el mensaje de uso del programa actual ("self.usage") en
   *file* (que por defecto es la salida estándar). Cualquier aparición
   de la cadena de caracteres "%prog" en "self.usage" es reemplazada
   con el nombre del programa actual. No hace nada si "self.usage"
   está vacío o no ha sido definido.

OptionParser.get_usage()

   Igual que "print_usage()" pero retorna la cadena de uso en vez de
   imprimirla.

OptionParser.set_defaults(dest=value, ...)

   Establece valores por defecto para varios destinos de opción a la
   vez. Usar el método "set_defaults()" es la forma preferida de
   establecer valores por defecto para las opciones, ya que varias
   opciones pueden compartir el mismo destino. Por ejemplo, si varias
   opciones de "mode" tienen el mismo destino, cualquiera de ellas
   puede establecer el valor por defecto, pero el último establecido
   es el que finalmente queda establecido:

      parser.add_option("--advanced", action="store_const",
                        dest="mode", const="advanced",
                        default="novice")    # overridden below
      parser.add_option("--novice", action="store_const",
                        dest="mode", const="novice",
                        default="advanced")  # overrides above setting

   Para evitar esta confusión, usa el método "set_defaults()":

      parser.set_defaults(mode="advanced")
      parser.add_option("--advanced", action="store_const",
                        dest="mode", const="advanced")
      parser.add_option("--novice", action="store_const",
                        dest="mode", const="novice")

## Retrollamadas de opción

When "optparse"'s built-in actions and types aren't quite enough for
your needs, you have two choices: extend "optparse" or define a
callback option. Extending "optparse" is more general, but overkill
for a lot of simple cases.  Quite often a simple callback is all you
need.

Hay dos pasos a seguir para definir una opción con retrollamada:

* definir la opción en sí usando la acción ""callback""

* escribir la retrollamada. Esta es una función (o método) que toma al
  menos cuatro argumentos, los cuales son descritos a continuación

### Definición de una opción con retrollamada

Generalmente, la forma más sencilla de definir una opción con
retrollamada es mediante el método "OptionParser.add_option()". Aparte
de "action", el único atributo de opción que debes especificar es
"callback", que es la función a llamar:

   parser.add_option("-c", action="callback", callback=my_callback)

"callback" is a function (or other callable object), so you must have
already defined "my_callback()" when you create this callback option.
In this simple case, "optparse" doesn't even know if "-c" takes any
arguments, which usually means that the option takes no arguments---
the mere presence of "-c" on the command-line is all it needs to know.
In some circumstances, though, you might want your callback to consume
an arbitrary number of command-line arguments.  This is where writing
callbacks gets tricky; it's covered later in this section.

"optparse" always passes four particular arguments to your callback,
and it will only pass additional arguments if you specify them via
"callback_args" and "callback_kwargs".  Thus, the minimal callback
function signature is:

   def my_callback(option, opt, value, parser):

Los cuatro argumentos para la retrollamada se describen a
continuación.

Hay varios atributos de opción adicionales que se pueden proporcionar
cuando se define una opción con retrollamada:

"type"
   has its usual meaning: as with the ""store"" or ""append"" actions,
   it instructs "optparse" to consume one argument and convert it to
   "type".  Rather than storing the converted value(s) anywhere,
   though, "optparse" passes it to your callback function.

"nargs"
   also has its usual meaning: if it is supplied and > 1, "optparse"
   will consume "nargs" arguments, each of which must be convertible
   to "type".  It then passes a tuple of converted values to your
   callback.

"callback_args"
   una tupla con los argumentos posicionales adicionales para pasar a
   la retrollamada

"callback_kwargs"
   un diccionario con los argumentos por palabra clave para pasar a la
   retrollamada

### Cómo son invocadas las retrollamadas

Todas las retrollamadas son invocadas de la siguiente forma:

   func(option, opt_str, value, parser, *args, **kwargs)

donde

"option"
   es la instancia de Option que invoca a la retrollamada

"opt_str"
   es la cadena de opción encontrada en la línea de comandos que
   activa la retrollamada. (Si se utilizó una opción larga abreviada,
   "opt_str" será la cadena de opción canónica completa--- por
   ejemplo, si el usuario ingresa "--foo" en la línea de comandos como
   una abreviatura de "--foobar", entonces "opt_str" será ""--
   foobar"".)

"value"
   is the argument to this option seen on the command-line.
   "optparse" will only expect an argument if "type" is set; the type
   of "value" will be the type implied by the option's type.  If
   "type" for this option is "None" (no argument expected), then
   "value" will be "None".  If "nargs" > 1, "value" will be a tuple of
   values of the appropriate type.

"parser"
   es la instancia de OptionParser que controla todo. Su utilidad
   principal radica en que permite acceder a otros datos de interés a
   través de sus atributos de instancia:

   "parser.largs"
      la lista actual de argumentos que sobran, es decir, argumentos
      que se han consumido pero que no son opciones ni argumentos de
      opción. Siéntete libre de modificar "parser.largs", por ejemplo,
      agregando más argumentos. (Esta lista se convertirá en "args",
      el segundo valor de retorno del método "parse_args()".)

   "parser.rargs"
      la lista actual de argumentos restantes, es decir, los
      argumentos que quedan a continuación de "opt_str" y "value" (si
      corresponde), una vez eliminados ambos. Siéntete libre de
      modificar "parser.rargs", por ejemplo, consumiendo más
      argumentos.

   "parser.values"
      the object where option values are by default stored (an
      instance of optparse.OptionValues).  This lets callbacks use the
      same mechanism as the rest of "optparse" for storing option
      values; you don't need to mess around with globals or closures.
      You can also access or modify the value(s) of any options
      already encountered on the command-line.

"args"
   es una tupla de argumentos posicionales arbitrarios suministrados a
   través del atributo de opción "callback_args".

"kwargs"
   es un diccionario con argumentos por palabra clave arbitrarios
   proporcionados por "callback_kwargs".

### Lanzando errores en una retrollamada

The callback function should raise "OptionValueError" if there are any
problems with the option or its argument(s).  "optparse" catches this
and terminates the program, printing the error message you supply to
stderr.  Your message should be clear, concise, accurate, and mention
the option at fault. Otherwise, the user will have a hard time
figuring out what they did wrong.

### Ejemplo de retrollamada 1: una retrollamada trivial

Aquí hay un ejemplo de una opción con retrollamada que no tiene
argumentos y simplemente registra que se encontró la opción en la
línea de comandos:

   def record_foo_seen(option, opt_str, value, parser):
       parser.values.saw_foo = True

   parser.add_option("--foo", action="callback", callback=record_foo_seen)

Ciertamente, se puede hacer lo mismo simplemente con la acción
""store_true"".

### Ejemplo de retrollamada 2: comprobar el orden de las opciones

Aquí tenemos un ejemplo un poco más interesante: registra el hecho de
que se ha encontrado "-a", pero lanza un error si viene después de
"-b" en la línea de comandos

   def check_order(option, opt_str, value, parser):
       if parser.values.b:
           raise OptionValueError("can't use -a after -b")
       parser.values.a = 1
   ...
   parser.add_option("-a", action="callback", callback=check_order)
   parser.add_option("-b", action="store_true", dest="b")

### Ejemplo de retrollamada 3: comprobar el orden de las opciones (generalizado)

If you want to reuse this callback for several similar options (set a
flag, but blow up if "-b" has already been seen), it needs a bit of
work: the error message and the flag that it sets must be generalized.

   def check_order(option, opt_str, value, parser):
       if parser.values.b:
           raise OptionValueError("can't use %s after -b" % opt_str)
       setattr(parser.values, option.dest, 1)
   ...
   parser.add_option("-a", action="callback", callback=check_order, dest='a')
   parser.add_option("-b", action="store_true", dest="b")
   parser.add_option("-c", action="callback", callback=check_order, dest='c')

### Ejemplo de retrollamada 4: comprobar una condición arbitraria

Por supuesto, puedes poner cualquier condición aquí, no estás limitado
a verificar los valores de las opciones previamente definidas. Por
ejemplo, si tienes opciones que no deberían llamarse cuando hay luna
llena, todo lo que tienes que hacer es lo siguiente:

   def check_moon(option, opt_str, value, parser):
       if is_moon_full():
           raise OptionValueError("%s option invalid when moon is full"
                                  % opt_str)
       setattr(parser.values, option.dest, 1)
   ...
   parser.add_option("--foo",
                     action="callback", callback=check_moon, dest="foo")

(La definición de "is_moon_full()" se deja como ejercicio para el
lector).

### Ejemplo de retrollamada 5: argumentos fijos

Las cosas se ponen un poco más interesantes cuando se definen opciones
con retrollamada que toman un número fijo de argumentos. Especificar
que una opción con retrollamada toma argumentos es similar a definir
una opción ""store"" o ""append"": si se define "type", entonces la
opción toma un argumento que debe poder convertirse a ese tipo; si
además se define "nargs", entonces la opción toma "nargs" argumentos.

Aquí hay un ejemplo que simplemente emula la acción ""store""
estándar:

   def store_value(option, opt_str, value, parser):
       setattr(parser.values, option.dest, value)
   ...
   parser.add_option("--foo",
                     action="callback", callback=store_value,
                     type="int", nargs=3, dest="foo")

Note that "optparse" takes care of consuming 3 arguments and
converting them to integers for you; all you have to do is store them.
(Or whatever; obviously you don't need a callback for this example.)

### Ejemplo de retrollamada 6: argumentos variables

Things get hairy when you want an option to take a variable number of
arguments. For this case, you must write a callback, as "optparse"
doesn't provide any built-in capabilities for it.  And you have to
deal with certain intricacies of conventional Unix command-line
parsing that "optparse" normally handles for you.  In particular,
callbacks should implement the conventional rules for bare "--" and
"-" arguments:

* tanto "--" como "-" pueden ser argumentos de opción

* "--" desnudo (si no es el argumento de alguna opción): detener el
  procesamiento de la línea de comandos y descartar el "--"

* "-" desnudo (si no es el argumento de alguna opción): detener el
  procesamiento de la línea de comandos pero mantener el "-"
  (añadiéndolo a "parser.largs")

If you want an option that takes a variable number of arguments, there
are several subtle, tricky issues to worry about.  The exact
implementation you choose will be based on which trade-offs you're
willing to make for your application (which is why "optparse" doesn't
support this sort of thing directly).

En cualquier caso, aquí hay un intento de una retrollamada para una
opción con un número de argumentos variable:

   def vararg_callback(option, opt_str, value, parser):
       assert value is None
       value = []

       def floatable(str):
           try:
               float(str)
               return True
           except ValueError:
               return False

       for arg in parser.rargs:
           # stop on --foo like options
           if arg[:2] == "--" and len(arg) > 2:
               break
           # stop on -a, but not on -3 or -3.0
           if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
               break
           value.append(arg)

       del parser.rargs[:len(value)]
       setattr(parser.values, option.dest, value)

   ...
   parser.add_option("-c", "--callback", dest="vararg_attr",
                     action="callback", callback=vararg_callback)

## Extending "optparse"

Since the two major controlling factors in how "optparse" interprets
command-line options are the action and type of each option, the most
likely direction of extension is to add new actions and new types.

### Agregando nuevos tipos

To add new types, you need to define your own subclass of "optparse"'s
"Option" class.  This class has a couple of attributes that define
"optparse"'s types: "TYPES" and "TYPE_CHECKER".

Option.TYPES

   Una tupla con nombres de tipos. En tu subclase, simplemente define
   una nueva tupla "TYPES" que se base en la estándar.

Option.TYPE_CHECKER

   Un diccionario que asigna nombres de tipos a funciones de
   verificación de tipo. Una función de verificación de tipo tiene la
   siguiente firma:

      def check_mytype(option, opt, value)

   donde "option" es una instancia de "Option", "opt" es una cadena de
   opción (por ejemplo, "-f") y "value" es la cadena de caracteres de
   la línea de comandos que debe comprobarse y convertirse al tipo
   deseado. "check_mytype()" debería retornar un objeto del tipo
   hipotético "mytype". El valor retornado por una función de
   verificación de tipo terminará formando parte de la instancia de
   OptionValues retornada por el método "OptionParser.parse_args()" o
   será pasada a una retrollamada como parámetro "value".

   Tu función de verificación de tipo debería lanzar una excepción
   "OptionValueError" si encuentra algún problema. "OptionValueError"
   toma una cadena de caracteres como único argumento, que es pasada
   tal cual al método "error()" de la clase "OptionParser", que a su
   vez antepone a la misma el nombre del programa y la cadena
   ""error:"" e imprime todo en la salida de error estándar antes de
   finalizar el proceso.

Here's a silly example that demonstrates adding a ""complex"" option
type to parse Python-style complex numbers on the command line.  (This
is even sillier than it used to be, because "optparse" 1.3 added
built-in support for complex numbers, but never mind.)

Primero, las importaciones necesarias:

   from copy import copy
   from optparse import Option, OptionValueError

En primer lugar, debes definir tu verificador de tipo, ya que se hace
referencia a él más adelante (en el atributo de clase "TYPE_CHECKER"
de tu subclase de Option):

   def check_complex(option, opt, value):
       try:
           return complex(value)
       except ValueError:
           raise OptionValueError(
               "option %s: invalid complex value: %r" % (opt, value))

Finalmente, la subclase de Option:

   class MyOption (Option):
       TYPES = Option.TYPES + ("complex",)
       TYPE_CHECKER = copy(Option.TYPE_CHECKER)
       TYPE_CHECKER["complex"] = check_complex

(If we didn't make a "copy()" of "Option.TYPE_CHECKER", we would end
up modifying the "TYPE_CHECKER" attribute of "optparse"'s Option
class.  This being Python, nothing stops you from doing that except
good manners and common sense.)

That's it!  Now you can write a script that uses the new option type
just like any other "optparse"-based script, except you have to
instruct your OptionParser to use MyOption instead of Option:

   parser = OptionParser(option_class=MyOption)
   parser.add_option("-c", type="complex")

Alternativamente, puedes crear tu propia lista de opciones y pasarla a
OptionParser; si no usas "add_option()" de la manera anterior, no
necesitas decirle a OptionParser qué clase de opción usar:

   option_list = [MyOption("-c", action="store", type="complex", dest="c")]
   parser = OptionParser(option_list=option_list)

### Agregando nuevas acciones

Adding new actions is a bit trickier, because you have to understand
that "optparse" has a couple of classifications for actions:

Acciones "store"
   actions that result in "optparse" storing a value to an attribute
   of the current OptionValues instance; these options require a
   "dest" attribute to be supplied to the Option constructor.

Acciones "typed"
   acciones que toman un valor de la línea de comandos, esperando que
   sea de cierto tipo; o mejor dicho, una cadena de caracteres que se
   pueda convertir a un determinado tipo. Estas opciones requieren un
   atributo "type" para el constructor de Option.

Ambas categorías se solapan entre si: algunas acciones "store"
predeterminadas son ""store"", ""store_const"", ""append"" y
""count"", mientras que las acciones "typed" predeterminadas son
""store"", ""append"" y ""callback"".

Cuando agregas una acción, debes categorizarla enumerándola en al
menos uno de los siguientes atributos de clase de la clase Option
(todos ellos son listas de cadenas de caracteres):

Option.ACTIONS

   Todas las acciones deben aparecer en ACTIONS.

Option.STORE_ACTIONS

   Las acciones "store" también se enumeran aquí.

Option.TYPED_ACTIONS

   Las acciones "typed" también se enumeran aquí.

Option.ALWAYS_TYPED_ACTIONS

   Actions that always take a type (i.e. whose options always take a
   value) are additionally listed here.  The only effect of this is
   that "optparse" assigns the default type, ""string"", to options
   with no explicit type whose action is listed in
   "ALWAYS_TYPED_ACTIONS".

Para implementar realmente tu nueva acción, debes redefinir el método
"take_action()" de Option, implementando un nuevo método que reconozca
tu acción.

Por ejemplo, agreguemos una nueva acción ""extend"". Esta es similar a
la acción estándar ""append"", pero en lugar de tomar un solo valor de
la línea de comandos y agregarlo a una lista existente, ""extend""
tomará múltiples valores en una sola cadena de caracteres delimitada
por comas y amplía una lista previamente existente con ellos. Es
decir, si "--names" es una opción ""extend"" de tipo ""string"", la
línea de comandos

   --names=foo,bar --names blah --names ding,dong

daría como resultado una lista como la siguiente:

   ["foo", "bar", "blah", "ding", "dong"]

De nuevo, definimos una subclase de Option:

   class MyOption(Option):

       ACTIONS = Option.ACTIONS + ("extend",)
       STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
       TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
       ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

       def take_action(self, action, dest, opt, value, values, parser):
           if action == "extend":
               lvalue = value.split(",")
               values.ensure_value(dest, []).extend(lvalue)
           else:
               Option.take_action(
                   self, action, dest, opt, value, values, parser)

Detalles a tener en cuenta:

* ""extend"" espera un valor en la línea de comandos y también
  almacena ese valor en algún lugar, por lo que lo agregamos tanto a
  "STORE_ACTIONS" como a "TYPED_ACTIONS".

* to ensure that "optparse" assigns the default type of ""string"" to
  ""extend"" actions, we put the ""extend"" action in
  "ALWAYS_TYPED_ACTIONS" as well.

* "MyOption.take_action()" implements just this one new action, and
  passes control back to "Option.take_action()" for the standard
  "optparse" actions.

* "values" es una instancia de la clase *optparse_parser.Values*, que
  proporciona el útil método "ensure_value()". El método
  "ensure_value()" es en esencia lo mismo que "getattr()" pero con un
  mecanismo de seguridad agregado. Es llamado como:

     values.ensure_value(attr, value)

  Si el atributo "attr" de "values" no existe o es "None", entonces
  *ensure_value()* primero lo establece en "value" y luego retorna el
  atributo actualizado ("value"). Esto es muy útil para acciones como
  ""extend"", ""append"" y ""count"", dado que todas ellas acumulan
  datos en una variable y esperan que esa variable sea de cierto tipo
  (una lista para las dos primeras, un número entero para la última).
  Usar el método "ensure_value()" significa que los scripts que usan
  tu acción no tienen que preocuparse por establecer un valor
  predeterminado para los destinos de opción en cuestión; simplemente
  pueden dejar el valor predeterminado como "None" y "secure_value()"
  se encargará de que todo esté correcto cuando sea necesario.

## Excepciones

exception optparse.OptionError

   Lanzada si se crea con argumentos inválidos o inconsistentes una
   instancia de "Option".

exception optparse.OptionConflictError

   Lanzada si se añaden opciones que entren en conflicto en una
   "OptionParser".

exception optparse.OptionValueError

   Lanzada si se encuentra una opción inválida en la línea de
   comandos.

exception optparse.BadOptionError

   Lanzada si se pasa una opción inválida en la línea de comandos.

exception optparse.AmbiguousOptionError

   Lanzada si se pasa una opción ambigua en la línea de comandos.
