---
title: '"_thread" --- Low-level threading API'
source_url: https://docs.python.org/es/3
source_path: library/_thread.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1480
---

# "_thread" --- Low-level threading API

======================================================================

Este módulo ofrece primitivas de bajo nivel para trabajar con
múltiples *threads* o hilos (también llamados *light-weight processes*
o *tasks*) -- múltiples hilos de control compartiendo su espacio de
datos global. Para sincronizar, provee "candados" simples (también
llamados  *mutexes* o *binary semaphores*). El módulo "threading"
provee una API de manejo de hilos más fácil de usar y de más alto
nivel, construida sobre este módulo.

Distinto en la versión 3.7: Este módulo solía ser opcional, pero ahora
está siempre disponible.

Este módulo define las siguientes constantes y funciones:

exception _thread.error

   Lanzado ante errores específicos de un hilo.

   Distinto en la versión 3.3: Ahora es un sinónimo de la excepción
   incorporada "RuntimeError".

_thread.start_new_thread(function, args[, kwargs])

   Inicia un nuevo hilo y retorna su identificador. El hilo ejecuta la
   función *function* con la lista de argumentos *args* (que debe ser
   una tupla). El argumento opcional *kwargs* especifica un
   diccionario de argumentos por palabras clave.

   Cuando la función retorna, el hilo finaliza silenciosamente.

   Cuando la función termina con una excepción no gestionada, se
   invoca a "sys.unraisablehook()" para que gestione la excepción. El
   atributo *object* del argumento gancho (*hook*), es *function*. Por
   defecto, se muestra un seguimiento de pila y luego el hilo sale
   (pero los otros hilos continúan funcionando).

   Cuando la función lanza una excepción "SystemExit", se ignora
   silenciosamente.

   Lanza un evento de auditoría "_thread.start_new_thread" con los
   argumentos "function", "args", "kwargs".

   Distinto en la versión 3.8: Ahora se utiliza "sys.unraisablehook()"
   para gestionar las excepciones no gestionadas.

_thread.interrupt_main(signum=signal.SIGINT, /)

   Simular el efecto de una señal que llega al hilo principal. Un hilo
   puede usar esta función para interrumpir el hilo principal, aunque
   no hay garantías de que la interrupción ocurrirá inmediatamente.

   Si es dada, *signum* es el número de la señal a simular. Si
   *signum* no es dada, "signal.SIGINT" es simulado.

   Si la señal dada no es manejada por Python (se estableció en
   "signal.SIG_DFL" o "signal.SIG_IGN"), esta función no hace nada.

   Distinto en la versión 3.10: Se agrega el argumento *signum* para
   personalizar el número de señal.

   Nota:

     Esto no emite la señal correspondiente, sino que programa una
     llamada al controlador asociado (si existe). Si realmente se
     quiere emitir la señal, se utiliza "signal.raise_signal()".

_thread.exit()

   Lanza la excepción "SystemExit". Cuando no es gestionada, causa que
   el hilo salga silenciosamente.

_thread.allocate_lock()

   Retorna un nuevo objeto candado (*lock object*). Los métodos de los
   candados se describen más abajo. El candado está abierto al inicio.

_thread.get_ident()

   Retorna el 'identificador de hilo' (*thread identifier*) del hilo
   actual. Es un entero distinto de cero. Su valor no tiene un
   significado directo, tiene la intención de ser utilizada como una
   *cookie* mágica para, por ejemplo, indexar un diccionario con datos
   específicos del hilo. Los identificadores de hilo pueden reciclarse
   cuando un hilo sale y otro se crea.

_thread.get_native_id()

   Retorna el ID de hilo nativo integral del hilo asignado por el
   kernel. Es un entero no-negativo. Su valor puede utilizarse para
   identificar inequívocamente este hilo en particular en todo el
   sistema (hasta que el hilo termine, luego de lo cual el valor puede
   ser reciclado por el Sistema Operativo).

   Availability: Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX,
   DragonFlyBSD, GNU/kFreeBSD.

   Added in version 3.8.

   Distinto en la versión 3.13: Added support for GNU/kFreeBSD.

