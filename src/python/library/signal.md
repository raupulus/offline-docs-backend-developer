---
title: '"signal" --- Set handlers for asynchronous events'
source_url: https://docs.python.org/es/3
source_path: library/signal.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3790
---

# "signal" --- Set handlers for asynchronous events

**Código fuente:** Lib/signal.py

======================================================================

Este módulo proporciona mecanismos para usar gestores de señales en
Python.

## Reglas generales

La función "signal.signal()" permite definir gestores personalizados
que serán ejecutados cuando una señal es recibida. Un pequeño número
de gestores por defecto son instalados: "SIGPIPE" es ignorada (por lo
que los errores de escritura en tuberías y sockets se pueden informar
como excepciones ordinarias de Python) y "SIGINT" es trasladada en una
excepción "KeyboardInterrupt" si el proceso padre no lo ha cambiado.

El gestor para una señal en particular, una vez establecido, continua
instalado hasta que se resetea explícitamente (Python emula el estilo
de interfaz BSD independientemente de la implementación subyacente),
con la excepción del gestor para "SIGCHLD", que sigue la
implementación subyacente.

On WebAssembly platforms, signals are emulated and therefore behave
differently. Several functions and signals are not available on these
platforms.

### Ejecución de los gestores de señales de Python

A Python signal handler does not get executed inside the low-level (C)
signal handler.  Instead, the low-level signal handler sets a flag
which tells the *virtual machine* to execute the corresponding Python
signal handler at a later point (for example, at the next *bytecode*
instruction). This has consequences:

* Tiene poco sentido detectar errores sincrónicos como "SIGFPE" o
  "SIGSEGV" que son causados por una operación no válida en código C.
  Python retornará desde el gestor de señales a código C, que es
  probable que extienda la misma señal otra vez, ocasionando que
  Python se cuelgue aparentemente. Desde Python 3.3 en adelante,
  puedes usar el módulo "faulthandler" para reportar errores
  síncronos.

* Un cálculo de larga duración implementado exclusivamente en C (como
  una coincidencia de expresiones regulares en un gran cuerpo de
  texto) puede funcionar interrumpidamente durante una cantidad
  arbitraria de tiempo, independientemente de las señales recibidas.
  Los gestores de señales de Python serán llamados cuando el cálculo
  finalice.

* Si el gestor genera alguna excepción, será lanzada inesperadamente.
  Vea la nota abajo para discusión.

### Señales e hilos

Los gestores de señales de Python se ejecutan siempre en el hilo
principal de Python, incluso si la señal fue recibida desde otro hilo.
Esto significa que las señales no pueden ser usadas como un medio de
comunicación entre hilos. Puedes usar las primitivas de sincronización
desde el módulo "threading" en su lugar.

Además, solo el hilo principal puede configurar un nuevo gestor de
señal.

Advertencia:

  Synchronization primitives such as "threading.Lock" should not be
  used within signal handlers.  Doing so can lead to unexpected
  deadlocks.

## Contenidos del módulo

Distinto en la versión 3.5: Las constantes relacionadas con señal
(SIG*), gestor ("SIG_DFL", "SIG_IGN") y sigmask ("SIG_BLOCK",
"SIG_UNBLOCK", "SIG_SETMASK") enumeradas a continuación fueron
convertidas en "enums" ("Signals", "Handlers" y "Sigmasks",
respectivamente). Las funciones "getsignal()", "pthread_sigmask()",
"sigpending()" y "sigwait()" devuelven "enums" legibles por humanos
como objetos "Signals".

El módulo signal define tres enums:

class signal.Signals

   "enum.IntEnum" colección de constantes SIG* y colección de
   constantes CTRL_*.

   Added in version 3.5.

class signal.Handlers

   "enum.IntEnum" collection of the constants "SIG_DFL" and "SIG_IGN".

   Added in version 3.5.

class signal.Sigmasks

   "enum.IntEnum" collection of the constants "SIG_BLOCK",
   "SIG_UNBLOCK" and "SIG_SETMASK".

   Availability: Unix.

   Consulta la página del manual *sigprocmask(2)* y
   *pthread_sigmask(3)* para obtener más información.

   Added in version 3.5.

