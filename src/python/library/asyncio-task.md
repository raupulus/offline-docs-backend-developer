---
title: Coroutines and tasks
source_url: https://docs.python.org/es/3
source_path: library/asyncio-task.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1740
---

# Coroutines and tasks

Esta sección describe las API de asyncio de alto nivel para trabajar
con corrutinas y tareas.

* Corrutinas

* Esperables

* Creating tasks

* Task cancellation

* Task groups

* Durmiendo

* Running tasks concurrently

* Eager task factory

* Shielding from cancellation

* Tiempo agotado

* Waiting primitives

* Running in threads

* Scheduling from other threads

* Introspección

* Task object

## Corrutinas

**Source code:** Lib/asyncio/coroutines.py

======================================================================

*Coroutines* declarado con la sintaxis async/await es la forma
preferida de escribir aplicaciones asyncio. Por ejemplo, el siguiente
fragmento de código imprime "hola", espera 1 segundo y luego imprime
"mundo":

   >>> import asyncio

   >>> async def main():
   ...     print('hello')
   ...     await asyncio.sleep(1)
   ...     print('world')

   >>> asyncio.run(main())
   hello
   world

Tenga en cuenta que simplemente llamando a una corrutina no programará
para que se ejecute:

   >>> main()
   <coroutine object main at 0x1053bb7c8>

Para ejecutar realmente una corutina, asyncio proporciona los
siguientes mecanismos:

* La función "asyncio.run()" para ejecutar la función de punto de
  entrada de nivel superior "main()" (consulte el ejemplo anterior.)

* Esperando en una corrutina. El siguiente fragmento de código
  imprimirá "hola" después de esperar 1 segundo y luego imprimirá
  "mundo" después de esperar *otros* 2 segundos:

     import asyncio
     import time

     async def say_after(delay, what):
         await asyncio.sleep(delay)
         print(what)

     async def main():
         print(f"started at {time.strftime('%X')}")

         await say_after(1, 'hello')
         await say_after(2, 'world')

         print(f"finished at {time.strftime('%X')}")

     asyncio.run(main())

  Salida esperada:

     started at 17:13:52
     hello
     world
     finished at 17:13:55

* La función "asyncio.create_task()" para ejecutar corrutinas
  concurrentemente como asyncio "Tasks".

  Modifiquemos el ejemplo anterior y ejecutemos dos corrutinas
  "say_after" *concurrentemente*:

     async def main():
         task1 = asyncio.create_task(
             say_after(1, 'hello'))

         task2 = asyncio.create_task(
             say_after(2, 'world'))

         print(f"started at {time.strftime('%X')}")

         # Wait until both tasks are completed (should take
         # around 2 seconds.)
         await task1
         await task2

         print(f"finished at {time.strftime('%X')}")

  Tenga en cuenta que la salida esperada ahora muestra que el
  fragmento de código se ejecuta 1 segundo más rápido que antes:

     started at 17:14:32
     hello
     world
     finished at 17:14:34

* La clase "asyncio.TaskGroup" proporciona una alternativa más moderna
  a "create_task()". Usando esta API, el último ejemplo se convierte
  en:

     async def main():
         async with asyncio.TaskGroup() as tg:
             task1 = tg.create_task(
                 say_after(1, 'hello'))

             task2 = tg.create_task(
                 say_after(2, 'world'))

             print(f"started at {time.strftime('%X')}")

         # The await is implicit when the context manager exits.

         print(f"finished at {time.strftime('%X')}")

  El tiempo y la salida deben ser los mismos que para la versión
  anterior.

  Added in version 3.11: "asyncio.TaskGroup".

## Esperables

Decimos que un objeto es un objeto **esperable** si se puede utilizar
en una expresión "await". Muchas API de asyncio están diseñadas para
aceptar los valores esperables.

Hay tres tipos principales de objetos *esperables*: **corrutinas**,
**Tareas** y **Futures**.

-[ Corrutinas ]-

Las corrutinas de Python son *esperables* y por lo tanto se pueden
esperar de otras corrutinas:

   import asyncio

   async def nested():
       return 42

   async def main():
       # Nothing happens if we just call "nested()".
       # A coroutine object is created but not awaited,
       # so it *won't run at all*.
       nested()  # will raise a "RuntimeWarning".

       # Let's do it differently now and await it:
       print(await nested())  # will print "42".

   asyncio.run(main())

Importante:

  En esta documentación se puede utilizar el término "corrutina" para
  dos conceptos estrechamente relacionados:

  * una *función corrutina*: una función "async def";

  * un *objeto corrutina*: un objeto retornado llamando a una *función
    corrutina*.

-[ Tareas ]-

*Las tareas* se utilizan para programar corrutinas *concurrentemente*.

Cuando una corrutina se envuelve en una *Tarea* con funciones como
"asyncio.create_task()" la corrutina se programa automáticamente para
ejecutarse pronto:

   import asyncio

   async def nested():
       return 42

   async def main():
       # Schedule nested() to run soon concurrently
       # with "main()".
       task = asyncio.create_task(nested())

       # "task" can now be used to cancel "nested()", or
       # can simply be awaited to wait until it is complete:
       await task

   asyncio.run(main())

-[ Futures ]-

Un "Future" es un objeto esperable especial de **bajo-nivel** que
representa un **resultado eventual** de una operación asíncrona.

Cuando un objeto Future es *esperado* significa que la corrutina
esperará hasta que el Future se resuelva en algún otro lugar.

Los objetos Future de asyncio son necesarios para permitir que el
código basado en retro llamada se use con async/await.

Normalmente , **no es necesario** crear objetos Future en el código de
nivel de aplicación.

Los objetos Future, a veces expuestos por bibliotecas y algunas API de
asyncio, pueden ser esperados:

   async def main():
       await function_that_returns_a_future_object()

       # this is also valid:
       await asyncio.gather(
           function_that_returns_a_future_object(),
           some_python_coroutine()
       )

Un buen ejemplo de una función de bajo nivel que retorna un objeto
Future es "loop.run_in_executor()".

## Creating tasks

**Source code:** Lib/asyncio/tasks.py

======================================================================

