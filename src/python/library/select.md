---
title: '"select" --- Waiting for I/O completion'
source_url: https://docs.python.org/es/3
source_path: library/select.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3740
---

# "select" --- Waiting for I/O completion

======================================================================

This module provides access to the "select()" and "poll()" functions
available in most operating systems, "devpoll()" available on Solaris
and derivatives, "epoll()" available on Linux 2.5+ and "kqueue()"
available on most BSD. Note that on Windows, it only works for
sockets; on other operating systems, it also works for other file
types (in particular, on Unix, it works on pipes). It cannot be used
on regular files to determine whether a file has grown since it was
last read.

Nota:

  The "selectors" module allows high-level and efficient I/O
  multiplexing, built upon the "select" module primitives. Users are
  encouraged to use the "selectors" module instead, unless they want
  precise control over the OS-level primitives used.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

El módulo define lo siguiente:

exception select.error

   Un alias en desuso de "OSError".

   Distinto en la versión 3.3: Siguiente **PEP 3151**, esta clase se
   convirtió en un alias de "OSError".

select.devpoll()

   Returns a "/dev/poll" polling object; see section /dev/poll polling
   objects below for the methods supported by devpoll objects.

   "devpoll()" objects are linked to the number of file descriptors
   allowed at the time of instantiation. If your program reduces this
   value, "devpoll()" will fail. If your program increases this value,
   "devpoll()" may return an incomplete list of active file
   descriptors.

   El nuevo descriptor del archivo es non-inheritable.

   Added in version 3.3.

   Distinto en la versión 3.4: El nuevo descriptor de archivo ahora no
   es heredable.

   Availability: Solaris.

select.epoll(sizehint=-1, flags=0)

   Return an edge polling object, which can be used as Edge or Level
   Triggered interface for I/O events.

   *sizehint* informs epoll about the expected number of events to be
   registered.  It must be positive, or "-1" to use the default. It is
   only used on older systems where "epoll_create1()" is not
   available; otherwise it has no effect (though its value is still
   checked).

   *flags* está en desuso y se ignora por completo. Sin embargo,
   cuando se proporciona, su valor debe ser "0" o
   "select.EPOLL_CLOEXEC", de lo contrario, se lanzará "OSError".

   Consulte la sección Edge and level trigger polling (epoll) objects
   a continuación para conocer los métodos admitidos por los objetos
   epolling.

   Los objetos "epoll" admiten el protocolo *context management*:
   cuando se usa en una declaración "with", el nuevo descriptor de
   archivo se cierra automáticamente al final del bloque.

   El nuevo descriptor del archivo es non-inheritable.

   Distinto en la versión 3.3: Se agregó el parámetro *flags*.

   Distinto en la versión 3.4: Se agregó soporte para la declaración
   "with". El nuevo descriptor de archivo ahora no es heredable.

   Obsoleto desde la versión 3.4: El parámetro *flags*.
   "select.EPOLL_CLOEXEC" se usa por defecto ahora. Use
   "os.set_inheritable()" para hacer que el descriptor de archivo sea
   heredable.

   Availability: Linux >= 2.5.44.

select.poll()

   Returns a polling object, which supports registering and
   unregistering file descriptors, and then polling them for I/O
   events; see section Polling objects below for the methods supported
   by polling objects.

   Availability: Unix.

select.kqueue()

   Returns a kernel queue object; see section Kqueue objects below for
   the methods supported by kqueue objects.

   El nuevo descriptor del archivo es non-inheritable.

   Distinto en la versión 3.4: El nuevo descriptor de archivo ahora no
   es heredable.

   Availability: BSD, macOS.

select.kevent(ident, filter=KQ_FILTER_READ, flags=KQ_EV_ADD, fflags=0, data=0, udata=0)

   Returns a kernel event object; see section Kevent objects below for
   the methods supported by kevent objects.

   Availability: BSD, macOS.

