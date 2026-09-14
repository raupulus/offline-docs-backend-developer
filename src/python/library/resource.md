---
title: '"resource" --- Resource usage information'
source_url: https://docs.python.org/es/3
source_path: library/resource.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3680
---

# "resource" --- Resource usage information

======================================================================

Este módulo proporciona mecanismos básicos para medir y controlar los
recursos del sistema utilizados por un programa.

Availability: Unix, not WASI.

Las constantes simbólicas se utilizan para especificar recursos
concretos del sistema y para solicitar información de uso sobre el
proceso actual o sus elementos secundarios.

Se genera un "OSError" cuando la llamada al sistema (*syscall*) falla.

exception resource.error

   Un alias en desuso de "OSError".

   Distinto en la versión 3.3: Tras **PEP 3151** esta clase se
   convirtió en un alias de "OSError".

## Límites de recursos

El uso de recursos se puede limitar usando la función "setrlimit()"
que se describe a continuación. Cada recurso está controlado por un
par de límites: un límite flexible y un límite duro. El límite
flexible es el límite actual, y puede ser reducido o elevado con el
tiempo mediante un proceso. El límite flexible nunca puede exceder el
límite duro. El límite duro se puede reducir a cualquier valor mayor
que el del límite flexible, pero no se puede elevar. (Solo los
procesos con el UID efectivo del superusuario pueden aumentar un
límite duro.)

Los recursos específicos que se pueden limitar dependen del sistema.
Se describen en la página de manual *getrlimit(2)*. Los recursos
enumerados a continuación se admiten cuando el sistema operativo
subyacente los admite; los recursos que no pueden ser verificados o
controlados por el sistema operativo no se definen en este módulo para
esas plataformas.

resource.RLIM_INFINITY

   Constante utilizada para representar el límite de un recurso
   ilimitado.

resource.getrlimit(resource)

   Retorna una tupla "(soft, hard)" con los límites flexible y duro
   actuales de *resource*. Genera "ValueError" si se especifica un
   recurso no válido o "error" si la llamada al sistema subyacente
   falla inesperadamente.

resource.setrlimit(resource, limits)

   Sets new limits of consumption of *resource*. The *limits* argument
   must be a tuple "(soft, hard)" of two integers describing the new
   limits. A value of "RLIM_INFINITY" can be used to request a limit
   that is unlimited.

   Raises "ValueError" if an invalid resource is specified, if the new
   soft limit exceeds the hard limit, or if a process tries to raise
   its hard limit. Specifying a limit of "RLIM_INFINITY" when the hard
   or system limit for that resource is not unlimited will result in a
   "ValueError".  A process with the effective UID of super-user can
   request any valid limit value, including unlimited, but
   "ValueError" will still be raised if the requested limit exceeds
   the system imposed limit.

   "setrlimit" también puede generar un "error" si falla la llamada al
   sistema subyacente.

   VxWorks only supports setting "RLIMIT_NOFILE".

   Genera un auditing event "resource.setrlimit" con los argumentos
   "resource", "limits".

resource.prlimit(pid, resource[, limits])

   Combina "setrlimit()" y "getrlimit()" en una sola función y admite
   obtener y establecer los límites de recursos de un proceso
   arbitrario. Si *pid* es 0, entonces la llamada se aplica al proceso
   actual. *resource* y *limits* tienen el mismo significado que en
   "setrlimit()", excepto por que *limits* es opcional.

   Cuando no se proporciona *limits* la función retorna el límite de
   *resource* del proceso *pid*. Cuando se proporciona *limits*, se
   establece el límite de *resource* del proceso y se retorna el
   límite de recursos anterior.

   Genera "ProcessLookupError" cuando no se encuentra *pid* y
   "PermissionError" cuando el usuario no tiene "CAP_SYS_RESOURCE"
   para el proceso.

   Genera un evento de auditoría "resource.prlimit" con los argumentos
   "pid", "resource", "limits".

   Availability: Linux >= 2.6.36 with glibc >= 2.13.

   Added in version 3.4.

Estos símbolos definen los recursos cuyo consumo se puede controlar
usando las funciones "setrlimit()" y "getrlimit()" que se describen
más abajo. Los valores de estos símbolos son exactamente las
constantes utilizadas por programas en C.

La página de manual de Unix para *getrlimit(2)* detalla los recursos
disponibles. Tenga en cuenta que no todos los sistemas usan el mismo
símbolo o el mismo valor para referirse al mismo recurso. Este módulo
no pretende enmascarar las diferencias entre plataformas --- los
símbolos no definidos para una plataforma no estarán disponibles en
este módulo en esa plataforma.