asyncio.create_task(coro, *, name=None, context=None, eager_start=None, **kwargs)

   Envuelve una coroutine *coro* en una "Task" y programa su
   ejecución. Retorna el objeto Tarea.

   The full function signature is largely the same as that of the
   "Task" constructor (or factory) - all of the keyword arguments to
   this function are passed through to that interface.

   Un argumento *context* opcional de solo palabra clave permite
   especificar un "contextvars.Context" personalizado para que se
   ejecute el *coro*. La copia de contexto actual se crea cuando no se
   proporciona *context*.

   An optional keyword-only *eager_start* argument allows specifying
   if the task should execute eagerly during the call to create_task,
   or be scheduled later. If *eager_start* is not passed the mode set
   by "loop.set_task_factory()" will be used.

   La tarea se ejecuta en el bucle retornado por "get_running_loop()",
   "RuntimeError" se genera si no hay ningún bucle en ejecución en el
   subproceso actual.

   Nota:

     "asyncio.TaskGroup.create_task()" es una alternativa más nueva
     que permite una espera conveniente para un grupo de tareas
     relacionadas.

   Importante:

     Guarde una referencia al resultado de esta función, para evitar
     que una tarea desaparezca en medio de la ejecución. El bucle de
     eventos solo mantiene referencias débiles a las tareas. Una tarea
     a la que no se hace referencia en ningún otro lugar puede ser
     recolectada por el recolector de basura  en cualquier momento,
     incluso antes de que se complete. Para tareas confiables en
     segundo plano,  de tipo "lanzar y olvidar", reúnalas en una
     colección:

        background_tasks = set()

        for i in range(10):
            task = asyncio.create_task(some_coro(param=i))

            # Add task to the set. This creates a strong reference.
            background_tasks.add(task)

            # To prevent keeping references to finished tasks forever,
            # make each task remove its own reference from the set after
            # completion:
            task.add_done_callback(background_tasks.discard)

   Added in version 3.7.

   Distinto en la versión 3.8: Se ha añadido el parámetro *name*.

   Distinto en la versión 3.11: Se ha añadido el parámetro *context*.

   Distinto en la versión 3.14: Added the *eager_start* parameter by
   passing on all *kwargs*.

## Task cancellation

Las tareas se pueden cancelar de forma fácil y segura. Cuando se
cancela una tarea, se generará "asyncio.CancelledError" en la tarea en
la próxima oportunidad.

Se recomienda que las corrutinas utilicen bloques "try/finally" para
realizar de forma sólida la lógica de limpieza. En caso de que
"asyncio.CancelledError" se detecte explícitamente, generalmente
debería propagarse cuando se complete la limpieza.
"asyncio.CancelledError" subclasifica directamente a "BaseException",
por lo que la mayor parte del código no necesitará tenerlo en cuenta.

Los componentes asyncio que permiten la simultaneidad estructurada,
como "asyncio.TaskGroup" y "asyncio.timeout()", se implementan
mediante cancelación internamente y podrían comportarse mal si una
rutina traga "asyncio.CancelledError". De manera similar, el código de
usuario generalmente no debería llamar a "uncancel". Sin embargo, en
los casos en los que realmente se desea suprimir
"asyncio.CancelledError", es necesario llamar también a "uncancel()"
para eliminar completamente el estado de cancelación.

## Task groups

Los grupos de tareas combinan una API de creación de tareas con una
forma conveniente y confiable de esperar a que finalicen todas las
tareas del grupo.

class asyncio.TaskGroup

   Un asynchronous context manager que contiene un grupo de tareas.
   Las tareas se pueden agregar al grupo usando "create_task()". Se
   esperan todas las tareas cuando sale el administrador de contexto.

   Added in version 3.11.

   create_task(coro, *, name=None, context=None, eager_start=None, **kwargs)

      Create a task in this task group. The signature matches that of
      "asyncio.create_task()". If the task group is inactive (e.g. not
      yet entered, already finished, or in the process of shutting
      down), we will close the given "coro".

      Distinto en la versión 3.13: Close the given coroutine if the
      task group is not active.

      Distinto en la versión 3.14: Passes on all *kwargs* to
      "loop.create_task()"

Ejemplo:

   async def main():
       async with asyncio.TaskGroup() as tg:
           task1 = tg.create_task(some_coro(...))
           task2 = tg.create_task(another_coro(...))
       print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")

La instrucción "async with" esperará a que finalicen todas las tareas
del grupo. Mientras espera, aún se pueden agregar nuevas tareas al
grupo (por ejemplo, pasando "tg" a una de las corrutinas y llamando a
"tg.create_task()" en esa corrutina). Una vez finalizada la última
tarea y salido del bloque "async with", no se podrán añadir nuevas
tareas al grupo.

La primera vez que alguna de las tareas pertenecientes al grupo falla
con una excepción que no sea "asyncio.CancelledError", las tareas
restantes del grupo se cancelan. No se pueden añadir más tareas al
grupo. En este punto, si el cuerpo de la instrucción "async with" aún
está activo (es decir, aún no se ha llamado a "__aexit__()"), la tarea
que contiene directamente la instrucción "async with" también se
cancela. El "asyncio.CancelledError" resultante interrumpirá un
"await", pero no saldrá de la instrucción "async with" que lo
contiene.

Una vez que todas las tareas han finalizado, si alguna tarea ha
fallado con una excepción que no sea "asyncio.CancelledError", esas
excepciones se combinan en un "ExceptionGroup" o "BaseExceptionGroup"
(según corresponda; consulte su documentación) que luego se genera.

Dos excepciones básicas se tratan de manera especial: si alguna tarea
falla con "KeyboardInterrupt" o "SystemExit", el grupo de tareas aún
cancela las tareas restantes y las espera, pero luego se vuelve a
generar el "KeyboardInterrupt" o "SystemExit" inicial en lugar de
"ExceptionGroup" o "BaseExceptionGroup".

Si el cuerpo de la instrucción "async with" finaliza con una excepción
(por lo que se llama a "__aexit__()" con un conjunto de excepciones),
esto se trata igual que si una de las tareas fallara: las tareas
restantes se cancelan y luego se esperan, y las excepciones de no
cancelación se agrupan en un grupo de excepción y se generan. La
excepción pasada a "__aexit__()", a menos que sea
"asyncio.CancelledError", también se incluye en el grupo de
excepciones. Se hace el mismo caso especial para "KeyboardInterrupt" y
"SystemExit" que en el párrafo anterior.

