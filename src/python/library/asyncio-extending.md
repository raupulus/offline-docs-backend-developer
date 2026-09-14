---
title: Extensión
source_url: https://docs.python.org/es/3
source_path: library/asyncio-extending.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1620
---

# Extensión

La dirección principal para extender "asyncio" es escribir clases
*event loop* personalizadas. Asyncio tiene ayudantes que podrían
usarse para simplificar esta tarea.

Nota:

  Los terceros deben reutilizar el código asyncio existente con
  precaución, una nueva versión de Python es gratuita para romper la
  compatibilidad con versiones anteriores en la parte *internal* de la
  API.

## Escribir un bucle de eventos personalizado

"asyncio.AbstractEventLoop" declara muchos métodos. Implementarlos
todos desde cero es un trabajo tedioso.

Un bucle puede obtener la implementación de muchos métodos comunes de
forma gratuita al heredar de "asyncio.BaseEventLoop".

A su vez, el sucesor debería implementar un montón de métodos
*privados* declarados pero no implementados en
"asyncio.BaseEventLoop".

Por ejemplo, "loop.create_connection()" comprueba los argumentos,
resuelve las direcciones DNS y llama a "loop._make_socket_transport()"
que debería implementar la clase heredada. El método
"_make_socket_transport()" no está documentado y se considera como una
API *internal*.

## Constructores privados Future y Task

"asyncio.Future" y "asyncio.Task" nunca deben crearse directamente; en
su lugar, utilice las fábricas "loop.create_future()" y
"loop.create_task()" o "asyncio.create_task()" correspondientes.

Sin embargo, *event loops* de terceros puede *reuse* incorporar
futuras implementaciones y tareas con el fin de obtener un código
complejo y altamente optimizado de forma gratuita.

Para ello se listan los siguientes constructores *private*:

Future.__init__(*, loop=None)

   Cree una instancia futura integrada.

   *loop* es una instancia de bucle de eventos opcional.

Task.__init__(coro, *, loop=None, name=None, context=None)

   Cree una instancia de tarea integrada.

   *loop* es una instancia de bucle de eventos opcional. El resto de
   argumentos se describen en la descripción de "loop.create_task()".

   Distinto en la versión 3.11: Se agrega el argumento *context*.

## Soporte de por vida de tareas

La implementación de una tarea de terceros debe llamar a las
siguientes funciones para mantener una tarea visible para
"asyncio.all_tasks()" y "asyncio.current_task()":

asyncio._register_task(task)

   Registre un nuevo *task* como administrado por *asyncio*.

   Llame a la función desde un constructor de tareas.

asyncio._unregister_task(task)

   Anule el registro de un *task* de las estructuras internas de
   *asyncio*.

   La función debe llamarse cuando una tarea está a punto de
   finalizar.

asyncio._enter_task(loop, task)

   Cambie la tarea actual al argumento *task*.

   Llame a la función justo antes de ejecutar una parte del
   *coroutine* incrustado ("coroutine.send()" o "coroutine.throw()").

asyncio._leave_task(loop, task)

   Vuelva a cambiar la tarea actual de *task* a "None".

   Llame a la función justo después de la ejecución de
   "coroutine.send()" o "coroutine.throw()".
