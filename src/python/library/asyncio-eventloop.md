---
title: Event loop
source_url: https://docs.python.org/es/3
source_path: library/asyncio-eventloop.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1600
---

# Event loop

**Código fuente:** Lib/asyncio/events.py, Lib/asyncio/base_events.py

======================================================================

-[ Prólogo ]-

El bucle de eventos es el núcleo de cada aplicación asyncio. Los
bucles de eventos ejecutan tareas asíncronas y llamadas de retorno,
realizan operaciones de E/S de red y ejecutan subprocesos.

Los desarrolladores de aplicaciones normalmente deberían usar las
funciones asyncio de alto nivel, como: "asyncio.run()", y rara vez
deberían necesitar hacer referencia al objeto de bucle o llamar a sus
métodos. Esta sección esta dirigida principalmente a autores de código
de nivel inferior, bibliotecas y frameworks, quienes necesitan un
control mas preciso sobre el comportamiento del bucle de eventos.

-[ Obtención del bucle de eventos ]-

Las siguientes funciones de bajo nivel se pueden utilizar para
obtener, establecer o crear un bucle de eventos:

asyncio.get_running_loop()

   Retorna el bucle de eventos en ejecución en el hilo del sistema
   operativo actual.

   Raise a "RuntimeError" if there is no running event loop.

   This function can only be called from a coroutine or a callback.

   Added in version 3.7.

asyncio.get_event_loop()

   Obtiene bucle de eventos actual.

   When called from a coroutine or a callback (e.g. scheduled with
   call_soon or similar API), this function will always return the
   running event loop.

   If there is no running event loop set, the function will return the
   result of the "get_event_loop_policy().get_event_loop()" call.

   Dado que esta función tiene un comportamiento bastante complejo
   (especialmente cuando están en uso las políticas de bucle de
   eventos personalizadas), usar la función "get_running_loop()" es
   preferible antes que "get_event_loop()" en corrutinas y llamadas de
   retorno.

   As noted above, consider using the higher-level "asyncio.run()"
   function, instead of using these lower level functions to manually
   create and close an event loop.

   Distinto en la versión 3.14: Raises a "RuntimeError" if there is no
   current event loop.

   Nota:

     The "asyncio" policy system is deprecated and will be removed in
     Python 3.16; from there on, this function will return the current
     running event loop if present else it will return the loop set by
     "set_event_loop()".

asyncio.set_event_loop(loop)

   Set *loop* as the current event loop for the current OS thread.

asyncio.new_event_loop()

   Crea y retorna un nuevo objeto de bucle de eventos.

Tenga en cuenta que el comportamiento de las funciones
"get_event_loop()", "set_event_loop()", y "new_event_loop()" puede ser
modificado mediante estableciendo una política de bucle de eventos
personalizada.

-[ Contenidos ]-

Esta página de documentación contiene las siguientes secciones:

* La sección Métodos del bucle de eventos es la documentación de
  referencia de las APIs del bucle de eventos;

* La sección Callback Handles documenta las instancias "Handle" y
  "TimerHandle" las cuales son retornadas por métodos planificados
  como "loop.call_soon()" y "loop.call_later()";

* La sección Objetos del servidor documenta tipos retornados por los
  métodos del bucle de eventos como "loop.create_server()";

* La sección Implementaciones de bucle de eventos documenta las clases
  "SelectorEventLoop" y "ProactorEventLoop";

* La sección Ejemplos muestra como trabajar con algunas APIs de bucle
  de eventos.

## Event loop methods

Los bucles de eventos tienen APIs de **bajo nivel** para lo siguiente:

* Iniciar y para el bucle

* Programación de llamadas de retorno

* Planificando llamadas retardadas

* Creating futures and tasks

* Abriendo conexiones de red

* Creando servidores de red

* Transfiriendo archivos

* TLS upgrade

* Viendo descriptores de archivos

* Trabajar con objetos sockets directamente

* DNS

* Trabajando con tuberías

* Señales Unix

* Ejecutando código en un hilos o grupos de procesos

* Error handling API

* Habilitando el modo depuración

* Running subprocesses

### Iniciar y para el bucle

loop.run_until_complete(future)

   Se ejecuta hasta que *future* (una instancia de "Future") se haya
   completado.

   Si el argumento es un objeto corrutina está implícitamente
   planificado para ejecutarse como una "asyncio.Task".

   Retorna el resultado del Futuro o genera una excepción.

loop.run_forever()

   Ejecuta el bucle de eventos hasta que "stop()" es llamado.

   If "stop()" is called before "run_forever()" is called, the loop
   will poll the I/O selector once with a timeout of zero, run all
   callbacks scheduled in response to I/O events (and those that were
   already scheduled), and then exit.

   Si "stop()" es llamado mientras "run_forever()" se está ejecutando,
   el loop ejecutará el lote actual de llamadas y después finalizará.
   Tenga en cuenta que llamadas planificadas por otras llamadas no se
   ejecutarán en este caso; en su lugar, ellas correrán la próxima vez
   que "run_forever()" o "run_until_complete()" sean llamados.

loop.stop()

   Detener el bucle de eventos.

loop.is_running()

   Retorna "True" si el bucle de eventos esta en ejecución
   actualmente.

loop.is_closed()

   Retorna "True" si el bucle de eventos se cerró.

loop.close()

   Cierra el bucle de eventos.

   El bucle no debe estar en ejecución cuando se llama a esta función.
   Cualquier llamada de retorno pendiente será descartada.

   Este método limpia todas las colas y apaga el ejecutor, pero no
   espera a que el ejecutor termine.

   Este método es idempotente e irreversible. No se debe llamar ningún
   otro método después que el bucle de eventos es cerrado.

async loop.shutdown_asyncgens()

   Schedule all currently open *asynchronous generator* objects to
   close with an "aclose()" call.  After calling this method, the
   event loop will issue a warning if a new asynchronous generator is
   iterated. This should be used to reliably finalize all scheduled
   asynchronous generators.

   Tenga en cuenta que no hay necesidad de llamar esta función cuando
   "asyncio.run()" es utilizado.

   Ejemplo:

      try:
          loop.run_forever()
      finally:
          loop.run_until_complete(loop.shutdown_asyncgens())
          loop.close()

   Added in version 3.6.

async loop.shutdown_default_executor(timeout=None)

   Schedule the closure of the default executor and wait for it to
   join all of the threads in the "ThreadPoolExecutor". Once this
   method has been called, using the default executor with
   "loop.run_in_executor()" will raise a "RuntimeError".

   The *timeout* parameter specifies the amount of time (in "float"
   seconds) the executor will be given to finish joining. With the
   default, "None", the executor is allowed an unlimited amount of
   time.

   If the *timeout* is reached, a "RuntimeWarning" is emitted and the
   default executor is terminated without waiting for its threads to
   finish joining.

   Nota:

     Do not call this method when using "asyncio.run()", as the latter
     handles default executor shutdown automatically.

   Added in version 3.9.

   Distinto en la versión 3.12: Added the *timeout* parameter.

### Programación de llamadas de retorno

loop.call_soon(callback, *args, context=None)

   Programa el *callback* (retrollamada) *callback* para que se llame
   con argumentos *args* en la próxima iteración del ciclo de eventos.

   Return an instance of "asyncio.Handle", which can be used later to
   cancel the callback.

   Llamadas que son ejecutadas en el orden en el que fueron
   registradas. Cada llamada será ejecutada exactamente una sola vez.

   The optional keyword-only *context* argument specifies a custom
   "contextvars.Context" for the *callback* to run in. Callbacks use
   the current context when no *context* is provided.

   Unlike "call_soon_threadsafe()", this method is not thread-safe.

loop.call_soon_threadsafe(callback, *args, context=None)

   A thread-safe variant of "call_soon()". When scheduling callbacks
   from another thread, this function *must* be used, since
   "call_soon()" is not thread-safe.

   This function is safe to be called from a reentrant context or
   signal handler, however, it is not safe or fruitful to use the
   returned handle in such contexts.

   Lanza "RuntimeError" si se llama en un bucle que ha sido cerrado.
   Esto puede suceder en un hilo secundario cuando la aplicación
   principal se está apagando.

   Vea sección concurrencia y multiproceso de la documentación.

   Distinto en la versión 3.7: Fue agregado el parámetro solo de
   palabra clave *context*. Vea **PEP 567** para mas detalles.