select.select(rlist, wlist, xlist, timeout=None)

   This is a straightforward interface to the Unix "select()" system
   call. The first three arguments are iterables of 'waitable
   objects': either integers representing file descriptors or objects
   with a parameterless method named "fileno()" returning such an
   integer:

   * *rlist*: espera hasta que esté listo para leer

   * *wlist*: espera hasta que esté listo para escribir

   * *xlist*: espera una "condición excepcional" (consulte la página
     del manual para ver lo que su sistema considera tal condición)

   Empty iterables are allowed, but acceptance of three empty
   iterables is platform-dependent. (It is known to work on Unix but
   not on Windows.)  The optional *timeout* argument specifies a time-
   out as a floating-point number in seconds. When the *timeout*
   argument is omitted or "None", the function blocks until at least
   one file descriptor is ready.  A time-out value of zero specifies a
   poll and never blocks.

   El valor de retorno es un triple de listas de objetos que están
   listos: subconjuntos de los primeros tres argumentos. Cuando se
   alcanza el tiempo de espera sin que esté listo un descriptor de
   archivo, se retornan tres listas vacías.

   Entre los tipos de objetos aceptables en los iterables se
   encuentran Python *objetos de archivo* (por ejemplo, "sys.stdin", u
   objetos retornados por "open()" o "os.popen()" ), objetos de socket
   retornados por "socket.socket()". También puede definir una clase
   *wrapper* usted mismo, siempre que tenga un método "fileno()"
   apropiado (que realmente retorne un descriptor de archivo, no solo
   un entero aleatorio).

   Nota:

     File objects on Windows are not acceptable, but sockets are.  On
     Windows, the underlying "select()" function is provided by the
     WinSock library, and does not handle file descriptors that don't
     originate from WinSock.

   Distinto en la versión 3.5: La función ahora se vuelve a intentar
   con un tiempo de espera (*timeout*) recalculado cuando se
   interrumpe por una señal, excepto si el controlador de señal genera
   una excepción (ver **PEP 475** para la justificación), en lugar de
   generar "InterruptedError".

select.PIPE_BUF

   The minimum number of bytes which can be written without blocking
   to a pipe when the pipe has been reported as ready for writing by
   "select()", "poll()" or another interface in this module.  This
   doesn't apply to other kinds of file-like objects such as sockets.

   Este valor es garantizado por POSIX para ser menor a 512.

   Availability: Unix

   Added in version 3.2.

## "/dev/poll" polling objects

Solaris and derivatives have "/dev/poll". While "select()" is
*O*(*highest file descriptor*) and "poll()" is *O*(*number of file
descriptors*), "/dev/poll" is *O*(*active file descriptors*).

"/dev/poll" behaviour is very close to the standard "poll()" object.

devpoll.close()

   Cierra el descriptor de archivo del objeto de sondeo.

   Added in version 3.4.

devpoll.closed

   "True" si el objeto de sondeo está cerrado.

   Added in version 3.4.

devpoll.fileno()

   Retorna el número de descriptor de archivo del objeto de sondeo.

   Added in version 3.4.

devpoll.register(fd[, eventmask])

   Registra un descriptor de archivo con el objeto de sondeo. Las
   futuras llamadas al método "poll()" comprobarán si el descriptor
   del archivo tiene algún evento I/O pendiente. *fd* puede ser un
   entero o un objeto con un método "fileno()" que retorna un entero.
   Los objetos de archivo implementan "Fileno()", por lo que también
   pueden usarse como argumento.

   *eventmask* is an optional bitmask describing the type of events
   you want to check for. The constants are the same as with "poll()"
   object. The default value is a combination of the constants
   "POLLIN", "POLLPRI", and "POLLOUT".

   Advertencia:

     Registering a file descriptor that's already registered is not an
     error, but the result is undefined. The appropriate action is to
     unregister or modify it first. This is an important difference
     compared with "poll()".

