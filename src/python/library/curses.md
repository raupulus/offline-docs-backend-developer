---
title: '"curses" --- Terminal handling for character-cell displays'
source_url: https://docs.python.org/es/3
source_path: library/curses.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2220
---

# "curses" --- Terminal handling for character-cell displays

**Source code:** Lib/curses

======================================================================

The "curses" module provides an interface to the curses library, the
de-facto standard for portable advanced terminal handling.

Mientras que curses es más ampliamente usado en los ambientes Unix,
las versiones están disponibles para Windows, DOS, y posiblemente para
otros sistemas también. Esta extensión del módulo es diseñada para
coincidir con el API de ncurses, una librería de código abierto
almacenada en Linux y las variantes BSD de Unix.

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

Availability: Unix.

Nota:

  Cuando la documentación menciona un *carácter*, esto puede ser
  especificado como un entero, una cadena Unicode de un carácter o una
  cadena de bytes de un byte.Cuando la documentación menciona una
  *cadena de caracteres*, esto puede ser especificado como una cadena
  Unicode o una cadena de bytes.

Ver también:

  Módulo "curses.ascii"
     Utilidades para trabajar con caracteres ASCII, independientemente
     de tu configuración local.

  Módulo "curses.panel"
     Una extensión de la pila de paneles que añade profundidad a las
     ventanas de curses.

  Módulo "curses.textpad"
     Widget de texto editable para apoyar curses  **Emacs**- como
     enlaces.

  Programación de curses con Python
     Material del tutorial usando curses con Python, por *Andrew
     Kuchling* y *Eric Raymond*.

## Funciones

The module "curses" defines the following exception:

exception curses.error

   Una excepción se lanza cuando una función de la librería curses
   retorna un error.

Nota:

  Cuando los argumentos *x* o *y* para una función o un método son
  opcionales, se predetermina la ubicación actual del cursor.  Cuando
  *attr* es opcional, por defecto es "A_NORMAL".

The module "curses" defines the following functions:

curses.assume_default_colors(fg, bg, /)

   Allow use of default values for colors on terminals supporting this
   feature. Use this to support transparency in your application.

   * Assign terminal default foreground/background colors to color
     number "-1". So "init_pair(x, COLOR_RED, -1)" will initialize
     pair *x* as red on default background and "init_pair(x, -1,
     COLOR_BLUE)" will initialize pair *x* as default foreground on
     blue.

   * Change the definition of the color-pair "0" to "(fg, bg)".

   This is an ncurses extension.

   Added in version 3.14.

curses.baudrate()

   Retorna la velocidad de salida de la terminal en bits por segundo.
   En emuladores de terminal de software esto tendrá un alto valor
   fijado. Incluido por razones históricas; en tiempos pasados, esto
   fue usado para escribir los ciclos de salida por retrasos de tiempo
   y ocasionalmente para cambiar interfaces dependiendo de la
   velocidad en la línea.

curses.beep()

   Emite un corto sonido de atención.

curses.can_change_color()

   Retorna "True" o "False", dependiendo ya sea que el programador
   puede cambiar los colores presentados por la terminal.

curses.cbreak()

   Entra al modo *cbreak*.  En el modo *cbreak* (a veces llamado modo
   "raro") del buffer de línea *tty* normal es apagado y los
   caracteres están disponibles para ser leídos uno por uno.  Sin
   embargo, a diferencia del modo raw, los caracteres especiales
   (interrumpir, salir, suspender y control de flujo) retiene sus
   efectos en el manejador *tty* y el programa de llamada.  Llamando
   primero "raw()" luego "cbreak()" dejando la terminal en modo
   *cbreak*.

curses.color_content(color_number)

   Return the intensity of the red, green, and blue (RGB) components
   in the color *color_number*, which must be between "0" and "COLORS
   - 1".  Return a 3-tuple, containing the R,G,B values for the given
   color, which will be between "0" (no component) and "1000" (maximum
   amount of component).  Raise an exception if the color is not
   supported.

curses.color_pair(pair_number)

   Return the attribute value for displaying text in the specified
   color pair. Only the first 256 color pairs are supported. This
   attribute value can be combined with "A_STANDOUT", "A_REVERSE", and
   the other "A_*" attributes.  "pair_number()" is the counterpart to
   this function.

curses.curs_set(visibility)

   Configura el estado del cursor. *visibilidad* puede estar
   configurado para "0", "1" o "2", para invisible, normal o muy
   visible.  Si la terminal soporta la visibilidad requerida, retorna
   el estado del cursor previo; de otra manera ejecuta una excepción.
   En muchos terminales, el modo "visible" es un cursor subrayado y el
   modo "muy visible" es un cursor de bloque.

curses.def_prog_mode()

   Guardar el modo del terminal actual como el modo "program", el modo
   cuando el programa corriendo está usando curses. (Su contraparte es
   el modo "shell", para cuando el programa no está en curses.)
   Seguido de la llamada a "reset_prog_mode()" restaurará este modo.

curses.def_shell_mode()

   Guarde el modo de terminal actual como el modo "shell", el modo en
   el que el programa en ejecución no utiliza curses. (Su contraparte
   es el modo "program", cuando el programa está usando las
   capacidades de curses.)  Las llamadas subsecuentes a
   "reset_shell_mode()" restaurarán este modo.

curses.delay_output(ms)

   Inserte una pausa en milisegundo *ms* en la salida.

curses.doupdate()

   Update the physical screen.  The curses library keeps two data
   structures, one representing the current physical screen contents
   and a virtual screen representing the desired next state.  The
   "doupdate()" function updates the physical screen to match the
   virtual screen.

   La pantalla virtual puede ser actualizada por una llamada
   "noutrefresh()" después de escribir las operaciones tales como
   "addstr()" ha sido ejecutada en una ventana. La llamada normal
   "refresh()" es simplemente "noutrefresh()" seguido por
   "doupdate()"; si tienes para actualizar múltiples ventanas, puedes
   aumentar el rendimiento y quizás reducir los parpadeos de la
   pantalla usando la llamada "noutrefresh()" en todas las ventanas,
   seguido por un simple "doupdate()".

curses.echo()

   Entrar en modo echo.  En modo echo, cada caracter de entrada es
   repercutido a la pantalla como este es introducido.

curses.endwin()

   Desinicializa la librería y retorne el terminal al estado normal.

curses.erasechar()

   Retorne el carácter borrado del usuario actual como un objeto de
   bytes de un byte. Bajo el sistema de operaciones Unix esta es una
   propiedad de el controlador tty de el programa curses, y no es
   configurado por la librería curses en sí misma.

curses.filter()

   The "filter()" routine, if used, must be called before "initscr()"
   is called.  The effect is that, during the initialization, "LINES"
   is set to "1"; the capabilities "clear", "cup", "cud", "cud1",
   "cuu1", "cuu", "vpa" are disabled; and the "home" string is set to
   the value of "cr". The effect is that the cursor is confined to the
   current line, and so are screen updates.  This may be used for
   enabling character-at-a-time  line editing without touching the
   rest of the screen.

curses.flash()

   La pantalla Flash. Eso es, cambiar lo a video inverso y luego
   cambie lo de nuevo en un corto intervalo.  Algunas personas
   prefieren como 'campana visible' para la señal de atención audible
   producida por "beep()".

curses.flushinp()

   Vacíe todos los búferes de entrada.  Esto desecha cualquier
   mecanografiado que ha sido escrito por el usuario y no ha sido aún
   procesado por el programa.

curses.getmouse()

   Después de "getch()" retorna "KEY_MOUSE" para señalar un evento de
   mouse, se debe llamar a este método para recuperar el evento de
   mouse en cola, representado como una tupla de 5 "(id, x, y, z,
   bstate)". *id* es un valor de ID que se utiliza para distinguir
   varios dispositivos, y *x*, *y*, *z* son las coordenadas del
   evento. (*z* no se usa actualmente.) *bstate* es un valor entero
   cuyos bits se establecerán para indicar el tipo de evento, y será
   el OR bit a bit de una o más de las siguientes constantes, donde
   *n* es el botón número de 1 a 5: "BUTTONn_PRESSED",
   "BUTTONn_RELEASED", "BUTTONn_CLICKED", "BUTTONn_DOUBLE_CLICKED",
   "BUTTONn_TRIPLE_CLICKED", "BUTTON_SHIFT", "BUTTON_CTRL",
   "BUTTON_ALT".

   Distinto en la versión 3.10: Las constantes "BUTTON5_*" ahora están
   expuestas si son proporcionadas por la biblioteca curses
   subyacente.

curses.getsyx()

   Retorna las coordenadas actuales del cursor en la pantalla virtual
   como una tupla "(y, x)".  Si "leaveok" es actualmente "True"
   entonces retorna "(-1,-1)".

curses.getwin(file)

   Read window-related data stored in the file by an earlier
   "window.putwin()" call. The routine then creates and initializes a
   new window using that data, returning the new window object.  The
   *file* argument must be a file object opened for reading in binary
   mode.