Nota:

  La mayoría de las funciones planificadas de "asyncio" no permiten
  pasar argumentos de palabra clave. Para hacer eso utilice
  "functools.partial()":

     # will schedule "print("Hello", flush=True)"
     loop.call_soon(
         functools.partial(print, "Hello", flush=True))

  El uso de objetos parciales es usualmente mas conveniente que
  utilizar lambdas, ya que asyncio puede renderizar mejor objetos
  parciales en mensajes de depuración y error.

### Planificando llamadas retardadas

El bucle de eventos provee mecanismos para planificar funciones de
llamadas que serán ejecutadas en algún punto en el futuro. El bucle de
eventos usa relojes monotónicos para seguir el tiempo.

loop.call_later(delay, callback, *args, context=None)

   Planifica *callback* para ser ejecutada luego de *delay* número de
   segundos (puede ser tanto un entero como un flotante).

   Una instancia de "asyncio.TimerHandle" es retornada, la que puede
   ser utilizada para cancelar la ejecución.

   *callback* será ejecutada exactamente una sola vez. Si dos llamadas
   son planificadas para el mismo momento exacto, el orden en el que
   son ejecutadas es indefinido.

   The optional positional *args* will be passed to the callback when
   it is called. Use "functools.partial()" to pass keyword arguments
   to *callback*.

   Un argumento *context* opcional y solo de palabra clave que permite
   especificar una clase "contextvars.Context" personalizada en la
   cual *callback* será ejecutada. Cuando no se provee *context* el
   contexto actual es utilizado.

   Nota:

     For performance, callbacks scheduled with "loop.call_later()" may
     run up to one clock-resolution early (see
     "time.get_clock_info('monotonic').resolution").

   Distinto en la versión 3.7: Fue agregado el parámetro solo de
   palabra clave *context*. Vea **PEP 567** para mas detalles.

   Distinto en la versión 3.8: En Python 3.7 y versiones anteriores
   con la implementación del bucle de eventos predeterminada, el
   *delay* no puede exceder un día. Esto fue arreglado en Python 3.8.

loop.call_at(when, callback, *args, context=None)

   Planifica *callback* para ser ejecutada en una marca de tiempo
   absoluta *when* (un entero o un flotante), usando la misma
   referencia de tiempo que "loop.time()".

   El comportamiento de este método es el mismo que "call_later()".

   Una instancia de "asyncio.TimerHandle" es retornada, la que puede
   ser utilizada para cancelar la ejecución.

   Nota:

     For performance, callbacks scheduled with "loop.call_at()" may
     run up to one clock-resolution early (see
     "time.get_clock_info('monotonic').resolution").

   Distinto en la versión 3.7: Fue agregado el parámetro solo de
   palabra clave *context*. Vea **PEP 567** para mas detalles.

   Distinto en la versión 3.8: En Python 3.7 y versiones anteriores
   con la implementación del bucle de eventos predeterminada, la
   diferencia entre *when* y el tiempo actual no puede exceder un día.
   Esto fue arreglado en Python 3.8.

loop.time()

   Retorna el tiempo actual, como un "float", de acuerdo al reloj
   monotónico interno del bucle de evento.

Nota:

  Distinto en la versión 3.8: En Python 3.7 y versiones anteriores los
  tiempos de espera (*delay* relativo o *when* absoluto) no deben
  exceder un día. Esto fue arreglado en Python 3.8.

Ver también: La función "asyncio.sleep()".

### Creating futures and tasks

loop.create_future()

   Crea un objeto "asyncio.Future" adjunto al bucle de eventos.

   Esta es la manera preferida de crear Futures en asyncio. Esto
   permite que bucles de eventos de terceros provean implementaciones
   alternativas del objeto Future (con mejor rendimiento o
   instrumentación).

   Added in version 3.5.2.

loop.create_task(coro, *, name=None, context=None, eager_start=None, **kwargs)

   Planifica la ejecución de la corrutina *coro*. Retorna un objeto
   "Task".

   Bucles de eventos de terceros pueden usar sus propias subclases de
   "Task" por interoperabilidad. En este caso, el tipo de resultado es
   una subclase de "Task".

   The full function signature is largely the same as that of the
   "Task" constructor (or factory) - all of the keyword arguments to
   this function are passed through to that interface.

   Si el argumento *name* es provisto y no "None", se establece como
   el nombre de la tarea usando "Task.set_name()".

   Un argumento opcional y solo de palabra clave *context* que permite
   especificar una clase "contextvars.Context" personalizada en la
   cual *coro* será ejecutada. Cuando no se provee *context* el
   contexto actual es utilizado.

   An optional keyword-only *eager_start* argument allows specifying
   if the task should execute eagerly during the call to create_task,
   or be scheduled later. If *eager_start* is not passed the mode set
   by "loop.set_task_factory()" will be used.

   Distinto en la versión 3.8: Agregado el parámetro *name*.

   Distinto en la versión 3.11: Agregado el parámetro *context*.

   Distinto en la versión 3.13.3: Added "kwargs" which passes on
   arbitrary extra parameters, including  "name" and "context".

   Distinto en la versión 3.13.4: Rolled back the change that passes
   on *name* and *context* (if it is None), while still passing on
   other arbitrary keyword arguments (to avoid breaking backwards
   compatibility with 3.13.3).

   Distinto en la versión 3.14: All *kwargs* are now passed on. The
   *eager_start* parameter works with eager task factories.

loop.set_task_factory(factory)

   Establece una fábrica de tareas que será utilizada por
   "loop.create_task()".

   If *factory* is "None" the default task factory will be set.
   Otherwise, *factory* must be a *callable* with the signature
   matching "(loop, coro, **kwargs)", where *loop* is a reference to
   the active event loop, and *coro* is a coroutine object.  The
   callable must pass on all *kwargs*, and return a
   "asyncio.Task"-compatible object.

   Distinto en la versión 3.13.3: Required that all *kwargs* are
   passed on to "asyncio.Task".

   Distinto en la versión 3.13.4: *name* is no longer passed to task
   factories. *context* is no longer passed to task factories if it is
   "None".

   Distinto en la versión 3.14: *name* and *context* are now
   unconditionally passed on to task factories again.

loop.get_task_factory()

   Retorna una fábrica de tareas o "None" si la predefinida está en
   uso.

### Abriendo conexiones de red