Task groups are careful not to mix up the internal cancellation used
to "wake up" their "__aexit__()" with cancellation requests for the
task in which they are running made by other parties. In particular,
when one task group is syntactically nested in another, and both
experience an exception in one of their child tasks simultaneously,
the inner task group will process its exceptions, and then the outer
task group will receive another cancellation and process its own
exceptions.

In the case where a task group is cancelled externally and also must
raise an "ExceptionGroup", it will call the parent task's "cancel()"
method. This ensures that a "asyncio.CancelledError" will be raised at
the next "await", so the cancellation is not lost.

Task groups preserve the cancellation count reported by
"asyncio.Task.cancelling()".

Distinto en la versión 3.13: Improved handling of simultaneous
internal and external cancellations and correct preservation of
cancellation counts.

### Terminating a task group

While terminating a task group is not natively supported by the
standard library, termination can be achieved by adding an exception-
raising task to the task group and ignoring the raised exception:

   import asyncio
   from asyncio import TaskGroup

   class TerminateTaskGroup(Exception):
       """Exception raised to terminate a task group."""

   async def force_terminate_task_group():
       """Used to force termination of a task group."""
       raise TerminateTaskGroup()

   async def job(task_id, sleep_time):
       print(f'Task {task_id}: start')
       await asyncio.sleep(sleep_time)
       print(f'Task {task_id}: done')

   async def main():
       try:
           async with TaskGroup() as group:
               # spawn some tasks
               group.create_task(job(1, 0.5))
               group.create_task(job(2, 1.5))
               # sleep for 1 second
               await asyncio.sleep(1)
               # add an exception-raising task to force the group to terminate
               group.create_task(force_terminate_task_group())
       except* TerminateTaskGroup:
           pass

   asyncio.run(main())

Expected output:

   Task 1: start
   Task 2: start
   Task 1: done

## Durmiendo

async asyncio.sleep(delay, result=None)

   Bloquea por *delay* segundos.

   Si se proporciona *result*, se retorna al autor de la llamada
   cuando se completa la corrutina.

   "sleep()" siempre suspende la tarea actual, permitiendo que se
   ejecuten otras tareas.

   Establecer el retraso en 0 proporciona una ruta optimizada para
   permitir que se ejecuten otras tareas. Esto puede ser utilizado por
   funciones de ejecución prolongada para evitar bloquear el bucle de
   eventos durante toda la duración de la llamada a la función.

   Ejemplo de una rutina que muestra la fecha actual cada segundo
   durante 5 segundos:

      import asyncio
      import datetime as dt

      async def display_date():
          loop = asyncio.get_running_loop()
          end_time = loop.time() + 5.0
          while True:
              print(dt.datetime.now())
              if (loop.time() + 1.0) >= end_time:
                  break
              await asyncio.sleep(1)

      asyncio.run(display_date())

   Distinto en la versión 3.10: Se quitó el parámetro *loop*.

   Distinto en la versión 3.13: Raises "ValueError" if *delay* is
   "nan".

## Running tasks concurrently

awaitable asyncio.gather(*aws, return_exceptions=False)

   Ejecute objetos esperables en la secuencia *aws* de forma
   *concurrently*.

   Si cualquier esperable en *aws* es una corrutina, se programa
   automáticamente como una Tarea.

   Si todos los esperables se completan correctamente, el resultado es
   una lista agregada de valores retornados. El orden de los valores
   de resultado corresponde al orden de esperables en *aws*.

   Si *return_exceptions* es "False" (valor predeterminado), la
   primera excepción provocada se propaga inmediatamente a la tarea
   que espera en "gather()". Otros esperables en la secuencia *aws*
   **no se cancelarán** y continuarán ejecutándose.

   Si *return_exceptions* es "True", las excepciones se tratan igual
   que los resultados correctos y se agregan en la lista de
   resultados.

   Si "gather()" es *cancelado*, todos los esperables enviados (que
   aún no se han completado) también se *cancelan*.

   Si alguna Tarea o Future de la secuencia *aws* se *cancela*, se
   trata como si se lanzara "CancelledError" -- la llamada "gather()"
   **no** se cancela en este caso. Esto es para evitar la cancelación
   de una Tarea/Future enviada para hacer que otras Tareas/Futures
   sean canceladas.

   Nota:

     A new alternative to create and run tasks concurrently and wait
     for their completion is "asyncio.TaskGroup". *TaskGroup* provides
     stronger safety guarantees than *gather* for scheduling a nesting
     of subtasks: if a task (or a subtask, a task scheduled by a task)
     raises an exception, *TaskGroup* will, while *gather* will not,
     cancel the remaining scheduled tasks.

   Ejemplo:

      import asyncio

      async def factorial(name, number):
          f = 1
          for i in range(2, number + 1):
              print(f"Task {name}: Compute factorial({number}), currently i={i}...")
              await asyncio.sleep(1)
              f *= i
          print(f"Task {name}: factorial({number}) = {f}")
          return f

      async def main():
          # Schedule three calls *concurrently*:
          L = await asyncio.gather(
              factorial("A", 2),
              factorial("B", 3),
              factorial("C", 4),
          )
          print(L)

      asyncio.run(main())

      # Expected output:
      #
      #     Task A: Compute factorial(2), currently i=2...
      #     Task B: Compute factorial(3), currently i=2...
      #     Task C: Compute factorial(4), currently i=2...
      #     Task A: factorial(2) = 2
      #     Task B: Compute factorial(3), currently i=3...
      #     Task C: Compute factorial(4), currently i=3...
      #     Task B: factorial(3) = 6
      #     Task C: Compute factorial(4), currently i=4...
      #     Task C: factorial(4) = 24
      #     [2, 6, 24]

   Nota:

     If *return_exceptions* is false, cancelling gather() after it has
     been marked done won't cancel any submitted awaitables. For
     instance, gather can be marked done after propagating an
     exception to the caller, therefore, calling "gather.cancel()"
     after catching an exception (raised by one of the awaitables)
     from gather won't cancel any other awaitables.

   Distinto en la versión 3.7: Si se cancela el propio *gather*, la
   cancelación se propaga independientemente de *return_exceptions*.

   Distinto en la versión 3.10: Se quitó el parámetro *loop*.

   Obsoleto desde la versión 3.10: Se emite una advertencia de
   obsolescencia si no se proporcionan argumentos posicionales o no
   todos los argumentos posicionales son objetos de tipo Future y no
   hay un bucle de eventos en ejecución.