curses.has_colors()

   Retorna "True" si el terminal puede desplegar colores, en caso
   contrario, retorna "False".

curses.has_extended_color_support()

   Return "True" if the module supports extended colors; otherwise,
   return "False". Extended color support allows more than 256 color
   pairs for terminals that support more than 16 colors (for example,
   xterm-256color).

   El soporte de color extendido requiere ncurses versión 6.1 o
   posterior.

   Added in version 3.10.

curses.has_ic()

   Retorna "True" si el terminal tiene la capacidad de insertar y
   eliminar caracteres.  Esta función es incluida por razones
   históricas solamente, ya que todos los emuladores de la terminal de
   software modernos tienen tales capacidades.

curses.has_il()

   Retorna "True" si la terminal tiene la capacidad de insertar y
   eliminar caracteres o pueden simularlos usando las regiones de
   desplazamiento.  Esta función es incluida por razones históricas
   solamente, como todos los emuladores de terminales de software
   modernos tienen tales capacidades.

curses.has_key(ch)

   Toma una clave valor *ch*, y retorna "True" si el tipo de terminal
   actual reconoce una clave con ese valor.

curses.halfdelay(tenths)

   Usado por el modo de medio retardo, el cual es similar al modo
   *cbreak* en que los caracteres escritos por el usuario están
   disponibles inmediatamente para el programa.  Sin embargo, después
   de bloquearlos por *tenths* décimas de segundos, se lanza una
   excepción si nada ha sido escrito. El valor de *tenths* debe ser un
   número entre "1" y "255".  Use "nocbreak()" para salir del modo de
   medio retardo.

curses.init_color(color_number, r, g, b)

   Change the definition of a color, taking the number of the color to
   be changed followed by three RGB values (for the amounts of red,
   green, and blue components).  The value of *color_number* must be
   between "0" and "COLORS - 1".  Each of *r*, *g*, *b*, must be a
   value between "0" and "1000".  When "init_color()" is used, all
   occurrences of that color on the screen immediately change to the
   new definition.  This function is a no-op on most terminals; it is
   active only if "can_change_color()" returns "True".

curses.init_pair(pair_number, fg, bg)

   Change the definition of a color-pair.  It takes three arguments:
   the number of the color-pair to be changed, the foreground color
   number, and the background color number.  The value of
   *pair_number* must be between "1" and "COLOR_PAIRS - 1" (the "0"
   color pair can only be changed by "use_default_colors()" and
   "assume_default_colors()"). The value of *fg* and *bg* arguments
   must be between "0" and "COLORS - 1", or, after calling
   "use_default_colors()" or "assume_default_colors()", "-1". If the
   color-pair was previously initialized, the screen is refreshed and
   all occurrences of that color-pair are changed to the new
   definition.

curses.initscr()

   Inicializa la librería. Retorna un objeto window el cual representa
   a toda la pantalla.

   See "setupterm()" for a caveat about calling it before this
   function.

   Nota:

     Si hay un error al abrir el terminal, la librería curses
     subyacente puede causar que el interprete salga.

curses.intrflush(flag)

   If *flag* is "True", pressing an interrupt key (interrupt, break,
   or quit) will flush all output in the terminal driver queue.  If
   *flag* is "False", no flushing is done.

curses.is_term_resized(nlines, ncols)

   Retorna "True" si "resize_term()" modificaría la estructura de la
   ventana, "False" en caso contrario.

curses.isendwin()

   Retorna "True" si "endwin()" ha sido llamado (eso es que la
   librería curses ha sido desinicializada).

curses.keyname(k)

   Retorna el nombre de la tecla enumerada *k* como un objeto de
   bytes.  El nombre de una tecla que genera un carácter ASCII
   imprimible es el carácter de la tecla.  El nombre de una
   combinación de teclas de control es un consistente objeto de bytes
   de dos bytes de un signo de intercalación ("b'^'") seguido por el
   correspondiente carácter ASCII imprimible. El nombre de una
   combinación de tecla *alt* (128-255) es un objeto de bytes
   consistente del prefijo "b'M-'" seguido por el nombre del
   correspondiente carácter ASCII.

   Raise a "ValueError" if *k* is negative.

curses.killchar()

   Retorna el carácter de eliminación de la línea actual del usuario
   como un objeto de bytes de un byte.  Bajo el sistema operativo Unix
   esta es una propiedad del controlador *tty* del programa *curses*,
   y no está configurado por la librería *curses* por sí mismo.

curses.longname()

   Retorna un objeto de bytes que contiene el campo de nombre largo
   *terminfo* que describe el terminal actual.  La longitud máxima de
   una descripción verbosa es 128 caracteres.  Esto es definido
   solamente después de la llamada a "initscr()".

curses.meta(flag)

   Si *flag* es "True", permite caracteres de 8 bits para ser
   introducidos.  Si *flag* es "False", permite solamente caracteres
   de 7 bits.

curses.mouseinterval(interval)

   Set the maximum time in milliseconds that can elapse between press
   and release events in order for them to be recognized as a click,
   and return the previous interval value.  The default value is 166
   milliseconds, or one sixth of a second. Use a negative *interval*
   to obtain the interval value without changing it.

curses.mousemask(mousemask)

   Set the mouse events to be reported, and return a tuple
   "(availmask, oldmask)".   *availmask* indicates which of the
   specified mouse events can be reported; on complete failure it
   returns "0".  *oldmask* is the previous value of the mouse event
   mask.  If this function is never called, no mouse events are ever
   reported.

curses.napms(ms)

   Duerme durante *ms* milisegundos.

curses.newpad(nlines, ncols)

   Crea y retorna un apuntador para una nueva estructura de datos de
   *pad* con el número dado de líneas y columnas.  Retorna un *pad*
   como un objeto de ventana.

   A pad is like a window, except that it is not restricted by the
   screen size, and is not necessarily associated with a particular
   part of the screen.  Pads can be used when a large window is
   needed, and only a part of the window will be on the screen at one
   time.  Automatic refreshes of pads (such as from scrolling or
   echoing of input) do not occur.  The "refresh()" and
   "noutrefresh()" methods of a pad require 6 arguments to specify the
   part of the pad to be displayed and the location on the screen to
   be used for the display. The arguments are *pminrow*, *pmincol*,
   *sminrow*, *smincol*, *smaxrow*, *smaxcol*; the *p* arguments refer
   to the upper-left corner of the pad region to be displayed and the
   *s* arguments define a clipping box on the screen within which the
   pad region is to be displayed.