async loop.create_connection(protocol_factory, host=None, port=None, *, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, happy_eyeballs_delay=None, interleave=None, all_errors=False)

   Abre una conexión de transmisión de transporte a una dirección
   especificada por *host* y *port*.

   The socket family can be either "AF_INET" or "AF_INET6" depending
   on *host* (or the *family* argument, if provided).

   The socket type will be "SOCK_STREAM".

   *protocol_factory* debe ser un ejecutable que retorna una
   implementación del asyncio protocol.

   Este método tratará de establecer la conexión en un segundo plano.
   Cuando es exitosa, retorna un par "(transport, protocol)".

   La sinopsis cronológica de las operaciones subyacentes es como
   sigue:

   1. La conexión es establecida y un transporte es creado para ello.

   2. *protocol_factory* es llamado sin argumentos y se espera que
      retorne una instancia de protocol.

   3. La instancia del protocolo se acopla con el transporte mediante
      el llamado de su método "connection_made()".

   4. Una tupla "(transport, protocol)" es retornada cuando se tiene
      éxito.

   El transporte creado es una transmisión (*stream*) bidireccional
   que depende de la implementación.

   Otros argumentos:

   * *ssl*: si se provee y no es falso, un transporte SSL/TLS es
     creado (de manera predeterminada se crea un transporte TCP
     plano).  Si *ssl* es un objeto "ssl.SSLContext", este contexto es
     utilizado para crear el transporte; si *ssl* es "True", se
     utiliza un contexto predeterminado retornado por
     "ssl.create_default_context()".

     Ver también: Consideraciones de seguridad SSL/TLS

   * *server_hostname* establece o reemplaza el nombre de servidor
     (*hostname*) contra el cual el certificado del servidor de
     destino será comparado. Sólo debería ser pasado si *ssl* no es
     "None". De manera predeterminada es usado el valor del argumento
     *host*.  Si *host* está vacío, no hay valor predeterminado y
     debes pasar un valor para *server_hostname*. Si *server_hostname*
     es una cadena vacía, la comparación de nombres de servidores es
     deshabilitada (lo que es un riesgo de seguridad serio,
     permitiendo potenciales ataques de hombre-en-el-medio, *man-in-
     the-middle attacks*).

   * *family*, *proto*, *flags* son dirección de familia, protocolo y
     banderas opcionales que serán pasadas a través de *getaddrinfo()*
     para la resolución de *host*. Si están dados, todos ellos
     deberían ser enteros de las constantes del módulo "socket"
     correspondiente.

   * *happy_eyeballs_delay*, si se proporciona, habilita Happy
     Eyeballs para esta conexión. Debe ser un número de punto flotante
     que represente la cantidad de tiempo en segundos para esperar a
     que se complete un intento de conexión, antes de comenzar el
     siguiente intento en paralelo. Este es el "Retraso de intento de
     conexión" como se define en **RFC 8305**. Un valor predeterminado
     sensato recomendado por el RFC es "0.25" (250 milisegundos).

   * *interleave* controla reordenamientos de dirección cuando un
     nombre de servidor resuelve a múltiples direcciones IP. Si es "0"
     o no es especificado, no se hace ningún reordenamiento, y las
     direcciones son intentadas en el orden retornado por
     "getaddrinfo()". Si un entero positivo es especificado, las
     direcciones son intercaladas por dirección de familia, y el
     entero dado es interpretado como "Número de familias de la
     primera dirección" (*First Address Family Count*) como es
     definida en **RFC 8305**. El valor predefinido es "0" si
     *happy_eyeballs_delay* no es especificado, y "1" si lo es.

   * *sock*, si está dado, debe ser un objeto "socket.socket"
     existente y ya conectado, que será utilizado por el transporte.
     Si *sock* es dado, ningún *host*, *port*, *family*, *proto*,
     *flags*, *happy_eyeballs_delay*, *interleave* o *local_addr*
     deben ser especificados.

     Nota:

       El argumento *sock* transfiere la propiedad del socket al
       transporte creado. Para cerrar el socket, llame al método
       "close()" del transporte.

   * *local_addr*, si está dado, es una tupla "(local_host,
     local_port)" usada para enlazar el socket localmente.  Los
     *local_host* y *local_port* son buscados usando "getaddrinfo()",
     de manera similar que con *host* y *port*.

   * *ssl_handshake_timeout* es (para una conexión TLS) el tiempo en
     segundos a esperar que se complete el *handshake* TLS antes de
     abortar la conexión. "60.0" segundos si es "None" (predefinido).

   * *ssl_shutdown_timeout* es el tiempo en segundos a esperar a que
     se complete el apagado SSL antes de abortar la conexión. "30.0"
     segundos si es "None" (predefinido).

   * *all_errors* determines what exceptions are raised when a
     connection cannot be created. By default, only a single
     "Exception" is raised: the first exception if there is only one
     or all errors have same message, or a single "OSError" with the
     error messages combined. When "all_errors" is "True", an
     "ExceptionGroup" will be raised containing all exceptions (even
     if there is only one).

   Distinto en la versión 3.5: Agregado el soporte para SSL/TLS en
   "ProactorEventLoop".

   Distinto en la versión 3.6: The socket option socket.TCP_NODELAY is
   set by default for all TCP connections.

   Distinto en la versión 3.7: Agregado el parámetro
   *ssl_handshake_timeout*.

   Distinto en la versión 3.8: Agregados los parámetros
   *happy_eyeballs_delay* y *interleave*.Happy Eyeballs Algorithm:
   Success with Dual-Stack Hosts. When a server's IPv4 path and
   protocol are working, but the server's IPv6 path and protocol are
   not working, a dual-stack client application experiences
   significant connection delay compared to an IPv4-only client.  This
   is undesirable because it causes the dual-stack client to have a
   worse user experience.  This document specifies requirements for
   algorithms that reduce this user-visible delay and provides an
   algorithm.For more information:
   https://datatracker.ietf.org/doc/html/rfc6555

   Distinto en la versión 3.11: Agregado el parámetro
   *ssl_shutdown_timeout*.

   Distinto en la versión 3.12: *all_errors* was added.

   Ver también:

     La función "open_connection()" es una API alternativa de alto
     nivel. Retorna un par de ("StreamReader", "StreamWriter") que
     puede ser usado directamente en código async/await.

async loop.create_datagram_endpoint(protocol_factory, local_addr=None, remote_addr=None, *, family=0, proto=0, flags=0, reuse_port=None, allow_broadcast=None, sock=None)

   Crea un datagrama de conexión.

   The socket family can be either "AF_INET", "AF_INET6", or
   "AF_UNIX", depending on *host* (or the *family* argument, if
   provided).

   The socket type will be "SOCK_DGRAM".

   *protocol_factory* debe ser un ejecutable que retorne una
   implementación de protocol.

   Una tupla de "(transport, protocol)" es retornada cuando se tiene
   éxito.

   Otros argumentos:

   * *local_addr*, si está dado, es una tupla "(local_host,
     local_port)" usada para enlazar el socket localmente.  Los
     *local_host* y *local_port* son buscados utilizando
     "getaddrinfo()".

     Nota:

       On Windows, when using the proactor event loop with
       "local_addr=None", an "OSError" with "errno.WSAEINVAL" will be
       raised when running it.

   * *remote_addr*, si está dado, es una tupla "(remote_host,
     remote_port)" utilizada para conectar el socket a una dirección
     remota. Los *remote_host* y *remote_port* son buscados utilizando
     "getaddrinfo()".

   * *family*, *proto*, *flags* son direcciones de familia, protocolo
     y banderas opcionales que serán pasadas a través de
     "getaddrinfo()" para la resolución de *host*. Si está dado, estos
     deben ser todos enteros de las constantes del módulo "socket"
     correspondiente.

   * *reuse_port* tells the kernel to allow this endpoint to be bound
     to the same port as other existing endpoints are bound to, so
     long as they all set this flag when being created. This option is
     not supported on Windows and some Unixes. If the
     socket.SO_REUSEPORT constant is not defined then this capability
     is unsupported.

   * *allow_broadcast* dice al kernel que habilite este punto de
     conexión para enviar mensajes a la dirección de transmisión
     (*broadcast*).

   * *sock* puede opcionalmente ser especificado para usar un objeto
     "socket.socket" preexistente y ya conectado que será utilizado
     por el transporte. Si están especificados, *local_addr* y
     *remote_addr* deben ser omitidos (tienen que ser "None").

     Nota:

       El argumento *sock* transfiere la propiedad del socket al
       transporte creado. Para cerrar el socket, llame al método
       "close()" del transporte.

   Refiérase a los ejemplos UDP echo client protocol y UDP echo server
   protocol.

   Distinto en la versión 3.4.4: Los parámetros *family*, *proto*,
   *flags*, *reuse_address*, *reuse_port*, *allow_broadcast* y *sock*
   fueron agregados.

   Distinto en la versión 3.8: Se agregó soporte para Windows.

   Distinto en la versión 3.8.1: The *reuse_address* parameter is no
   longer supported, as using socket.SO_REUSEADDR poses a significant
   security concern for UDP. Explicitly passing "reuse_address=True"
   will raise an exception.Cuando múltiples procesos con UIDs
   diferentes asignan sockets a una misma dirección socket UDP con
   "SO_REUSEADDR", los paquetes entrantes pueden distribuirse
   aleatoriamente entre los sockets.For supported platforms,
   *reuse_port* can be used as a replacement for similar
   functionality. With *reuse_port*, socket.SO_REUSEPORT is used
   instead, which specifically prevents processes with differing UIDs
   from assigning sockets to the same socket address.

   Distinto en la versión 3.11: The *reuse_address* parameter,
   disabled since Python 3.8.1, 3.7.6 and 3.6.10, has been entirely
   removed.

async loop.create_unix_connection(protocol_factory, path=None, *, ssl=None, sock=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)

   Crear una conexión Unix.

   The socket family will be "AF_UNIX"; socket type will be
   "SOCK_STREAM".

   Una tupla de "(transport, protocol)" es retornada cuando se tiene
   éxito.

   *path* es el nombre de un dominio de un socket Unix y es requerido,
   a menos que un parámetro *sock* sea especificado. Los socket Unix
   abstractos, "str", "bytes", y "Path" son soportados.

   Vea la documentación del método "loop.create_connection()" para
   información acerca de los argumentos de este método.

   Availability: Unix.

   Distinto en la versión 3.7: Agregado el parámetro
   *ssl_handshake_timeout*. El parámetro *path* ahora puede ser un
   *path-like object*.

   Distinto en la versión 3.11: Agregado el parámetro
   *ssl_shutdown_timeout*.

