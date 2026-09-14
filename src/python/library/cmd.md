---
title: '"cmd" --- Support for line-oriented command interpreters'
source_url: https://docs.python.org/es/3
source_path: library/cmd.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1940
---

# "cmd" --- Support for line-oriented command interpreters

**Código fuente:** Lib/cmd.py

======================================================================

La clase "Cmd" proporciona un *framework* simple para escribir
intérpretes de comandos orientados a línea. A menudo son útiles para
agentes de prueba, herramientas administrativas y prototipos que luego
se incluirán en una interfaz más sofisticada.

class cmd.Cmd(completekey='tab', stdin=None, stdout=None)

   Una instancia "Cmd" o subclase de la instancia es un *framework*
   intérprete orientado a líneas. No hay una buena razón para crear
   instancias "Cmd"; mas bien, es útil como una super clase de una
   clase intérprete que usted define con el fin de heredar métodos
   "Cmd" y encapsular métodos de acción.

   El argumento opcional *completekey* es el nombre "readline" de una
   llave de finalización; por defecto es "Tab". Si *completekey* no es
   "None" y "readline" está disponible, el comando de finalización es
   hecho automáticamente.

   The default, "'tab'", is treated specially, so that it refers to
   the "Tab" key on every "readline.backend". Specifically, if
   "readline.backend" is "editline", "Cmd" will use "'^I'" instead of
   "'tab'". Note that other values are not treated this way, and might
   only work with a specific backend.

   Los argumentos opcionales *stdin* y *stdout* especifican la entrada
   y salida de los objetos archivo que la instancia Cmd o la instancia
   subclase usará para la entrada y salida. Si no está especificado,
   se predeterminarán a "sys.stdin" y "sys.stdout".

   Si desea un *stdin* dado a ser usado, asegúrese de establecer las
   instancias atributo "use_rawinput" a "False", de lo contrario
   *stdin* será ignorado.

   Distinto en la versión 3.13: "completekey='tab'" is replaced by
   "'^I'" for "editline".

## Objetos Cmd

Una instancia "Cmd" tiene los siguientes métodos:

Cmd.cmdloop(intro=None)

   Emita repetidamente una solicitud, acepte la entrada, analice un
   prefijo inicial de la entrada recibida y envíe a los métodos de
   acción, pasándoles el resto de la línea como argumento.

   El argumento opcional es un *banner* o cadena de caracteres
   introductoria que se tramitará antes del primer mensaje (esto anula
   el atributo de clase "intro").

   Si el módulo "readline" es cargado, la entrada heredará
   automáticamente **bash**-como edición historia-lista (e.g.
   "Control"-"P" retorna al último comando, "Control"-"N" adelanta al
   siguiente, "Control"-"F" mueve el cursor a la derecha no
   destructivamente, "Control"-"B" mueve el cursor a la izquierda no
   destructivamente, etc.).

   Un fin-de-archivo en la entrada es retornado como cadena de
   caracteres "’EOF’".

   An interpreter instance will recognize a command name "foo" if and
   only if it has a method "do_foo()".  As a special case, a line
   beginning with the character "'?'" is dispatched to the method
   "do_help()".  As another special case, a line beginning with the
   character "'!'" is dispatched to the method "do_shell()" (if such a
   method is defined).

   This method will return when the "postcmd()" method returns a true
   value. The *stop* argument to "postcmd()" is the return value from
   the command's corresponding "do_*()" method.

   If completion is enabled, completing commands will be done
   automatically, and completing of commands args is done by calling
   "complete_foo()" with arguments *text*, *line*, *begidx*, and
   *endidx*.  *text* is the string prefix we are attempting to match:
   all returned matches must begin with it. *line* is the current
   input line with leading whitespace removed, *begidx* and *endidx*
   are the beginning and ending indexes of the prefix text, which
   could be used to provide different completion depending upon which
   position the argument is in.

Cmd.do_help(arg)

   All subclasses of "Cmd" inherit a predefined "do_help()".  This
   method, called with an argument "'bar'", invokes the corresponding
   method "help_bar()", and if that is not present, prints the
   docstring of "do_bar()", if available.  With no argument,
   "do_help()" lists all available help topics (that is, all commands
   with corresponding "help_*()" methods or commands that have
   docstrings), and also lists any undocumented commands.

