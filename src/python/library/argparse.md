---
title: '"argparse" --- Parser for command-line options, arguments and subcommands'
source_url: https://docs.python.org/es/3
source_path: library/argparse.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1540
---

# "argparse" --- Parser for command-line options, arguments and subcommands

Added in version 3.2.

**Código fuente:** Lib/argparse.py

Nota:

  While "argparse" is the default recommended standard library module
  for implementing basic command line applications, authors with more
  exacting requirements for exactly how their command line
  applications behave may find it doesn't provide the necessary level
  of control. Refer to Choosing an argument parsing library for
  alternatives to consider when "argparse" doesn't support behaviors
  that the application requires (such as entirely disabling support
  for interspersed options and positional arguments, or accepting
  option parameter values that start with "-" even when they
  correspond to another defined option).

======================================================================

##### Tutorial

Esta página contiene la información de referencia de la API. Para una
introducción más amigable al análisis de la línea de comandos de
Python, echa un vistazo al argparse tutorial.

The "argparse" module makes it easy to write user-friendly command-
line interfaces. The program defines what arguments it requires, and
"argparse" will figure out how to parse those out of "sys.argv".  The
"argparse" module also automatically generates help and usage
messages.  The module will also issue errors when users give the
program invalid arguments.

The "argparse" module's support for command-line interfaces is built
around an instance of "argparse.ArgumentParser".  It is a container
for argument specifications and has options that apply to the parser
as whole:

   parser = argparse.ArgumentParser(
                       prog='ProgramName',
                       description='What the program does',
                       epilog='Text at the bottom of help')

El método "ArgumentParser.add_argument()" adjunta especificaciones de
argumentos individuales al analizador. Soporta argumentos
posicionales, opciones que aceptan valores, y banderas de activación y
desactivación:

   parser.add_argument('filename')           # positional argument
   parser.add_argument('-c', '--count')      # option that takes a value
   parser.add_argument('-v', '--verbose',
                       action='store_true')  # on/off flag

El método "ArgumentParser.parse_args()" corre el analizador y coloca
los datos extraídos en un objeto "argparse.Namespace":

   args = parser.parse_args()
   print(args.filename, args.count, args.verbose)

Nota:

  If you're looking for a guide about how to upgrade "optparse" code
  to "argparse", see Upgrading Optparse Code.

## Objetos *ArgumentParser*

class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True, *, suggest_on_error=False, color=True)

   Crea un nuevo objeto "ArgumentParser". Todos los parámetros deben
   pasarse como argumentos de palabra clave. Cada parámetro tiene su
   propia descripción más detallada a continuación, pero en resumen
   son:

   * prog - The name of the program (default: generated from the
     "__main__" module attributes and "sys.argv[0]")

   * usage - La cadena de caracteres que describe el uso del programa
     (por defecto: generado a partir de los argumentos añadidos al
     analizador)

   * description - Texto a mostrar antes del argumento ayuda (por
     defecto, ninguno)

   * epilog - Texto a mostrar después del argumento ayuda (por
     defecto, ninguno)

   * parents - Una lista de objetos "ArgumentParser" cuyos argumentos
     también deberían ser incluidos

   * formatter_class - Una clase para personalizar la salida de la
     ayuda

   * prefix_chars - El conjunto de caracteres que preceden a los
     argumentos opcionales (por defecto: ‘-‘)

   * fromfile_prefix_chars - El conjunto de caracteres que preceden a
     los archivos de los cuales se deberían leer los argumentos
     adicionales (por defecto: "None")

   * argument_default - El valor global por defecto de los argumentos
     (por defecto: "None")

   * conflict_handler - La estrategia para resolver los opcionales
     conflictivos (normalmente es innecesaria)

   * add_help - Añade una opción "-h/--help" al analizador (por
     defecto: "True")

   * allow_abbrev - Allows long options to be abbreviated if the
     abbreviation is unambiguous (default: "True")

   * exit_on_error - Determines whether or not "ArgumentParser" exits
     with error info when an error occurs. (default: "True")

   * suggest_on_error - Enables suggestions for mistyped argument
     choices and subparser names (default: "False")

   * color - Allow color output (default: "True")

   Distinto en la versión 3.5: se añadió el parámetro *allow_abbrev*.

   Distinto en la versión 3.8: En versiones anteriores, *allow_abbrev*
   también deshabilitaba la agrupación de banderas (*flags*) cortas
   como "-vv" para que sea "-v -v".

   Distinto en la versión 3.9: Se agregó el parámetro *exit_on_error*.

   Distinto en la versión 3.14: *suggest_on_error* and *color*
   parameters were added.

En las siguientes secciones se describe cómo se utiliza cada una de
ellas.

### *prog*

By default, "ArgumentParser" calculates the name of the program to
display in help messages depending on the way the Python interpreter
was run:

* The "base name" of "sys.argv[0]" if a file was passed as argument.

* The Python interpreter name followed by "sys.argv[0]" if a directory
  or a zipfile was passed as argument.

* The Python interpreter name followed by "-m" followed by the module
  or package name if the "-m" option was used.

This default is almost always desirable because it will make the help
messages match the string that was used to invoke the program on the
command line. However, to change this default behavior, another value
can be supplied using the "prog=" argument to "ArgumentParser":

   >>> parser = argparse.ArgumentParser(prog='myprogram')
   >>> parser.print_help()
   usage: myprogram [-h]

   options:
    -h, --help  show this help message and exit

Note that the program name, whether determined from "sys.argv[0]",
from the "__main__" module attributes or from the "prog=" argument, is
available to help messages using the "%(prog)s" format specifier.

   >>> parser = argparse.ArgumentParser(prog='myprogram')
   >>> parser.add_argument('--foo', help='foo of the %(prog)s program')
   >>> parser.print_help()
   usage: myprogram [-h] [--foo FOO]

   options:
    -h, --help  show this help message and exit
    --foo FOO   foo of the myprogram program

Distinto en la versión 3.14: The default "prog" value now reflects how
"__main__" was actually executed, rather than always being
"os.path.basename(sys.argv[0])".

### uso

By default, "ArgumentParser" calculates the usage message from the
arguments it contains. The default message can be overridden with the
"usage=" keyword argument:

   >>> parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
   >>> parser.add_argument('--foo', nargs='?', help='foo help')
   >>> parser.add_argument('bar', nargs='+', help='bar help')
   >>> parser.print_help()
   usage: PROG [options]

   positional arguments:
    bar          bar help

   options:
    -h, --help   show this help message and exit
    --foo [FOO]  foo help

El especificador de formato "%(prog)s" está preparado para introducir
el nombre del programa en los mensajes de ayuda.

When a custom usage message is specified for the main parser, you may
also want to consider passing  the "prog" argument to
"add_subparsers()" or the "prog" and the "usage" arguments to
"add_parser()", to ensure consistent command prefixes and usage
information across subparsers.

### *description*

Most calls to the "ArgumentParser" constructor will use the
"description=" keyword argument.  This argument gives a brief
description of what the program does and how it works.  In help
messages, the description is displayed between the command-line usage
string and the help messages for the various arguments.

Por defecto, la descripción será ajustada a una línea para que encaje
en el espacio dado. Para cambiar este comportamiento, revisa el
argumento formatter_class.

### *epilog*

A algunos programas les gusta mostrar una descripción adicional del
programa después de la descripción de los argumentos. Dicho texto
puede ser especificado usando el argumento "epilog=" para
"ArgumentParser":

   >>> parser = argparse.ArgumentParser(
   ...     description='A foo that bars',
   ...     epilog="And that's how you'd foo a bar")
   >>> parser.print_help()
   usage: argparse.py [-h]

   A foo that bars

   options:
    -h, --help  show this help message and exit

   And that's how you'd foo a bar

Al igual que con el argumento description, el texto "epilog=" está por
defecto ajustado a una línea, pero este comportamiento puede ser
modificado con el argumento formatter_class para "ArgumentParser".

### *parents*

A veces, varios analizadores comparten un conjunto de argumentos
comunes. En lugar de repetir las definiciones de estos argumentos, se
puede usar un único analizador con todos los argumentos compartidos y
pasarlo en el argumento "parents=" a "ArgumentParser". El argumento
"parents=" toma una lista de objetos "ArgumentParser", recoge todas
las acciones de posición y de opción de éstos, y añade estas acciones
al objeto "ArgumentParser" que se está construyendo:

   >>> parent_parser = argparse.ArgumentParser(add_help=False)
   >>> parent_parser.add_argument('--parent', type=int)

   >>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])
   >>> foo_parser.add_argument('foo')
   >>> foo_parser.parse_args(['--parent', '2', 'XXX'])
   Namespace(foo='XXX', parent=2)

   >>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])
   >>> bar_parser.add_argument('--bar')
   >>> bar_parser.parse_args(['--bar', 'YYY'])
   Namespace(bar='YYY', parent=None)

Ten en cuenta que la mayoría de los analizadores padre especificarán
"add_help=False". De lo contrario, el "ArgumentParser" verá dos
opciones "-h/—help" (una para el padre y otra para el hijo) y generará
un error.

Nota:

  Debes inicializar completamente los analizadores antes de pasarlos a
  través de "parents=". Si cambias los analizadores padre después del
  analizador hijo, esos cambios no se reflejarán en el hijo.

### *formatter_class*

Los objetos "ArgumentParser" permiten personalizar el formato de la
ayuda especificando una clase de formato alternativa. Actualmente, hay
cuatro clases de este tipo:

class argparse.RawDescriptionHelpFormatter
class argparse.RawTextHelpFormatter
class argparse.ArgumentDefaultsHelpFormatter
class argparse.MetavarTypeHelpFormatter