### Creando servidores de red

async loop.create_server(protocol_factory, host=None, port=None, *, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, keep_alive=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)

   Create a TCP server (socket type "SOCK_STREAM") listening on *port*
   of the *host* address.

   Retorna un objeto "Server".

   Argumentos:

   * *protocol_factory* debe ser un ejecutable que retorne una
     implementación de protocol.

   * El parámetro *host* puede ser establecido a distintos tipos que
     determinan donde el servidor estaría escuchando:

     * Si *host* es una cadena, el servidor TCP está enlazado a una
       sola interfaz de red especificada por *host*.

     * Si *host* es una secuencia de cadenas, el servidor TCP está
       enlazado a todas las interfaces de red especificadas por la
       secuencia.

     * Si *host* es una cadena vacía o "None", se asumen todas las
       interfaces y una lista con múltiples sockets será retornada
       (mas probablemente uno para IPv4 y otro para IPv6).

   * El parámetro *port* puede establecerse para especificar en qué
     puerto debe escuchar el servidor. Si es "0" o "None" (por
     defecto), se seleccionará un puerto aleatorio no utilizado (tenga
     en cuenta que si *host* resuelve a múltiples interfaces de red,
     se seleccionará un puerto aleatorio diferente para cada
     interfaz).

   * *family* can be set to either "socket.AF_INET" or "AF_INET6" to
     force the socket to use IPv4 or IPv6. If not set, the *family*
     will be determined from host name (defaults to "AF_UNSPEC").

   * *flags* es una máscara de bits para "getaddrinfo()".

   * *sock* puede ser especificado opcionalmente para usar objetos
     socket preexistentes. Si se utiliza, entonces *host* y *port* no
     deben ser especificados.

     Nota:

       El argumento *sock* transfiere la propiedad del socket al
       servidor creado. Para cerrar el socket, llame al método
       "close()" del servidor.

   * *backlog* es el número máximo de conexiones encoladas pasadas a
     "listen()" (el valor predeterminado es 100).

   * *ssl* puede ser establecido como una instancia de "SSLContext"
     para habilitar TLS sobre las conexiones aceptadas.

   * *reuse_address* indica al kernel que reutilice un socket local en
     estado "TIME_WAIT", sin esperar que su plazo de ejecución expire.
     Si no es especificado será establecido automáticamente como
     "True" en Unix.

   * *reuse_port* dice al kernel que habilite este punto de conexión
     para ser unido al mismo puerto de la misma forma que otros puntos
     de conexión existentes también están unidos, siempre y cuando
     todos ellos establezcan esta bandera al ser creados.

   * *keep_alive* set to "True" keeps connections active by enabling
     the periodic transmission of messages.

   Distinto en la versión 3.13: Added the *keep_alive* parameter.

   * *ssl_handshake_timeout* es (para un servidor TLS) el tiempo en
     segundos a esperar por el apretón de manos (*handshake*) TLS a
     ser completado antes de abortar la conexión. "60.0" si es "None"
     (su valor predeterminado).

   * *ssl_shutdown_timeout* es el tiempo en segundos a esperar a que
     se complete el apagado SSL antes de abortar la conexión. "30.0"
     segundos si es "None" (predefinido).

   * *start_serving* establecido como "True" (de manera
     predeterminada) produce que los servidores creados comiencen a
     aceptar conexiones inmediatamente. Si es establecido como
     "False", el usuario debe esperar por "Server.start_serving()" o
     "Server.serve_forever()" para que el servidor comience a aceptar
     conexiones.

   Distinto en la versión 3.5: Agregado el soporte para SSL/TLS en
   "ProactorEventLoop".

   Distinto en la versión 3.5.1: El parámetro *host* puede ser una
   secuencia de cadenas.

   Distinto en la versión 3.6: Added *ssl_handshake_timeout* and
   *start_serving* parameters. The socket option socket.TCP_NODELAY is
   set by default for all TCP connections.

   Distinto en la versión 3.11: Agregado el parámetro
   *ssl_shutdown_timeout*.

   Ver también:

     La función "start_server()" es una API alternativa de alto nivel
     que retorna un par de "StreamReader" y "StreamWriter" que pueden
     ser usados en código async/await.

async loop.create_unix_server(protocol_factory, path=None, *, sock=None, backlog=100, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True, cleanup_socket=True)

   Similar to "loop.create_server()" but works with the "AF_UNIX"
   socket family.

   *path* es el nombre de un dominio de socket Unix, y es requerido a
   menos que el argumento *sock* sea provisto. Son soportados sockets
   unix abstractos, "str", "bytes", y rutas "Path".

   If *cleanup_socket* is true then the Unix socket will automatically
   be removed from the filesystem when the server is closed, unless
   the socket has been replaced after the server has been created.

   Vea la documentación de el método "loop.create_server()" para mas
   información acerca de los argumentos de este método.

   Availability: Unix.

   Distinto en la versión 3.7: Agregados los parámetros
   *ssl_handshake_timeout* y *start_serving*. El parámetro *path*
   ahora puede ser un objeto "Path".

   Distinto en la versión 3.11: Agregado el parámetro
   *ssl_shutdown_timeout*.

   Distinto en la versión 3.13: Added the *cleanup_socket* parameter.

async loop.connect_accepted_socket(protocol_factory, sock, *, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)

   Envuelve una conexión ya aceptada en un par de
   transporte/protocolo.

   Este método puede ser usado por servidores que acepten conexiones
   por fuera de asyncio, pero que usen asyncio para manejarlas.

   Parámetros:

   * *protocol_factory* debe ser un ejecutable que retorne una
     implementación de protocol.

   * *sock* es un objeto socket preexistente retornado por
     "socket.accept".

     Nota:

       El argumento *sock* transfiere la propiedad del socket al
       transporte creado. Para cerrar el socket, llame al método
       "close()" del transporte.

   * *ssl* puede ser establecido como un "SSLContext" para habilitar
     SSL sobre las conexiones aceptadas.

   * *ssl_handshake_timeout* es (para una conexión SSL) el tiempo en
     segundos que se esperará para que se complete el apretón de manos
     (*handshake*) SSL antes de abortar la conexión. "60.0" si es
     "None" (su valor predeterminado).

   * *ssl_shutdown_timeout* es el tiempo en segundos a esperar a que
     se complete el apagado SSL antes de abortar la conexión. "30.0"
     segundos si es "None" (predefinido).

   Retorna un par "(transport, protocol)".

   Added in version 3.5.3.

   Distinto en la versión 3.7: Agregado el parámetro
   *ssl_handshake_timeout*.

   Distinto en la versión 3.11: Agregado el parámetro
   *ssl_shutdown_timeout*.

### Transfiriendo archivos

async loop.sendfile(transport, file, offset=0, count=None, *, fallback=True)

   Envía un *file* a través de un *transport*. Retorna el numero total
   de bytes enviados.

   El método usa "os.sendfile()" de alto rendimiento si está
   disponible.

   *file* debe ser un objeto de archivo regular abierto en modo
   binario.

   *offset* indica desde donde se empezará a leer el archivo. Si es
   especificado, *count* es el número total de bytes a transmitir en
   contraposición con enviar el archivo hasta que se alcance EOF. La
   posición del archivo es actualizada siempre, incluso cuando este
   método genere un error, y "file.tell()" puede ser usado para
   obtener el número de bytes enviados hasta el momento.

   *fallback* establecido como "True" hace que asyncio lea y envíe el
   archivo manualmente cuando la plataforma no soporta la llamada de
   envío de archivos del sistema (por ejemplo, Windows o sockets SSL
   en Unix).

   Lanza "SendfileNotAvailableError" si el sistema no soporta la
   llamada de envío de archivos del sistema y *fallback* es "True".

   Added in version 3.7.

### TLS upgrade