curses.newwin(nlines, ncols)
curses.newwin(nlines, ncols, begin_y, begin_x)

   Retorna una nueva window, cuya esquina superior izquierda esta en
   "(begin_y, begin_x)", y cuyo alto/ancho es *nlines*/*ncols*.

   Por defecto, la ventana extenderá desde la posición especificada
   para la esquina inferior derecha de la pantalla.

curses.nl(flag=True)

   Ingrese al modo de línea nueva.  Este modo pone la tecla de retorno
   en una nueva línea en la entrada, y traduce la nueva línea en
   retorno y avance de línea en la salida. El modo de nueva línea está
   inicialmente encendida.

   If *flag* is "False", the effect is the same as calling "nonl()".

curses.nocbreak()

   Salir del modo *cbreak*.  Retorne al modo normal "cooked" con la
   línea del búfer.

curses.noecho()

   Salir del modo echo. El eco de los caracteres de entrada está
   desactivado.

curses.nonl()

   Dejar el modo de nueva línea. Desactiva la traducción de retorno en
   una nueva línea en la entrada, y desactiva la traducción a bajo
   nivel de una nueva línea en nueva línea/retorno en la salida (pero
   esto no cambia el comportamiento de "addch('\n')", el cual siempre
   es el equivalente de retornar y avanzar la línea en la pantalla
   virtual). Con las traducciones apagadas, *curses* puede aumentar
   algunas veces la velocidad del movimiento vertical un poco;
   también, estará disponible para detectar la tecla de retorno en la
   entrada.

curses.noqiflush()

   Cuando la rutina "noqiflush()" es usada, descarga normal de colas
   de entrada y salida asociadas con el "INTR", los caracteres "QUIT"
   and "SUSP" no serán hechos.  Puedes querer llamar "noqiflush()" en
   un manejador de señales si quieres que la salida continúe como si
   la interrupción no hubiera ocurrido después de que el manejador
   exista.

curses.noraw()

   Salir del modo raw. Retorna al modo normal "cooked" con la línea
   del búfer.

curses.pair_content(pair_number)

   Retorna una tupla "(fg, bg)" conteniendo los colores del par de
   color solicitado. El valor de *pair_number* debe ser entre "0" y
   "COLOR_PAIRS-1".

curses.pair_number(attr)

   Retorna el numero del conjunto de pares de colores para el valor
   del atributo *attr*. "color_pair()" es la contraparte de esta
   función.

curses.putp(str)

   Equivalente a "tputs(str, 1, putchar)"; emite el valor de una
   capacidad especificada *terminfo* para el terminal actual. Nota que
   la salida de "putp()" siempre va a la salida estándar.

   "setupterm()" (or "initscr()") must be called first.

curses.qiflush([flag])

   Si *flag* es "False", el efecto es el mismo como llamar
   "noqiflush()".  Si *flag* es "True",  o el argumento no es
   proveído, la cola será nivelada cuando estos caracteres de control
   son leídos.

curses.raw()

   Entrar al modo crudo.  En el modo crudo, el almacenamiento en búfer
   de la línea normal y procesamiento de las teclas de interrupción,
   salida, suspensión y control de flujo son apagadas; los caracteres
   son presentados a la función de entrada de *curses* una por una.

curses.reset_prog_mode()

   Restaura la terminal para el modo "program", anteriormente guardado
   por "def_prog_mode()".

curses.reset_shell_mode()

   Restablece el terminal al modo "shell" como lo guardó previamente
   "def_shell_mode()".

curses.resetty()

   Restablece el estado del modo del terminal para lo que esto fue en
   el último llamado a "savetty()".

curses.resize_term(nlines, ncols)

   La función *backend* usada por "resizeterm()", caracteriza más de
   el trabajo; cuando se redimensiona la ventana, "resize_term()" los
   rellenos blancos de las áreas que son extendidas.  La aplicación de
   llamada llenaría en estas áreas con datos apropiados.  La función
   "resize_term()" intenta redimensionar todas las ventanas.  Sin
   embargo, debido a la convención de llamadas del las almohadillas,
   esto no es posible para redimensionar estos sin interacciones
   adicionales con la aplicación.

curses.resizeterm(nlines, ncols)

   Ajusta el tamaño al estándar y la ventana actual para las
   dimensiones especificadas, y ajusta otros datos contables usados
   por la librería *curses* que registra las dimensiones de la ventana
   (en particular el manejador SIGWINCH ).

curses.savetty()

   Guarda el estado actual del modo del terminal en un búfer, usable
   por "resetty()".

curses.get_escdelay()

   Recupera el valor establecido por "set_escdelay()".

   Added in version 3.9.

curses.set_escdelay(ms)

   Establece el número de milisegundos de espera después de leer un
   carácter de escape, para distinguir entre un carácter de escape
   individual ingresado en el teclado de las secuencias de escape
   enviadas por el cursor y las teclas de función.

   Added in version 3.9.

curses.get_tabsize()

   Recupera el valor establecido por "set_tabsize()".

   Added in version 3.9.

curses.set_tabsize(size)

   Establece el número de columnas utilizadas por la biblioteca de
   curses al convertir un carácter de tabulación en espacios, ya que
   agrega la tabulación a una ventana.

   Added in version 3.9.

curses.setsyx(y, x)

   Fija el cursor de la pantalla virtual para *y*, *x*.  Si *y* y *x*
   son ambos "-1", entonces "leaveok" es configurado "True".

curses.setupterm(term=None, fd=-1)

   Inicializa la terminal.  *term* es una cadena de caracteres dando
   el nombre de la terminal, o "None"; si es omitido o "None", el
   valor de la variable de entorno "TERM" será usada.  *fd* es el
   archivo descriptor al cual alguna secuencia de inicialización será
   enviada; si no es suministrada o "-1", el archivo descriptor para
   "sys.stdout" será usado.

   Raise a "curses.error" if the terminal could not be found or its
   terminfo database entry could not be read.  If the terminal has
   already been initialized, this function has no effect.

   Nota:

     Calling "initscr()" after "setupterm()" leaks the terminal that
     "setupterm()" allocated: the curses library keeps only a single
     current terminal and does not free the previously allocated one.

curses.start_color()

   Debe ser llamado si el programador quiere usar colores, y antes de
   que cualquier otra rutina de manipulación de colores sea llamada.
   Esta es una buena práctica para llamar esta rutina inmediatamente
   después de "initscr()".

   "start_color()" initializes eight basic colors (black, red,  green,
   yellow, blue, magenta, cyan, and white), and two global variables
   in the "curses" module, "COLORS" and "COLOR_PAIRS", containing the
   maximum number of colors and color-pairs the terminal can support.
   It also restores the colors on the terminal to the values they had
   when the terminal was just turned on.

curses.termattrs()

   Retorna un *OR* lógico de todos los atributos del video soportados
   por el terminal.  Esta información es útil cuando un programa
   *curses* necesita completar el control sobre la apariencia de la
   pantalla.

curses.termname()

   Retorna el valor de la variable de entorno "TERM", como un objeto
   de bytes, trucado para 14 caracteres.

curses.tigetflag(capname)

   Retorna el valor de la capacidad booleana correspondiente al nombre
   de la capacidad *terminfo* *capname* como un número entero.
   Retorna el valor "-1" si *capname* no es una capacidad booleana, o
   "0" si es cancelada o ausente desde la descripción de la terminal.

   "setupterm()" (or "initscr()") must be called first.

curses.tigetnum(capname)

   Retorna el valor de la capacidad numérica correspondiente al nombre
   de la capacidad *terminfo* *capname* como un entero.  Regresa el
   valor "-2" si *capname* no es una capacidad numérica, o "-1" si
   esta es cancelada o ausente desde la descripción del terminal.

   "setupterm()" (or "initscr()") must be called first.

curses.tigetstr(capname)

   Retorna el valor de la capacidad de la cadena de caracteres
   correspondiente al nombre de la capacidad *terminfo* *capname* como
   un objeto de bytes.  Retorna "None" si *capname* no es una
   "capacidad de cadena de caracteres" de *terminfo*, o es cancelada o
   ausente desde la descripción de la terminal.

   "setupterm()" (or "initscr()") must be called first.

curses.tparm(str[, ...])

   Instantiate the bytes object *str* with the supplied parameters,
   where *str* should be a parameterized string obtained from the
   terminfo database.  For example, "tparm(tigetstr("cup"), 5, 3)"
   could result in "b'\033[6;4H'", the exact result depending on
   terminal type.  Up to nine integer parameters may be supplied.

   "setupterm()" (or "initscr()") must be called first.

curses.typeahead(fd)

   Especifica que el descriptor de archivo *fd* es usado para la
   verificación anticipada. Si *fd* es "-1", entonces no se realiza
   ninguna verificación anticipada.

   La librería *curses* hace "la optimización del rompimiento de
   línea" por la búsqueda para mecanografiar periódicamente mientras
   se actualiza la pantalla.  Si la entrada es encontrada, y viene
   desde un *tty*, la actualización actual es pospuesta hasta que se
   vuelva a llamar la actualización, permitiendo la respuesta más
   rápida para comandos escritos en avance.  Esta función permite
   especificar un archivo diferente al descriptor para la verificación
   anticipada.

curses.unctrl(ch)

   Regresa un objeto de bytes el cual es una representación imprimible
   del carácter *ch*.  Los caracteres de control son representados
   como un símbolo de intercalación seguido del carácter, por ejemplo
   como "b'^C'".  La impresión de caracteres son dejados como están.

curses.ungetch(ch)

   Presiona *ch* para que el siguiente "getch()" lo retorne.

   Nota:

     Solamente un *ch* puede ser colocado antes "getch()" es llamada.

curses.update_lines_cols()

   Update the "LINES" and "COLS" module variables. Useful for
   detecting manual screen resize.

   Added in version 3.5.

curses.unget_wch(ch)

   Presiona *ch* para que el siguiente "get_wch()" lo retorne.

   Nota:

     Solamente un *ch* puede ser presionado antes "get_wch()" es
     llamada.

   Added in version 3.3.

curses.ungetmouse(id, x, y, z, bstate)

   Coloca un evento "KEY_MOUSE" en la cola de entrada, asociando el
   estado de los datos dados con esto.

curses.use_env(flag)

   Si es usado, esta función sería llamada antes de "initscr()" o
   *newterm* son llamados.  Cuando *flag* es "False", los valores de
   líneas y columnas especificadas en la base de datos *terminfo* será
   usado, incluso si las variables de entorno "LINES" y "COLUMNS"
   (usadas por defecto) son configuradas, o si *curses* está corriendo
   en una ventana (en cuyo caso el comportamiento por defecto sería
   usar el tamaño de ventana si "LINES" y "COLUMNS" no están
   configuradas).

curses.use_default_colors()

   Equivalent to "assume_default_colors(-1, -1)".

curses.wrapper(func, /, *args, **kwargs)

   Inicializa *curses* y llama a otro objeto invocable, *func*, el
   cual debería ser el resto de tu aplicación que usa *curses*.  Si la
   aplicación lanza una excepción, esta función restaurará la terminal
   para un estado sano antes de re-lanzar la excepción y generar un
   una pista.  El objeto invocable *func* es entonces pasado a la
   ventana principal 'stdscr' como su primer argumento, seguido por
   algún otro argumento pasado a "wrapper()".  Antes de llamar a
   *func*, "wrapper()" habilita el modo *cbreak*, desactiva echo,
   permite el teclado del terminal, e inicializa los colores si la
   terminal tiene soporte de color.  En salida (ya sea normal o por
   excepción) esto restaura el modo *cooked*, habilita el echo, y
   desactiva el teclado del terminal.

## Window objects

class curses.window

   Los objetos ventana, retornados por "initscr()" y "newwin()"
   anteriores, tienen los siguientes métodos y atributos:

window.addch(ch[, attr])
window.addch(y, x, ch[, attr])

   Pinta el carácter *ch* en "(y, x)" con atributos *attr*,
   sobrescribiendo cualquier carácter pintado previamente en esa
   ubicación. De forma predeterminada, la posición y los atributos del
   carácter son la configuración actual del objeto ventana.

   Nota:

     Writing outside the window, subwindow, or pad raises a
     "curses.error". Attempting to write to the lower-right corner of
     a window, subwindow, or pad will cause an exception to be raised
     after the character is printed.

window.addnstr(str, n[, attr])
window.addnstr(y, x, str, n[, attr])

   Pintar como máximo *n* caracteres de la cadena de texto *str* en
   "(y,x)" con atributos *attr*, sobrescribiendo algo previamente en
   la pantalla.

window.addstr(str[, attr])
window.addstr(y, x, str[, attr])

   Dibuja la cadena de caracteres *str* en "(y,x)" con atributos
   *attr*, sobrescribiendo cualquier cosa previamente en la pantalla.

   Nota:

     * Writing outside the window, subwindow, or pad raises
       "curses.error". Attempting to write to the lower-right corner
       of a window, subwindow, or pad will cause an exception to be
       raised after the string is printed.

     * A bug in ncurses, the backend for this Python module, could
       cause segfaults when resizing windows.  This was fixed in
       ncurses-6.1-20190511. If you are stuck with an earlier ncurses,
       you can avoid triggering it by not calling "addstr()" with a
       *str* that has embedded newlines; instead, call "addstr()"
       separately for each line.

window.attroff(attr)

   Remueve el atributo *attr* desde el conjunto "background" aplicado
   a todos los escritos para la ventana actual.

window.attron(attr)

   Add attribute *attr* to the "background" set applied to all writes
   to the current window.

window.attrset(attr)

   Establezca el conjunto de atributos "background para *attr*.  Este
   conjunto es inicialmente "0" (sin atributos).

window.bkgd(ch[, attr])

   Configura la propiedad de fondo de la ventana para el carácter
   *ch*, con atributos *atte*.  El cambio es entonces aplicado para la
   posición de cada carácter en esa ventana:

   * El atributo de cada carácter en la ventana es cambiado por el
     nuevo atributo de fondo.

   * Dónde quiera que el carácter del fondo anterior aparezca, es
     cambiado al nuevo carácter de fondo.

window.bkgdset(ch[, attr])

   Configura el fondo de la ventana.  Un fondo de ventana consiste de
   un carácter y cualquier combinación de atributos.  La parte del
   atributo del fondo es combinado (OR' ed) con todos los caracteres
   que no son blancos escritos en la ventana.  Tanto las partes del
   carácter y del atributo del fondo son combinados con los caracteres
   en blanco.  El fondo se convierte en una propiedad del carácter y
   se mueve con el carácter a través de cualquier operación de
   desplazamiento e inserción/eliminación de línea/carácter.

window.border([ls[, rs[, ts[, bs[, tl[, tr[, bl[, br]]]]]]]])

   Dibuja un borde alrededor de las orillas de la ventana.  Cada
   parámetro especifica el carácter a usar para una parte específica
   del borde; ve la tabla abajo para más detalles.

   Nota:

     Un valor "0" para cualquier parámetro causará el carácter por
     defecto a ser usado para ese parámetro. parámetros de palabras
     clave pueden *no* ser usados. Los valores predeterminados son
     listados en esta tabla:

   +-------------+-----------------------+-------------------------+
   | Parámetro   | Descripción           | Valor por defecto       |
   |=============|=======================|=========================|
   | *ls*        | Lado izquierdo        | "ACS_VLINE"             |
   +-------------+-----------------------+-------------------------+
   | *rs*        | Lado derecho          | "ACS_VLINE"             |
   +-------------+-----------------------+-------------------------+
   | *ts*        | Arriba                | "ACS_HLINE"             |
   +-------------+-----------------------+-------------------------+
   | *bs*        | Abajo                 | "ACS_HLINE"             |
   +-------------+-----------------------+-------------------------+
   | *tl*        | Esquina superior      | "ACS_ULCORNER"          |
   |             | izquierda             |                         |
   +-------------+-----------------------+-------------------------+
   | *tr*        | Esquina superior      | "ACS_URCORNER"          |
   |             | derecha               |                         |
   +-------------+-----------------------+-------------------------+
   | *bl*        | Esquina inferior      | "ACS_LLCORNER"          |
   |             | izquierda             |                         |
   +-------------+-----------------------+-------------------------+
   | *br*        | Esquina inferior      | "ACS_LRCORNER"          |
   |             | derecha               |                         |
   +-------------+-----------------------+-------------------------+

window.box([vertch, horch])

   Similar a "border()", pero ambos *ls y *rs* son *vertch* y ambos
   *ts* y *bs* son *horch*.  Los caracteres de esquina predeterminados
   son siempre usados por esta función.

window.chgat(attr)
window.chgat(num, attr)
window.chgat(y, x, attr)
window.chgat(y, x, num, attr)

   Configura los atributos de *num* de caracteres en la posición del
   cursor, o una posición "(y, x)" si es suministrado.  Si *num* no es
   dado o es "-1", el atributo será configurado en todos los
   caracteres para el final de la línea.  Esta función mueve el cursor
   a la posición "(y, x)" si es suministrado.  La línea cambiada será
   tocada usando el método "touchline()" tal que el contenido será
   vuelto a mostrar por la actualización de la siguiente ventana.

window.clear()

   Semejante a "erase()", pero también causa que toda la ventana sea
   repintada sobre la siguiente llamada para "refresh()".

window.clearok(flag)

   Si *flag* es "True", la siguiente llamada para "refresh()" limpiará
   la ventana completamente.

window.clrtobot()

   Borrar desde el cursor hasta el final de la ventana: todas las
   líneas bajo el cursor son eliminadas, y entonces el equivalente de
   "clrtoeol()" es realizado.

window.clrtoeol()

   Borrar desde el cursor hasta el final de la línea.

window.cursyncup()

   Actualice la posición actual del cursor de todos los ancestros de
   la ventana para reflejar la posición actual del cursor de la
   ventana.

window.delch([y, x])

   Delete the character under the cursor, or at "(y, x)" if specified.
   All characters to the right on the same line are shifted one
   position left.

window.deleteln()

   Borra la línea bajo el cursor.  Todas las líneas siguientes son
   movidas una línea hacía arriba.

window.derwin(begin_y, begin_x)
window.derwin(nlines, ncols, begin_y, begin_x)

   Una abreviación para "ventana derivada", "derwin()" es el mismo
   cómo llamar "subwin()", excepto que *begin_y* y *begin_x* son
   relativos al origen de la ventana, más bien relativo a la pantalla
   completa.  Retorna un objeto ventana para la ventana derivada.

window.echochar(ch[, attr])

   Añada el carácter *ch* con atributo *attr*, e inmediatamente llame
   a "refresh()" en la ventana.

window.enclose(y, x)

   Pruebe si el par dado de las coordenadas de celda del carácter
   relativas de la ventana son encerrados por la ventana dada,
   retornando "True" o "False". Esto es útil para determinar que
   subconjunto de las ventanas de pantalla encierran la locación de un
   evento del mouse.

   Distinto en la versión 3.10: Anteriormente retornaba "1" o "0" en
   lugar de "True" o "False".

window.encoding

   Encoding used to encode method arguments (Unicode strings and
   characters). The encoding attribute is inherited from the parent
   window when a subwindow is created, for example with
   "window.subwin()". By default, current locale encoding is used (see
   "locale.getencoding()").

   Added in version 3.3.

window.erase()

   Limpiar la ventana.

window.getbegyx()

   Return a tuple "(y, x)" of coordinates of upper-left corner.

window.getbkgd()

   Return the given window's current background character/attribute
   pair. Its components can be extracted like those of "inch()".

window.getch([y, x])

   Obtener un carácter.  Nota que el entero retornado *no* tiene que
   estar en el rango ASCII: teclas de función, claves de teclado y los
   demás son representados por números mayores que 255.  En el modo
   sin demora, retorna "-1" si no hay entrada, en caso contrario
   espere hasta que una tecla es presionada.

window.get_wch([y, x])

   Obtener un carácter amplio.  Retorna un carácter para la mayoría de
   las teclas, o un entero para las teclas de función, teclas del
   teclado, y otras teclas especiales.  En modo de no retorna, genera
   una excepción si no hay entrada.

   Added in version 3.3.

window.getkey([y, x])

   Obtener un carácter, retornando una cadena de caracteres en lugar
   de un entero, como "getch()" lo hace.  Las teclas de función,
   teclas del teclado y otras teclas especiales retornan una cadena
   *multibyte* conteniendo el nombre de la tecla.  En modo de no
   retardo, genera una excepción si no hay entrada.

window.getmaxyx()

   Retorna una tupla "(y,x)" de el alto y ancho de la ventana.

window.getparyx()

   Retorne las coordenadas iniciales de esta ventana relativa para su
   ventana padre como una tupla "(y, x)".  Retorna "(-1, -1)" si esta
   ventana no tiene padre.

window.getstr()
window.getstr(n)
window.getstr(y, x)
window.getstr(y, x, n)

   Read a bytes object from the user, with primitive line editing
   capacity. At most *n* characters are read; *n* defaults to and
   cannot exceed 2047.

   Distinto en la versión 3.14: The maximum value for *n* was
   increased from 1023 to 2047.

window.getyx()

   Retorna una tupla "(y, x)" de la posición actual del cursor
   relativa para la esquina superior izquierda de la ventana.

window.hline(ch, n[, attr])
window.hline(y, x, ch, n[, attr])

   Display a horizontal line starting at "(y, x)" with length *n*
   consisting of the character *ch* with attributes *attr*.  The line
   stops at the right edge of the window if fewer than *n* cells are
   available.

window.idcok(flag)

   Si *flag* es "False", *curses* ya no considera el uso de la función
   de insertar/eliminar caracteres de hardware del terminal; si *flag*
   "True", el uso de inserción y borrado  de caracteres está
   habilitado.  Cuando *curses* es inicializado primero, el uso de
   caracteres de inserción / borrado está habilitado por defecto.

window.idlok(flag)

   If *flag* is "True", "curses" will try to use hardware line editing
   facilities.  Otherwise, curses will not use them.

window.immedok(flag)

   Si *flag* es "True", cualquier cambio en la imagen de la ventana
   automáticamente causará que la ventana sea refrescada; ya no tienes
   que llamar a "refresh()" por ti mismo.  Sin embargo, esto puede
   degradar el rendimiento considerablemente, debido a las
   repeticiones de llamada a *wrefresh*.  Esta opción está
   deshabilitada por defecto.

window.inch([y, x])

   Return the character at the given position in the window. The
   bottom 8 bits are the character proper and the upper bits are the
   attributes; extract them with the "A_CHARTEXT" and "A_ATTRIBUTES"
   bit-masks, and the color pair with "pair_number()". The character
   byte is the locale-encoded byte of the cell's character, consistent
   with "instr()". On a wide-character build, a character that does
   not fit in a single byte in the current locale has a character byte
   of "0"; use "instr()" to read such characters.

window.insch(ch[, attr])
window.insch(y, x, ch[, attr])

   Insert character *ch* with attributes *attr* before the character
   under the cursor, or at "(y, x)" if specified.  All characters to
   the right of the cursor are shifted one position right, with the
   rightmost character on the line being lost.  The cursor position
   does not change.

window.insdelln(nlines)

   Inserta *nlines* líneas en la ventana especificada arriba de la
   línea actual.  Las *nlines* líneas de fondo se pierden.  Para
   *nlines* negativos, elimine *nlines* líneas comenzando con la que
   está debajo del cursor, y mueve las restantes hacia arriba. Se
   borran las *nlines* líneas inferiores.  La posición del cursor
   actual se mantiene igual.

window.insertln()

   Inserte una línea en blanco bajo el cursos.  Las líneas siguientes
   se moverán una línea hacía abajo.

window.insnstr(str, n[, attr])
window.insnstr(y, x, str, n[, attr])

   Inserte una cadena de caracteres (tantos caracteres quepan en la
   línea) antes los caracteres bajo el cursor, sobre los *n*
   caracteres.  Si *n* es cero o negativo, la cadena entera es
   insertada.  Todos los caracteres a la derecha de el cursor son
   desplazados a la derecha, perdiéndose los caracteres de la derecha
   en la línea.  La posición del cursor no cambia (después de mover a
   *y*, *x*, si es especificado).

window.insstr(str[, attr])
window.insstr(y, x, str[, attr])

   Inserte una cadena de caracteres ( tantos caracteres encajen en la
   línea) antes los caracteres bajo el cursor.  Todos los caracteres a
   la derecha de el cursor son desplazados a la derecha, perdiéndose
   los caracteres de la derecha en línea.

window.instr([n])
window.instr(y, x[, n])

   Return a bytes object of characters, extracted from the window
   starting at the current cursor position, or at *y*, *x* if
   specified, and stopping at the end of the line. Attributes and
   color information are stripped from the characters.  If *n* is
   specified, "instr()" returns a string at most *n* characters long
   (exclusive of the trailing NUL). The maximum value for *n* is 2047.

   Distinto en la versión 3.14: The maximum value for *n* was
   increased from 1023 to 2047.

window.is_linetouched(line)

   Retorna "True" si la línea especificada fue modificada desde la
   última llamada a "refresh()"; de otra manera retorna "False".
   Genera una excepción "curses.error" si *line* no es válida para la
   ventana dada.

window.is_wintouched()

   Retorna "True" si la ventana especificada fue modificada desde la
   última llamada para "refresh()"; en caso contrario, retorna
   "False".

window.keypad(flag)

   If *flag* is "True", escape sequences generated by some keys
   (keypad,  function keys) will be interpreted by "curses". If *flag*
   is "False", escape sequences will be left as is in the input
   stream.

window.leaveok(flag)

   If *flag* is "True", cursor is left where it is on update, instead
   of being at "cursor position."  This reduces cursor movement where
   possible.

   Si *flag* es "False", el cursor siempre estará en "cursor position"
   después de una actualización.

window.move(new_y, new_x)

   Mueve el cursor a "(new_y, new_x)".

window.mvderwin(y, x)

   Mueve la ventana adentro de su ventana padre.  Los parámetros
   relativos a la pantalla de la ventana no son cambiados.  Esta
   rutina es usada para mostrar diferentes partes de la ventana padre
   en la misma posición física en la pantalla.

window.mvwin(new_y, new_x)

   Mueve la ventana a su esquina superior izquierda que está en
   "(new_y,new_x)".

   Moving the window so that any part of it would be off the screen is
   an error: the window is not moved and "curses.error" is raised.

window.nodelay(flag)

   Si *flag* es "True", "getch()" no será bloqueada.

window.notimeout(flag)

   Si *flag* es "True", las secuencias de escape no serán agotadas.

   Si *flag* es "False", después de pocos milisegundos, una secuencia
   de escape no será interpretada, y será dejada en el flujo de
   entrada como está.

window.noutrefresh()
window.noutrefresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)

   Marque para actualizar pero espere.  Esta función actualiza la
   estructura de datos representando el estado deseado de la ventana,
   pero no fuerza una actualización en la pantalla física.  Para
   realizar eso, llame "doupdate()".

   The 6 arguments can only be specified, and are then required, when
   the window is a pad created with "newpad()"; they have the same
   meaning as for "refresh()".

window.overlay(destwin[, sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol])

   Cubre la ventana en la parte superior de *destwin*.  La ventana no
   necesita ser del mismo tamaño, solamente se solapa la región
   copiada.  Esta copia no es destructiva, lo que significa que el
   carácter de fondo actual no sobre-escribe el contenido viejo de
   *destwin*.

   Para obtener el control de grano fino sobre la región copiada, la
   segunda forma de "overlay()" puede ser usada.  *sminrow* y
   *smincol* son las coordenadas superior izquierda de la ventana de
   origen, y las otras variables marcan un rectángulo en la ventana
   destino.

window.overwrite(destwin[, sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol])

   Sobre-escribe la ventana en la parte superior de *destwin*.  La
   ventana no necesita ser del mismo tamaño, en cuyo caso solamente se
   sobrepone la región que es copiada.  Esta copia es destructiva, lo
   cual significa que el carácter de fondo actual sobre-escribe el
   contenido viejo de *destwin*.

   Para obtener el control de grano fino sobre la región copiada, la
   segunda forma de "overwrite()" puede ser usada.  *sminrow* y
   *smincol* son las coordenadas superior izquierda de la ventana
   origen, las otras variables marcan un rectángulo en la ventana de
   destino.

window.putwin(file)

   Escribe todos los datos asociados con la ventana en el objeto de
   archivo proveído.  Esta información puede estar después recuperada
   usando la función "getwin()".

window.redrawln(beg, num)

   Indica que el *num* de líneas de la pantalla, empiezan en la línea
   *beg*, son corruptos y deberían ser completamente redibujado en la
   siguiente llamada "refresh()".

window.redrawwin()

   Toca la ventana completa, causando que se vuelva a dibujar
   completamente en la siguiente llamada "refresh()" .

window.refresh([pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol])

   Actualiza la pantalla inmediatamente (sincronice la pantalla actual
   con los métodos previos de dibujar/borrar).

   The 6 arguments can only be specified, and are then required, when
   the window is a pad created with "newpad()".  The additional
   parameters are needed to indicate what part of the pad and screen
   are involved. *pminrow* and *pmincol* specify the upper-left corner
   of the rectangle to be displayed in the pad.  *sminrow*, *smincol*,
   *smaxrow*, and *smaxcol* specify the edges of the rectangle to be
   displayed on the screen.  The lower-right corner of the rectangle
   to be displayed in the pad is calculated from the screen
   coordinates, since the rectangles must be the same size.  Both
   rectangles must be entirely contained within their respective
   structures.  Negative values of *pminrow*, *pmincol*, *sminrow*, or
   *smincol* are treated as if they were zero.

window.resize(nlines, ncols)

   Redistribuir el almacenamiento para una ventana *curses* para
   ajustar su dimensión para los valores especificados.  Si la
   dimensión también es mayor que los valores actuales, los datos de
   la ventana serán llenados con espacios en blanco que tiene la
   ejecución del fondo actual (como ajustado por "bkgdset()")
   uniéndolos.

window.scroll([lines=1])

   Scroll the screen or scrolling region.  Scroll upward by *lines*
   lines if *lines* is positive, or downward if it is negative.
   Scrolling has no effect unless it has been enabled for the window
   with "scrollok()".

window.scrollok(flag)

   Control que sucede cuando el cursor de una ventana es movida fuera
   del borde de la ventana o región de desplazamiento, también como un
   resultado de una acción de nueva línea en la línea inferior, o
   escribiendo el último carácter de la última línea.  Si *flag* es
   "False", el cursor está a la izquierda sobre la línea inferior.  Si
   *flag* es "True", la ventana será desplazada hacía arriba por una
   línea.  Note que en orden para obtener el efecto del desplazamiento
   físico en el terminal, también será necesario llamar "idlok()".

window.setscrreg(top, bottom)

   Configura la región de desplazamiento desde la línea *top* hasta la
   línea *bottom*. Todas las acciones de desplazamiento tomarán lugar
   en esta región.

window.standend()

   Desactive el atributo destacado.  En algunos terminales esto tiene
   el efecto secundario de desactivar todos los atributos.

window.standout()

   Active el atributo *A_STANDOUT*.

window.subpad(begin_y, begin_x)
window.subpad(nlines, ncols, begin_y, begin_x)

   Return a sub-pad, whose upper-left corner is at "(begin_y,
   begin_x)", and whose width/height is *ncols*/*nlines*.  The
   coordinates are relative to the parent pad (unlike "subwin()",
   which uses screen coordinates).  This method is only available for
   pads created with "newpad()".