Cmd.onecmd(str)

   Interpret the argument as though it had been typed in response to
   the prompt. This may be overridden, but should not normally need to
   be; see the "precmd()" and "postcmd()" methods for useful execution
   hooks.  The return value is a flag indicating whether
   interpretation of commands by the interpreter should stop.  If
   there is a "do_*()" method for the command *str*, the return value
   of that method is returned, otherwise the return value from the
   "default()" method is returned.

Cmd.emptyline()

   Método llamado cuando se ingresa una línea vacía en respuesta a la
   solicitud. Si este método no se anula, repite el último comando no
   vacío ingresado.

Cmd.default(line)

   Método llamado en una línea de entrada cuando no se reconoce el
   prefijo del comando. Si este método no se anula, imprime un mensaje
   de error y retorna.

Cmd.completedefault(text, line, begidx, endidx)

   Method called to complete an input line when no command-specific
   "complete_*()" method is available.  By default, it returns an
   empty list.

Cmd.columnize(list, displaywidth=80)

   Método llamado para mostrar una lista de cadenas de caracteres como
   un set compacto de columnas. Cada columna es tan amplia como sea
   necesaria. Las columnas se separan por dos espacios para facilidad
   de lectura.

Cmd.precmd(line)

   Método de enlace ejecutado justo antes de que se interprete la
   línea de comando *line*, pero después de que se genere y emita la
   solicitud de entrada. Este método es un trozo en "Cmd"; existe para
   ser anulado por subclases. El valor de retorno es utilizado como el
   comando que se ejecutará mediante el método "onecmd()"; la
   implementación "precmd()" puede reescribir el comando o simplemente
   retornar *line* sin cambios.

Cmd.postcmd(stop, line)

   Método de enlace ejecutado justo después de que finaliza un
   despacho de comando. Este método es un trozo en "Cmd"; existe para
   ser anulado por subclases. *line* es la línea de comando que se
   ejecutó, y *stop* es una bandera que indica si la ejecución
   finalizará después de la llamada a "postcmd()"; este será el valor
   de retorno del método "onecmd()". El valor de retorno de este
   método será usado como el nuevo valor para la bandera interna que
   corresponde a *stop*; retornando falso hará que la interpretación
   continúe.

Cmd.preloop()

   Método de enlace ejecutado una vez cuando "cmdloop()" es llamado.
   Este método es un trozo en "Cmd"; existe para ser anulado por
   subclases.

Cmd.postloop()

   Método de enlace ejecutado una vez cuando "cmdloop()" está a punto
   de retornar. Este método es un trozo en "Cmd"; existe para ser
   anulado por subclases.

Instancias de subclases "Cmd" tienen algunas variables de instancia
públicas:

Cmd.prompt

   El aviso emitido para solicitar entradas.

Cmd.identchars

   La cadena de caracteres aceptada para el prefijo del comando.

Cmd.lastcmd

   El último prefijo de comando no vacío visto.

Cmd.cmdqueue

   Una lista de líneas de entrada puestas en cola. La lista *cmdqueue*
   es verificada en "cmdloop()" cuando una nueva entrada es
   necesitada; Si es no vacía, sus elementos serán procesados en
   orden, como si se ingresara en la solicitud.

Cmd.intro

   Una cadena para emitir como introducción o *banner*. Puede ser
   anulado dando un argumento al método "cmdloop()".

Cmd.doc_header

   El encabezado a tramitar si la salida de ayuda tiene una sección
   para comandos documentados.

Cmd.misc_header

   The header to issue if the help output has a section for
   miscellaneous  help topics (that is, there are "help_*()" methods
   without corresponding "do_*()" methods).

Cmd.undoc_header

   The header to issue if the help output has a section for
   undocumented  commands (that is, there are "do_*()" methods without
   corresponding "help_*()" methods).

Cmd.ruler

   El carácter utilizado para dibujar líneas separadoras debajo de los
   encabezados mensajes-ayuda. Si está vacío, no se dibuja una línea
   regla. El valor predeterminado es "’=‘".

Cmd.use_rawinput

   A flag, defaulting to true.  If true, "cmdloop()" uses "input()" to
   display a prompt and read the next command; if false,
   "sys.stdout.write()" and "sys.stdin.readline()" are used. (This
   means that by importing "readline", on systems that support it, the
   interpreter will automatically support **Emacs**-like line editing
   and command-history keystrokes.)

## Ejemplo Cmd

The "cmd" module is mainly useful for building custom shells that let
a user work with a program interactively.

Esta sección presenta un ejemplo simple de cómo construir un *shell*
alrededor de algunos de los comandos en el módulo "turtle".