async loop.start_tls(transport, protocol, sslcontext, *, server_side=False, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)

   Actualiza una conexión basada en transporte ya existente a TLS.

   Create a TLS coder/decoder instance and insert it between the
   *transport* and the *protocol*. The coder/decoder implements both
   *transport*-facing protocol and *protocol*-facing transport.

   Return the created two-interface instance. After *await*, the
   *protocol* must stop using the original *transport* and communicate
   with the returned object only because the coder caches
   *protocol*-side data and sporadically exchanges extra TLS session
   packets with *transport*.

   In some situations (e.g. when the passed transport is already
   closing) this may return "None".

   Parámetros:

   * Las instancias *transport* y *protocol* que retornan los métodos
     como "create_server()" y "create_connection()".

   * *sslcontext*: una instancia configurada de "SSLContext".

   * *server_side* pasa *True* cuando se actualiza una conexión del
     lado del servidor (como en el caso de una creada por
     "create_server()").

   * *server_hostname*: establece o reemplaza el nombre del host
     contra el cual se compara el certificado del servidor de destino.

   * *ssl_handshake_timeout* es (para una conexión TLS) el tiempo en
     segundos a esperar que se complete el *handshake* TLS antes de
     abortar la conexión. "60.0" segundos si es "None" (predefinido).

   * *ssl_shutdown_timeout* es el tiempo en segundos a esperar a que
     se complete el apagado SSL antes de abortar la conexión. "30.0"
     segundos si es "None" (predefinido).

   Added in version 3.7.

   Distinto en la versión 3.11: Agregado el parámetro
   *ssl_shutdown_timeout*.

### Viendo descriptores de archivos

loop.add_reader(fd, callback, *args)

   Empieza a monitorear el descriptor de archivos *fd* para
   disponibilidad de lectura e invoca *callback* con los argumentos
   especificados una vez que *fd* está habilitado para ser leído.

   Any preexisting callback registered for *fd* is cancelled and
   replaced by *callback*.

loop.remove_reader(fd)

   Stop monitoring the *fd* file descriptor for read availability.
   Returns "True" if *fd* was previously being monitored for reads.

loop.add_writer(fd, callback, *args)

   Start monitoring the *fd* file descriptor for write availability
   and invoke *callback* with the specified arguments *args* once *fd*
   is available for writing.

   Any preexisting callback registered for *fd* is cancelled and
   replaced by *callback*.

   Use "functools.partial()" para pasar argumentos de palabra clave a
   *callback*.

loop.remove_writer(fd)

   Stop monitoring the *fd* file descriptor for write availability.
   Returns "True" if *fd* was previously being monitored for writes.

Vea también la sección Soporte de plataforma para algunas limitaciones
de estos métodos.

### Trabajar con objetos sockets directamente

En general, implementaciones de protocolo que usen APIs basadas en
transporte como "loop.create_connection()" y "loop.create_server()"
son mas rápidas que aquellas implementaciones que trabajan con
directamente con sockets. De cualquier forma, hay algunos casos de uso
en los cuales el rendimiento no es crítico, y trabajar directamente
con objetos "socket" es mas conveniente.

async loop.sock_recv(sock, nbytes)

   Recibe hasta *nbytes* de *sock*. Versión asíncrona de
   "socket.recv()".

   Retorna los datos recibidos como un objeto bytes.

   *sock* debe ser un socket no bloqueante.

   Distinto en la versión 3.7: A pesar de que este método siempre fue
   documentado como un método de corrutina, los lanzamientos previos a
   Python 3.7 retornaban un "Future". Desde Python 3.7 este es un
   método "async def".

async loop.sock_recv_into(sock, buf)

   Recibe datos desde *sock* en el búfer *buf*. Modelado después del
   método bloqueante "socket.recv_into()".

   Retorna el número de bytes escritos en el búfer.

   *sock* debe ser un socket no bloqueante.

   Added in version 3.7.

async loop.sock_recvfrom(sock, bufsize)

   Recibe un datagrama de hasta *bufsize* de *sock*.  Versión
   asíncrona de "socket.recvfrom()".

   Retorna una tupla de (datos recibidos, dirección remota).

   *sock* debe ser un socket no bloqueante.

   Added in version 3.11.

async loop.sock_recvfrom_into(sock, buf, nbytes=0)

   Recibe un datagrama de hasta *nbytes* de *sock* en *buf*. Versión
   asíncrona de "socket.recvfrom_into()".

   Retorna una dupla de (número de bytes recibidos, dirección remota).

   *sock* debe ser un socket no bloqueante.

   Added in version 3.11.

async loop.sock_sendall(sock, data)

   Envía *data* al socket *sock*. Versión asíncrona de
   "socket.sendall()".

   Este método continua enviando al socket hasta que se hayan enviado
   todos los datos en *data* u ocurra un error. "None" es retornado
   cuando se tiene éxito. Cuando ocurre un error, se lanza una
   excepción. Adicionalmente, no hay manera de determinar cuantos
   datos, si es que se hubo alguno, se procesaron correctamente por el
   extremo receptor de la conexión.

   *sock* debe ser un socket no bloqueante.

   Distinto en la versión 3.7: A pesar de que este método siempre fue
   documentado como un método de corrutina, antes de Python 3.7
   retorna un "Future". Desde Python 3.7, este es un método "async
   def".

async loop.sock_sendto(sock, data, address)

   Envía un datagrama desde *sock* a *address*. Versión asíncrona de
   "socket.sendto()".

   Retorna el número de bytes enviados.

   *sock* debe ser un socket no bloqueante.

   Added in version 3.11.

async loop.sock_connect(sock, address)

   Conecta *sock* a un socket remoto en *address*.

   Versión asíncrona de "socket.connect()".

   *sock* debe ser un socket no bloqueante.

   With "SelectorEventLoop", *address* does not need to be resolved:
   for "AF_INET" and "AF_INET6" sockets, "sock_connect" first checks
   whether *address* is already resolved by calling
   "socket.inet_pton()", and uses "loop.getaddrinfo()" to resolve it
   if it is not.

   "ProactorEventLoop", the default event loop on Windows, does not
   resolve *address*.  The host must already be a numeric IP address;
   passing a host name raises "OSError".  Resolve the address with
   "loop.getaddrinfo()" first, or use "loop.create_connection()",
   which resolves the address on every platform.

   Distinto en la versión 3.5.2: With "SelectorEventLoop", "address"
   no longer needs to be resolved.

   Ver también:

     "loop.create_connection()" y "asyncio.open_connection()".

async loop.sock_accept(sock)

   Acepta una conexión. Modelado después del método bloqueante
   "socket.accept()".

   The socket must be bound to an address and listening for
   connections. The return value is a pair "(conn, address)" where
   *conn* is a *new* socket object usable to send and receive data on
   the connection, and *address* is the address bound to the socket on
   the other end of the connection.

   *sock* debe ser un socket no bloqueante.

   Distinto en la versión 3.7: A pesar de que este método siempre fue
   documentado como un método de corrutina, antes de Python 3.7
   retorna un "Future". Desde Python 3.7, este es un método "async
   def".

   Ver también: "loop.create_server()" y "start_server()".

async loop.sock_sendfile(sock, file, offset=0, count=None, *, fallback=True)

   Envía un archivo usando "os.sendfile" de alto rendimiento si es
   posible. Retorna el número total de bytes enviados.

   Versión asíncrona de "socket.sendfile()".

   *sock* debe ser un "socket.SOCK_STREAM" "socket" no bloqueante.

   *file* debe ser un objeto de archivo regular abierto en modo
   binario.

   *offset* indica desde donde se empezará a leer el archivo. Si es
   especificado, *count* es el número total de bytes a transmitir en
   contraposición con enviar el archivo hasta que se alcance EOF. La
   posición del archivo es actualizada siempre, incluso cuando este
   método genere un error, y "file.tell()" puede ser usado para
   obtener el número de bytes enviados hasta el momento.

   *fallback*, cuando es establecida como "True", hace que asyncio lea
   y escriba el archivo manualmente cuando el sistema no soporta la
   llamada de envío de archivos del sistema (por ejemplo, Windows o
   sockets SSL en Unix).

   Lanza "SendfileNotAvailableError" si el sistema no soporta la
   llamada de envío de archivos del sistema *sendfile* y *fallback* es
   "False".

   *sock* debe ser un socket no bloqueante.

   Added in version 3.7.

### DNS

async loop.getaddrinfo(host, port, *, family=0, type=0, proto=0, flags=0)

   Versión asíncrona de "socket.getaddrinfo()".