"RawDescriptionHelpFormatter" y "RawTextHelpFormatter" dan más control
sobre cómo se muestran las descripciones de texto. Por defecto, los
objetos "ArgumentParser" ajustan a la línea los textos de description
y epilog en los mensajes de ayuda de la línea de comandos:

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     description='''this description
   ...         was indented weird
   ...             but that is okay''',
   ...     epilog='''
   ...             likewise for this epilog whose whitespace will
   ...         be cleaned up and whose words will be wrapped
   ...         across a couple lines''')
   >>> parser.print_help()
   usage: PROG [-h]

   this description was indented weird but that is okay

   options:
    -h, --help  show this help message and exit

   likewise for this epilog whose whitespace will be cleaned up and whose words
   will be wrapped across a couple lines

Pasar "RawDescriptionHelpFormatter" como "formatter_class=" indica que
description y epilog ya tienen el formato correcto y no deben ser
ajustados a la línea:

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     formatter_class=argparse.RawDescriptionHelpFormatter,
   ...     description=textwrap.dedent('''\
   ...         Please do not mess up this text!
   ...         --------------------------------
   ...             I have indented it
   ...             exactly the way
   ...             I want it
   ...         '''))
   >>> parser.print_help()
   usage: PROG [-h]

   Please do not mess up this text!
   --------------------------------
      I have indented it
      exactly the way
      I want it

   options:
    -h, --help  show this help message and exit

"RawTextHelpFormatter" maintains whitespace for all sorts of help
text, including argument descriptions. However, multiple newlines are
replaced with one. If you wish to preserve multiple blank lines, add
spaces between the newlines.

"ArgumentDefaultsHelpFormatter" añade automáticamente información
sobre los valores por defecto a cada uno de los mensajes de ayuda de
los argumentos:

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
   >>> parser.add_argument('--foo', type=int, default=42, help='FOO!')
   >>> parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
   >>> parser.print_help()
   usage: PROG [-h] [--foo FOO] [bar ...]

   positional arguments:
    bar         BAR! (default: [1, 2, 3])

   options:
    -h, --help  show this help message and exit
    --foo FOO   FOO! (default: 42)

"MetavarTypeHelpFormatter" utiliza el nombre del parámetro type para
cada argumento como el nombre a mostrar para sus valores (en lugar de
utilizar dest como lo hace el formato habitual):

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     formatter_class=argparse.MetavarTypeHelpFormatter)
   >>> parser.add_argument('--foo', type=int)
   >>> parser.add_argument('bar', type=float)
   >>> parser.print_help()
   usage: PROG [-h] [--foo int] float

   positional arguments:
     float

   options:
     -h, --help  show this help message and exit
     --foo int

### *prefix_chars*

Most command-line options will use "-" as the prefix, e.g. "-f/--foo".
Parsers that need to support different or additional prefix
characters, e.g. for options like "+f" or "/foo", may specify them
using the "prefix_chars=" argument to the "ArgumentParser"
constructor:

   >>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
   >>> parser.add_argument('+f')
   >>> parser.add_argument('++bar')
   >>> parser.parse_args('+f X ++bar Y'.split())
   Namespace(bar='Y', f='X')

El argumento "prefix_chars=" tiene un valor por defecto de "'-'".
Proporcionar un conjunto de caracteres que no incluya "-" causará que
las opciones "-f/--foo" no sean inhabilitadas.

### *fromfile_prefix_chars*

Algunas veces, cuando se trata de una lista de argumentos
particularmente larga, puede tener sentido mantener la lista de
argumentos en un archivo en lugar de escribirla en la línea de
comandos. Si el argumento "fromfile_prefix_chars=" se da al
constructor "ArgumentParser", entonces los argumentos que empiezan con
cualquiera de los caracteres especificados se tratarán como archivos,
y serán reemplazados por los argumentos que contienen. Por ejemplo:

   >>> with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
   ...     fp.write('-f\nbar')
   ...
   >>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
   >>> parser.add_argument('-f')
   >>> parser.parse_args(['-f', 'foo', '@args.txt'])
   Namespace(f='bar')

Arguments read from a file must be one per line by default (but see
also "convert_arg_line_to_args()") and are treated as if they were in
the same place as the original file referencing argument on the
command line.  So in the example above, the expression "['-f', 'foo',
'@args.txt']" is considered equivalent to the expression "['-f',
'foo', '-f', 'bar']".

Nota:

  Each line is treated as a single argument, so an empty line is read
  as an empty string ("''").

"ArgumentParser" utiliza *codificación del sistema de archivos y
manejador de errores* para leer el archivo que contiene argumentos.

El argumento "fromfile_prefix_chars=" por defecto es "None", lo que
significa que los argumentos nunca serán tratados como referencias de
archivos.

Distinto en la versión 3.12: "ArgumentParser" changed encoding and
errors to read arguments files from default (e.g.
"locale.getpreferredencoding(False)" and ""strict"") to the
*filesystem encoding and error handler*. Arguments file should be
encoded in UTF-8 instead of ANSI Codepage on Windows.

### *argument_default*

Generalmente, los valores por defecto de los argumentos se especifican
ya sea pasando un valor por defecto a "add_argument()" o llamando a
los métodos "set_defaults()" con un conjunto específico de pares
nombre-valor. A veces, sin embargo, puede ser útil especificar un
único valor por defecto para todos los argumentos del analizador. Esto
se puede lograr pasando el argumento de palabra clave
"argument_default=" a "ArgumentParser". Por ejemplo, para suprimir
globalmente la creación de atributos en las llamadas a "parse_args()"
, proporcionamos el argumento "argument_default=SUPPRESS":

   >>> parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
   >>> parser.add_argument('--foo')
   >>> parser.add_argument('bar', nargs='?')
   >>> parser.parse_args(['--foo', '1', 'BAR'])
   Namespace(bar='BAR', foo='1')
   >>> parser.parse_args([])
   Namespace()

### *allow_abbrev*

Normalmente, cuando pasas una lista de argumentos al método
"parse_args()" de un "ArgumentParser", reconoce las abreviaturas de
las opciones largas.

Esta característica puede ser desactivada poniendo "allow_abbrev" a
"False":

   >>> parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
   >>> parser.add_argument('--foobar', action='store_true')
   >>> parser.add_argument('--foonley', action='store_false')
   >>> parser.parse_args(['--foon'])
   usage: PROG [-h] [--foobar] [--foonley]
   PROG: error: unrecognized arguments: --foon

Added in version 3.5.

### *conflict_handler*

Los objetos "ArgumentParser" no permiten dos acciones con la misma
cadena de caracteres de opción. Por defecto, los objetos
"ArgumentParser" lanzan una excepción si se intenta crear un argumento
con una cadena de caracteres de opción que ya está en uso:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-f', '--foo', help='old foo help')
   >>> parser.add_argument('--foo', help='new foo help')
   Traceback (most recent call last):
    ..
   ArgumentError: argument --foo: conflicting option string(s): --foo

A veces (por ejemplo, cuando se utiliza parents) puede ser útil anular
simplemente cualquier argumento antiguo con la misma cadena de
caracteres de opción. Para lograr este comportamiento, se puede
suministrar el valor "'resolve'" al argumento "conflict_handler=" de
"ArgumentParser":

   >>> parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
   >>> parser.add_argument('-f', '--foo', help='old foo help')
   >>> parser.add_argument('--foo', help='new foo help')
   >>> parser.print_help()
   usage: PROG [-h] [-f FOO] [--foo FOO]

   options:
    -h, --help  show this help message and exit
    -f FOO      old foo help
    --foo FOO   new foo help

Ten en cuenta que los objetos "ArgumentParser" sólo eliminan una
acción si todas sus cadenas de caracteres de opción están anuladas.
Así, en el ejemplo anterior, la antigua acción "-f/--foo" se mantiene
como la acción "-f", porque sólo la cadena de caracteres de opción "--
foo" fue anulada.

### *add_help*

By default, "ArgumentParser" objects add an option which simply
displays the parser's help message. If "-h" or "--help" is supplied at
the command line, the "ArgumentParser" help will be printed.

Ocasionalmente, puede ser útil desactivar la inclusión de esta opción
de ayuda. Esto se puede lograr pasando "False" como argumento de
"add_help=" a "ArgumentParser":

   >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
   >>> parser.add_argument('--foo', help='foo help')
   >>> parser.print_help()
   usage: PROG [--foo FOO]

   options:
    --foo FOO  foo help

La opción de ayuda es típicamente "-h/--help". La excepción a esto es
si "prefix_chars=" se especifica y no incluye "-", en cuyo caso "-h" y
"--help" no son opciones válidas. En este caso, el primer carácter en
"prefix_chars" se utiliza para preceder a las opciones de ayuda:

   >>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
   >>> parser.print_help()
   usage: PROG [+h]

   options:
     +h, ++help  show this help message and exit

### exit_on_error

Normally, when you pass an invalid argument list to the "parse_args()"
method of an "ArgumentParser", it will print a *message* to
"sys.stderr" and exit with a status code of 2.