resource.RLIMIT_CORE

   El tamaño máximo (en bytes) de un archivo central que puede crear
   el proceso actual. Esto podría resultar en la creación de un
   archivo central parcial si se requiriera uno más grande para
   contener la imagen del proceso entera.

resource.RLIMIT_CPU

   The maximum amount of processor time (in seconds) that a process
   can use. If this limit is exceeded, a "SIGXCPU" signal is sent to
   the process. (See the "signal" module documentation for information
   about how to catch this signal and do something useful, e.g. flush
   open files to disk.)

resource.RLIMIT_FSIZE

   El tamaño máximo de un archivo que pueda crear el proceso.

resource.RLIMIT_DATA

   El tamaño máximo (en bytes) de la memoria *heap* del proceso.

resource.RLIMIT_STACK

   El tamaño máximo (en bytes) de la pila de llamadas para el proceso
   actual. Esto afecta únicamente a la pila del hilo principal en un
   proceso multi-hilo.

resource.RLIMIT_RSS

   El tamaño máximo del conjunto residente (*RSS*) del que puede
   disponer el proceso.

resource.RLIMIT_NPROC

   El número máximo de procesos que puede crear el proceso actual.

resource.RLIMIT_NOFILE

   El número máximo de descriptores de archivo abierto para el proceso
   actual.

resource.RLIMIT_OFILE

   El nombre BDS para "RLIMIT_NOFILE".

resource.RLIMIT_MEMLOCK

   El espacio de direcciones máximo que se puede bloquear en la
   memoria.

resource.RLIMIT_VMEM

   The largest area of mapped memory which the process may occupy.
   Usually an alias of "RLIMIT_AS".

   Availability: Solaris, FreeBSD, NetBSD.

resource.RLIMIT_AS

   El área máxima (en bytes) de espacio de direcciones que puede tomar
   el proceso.

resource.RLIMIT_MSGQUEUE

   El número de bytes que se pueden asignar a las colas de mensajes
   POSIX.

   Availability: Linux >= 2.6.8.

   Added in version 3.4.

resource.RLIMIT_NICE

   El techo del nivel del proceso *nice* (calculado como 20 -
   rlim_cur).

   Availability: Linux >= 2.6.12.

   Added in version 3.4.

resource.RLIMIT_RTPRIO

   El techo de la prioridad en tiempo real.

   Availability: Linux >= 2.6.12.

   Added in version 3.4.

resource.RLIMIT_RTTIME

   El límite de tiempo (en microsegundos) en tiempo de CPU que puede
   dedicar un proceso de programación en tiempo real sin hacer una
   llamada al sistema de bloqueo.

   Availability: Linux >= 2.6.25.

   Added in version 3.4.

resource.RLIMIT_SIGPENDING

   El número de señales que el proceso puede poner en cola.

   Availability: Linux >= 2.6.8.

   Added in version 3.4.

resource.RLIMIT_SBSIZE

   El tamaño máximo (en bytes) de uso del búfer del socket para este
   usuario. Esto limita la cantidad de memoria de red, y por lo tanto
   la cantidad de mbufs, que este usuario puede retener en todo
   momento.

   Availability: FreeBSD, NetBSD.

   Added in version 3.4.

resource.RLIMIT_SWAP

   El tamaño máximo (en bytes) del espacio de intercambio que puede
   ser reservado o utilizado por todos los procesos de este ID de
   usuario. Este límite se aplica solo si se establece el bit 1 de
   vm.overcommit sysctl. Consulte tuning(7) para obtener una
   descripción completa de este sysctl.

   Availability: FreeBSD >= 8.

   Added in version 3.4.

resource.RLIMIT_NPTS

   El número máximo de pseudo-terminales que puede crear esta ID de
   usuario.

   Availability: FreeBSD >= 8.

   Added in version 3.4.

resource.RLIMIT_KQUEUES

   El número máximo de kqueues que este ID de usuario puede crear.

   Availability: FreeBSD >= 11.

   Added in version 3.10.

## Utilización de recursos

Estas funciones se usan para recuperar la información de utilización
de recursos:

resource.getrusage(who)

   This function returns an object that describes the resources
   consumed by either the current process or its children, as
   specified by the *who* parameter.  The *who* parameter should be
   specified using one of the "RUSAGE_*" constants described below.

   Un ejemplo sencillo:

      from resource import *
      import time

      # a non CPU-bound task
      time.sleep(3)
      print(getrusage(RUSAGE_SELF))

      # a CPU-bound task
      for i in range(10 ** 8):
         _ = 1 + 1
      print(getrusage(RUSAGE_SELF))

   The fields of the return value each describe how a particular
   system resource has been used, e.g. amount of time spent running in
   user mode or number of times the process was swapped out of main
   memory. Some values are dependent on the clock tick interval, e.g.
   the amount of memory the process is using.

   Por compatibilidad con versiones anteriores, el valor retornado es
   accesible también como una tupla de 16 elementos.

   The fields "ru_utime" and "ru_stime" of the return value are
   floating-point values representing the amount of time spent
   executing in user mode and the amount of time spent executing in
   system mode, respectively. The remaining values are integers.
   Consult the *getrusage(2)* man page for detailed information about
   these values. A brief summary is presented here:

   +----------+------------------------+-----------------------------------------+
   | Índice   | Campo                  | Recurso                                 |
   |==========|========================|=========================================|
   | "0"      | "ru_utime"             | tiempo en modo usuario (flotante en     |
   |          |                        | segundos)                               |
   +----------+------------------------+-----------------------------------------+
   | "1"      | "ru_stime"             | tiempo en modo sistema (flotante en     |
   |          |                        | segundos)                               |
   +----------+------------------------+-----------------------------------------+
   | "2"      | "ru_maxrss"            | tamaño máximo del conjunto residente    |
   +----------+------------------------+-----------------------------------------+
   | "3"      | "ru_ixrss"             | tamaño de memoria compartida            |
   +----------+------------------------+-----------------------------------------+
   | "4"      | "ru_idrss"             | tamaño de memoria no compartida         |
   +----------+------------------------+-----------------------------------------+
   | "5"      | "ru_isrss"             | tamaño de la pila no compartida         |
   +----------+------------------------+-----------------------------------------+
   | "6"      | "ru_minflt"            | fallos de página que no requieran E/S   |
   +----------+------------------------+-----------------------------------------+
   | "7"      | "ru_majflt"            | fallos de página que requieran E/S      |
   +----------+------------------------+-----------------------------------------+
   | "8"      | "ru_nswap"             | número de intercambios                  |
   +----------+------------------------+-----------------------------------------+
   | "9"      | "ru_inblock"           | bloque de operaciones de entrada        |
   +----------+------------------------+-----------------------------------------+
   | "10"     | "ru_oublock"           | bloque de operaciones de salida         |
   +----------+------------------------+-----------------------------------------+
   | "11"     | "ru_msgsnd"            | mensajes enviados                       |
   +----------+------------------------+-----------------------------------------+
   | "12"     | "ru_msgrcv"            | mensajes recibidos                      |
   +----------+------------------------+-----------------------------------------+
   | "13"     | "ru_nsignals"          | señales recibidas                       |
   +----------+------------------------+-----------------------------------------+
   | "14"     | "ru_nvcsw"             | intercambios de contexto voluntarios    |
   +----------+------------------------+-----------------------------------------+
   | "15"     | "ru_nivcsw"            | intercambios de contexto involuntarios  |
   +----------+------------------------+-----------------------------------------+

   Esta función lanzará un "ValueError" si el parámetro *who*
   especificado no es válido. También puede generar una excepción
   "error" en circunstancias inusuales.

resource.getpagesize()

   Retorna el número de bytes en una página de sistema. (Esta no es
   necesariamente del mismo tamaño que la página de hardware).

The following "RUSAGE_*" symbols are passed to the "getrusage()"
function to specify which processes information should be provided
for.

resource.RUSAGE_SELF

   Pasar a "getrusage()" para solicitar recursos consumidos por el
   proceso de llamada, que es la suma de recursos utilizados por todos
   los hilos en el proceso.

resource.RUSAGE_CHILDREN

   Pasar a "getrusage()" para solicitar recursos consumidos por
   procesos secundarios del proceso de llamada que se han terminado o
   a los que se les está esperando.

resource.RUSAGE_BOTH

   Pasar a "getrusage()" para solicitar recursos consumidos por el
   proceso actual y sus procesos secundarios. Puede que no esté
   disponible en todos los sistemas.

resource.RUSAGE_THREAD

   Pasa a "getrusage()" para solicitar recursos consumidos por el hilo
   actual. Puede que no esté disponible en todos los sistemas.

   Added in version 3.2.