devpoll.modify(fd[, eventmask])

   This method does an "unregister()" followed by a "register()". It
   is (a bit) more efficient than doing the same explicitly.

devpoll.unregister(fd)

   Elimina un descriptor de archivo que está siendo rastreado por un
   objeto de sondeo. Al igual que el método "register()", *fd* puede
   ser un entero o un objeto con un método "fileno()" que retorna un
   entero.

   Al intentar eliminar un descriptor de archivo que nunca se registró
   se ignora de forma segura.

devpoll.poll([timeout])

   Sondea el conjunto de descriptores de archivos registrados y
   retorna una lista posiblemente vacía que contiene tuplas de dos
   elementos "(fd, event)" para los descriptores que tienen eventos o
   errores para informar. *fd* es el descriptor de archivo, y *event*
   es una máscara de bits con bits configurados para los eventos
   informados para ese descriptor --- "POLLIN" para entrada en espera,
   "POLLOUT" para indicar que se puede escribir en el descriptor, y
   así sucesivamente. Una lista vacía indica que se agotó el tiempo de
   espera de la llamada y que ningún descriptor de archivo tuvo
   eventos para informar. Si se proporciona *timeout*, especifica el
   período de tiempo en milisegundos que el sistema esperará por los
   eventos antes de regresar. Si se omite *timeout*, -1 o "None", la
   llamada se bloqueará hasta que haya un evento para este objeto de
   sondeo.

   Distinto en la versión 3.5: La función ahora se vuelve a intentar
   con un tiempo de espera (*timeout*) recalculado cuando se
   interrumpe por una señal, excepto si el controlador de señal genera
   una excepción (ver **PEP 475** para la justificación), en lugar de
   generar "InterruptedError".

## Edge and level trigger polling (epoll) objects

   https://linux.die.net/man/4/epoll

   The *eventmask* is a bit mask using the following constants:

   +---------------------------+--------------------------------------------------+
   | Constante                 | Significado                                      |
   |===========================|==================================================|
   | "EPOLLIN"                 | Available for read.                              |
   +---------------------------+--------------------------------------------------+
   | "EPOLLOUT"                | Available for write.                             |
   +---------------------------+--------------------------------------------------+
   | "EPOLLPRI"                | Urgent data for read.                            |
   +---------------------------+--------------------------------------------------+
   | "EPOLLERR"                | Error condition happened on the associated fd.   |
   +---------------------------+--------------------------------------------------+
   | "EPOLLHUP"                | Hang up happened on the associated fd.           |
   +---------------------------+--------------------------------------------------+
   | "EPOLLET"                 | Set Edge Trigger behavior, the default is Level  |
   |                           | Trigger behavior.                                |
   +---------------------------+--------------------------------------------------+
   | "EPOLLONESHOT"            | Set one-shot behavior. After one event is pulled |
   |                           | out, the fd is internally disabled.              |
   +---------------------------+--------------------------------------------------+
   | "EPOLLEXCLUSIVE"          | Wake only one epoll object when the associated   |
   |                           | fd has an event. The default (if this flag is    |
   |                           | not set) is to wake all epoll objects polling on |
   |                           | an fd.                                           |
   +---------------------------+--------------------------------------------------+
   | "EPOLLRDHUP"              | Socket de flujo de conexión cerrada por pares o  |
   |                           | apagado escribiendo la mitad de la conexión.     |
   +---------------------------+--------------------------------------------------+
   | "EPOLLRDNORM"             | Equivalente a "EPOLLIN"                          |
   +---------------------------+--------------------------------------------------+
   | "EPOLLRDBAND"             | La banda de datos de prioridad se puede leer.    |
   +---------------------------+--------------------------------------------------+
   | "EPOLLWRNORM"             | Equivalent to "EPOLLOUT".                        |
   +---------------------------+--------------------------------------------------+
   | "EPOLLWRBAND"             | Se pueden escribir datos de prioridad.           |
   +---------------------------+--------------------------------------------------+
   | "EPOLLMSG"                | Ignorado.                                        |
   +---------------------------+--------------------------------------------------+
   | "EPOLLWAKEUP"             | Prevents sleep during event waiting.             |
   +---------------------------+--------------------------------------------------+

   Added in version 3.6: "EPOLLEXCLUSIVE" fue agregado. Solo es
   compatible con Linux Kernel 4.5 o posterior.

   Added in version 3.14: "EPOLLWAKEUP" was added. It's only supported
   by Linux Kernel 3.5 or later.