_thread.stack_size([size])

   Retorna el tamaño de la pila del hilo (*thread stack*) utilizada al
   crear nuevos hilos. El argumento opcional *size* especifica el
   tamaño de la pila a utilizar en los hilos que se creen a
   continuación, y debe ser 0 (utiliza el valor por defecto de la
   plataforma o el configurado) o un entero positivo de al menos 32768
   (32KiB). Si *size* no se especifica, se utiliza 0. Si no está
   soportado el cambio del tamaño de pila del hilo, se lanza una
   excepción "RuntimeError". Si la pila especificada es inválida se
   lanza un "ValueError" y el tamaño de la pila no se modifica. 32KiB
   es actualmente el menor valor soportado para el tamaño de la pila,
   para garantizar suficiente espacio en la misma para que quepa el
   propio intérprete. Tenga en cuenta que alguna plataformas pueden
   tener restricciones particulares en los valores para el tamaño de
   la pila, como requerir un mínimo que supere los 32KiB, o requerir
   una asignación en múltiplos del tamaño de página de memoria del
   sistema. Es necesario consultar la documentación de la plataforma
   para mayor información (son habituales las páginas de 4KiB; usar
   múltiplos de 4096 para el tamaño de pila es la estrategia sugerida
   si no se cuenta con información más específica).

   Availability: Windows, pthreads.

   Plataformas Unix con soporte para hilos POSIX.

_thread.TIMEOUT_MAX

   El máximo valor permitido para el parámetro *timeout* de
   "Lock.acquire". Especificar un tiempo de espera (*timeout*) mayor
   que este valor lanzará una excepción "OverflowError".

   Added in version 3.2.

class _thread.LockType

   Este es el tipo de los objetos candado (*lock objects*).

   Los objetos candado (*lock objects*) tienen los siguientes métodos:

   acquire(blocking=True, timeout=-1)

      Sin ningún argumento opcional, este método adquiere el candado
      incondicionalmente, si es necesario esperando que éste sea
      liberado por otro hilo (solamente un hilo por vez puede adquirir
      un candado; para eso existen).

      If the *blocking* argument is present, the action depends on its
      value: if it is false, the lock is only acquired if it can be
      acquired immediately without waiting, while if it is true, the
      lock is acquired unconditionally as above.

      If the floating-point *timeout* argument is present and
      positive, it specifies the maximum wait time in seconds before
      returning.  A negative *timeout* argument specifies an unbounded
      wait.  You cannot specify a *timeout* if *blocking* is false.

      El valor de retorno es "True" si el candado (*lock*) se adquirió
      exitosamente, "False" de lo contrario.

      Distinto en la versión 3.2: El parámetro *timeout* es nuevo.

      Distinto en la versión 3.2: La adquisición de candados ahora
      puede ser interrumpida por señales en POSIX.

      Distinto en la versión 3.14: Lock acquires can now be
      interrupted by signals on Windows.

   release()

      Libera el candado. El candado debe haber sido adquirido
      previamente, pero no necesariamente por el mismo hilo.

   locked()

      Retorna el estado del candado: "True" si ha sido adquirido por
      algún hilo, "False" de lo contrario.

   Además de estos métodos, los objetos candado pueden ser utilizados
   mediante la declaración "with", por ejemplo:

      import _thread

      a_lock = _thread.allocate_lock()

      with a_lock:
          print("a_lock is locked while this executes")

**Salvedades:**

* Interrupts always go to the main thread (the "KeyboardInterrupt"
  exception will be received by that thread.)

* Invocar a "sys.exit()" o lanzar la excepción "SystemExit" equivale a
  invocar "_thread.exit()".

* Cuando el hilo principal sale, ¿sobreviven los otros hilos? Depende
  de cómo esté definido por el sistema. En la mayoría de los sistemas,
  los hilos se cierran inmediatamente (*killed*), sin ejecutar las
  cláusulas "try" ... "finally" o los destructores del objeto.
