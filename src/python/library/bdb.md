---
title: '"bdb" --- Debugger framework'
source_url: https://docs.python.org/es/3
source_path: library/bdb.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1830
---

# "bdb" --- Debugger framework

**Source code:** Lib/bdb.py

======================================================================

The "bdb" module handles basic debugger functions, like setting
breakpoints or managing execution via the debugger.

La siguiente excepción es definida:

exception bdb.BdbQuit

   Excepción lanzada por la clase "Bdb" al salir del depurador.

The "bdb" module also defines two classes:

class bdb.Breakpoint(self, file, line, temporary=False, cond=None, funcname=None)

   Esta clase implementa puntos de interrupción temporales,
   permitiendo ignorar recuentos, desactivar y (re-)activar puntos de
   interrupción y definir condiciones de interrupción para los mismos.

   Los puntos de interrupción se indexan numéricamente mediante una
   lista llamada "bpbynumber" y por pares "(archivo, linea)" mediante
   "bplist". En el primer caso se apunta a una única instancia de
   "Breakpoint". En el segundo caso se apunta a una lista de tales
   instancias, ya que puede haber más de un punto de interrupción por
   línea.

   Al crear un punto de interrupción, el "nombre del archivo" asociado
   debe estar en su forma canónica. Si se define un "funcname", se
   contará un "hit" de punto de interrupción cuando se ejecute la
   primera línea de esa función. Un punto de interrupción
   "condicional" siempre cuenta un "hit".

   Las instancias de la clase "Breakpoint" tienen los siguientes
   métodos:

   deleteMe()

      Elimina el punto de interrupción de la lista asociada a un
      archivo/línea. Si es el último punto de interrupción en esa
      posición, también borra la entrada correspondiente del
      archivo/línea correspondiente.

   enable()

      Marca el punto de interrupción como habilitado.

   disable()

      Marca el punto de interrupción como deshabilitado.

   bpformat()

      Retorna una cadena de caracteres que contiene toda la
      información sobre el punto de interrupción, apropiadamente
      formateada:

      * El número del punto de interrupción.

      * Estado temporal (del o keep)

      * Posición del archivo/línea.

      * Condición de interrupción.

      * Número de veces para ignorar.

      * Número de veces alcanzado.

      Added in version 3.2.

   bpprint(out=None)

      Imprime la salida de "bpformat()" en el archivo *out*, o en la
      salida estándar si es "None".

   Las instancias de la clase "Breakpoint" tienen los siguientes
   atributos:

   file

      Nombre del archivo de la clase "Breakpoint".

   line

      Número de línea de la clase "Breakpoint" dentro de "file".

   temporary

      "True" if a "Breakpoint" at (file, line) is temporary.

   cond

      Condición para evaluar una clase "Breakpoint" en (file, line).

   funcname

      Nombre de la función que define si se alcanza un "Breakpoint" al
      ingresar a la función.

   enabled

      "True" if "Breakpoint" is enabled.

   bpbynumber

      Índice numérico para una sola instancia de un "Breakpoint".

   bplist

      Diccionario de instancias "Breakpoint" indexadas por tuplas
      ("file", "line").

   ignore

      Número de veces para ignorar un "Breakpoint".

   hits

      Recuento del número de veces que se alcanzó un "Breakpoint".