epoll.close()

   Cierra el descriptor del archivo de control del objeto epoll.

epoll.closed

   "True" si el objeto epoll está cerrado.

epoll.fileno()

   Retorna el número de descriptor de archivo del control fd.

epoll.fromfd(fd)

   Crea un objeto epoll a partir de un descriptor de archivo dado.

epoll.register(fd[, eventmask])

   Register a file descriptor *fd* with the epoll object.

epoll.modify(fd, eventmask)

   Modify a registered file descriptor *fd*.

epoll.unregister(fd)

   Elimina un descriptor de archivo registrado del objeto epoll.

   Distinto en la versión 3.9: El método ya no ignora el error
   "EBADF".

epoll.poll(timeout=None, maxevents=-1)

   Espera los eventos. tiempo de espera (*timeout*) en segundos
   (float)

   Distinto en la versión 3.5: La función ahora se vuelve a intentar
   con un tiempo de espera (*timeout*) recalculado cuando se
   interrumpe por una señal, excepto si el controlador de señal genera
   una excepción (ver **PEP 475** para la justificación), en lugar de
   generar "InterruptedError".

## Polling objects

The "poll()" system call, supported on most Unix systems, provides
better scalability for network servers that service many, many clients
at the same time. "poll()" scales better because the system call only
requires listing the file descriptors of interest, while "select()"
builds a bitmap, turns on bits for the fds of interest, and then
afterward the whole bitmap has to be linearly scanned again.
"select()" is *O*(*highest file descriptor*), while "poll()" is
*O*(*number of file descriptors*).

poll.register(fd[, eventmask])

   Registra un descriptor de archivo con el objeto de sondeo. Las
   futuras llamadas al método "poll()" comprobarán si el descriptor
   del archivo tiene algún evento I/O pendiente. *fd* puede ser un
   entero o un objeto con un método "fileno()" que retorna un entero.
   Los objetos de archivo implementan "Fileno()", por lo que también
   pueden usarse como argumento.

   *eventmask* es una máscara de bits opcional que describe el tipo de
   eventos que se desea verificar y puede ser una combinación de las
   constantes "POLLIN", "POLLPRI", y "POLLOUT", descrito en la mesa de
   abajo. Si no se especifica, el valor predeterminado utilizado
   verificará los 3 tipos de eventos.

   +---------------------+---------------------------------------------+
   | Constante           | Significado                                 |
   |=====================|=============================================|
   | "POLLIN"            | There is data to read.                      |
   +---------------------+---------------------------------------------+
   | "POLLPRI"           | There is urgent data to read.               |
   +---------------------+---------------------------------------------+
   | "POLLOUT"           | Ready for output: writing will not block.   |
   +---------------------+---------------------------------------------+
   | "POLLERR"           | Error condition of some sort.               |
   +---------------------+---------------------------------------------+
   | "POLLHUP"           | Hung up.                                    |
   +---------------------+---------------------------------------------+
   | "POLLRDHUP"         | Stream socket peer closed connection, or    |
   |                     | shut down writing half of connection.       |
   +---------------------+---------------------------------------------+
   | "POLLNVAL"          | Invalid request: descriptor not open.       |
   +---------------------+---------------------------------------------+

   Al registrar un descriptor de archivo que ya está registrado no es
   un error y tiene el mismo efecto que registrar el descriptor
   exactamente una vez.