The variables defined in the "signal" module are:

signal.SIG_DFL

   Ésta es una de las dos opciones estándar de manejo de señales;
   simplemente realizará la función predeterminada para la señal. Por
   ejemplo, en la mayoría de los sistemas, la acción predeterminada
   para "SIGQUIT" es volcar el núcleo y salir, mientras que la acción
   predeterminada para "SIGCHLD" es simplemente ignorarlo.

signal.SIG_IGN

   Este es otro manejador de señales estándar, que simplemente
   ignorará la señal dada.

signal.SIGABRT

   Abortar señal de *abort(3)*.

signal.SIGALRM

   Señal de temporizador de *alarm(2)*.

   Availability: Unix.

signal.SIGBREAK

   Interrumpir desde el teclado (CTRL + BREAK).

   Availability: Windows.

signal.SIGBUS

   Error de bus (mal acceso a la memoria).

   Availability: Unix.

signal.SIGCHLD

   El proceso hijo se detuvo o terminó.

   Availability: Unix.

signal.SIGCLD

   Alias para "SIGCHLD".

   Availability: not macOS.

signal.SIGCONT

   Continuar el proceso si está detenido actualmente

   Availability: Unix.

signal.SIGFPE

   Excepción de coma flotante. Por ejemplo, división por cero.

   Ver también:

     "ZeroDivisionError" se genera cuando el segundo argumento de una
     operación de división o módulo es cero.

signal.SIGHUP

   Se detectó un bloqueo en el terminal de control o muerte del
   proceso de control.

   Availability: Unix.

signal.SIGILL

   Instrucción ilegal.

signal.SIGINT

   Interrumpir desde el teclado (CTRL + C).

   La acción predeterminada es generar "KeyboardInterrupt".

signal.SIGKILL

   Señal de muerte.

   No se puede detectar, bloquear ni ignorar.

   Availability: Unix.

signal.SIGPIPE

   Tubería rota: escriba en la tubería sin lectores.

   La acción predeterminada es ignorar la señal.

   Availability: Unix.

signal.SIGPROF

   Profiling timer expired.

   Availability: Unix.

signal.SIGQUIT

   Terminal quit signal.

   Availability: Unix.

signal.SIGSEGV

   Fallo de segmentación: referencia de memoria no válida.

signal.SIGSTOP

   Stop executing (cannot be caught or ignored).

   Availability: Unix.

signal.SIGSTKFLT

   Fallo en el coprocesador del stack. El kernel de Linux no lanza
   esta señal,esta sólo puede ser lanzada en el espacio de usuario.

   Availability: Linux.

   En arquitecturas donde la señal está disponible. Consulta la página
   del manual *signal(7)* para obtener más información.

   Added in version 3.11.

signal.SIGTERM

   Señal de terminación.

signal.SIGUSR1

   Señal definida por el usuario 1.

   Availability: Unix.

signal.SIGUSR2

   Señal definida por el usuario 2.

   Availability: Unix.

signal.SIGVTALRM

   Virtual timer expired.

   Availability: Unix.

signal.SIGWINCH

   Señal de cambio de tamaño de ventana.

   Availability: Unix.

signal.SIGXCPU

   CPU time limit exceeded.

   Availability: Unix.

SIG*

   All the signal numbers are defined symbolically.  For example, the
   hangup signal is defined as "signal.SIGHUP"; the variable names are
   identical to the names used in C programs, as found in
   "<signal.h>".  The Unix man page for '"signal"' lists the existing
   signals (on some systems this is *signal(2)*, on others the list is
   in *signal(7)*). Note that not all systems define the same set of
   signal names; only those names defined by the system are defined by
   this module.

signal.CTRL_C_EVENT

   La señal correspondiente al evento de pulsación de tecla "Ctrl"
   ""+"" "C". Esta señal solo se puede utilizar con "os.kill()".

   Availability: Windows.

   Added in version 3.2.