## Eager task factory

asyncio.eager_task_factory(loop, coro, *, name=None, context=None)

   Una fábrica de tareas para una ejecución entusiasta de tareas.

   Cuando se utiliza esta fábrica (a través de
   "loop.set_task_factory(asyncio.eager_task_factory)"), las
   corrutinas comienzan a ejecutarse sincrónicamente durante la
   construcción de "Task". Las tareas sólo se programan en el bucle de
   eventos si se bloquean. Esto puede suponer una mejora del
   rendimiento, ya que se evita la sobrecarga de la programación del
   bucle para las corrutinas que se completan sincrónicamente.

   Un ejemplo común en el que esto resulta beneficioso son las rutinas
   que emplean almacenamiento en caché o memorización para evitar E/S
   reales cuando sea posible.

   Nota:

     La ejecución inmediata de la corrutina es un cambio semántico. Si
     la rutina regresa o se activa, la tarea nunca se programa en el
     bucle de eventos. Si la ejecución de la rutina se bloquea, la
     tarea se programa en el bucle de eventos. Este cambio puede
     introducir cambios de comportamiento en las aplicaciones
     existentes. Por ejemplo, es probable que cambie el orden de
     ejecución de las tareas de la aplicación.

   Added in version 3.12.

asyncio.create_eager_task_factory(custom_task_constructor)

   Cree una fábrica de tareas entusiastas, similar a
   "eager_task_factory()", utilizando el *custom_task_constructor*
   proporcionado al crear una nueva tarea en lugar del "Task"
   predeterminado.

   *custom_task_constructor* debe ser un *callable* con la firma que
   coincida con la firma de "Task.__init__". El invocable debe
   devolver un objeto compatible con "asyncio.Task".

   Esta función devuelve un *callable* destinado a ser utilizado como
   fábrica de tareas de un bucle de eventos a través de
   "loop.set_task_factory(factory)").

   Added in version 3.12.

## Shielding from cancellation

awaitable asyncio.shield(aw)

   Protege un objeto esperable de ser "cancelado".

   Si *aw* es una corrutina, se programa automáticamente como una
   Tarea.

   La declaración:

      task = asyncio.create_task(something())
      res = await shield(task)

   es equivalente a:

      res = await something()

   *excepto* que si la corrutina que lo contiene se cancela, la tarea
   que se ejecuta en "something()" no se cancela. Desde el punto de
   vista de "something()", la cancelación no ocurrió. Aunque su
   invocador siga cancelado, por lo que la expresión "await" sigue
   generando un "CancelledError".

   Si "something()" se cancela por otros medios (es decir, desde
   dentro de sí mismo) eso también cancelaría "shield()".

   Si se desea ignorar por completo la cancelación (no se recomienda)
   la función "shield()" debe combinarse con una cláusula try/except,
   como se indica a continuación:

      task = asyncio.create_task(something())
      try:
          res = await shield(task)
      except CancelledError:
          res = None

   Importante:

     Guarde una referencia a las tareas pasadas a esta función, para
     evitar que una tarea desaparezca a mitad de la ejecución. El
     bucle de eventos solo mantiene referencias débiles a las tareas.
     Una tarea a la que no se hace referencia en ningún otro lugar
     puede  ser recolectada por el recolector de basura en cualquier
     momento, incluso antes de que se complete.

   Distinto en la versión 3.10: Se quitó el parámetro *loop*.

   Obsoleto desde la versión 3.10: Se emite una advertencia de
   obsolescencia si *aw* no es un objeto similares a Futures y no hay
   un bucle de eventos en ejecución.

## Tiempo agotado

asyncio.timeout(delay)

   Un asynchronous context manager que se puede usar para limitar la
   cantidad de tiempo que se pasa esperando algo.

   *delay* puede ser "None" o un número flotante/int de segundos de
   espera. Si *delay* es "None", no se aplicará ningún límite de
   tiempo; esto puede ser útil si se desconoce el retraso cuando se
   crea el administrador de contexto.

   En cualquier caso, el administrador de contexto se puede
   reprogramar después de la creación mediante "Timeout.reschedule()".

   Ejemplo:

      async def main():
          async with asyncio.timeout(10):
              await long_running_task()

   Si "long_running_task" tarda más de 10 segundos en completarse, el
   administrador de contexto cancelará la tarea actual y manejará
   internamente el "asyncio.CancelledError" resultante,
   transformándolo en un "asyncio.TimeoutError" que se puede capturar
   y manejar.

   Nota:

     El administrador de contexto "asyncio.timeout()" es lo que
     transforma el "asyncio.CancelledError" en un
     "asyncio.TimeoutError", lo que significa que el
     "asyncio.TimeoutError" solo puede capturarse *outside* del
     administrador de contexto.

   Ejemplo de captura de "TimeoutError":

      async def main():
          try:
              async with asyncio.timeout(10):
                  await long_running_task()
          except TimeoutError:
              print("The long operation timed out, but we've handled it.")

          print("This statement will run regardless.")

   El administrador de contexto producido por "asyncio.timeout()"
   puede reprogramarse para una fecha límite diferente e
   inspeccionarse.

   class asyncio.Timeout(when)

      Un asynchronous context manager para cancelar corrutinas
      vencidas.

      Prefer using "asyncio.timeout()" or "asyncio.timeout_at()"
      rather than instantiating "Timeout" directly.

      "when" debe ser un tiempo absoluto en el que el contexto debe
      expirar, según lo medido por el reloj del bucle de eventos:

      * Si "when" es "None", el tiempo de espera nunca se activará.

      * Si "when < loop.time()", el tiempo de espera se activará en la
        próxima iteración del bucle de eventos

         when() -> float | None

            Retorna la fecha límite actual, o "None" si la fecha
            límite actual no está establecida.

         reschedule(when: float | None)

            Reprogramar el tiempo de espera.

         expired() -> bool

            Retorna si el administrador de contexto ha excedido su
            fecha límite (caducada).

   Ejemplo:

      async def main():
          try:
              # We do not know the timeout when starting, so we pass ``None``.
              async with asyncio.timeout(None) as cm:
                  # We know the timeout now, so we reschedule it.
                  new_deadline = get_running_loop().time() + 10
                  cm.reschedule(new_deadline)

                  await long_running_task()
          except TimeoutError:
              pass

          if cm.expired():
              print("Looks like we haven't finished on time.")

   Los administradores de contexto de tiempo de espera se pueden
   anidar de forma segura.

   Added in version 3.11.

