---
title: '"sched" --- Event scheduler'
source_url: https://docs.python.org/es/3
source_path: library/sched.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3710
---

# "sched" --- Event scheduler

**Código fuente:** Lib/sched.py

======================================================================

The "sched" module defines a class which implements a general purpose
event scheduler:

class sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)

   La clase "scheduler" define una interfaz genérica para planificar
   eventos. Necesita dos funciones para tratar con el "mundo exterior"
   --- *timefunc* debe poder llamarse sin argumentos y retornar un
   número (el "time", en cualquier unidad). La función *delayfunc*
   debería ser invocable con un argumento, compatible con la salida de
   *timefunc*, y debería retrasar tantas unidades de tiempo.
   *delayfunc* también se llamará con el argumento "0" después de que
   se ejecute cada evento para permitir que otros hilos tengan la
   oportunidad de ejecutarse en aplicaciones multihilo.

   Distinto en la versión 3.3: Los argumentos *timefunc* and
   *delayfunc* son opcionales.

   Distinto en la versión 3.3: "scheduler" La clase se puede usar de
   forma segura en entornos multihilo.

Ejemplo:

   >>> import sched, time
   >>> s = sched.scheduler(time.time, time.sleep)
   >>> def print_time(a='default'):
   ...     print("From print_time", time.time(), a)
   ...
   >>> def print_some_times():
   ...     print(time.time())
   ...     s.enter(10, 1, print_time)
   ...     s.enter(5, 2, print_time, argument=('positional',))
   ...     # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
   ...     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
   ...     s.enterabs(1_650_000_000, 10, print_time, argument=("first enterabs",))
   ...     s.enterabs(1_650_000_000, 5, print_time, argument=("second enterabs",))
   ...     s.run()
   ...     print(time.time())
   ...
   >>> print_some_times()
   1652342830.3640375
   From print_time 1652342830.3642538 second enterabs
   From print_time 1652342830.3643398 first enterabs
   From print_time 1652342835.3694863 positional
   From print_time 1652342835.3696074 keyword
   From print_time 1652342840.369612 default
   1652342840.3697174

## Objetos de "Scheduler"

"scheduler" Las sentencias tienen los siguientes métodos y atributos:

scheduler.enterabs(time, priority, action, argument=(), kwargs={})

   Planifica un nuevo evento. El argumento *time* debe ser un tipo
   numérico compatible con el valor de retorno de la función
   *timefunc* que se pasa al constructor. Los eventos planificados
   para la misma *time* se ejecutarán en el orden de su *priority*. Un
   número más bajo representa una prioridad más alta.

   Ejecutar el evento significa ejecutar "action(*argument,
   **kwargs)". *argument* es una secuencia que contiene los argumentos
   posicionales para *action*. *kwargs* es un diccionario que contiene
   los argumentos de palabras clave para *action*.

   El valor de retorno es un evento que puede usarse para una
   cancelación posterior del evento (ver "cancel()").

   Distinto en la versión 3.3: El argumento *argument* es opcional.

   Distinto en la versión 3.3: Se agregó el argumento *kwargs*.

scheduler.enter(delay, priority, action, argument=(), kwargs={})

   Planifica un evento *delay* para más unidades de tiempo. Aparte del
   tiempo relativo, los otros argumentos, el efecto y el valor de
   retorno son los mismos que para "enterabs()".

   Distinto en la versión 3.3: El argumento *argument* es opcional.

   Distinto en la versión 3.3: Se agregó el argumento *kwargs*.

scheduler.cancel(event)

   Elimina el evento de la cola. Si *event* no es un evento
   actualmente en la cola, este método lanzará un "ValueError".

scheduler.empty()

   Retorna "True" si la cola de eventos está vacía.

scheduler.run(blocking=True)

   Ejecuta todos los eventos planificados. Este método esperará
   (usando la función *delayfunc* enviada al constructor) al próximo
   evento, luego lo ejecutará y así sucesivamente hasta que no haya
   más eventos planificados.

   If *blocking* is false, immediately executes all events in the
   queue which have a time value less than or equal to the current
   *timefunc* value (if any) and returns the difference between the
   current *timefunc* value and the time value of the next scheduled
   event in the scheduler's event queue.  If the queue is empty,
   returns "None".

   *action* o *delayfunc* pueden generar una excepción. En cualquier
   caso, el planificador mantendrá un estado consistente y propagará
   la excepción. Si *action* genera una excepción, el evento no se
   intentará en futuras llamadas a "run()".

   Si una secuencia de eventos tarda más en ejecutarse que el tiempo
   disponible antes del próximo evento, el planificador simplemente se
   retrasará. No se descartarán eventos; el código de llamada es
   responsable de cancelar eventos que ya no son oportunos.

   Distinto en la versión 3.3: Se agregó el argumento *blocking*.

scheduler.queue

   Atributo de solo lectura que retorna una lista de los próximos
   eventos en el orden en que se ejecutarán. Cada evento se muestra
   como un *named tuple* con los siguientes campos : *time, priority,
   action, argument, kwargs*.