signal.CTRL_BREAK_EVENT

   La señal correspondiente al evento de pulsación de tecla "Ctrl"
   ""+"" "Break". Esta señal solo se puede utilizar con "os.kill()".

   Availability: Windows.

   Added in version 3.2.

signal.NSIG

   Un número más alto que el número más alto de señal. Use
   "valid_signals()" para obtener números válidos de señales.

signal.ITIMER_REAL

   Reduce el temporizador de intervalo en tiempo real y entrega
   "SIGALRM" al vencimiento.

signal.ITIMER_VIRTUAL

   Disminuye el temporizador de intervalo solo cuando el proceso se
   está ejecutando y entrega SIGVTALRM al vencimiento.

signal.ITIMER_PROF

   Disminuye el temporizador de intervalo tanto cuando se ejecuta el
   proceso como cuando el sistema se está ejecutando en nombre del
   proceso. Junto con ITIMER_VIRTUAL, este temporizador generalmente
   se usa para perfilar el tiempo que pasa la aplicación en el espacio
   del usuario y del kernel. SIGPROF se entrega al vencimiento.

signal.SIG_BLOCK

   Un valor posible para el parámetro *how* para "pthread_sigmask()"
   que indica que las señales deben bloquearse.

   Added in version 3.3.

signal.SIG_UNBLOCK

   Un valor posible para el parámetro *how* para "pthread_sigmask()"
   que indica que las señales deben desbloquearse.

   Added in version 3.3.

signal.SIG_SETMASK

   Un valor posible para el parámetro *how* para "pthread_sigmask()"
   que indica que la máscara de señal debe ser reemplazada.

   Added in version 3.3.

The "signal" module defines one exception:

exception signal.ItimerError

   Se genera para señalar un error de la implementación subyacente
   "setitimer()" o "getitimer()". Espere este error si se pasa un
   temporizador de intervalo no válido o un tiempo negativo a
   "setitimer()". Este error es un subtipo de "OSError".

   Added in version 3.3: Este error solía ser un subtipo de "IOError",
   que ahora es un alias de "OSError".

The "signal" module defines the following functions:

signal.alarm(time)

   Si *time* es distinto de cero, esta función solicita que se envíe
   una señal "SIGALRM" al proceso en *time* segundos. Se cancela
   cualquier alarma programada previamente (solo se puede programar
   una alarma en cualquier momento). El valor retornado es entonces el
   número de segundos antes de que se entregara cualquier alarma
   previamente configurada. Si *time* es cero, no se programa ninguna
   alarma y se cancela cualquier alarma programada. Si el valor de
   retorno es cero, no hay ninguna alarma programada actualmente.

   Availability: Unix.

   Consulta la página del manual *alarm(2)* para obtener más
   información.

signal.getsignal(signalnum)

   Retorna el manejador de señales actual para la señal *signalnum*.
   El valor retornado puede ser un objeto de Python invocable o uno de
   los valores especiales "signal.SIG_IGN", "signal.SIG_DFL" o "None".
   Aquí, "signal.SIG_IGN" significa que la señal fue previamente
   ignorada, "signal.SIG_DFL" significa que la forma predeterminada de
   manejar la señal estaba en uso anteriormente, y el gestor de
   señales no se instaló desde Python.

signal.strsignal(signalnum)

   Retorna la descripción de la señal *signalnum*, como "Interrupt"
   para "SIGINT". Retorna "None" si *signalnum* no tiene descripción.
   Lanza "ValueError" si *signalnum* no es válido.

   Added in version 3.8.

signal.valid_signals()

   Retorna el conjunto de números de señal válidos en esta plataforma.
   Esto puede ser menor que "rango(1, NSIG)" si el sistema reserva
   algunas señales para uso interno.

   Added in version 3.8.

signal.pause()

   Hacer que el proceso duerma hasta que se reciba una señal; entonces
   se llamará al manejador apropiado. No retorna nada.

   Availability: Unix.

   Consulta la página del manual *signal(2)* para obtener más
   información.

   Vea también "sigwait()", "sigwaitinfo()", "sigtimedwait()" y
   "sigpending()".

signal.raise_signal(signum)

   Envía una señal al proceso de llamada. No retorna nada.

   Added in version 3.8.