async loop.getnameinfo(sockaddr, flags=0)

   Asynchronous version of "socket.getnameinfo()".

Nota:

  Both *getaddrinfo* and *getnameinfo* internally utilize their
  synchronous versions through the loop's default thread pool
  executor. When this executor is saturated, these methods may
  experience delays, which higher-level networking libraries may
  report as increased timeouts. To mitigate this, consider using a
  custom executor for other user tasks, or setting a default executor
  with a larger number of workers.

Distinto en la versión 3.7: Ambos métodos *getaddrinfo* y
*getnameinfo* siempre fueron documentados para retornar una corrutina,
pero antes de Python 3.7 retornaban, de hecho, objetos "Future". A
partir de Python 3.7, ambos métodos son corrutinas.

### Trabajando con tuberías

async loop.connect_read_pipe(protocol_factory, pipe)

   Registra el fin de lectura de *pipe* en el bucle de eventos.

   *protocol_factory* debe ser un ejecutable que retorna una
   implementación del asyncio protocol.

   *pipe* is a *file-like object*.  See Supported pipe objects for the
   objects supported as *pipe*.

   Retorna un par "(transport, protocol)", donde *transport*  soporta
   la interface "ReadTransport" y *protocol* es un objeto instanciado
   por *protocol_factory*.

   Con el bucle de eventos "SelectorEventLoop", el *pipe* es
   establecido en modo no bloqueante.

async loop.connect_write_pipe(protocol_factory, pipe)

   Registra el fin de escritura de *pipe* en el bucle de eventos.

   *protocol_factory* debe ser un ejecutable que retorna una
   implementación del asyncio protocol.

   *pipe* is a *file-like object*.  See Supported pipe objects for the
   objects supported as *pipe*.

   Retorna un par "(transport, protocol)", donde *transport* soporta
   la interface "WriteTransport" y *protocol* es un objeto
   inicializado por *protocol_factory*.

   Con el bucle de eventos "SelectorEventLoop", el *pipe* es
   establecido en modo no bloqueante.

-[ Supported pipe objects ]-

These methods only work with objects the operating system can poll for
readiness or perform overlapped I/O on.  Regular files on disk are
**not** supported on any platform.  There is no asynchronous file I/O
in asyncio; use "loop.run_in_executor()" to read and write regular
files without blocking the event loop.

On Unix, with "SelectorEventLoop", *pipe* must wrap one of the
following:

* a pipe, such as an end of an "os.pipe()" pair or a FIFO created with
  "os.mkfifo()";

* a socket;

* a character device, such as a terminal.

On Windows, where only "ProactorEventLoop" implements these methods,
*pipe* must wrap a handle opened for overlapped I/O (that is, created
with the "FILE_FLAG_OVERLAPPED" flag), since the handle has to be
associated with an I/O completion port.  Handles that were not opened
for overlapped I/O are rejected.  In particular, the standard streams
("sys.stdin", "sys.stdout" and "sys.stderr"), console handles, and the
pipes created by "os.pipe()" are **not** opened for overlapped I/O and
therefore cannot be used with these methods.

Nota:

  "SelectorEventLoop" no soporta los métodos anteriores en windows. En
  su lugar, use "ProactorEventLoop" para Windows.

Ver también:

  Los métodos "loop.subprocess_exec()" y "loop.subprocess_shell()".

### Señales Unix

loop.add_signal_handler(signum, callback, *args)

   Set *callback* as the handler for the *signum* signal, passing
   *args* as positional arguments.

   La llamada será invocada por *loop*, junto con otras llamadas
   encoladas y corrutinas ejecutables de ese bucle de eventos. A menos
   que los gestores de señal la registren usando "signal.signal()",
   una llamada registrada con esta función tiene permitido interactuar
   con el bucle de eventos.

   Lanza "ValueError" si el número de señal es invalido o
   inalcanzable. Lanza "RuntimeError" si hay algún problema preparando
   el gestor.

   Use "functools.partial()" para pasar argumentos de palabra clave a
   *callback*.

   Como "signal.signal()", esta función debe ser invocada en el hilo
   principal.

loop.remove_signal_handler(sig)

   Elimina el gestor para la señal *sig*.

   Retorna "True" si el gestor de señal fue eliminado, o "False" si no
   se estableció gestor para la señal dada.

   Availability: Unix.

Ver también: El módulo "signal".

### Ejecutando código en un hilos o grupos de procesos