Basic turtle commands such as "forward()" are added to a "Cmd"
subclass with method named "do_forward()".  The argument is converted
to a number and dispatched to the turtle module.  The docstring is
used in the help utility provided by the shell.

The example also includes a basic record and playback facility
implemented with the "precmd()" method which is responsible for
converting the input to lowercase and writing the commands to a file.
The "do_playback()" method reads the file and adds the recorded
commands to the "cmdqueue" for immediate playback:

   import cmd, sys
   from turtle import *

   class TurtleShell(cmd.Cmd):
       intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
       prompt = '(turtle) '
       file = None

       # ----- basic turtle commands -----
       def do_forward(self, arg):
           'Move the turtle forward by the specified distance:  FORWARD 10'
           forward(*parse(arg))
       def do_right(self, arg):
           'Turn turtle right by given number of degrees:  RIGHT 20'
           right(*parse(arg))
       def do_left(self, arg):
           'Turn turtle left by given number of degrees:  LEFT 90'
           left(*parse(arg))
       def do_goto(self, arg):
           'Move turtle to an absolute position with changing orientation.  GOTO 100 200'
           goto(*parse(arg))
       def do_home(self, arg):
           'Return turtle to the home position:  HOME'
           home()
       def do_circle(self, arg):
           'Draw circle with given radius an options extent and steps:  CIRCLE 50'
           circle(*parse(arg))
       def do_position(self, arg):
           'Print the current turtle position:  POSITION'
           print('Current position is %d %d\n' % position())
       def do_heading(self, arg):
           'Print the current turtle heading in degrees:  HEADING'
           print('Current heading is %d\n' % (heading(),))
       def do_color(self, arg):
           'Set the color:  COLOR BLUE'
           color(arg.lower())
       def do_undo(self, arg):
           'Undo (repeatedly) the last turtle action(s):  UNDO'
       def do_reset(self, arg):
           'Clear the screen and return turtle to center:  RESET'
           reset()
       def do_bye(self, arg):
           'Stop recording, close the turtle window, and exit:  BYE'
           print('Thank you for using Turtle')
           self.close()
           bye()
           return True

       # ----- record and playback -----
       def do_record(self, arg):
           'Save future commands to filename:  RECORD rose.cmd'
           self.file = open(arg, 'w')
       def do_playback(self, arg):
           'Playback commands from a file:  PLAYBACK rose.cmd'
           self.close()
           with open(arg) as f:
               self.cmdqueue.extend(f.read().splitlines())
       def precmd(self, line):
           line = line.lower()
           if self.file and 'playback' not in line:
               print(line, file=self.file)
           return line
       def close(self):
           if self.file:
               self.file.close()
               self.file = None

   def parse(arg):
       'Convert a series of zero or more numbers to an argument tuple'
       return tuple(map(int, arg.split()))

   if __name__ == '__main__':
       TurtleShell().cmdloop()

Aquí hay una sesión de muestra con la *turle shell* mostrando las
funciones de ayuda, de ayuda, usando líneas en blanco para repetir
comandos, un registro simple y facilidad de reproducción:

   Welcome to the turtle shell.   Type help or ? to list commands.

   (turtle) ?

   Documented commands (type help <topic>):
   ========================================
   bye     color    goto     home  playback  record  right
   circle  forward  heading  left  position  reset   undo

   (turtle) help forward
   Move the turtle forward by the specified distance:  FORWARD 10
   (turtle) record spiral.cmd
   (turtle) position
   Current position is 0 0

   (turtle) heading
   Current heading is 0

   (turtle) reset
   (turtle) circle 20
   (turtle) right 30
   (turtle) circle 40
   (turtle) right 30
   (turtle) circle 60
   (turtle) right 30
   (turtle) circle 80
   (turtle) right 30
   (turtle) circle 100
   (turtle) right 30
   (turtle) circle 120
   (turtle) right 30
   (turtle) circle 120
   (turtle) heading
   Current heading is 180

   (turtle) forward 100
   (turtle)
   (turtle) right 90
   (turtle) forward 100
   (turtle)
   (turtle) right 90
   (turtle) forward 400
   (turtle) right 90
   (turtle) forward 500
   (turtle) right 90
   (turtle) forward 400
   (turtle) right 90
   (turtle) forward 300
   (turtle) playback spiral.cmd
   Current position is 0 0

   Current heading is 0

   Current heading is 180

   (turtle) bye
   Thank you for using Turtle