signal.pidfd_send_signal(pidfd, sig, siginfo=None, flags=0)

   Envía la señal *sig* al proceso referido por el descriptor de
   archivo *pidfd*. Python actualmente no soporta el parámetro
   *siginfo*; éste debe ser "None". El argumento *flags* está proveído
   para extensiones futuras; no hay valores actualmente definidos para
   *flags*.

   Para más información vea la página de manual
   *pidfd_send_signal(2)*.

   Availability: Linux >= 5.1, Android >= "build-time" API level 31

   Added in version 3.9.

signal.pthread_kill(thread_id, signalnum)

   Envíe la señal *signalnum* al hilo *thread_id*, otro hilo en el
   mismo proceso que el llamador. El hilo de destino puede ejecutar
   cualquier código (Python o no). Sin embargo, si el hilo de destino
   está ejecutando el intérprete de Python, los manejadores de señales
   de Python serán ejecutados por el hilo principal. Por lo tanto, el
   único punto de enviar una señal a un hilo de Python en particular
   sería forzar que una llamada al sistema en ejecución falle con
   "InterruptedError".

   Use "threading.get_ident()" or the "ident" attribute of
   "threading.Thread" objects to get a suitable value for *thread_id*.

   Si *signalnum* es 0, no se envía ninguna señal, pero se sigue
   realizando la comprobación de errores; esto se puede usar para
   verificar si el hilo de destino aún se está ejecutando.

   Genera un evento de auditoría "signal.pthread_kill" con argumentos
   "thread_id", "signalnum".

   Availability: Unix.

   Consulta la página del manual *pthread_kill(3)* para obtener más
   información.

   Vea también "os.kill()".

   Added in version 3.3.

signal.pthread_sigmask(how, mask)

   Busca o cambia la máscara de señal del hilo de llamada. La máscara
   de señal es el conjunto de señales cuya entrega está actualmente
   bloqueada para la persona que llama. Retorna la máscara de señal
   anterior como un conjunto de señales.

   El comportamiento de la llamada depende del valor de *how*, como
   sigue.

   * "SIG_BLOCK": El conjunto de señales bloqueadas es la unión del
     conjunto actual y el argumento *mask*.

   * "SIG_UNBLOCK": Las señales en *mask* se eliminan del conjunto
     actual de señales bloqueadas. Está permitido intentar desbloquear
     una señal que no esté bloqueada.

   * "SIG_SETMASK": El conjunto de señales bloqueadas se establece en
     el argumento *mask*.

   *mask* es un conjunto de números de señales (por ejemplo,
   {"signal.SIGINT", "signal.SIGTERM"}). Utilice "valid_signals()"
   para una máscara completa que incluya todas las señales.

   Por ejemplo, "signal.pthread_sigmask(signal.SIG_BLOCK, [])" lee la
   máscara de señal del hilo de llamada.

   "SIGKILL" y "SIGSTOP" no se pueden bloquear.

   Availability: Unix.

   Consulta la página del manual *sigprocmask(2)* y
   *pthread_sigmask(3)* para obtener más información.

   Vea también "pause()", "sigpending()" y "sigwait()".

   Added in version 3.3.

signal.setitimer(which, seconds, interval=0.0)

   Establece el temporizador de intervalo dado (uno de
   "signal.ITIMER_REAL", "signal.ITIMER_VIRTUAL" o
   "signal.ITIMER_PROF") especificado por *which* disparar después de
   *seconds* (se acepta el números de punto flotante, diferente de
   "alarm()") y luego cada *interval* segundos (si *interval* es
   distinto de cero). El temporizador de intervalo especificado por
   *which* se puede borrar estableciendo *seconds* en cero.

   Cuando se dispara un temporizador de intervalos, se envía una señal
   al proceso. La señal enviada depende del temporizador que se
   utilice; "signal.ITIMER_REAL" entregará "SIGALRM",
   "signal.ITIMER_VIRTUAL" envía "SIGVTALRM", y "signal.ITIMER_PROF"
   entregará "SIGPROF".

   Los valores antiguos se retornan como una tupla: (retraso,
   intervalo).

   Si intenta pasar un temporizador de intervalo no válido, se
   producirá un "ItimerError".

   Availability: Unix.