poll.modify(fd, eventmask)

   Modifica un fd ya registrado. Esto tiene el mismo efecto que
   "register(fd, eventmask)". Si se intenta modificar un descriptor de
   archivo que nunca se registró, se genera una excepción "OSError"
   con *errno* "ENOENT".

poll.unregister(fd)

   Elimina un descriptor de archivo que está siendo rastreado por un
   objeto de sondeo. Al igual que el método "register()", *fd* puede
   ser un entero o un objeto con un método "fileno()" que retorna un
   entero.

   Intenta eliminar un descriptor de archivo que nunca se registró
   provoca una excepción "KeyError".

poll.poll([timeout])

   Sondea el conjunto de descriptores de archivos registrados y
   retorna una lista posiblemente vacía que contiene tuplas de 2
   elementos "(fd, event)" para los descriptores que tienen eventos o
   errores para informar. *fd* es el descriptor de archivo, y *event*
   es una máscara de bits con bits configurados para los eventos
   informados para ese descriptor --- "POLLIN" para entrada en espera,
   "POLLOUT" para indicar que se puede escribir en el descriptor, y
   así sucesivamente. Una lista vacía indica que se agotó el tiempo de
   espera de la llamada y que ningún descriptor de archivo tuvo
   eventos para informar. Si se proporciona *timeout*, especifica el
   período de tiempo en milisegundos que el sistema esperará por los
   eventos antes de regresar. Si se omite *timeout*, es negativo o
   "None", la llamada se bloqueará hasta que haya un evento para este
   objeto de sondeo.

   Distinto en la versión 3.5: La función ahora se vuelve a intentar
   con un tiempo de espera (*timeout*) recalculado cuando se
   interrumpe por una señal, excepto si el controlador de señal genera
   una excepción (ver **PEP 475** para la justificación), en lugar de
   generar "InterruptedError".

## Kqueue objects

kqueue.close()

   Cierra el descriptor del archivo de control del objeto kqueue.

kqueue.closed

   "True" si el objeto *kqueue* está cerrado.

kqueue.fileno()

   Retorna el número de descriptor de archivo del control fd.

kqueue.fromfd(fd)

   Crea un objeto *kqueue* a partir de un descriptor de archivo dado.

kqueue.control(changelist, max_events[, timeout]) -> eventlist

   Interfaz de bajo nivel para kevent

   * la lista de cambios (*changelist*) debe ser iterable de objetos
     kevent o "None"

   * max_events debe ser 0 o un entero positivo

   * tiempo de espera (*timeout*) en segundos (posible con *floats*);
     el valor predeterminado es "None", para esperar para siempre

   Distinto en la versión 3.5: La función ahora se vuelve a intentar
   con un tiempo de espera (*timeout*) recalculado cuando se
   interrumpe por una señal, excepto si el controlador de señal genera
   una excepción (ver **PEP 475** para la justificación), en lugar de
   generar "InterruptedError".

## Kevent objects

https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2

kevent.ident

   Valor utilizado para identificar el evento. La interpretación
   depende del filtro, pero generalmente es el descriptor de archivo.
   En el constructor, ident puede ser un int o un objeto con un método
   "fileno()". kevent almacena el entero internamente.