class bdb.Bdb(skip=None, backend='settrace')

   La clase "Bdb" actúa como clase base del depurador genérico de
   Python.

   Esta clase se encarga de los detalles de la funcionalidad de
   seguimiento; una clase derivada debería encargarse de implementar
   la interacción con el usuario. Un ejemplo es la clase de depuración
   estándar ("pdb.Pdb").

   El argumento *skip*, si se proporciona, debe ser un iterable con
   patrones de nombre de archivo, al estilo del módulo glob. El
   depurador no entrará en aquellos marcos de ejecución que se
   originen en un módulo que coincida con uno de estos patrones. Para
   determinar si un marco de ejecución se origina en un módulo
   determinado, se hace uso de "__name__" en las variables globales
   del marco de ejecución dado.

   The *backend* argument specifies the backend to use for "Bdb". It
   can be either "'settrace'" or "'monitoring'". "'settrace'" uses
   "sys.settrace()" which has the best backward compatibility. The
   "'monitoring'" backend uses the new "sys.monitoring" that was
   introduced in Python 3.12, which can be much more efficient because
   it can disable unused events. We are trying to keep the exact
   interfaces for both backends, but there are some differences. The
   debugger developers are encouraged to use the "'monitoring'"
   backend to achieve better performance.

   Distinto en la versión 3.1: Added the *skip* parameter.

   Distinto en la versión 3.14: Added the *backend* parameter.

   Los siguientes métodos de la clase "Bdb" normalmente no necesitan
   ser redefinidos.

   canonic(filename)

      Retorna la forma canónica de *filename*.

      Para nombres de archivos reales, la forma canónica es una "ruta
      absoluta" "normalizada entre mayúsculas y minúsculas" que
      depende del sistema operativo. Un *filename* con corchetes
      angulares, como ""<stdin>"" generado en modo interactivo, se
      retorna sin cambios.

   start_trace(self)

      Start tracing. For "'settrace'" backend, this method is
      equivalent to "sys.settrace(self.trace_dispatch)"

      Added in version 3.14.

   stop_trace(self)

      Stop tracing. For "'settrace'" backend, this method is
      equivalent to "sys.settrace(None)"

      Added in version 3.14.

   reset()

      Set the "botframe", "stopframe", "returnframe" and "quitting"
      attributes with values ready to start debugging.

   trace_dispatch(frame, event, arg)

      Esta función se instala como función de seguimiento de los
      marcos de ejecución depurados. Su valor de retorno es la nueva
      función de seguimiento a usar (en la mayoría de los casos, ella
      misma).

      La implementación predeterminada decide cómo despachar un marco
      de ejecución, dependiendo del tipo de evento (pasado como una
      cadena) que está a punto de ejecutarse. *event* puede tomar uno
      de los siguientes valores:

      * ""line"": Se va a ejecutar una nueva línea de código.

      * ""call"": Está a punto de llamarse a una función o se ha
        entrado en otro bloque de código.

      * ""return"": Una función u otro bloque de código está a punto
        de retornar.

      * ""exception"": Ha ocurrido una excepción.

      * ""c_call"": Una función de C está a punto de llamarse .

      * ""c_return"": Una función de C ha retornado.

      * ""c_exception"": Una función de C ha lanzado una excepción.

      Para los eventos de Python, son llamadas funciones
      especializadas (ver más abajo). En cambio, para los eventos de C
      no se realiza ninguna acción.

      El parámetro *arg* depende del evento previo.

      Consulta la documentación de "sys.settrace()" para obtener más
      información sobre la función de seguimiento. Para obtener más
      información sobre los objetos código y los objetos marco
      consulte Jerarquía de tipos estándar.

   dispatch_line(frame)

      If the debugger should stop on the current line, invoke the
      "user_line()" method (which should be overridden in subclasses).
      Raise a "BdbQuit" exception if the "quitting" flag is set (which
      can be set from "user_line()").  Return a reference to the
      "trace_dispatch()" method for further tracing in that scope.

   dispatch_call(frame, arg)

      If the debugger should stop on this function call, invoke the
      "user_call()" method (which should be overridden in subclasses).
      Raise a "BdbQuit" exception if the "quitting" flag is set (which
      can be set from "user_call()").  Return a reference to the
      "trace_dispatch()" method for further tracing in that scope.

   dispatch_return(frame, arg)

      If the debugger should stop on this function return, invoke the
      "user_return()" method (which should be overridden in
      subclasses). Raise a "BdbQuit" exception if the "quitting" flag
      is set (which can be set from "user_return()").  Return a
      reference to the "trace_dispatch()" method for further tracing
      in that scope.

   dispatch_exception(frame, arg)

      If the debugger should stop at this exception, invokes the
      "user_exception()" method (which should be overridden in
      subclasses). Raise a "BdbQuit" exception if the "quitting" flag
      is set (which can be set from "user_exception()").  Return a
      reference to the "trace_dispatch()" method for further tracing
      in that scope.

   Las clases derivadas normalmente no necesitan redefinir los
   siguientes métodos, pero pueden hacerlo si necesitan redefinir la
   definición de parada y los puntos de interrupción.

   is_skipped_module(module_name)

      Return "True" if *module_name* matches any skip pattern.

   stop_here(frame)

      Return "True" if *frame* is below the starting frame in the
      stack.

   break_here(frame)

      Return "True" if there is an effective breakpoint for this line.

      Comprueba si existe un punto de interrupción de línea o de una
      función y si está en vigor. Elimina puntos de interrupción
      temporales basados en la información de "effective()".

   break_anywhere(frame)

      Return "True" if any breakpoint exists for *frame*'s filename.

   Las clases derivadas deben redefinir estos métodos para adquirir el
   control sobre las operaciones de depuración.

   user_call(frame, argument_list)

      Se llama desde "dispatch_call()" si una interrupción puede
      detenerse dentro de la función llamada.

      *argument_list* is not used anymore and will always be "None".
      The argument is kept for backwards compatibility.

   user_line(frame)

      Se llama desde "dispatch_line()" cuando "stop_here()" o
      "break_here()" retornan "True".

   user_return(frame, return_value)

      Se llama desde "dispatch_return()" cuando "stop_here()" retorna
      "True".

   user_exception(frame, exc_info)

      Se llama desde "dispatch_exception()" cuando "stop_here()"
      retorna "True".

   do_clear(arg)

      Maneja cómo un punto de interrupción debe ser eliminado cuando
      es temporal.

      Este método debe ser implementado por las clases derivadas.

   Las clases derivadas y los clientes pueden llamar a los siguientes
   métodos para influir en el estado de transición.

   set_step()

      Se detiene después de una línea de código.

   set_next(frame)

      Se detiene en la siguiente línea del marco de ejecución dado o
      en la de uno inferior.

   set_return(frame)

      Se detiene cuando se retorna desde el marco de ejecución dado.

   set_until(frame, lineno=None)

      Se detiene cuando se alcanza la línea con el *lineno* mayor que
      el actual o al retornar desde el marco actual.

   set_trace([frame])

      Inicia la depuración desde el marco de ejecución *frame*. Si
      *frame* no se especifica, la depuración se inicia desde el marco
      de ejecución que produce la llamada.

      Distinto en la versión 3.13: "set_trace()" will enter the
      debugger immediately, rather than on the next line of code to be
      executed.

   set_continue()

      Se detiene solo en los puntos de interrupción o cuando haya
      terminado. Si no hay puntos de interrupción, se configura la
      función de seguimiento del sistema en "None".

   set_quit()

      Set the "quitting" attribute to "True".  This raises "BdbQuit"
      in the next call to one of the "dispatch_*()" methods.

   Las clases derivadas y los clientes pueden llamar a los siguientes
   métodos para manipular los puntos de interrupción. Estos métodos
   retornan una cadena de caracteres que contiene un mensaje de error
   si algo fue mal, o "None" si todo fue correctamente.

   set_break(filename, lineno, temporary=False, cond=None, funcname=None)

      Establece un nuevo punto de interrupción. Si la línea en la
      posición *lineno* no existe en el archivo con nombre *filename*
      pasado como argumento, se retorna un mensaje de error.
      *filename* debe estar en su forma canónica, tal como se describe
      en el método "canonic()".

   clear_break(filename, lineno)

      Elimina los puntos de interrupción en *filename* y *lineno*. Si
      no se estableció ninguno, se retorna un mensaje de error.

   clear_bpbynumber(arg)

      Elimina el punto de interrupción que tiene el índice *arg* en
      "Breakpoint.bpbynumber". Si *arg* no es un valor numérico o es
      un indice fuera de rango, se retorna un mensaje de error.

   clear_all_file_breaks(filename)

      Elimina todos los puntos de interrupción en *filename*. Si no se
      estableció ninguno, se retorna un mensaje de error.

   clear_all_breaks()

      Elimina todos los puntos de interrupción. Si no se estableció
      ninguno, se retorna un mensaje de error.

   get_bpbynumber(arg)

      Retorna un punto de interrupción especificado por el número
      dado. Si *arg* es una cadena de caracteres, será convertida en
      un número. Si *arg* es una cadena no numérica, o el punto de
      interrupción dado nunca existió o ya ha sido eliminado, se lanza
      una excepción "ValueError".

      Added in version 3.2.

   get_break(filename, lineno)

      Return "True" if there is a breakpoint for *lineno* in
      *filename*.

   get_breaks(filename, lineno)

      Retorna todos los puntos de interrupción en la línea número
      *lineno* del archivo *filename*, o una lista vacía si no se ha
      establecido ninguno.

   get_file_breaks(filename)

      Retorna todos los puntos de interrupción en el archivo
      *filename*, o una lista vacía si no hay ninguno establecido.

   get_all_breaks()

      Retorna todos los puntos de interrupción establecidos.

   Derived classes and clients can call the following methods to
   disable and restart events to achieve better performance. These
   methods only work when using the "'monitoring'" backend.

   disable_current_event()

      Disable the current event until the next time "restart_events()"
      is called. This is helpful when the debugger is not interested
      in the current line.

      Added in version 3.14.

   restart_events()

      Restart all the disabled events. This function is automatically
      called in "dispatch_*" methods after "user_*" methods are
      called. If the "dispatch_*" methods are not overridden, the
      disabled events will be restarted after each user interaction.

      Added in version 3.14.

   Las clases derivadas y clientes pueden llamar los siguientes
   métodos para obtener una estructura de datos que representa un
   seguimiento de pila.

   get_stack(f, t)

      Retorna una lista de tuplas (frame, lineno) en un seguimiento de
      pila y un tamaño.

      El marco llamado más recientemente es el último en la lista. El
      tamaño es el número de marcos por debajo del marco en el que se
      invocó el depurador.

   format_stack_entry(frame_lineno, lprefix=': ')

      Retorna una cadena de caracteres con información sobre una
      entrada de pila, identificada por una tupla de la forma "(frame,
      lineno)". La cadena de caracteres que retorna contiene:

      * El nombre de archivo canónico que contiene el marco de
        ejecución.

      * El nombre de la función o ""<lambda>"".

      * Los argumentos de entrada.

      * El valor de retorno.

      * La linea de código (si existe).

   Los dos métodos descritos a continuación pueden ser llamados por
   los clientes para usar un depurador que se encargue de depurar un
   *statement*, proporcionado como una cadena de caracteres.

   run(cmd, globals=None, locals=None)

      Debug a statement executed via the "exec()" function.  *globals*
      defaults to "__main__.__dict__", *locals* defaults to *globals*.

   runeval(expr, globals=None, locals=None)

      Depura una expresión ejecutada mediante la función "eval()".
      *globals* y *locals* tienen el mismo significado que en "run()".

   runctx(cmd, globals, locals)

      Definido solo por compatibilidad con versiones anteriores. Llama
      al método "run()".

   runcall(func, /, *args, **kwds)

      Depura una única llamada a función y retorna su resultado.

Por último, el módulo también define las siguientes funciones:

bdb.checkfuncname(b, frame)

   Return "True" if we should break here, depending on the way the
   "Breakpoint" *b* was set.

   Si se estableció a través del número de línea, comprueba si
   "b.line" es el mismo que el de *frame*. Si el punto de interrupción
   se estableció a través del "nombre de la función", se tiene que
   comprobar que estamos en el *frame* correcto (la función correcta)
   y si se está en su primera línea ejecutable.

bdb.effective(file, line, frame)

   Retorna "(active breakpoint, delete temporary flag)" o "(None,
   None)" como el punto de interrupción para actuar.

   The *active breakpoint* is the first entry in "bplist" for the
   ("file", "line") (which must exist) that is "enabled", for which
   "checkfuncname()" is true, and that has neither a false "condition"
   nor positive "ignore" count.  The *flag*, meaning that a temporary
   breakpoint should be deleted, is "False" only when the "cond"
   cannot be evaluated (in which case, "ignore" count is ignored).

   If no such entry exists, then "(None, None)" is returned.

bdb.set_trace()

   Inicia la depuración usando una instancia de "Bdb", partiendo desde
   el marco de ejecución que realiza la llamada.