signal.getitimer(which)

   Retorna el valor actual de un temporizador de intervalo dado
   especificado por *which*.

   Availability: Unix.

signal.set_wakeup_fd(fd, *, warn_on_full_buffer=True)

   Set the wakeup file descriptor to *fd*.  When a signal your program
   has registered a signal handler for is received, the signal number
   is written as a single byte into the fd.  If you haven't registered
   a signal handler for the signals you care about, then nothing will
   be written to the wakeup fd. This can be used by a library to
   wakeup a poll or select call, allowing the signal to be fully
   processed.

   Se retorna el antiguo fd de activación (o -1 si la activación del
   descriptor de archivo no estaba habilitada). Si *fd* es -1, la
   activación del descriptor de archivo está deshabilitada. Si no es
   -1, *fd* debe ser sin bloqueo. Depende de la biblioteca eliminar
   los bytes de *fd* antes de llamar a poll o seleccionar nuevamente.

   Cuando los hilos están habilitados, esta función solo se puede
   llamar desde el subproceso principal del intérprete principal;
   intentar llamarlo desde otros hilos hará que se lance una excepción
   "ValueError".

   Hay dos formas habituales de utilizar esta función. En ambos
   enfoques, usa el fd para despertarse cuando llega una señal, pero
   luego difieren en cómo determinan *which* señal o señales han
   llegado.

   En el primer enfoque, leemos los datos del búfer de fd, y los
   valores de bytes le dan los números de señal. Esto es simple, pero
   en casos raros puede surgir un problema: generalmente el fd tendrá
   una cantidad limitada de espacio en el búfer, y si llegan
   demasiadas señales demasiado rápido, entonces el búfer puede
   llenarse y algunas señales pueden perderse. Si usa este enfoque,
   entonces debe configurar "warn_on_full_buffer = True", que al menos
   causará que se imprima una advertencia en stderr cuando se pierdan
   las señales.

   En el segundo enfoque, usamos el wakeup fd *solo* para wakeups e
   ignoramos los valores de bytes reales. En este caso, lo único que
   nos importa es si el búfer de fd está vacío o no; un búfer lleno no
   indica ningún problema. Si utiliza este enfoque, debe configurar
   "warn_on_full_buffer = False", para que sus usuarios no se
   confundan con mensajes de advertencia falsos.

   Distinto en la versión 3.5: En Windows, la función ahora también
   admite identificadores de socket.

   Distinto en la versión 3.7: Se agregó el parámetro
   "warn_on_full_buffer".

signal.siginterrupt(signalnum, flag)

   Cambiar el comportamiento de reinicio de la llamada al sistema: si
   *flag* es "False", las llamadas al sistema se reiniciarán cuando
   las interrumpa la señal *signalnum*, de lo contrario, las llamadas
   al sistema se interrumpirán. No retorna nada.

   Availability: Unix.

   Consulta la página del manual *siginterrupt(3)* para obtener más
   información.

   Tenga en cuenta que la instalación de un gestor de señales con
   "signal()" restablecerá el comportamiento de reinicio a
   interrumpible llamando implícitamente a "siginterrupt()" con un
   valor de *flag* verdadero para la señal dada.

signal.signal(signalnum, handler)

   Establece el gestor de la señal *signalnum* en la función *handler*
   (manejador). *handler* puede ser un objeto de Python invocable que
   toma dos argumentos (ver más abajo), o uno de los valores
   especiales "signal.SIG_IGN" o "signal.SIG_DFL". Se retornará el
   manejador de señales anterior (vea la descripción de "getsignal()"
   arriba). (Consulte la página del manual de Unix *signal(2)* para
   obtener más información).

   Cuando los hilos están habilitados, esta función solo se puede
   llamar desde el subproceso principal del intérprete principal;
   intentar llamarlo desde otros hilos hará que se lance una excepción
   "ValueError".

   El *handler* se llama con dos argumentos: el número de señal y el
   marco de pila actual ("None" o un objeto marco; para obtener una
   descripción de los objetos marco, consulte la descripción en la
   jerarquía de tipos o vea las descripciones de los atributos en el
   módulo "inspect").

   En Windows, "signal()" solo se puede llamar con "SIGABRT",
   "SIGFPE", "SIGILL", "SIGINT", "SIGSEGV", "SIGTERM", o "SIGBREAK".
   Un "ValueError" se lanzará en cualquier otro caso. Tenga en cuenta
   que no todos los sistemas definen el mismo conjunto de nombres de
   señales; un "AttributeError" se lanzará si un nombre de señal no
   está definido como constante de nivel de módulo "SIG*".