asyncio.timeout_at(when)

   Similar a "asyncio.timeout()", excepto que *when* es el tiempo
   absoluto para dejar de esperar, o "None".

   Ejemplo:

      async def main():
          loop = get_running_loop()
          deadline = loop.time() + 20
          try:
              async with asyncio.timeout_at(deadline):
                  await long_running_task()
          except TimeoutError:
              print("The long operation timed out, but we've handled it.")

          print("This statement will run regardless.")

   Added in version 3.11.

async asyncio.wait_for(aw, timeout)

   Espere a que el *aw* esperable se complete con un tiempo agotado.

   Si *aw* es una corrutina, se programa automáticamente como una
   Tarea.

   *timeout* puede ser "None" o punto flotante o un número entero de
   segundos a esperar. Si *timeout* es "None", se bloquea hasta que
   Future se completa.

   Si se agota el tiempo de espera, cancela la tarea y lanza
   "TimeoutError".

   Para evitar la "cancelación" de la tarea , envuélvala en
   "shield()".

   La función esperará hasta que se cancele el Future, por lo que el
   tiempo de espera total puede exceder el *timeout*. Si ocurre una
   excepción durante la cancelación, se propaga.

   Si se cancela la espera, el Future *aw* también se cancela.

   Ejemplo:

      async def eternity():
          # Sleep for one hour
          await asyncio.sleep(3600)
          print('yay!')

      async def main():
          # Wait for at most 1 second
          try:
              await asyncio.wait_for(eternity(), timeout=1.0)
          except TimeoutError:
              print('timeout!')

      asyncio.run(main())

      # Expected output:
      #
      #     timeout!

   Distinto en la versión 3.7: Cuando se cancela *aw* debido a un
   tiempo de espera, "wait_for" espera a que se cancele *aw*.
   Anteriormente, lanzaba "TimeoutError" inmediatamente.

   Distinto en la versión 3.10: Se quitó el parámetro *loop*.

   Distinto en la versión 3.11: Raises "TimeoutError" instead of
   "asyncio.TimeoutError".

## Waiting primitives

async asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)

   Ejecuta instancias "Future" y "Task" en el iterable *aws*
   simultáneamente y bloquea hasta la condición especificada por
   *return_when*.

   El iterable *aws* no debe estar vacío.

   Retorna dos conjuntos de Tareas/Futures: "(done, pending)".

   Uso:

      done, pending = await asyncio.wait(aws)

   *timeout* (un punto flotante o int), si se especifica, se puede
   utilizar para controlar el número máximo de segundos que hay que
   esperar antes de retornar.

   Tenga en cuenta que esta función no lanza "TimeoutError". Los
   futuros o las tareas que no se realizan cuando se agota el tiempo
   de espera simplemente se retornan en el segundo conjunto.

   *return_when* indica cuándo debe retornar esta función. Debe ser
   una de las siguientes constantes:

   +----------------------------------------------------+----------------------------------------------------+
   | Constante                                          | Descripción                                        |
   |====================================================|====================================================|
   | asyncio.FIRST_COMPLETED                            | La función retornará cuando cualquier Future       |
   |                                                    | termine o se cancele.                              |
   +----------------------------------------------------+----------------------------------------------------+
   | asyncio.FIRST_EXCEPTION                            | The function will return when any future finishes  |
   |                                                    | by raising an exception. If no future raises an    |
   |                                                    | exception then it is equivalent to                 |
   |                                                    | "ALL_COMPLETED".                                   |
   +----------------------------------------------------+----------------------------------------------------+
   | asyncio.ALL_COMPLETED                              | La función retornará cuando todos los Futures      |
   |                                                    | terminen o se cancelen.                            |
   +----------------------------------------------------+----------------------------------------------------+

   A diferencia de "wait_for()", "wait()" no cancela los Futures
   cuando se produce un agotamiento de tiempo.

   If "wait()" is cancelled, the futures in *aws* are not cancelled
   and continue to run.

   Distinto en la versión 3.10: Se quitó el parámetro *loop*.

   Distinto en la versión 3.11: Está prohibido pasar objetos de rutina
   a "wait()" directamente.

   Distinto en la versión 3.12: Se agregó soporte para generadores que
   generan tareas.

