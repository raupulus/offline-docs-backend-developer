---
title: '"termios" --- POSIX style tty control'
source_url: https://docs.python.org/es/3
source_path: library/termios.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4090
---

# "termios" --- POSIX style tty control

======================================================================

Este módulo proporciona una interfaz para las llamadas POSIX para el
control de E/S (entrada/salida) tty. Para obtener una descripción
completa de estas llamadas, consulte *termios (3)* Página de manual de
Unix. Solo está disponible para aquellas versiones de Unix que admitan
el control de E/S tty estilo POSIX *termios* configurado durante la
instalación.

Availability: Unix.

Todas las funciones de este módulo toman un descriptor de archivo *fd*
como primer argumento. Puede ser un descriptor de archivo entero, como
el que retorna "sys.stdin.fileno()", o un *file object*, como el
propio "sys.stdin".

Este módulo también define todas las constantes necesarias para
trabajar con las funciones proporcionadas aquí; tienen el mismo nombre
que sus contrapartes en C. Consulte la documentación de su sistema
para obtener más información sobre el uso de estas interfaces de
control de terminal.

El módulo define las siguientes funciones:

termios.tcgetattr(fd)

   Return a list containing the tty attributes for file descriptor
   *fd*, as follows: "[iflag, oflag, cflag, lflag, ispeed, ospeed,
   cc]" where *cc* is a list of the tty special characters (each a
   string of length 1, except the items with indices "VMIN" and
   "VTIME", which are integers when these fields are defined).  The
   interpretation of the flags and the speeds as well as the indexing
   in the *cc* array must be done using the symbolic constants defined
   in the "termios" module.

termios.tcsetattr(fd, when, attributes)

   Set the tty attributes for file descriptor *fd* from the
   *attributes*, which is a list like the one returned by
   "tcgetattr()".  The *when* argument determines when the attributes
   are changed:

   termios.TCSANOW

      Change attributes immediately.

   termios.TCSADRAIN

      Change attributes after transmitting all queued output.

   termios.TCSAFLUSH

      Change attributes after transmitting all queued output and
      discarding all queued input.

termios.tcsendbreak(fd, duration)

   Envíe una pausa en el descriptor de archivo *fd*. Una *duración*
   cero envía una pausa de 0.25 a 0.5 segundos;  una *duración*
   distinta de cero tiene un significado dependiente del sistema.

termios.tcdrain(fd)

   Espere hasta que se haya transmitido toda la salida escrita en el
   descriptor de archivo *fd*.

termios.tcflush(fd, queue)

   Descartar datos en cola en el descriptor de archivo *fd*. El
   selector *queue* especifica qué cola: "TCIFLUSH" para la cola de
   entrada, "TCOFLUSH" para la cola de salida, o "TCIOFLUSH" para
   ambas colas.

termios.tcflow(fd, action)

   Suspender o reanudar la entrada o salida en el descriptor de
   archivo *fd*. El argumento *action* puede ser  "TCOOFF" para
   suspender la salida, "TCOON" para reiniciar la salida, "TCIOFF"
   para suspender la entrada, o "TCION" para reiniciar la entrada.

termios.tcgetwinsize(fd)

   Devuelve una tupla "(ws_row, ws_col)" que contiene el tamaño de la
   ventana tty para el descriptor de archivo *fd*. Requiere
   "termios.TIOCGWINSZ" o "termios.TIOCGSIZE".

   Added in version 3.11.

termios.tcsetwinsize(fd, winsize)

   Establezca el tamaño de la ventana tty para el descriptor de
   archivo *fd* de *winsize*, que es un tupla de dos elementos
   "(ws_row, ws_col)" como la devuelta por "tcgetwinsize()". Requiere
   que al menos uno de los pares ("termios.TIOCGWINSZ",
   "termios.TIOCSWINSZ"); ("termios.TIOCGSIZE", "termios.TIOCSSIZE")
   por definir.

   Added in version 3.11.

Ver también:

  Módulo "tty"
     Funciones de conveniencia para operaciones comunes de control de
     terminal.

## Ejemplo

Aquí hay una función que solicita una contraseña con el eco
desactivado. Tenga en cuenta la técnica utilizando una llamada
separada  "tcgetattr()" y una sentencia "try" ... "finally"  para
asegurarse de que los antiguos atributos tty se restauran exactamente
sin importar lo que suceda:

   def getpass(prompt="Password: "):
       import termios, sys
       fd = sys.stdin.fileno()
       old = termios.tcgetattr(fd)
       new = termios.tcgetattr(fd)
       new[3] = new[3] & ~termios.ECHO          # lflags
       try:
           termios.tcsetattr(fd, termios.TCSADRAIN, new)
           passwd = input(prompt)
       finally:
           termios.tcsetattr(fd, termios.TCSADRAIN, old)
       return passwd