signal.sigpending()

   Examine el conjunto de señales que están pendientes de entrega al
   hilo de llamada (es decir, las señales que se han generado mientras
   estaban bloqueadas). Retorna el conjunto de señales pendientes.

   Availability: Unix.

   Consulta la página del manual *sigpending(2)* para obtener más
   información.

   Vea también "pause()", "pthread_sigmask()" y "sigwait()".

   Added in version 3.3.

signal.sigwait(sigset)

   Suspende la ejecución del hilo de llamada hasta la entrega de una
   de las señales especificadas en el conjunto de señales *sigset*. La
   función acepta la señal (la elimina de la lista pendiente de
   señales) y retorna el número de señal.

   Availability: Unix.

   Consulta la página del manual *sigwait(3)* para obtener más
   información.

   Vea también "pause()", "pthread_sigmask()", "sigpending()",
   "sigwaitinfo()" y "sigtimedwait()".

   Added in version 3.3.

signal.sigwaitinfo(sigset)

   Suspende la ejecución del hilo de llamada hasta la entrega de una
   de las señales especificadas en el conjunto de señales *sigset*. La
   función acepta la señal y la elimina de la lista de señales
   pendientes. Si una de las señales en *sigset* ya está pendiente
   para el hilo de llamada, la función regresará inmediatamente con
   información sobre esa señal. No se llama al gestor de señales para
   la señal enviada. La función genera un "InterruptedError" si es
   interrumpida por una señal que no está en *sigset*.

   The return value is an object representing the data contained in
   the "siginfo_t" structure, namely: "si_signo", "si_code",
   "si_errno", "si_pid", "si_uid", "si_status", "si_band".

   Availability: Unix.

   Consulta la página del manual *sigwaitinfo(2)* para obtener más
   información.

   Vea también "pause()", "sigwait()" y "sigtimedwait()".

   Added in version 3.3.

   Distinto en la versión 3.5: La función ahora se vuelve a intentar
   si es interrumpida por una señal que no está en *sigset* y el
   manejador de señales no genera una excepción (ver **PEP 475** para
   la justificación).

signal.sigtimedwait(sigset, timeout)

   Similar a "sigwaitinfo()", pero toma un argumento *timeout*
   adicional que especifica un tiempo de espera. Si *timeout* se
   especifica como "0", se realiza una encuesta. Retorna "None" si se
   agota el tiempo de espera.

   Availability: Unix.

   Consulta la página del manual *sigtimedwait(2)* para obtener más
   información.

   Vea también "pause()", "sigwait()" y "sigwaitinfo()".

   Added in version 3.3.

   Distinto en la versión 3.5: La función ahora se reintenta con el
   *timeout* recalculado si se interrumpe por una señal que no está en
   *sigset* y el manejador de señales no genera una excepción (ver
   **PEP 475** para la justificación).

## Ejemplos

Aquí hay un programa de ejemplo mínimo. Utiliza la función "alarm()"
para limitar el tiempo de espera para abrir un archivo; esto es útil
si el archivo es para un dispositivo serial que puede no estar
encendido, lo que normalmente haría que "os.open()" se cuelgue
indefinidamente. La solución es configurar una alarma de 5 segundos
antes de abrir el archivo; si la operación lleva demasiado tiempo, se
enviará la señal de alarma y el gestor genera una excepción.

   import signal, os

   def handler(signum, frame):
       signame = signal.Signals(signum).name
       print(f'Signal handler called with signal {signame} ({signum})')
       raise OSError("Couldn't open device!")

   # Set the signal handler and a 5-second alarm
   signal.signal(signal.SIGALRM, handler)
   signal.alarm(5)

   # This open() may hang indefinitely
   fd = os.open('/dev/ttyS0', os.O_RDWR)

   signal.alarm(0)          # Disable the alarm