window.subwin(begin_y, begin_x)
window.subwin(nlines, ncols, begin_y, begin_x)

   Return a sub-window, whose upper-left corner is at the screen-
   relative coordinates "(begin_y, begin_x)", and whose width/height
   is *ncols*/*nlines*.

   Por defecto, la sub-ventana extenderá desde la posición
   especificada para la esquina inferior derecha de la ventana.

window.syncdown()

   Toca cada ubicación en la ventana que ha sido tocado por alguna de
   sus ventanas padres.  Esta rutina es llamada por "refresh()", esto
   casi nunca debería ser necesario para llamarlo manualmente.

window.syncok(flag)

   Si *flag* es "True", entonces "syncup()" es llamada automáticamente
   cuando hay un cambio en la ventana.

window.syncup()

   Toque todas las locaciones de los ancestros de la ventana que han
   sido cambiados en la ventana.

window.timeout(delay)

   Configura el bloqueo o no bloqueo del comportamiento para la
   ventana.  Si el *delay* es negativo, bloqueando la lectura usada
   (el cual esperará indefinidamente para la entrada).  Si *delay* es
   cero, entonces no se bloqueará la lectura usada, y "getch()"
   retornará "-1" si la entrada no está esperando.  Si *delay* es
   positivo, entonces "getch()" se bloqueará por *delay* milisegundos,
   y retorna "-1" si aún no entra en el final de ese tiempo.

window.touchline(start, count[, changed])

   Supone *count* líneas han sido cambiadas, iniciando con la línea
   *start*.  Si *changed* es suministrado, específica que las líneas
   afectadas son marcadas como hayan sido cambiadas (*changed*"=True")
   o no cambiadas (*changed*"=False").

window.touchwin()

   Suponga que toda la ventana ha sido cambiada, con el fin de
   optimizar el dibujo.

window.untouchwin()

   Marque todas las líneas en la ventana como no cambiadas desde la
   última llamada para "refresh()".

window.vline(ch, n[, attr])
window.vline(y, x, ch, n[, attr])

   Display a vertical line starting at "(y, x)" with length *n*
   consisting of the character *ch* with attributes *attr*.

## Constantes

The "curses" module defines the following data members:

curses.ERR

   Algunas rutinas de *curses* que retornan un entero, tales como
   "getch()", retorna "ERR" sobre el fallo.

curses.OK

   Algunas rutinas de *curses* que retornan un entero, tales como
   "napms()", retorna "OK" tras el éxito.

curses.version

   A bytes object representing the current version of the module.

curses.ncurses_version

   Una tupla nombrada contiene los 3 componentes de la versión de la
   librería *ncurses* *major*, *minor*, y *patch*.  Todos los valores
   son enteros.  Los componentes pueden también ser accedidos por
   nombre, así "curses.ncurses_version[0]" es equivalente a
   "curses.ncurses_version.major" y así.

   Disponibilidad: si la librería ncurses es usada.

   Added in version 3.8.

curses.COLORS

   The maximum number of colors the terminal can support. It is
   defined only after the call to "start_color()".

curses.COLOR_PAIRS

   The maximum number of color pairs the terminal can support. It is
   defined only after the call to "start_color()".

curses.COLS

   The width of the screen, that is, the number of columns. It is
   defined only after the call to "initscr()". Updated by
   "update_lines_cols()", "resizeterm()" and "resize_term()".

curses.LINES

   The height of the screen, that is, the number of lines. It is
   defined only after the call to "initscr()". Updated by
   "update_lines_cols()", "resizeterm()" and "resize_term()".

Algunas constantes están disponibles para especificar los atributos
del celdas de caracteres.  Las constantes exactas disponible dependen
del sistema.

+--------------------------+---------------------------------+
| Atributo                 | Significado                     |
|==========================|=================================|
| curses.A_ALTCHARSET      | Modo de conjunto de caracteres  |
## |                          | alternativo                     |

## | curses.A_BLINK           | Modo parpadeo                   |

## | curses.A_BOLD            | Modo negrita                    |

## | curses.A_DIM             | Modo tenue                      |

## | curses.A_INVIS           | Modo invisible o en blanco      |

## | curses.A_ITALIC          | Modo cursiva                    |

## | curses.A_NORMAL          | Atributo normal                 |

## | curses.A_PROTECT         | Modo protegido                  |

| curses.A_REVERSE         | Fondo inverso y colores de      |
## |                          | primer plano                    |

## | curses.A_STANDOUT        | Modo destacado                  |

## | curses.A_UNDERLINE       | Modo subrayado                  |

## | curses.A_HORIZONTAL      | Resaltado horizontal            |

## | curses.A_LEFT            | Resaltado a la izquierda        |

## | curses.A_LOW             | Resaltado bajo                  |

## | curses.A_RIGHT           | Resaltado a la derecha          |

## | curses.A_TOP             | Resaltado arriba                |

## | curses.A_VERTICAL        | Resaltado vertical              |

Added in version 3.7: "A_ITALIC" fue añadido.

Varias constantes están disponibles para extraer los atributos
correspondientes retornados por algunos métodos.

+---------------------------+---------------------------------+
| Mascara de bits           | Significado                     |
|===========================|=================================|
| curses.A_ATTRIBUTES       | Mascara de bits para extraer    |
## |                           | atributos                       |

| curses.A_CHARTEXT         | Mascara de bits para extraer un |
## |                           | caracter                        |

| curses.A_COLOR            | Mascara de bits para extraer    |
|                           | información de campo de pares   |
## |                           | de colores                      |

Las teclas se denominan constantes enteras con nombres que comienzan
con "KEY_". Las teclas exactas disponibles son dependientes del
sistema.

+---------------------------+----------------------------------------------+
| Clave constante           | Clave                                        |
|===========================|==============================================|
## | curses.KEY_MIN            | Valor mínimo de la clave                     |

## | curses.KEY_BREAK          | Clave rota (no confiable)                    |

## | curses.KEY_DOWN           | Flecha hacia abajo                           |

## | curses.KEY_UP             | Flecha hacia arriba                          |

## | curses.KEY_LEFT           | Flecha hacia la izquierda                    |

## | curses.KEY_RIGHT          | Flecha hacia la derecha                      |

| curses.KEY_HOME           | Tecla de inicio (flecha hacia arriba +       |
## |                           | flecha hacia la izquierda)                   |

## | curses.KEY_BACKSPACE      | Retroceso (no confiable)                     |

| curses.KEY_F0             | Teclas de función. Más de 64 teclas de       |
## |                           | función son soportadas.                      |

## | curses.KEY_Fn             | Valor de tecla de función *n*                |

## | curses.KEY_DL             | Borrar línea                                 |

## | curses.KEY_IL             | Inserte línea                                |

## | curses.KEY_DC             | Borrar caracter                              |

| curses.KEY_IC             | Insertar carácter o ingresara al modo de     |
## |                           | inserción                                    |

## | curses.KEY_EIC            | Salir del modo de inserción de caracteres    |

## | curses.KEY_CLEAR          | Limpiar pantalla                             |

## | curses.KEY_EOS            | Limpiar al final de pantalla                 |

## | curses.KEY_EOL            | Limpiar al final de la línea                 |

## | curses.KEY_SF             | Desplazar una línea hacia adelante           |

## | curses.KEY_SR             | Desplazar una línea hacia atrás (reversa)    |

## | curses.KEY_NPAGE          | Página siguiente                             |

## | curses.KEY_PPAGE          | Página anterior                              |

## | curses.KEY_STAB           | Establecer pestaña                           |

## | curses.KEY_CTAB           | Limpiar pestaña                              |

## | curses.KEY_CATAB          | Limpiar todas las pestañas                   |

## | curses.KEY_ENTER          | Ingresar o enviar (no confiable)             |

## | curses.KEY_SRESET         | Reinicio suave (parcial) (no confiable)      |

## | curses.KEY_RESET          | Reinicio o reinicio fuerte (no confiable)    |

## | curses.KEY_PRINT          | Imprimir                                     |

## | curses.KEY_LL             | Inicio abajo o abajo (abajo a la izquierda)  |

## | curses.KEY_A1             | Superior izquierda del teclado               |

## | curses.KEY_A3             | Superior derecha de el teclado               |

## | curses.KEY_B2             | Centro del teclado                           |

## | curses.KEY_C1             | Inferior izquierdo del teclado               |

## | curses.KEY_C3             | Inferior derecho del teclado                 |

## | curses.KEY_BTAB           | Pestaña trasera                              |

## | curses.KEY_BEG            | Mendigar (Comienzo)                          |

## | curses.KEY_CANCEL         | Cancelar                                     |

## | curses.KEY_CLOSE          | Cerrar                                       |

## | curses.KEY_COMMAND        | Cmd (Comando)                                |

## | curses.KEY_COPY           | Copiar                                       |

## | curses.KEY_CREATE         | Crear                                        |

## | curses.KEY_END            | Final                                        |

## | curses.KEY_EXIT           | Salir                                        |

## | curses.KEY_FIND           | Encontrar                                    |

## | curses.KEY_HELP           | Ayudar                                       |

## | curses.KEY_MARK           | Marca                                        |

## | curses.KEY_MESSAGE        | Mensaje                                      |

## | curses.KEY_MOVE           | Mover                                        |

## | curses.KEY_NEXT           | Siguiente                                    |

## | curses.KEY_OPEN           | Abrir                                        |

## | curses.KEY_OPTIONS        | Opciones                                     |

## | curses.KEY_PREVIOUS       | Anterior                                     |

## | curses.KEY_REDO           | Rehacer                                      |

## | curses.KEY_REFERENCE      | Referencia                                   |

## | curses.KEY_REFRESH        | Refrescar                                    |

## | curses.KEY_REPLACE        | Re-emplazar                                  |

## | curses.KEY_RESTART        | Re-iniciar                                   |

## | curses.KEY_RESUME         | Resumir                                      |

## | curses.KEY_SAVE           | Guardar                                      |

## | curses.KEY_SBEG           | Mendicidad desplazada (comienzo)             |

## | curses.KEY_SCANCEL        | Cancelar cambiado                            |

## | curses.KEY_SCOMMAND       | Comando cambiado                             |

## | curses.KEY_SCOPY          | Copiado cambiado                             |

## | curses.KEY_SCREATE        | Crear con desplazamiento                     |

## | curses.KEY_SDC            | Borrar carácter desplazado                   |

## | curses.KEY_SDL            | Borrar línea desplazada                      |

## | curses.KEY_SELECT         | Seleccionar                                  |

## | curses.KEY_SEND           | Final desplazado                             |

## | curses.KEY_SEOL           | Limpiar línea desplazada                     |

## | curses.KEY_SEXIT          | Salida desplazada                            |

## | curses.KEY_SFIND          | Búsqueda desplazada                          |

## | curses.KEY_SHELP          | Ayuda desplazada                             |

## | curses.KEY_SHOME          | Inicio cambiado                              |

## | curses.KEY_SIC            | Entrada cambiada                             |

## | curses.KEY_SLEFT          | Flecha hacia la izquierda desplazada         |

## | curses.KEY_SMESSAGE       | Mensaje cambiado                             |

## | curses.KEY_SMOVE          | Movimiento desplazado                        |

## | curses.KEY_SNEXT          | Siguiente desplazado                         |

## | curses.KEY_SOPTIONS       | Opciones cambiadas                           |

## | curses.KEY_SPREVIOUS      | Anterior cambiado                            |

## | curses.KEY_SPRINT         | Imprimir desplazado                          |

## | curses.KEY_SREDO          | Rehacer cambiado                             |

## | curses.KEY_SREPLACE       | Re-emplazo cambiado                          |

## | curses.KEY_SRIGHT         | Flecha hacia la derecha cambiada             |

## | curses.KEY_SRSUME         | Resumen cambiado                             |

## | curses.KEY_SSAVE          | Guardar desplazado                           |

## | curses.KEY_SSUSPEND       | Suspender cambiado                           |

## | curses.KEY_SUNDO          | Deshacer desplazado                          |

## | curses.KEY_SUSPEND        | Suspender                                    |

## | curses.KEY_UNDO           | Deshacer                                     |

## | curses.KEY_MOUSE          | Evento del ratón ha ocurrido                 |

## | curses.KEY_RESIZE         | Evento de cambio de tamaño del terminal      |

## | curses.KEY_MAX            | Valor máximo de clave                        |

On VT100s and their software emulations, such as X terminal emulators,
there are normally at least four function keys ("KEY_F1", "KEY_F2",
"KEY_F3", "KEY_F4") available, and the arrow keys mapped to "KEY_UP",
"KEY_DOWN", "KEY_LEFT" and "KEY_RIGHT" in the obvious way.  If your
machine has a PC keyboard, it is safe to expect arrow keys and twelve
function keys (older PC keyboards may have only ten function keys);
also, the following keypad mappings are standard:

+--------------------+-------------+
| Tecla              | Constante   |
|====================|=============|
## | "Insert"           | KEY_IC      |

## | "Delete"           | KEY_DC      |

## | "Home"             | KEY_HOME    |

## | "End"              | KEY_END     |

## | "Page Up"          | KEY_PPAGE   |

## | "Page Down"        | KEY_NPAGE   |

La siguiente tabla lista los caracteres desde el conjunto alterno de
caracteres.  Estos son heredados desde el terminal VT100, y
generalmente estará disponible en emuladores de software tales como
terminales X.  Cuando no hay gráficos disponibles, *curses* cae en una
aproximación cruda de ASCII imprimibles.

Nota:

  Estos están disponibles solamente después de que "initscr()" ha sido
  llamada.

+--------------------------+--------------------------------------------+
| Código ACS               | Significado                                |
|==========================|============================================|
## | curses.ACS_BBSS          | alternate name for upper-right corner      |

## | curses.ACS_BLOCK         | bloque cuadrado sólido                     |

## | curses.ACS_BOARD         | tablero de cuadrados                       |

## | curses.ACS_BSBS          | nombre alternativo para línea horizontal   |

## | curses.ACS_BSSB          | alternate name for upper-left corner       |

| curses.ACS_BSSS          | nombre alternativo para el soporte         |
## |                          | superior                                   |

## | curses.ACS_BTEE          | soporte inferior                           |

## | curses.ACS_BULLET        | bala                                       |

## | curses.ACS_CKBOARD       | tablero inspector (punteado)               |

## | curses.ACS_DARROW        | flecha punteada hacia abajo                |

## | curses.ACS_DEGREE        | símbolo de grado                           |

## | curses.ACS_DIAMOND       | diamante                                   |

## | curses.ACS_GEQUAL        | mayor que o igual a                        |

## | curses.ACS_HLINE         | línea horizontal                           |

## | curses.ACS_LANTERN       | símbolo de la linterna                     |

## | curses.ACS_LARROW        | flecha izquierda                           |

## | curses.ACS_LEQUAL        | menor que o igual a                        |

## | curses.ACS_LLCORNER      | lower-left corner                          |

## | curses.ACS_LRCORNER      | lower-right corner                         |

## | curses.ACS_LTEE          | soporte izquierdo                          |

## | curses.ACS_NEQUAL        | signo no igual                             |

## | curses.ACS_PI            | letra pi                                   |

## | curses.ACS_PLMINUS       | signo más o menos                          |

## | curses.ACS_PLUS          | gran signo más                             |

## | curses.ACS_RARROW        | flecha hacia la derecha                    |

## | curses.ACS_RTEE          | soporte derecho                            |

## | curses.ACS_S1            | escanear línea 1                           |

## | curses.ACS_S3            | escanear línea 3                           |

## | curses.ACS_S7            | escanear línea 7                           |

## | curses.ACS_S9            | escanear línea 9                           |

## | curses.ACS_SBBS          | alternate name for lower-right corner      |

## | curses.ACS_SBSB          | nombre alterno para la línea vertical      |

## | curses.ACS_SBSS          | nombre alterno para el soporte derecho     |

## | curses.ACS_SSBB          | alternate name for lower-left corner       |

## | curses.ACS_SSBS          | nombre alterno para el soporte inferior    |

## | curses.ACS_SSSB          | nombre alterno para el soporte izquierdo   |

| curses.ACS_SSSS          | nombre alterno para *crossover* o un gran  |
## |                          | más                                        |

## | curses.ACS_STERLING      | libra esterlina                            |

## | curses.ACS_TTEE          | soporte superior                           |

## | curses.ACS_UARROW        | flecha hacia arriba                        |

## | curses.ACS_ULCORNER      | upper-left corner                          |

## | curses.ACS_URCORNER      | upper-right corner                         |

## | curses.ACS_VLINE         | línea vertical                             |

The following table lists mouse button constants used by "getmouse()":

+------------------------------------+-----------------------------------------------+
| Mouse button constant              | Significado                                   |
|====================================|===============================================|
## | curses.BUTTONn_PRESSED             | Mouse button *n* pressed                      |

## | curses.BUTTONn_RELEASED            | Mouse button *n* released                     |

## | curses.BUTTONn_CLICKED             | Mouse button *n* clicked                      |

## | curses.BUTTONn_DOUBLE_CLICKED      | Mouse button *n* double clicked               |

## | curses.BUTTONn_TRIPLE_CLICKED      | Mouse button *n* triple clicked               |

## | curses.BUTTON_SHIFT                | Shift was down during button state change     |

## | curses.BUTTON_CTRL                 | Control was down during button state change   |

## | curses.BUTTON_ALT                  | Alt was down during button state change       |

Distinto en la versión 3.10: Las constantes "BUTTON5_*" ahora están
expuestas si son proporcionadas por la biblioteca curses subyacente.

La siguiente tabla lista los colores pre-definidos:

+---------------------------+------------------------------+
| Constante                 | Color                        |
|===========================|==============================|
## | curses.COLOR_BLACK        | Negro                        |

## | curses.COLOR_BLUE         | Azul                         |

## | curses.COLOR_CYAN         | Cian (azul verdoso claro)    |

## | curses.COLOR_GREEN        | Verde                        |

## | curses.COLOR_MAGENTA      | Magenta (rojo violáceo)      |

## | curses.COLOR_RED          | Rojo                         |

## | curses.COLOR_WHITE        | Blanco                       |

## | curses.COLOR_YELLOW       | Amarillo                     |

# "curses.textpad" --- Text input widget for curses programs

The "curses.textpad" module provides a "Textbox" class that handles
elementary text editing in a curses window, supporting a set of
keybindings resembling those of Emacs (thus, also of Netscape
Navigator, BBedit 6.x, FrameMaker, and many other programs).  The
module also provides a rectangle-drawing function useful for framing
text boxes or for other purposes.

The module "curses.textpad" defines the following function:

curses.textpad.rectangle(win, uly, ulx, lry, lrx)

   Draw a rectangle.  The first argument must be a window object; the
   remaining arguments are coordinates relative to that window.  The
   second and third arguments are the y and x coordinates of the
   upper-left corner of the rectangle to be drawn; the fourth and
   fifth arguments are the y and x coordinates of the lower-right
   corner. The rectangle will be drawn using VT100/IBM PC forms
   characters on terminals that make this possible (including xterm
   and most other software terminal emulators).  Otherwise it will be
   drawn with ASCII  dashes, vertical bars, and plus signs.

## Objeto de caja de texto

Tú puedes instanciar un objeto "Textbox" como sigue:

class curses.textpad.Textbox(win, insert_mode=False)

   Return a textbox widget object.  The *win* argument should be a
   curses window object in which the textbox is to be contained.  If
   *insert_mode* is true, the textbox inserts typed characters,
   shifting existing text to the right, rather than overwriting it.
   The edit cursor of the textbox is initially located at the upper-
   left corner of the containing window, with coordinates "(0, 0)".
   The instance's "stripspaces" flag is initially on.

   Objeto "Textbox" tiene los siguientes métodos:

   edit(validate=None)

      This is the entry point you will normally use.  It accepts
      editing keystrokes until one of the termination keystrokes is
      entered.  If *validate* is supplied, it must be a function.  It
      will be called for each keystroke entered with the keystroke as
      a parameter; command dispatch is done on the result.  If it
      returns a false value, the keystroke is ignored.  This method
      returns the window contents as a string; whether blanks in the
      window are included is affected by the "stripspaces" attribute.

   do_command(ch)

      Process a single command keystroke.  Returns "1" to continue
      editing, or "0" if a termination keystroke was processed.  Here
      are the supported special keystrokes:

      +--------------------+---------------------------------------------+
      | Pulsación de tecla | Acción                                      |
      |====================|=============================================|
      | "Control"-"A"      | Ve al borde izquierdo de la ventana.        |
      +--------------------+---------------------------------------------+
      | "Control"-"B"      | Cursor hacia la izquierda, pasando a la     |
      |                    | línea anterior si corresponde.              |
      +--------------------+---------------------------------------------+
      | "Control"-"D"      | Borra el carácter bajo el cursor.           |
      +--------------------+---------------------------------------------+
      | "Control"-"E"      | Ve al borde derecho (quita los espacios) o  |
      |                    | al final de línea (eliminar los espacios).  |
      +--------------------+---------------------------------------------+
      | "Control"-"F"      | Cursor hacia la derecha, pasando a la línea |
      |                    | siguiente cuando corresponda.               |
      +--------------------+---------------------------------------------+
      | "Control"-"G"      | Terminar, retornando el contenido de la     |
      |                    | ventana.                                    |
      +--------------------+---------------------------------------------+
      | "Control"-"H"      | Eliminar carácter al revés.                 |
      +--------------------+---------------------------------------------+
      | "Control"-"J"      | Terminate if the window is 1 line,          |
      |                    | otherwise move to the start of the next     |
      |                    | line.                                       |
      +--------------------+---------------------------------------------+
      | "Control"-"K"      | Si la línea es blanca bórrela, en caso      |
      |                    | contrario, limpie hasta el final de línea.  |
      +--------------------+---------------------------------------------+
      | "Control"-"L"      | Refrescar la pantalla.                      |
      +--------------------+---------------------------------------------+
      | "Control"-"N"      | Cursor hacia abajo; mueve hacia abajo una   |
      |                    | línea.                                      |
      +--------------------+---------------------------------------------+
      | "Control"-"O"      | Inserte una línea en blanco en la posición  |
      |                    | del cursor.                                 |
      +--------------------+---------------------------------------------+
      | "Control"-"P"      | Cursor hacia arriba; mueve hacia arriba una |
      |                    | línea.                                      |
      +--------------------+---------------------------------------------+

      Las operaciones de movimiento no hacen nada si el cursor está en
      un borde donde el movimiento no es posible. Los siguientes
      sinónimos están apoyados siempre que sea posible:

      +----------------------------------+--------------------+
      | Constante                        | Pulsación de tecla |
      |==================================|====================|
      | "KEY_LEFT"                       | "Control"-"B"      |
      +----------------------------------+--------------------+
      | "KEY_RIGHT"                      | "Control"-"F"      |
      +----------------------------------+--------------------+
      | "KEY_UP"                         | "Control"-"P"      |
      +----------------------------------+--------------------+
      | "KEY_DOWN"                       | "Control"-"N"      |
      +----------------------------------+--------------------+
      | "KEY_BACKSPACE"                  | "Control"-"h"      |
      +----------------------------------+--------------------+

      Todas las otras pulsaciones de teclas están tratadas como un
      comando para insertar el carácter dado y muévase a la derecha
      (con ajuste en la línea).

   gather()

      Retorne el contenido de la ventana como una cadena de texto; si
      se incluyen espacios en blanco en la ventana se ve afectado por
      el miembro "stripspaces".

   stripspaces

      Este atributo es una bandera que controla la interpretación de
      los espacios en blanco en la ventana.  Cuando está encendido,
      los espacios en blanco al final en cada línea son ignorados;
      cualquier movimiento del cursor que lo coloque en un espacio en
      blanco final va hasta el final de esa línea, y los espacios en
      blanco finales son despejados cuando se recopila el contenido de
      la ventana.