asyncio.as_completed(aws, *, timeout=None)

   Run awaitable objects in the *aws* iterable concurrently. The
   returned object can be iterated to obtain the results of the
   awaitables as they finish.

   The object returned by "as_completed()" can be iterated as an
   *asynchronous iterator* or a plain *iterator*. When asynchronous
   iteration is used, the originally-supplied awaitables are yielded
   if they are tasks or futures. This makes it easy to correlate
   previously-scheduled tasks with their results. Example:

      ipv4_connect = create_task(open_connection("127.0.0.1", 80))
      ipv6_connect = create_task(open_connection("::1", 80))
      tasks = [ipv4_connect, ipv6_connect]

      async for earliest_connect in as_completed(tasks):
          # earliest_connect is done. The result can be obtained by
          # awaiting it or calling earliest_connect.result()
          reader, writer = await earliest_connect

          if earliest_connect is ipv6_connect:
              print("IPv6 connection established.")
          else:
              print("IPv4 connection established.")

   During asynchronous iteration, implicitly-created tasks will be
   yielded for supplied awaitables that aren't tasks or futures.

   When used as a plain iterator, each iteration yields a new
   coroutine that returns the result or raises the exception of the
   next completed awaitable. This pattern is compatible with Python
   versions older than 3.13:

      ipv4_connect = create_task(open_connection("127.0.0.1", 80))
      ipv6_connect = create_task(open_connection("::1", 80))
      tasks = [ipv4_connect, ipv6_connect]

      for next_connect in as_completed(tasks):
          # next_connect is not one of the original task objects. It must be
          # awaited to obtain the result value or raise the exception of the
          # awaitable that finishes next.
          reader, writer = await next_connect

   A "TimeoutError" is raised if the timeout occurs before all
   awaitables are done. This is raised by the "async for" loop during
   asynchronous iteration or by the coroutines yielded during plain
   iteration.

   "as_completed()" does not cancel the tasks running the supplied
   awaitables: if a timeout occurs or the iteration is cancelled, the
   remaining tasks continue to run.

   Distinto en la versión 3.10: Se quitó el parámetro *loop*.

   Obsoleto desde la versión 3.10: Se emite una advertencia de
   obsolescencia si no todos los objetos en espera en el iterable
   *aws* son objetos de tipo Future y no hay un bucle de eventos en
   ejecución.

   Distinto en la versión 3.12: Se agregó soporte para generadores que
   generan tareas.

   Distinto en la versión 3.13: The result can now be used as either
   an *asynchronous iterator* or as a plain *iterator* (previously it
   was only a plain iterator).

## Running in threads

async asyncio.to_thread(func, /, *args, **kwargs)

   Ejecutar asincrónicamente la función *func* en un hilo separado.

   Cualquier *args y **kwargs suministrados para esta función se pasan
   directamente a *func*. Además, el current "contextvars.Context" se
   propaga, lo que permite acceder a las variables de contexto del
   subproceso del bucle de eventos en el subproceso separado.

   Retorna una corrutina que se puede esperar para obtener el
   resultado final de *func*.

   Esta función de rutina está diseñada principalmente para ejecutar
   funciones/métodos vinculados a IO que, de otro modo, bloquearían el
   bucle de eventos si se ejecutaran en el subproceso principal. Por
   ejemplo:

      def blocking_io():
          print(f"start blocking_io at {time.strftime('%X')}")
          # Note that time.sleep() can be replaced with any blocking
          # IO-bound operation, such as file operations.
          time.sleep(1)
          print(f"blocking_io complete at {time.strftime('%X')}")

      async def main():
          print(f"started main at {time.strftime('%X')}")

          await asyncio.gather(
              asyncio.to_thread(blocking_io),
              asyncio.sleep(1))

          print(f"finished main at {time.strftime('%X')}")

      asyncio.run(main())

      # Expected output:
      #
      # started main at 19:50:53
      # start blocking_io at 19:50:53
      # blocking_io complete at 19:50:54
      # finished main at 19:50:54

   Llamar directamente a "blocking_io()" en cualquier rutina
   bloquearía el bucle de eventos durante su duración, lo que daría
   como resultado 1 segundo adicional de tiempo de ejecución. En
   cambio, al usar "asyncio.to_thread()", podemos ejecutarlo en un
   subproceso separado sin bloquear el ciclo de eventos.

   Nota:

     Debido a *GIL*, "asyncio.to_thread()" generalmente solo se puede
     usar para hacer que las funciones vinculadas a IO no bloqueen.
     Sin embargo, para los módulos de extensión que lanzan GIL o
     implementaciones alternativas de Python que no tienen uno,
     "asyncio.to_thread()" también se puede usar para funciones
     vinculadas a la CPU.

   Added in version 3.9.

## Scheduling from other threads

asyncio.run_coroutine_threadsafe(coro, loop)

   Envía una corrutina al bucle de eventos especificado. Seguro para
   Hilos.

   Retorna "concurrent.futures.Future" para esperar el resultado de
   otro hilo del SO (Sistema Operativo).

   Esta función está pensada para llamarse desde un hilo del SO
   diferente al que se ejecuta el bucle de eventos. Ejemplo:

      def in_thread(loop: asyncio.AbstractEventLoop) -> None:
          # Run some blocking IO
          pathlib.Path("example.txt").write_text("hello world", encoding="utf8")

          # Create a coroutine
          coro = asyncio.sleep(1, result=3)

          # Submit the coroutine to a given loop
          future = asyncio.run_coroutine_threadsafe(coro, loop)

          # Wait for the result with an optional timeout argument
          assert future.result(timeout=2) == 3

      async def amain() -> None:
          # Get the running loop
          loop = asyncio.get_running_loop()

          # Run something in a thread
          await asyncio.to_thread(in_thread, loop)

   It's also possible to run the other way around.  Example:

      @contextlib.contextmanager
      def loop_in_thread() -> Generator[asyncio.AbstractEventLoop]:
          loop_fut = concurrent.futures.Future[asyncio.AbstractEventLoop]()
          stop_event = asyncio.Event()

          async def main() -> None:
              loop_fut.set_result(asyncio.get_running_loop())
              await stop_event.wait()

          with concurrent.futures.ThreadPoolExecutor(1) as tpe:
              complete_fut = tpe.submit(asyncio.run, main())
              for fut in concurrent.futures.as_completed((loop_fut, complete_fut)):
                  if fut is loop_fut:
                      loop = loop_fut.result()
                      try:
                          yield loop
                      finally:
                          loop.call_soon_threadsafe(stop_event.set)
                  else:
                      fut.result()

      # Create a loop in another thread
      with loop_in_thread() as loop:
          # Create a coroutine
          coro = asyncio.sleep(1, result=3)

          # Submit the coroutine to a given loop
          future = asyncio.run_coroutine_threadsafe(coro, loop)

          # Wait for the result with an optional timeout argument
          assert future.result(timeout=2) == 3

   Si se lanza una excepción en la corrutina, el Future retornado será
   notificado. También se puede utilizar para cancelar la tarea en el
   bucle de eventos:

      try:
          result = future.result(timeout)
      except TimeoutError:
          print('The coroutine took too long, cancelling the task...')
          future.cancel()
      except Exception as exc:
          print(f'The coroutine raised an exception: {exc!r}')
      else:
          print(f'The coroutine returned: {result!r}')

   Consulte la sección de la documentación Concurrencia y multi hilos.

   A diferencia de otras funciones asyncio, esta función requiere que
   el argumento *loop* se pase explícitamente.

   Added in version 3.5.1.