Si el usuario desea detectar errores manualmente, la función se puede
habilitar configurando "exit_on_error" en "False"

   >>> parser = argparse.ArgumentParser(exit_on_error=False)
   >>> parser.add_argument('--integers', type=int)
   _StoreAction(option_strings=['--integers'], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
   >>> try:
   ...     parser.parse_args('--integers a'.split())
   ... except argparse.ArgumentError:
   ...     print('Catching an argumentError')
   ...
   Catching an argumentError

Added in version 3.9.

### suggest_on_error

By default, when a user passes an invalid argument choice or subparser
name, "ArgumentParser" will exit with error info and list the
permissible argument choices (if specified) or subparser names as part
of the error message.

If the user would like to enable suggestions for mistyped argument
choices and subparser names, the feature can be enabled by setting
"suggest_on_error" to "True". Note that this only applies for
arguments when the choices specified are strings:

   >>> parser = argparse.ArgumentParser(suggest_on_error=True)
   >>> parser.add_argument('--action', choices=['debug', 'dryrun'])
   >>> parser.parse_args(['--action', 'debugg'])
   usage: tester.py [-h] [--action {debug,dryrun}]
   tester.py: error: argument --action: invalid choice: 'debugg', maybe you meant 'debug'? (choose from debug, dryrun)

If you're writing code that needs to be compatible with older Python
versions and want to opportunistically use "suggest_on_error" when
it's available, you can set it as an attribute after initializing the
parser instead of using the keyword argument:

   >>> parser = argparse.ArgumentParser(description='Process some integers.')
   >>> parser.suggest_on_error = True

Added in version 3.14.

### color

By default, the help message is printed in color using ANSI escape
sequences. If you want plain text help messages, you can disable this
in your local environment, or in the argument parser itself by setting
"color" to "False":

   >>> parser = argparse.ArgumentParser(description='Process some integers.',
   ...                                  color=False)
   >>> parser.add_argument('--action', choices=['sum', 'max'])
   >>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
   ...                     help='an integer for the accumulator')
   >>> parser.parse_args(['--help'])

Note that when "color=True", colored output depends on both
environment variables and terminal capabilities.  However, if
"color=False", colored output is always disabled, even if environment
variables like "FORCE_COLOR" are set.