kevent.filter

   Nombre del filtro del kernel.

   +-----------------------------+-----------------------------------------------+
   | Constante                   | Significado                                   |
   |=============================|===============================================|
   | "KQ_FILTER_READ"            | Takes a descriptor and returns whenever there |
   |                             | is data available to read.                    |
   +-----------------------------+-----------------------------------------------+
   | "KQ_FILTER_WRITE"           | Takes a descriptor and returns whenever there |
   |                             | is data available to write.                   |
   +-----------------------------+-----------------------------------------------+
   | "KQ_FILTER_AIO"             | AIO requests.                                 |
   +-----------------------------+-----------------------------------------------+
   | "KQ_FILTER_VNODE"           | Returns when one or more of the requested     |
   |                             | events watched in *fflag* occurs.             |
   +-----------------------------+-----------------------------------------------+
   | "KQ_FILTER_PROC"            | Watch for events on a process ID.             |
   +-----------------------------+-----------------------------------------------+
   | "KQ_FILTER_NETDEV"          | Watch for events on a network device (not     |
   |                             | available on macOS).                          |
   +-----------------------------+-----------------------------------------------+
   | "KQ_FILTER_SIGNAL"          | Returns whenever the watched signal is        |
   |                             | delivered to the process.                     |
   +-----------------------------+-----------------------------------------------+
   | "KQ_FILTER_TIMER"           | Establishes an arbitrary timer.               |
   +-----------------------------+-----------------------------------------------+

kevent.flags

   Acción de filtro.

   +-----------------------------+------------------------------------------------+
   | Constante                   | Significado                                    |
   |=============================|================================================|
   | "KQ_EV_ADD"                 | Adds or modifies an event.                     |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_DELETE"              | Removes an event from the queue.               |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_ENABLE"              | Permits control() to return the event.         |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_DISABLE"             | Disables event.                                |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_ONESHOT"             | Removes event after first occurrence.          |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_CLEAR"               | Reset the state after an event is retrieved.   |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_SYSFLAGS"            | Internal event.                                |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_FLAG1"               | Internal event.                                |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_EOF"                 | Filter-specific EOF condition.                 |
   +-----------------------------+------------------------------------------------+
   | "KQ_EV_ERROR"               | See return values.                             |
   +-----------------------------+------------------------------------------------+

kevent.fflags

   Filter-specific flags.

   "KQ_FILTER_READ" y "KQ_FILTER_WRITE" bandera de filtro:

   +------------------------------+----------------------------------------------+
   | Constante                    | Significado                                  |
   |==============================|==============================================|
   | "KQ_NOTE_LOWAT"              | Low water mark of a socket buffer.           |
   +------------------------------+----------------------------------------------+

   "KQ_FILTER_VNODE" bandera de filtro:

   +------------------------------+----------------------------------------------+
   | Constante                    | Significado                                  |
   |==============================|==============================================|
   | "KQ_NOTE_DELETE"             | *unlink()* was called.                       |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_WRITE"              | A write occurred.                            |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_EXTEND"             | The file was extended.                       |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_ATTRIB"             | An attribute was changed.                    |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_LINK"               | The link count has changed.                  |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_RENAME"             | The file was renamed.                        |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_REVOKE"             | Access to the file was revoked.              |
   +------------------------------+----------------------------------------------+

   "KQ_FILTER_PROC" bandera de filtro:

   +------------------------------+----------------------------------------------+
   | Constante                    | Significado                                  |
   |==============================|==============================================|
   | "KQ_NOTE_EXIT"               | The process has exited.                      |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_FORK"               | The process has called *fork()*.             |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_EXEC"               | The process has executed a new process.      |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_PCTRLMASK"          | Internal filter flag.                        |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_PDATAMASK"          | Internal filter flag.                        |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_TRACK"              | Follow a process across *fork()*.            |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_CHILD"              | Returned on the child process for            |
   |                              | *NOTE_TRACK*.                                |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_TRACKERR"           | Unable to attach to a child.                 |
   +------------------------------+----------------------------------------------+

   Indicadores de filtro "KQ_FILTER_NETDEV" (no disponible en macOS):

   +------------------------------+----------------------------------------------+
   | Constante                    | Significado                                  |
   |==============================|==============================================|
   | "KQ_NOTE_LINKUP"             | Link is up.                                  |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_LINKDOWN"           | Link is down.                                |
   +------------------------------+----------------------------------------------+
   | "KQ_NOTE_LINKINV"            | Link state is invalid.                       |
   +------------------------------+----------------------------------------------+

kevent.data

   Filter-specific data.

kevent.udata

   User-defined value.