## Introspección

asyncio.current_task(loop=None)

   Retorna la instancia "Task" actualmente en ejecución o "None" si no
   se está ejecutando ninguna tarea.

   Si *loop* es "None" "get_running_loop()" se utiliza para obtener el
   bucle actual.

   Added in version 3.7.

asyncio.all_tasks(loop=None)

   Retorna un conjunto de objetos "Task" que se ejecutan por el bucle.

   Si *loop* es "None", "get_running_loop()" se utiliza para obtener
   el bucle actual.

   Added in version 3.7.

asyncio.iscoroutine(obj)

   Retorna "True" si *obj* es un objeto corutina.

   Added in version 3.4.

## Task object

class asyncio.Task(coro, *, loop=None, name=None, context=None, eager_start=False)

   Un objeto "similar a Future" que ejecuta Python coroutine. No es
   seguro hilos.

   Las tareas se utilizan para ejecutar corrutinas en bucles de
   eventos. Si una corrutina aguarda en un Future, la Tarea suspende
   la ejecución de la corrutina y espera la finalización del Future.
   Cuando el Future *termina*, se reanuda la ejecución de la corrutina
   envuelta.

   Los bucles de eventos usan la programación cooperativa: un bucle de
   eventos ejecuta una tarea a la vez. Mientras una Tarea espera para
   la finalización de un Future, el bucle de eventos ejecuta otras
   tareas, retorno de llamada o realiza operaciones de E/S.

   Utilice la función de alto nivel "asyncio.create_task()" para crear
   Tareas, o las funciones de bajo nivel "loop.create_task()" o
   "ensure_future()". Se desaconseja la creación de instancias
   manuales de Tareas.

   Para cancelar una Tarea en ejecución, utilice el método "cancel()".
   Llamarlo hará que la tarea lance una excepción "CancelledError" en
   la corrutina contenida. Si una corrutina está esperando en un
   objeto Future durante la cancelación, se cancelará el objeto
   Future.

   "cancelled()" se puede utilizar para comprobar si la Tarea fue
   cancelada. El método retorna "True" si la corrutina contenida no
   suprimió la excepción "CancelledError" y se canceló realmente.

   "asyncio.Task" hereda de "Future" todas sus API excepto
   "Future.set_result()" y "Future.set_exception()".

   Un argumento *context* opcional de solo palabra clave permite
   especificar un "contextvars.Context" personalizado para que se
   ejecute *coro*. Si no se proporciona ningún *context*, la tarea
   copia el contexto actual y luego ejecuta su rutina en el contexto
   copiado.

   Un argumento *eager_start* opcional de solo palabra clave permite
   iniciar con entusiasmo la ejecución de "asyncio.Task" en el momento
   de la creación de la tarea. Si se establece en "True" y el bucle de
   eventos se está ejecutando, la tarea comenzará a ejecutar la
   corrutina inmediatamente, hasta la primera vez que la corrutina se
   bloquee. Si la rutina regresa o se activa sin bloquearse, la tarea
   finalizará con entusiasmo y saltará la programación al bucle de
   eventos.

   Tasks are generic over the return type of their wrapped coroutines.

   Distinto en la versión 3.7: Agregado soporte para el módulo
   "contextvars".

   Distinto en la versión 3.8: Se ha añadido el parámetro *name*.

   Obsoleto desde la versión 3.10: Se emite una advertencia de
   obsolescencia si no se especifica *loop* y no hay un bucle de
   eventos en ejecución.

   Distinto en la versión 3.11: Se ha añadido el parámetro *context*.

   Distinto en la versión 3.12: Se ha añadido el parámetro
   *eager_start*.

   done()

      Retorna "True" si la Tarea está *finalizada*.

      Una tarea está *finalizada* cuando la corrutina contenida
      retornó un valor, lanzó una excepción, o se canceló la Tarea.

   result()

      Retorna el resultado de la Tarea.

      Si la tarea está *terminada*, se retorna el resultado de la
      corrutina contenida (o si la corrutina lanzó una excepción, esa
      excepción se vuelve a relanzar.)

      Si la Tarea ha sido *cancelada*, este método lanza una excepción
      "CancelledError".

      If the Task's result isn't yet available, this method raises an
      "InvalidStateError" exception.

   exception()

      Retorna la excepción de la Tarea.

      Si la corrutina contenida lanzó una excepción, esa excepción es
      retornada. Si la corrutina contenida retorna normalmente, este
      método retorna "None".

      Si la Tarea ha sido *cancelada*, este método lanza una excepción
      "CancelledError".

      Si la Tarea aún no está *terminada*, este método lanza una
      excepción "InvalidStateError".

   add_done_callback(callback, *, context=None)

      Agrega una retro llamada que se ejecutará cuando la Tarea esté
      *terminada*.

      Este método solo se debe usar en código basado en retrollamada
      de bajo nivel.

      Consulte la documentación de "Future.add_done_callback()" para
      obtener más detalles.

   remove_done_callback(callback)

      Remueve la *retrollamada* de la lista de retrollamadas.

      Este método solo se debe usar en código basado en retrollamada
      de bajo nivel.

      Consulte la documentación de "Future.remove_done_callback()"
      para obtener más detalles.

   get_stack(*, limit=None)

      Retorna la lista de marcos de pila para esta tarea.

      Si la corrutina contenida no se termina, esto retorna la pila
      donde se suspende. Si la corrutina se ha completado
      correctamente o se ha cancelado, retorna una lista vacía. Si la
      corrutina terminó por una excepción, esto retorna la lista de
      marcos de seguimiento.

      Los marcos siempre se ordenan de más antiguo a más nuevo.

      Solo se retorna un marco de pila para una corrutina suspendida.

      El argumento opcional *limit* establece el número máximo de
      marcos que se retornarán; de forma predeterminada se retornan
      todos los marcos disponibles. El orden de la lista retornada
      varía en función de si se retorna una pila o un *traceback*: se
      retornan los marcos más recientes de una pila, pero se retornan
      los marcos más antiguos de un *traceback*. (Esto coincide con el
      comportamiento del módulo traceback.)ss

   print_stack(*, limit=None, file=None)

      Imprime la pila o el seguimiento de esta tarea.

      Esto produce una salida similar a la del módulo traceback para
      los marcos recuperados por "get_stack()".

      El argumento *limit* se pasa directamente a "get_stack()".

      El argumento *file* es un flujo de E/S en el que se escribe la
      salida; por defecto, la salida se escribe en "sys.stdout".

   get_coro()

      Retorna el objeto corrutina contenido por "Task".

      Nota:

        Esto devolverá "None" para las tareas que ya se han completado
        con entusiasmo. Consulte el Eager Task Factory.

      Added in version 3.8.

      Distinto en la versión 3.12: La ejecución ansiosa de la tarea
      recientemente agregada significa que el resultado puede ser
      "None".

   get_context()

      Devuelve el objeto "contextvars.Context" asociado con la tarea.

      Added in version 3.12.

   get_name()

      Retorna el nombre de la Tarea.

      Si no se ha asignado explícitamente ningún nombre a la Tarea, la
      implementación de Tarea asyncio predeterminada genera un nombre
      predeterminado durante la creación de instancias.

      Added in version 3.8.

   set_name(value)

      Establece el nombre de la Tarea.

      El argumento *value* puede ser cualquier objeto, que luego se
      convierte en una cadena.

      En la implementación de Task predeterminada, el nombre será
      visible en la salida "repr()" de un objeto de tarea.

      Added in version 3.8.

   cancel(msg=None)

      Solicita que se cancele la Tarea.

      If the Task is already *done* or *cancelled*, return "False",
      otherwise, return "True".

      The method arranges for a "CancelledError" exception to be
      thrown into the wrapped coroutine on the next cycle of the event
      loop.

      Luego, la corrutina tiene la oportunidad de limpiar o incluso
      denegar la solicitud suprimiendo la excepción con un bloque
      "try"... ... "except CancelledError"... "finally". Por lo tanto,
      a diferencia de "Future.cancel()", "Task.cancel()" no garantiza
      que la tarea se cancelará, aunque suprimir la cancelación por
      completo no es común y se desaconseja activamente. Sin embargo,
      si la rutina decide suprimir la cancelación, debe llamar a
      "Task.uncancel()" además de detectar la excepción.

      Distinto en la versión 3.9: Se agregó el parámetro *msg*.

      Distinto en la versión 3.11: El parámetro "msg" se propaga desde
      la tarea cancelada a su espera.

      En el ejemplo siguiente se muestra cómo las corrutinas pueden
      interceptar la solicitud de cancelación:

         async def cancel_me():
             print('cancel_me(): before sleep')

             try:
                 # Wait for 1 hour
                 await asyncio.sleep(3600)
             except asyncio.CancelledError:
                 print('cancel_me(): cancel sleep')
                 raise
             finally:
                 print('cancel_me(): after sleep')

         async def main():
             # Create a "cancel_me" Task
             task = asyncio.create_task(cancel_me())

             # Wait for 1 second
             await asyncio.sleep(1)

             task.cancel()
             try:
                 await task
             except asyncio.CancelledError:
                 print("main(): cancel_me is cancelled now")

         asyncio.run(main())

         # Expected output:
         #
         #     cancel_me(): before sleep
         #     cancel_me(): cancel sleep
         #     cancel_me(): after sleep
         #     main(): cancel_me is cancelled now

   cancelled()

      Retorna "True" si la Tarea se *cancela*.

      La tarea se *cancela* cuando se solicitó la cancelación con
      "cancel()" y la corrutina contenida propagó la excepción
      "CancelledError" que se le ha lanzado.

   uncancel()

      Disminuye el recuento de solicitudes de cancelación a esta
      tarea.

      Retorna el número restante de solicitudes de cancelación.

      Tenga en cuenta que una vez que se completa la ejecución de una
      tarea cancelada, las llamadas posteriores a "uncancel()" no son
      efectivas.

      Added in version 3.11.

      Este método lo usan los componentes internos de asyncio y no se
      espera que lo use el código del usuario final. En particular, si
      una Tarea se cancela con éxito, esto permite que elementos de
      concurrencia estructurada como Task groups y "asyncio.timeout()"
      continúen ejecutándose, aislando la cancelación al bloque
      estructurado respectivo. Por ejemplo:

         async def make_request_with_timeout():
             try:
                 async with asyncio.timeout(1):
                     # Structured block affected by the timeout:
                     await make_request()
                     await make_another_request()
             except TimeoutError:
                 log("There was a timeout")
             # Outer code not affected by the timeout:
             await unrelated_code()

      Si bien el bloque con "make_request()" y
      "make_another_request()" podría cancelarse debido al tiempo de
      espera, "unrelated_code()" debería continuar ejecutándose
      incluso en caso de que se agote el tiempo de espera. Esto se
      implementa con "uncancel()". Los administradores de contexto
      "TaskGroup" usan "uncancel()" de manera similar.

      If end-user code is, for some reason, suppressing cancellation
      by catching "CancelledError", it needs to call this method to
      remove the cancellation state.

      When this method decrements the cancellation count to zero, the
      method checks if a previous "cancel()" call had arranged for
      "CancelledError" to be thrown into the task. If it hasn't been
      thrown yet, that arrangement will be rescinded (by resetting the
      internal "_must_cancel" flag).

   Distinto en la versión 3.13: Changed to rescind pending
   cancellation requests upon reaching zero.

   cancelling()

      Retorna el número de solicitudes de cancelación pendientes a
      esta Tarea, es decir, el número de llamadas a "cancel()" menos
      el número de llamadas a "uncancel()".

      Tenga en cuenta que si este número es mayor que cero pero la
      tarea aún se está ejecutando, "cancelled()" aún retornará
      "False". Esto se debe a que este número se puede reducir
      llamando a "uncancel()", lo que puede provocar que la tarea no
      se cancele después de todo si las solicitudes de cancelación se
      reducen a cero.

      Este método lo utilizan las partes internas de asyncio y no se
      espera que lo utilice el código del usuario final. Consulte
      "uncancel()" para obtener más detalles.

      Added in version 3.11.