awaitable loop.run_in_executor(executor, func, *args)

   Arrange for *func* to be called in the specified executor passing
   *args* as positional arguments.

   The *executor* argument should be an "concurrent.futures.Executor"
   instance. The default executor is used if *executor* is "None". The
   default executor can be set by "loop.set_default_executor()",
   otherwise, a "concurrent.futures.ThreadPoolExecutor" will be lazy-
   initialized and used by "run_in_executor()" if needed.

   Ejemplo:

      import asyncio
      import concurrent.futures

      def blocking_io():
          # File operations (such as logging) can block the
          # event loop: run them in a thread pool.
          with open('/dev/urandom', 'rb') as f:
              return f.read(100)

      def cpu_bound():
          # CPU-bound operations will block the event loop:
          # in general it is preferable to run them in a
          # process pool.
          return sum(i * i for i in range(10 ** 7))

      async def main():
          loop = asyncio.get_running_loop()

          ## Options:

          # 1. Run in the default loop's executor:
          result = await loop.run_in_executor(
              None, blocking_io)
          print('default thread pool', result)

          # 2. Run in a custom thread pool:
          with concurrent.futures.ThreadPoolExecutor() as pool:
              result = await loop.run_in_executor(
                  pool, blocking_io)
              print('custom thread pool', result)

          # 3. Run in a custom process pool:
          with concurrent.futures.ProcessPoolExecutor() as pool:
              result = await loop.run_in_executor(
                  pool, cpu_bound)
              print('custom process pool', result)

          # 4. Run in a custom interpreter pool:
          with concurrent.futures.InterpreterPoolExecutor() as pool:
              result = await loop.run_in_executor(
                  pool, cpu_bound)
              print('custom interpreter pool', result)

      if __name__ == '__main__':
          asyncio.run(main())

   Tenga en cuenta que la protección del punto de entrada ("if
   __name__ == '__main__'") es requerida para la opción 3 debido a las
   peculiaridades de "multiprocessing", que es utilizado por
   "ProcessPoolExecutor". Vea Importación segura del módulo principal.

   Este método retorna un objeto "asyncio.Future".

   Use "functools.partial()" para pasar argumentos de palabra clave a
   *func*.

   Distinto en la versión 3.5.3: "loop.run_in_executor()" ya no
   configura el "max_workers" del ejecutor del grupo de subprocesos
   que crea, sino que lo deja en manos del ejecutor del grupo de
   subprocesos ("ThreadPoolExecutor") para establecer el valor por
   defecto.

loop.set_default_executor(executor)

   Set *executor* as the default executor used by "run_in_executor()".
   *executor* must be an instance of "ThreadPoolExecutor", which
   includes "InterpreterPoolExecutor".

   Distinto en la versión 3.11: *executor* debe ser una instancia de
   "ThreadPoolExecutor".

### Error handling API

Permite personalizar como son manejadas las excepciones en el bucle de
eventos.

loop.set_exception_handler(handler)

   Establece *handler* como el nuevo gestor de excepciones del bucle
   de eventos.

   Si *handler* es "None", se establecerá el gestor de excepciones
   predeterminado. De otro modo, *handler* debe ser un invocable con
   la misma firma "(loop, context)", donde "loop" es una referencia al
   bucle de eventos activo, y "context" es un objeto "dict" que
   contiene los detalles de la excepción (vea la documentación de
   "call_exception_handler()" para detalles acerca del contexto).

   If the handler is called on behalf of a "Task" or "Handle", it is
   run in the "contextvars.Context" of that task or callback handle.

   Distinto en la versión 3.12: The handler may be called in the
   "Context" of the task or handle where the exception originated.

loop.get_exception_handler()

   Retorna el gesto de excepciones actual, o "None" si no fue
   establecido ningún gestor de excepciones personalizado.

   Added in version 3.5.2.

loop.default_exception_handler(context)

   Gestor de excepciones por defecto.

   Esto es llamado cuando ocurre una excepción y no se estableció
   ningún gestor de excepciones. Esto puede ser llamado por un gestor
   de excepciones personalizado que quiera cambiar el comportamiento
   del gestor predeterminado.

   El parámetro *context* tiene el mismo significado que en
   "call_exception_handler()".

loop.call_exception_handler(context)

   Llama al gestor de excepciones del bucle de eventos actual.

   *context* es un objeto "dict" conteniendo las siguientes claves (en
   futuras versiones de Python podrían introducirse nuevas claves):

   * 'message': Mensaje de error;

   * 'exception' (opcional): Objeto de excepción;

   * 'future' (opcional): instancia de "asyncio.Future";

   * 'task' (opcional): instancia de "asyncio.Task";

   * 'handle' (opcional): instancia de "asyncio.Handle";

   * 'protocol' (opcional): instancia de Protocol;

   * 'transport' (opcional): instancia de Transport;

   * 'socket' (opcional): instancia de "socket.socket";

   * 'source_traceback' (optional): Traceback of the source;

   * 'handle_traceback' (optional): Traceback of the handle;

   * 'asyncgen' (opcional): Generador asíncrono que causó
        la excepción.

   Nota:

     This method should not be overloaded in subclassed event loops.
     For custom exception handling, use the "set_exception_handler()"
     method.

### Habilitando el modo depuración

loop.get_debug()

   Obtiene el modo depuración ("bool") del bucle de eventos.

   El valor predeterminado es "True" si la variable de entorno
   "PYTHONASYNCIODEBUG" es establecida a una cadena no vacía, de otro
   modo será "False".

loop.set_debug(enabled: bool)

   Establece el modo de depuración del bucle de eventos.

   Distinto en la versión 3.7: El nuevo Python Modo de Desarrollo
   ahora también se puede usar para habilitar el modo de depuración.

loop.slow_callback_duration

   This attribute can be used to set the minimum execution duration in
   seconds that is considered "slow". When debug mode is enabled,
   "slow" callbacks are logged.

   Default value is 100 milliseconds.

Ver también: El modo depuración de asyncio.

### Running subprocesses

Los métodos descritos en esta subsección son de bajo nivel. En código
async/await regular considere usar las convenientes funciones de alto
nivel "asyncio.create_subprocess_shell()" y
"asyncio.create_subprocess_exec()".

Nota:

  En Windows, el bucle de eventos por defecto "ProactorEventLoop"
  soporta subprocesos, mientras que "SelectorEventLoop" no. Vea
  Soporte de subprocesos en Windows para más detalles.

async loop.subprocess_exec(protocol_factory, *args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)

   Crea un subproceso de uno o mas argumentos de cadena especificados
   por *args*.

   *args* debe ser una lista de cadenas representadas por:

   * "str";

   * o "bytes", codificados a la codificación del sistema de archivos.

   La primer cadena especifica el programa ejecutable, y las cadenas
   restantes especifican los argumentos. En conjunto, los argumentos
   de cadena forman el "argv" del programa.

   Esto es similar a la clase de la librería estándar
   "subprocess.Popen" llamada con "shell=False" y la lista de cadenas
   pasadas como el primer argumento; de cualquier forma, cuando
   "Popen" toma un sólo argumento que es una lista de cadenas,
   *subprocess_exec* toma múltiples cadenas como argumentos.

   El *protocol_factory* debe ser un ejecutable que retorne una
   subclase de la clase "asyncio.SubprocessProtocol".

   Otros parámetros:

   * *stdin* puede ser cualquier de estos:

     * a file-like object

     * an existing file descriptor (a positive integer), for example
       those created with "os.pipe()"

     * la constante "subprocess.PIPE" (predeterminado) que creará una
       tubería nueva y la conectará,

     * el valor "None" que hará que el subproceso herede el descriptor
       de archivo de este proceso

     * la constante "subprocess.DEVNULL" que indica que el archivo
       especial "os.devnull" será utilizado

   * *stdout* puede ser cualquier de estos:

     * a file-like object

     * la constante "subprocess.PIPE" (predeterminado) que creará una
       tubería nueva y la conectará,

     * el valor "None" que hará que el subproceso herede el descriptor
       de archivo de este proceso

     * la constante "subprocess.DEVNULL" que indica que el archivo
       especial "os.devnull" será utilizado

   * *stderr* puede ser cualquier de estos:

     * a file-like object

     * la constante "subprocess.PIPE" (predeterminado) que creará una
       tubería nueva y la conectará,

     * el valor "None" que hará que el subproceso herede el descriptor
       de archivo de este proceso

     * la constante "subprocess.DEVNULL" que indica que el archivo
       especial "os.devnull" será utilizado

     * la constante "subprocess.STDOUT" que conectará el flujo de
       errores predeterminado al flujo de salida predeterminado del
       proceso

   * El resto de argumentos de palabra clave son pasados a
     "subprocess.Popen" sin interpretación, excepto por *bufsize*,
     *universal_newlines*, *shell*, *text*, *encoding* y *errors*, que
     no deben ser especificados en lo absoluto.

     La API subproceso "asyncio" no soporta decodificar los flujos
     como texto. "bytes.decode()" puede ser usado para convertir a
     texto los bytes retornados por el flujo.

   If a file-like object passed as *stdin*, *stdout* or *stderr*
   represents a pipe, then the other side of this pipe should be
   registered with "connect_write_pipe()" or "connect_read_pipe()" for
   use with the event loop.

   Vea el constructor de la clase "subprocess.Popen" para
   documentación acerca de otros argumentos.

   Retorna un par de "(transport, protocol)", donde *transport* se
   ajusta a la clase base "asyncio.SubprocessTransport" y *protocol*
   es un objeto instanciado por *protocol_factory*.

   If the transport is closed or is garbage collected, the child
   process is killed if it is still running.

async loop.subprocess_shell(protocol_factory, cmd, *, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)

   Crea un subproceso desde *cmd*, que puede ser una cadena "str" o
   "bytes" codificado a la codificación del sistema de archivos,
   usando la sintaxis "shell" de la plataforma.

   Esto es similar a la clase de la librería estándar
   "subprocess.Popen" llamada con "shell=True".

   El *protocol_factory* debe ser un ejecutable que retorne una
   subclase de la clase "asyncio.SubprocessProtocol".

   Vea "subprocess_exec()" para mas detalles acerca de los argumentos
   restantes.

   Retorna un par de "(transport, protocol)", donde *transport* se
   ajusta a la clase base "SubprocessTransport" y *protocol* es un
   objeto instanciado por *protocol_factory*.

   If the transport is closed or is garbage collected, the child
   process is killed if it is still running.

Nota:

  Es responsabilidad de la aplicación asegurar que todos los espacios
  en blanco y caracteres especiales estén escapados correctamente para
  evitar vulnerabilidades de inyección de código. La función
  "shlex.quote()" puede ser usada para escapar apropiadamente espacios
  en blanco y caracteres especiales en cadenas que van a ser usadas
  para construir comandos de consola.

## Callback handles

class asyncio.Handle

   Un objeto de contenedor de llamada retornado por
   "loop.call_soon()", "loop.call_soon_threadsafe()".

   get_context()

      Return the "contextvars.Context" object associated with the
      handle.

      Added in version 3.12.

   cancel()

      Cancela la llamada. Si la llamada ya fue cancelada o ejecutada,
      este método no tiene efecto.

   cancelled()

      Retorna "True" si la llamada fue cancelada.

      Added in version 3.7.

class asyncio.TimerHandle

   Un objeto de contenedor de llamada retornado por
   "loop.call_later()", and "loop.call_at()".

   Esta clase es una subclase de "Handle".

   when()

      Retorna el tiempo de una llamada planificada como "float"
      segundos.

      El tiempo es una marca de tiempo absoluta, usando la misma
      referencia de tiempo que "loop.time()".

      Added in version 3.7.

## Server objects

Los objetos de servidor son creados por las funciones
"loop.create_server()", "loop.create_unix_server()", "start_server()",
y "start_unix_server()".

Do not instantiate the "Server" class directly.

class asyncio.Server

   Los objetos *Server* son gestores de asíncronos de contexto. Cuando
   son usados en una declaración "async with", está garantizado que el
   objeto Servidor está cerrado y no está aceptando nuevas conexiones
   cuando la declaración "async with" es completada:

      srv = await loop.create_server(...)

      async with srv:
          # some code

      # At this point, srv is closed and no longer accepts new connections.

   Distinto en la versión 3.7: El objeto Servidor es un gestor
   asíncrono de contexto desde Python 3.7.

   Distinto en la versión 3.11: This class was exposed publicly as
   "asyncio.Server" in Python 3.9.11, 3.10.3 and 3.11.

   close()

      Deja de servir: deja de escuchar sockets y establece el atributo
      "sockets" a "None".

      Los sockets que representan conexiones entrantes existentes de
      clientes se dejan abiertas.

      The server is closed asynchronously; use the "wait_closed()"
      coroutine to wait until the server is closed (and no more
      connections are active).

   close_clients()

      Close all existing incoming client connections.

      Calls "close()" on all associated transports.

      "close()" should be called before "close_clients()" when closing
      the server to avoid races with new clients connecting.

      Added in version 3.13.

   abort_clients()

      Close all existing incoming client connections immediately,
      without waiting for pending operations to complete.

      Calls "abort()" on all associated transports.

      "close()" should be called before "abort_clients()" when closing
      the server to avoid races with new clients connecting.

      Added in version 3.13.

   get_loop()

      Retorna el bucle de eventos asociado con el objeto Servidor.

      Added in version 3.7.

   async start_serving()

      Comienza a aceptar conexiones.

      Este método es idempotente, así que puede ser llamado cuando el
      servidor ya está sirviendo.

      El parámetro sólo de palabra clave *start_serving* de
      "loop.create_server()" y "asyncio.start_server()" permite crear
      un objeto Servidor que no está aceptando conexiones
      inicialmente. En este caso "Server.start_serving()", o
      "Server.serve_forever()" pueden ser usados para hacer que el
      servidor empiece a aceptar conexiones.

      Added in version 3.7.

   async serve_forever()

      Comienza a aceptar conexiones hasta que la corrutina sea
      cancelada. La cancelación de la tarea "serve_forever" hace que
      el servidor sea cerrado.

      Este método puede ser llamado si el servidor ya está aceptando
      conexiones. Solamente una tarea "serve_forever" puede existir
      para un objeto *Server*.

      Ejemplo:

         async def client_connected(reader, writer):
             # Communicate with the client with
             # reader/writer streams.  For example:
             await reader.readline()

         async def main(host, port):
             srv = await asyncio.start_server(
                 client_connected, host, port)
             await srv.serve_forever()

         asyncio.run(main('127.0.0.1', 0))

      Added in version 3.7.

   is_serving()

      Retorna "True" si el servidor está aceptando nuevas conexiones.

      Added in version 3.7.

   async wait_closed()

      Wait until the "close()" method completes and all active
      connections have finished.

      Distinto en la versión 3.12: "wait_closed()" now waits until the
      server is closed and all active connections have finished.
      Previously, it returned immediately if the server was already
      closed, even if connections were still active.

   sockets

      List of socket-like objects, "asyncio.trsock.TransportSocket",
      which the server is listening on.

      Distinto en la versión 3.7: Antes de Python 3.7 "Server.sockets"
      solía retornar directamente una lista interna de servidores
      socket. En 3.7 se retorna una copia de esa lista.

## Event loop implementations

asyncio viene con dos implementaciones diferentes del bucle de
eventos: "SelectorEventLoop" y "ProactorEventLoop".

By default asyncio is configured to use "EventLoop".

class asyncio.SelectorEventLoop

   A subclass of "AbstractEventLoop" based on the "selectors" module.

   Usa el *selector* disponible mas eficiente para la plataforma dada.
   También es posible configurar manualmente la implementación exacta
   del selector a utilizar:

      import asyncio
      import selectors

      async def main():
         ...

      loop_factory = lambda: asyncio.SelectorEventLoop(selectors.SelectSelector())
      asyncio.run(main(), loop_factory=loop_factory)

   Availability: Unix, Windows.

class asyncio.ProactorEventLoop

   A subclass of "AbstractEventLoop" for Windows that uses "I/O
   Completion Ports" (IOCP).

   Availability: Windows.

   Ver también: MSDN documentation on I/O Completion Ports.

class asyncio.EventLoop

      An alias to the most efficient available subclass of
      "AbstractEventLoop" for the given platform.

      It is an alias to "SelectorEventLoop" on Unix and
      "ProactorEventLoop" on Windows.

   Added in version 3.13.

class asyncio.AbstractEventLoop

   Clase base abstracta para bucles de evento compatibles con asyncio.

   La sección Event loop methods lista todos los métodos que una
   implementación alternativa de "AbstractEventLoop" debería tener
   definidos.

## Examples

Nótese que todos los ejemplos en esta sección muestran **a propósito**
como usar las APIs de bucle de eventos de bajo nivel, como ser
"loop.run_forever()" y "loop.call_soon()". Aplicaciones asyncio
modernas raramente necesitan ser escritas de esta manera; considere
utilizar funciones de alto nivel como "asyncio.run()".

### Hola Mundo con call_soon()

Un ejemplo usando el método "loop.call_soon()" para planificar una
llamada. La llamada muestra ""Hello World"" y luego para el bucle de
eventos:

   import asyncio

   def hello_world(loop):
       """A callback to print 'Hello World' and stop the event loop"""
       print('Hello World')
       loop.stop()

   loop = asyncio.new_event_loop()

   # Schedule a call to hello_world()
   loop.call_soon(hello_world, loop)

   # Blocking call interrupted by loop.stop()
   try:
       loop.run_forever()
   finally:
       loop.close()

Ver también:

  Un ejemplo similar de Hola Mundo creado con una corrutina y la
  función "run()".

### Muestra la fecha actual con call_later()

Un ejemplo de llamada mostrando la fecha actual cada un segundo. La
llamada usa el método "loop.call_later()" para volver a planificarse
después de 5 segundos, y después para el bucle de eventos:

   import asyncio
   import datetime as dt

   def display_date(end_time, loop):
       print(dt.datetime.now())
       if (loop.time() + 1.0) < end_time:
           loop.call_later(1, display_date, end_time, loop)
       else:
           loop.stop()

   loop = asyncio.new_event_loop()

   # Schedule the first call to display_date()
   end_time = loop.time() + 5.0
   loop.call_soon(display_date, end_time, loop)

   # Blocking call interrupted by loop.stop()
   try:
       loop.run_forever()
   finally:
       loop.close()

Ver también:

  Un ejemplo similar a fecha actual creado con una corrutina y la
  función "run()".

### Mirar un descriptor de archivo para leer eventos

Espera hasta que el descriptor de archivo reciba algún dato usando el
método "loop.add_reader()" y entonces cierra el bucle de eventos:

   import asyncio
   from socket import socketpair

   # Create a pair of connected file descriptors
   rsock, wsock = socketpair()

   loop = asyncio.new_event_loop()

   def reader():
       data = rsock.recv(100)
       print("Received:", data.decode())

       # We are done: unregister the file descriptor
       loop.remove_reader(rsock)

       # Stop the event loop
       loop.stop()

   # Register the file descriptor for read event
   loop.add_reader(rsock, reader)

   # Simulate the reception of data from the network
   loop.call_soon(wsock.send, 'abc'.encode())

   try:
       # Run the event loop
       loop.run_forever()
   finally:
       # We are done. Close sockets and the event loop.
       rsock.close()
       wsock.close()
       loop.close()

Ver también:

  * Un ejemplo similar usando transportes, protocolos y el método
    "loop.create_connection()".

  * Otro ejemplo similar usando la función de alto nivel
    "asyncio.open_connection()" y transmisiones.

### Establece los gestores de señal para SIGINT y SIGTERM

(This "signal" example only works on Unix.)

Register handlers for signals "SIGINT" and "SIGTERM" using the
"loop.add_signal_handler()" method:

   import asyncio
   import functools
   import os
   import signal

   def ask_exit(signame, loop):
       print("got signal %s: exit" % signame)
       loop.stop()

   async def main():
       loop = asyncio.get_running_loop()

       for signame in {'SIGINT', 'SIGTERM'}:
           loop.add_signal_handler(
               getattr(signal, signame),
               functools.partial(ask_exit, signame, loop))

       await asyncio.sleep(3600)

   print("Event loop running for 1 hour, press Ctrl+C to interrupt.")
   print(f"pid {os.getpid()}: send SIGINT or SIGTERM to exit.")

   asyncio.run(main())