## Nota sobre SIGPIPE

Canalizar la salida de su programa a herramientas como *head(1)* hará
que se envíe una señal "SIGPIPE" a su proceso cuando el receptor de su
salida estándar se cierre antes. Esto da como resultado una excepción
como "BrokenPipeError: [Errno 32] Broken pipe". Para manejar este
caso, envuelva su punto de entrada para detectar esta excepción de la
siguiente manera:

   import os
   import sys

   def main():
       try:
           # simulate large output (your code replaces this loop)
           for x in range(10000):
               print("y")
           # flush output here to force SIGPIPE to be triggered
           # while inside this try block.
           sys.stdout.flush()
       except BrokenPipeError:
           # Python flushes standard streams on exit; redirect remaining output
           # to devnull to avoid another BrokenPipeError at shutdown
           devnull = os.open(os.devnull, os.O_WRONLY)
           os.dup2(devnull, sys.stdout.fileno())
           sys.exit(1)  # Python exits with error code 1 on EPIPE

   if __name__ == '__main__':
       main()

No establezcas la disposición de "SIGPIPE" en "SIG_DFL" para evitar
"BrokenPipeError". Hacerlo causaría que tu programa se cierre
inesperadamente siempre que se interrumpa cualquier conexión de socket
mientras su programa aún esté escribiendo en él.

## Nota sobre Manejadores de Señales y Excepciones

Si un gestor de señal lanza una excepción, ésta excepción será
propagada al hilo principal de ejecución y podría ser lanzado luego de
cualquier instrucción de *bytecode*. Más notablemente,
"KeyboardInterrupt" podría aparecer en cualquier momento de la
ejecución. La mayoría del código python, incluida la librería
estándar, no puede robustecerse en contra esto, y por esto
"KeyboardInterrupt" (o cualquier otra excepción resultante de un
gestor de señal) podría poner el programa en un estado inesperado en
raras ocasiones.

Para ilustrar esto, considere el siguiente código:

   class SpamContext:
       def __init__(self):
           self.lock = threading.Lock()

       def __enter__(self):
           # If KeyboardInterrupt occurs here, everything is fine
           self.lock.acquire()
           # If KeyboardInterrupt occurs here, __exit__ will not be called
           ...
           # KeyboardInterrupt could occur just before the function returns

       def __exit__(self, exc_type, exc_val, exc_tb):
           ...
           self.lock.release()

Para muchos programas, especialmente para los que sólo quieren
interrumpir la ejecución ante un "KeyboardInterrupt", esto no es un
problema, pero las aplicaciones que son complejas o requieren alta
confiabilidad deben evitar lanzar excepciones desde los gestores de
señales. También deben evitar atrapar "KeyboardInterrupt" como medio
de una terminación de ejecución airosa. En su lugar, deben instalar su
propio gestor "SIGINT". A continuación, un ejemplo de un servidor HTTP
que evita el "KeyboardInterrupt":

   import signal
   import socket
   from selectors import DefaultSelector, EVENT_READ
   from http.server import HTTPServer, SimpleHTTPRequestHandler

   interrupt_read, interrupt_write = socket.socketpair()

   def handler(signum, frame):
       print('Signal handler called with signal', signum)
       interrupt_write.send(b'\0')
   signal.signal(signal.SIGINT, handler)

   def serve_forever(httpd):
       sel = DefaultSelector()
       sel.register(interrupt_read, EVENT_READ)
       sel.register(httpd, EVENT_READ)

       while True:
           for key, _ in sel.select():
               if key.fileobj == interrupt_read:
                   interrupt_read.recv(1)
                   return
               if key.fileobj == httpd:
                   httpd.handle_request()

   print("Serving on port 8000")
   httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
   serve_forever(httpd)
   print("Shutdown...")