Nota:

  Error messages will include color codes when redirecting stderr to a
  file. To avoid this, set the "NO_COLOR" or "PYTHON_COLORS"
  environment variable (for example, "NO_COLOR=1 python script.py 2>
  errors.txt").

Added in version 3.14.

## El método *add_argument()*

ArgumentParser.add_argument(name or flags..., *[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest][, deprecated])

   Define cómo se debe interpretar un determinado argumento de línea
   de comandos. Cada parámetro tiene su propia descripción más
   detallada a continuación, pero en resumen son:

   * name or flags - Either a name or a list of option strings, e.g.
     "'foo'" or "'-f', '--foo'".

   * action - El tipo básico de acción a tomar cuando este argumento
     se encuentra en la línea de comandos.

   * nargs - El número de argumentos de la línea de comandos que deben
     ser consumidos.

   * const - Un valor fijo requerido por algunas selecciones de action
     y nargs.

   * default - El valor producido si el argumento está ausente en la
     línea de comando y si está ausente en el objeto de espacio de
     nombres.

   * type - El tipo al que debe convertirse el argumento de la línea
     de comandos.

   * choices - Una secuencia de valores permitidos para el argumento.

   * required - Si se puede omitir o no la opción de la línea de
     comandos (sólo opcionales).

   * help - Una breve descripción de lo que hace el argumento.

   * metavar - Un nombre para el argumento en los mensajes de uso.

   * dest - El nombre del atributo que será añadido al objeto
     retornado por "parse_args()".

   * deprecated - Whether or not use of the argument is deprecated.

   The method returns an "Action" object representing the argument.

En las siguientes secciones se describe cómo se utiliza cada una de
ellas.

### *name or flags*

El método "add_argument()" debe saber si espera un argumento opcional,
como "-f" o "--foo", o un argumento posicional, como una lista de
nombres de archivos. Los primeros argumentos que se pasan a
"add_argument()" deben ser o bien una serie de banderas (*flags*), o
un simple nombre de un argumento (*name*).

Por ejemplo, se puede crear un argumento opcional como:

   >>> parser.add_argument('-f', '--foo')

mientras que un argumento posicional podría ser creado como:

   >>> parser.add_argument('bar')

Cuando se llama a "parse_args()" , los argumentos opcionales serán
identificados por el prefijo "-", y el resto de los argumentos serán
asumidos como posicionales:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-f', '--foo')
   >>> parser.add_argument('bar')
   >>> parser.parse_args(['BAR'])
   Namespace(bar='BAR', foo=None)
   >>> parser.parse_args(['BAR', '--foo', 'FOO'])
   Namespace(bar='BAR', foo='FOO')
   >>> parser.parse_args(['--foo', 'FOO'])
   usage: PROG [-h] [-f FOO] bar
   PROG: error: the following arguments are required: bar

By default, "argparse" automatically handles the internal naming and
display names of arguments, simplifying the process without requiring
additional configuration. As such, you do not need to specify the dest
and metavar parameters. For optional arguments, the dest parameter
defaults to the argument name, with underscores "_" replacing hyphens
"-". The metavar parameter defaults to the upper-cased name. For
example:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('--foo-bar')
   >>> parser.parse_args(['--foo-bar', 'FOO-BAR'])
   Namespace(foo_bar='FOO-BAR')
   >>> parser.print_help()
   usage:  [-h] [--foo-bar FOO-BAR]

   optional arguments:
    -h, --help  show this help message and exit
    --foo-bar FOO-BAR

### *action*

Los objetos "ArgumentParser" asocian los argumentos de la línea de
comandos con las acciones. Esta acciones pueden hacer casi cualquier
cosa con los argumentos de línea de comandos asociados a ellas, aunque
la mayoría de las acciones simplemente añaden un atributo al objeto
retornado por "parse_args()". El argumento de palabra clave "action"
especifica cómo deben ser manejados los argumentos de la línea de
comandos. Las acciones proporcionadas son:

* "'store'" - This just stores the argument's value.  This is the
  default action.

* "'store_const'" - Esto almacena el valor especificado por el
  argumento de palabra clave const; nótese que el argumento de palabra
  clave const por defecto es "None". La acción "'store_const'" se usa
  comúnmente con argumentos opcionales que especifican algún tipo de
  indicador (*flag*). Por ejemplo:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', action='store_const', const=42)
     >>> parser.parse_args(['--foo'])
     Namespace(foo=42)

* "'store_true'" and "'store_false'" - These are special cases of
  "'store_const'" that respectively store the values "True" and
  "False" with default values of "False" and "True":

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', action='store_true')
     >>> parser.add_argument('--bar', action='store_false')
     >>> parser.add_argument('--baz', action='store_false')
     >>> parser.parse_args('--foo --bar'.split())
     Namespace(foo=True, bar=False, baz=True)

* "'append'" - This appends each argument value to a list. It is
  useful for allowing an option to be specified multiple times. If the
  default value is a non-empty list, the parsed value will start with
  the default list's elements and any values from the command line
  will be appended after those default values. Example usage:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', action='append', default=['0'])
     >>> parser.parse_args('--foo 1 --foo 2'.split())
     Namespace(foo=['0', '1', '2'])

* "'append_const'" - This appends the value specified by the const
  keyword argument to a list; note that the const keyword argument
  defaults to "None". The "'append_const'" action is typically useful
  when multiple arguments need to store constants to the same list.
  For example:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--str', dest='types', action='append_const', const=str)
     >>> parser.add_argument('--int', dest='types', action='append_const', const=int)
     >>> parser.parse_args('--str --int'.split())
     Namespace(types=[<class 'str'>, <class 'int'>])

* "'extend'" - This appends each item from a multi-value argument to a
  list. The "'extend'" action is typically used with the nargs keyword
  argument value "'+'" or "'*'". Note that when nargs is "None" (the
  default) or "'?'", each character of the argument string will be
  appended to the list. Example usage:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument("--foo", action="extend", nargs="+", type=str)
     >>> parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"])
     Namespace(foo=['f1', 'f2', 'f3', 'f4'])

  Added in version 3.8.

* "'count'" - This counts the number of times an argument occurs. For
  example, this is useful for increasing verbosity levels:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--verbose', '-v', action='count', default=0)
     >>> parser.parse_args(['-vvv'])
     Namespace(verbose=3)

  Observa, *default* (el valor por defecto) será "None" a menos que
  explícitamente se establezca como *0*.

* "'help'" - Esta imprime un mensaje de ayuda completo para todas las
  opciones del analizador actual y luego termina. Por defecto, se
  añade una acción de ayuda automáticamente al analizador. Ver
  "ArgumentParser" para detalles de cómo se genera la salida.

* "’version’" - Esta espera un argumento de palabra clave "version="
  en la llamada "add_argument()", e imprime la información de la
  versión y finaliza cuando es invocada:

     >>> import argparse
     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
     >>> parser.parse_args(['--version'])
     PROG 2.0

You may also specify an arbitrary action by passing an "Action"
subclass (e.g. "BooleanOptionalAction") or other object that
implements the same interface. Only actions that consume command-line
arguments (e.g. "'store'", "'append'", "'extend'", or custom actions
with non-zero "nargs") can be used with positional arguments.

The recommended way to create a custom action is to extend "Action",
overriding the "__call__()" method and optionally the "__init__()" and
"format_usage()" methods. You can also register custom actions using
the "register()" method and reference them by their registered name.

Un ejemplo de una acción personalizada:

   >>> class FooAction(argparse.Action):
   ...     def __init__(self, option_strings, dest, nargs=None, **kwargs):
   ...         if nargs is not None:
   ...             raise ValueError("nargs not allowed")
   ...         super().__init__(option_strings, dest, **kwargs)
   ...     def __call__(self, parser, namespace, values, option_string=None):
   ...         print('%r %r %r' % (namespace, values, option_string))
   ...         setattr(namespace, self.dest, values)
   ...
   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', action=FooAction)
   >>> parser.add_argument('bar', action=FooAction)
   >>> args = parser.parse_args('1 --foo 2'.split())
   Namespace(bar=None, foo=None) '1' None
   Namespace(bar='1', foo=None) '2' '--foo'
   >>> args
   Namespace(bar='1', foo='2')

Para más detalles, ver "Action".

### *nargs*

"ArgumentParser" objects usually associate a single command-line
argument with a single action to be taken.  The "nargs" keyword
argument associates a different number of command-line arguments with
a single action. See also Especificando argumentos ambiguos. The
supported values are:

* "N" (un entero). "N" argumentos de la línea de comandos se agruparán
  en una lista. Por ejemplo:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', nargs=2)
     >>> parser.add_argument('bar', nargs=1)
     >>> parser.parse_args('c --foo a b'.split())
     Namespace(bar=['c'], foo=['a', 'b'])

  Ten en cuenta que "nargs=1" produce una lista de un elemento. Esto
  es diferente del valor por defecto, en el que el elemento se produce
  por sí mismo.

* "’?’". Un argumento se consumirá desde la línea de comandos si es
  posible, y se generará como un sólo elemento. Si no hay ningún
  argumento de línea de comandos, se obtendrá el valor de default. Ten
  en cuenta que para los argumentos opcionales, hay un caso adicional
  - la cadena de caracteres de opción está presente pero no va seguida
  de un argumento de línea de comandos. En este caso se obtendrá el
  valor de const. Algunos ejemplos para ilustrar esto:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', nargs='?', const='c', default='d')
     >>> parser.add_argument('bar', nargs='?', default='d')
     >>> parser.parse_args(['XX', '--foo', 'YY'])
     Namespace(bar='XX', foo='YY')
     >>> parser.parse_args(['XX', '--foo'])
     Namespace(bar='XX', foo='c')
     >>> parser.parse_args([])
     Namespace(bar='d', foo='d')

  Uno de los usos más comunes de "nargs='?'" es permitir archivos de
  entrada y salida opcionales:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('infile', nargs='?')
     >>> parser.add_argument('outfile', nargs='?')
     >>> parser.parse_args(['input.txt', 'output.txt'])
     Namespace(infile='input.txt', outfile='output.txt')
     >>> parser.parse_args(['input.txt'])
     Namespace(infile='input.txt', outfile=None)
     >>> parser.parse_args([])
     Namespace(infile=None, outfile=None)

* "’*’". Todos los argumentos presentes en la línea de comandos se
  recogen en una lista. Ten en cuenta que generalmente no tiene mucho
  sentido tener más de un argumento posicional con "nargs=‘*’", pero
  es posible tener múltiples argumentos opcionales con "nargs=‘*’".
  Por ejemplo:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', nargs='*')
     >>> parser.add_argument('--bar', nargs='*')
     >>> parser.add_argument('baz', nargs='*')
     >>> parser.parse_args('a b --foo x y --bar 1 2'.split())
     Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

* "'+'". Just like "'*'", all command-line arguments present are
  gathered into a list.  Additionally, an error message will be
  generated if there wasn't at least one command-line argument
  present.  For example:

     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> parser.add_argument('foo', nargs='+')
     >>> parser.parse_args(['a', 'b'])
     Namespace(foo=['a', 'b'])
     >>> parser.parse_args([])
     usage: PROG [-h] foo [foo ...]
     PROG: error: the following arguments are required: foo

If the "nargs" keyword argument is not provided, the number of
arguments consumed is determined by the action.  Generally this means
a single command-line argument will be consumed and a single item (not
a list) will be produced. Actions that do not consume command-line
arguments (e.g. "'store_const'") set "nargs=0".

### *const*

El argumento "const" de "add_argument()" se usa para mantener valores
constantes que no se leen desde la línea de comandos pero que son
necesarios para las diversas acciones de "ArgumentParser". Los dos
usos más comunes son:

* Cuando "add_argument()" es llamado con "action='store_const'" o
  "action='append_const'". Estas acciones añaden el valor "const" a
  uno de los atributos del objeto retornado por "parse_args()". Mira
  la descripción action para ver ejemplos. Si "const" no es
  proporcionado a "add_argument()", este recibirá el valor por defecto
  "None".

* When "add_argument()" is called with option strings (like "-f" or "
  --foo") and "nargs='?'".  This creates an optional argument that can
  be followed by zero or one command-line arguments. When parsing the
  command line, if the option string is encountered with no command-
  line argument following it, the value from "const" will be used. See
  the nargs description for examples.

Distinto en la versión 3.11: Por defecto "const=None", incluyendo
cuando "action='append_const'" o "action='store_const'".

### *default*

Todos los argumentos opcionales y algunos argumentos posicionales
pueden ser omitidos en la línea de comandos. El argumento de palabra
clave "default" de "add_argument()", cuyo valor por defecto es "None",
especifica qué valor debe usarse si el argumento de línea de comandos
no está presente. Para los argumentos opcionales, se usa el valor
"default" cuando la cadena de caracteres de opción no está presente en
la línea de comandos:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', default=42)
   >>> parser.parse_args(['--foo', '2'])
   Namespace(foo='2')
   >>> parser.parse_args([])
   Namespace(foo=42)

If the target namespace already has an attribute set, the action
*default* will not overwrite it:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', default=42)
   >>> parser.parse_args([], namespace=argparse.Namespace(foo=101))
   Namespace(foo=101)

Si el valor "default" es una cadena de caracteres, el analizador
procesa el valor como si fuera un argumento de la línea de comandos.
En particular, el analizador aplica cualquier argumento de conversión
type , si se proporciona, antes de establecer el atributo en el valor
de retorno "Namespace". En caso contrario, el analizador utiliza el
valor tal y como es:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--length', default='10', type=int)
   >>> parser.add_argument('--width', default=10.5, type=int)
   >>> parser.parse_args()
   Namespace(length=10, width=10.5)

Para argumentos posiciones con nargs igual a "?" o "*", el valor
"default" se utiliza cuando no hay ningún argumento de línea de
comandos presente:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('foo', nargs='?', default=42)
   >>> parser.parse_args(['a'])
   Namespace(foo='a')
   >>> parser.parse_args([])
   Namespace(foo=42)

Because "nargs='*'" gathers any supplied values into a list, an absent
positional argument yields an empty list ("[]"). Only a non-"None"
*default* overrides this (so "default=None" still gives "[]").

For required arguments, the "default" value is ignored. For example,
this applies to positional arguments with nargs values other than "?"
or "*", or optional arguments marked as "required=True".

Proporcionar "default=argparse.SUPPRESS" causa que no se agregue
ningún atributo si el argumento de la línea de comandos no está
presente:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', default=argparse.SUPPRESS)
   >>> parser.parse_args([])
   Namespace()
   >>> parser.parse_args(['--foo', '1'])
   Namespace(foo='1')

### *type*

De forma predeterminada, el analizador lee los argumentos de la línea
de comandos como cadenas simples. Sin embargo, a menudo, la cadena de
la línea de comandos debe interpretarse como otro tipo, como "float" o
"int". La palabra clave "type" para "add_argument()" permite realizar
cualquier verificación de tipo y conversión de tipo necesaria.

Si la palabra clave type se usa con la palabra clave default, el
convertidor de tipos solo se aplica si el valor predeterminado es una
cadena de caracteres.

The argument to "type" can be a callable that accepts a single string
or the name of a registered type (see "register()") If the function
raises "ArgumentTypeError", "TypeError", or "ValueError", the
exception is caught and a nicely formatted error message is displayed.
Other exception types are not handled.

Los tipos y funciones incorporados comunes se pueden utilizar como
convertidores de tipos:

   import argparse
   import pathlib

   parser = argparse.ArgumentParser()
   parser.add_argument('count', type=int)
   parser.add_argument('distance', type=float)
   parser.add_argument('street', type=ascii)
   parser.add_argument('code_point', type=ord)
   parser.add_argument('datapath', type=pathlib.Path)

Las funciones definidas por el usuario también se pueden utilizar:

   >>> def hyphenated(string):
   ...     return '-'.join([word[:4] for word in string.casefold().split()])
   ...
   >>> parser = argparse.ArgumentParser()
   >>> _ = parser.add_argument('short_title', type=hyphenated)
   >>> parser.parse_args(['"The Tale of Two Cities"'])
   Namespace(short_title='"the-tale-of-two-citi')

The "bool()" function is not recommended as a type converter.  All it
does is convert empty strings to "False" and non-empty strings to
"True". This is usually not what is desired:

   >>> parser = argparse.ArgumentParser()
   >>> _ = parser.add_argument('--verbose', type=bool)
   >>> parser.parse_args(['--verbose', 'False'])
   Namespace(verbose=True)

See "BooleanOptionalAction" or "action='store_true'" for common
alternatives.

En general, la palabra clave "type" es una conveniencia que solo debe
usarse para conversiones simples que solo pueden generar una de las
tres excepciones admitidas. Cualquier cosa con un manejo de errores o
de recursos más interesante debe hacerse en sentido descendente
después de analizar los argumentos.

Por ejemplo, las conversiones JSON o YAML tienen casos de error
complejos que requieren mejores informes que los que puede
proporcionar la palabra clave "type". Un "JSONDecodeError" no estaría
bien formateado y un "FileNotFoundError" no se manejaría en absoluto.

Even "FileType" has its limitations for use with the "type" keyword.
If one argument uses "FileType" and then a subsequent argument fails,
an error is reported but the file is not automatically closed.  In
this case, it would be better to wait until after the parser has run
and then use the "with"-statement to manage the files.

Para los verificadores de tipo que simplemente verifican un conjunto
fijo de valores, considere usar la palabra clave choices en su lugar.

### *choices*

Algunos argumentos de la línea de comandos deberían seleccionarse de
un conjunto restringido de valores. Estos pueden ser manejados pasando
un objeto de secuencia como el argumento de palabra clave *choices* a
"add_argument()". Cuando se analiza la línea de comandos, se
comprueban los valores de los argumentos y se muestra un mensaje de
error si el argumento no era uno de los valores aceptables:

   >>> parser = argparse.ArgumentParser(prog='game.py')
   >>> parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
   >>> parser.parse_args(['rock'])
   Namespace(move='rock')
   >>> parser.parse_args(['fire'])
   usage: game.py [-h] {rock,paper,scissors}
   game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
   'paper', 'scissors')

Se puede pasar cualquier secuencia como el valor para *choices*, así
que los objetos "list", "tuple" , y las secuencias personalizadas
están soportados.

No se recomienda el uso de "enum.Enum" porque es difícil controlar su
apariencia en el uso, la ayuda y los mensajes de error.

Note that *choices* are checked after any type conversions have been
performed, so objects in *choices* should match the type specified.
This can make *choices* appear unfamiliar in usage, help, or error
messages.

To keep *choices* user-friendly, consider a custom type wrapper that
converts and formats values, or omit type and handle conversion in
your application code.

Las opciones formateadas anulan el *metavar* predeterminado que
normalmente se deriva de *dest*. Esto suele ser lo que se quiere
porque el usuario nunca ve el parámetro *dest*. Si esta visualización
no es deseable (quizás porque hay muchas opciones), simplemente
especifique un metavar explícito.

### *required*

In general, the "argparse" module assumes that flags like "-f" and "--
bar" indicate *optional* arguments, which can always be omitted at the
command line. To make an option *required*, "True" can be specified
for the "required=" keyword argument to "add_argument()":

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', required=True)
   >>> parser.parse_args(['--foo', 'BAR'])
   Namespace(foo='BAR')
   >>> parser.parse_args([])
   usage: [-h] --foo FOO
   : error: the following arguments are required: --foo

Como muestra el ejemplo, si una opción está marcada como "required",
"parse_args()" informará de un error si esa opción no está presente en
la línea de comandos.

Nota:

  Las opciones requeridas están consideradas generalmente mala
  práctica porque los usuarios esperan que las *opciones* sean
  *opcionales*, y por lo tanto deberían ser evitadas cuando sea
  posible.

### *help*

The "help" value is a string containing a brief description of the
argument. When a user requests help (usually by using "-h" or "--help"
at the command line), these "help" descriptions will be displayed with
each argument.

Las cadenas de texto "help" pueden incluir varios descriptores de
formato para evitar la repetición de cosas como el nombre del programa
o el argumento default. Los descriptores disponibles incluyen el
nombre del programa, "%(prog)s" y la mayoría de los argumentos de
palabra clave de "add_argument()", por ejemplo "%(default)s",
"%(type)s", etc.:

   >>> parser = argparse.ArgumentParser(prog='frobble')
   >>> parser.add_argument('bar', nargs='?', type=int, default=42,
   ...                     help='the bar to %(prog)s (default: %(default)s)')
   >>> parser.print_help()
   usage: frobble [-h] [bar]

   positional arguments:
    bar     the bar to frobble (default: 42)

   options:
    -h, --help  show this help message and exit

Como la cadena de caracteres de ayuda soporta el formato-%, si se
quiere que aparezca un "%" literal en la cadena de caracteres de
ayuda, se debe escribir como "%%".

"argparse" supports silencing the help entry for certain options, by
setting the "help" value to "argparse.SUPPRESS":

   >>> parser = argparse.ArgumentParser(prog='frobble')
   >>> parser.add_argument('--foo', help=argparse.SUPPRESS)
   >>> parser.print_help()
   usage: frobble [-h]

   options:
     -h, --help  show this help message and exit

### *metavar*

When "ArgumentParser" generates help messages, it needs some way to
refer to each expected argument.  By default, "ArgumentParser" objects
use the dest value as the "name" of each object.  By default, for
positional argument actions, the dest value is used directly, and for
optional argument actions, the dest value is uppercased.  So, a single
positional argument with "dest='bar'" will be referred to as "bar". A
single optional argument "--foo" that should be followed by a single
command-line argument will be referred to as "FOO".  An example:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo')
   >>> parser.add_argument('bar')
   >>> parser.parse_args('X --foo Y'.split())
   Namespace(bar='X', foo='Y')
   >>> parser.print_help()
   usage:  [-h] [--foo FOO] bar

   positional arguments:
    bar

   options:
    -h, --help  show this help message and exit
    --foo FOO

Un nombre alternativo se puede especificar con "metavar":

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', metavar='YYY')
   >>> parser.add_argument('bar', metavar='XXX')
   >>> parser.parse_args('X --foo Y'.split())
   Namespace(bar='X', foo='Y')
   >>> parser.print_help()
   usage:  [-h] [--foo YYY] XXX

   positional arguments:
    XXX

   options:
    -h, --help  show this help message and exit
    --foo YYY

Ten en cuenta que "metavar" sólo cambia el nombre *mostrado* - el
nombre del atributo en el objeto "parse_args()" sigue estando
determinado por el valor dest.

Diferentes valores de "nargs" pueden causar que *metavar* sea usado
múltiples veces. Proporcionar una tupla a "metavar" especifica una
visualización diferente para cada uno de los argumentos:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x', nargs=2)
   >>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
   >>> parser.print_help()
   usage: PROG [-h] [-x X X] [--foo bar baz]

   options:
    -h, --help     show this help message and exit
    -x X X
    --foo bar baz

### *dest*

La mayoría de las acciones "ArgumentParser" añaden algún valor como
atributo del objeto retornado por "parse_args()". El nombre de este
atributo está determinado por el argumento de palabra clave "dest" de
"add_argument()". Para acciones de argumento posicional, se
proporciona "dest" normalmente como primer argumento de
"add_argument()":

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('bar')
   >>> parser.parse_args(['XXX'])
   Namespace(bar='XXX')

Para las acciones de argumentos opcionales, el valor de "dest" se
infiere normalmente de las cadenas de caracteres de opción.
"ArgumentParser" genera el valor de "dest" tomando la primera cadena
de caracteres de opción larga y quitando la cadena inicial "--". Si no
se proporcionaron cadenas de caracteres de opción largas, "dest" se
derivará de la primera cadena de caracteres de opción corta quitando
el carácter "-". Cualquier carácter "-" interno se convertirá a
caracteres "_" para asegurarse de que la cadena de caracteres es un
nombre de atributo válido. Los ejemplos siguientes ilustran este
comportamiento:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('-f', '--foo-bar', '--foo')
   >>> parser.add_argument('-x', '-y')
   >>> parser.parse_args('-f 1 -x 2'.split())
   Namespace(foo_bar='1', x='2')
   >>> parser.parse_args('--foo 1 -y 2'.split())
   Namespace(foo_bar='1', x='2')

"dest" permite que se proporcione un nombre de atributo personalizado:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', dest='bar')
   >>> parser.parse_args('--foo XXX'.split())
   Namespace(bar='XXX')

Multiple arguments may share the same "dest".  By default, the value
from the last such argument given on the command line wins.  Use
"action='append'" to collect values from all of them into a list
instead.  For conflicting *option strings* rather than "dest" names,
see conflict_handler.

### deprecated

During a project's lifetime, some arguments may need to be removed
from the command line. Before removing them, you should inform your
users that the arguments are deprecated and will be removed. The
"deprecated" keyword argument of "add_argument()", which defaults to
"False", specifies if the argument is deprecated and will be removed
in the future. For arguments, if "deprecated" is "True", then a
warning will be printed to "sys.stderr" when the argument is used:

   >>> import argparse
   >>> parser = argparse.ArgumentParser(prog='snake.py')
   >>> parser.add_argument('--legs', default=0, type=int, deprecated=True)
   >>> parser.parse_args([])
   Namespace(legs=0)
   >>> parser.parse_args(['--legs', '4'])
   snake.py: warning: option '--legs' is deprecated
   Namespace(legs=4)

Added in version 3.13.

### Las clases *Action*

"Action" classes implement the Action API, a callable which returns a
callable which processes arguments from the command-line. Any object
which follows this API may be passed as the "action" parameter to
"add_argument()".

class argparse.Action(option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None)

   "Action" objects are used by an "ArgumentParser" to represent the
   information needed to parse a single argument from one or more
   strings from the command line. The "Action" class must accept the
   two positional arguments plus any keyword arguments passed to
   "ArgumentParser.add_argument()" except for the "action" itself.

   Instances of "Action" (or return value of any callable to the
   "action" parameter) should have attributes "dest",
   "option_strings", "default", "type", "required", "help", etc.
   defined. The easiest way to ensure these attributes are defined is
   to call "Action.__init__()".

   __call__(parser, namespace, values, option_string=None)

      "Action" instances should be callable, so subclasses must
      override the "__call__()" method, which should accept four
      parameters:

      * *parser* - The "ArgumentParser" object which contains this
        action.

      * *namespace* - The "Namespace" object that will be returned by
        "parse_args()".  Most actions add an attribute to this object
        using "setattr()".

      * *values* - The associated command-line arguments, with any
        type conversions applied.  Type conversions are specified with
        the type keyword argument to "add_argument()".

      * *option_string* - The option string that was used to invoke
        this action. The "option_string" argument is optional, and
        will be absent if the action is associated with a positional
        argument.

      The "__call__()" method may perform arbitrary actions, but will
      typically set attributes on the "namespace" based on "dest" and
      "values".

   format_usage()

      "Action" subclasses can define a "format_usage()" method that
      takes no argument and return a string which will be used when
      printing the usage of the program. If such method is not
      provided, a sensible default will be used.

class argparse.BooleanOptionalAction

   A subclass of "Action" for handling boolean flags with positive and
   negative options. Adding a single argument such as "--foo"
   automatically creates both "--foo" and "--no-foo" options, storing
   "True" and "False" respectively:

      >>> import argparse
      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', action=argparse.BooleanOptionalAction)
      >>> parser.parse_args(['--no-foo'])
      Namespace(foo=False)

   Added in version 3.9.

## El método *parse_args()*

ArgumentParser.parse_args(args=None, namespace=None)

   Convierte las cadenas de caracteres de argumentos en objetos y los
   asigna como atributos del espacio de nombres (*namespace*). Retorna
   el espacio de nombres (*namespace*) ocupado.

   Previous calls to "add_argument()" determine exactly what objects
   are created and how they are assigned. See the documentation for
   "add_argument()" for details.

   * args - Lista de cadenas de caracteres para analizar. El valor por
     defecto se toma de "sys.argv".

   * namespace - Un objeto para obtener los atributos. Por defecto es
     un nuevo objeto vacío "Namespace".

### Sintaxis del valor de la opción

El método "parse_args()" soporta diversas formas de especificar el
valor de una opción (si requiere uno). En el caso más simple, la
opción y su valor se pasan como dos argumentos separados:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x')
   >>> parser.add_argument('--foo')
   >>> parser.parse_args(['-x', 'X'])
   Namespace(foo=None, x='X')
   >>> parser.parse_args(['--foo', 'FOO'])
   Namespace(foo='FOO', x=None)

En el caso de opciones largas (opciones con nombres más largos que un
sólo carácter), la opción y el valor también se pueden pasar como un
sólo argumento de línea de comandos, utilizando "=" para separarlos:

   >>> parser.parse_args(['--foo=FOO'])
   Namespace(foo='FOO', x=None)

Para las opciones cortas (opciones de un sólo carácter de largo), la
opción y su valor pueden ser concatenados:

   >>> parser.parse_args(['-xX'])
   Namespace(foo=None, x='X')

Se pueden unir varias opciones cortas, usando un sólo prefijo "-",
siempre y cuando sólo la última opción (o ninguna de ellas) requiera
un valor:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x', action='store_true')
   >>> parser.add_argument('-y', action='store_true')
   >>> parser.add_argument('-z')
   >>> parser.parse_args(['-xyzZ'])
   Namespace(x=True, y=True, z='Z')

### Argumentos no válidos

Mientras analiza la línea de comandos, "parse_args()" comprueba una
variedad de errores, incluyendo opciones ambiguas, tipos no válidos,
opciones no válidas, número incorrecto de argumentos de posición, etc.
Cuando encuentra un error de este tipo, termina y muestra el error
junto con un mensaje de uso:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('--foo', type=int)
   >>> parser.add_argument('bar', nargs='?')

   >>> # invalid type
   >>> parser.parse_args(['--foo', 'spam'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: argument --foo: invalid int value: 'spam'

   >>> # invalid option
   >>> parser.parse_args(['--bar'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: no such option: --bar

   >>> # wrong number of arguments
   >>> parser.parse_args(['spam', 'badger'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: extra arguments found: badger

### Argumentos conteniendo "-"

El método "parse_args()" busca generar errores cuando el usuario ha
cometido claramente una equivocación, pero algunas situaciones son
inherentemente ambiguas. Por ejemplo, el argumento de línea de
comandos "-1" podría ser un intento de especificar una opción o un
intento de proporcionar un argumento de posición. El método
"parse_args()" es cauteloso aquí: los argumentos de posición sólo
pueden comenzar con "-" si se ven como números negativos y no hay
opciones en el analizador que se puedan ver como números negativos

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x')
   >>> parser.add_argument('foo', nargs='?')

   >>> # no negative number options, so -1 is a positional argument
   >>> parser.parse_args(['-x', '-1'])
   Namespace(foo=None, x='-1')

   >>> # no negative number options, so -1 and -5 are positional arguments
   >>> parser.parse_args(['-x', '-1', '-5'])
   Namespace(foo='-5', x='-1')

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-1', dest='one')
   >>> parser.add_argument('foo', nargs='?')

   >>> # negative number options present, so -1 is an option
   >>> parser.parse_args(['-1', 'X'])
   Namespace(foo=None, one='X')

   >>> # negative number options present, so -2 is an option
   >>> parser.parse_args(['-2'])
   usage: PROG [-h] [-1 ONE] [foo]
   PROG: error: no such option: -2

   >>> # negative number options present, so both -1s are options
   >>> parser.parse_args(['-1', '-1'])
   usage: PROG [-h] [-1 ONE] [foo]
   PROG: error: argument -1: expected one argument

Si tienes argumentos de posición que deben comenzar con "-" y no
parecen números negativos, puedes insertar el pseudo-argumento "'--'"
que indica a "parse_args()" que todo lo que sigue es un argumento de
posición:

   >>> parser.parse_args(['--', '-f'])
   Namespace(foo='-f', one=None)

También ver la guía de argparse sobre cómo manejar argumentos ambiguos
para más detalles.

### Abreviaturas de los argumentos (coincidencia de prefijos)

El método "parse_args()" por defecto permite abreviar las opciones
largas a un prefijo, si la abreviatura es inequívoca (el prefijo
coincide con una opción única):

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-bacon')
   >>> parser.add_argument('-badger')
   >>> parser.parse_args('-bac MMM'.split())
   Namespace(bacon='MMM', badger=None)
   >>> parser.parse_args('-bad WOOD'.split())
   Namespace(bacon=None, badger='WOOD')
   >>> parser.parse_args('-ba BA'.split())
   usage: PROG [-h] [-bacon BACON] [-badger BADGER]
   PROG: error: ambiguous option: -ba could match -badger, -bacon

Se incurre en un error por argumentos que podrían derivar en más de
una opción. Esta característica puede ser desactivada poniendo
allow_abbrev a "False".

### Más allá de "sys.argv"

Sometimes it may be useful to have an "ArgumentParser" parse arguments
other than those of "sys.argv".  This can be accomplished by passing a
list of strings to "parse_args()".  This is useful for testing at the
interactive prompt:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument(
   ...     'integers', metavar='int', type=int, choices=range(10),
   ...     nargs='+', help='an integer in the range 0..9')
   >>> parser.add_argument(
   ...     '--sum', dest='accumulate', action='store_const', const=sum,
   ...     default=max, help='sum the integers (default: find the max)')
   >>> parser.parse_args(['1', '2', '3', '4'])
   Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
   >>> parser.parse_args(['1', '2', '3', '4', '--sum'])
   Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])

### El objeto *Namespace*

class argparse.Namespace

   Clase simple utilizada por defecto por "parse_args()" para crear un
   objeto que contenga atributos y retornarlo.

   Esta clase es deliberadamente simple, sólo una subclase "object"
   con una representación de cadena de texto legible. Si prefieres
   tener una vista en forma de diccionario de los atributos, puedes
   usar el lenguaje estándar de Python, "vars()":

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> args = parser.parse_args(['--foo', 'BAR'])
      >>> vars(args)
      {'foo': 'BAR'}

   También puede ser útil tener un "ArgumentParser" que asigne
   atributos a un objeto ya existente, en lugar de un nuevo objeto
   "Namespace". Esto se puede lograr especificando el argumento de
   palabra clave "namespace=":

      >>> class C:
      ...     pass
      ...
      >>> c = C()
      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
      >>> c.foo
      'BAR'

## Otras utilidades

### Subcommands

ArgumentParser.add_subparsers(*[, title][, description][, prog][, parser_class][, action][, dest][, required][, help][, metavar])

   Many programs split up their functionality into a number of
   subcommands, for example, the "svn" program can invoke subcommands
   like "svn checkout", "svn update", and "svn commit".  Splitting up
   functionality this way can be a particularly good idea when a
   program performs several different functions which require
   different kinds of command-line arguments. "ArgumentParser"
   supports the creation of such subcommands with the
   "add_subparsers()" method.  The "add_subparsers()" method is
   normally called with no arguments and returns a special action
   object.  This object has a single method, "add_parser()", which
   takes a command name and any "ArgumentParser" constructor
   arguments, and returns an "ArgumentParser" object that can be
   modified as usual.

   Descripción de los parámetros:

   * *title* - title for the sub-parser group in help output; by
     default "subcommands" if description is provided, otherwise uses
     title for positional arguments

   * *description* - description for the sub-parser group in help
     output, by default "None"

   * *prog* - usage information that will be displayed with subcommand
     help, by default the name of the program and any positional
     arguments before the subparser argument

   * *parser_class* - class which will be used to create sub-parser
     instances, by default the class of the current parser (e.g.
     "ArgumentParser")

   * action - el tipo básico de acción a tomar cuando este argumento
     se encuentre en la línea de comandos

   * dest - name of the attribute under which subcommand name will be
     stored; by default "None" and no value is stored

   * required - Si se debe proporcionar o no un sub-comando, por
     defecto "False" (añadido en 3.7)

   * help - ayuda para el grupo de análisis secundario en la salida de
     la ayuda, por defecto "None"

   * metavar - string presenting available subcommands in help; by
     default it is "None" and presents subcommands in form {cmd1,
     cmd2, ..}

   Algún ejemplo de uso:

      >>> # create the top-level parser
      >>> parser = argparse.ArgumentParser(prog='PROG')
      >>> parser.add_argument('--foo', action='store_true', help='foo help')
      >>> subparsers = parser.add_subparsers(help='subcommand help')
      >>>
      >>> # create the parser for the "a" command
      >>> parser_a = subparsers.add_parser('a', help='a help')
      >>> parser_a.add_argument('bar', type=int, help='bar help')
      >>>
      >>> # create the parser for the "b" command
      >>> parser_b = subparsers.add_parser('b', help='b help')
      >>> parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')
      >>>
      >>> # parse some argument lists
      >>> parser.parse_args(['a', '12'])
      Namespace(bar=12, foo=False)
      >>> parser.parse_args(['--foo', 'b', '--baz', 'Z'])
      Namespace(baz='Z', foo=True)

   Ten en cuenta que el objeto retornado por "parse_args()" sólo
   contendrá atributos para el analizador principal y el analizador
   secundario que fue seleccionado por la línea de comandos (y no
   cualquier otro analizador secundario). Así que en el ejemplo
   anterior, cuando se especifica el comando "a", sólo están presentes
   los atributos "foo" y "bar", y cuando se especifica el comando "b",
   sólo están presentes los atributos "foo" y "baz".

   If a subparser defines an argument with the same "dest" as the
   parent parser, the two share a single namespace attribute, so the
   parent's value won't be retained. Users should give them  distinct
   "dest" values to keep both.

   Del mismo modo, cuando se solicita un mensaje de ayuda de un
   analizador secundario, sólo se imprimirá la ayuda para ese
   analizador en particular. El mensaje de ayuda no incluirá mensajes
   del analizador principal o de analizadores relacionados. (Sin
   embargo, se puede dar un mensaje de ayuda para cada comando del
   analizador secundario suministrando el argumento "help=" a
   "add_parser()" como se ha indicado anteriormente).

      >>> parser.parse_args(['--help'])
      usage: PROG [-h] [--foo] {a,b} ...

      positional arguments:
        {a,b}   subcommand help
          a     a help
          b     b help

      options:
        -h, --help  show this help message and exit
        --foo   foo help

      >>> parser.parse_args(['a', '--help'])
      usage: PROG a [-h] bar

      positional arguments:
        bar     bar help

      options:
        -h, --help  show this help message and exit

      >>> parser.parse_args(['b', '--help'])
      usage: PROG b [-h] [--baz {X,Y,Z}]

      options:
        -h, --help     show this help message and exit
        --baz {X,Y,Z}  baz help

   El método "add_subparsers()" también soporta los argumentos de
   palabra clave "title" y "description". Cuando cualquiera de los dos
   esté presente, los comandos del analizador secundario aparecerán en
   su propio grupo en la salida de la ayuda. Por ejemplo:

      >>> parser = argparse.ArgumentParser()
      >>> subparsers = parser.add_subparsers(title='subcommands',
      ...                                    description='valid subcommands',
      ...                                    help='additional help')
      >>> subparsers.add_parser('foo')
      >>> subparsers.add_parser('bar')
      >>> parser.parse_args(['-h'])
      usage:  [-h] {foo,bar} ...

      options:
        -h, --help  show this help message and exit

      subcommands:
        valid subcommands

        {foo,bar}   additional help

   Furthermore, "add_parser()" supports an additional *aliases*
   argument, which allows multiple strings to refer to the same
   subparser. This example, like "svn", aliases "co" as a shorthand
   for "checkout":

      >>> parser = argparse.ArgumentParser()
      >>> subparsers = parser.add_subparsers()
      >>> checkout = subparsers.add_parser('checkout', aliases=['co'])
      >>> checkout.add_argument('foo')
      >>> parser.parse_args(['co', 'bar'])
      Namespace(foo='bar')

   "add_parser()" supports also an additional *deprecated* argument,
   which allows to deprecate the subparser.

   >>> import argparse
   >>> parser = argparse.ArgumentParser(prog='chicken.py')
   >>> subparsers = parser.add_subparsers()
   >>> run = subparsers.add_parser('run')
   >>> fly = subparsers.add_parser('fly', deprecated=True)
   >>> parser.parse_args(['fly'])
   chicken.py: warning: command 'fly' is deprecated
   Namespace()

   Added in version 3.13.

   One particularly effective way of handling subcommands is to
   combine the use of the "add_subparsers()" method with calls to
   "set_defaults()" so that each subparser knows which Python function
   it should execute.  For example:

      >>> # subcommand functions
      >>> def foo(args):
      ...     print(args.x * args.y)
      ...
      >>> def bar(args):
      ...     print('((%s))' % args.z)
      ...
      >>> # create the top-level parser
      >>> parser = argparse.ArgumentParser()
      >>> subparsers = parser.add_subparsers(required=True)
      >>>
      >>> # create the parser for the "foo" command
      >>> parser_foo = subparsers.add_parser('foo')
      >>> parser_foo.add_argument('-x', type=int, default=1)
      >>> parser_foo.add_argument('y', type=float)
      >>> parser_foo.set_defaults(func=foo)
      >>>
      >>> # create the parser for the "bar" command
      >>> parser_bar = subparsers.add_parser('bar')
      >>> parser_bar.add_argument('z')
      >>> parser_bar.set_defaults(func=bar)
      >>>
      >>> # parse the args and call whatever function was selected
      >>> args = parser.parse_args('foo 1 -x 2'.split())
      >>> args.func(args)
      2.0
      >>>
      >>> # parse the args and call whatever function was selected
      >>> args = parser.parse_args('bar XYZYX'.split())
      >>> args.func(args)
      ((XYZYX))

   De esta manera, puedes dejar que "parse_args()" haga el trabajo de
   llamar a la función apropiada después de que el análisis de los
   argumentos se haya completado. Asociar funciones con acciones como
   esta es típicamente la forma más fácil de manejar las diferentes
   acciones para cada uno de tus analizadores secundarios. Sin
   embargo, si es necesario comprobar el nombre del analizador
   secundario que se ha invocado, el argumento de palabra clave "dest"
   a la llamada "add_subparsers()" hará el trabajo:

      >>> parser = argparse.ArgumentParser()
      >>> subparsers = parser.add_subparsers(dest='subparser_name')
      >>> subparser1 = subparsers.add_parser('1')
      >>> subparser1.add_argument('-x')
      >>> subparser2 = subparsers.add_parser('2')
      >>> subparser2.add_argument('y')
      >>> parser.parse_args(['2', 'frobble'])
      Namespace(subparser_name='2', y='frobble')

   Distinto en la versión 3.7: New *required* keyword-only parameter.

   Distinto en la versión 3.14: Subparser's *prog* is no longer
   affected by a custom usage message in the main parser.

### Objetos *FileType*

class argparse.FileType(mode='r', bufsize=-1, encoding=None, errors=None)

   El generador "FileType" crea objetos que pueden ser transferidos al
   argumento tipo de "ArgumentParser.add_argument()". Los argumentos
   que tienen objetos "FileType" como su tipo abrirán los argumentos
   de líneas de comandos como archivos con los modos, tamaños de
   búfer, codificaciones y manejo de errores solicitados (véase la
   función "open()" para más detalles):

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--raw', type=argparse.FileType('wb', 0))
      >>> parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
      >>> parser.parse_args(['--raw', 'raw.dat', 'file.txt'])
      Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<_io.FileIO name='raw.dat' mode='wb'>)

   Los objetos *FileType* entienden el pseudo-argumento "'-'" y lo
   convierten automáticamente en "sys.stdin" para objetos de lectura
   "FileType" y "sys.stdout" para objetos de escritura "FileType":

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('infile', type=argparse.FileType('r'))
      >>> parser.parse_args(['-'])
      Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)

   Nota:

     If one argument uses *FileType* and then a subsequent argument
     fails, an error is reported but the file is not automatically
     closed. This can also clobber the output files. In this case, it
     would be better to wait until after the parser has run and then
     use the "with"-statement to manage the files.

   Distinto en la versión 3.4: Added the *encoding* and *errors*
   parameters.

   Obsoleto desde la versión 3.14.

### Grupos de argumentos

ArgumentParser.add_argument_group(title=None, description=None, *[, argument_default][, conflict_handler])

   By default, "ArgumentParser" groups command-line arguments into
   "positional arguments" and "options" when displaying help messages.
   When there is a better conceptual grouping of arguments than this
   default one, appropriate groups can be created using the
   "add_argument_group()" method:

      >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
      >>> group = parser.add_argument_group('group')
      >>> group.add_argument('--foo', help='foo help')
      >>> group.add_argument('bar', help='bar help')
      >>> parser.print_help()
      usage: PROG [--foo FOO] bar

      group:
        bar    bar help
        --foo FOO  foo help

   The "add_argument_group()" method returns an argument group object
   which has an "add_argument()" method just like a regular
   "ArgumentParser".  When an argument is added to the group, the
   parser treats it just like a normal argument, but displays the
   argument in a separate group for help messages.  The
   "add_argument_group()" method accepts *title* and *description*
   arguments which can be used to customize this display:

      >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
      >>> group1 = parser.add_argument_group('group1', 'group1 description')
      >>> group1.add_argument('foo', help='foo help')
      >>> group2 = parser.add_argument_group('group2', 'group2 description')
      >>> group2.add_argument('--bar', help='bar help')
      >>> parser.print_help()
      usage: PROG [--bar BAR] foo

      group1:
        group1 description

        foo    foo help

      group2:
        group2 description

        --bar BAR  bar help

   The optional, keyword-only parameters argument_default and
   conflict_handler allow for finer-grained control of the behavior of
   the argument group. These parameters have the same meaning as in
   the "ArgumentParser" constructor, but apply specifically to the
   argument group rather than the entire parser.

   Ten en cuenta que cualquier argumento que no esté en los grupos
   definidos por el usuario terminará en las secciones habituales de
   "argumentos de posición" y "argumentos opcionales".

   Within each argument group, arguments are displayed in help output
   in the order in which they are added.

   Deprecated since version 3.11, removed in version 3.14: Calling
   "add_argument_group()" on an argument group now raises an
   exception. This nesting was never supported, often failed to work
   correctly, and was unintentionally exposed through inheritance.

   Obsoleto desde la versión 3.14: Passing prefix_chars to
   "add_argument_group()" is now deprecated.

### Exclusión mutua

ArgumentParser.add_mutually_exclusive_group(required=False)

   Create a mutually exclusive group. "argparse" will make sure that
   only one of the arguments in the mutually exclusive group was
   present on the command line:

      >>> parser = argparse.ArgumentParser(prog='PROG')
      >>> group = parser.add_mutually_exclusive_group()
      >>> group.add_argument('--foo', action='store_true')
      >>> group.add_argument('--bar', action='store_false')
      >>> parser.parse_args(['--foo'])
      Namespace(bar=True, foo=True)
      >>> parser.parse_args(['--bar'])
      Namespace(bar=False, foo=False)
      >>> parser.parse_args(['--foo', '--bar'])
      usage: PROG [-h] [--foo | --bar]
      PROG: error: argument --bar: not allowed with argument --foo

   El método "add_mutually_exclusive_group()" también acepta un
   argumento *required*, para indicar que se requiere al menos uno de
   los argumentos mutuamente exclusivos:

      >>> parser = argparse.ArgumentParser(prog='PROG')
      >>> group = parser.add_mutually_exclusive_group(required=True)
      >>> group.add_argument('--foo', action='store_true')
      >>> group.add_argument('--bar', action='store_false')
      >>> parser.parse_args([])
      usage: PROG [-h] (--foo | --bar)
      PROG: error: one of the arguments --foo --bar is required

   Tomar en cuenta que actualmente los grupos de argumentos mutuamente
   exclusivos no admiten los argumentos *title* y *description* de
   "add_argument_group()". Sin embargo, se puede agregar un grupo
   mutuamente exclusivo a un grupo de argumentos que tenga un título y
   una descripción. Por ejemplo:

      >>> parser = argparse.ArgumentParser(prog='PROG')
      >>> group = parser.add_argument_group('Group title', 'Group description')
      >>> exclusive_group = group.add_mutually_exclusive_group(required=True)
      >>> exclusive_group.add_argument('--foo', help='foo help')
      >>> exclusive_group.add_argument('--bar', help='bar help')
      >>> parser.print_help()
      usage: PROG [-h] (--foo FOO | --bar BAR)

      options:
        -h, --help  show this help message and exit

      Group title:
        Group description

        --foo FOO   foo help
        --bar BAR   bar help

   Deprecated since version 3.11, removed in version 3.14: Calling
   "add_argument_group()" or "add_mutually_exclusive_group()" on a
   mutually exclusive group now raises an exception. This nesting was
   never supported, often failed to work correctly, and was
   unintentionally exposed through inheritance.

### Valores por defecto del analizador

ArgumentParser.set_defaults(**kwargs)

   La mayoría de las veces, los atributos del objeto retornado por
   "parse_args()" se determinarán completamente inspeccionando los
   argumentos de la línea de comandos y las acciones de los
   argumentos. "set_defaults()" permite que se añadan algunos
   atributos adicionales que se determinan sin ninguna inspección de
   la línea de comandos:

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('foo', type=int)
      >>> parser.set_defaults(bar=42, baz='badger')
      >>> parser.parse_args(['736'])
      Namespace(bar=42, baz='badger', foo=736)

   Note that defaults can be set at both the parser level using
   "set_defaults()" and at the argument level using "add_argument()".
   If both are called for the same argument, the last default set for
   an argument is used:

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', default='bar')
      >>> parser.set_defaults(foo='spam')
      >>> parser.parse_args([])
      Namespace(foo='spam')

   Los valores por defecto a nivel analizador pueden ser muy útiles
   cuando se trabaja con varios analizadores. Consulta el método
   "add_subparsers()" para ver un ejemplo de este tipo.

ArgumentParser.get_default(dest)

   Obtiene el valor por defecto para un atributo del espacio de
   nombres (*namespace*), establecido ya sea por "add_argument()" o
   por "set_defaults()":

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', default='badger')
      >>> parser.get_default('foo')
      'badger'

### Mostrando la ayuda

En la mayoría de las aplicaciones típicas, "parse_args()" se encargará
de dar formato y mostrar cualquier mensaje de uso o de error. Sin
embargo, hay varios métodos para dar formato disponibles:

ArgumentParser.print_usage(file=None)

   Muestra una breve descripción de cómo se debe invocar el
   "ArgumentParser" en la línea de comandos. Si *file* es "None", se
   asume "sys.stdout".

ArgumentParser.print_help(file=None)

   Muestra un mensaje de ayuda, incluyendo el uso del programa e
   información sobre los argumentos registrados en el
   "ArgumentParser". Si *file* es "None", se asume "sys.stdout".

También hay variantes de estos métodos que simplemente retornan una
cadena de caracteres en lugar de mostrarla:

ArgumentParser.format_usage()

   Retorna una cadena de caracteres que contiene una breve descripción
   de cómo se debe invocar el "ArgumentParser" en la línea de
   comandos.

ArgumentParser.format_help()

   Retorna una cadena de caracteres que contiene un mensaje de ayuda,
   incluyendo el uso del programa e información sobre los argumentos
   registrados en el "ArgumentParser".

### Análisis parcial

ArgumentParser.parse_known_args(args=None, namespace=None)

   Sometimes a script only needs to handle a specific set of command-
   line arguments, leaving any unrecognized arguments for another
   script or program. In these cases, the "parse_known_args()" method
   can be useful.

   This method works similarly to "parse_args()", but it does not
   raise an error for extra, unrecognized arguments. Instead, it
   parses the known arguments and returns a two item tuple that
   contains the populated namespace and the list of any unrecognized
   arguments.

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', action='store_true')
      >>> parser.add_argument('bar')
      >>> parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
      (Namespace(bar='BAR', foo=True), ['--badger', 'spam'])

Advertencia:

  Coincidencia de prefijos las reglas se aplican a
  "parse_known_args()". El analizador puede consumir una opción aunque
  sea sólo un prefijo de una de sus opciones conocidas, en lugar de
  dejarla en la lista de argumentos restantes.

### Personalizando el análisis de archivos

ArgumentParser.convert_arg_line_to_args(arg_line)

   Los argumentos que se leen de un archivo (mira el argumento de
   palabra clave *fromfile_prefix_chars* para el constructor
   "ArgumentParser") se leen uno por línea.
   "convert_arg_line_to_args()" puede ser invalidado para una lectura
   más elegante.

   Este método utiliza un sólo argumento *arg_line* que es una cadena
   de caracteres leída desde el archivo de argumentos. Retorna una
   lista de argumentos analizados a partir de esta cadena de
   caracteres. El método se llama una vez por línea leída del fichero
   de argumentos, en orden.

   Una alternativa útil de este método es la que trata cada palabra
   separada por un espacio como un argumento. El siguiente ejemplo
   demuestra cómo hacerlo:

      class MyArgumentParser(argparse.ArgumentParser):
          def convert_arg_line_to_args(self, arg_line):
              return arg_line.split()

   Note that with this override an argument can no longer contain
   spaces, since each space-separated word becomes a separate
   argument.

### Métodos de salida

ArgumentParser.exit(status=0, message=None)

   This method terminates the program, exiting with the specified
   *status* and, if given, it prints a *message* to "sys.stderr"
   before that. The user can override this method to handle these
   steps differently:

      class ErrorCatchingArgumentParser(argparse.ArgumentParser):
          def exit(self, status=0, message=None):
              if status:
                  raise Exception(f'Exiting because of an error: {message}')
              exit(status)

ArgumentParser.error(message)

   This method prints a usage message, including the *message*, to
   "sys.stderr" and terminates the program with a status code of 2.

### Análisis entremezclado

ArgumentParser.parse_intermixed_args(args=None, namespace=None)

ArgumentParser.parse_known_intermixed_args(args=None, namespace=None)

   Una serie de comandos *Unix* permiten al usuario mezclar argumentos
   opcionales con argumentos de posición. Los métodos
   "parse_intermixed_args()" y "parse_known_intermixed_args()"
   soportan este modo de análisis.

   These parsers do not support all the "argparse" features, and will
   raise exceptions if unsupported features are used.  In particular,
   subparsers, and mutually exclusive groups that include both
   optionals and positionals are not supported.

   El siguiente ejemplo muestra la diferencia entre
   "parse_known_args()" y "parse_intermixed_args()": el primero
   retorna "['2', '3']" como argumentos sin procesar, mientras que el
   segundo recoge todos los de posición en "rest".

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> parser.add_argument('cmd')
      >>> parser.add_argument('rest', nargs='*', type=int)
      >>> parser.parse_known_args('doit 1 --foo bar 2 3'.split())
      (Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
      >>> parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
      Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])

   "parse_known_intermixed_args()" retorna una tupla de dos elementos
   que contiene el espacio de nombres poblado y la lista de los
   restantes argumentos de cadenas de caracteres.
   "parse_intermixed_args()" arroja un error si quedan argumentos de
   cadenas de caracteres sin procesar.

   Added in version 3.7.

### Registering custom types or actions

ArgumentParser.register(registry_name, value, object)

   Sometimes it's desirable to use a custom string in error messages
   to provide more user-friendly output. In these cases, "register()"
   can be used to register custom actions or types with a parser and
   allow you to reference the type by their registered name instead of
   their callable name.

   The "register()" method accepts three arguments - a
   *registry_name*, specifying the internal registry where the object
   will be stored (e.g., "action", "type"), *value*, which is the key
   under which the object will be registered, and object, the callable
   to be registered.

   The following example shows how to register a custom type with a
   parser:

      >>> import argparse
      >>> parser = argparse.ArgumentParser()
      >>> parser.register('type', 'hexadecimal integer', lambda s: int(s, 16))
      >>> parser.add_argument('--foo', type='hexadecimal integer')
      _StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type='hexadecimal integer', choices=None, required=False, help=None, metavar=None, deprecated=False)
      >>> parser.parse_args(['--foo', '0xFA'])
      Namespace(foo=250)
      >>> parser.parse_args(['--foo', '1.2'])
      usage: PROG [-h] [--foo FOO]
      PROG: error: argument --foo: invalid 'hexadecimal integer' value: '1.2'

## Excepciones

exception argparse.ArgumentError

   Un error al crear o usar un argumento (opcional o posicional).

   El valor de la cadena de caracteres de esta excepción es el
   mensaje, ampliado con información sobre el argumento que lo causó.

exception argparse.ArgumentTypeError

   Se lanza cuando algo sale mal al convertir una cadena de caracteres
   de la línea de comandos a un tipo.

-[ Guides and Tutorials ]-

* Tutorial de *argparse*

* Migrating "optparse" code to "argparse"
