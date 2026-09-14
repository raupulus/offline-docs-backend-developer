---
title: '"sys.monitoring" --- Execution event monitoring'
source_url: https://docs.python.org/es/3
source_path: library/sys.monitoring.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4000
---

# "sys.monitoring" --- Execution event monitoring

Added in version 3.12.

======================================================================

Nota:

  "sys.monitoring" is a namespace within the "sys" module, not an
  independent module, and "import sys.monitoring" would fail with a
  "ModuleNotFoundError". Instead, simply "import sys" and then use
  "sys.monitoring".

Este espacio de nombres proporciona acceso a las funciones y
constantes necesarias para activar y controlar el monitoreo de
eventos.

As programs execute, events occur that might be of interest to tools
that monitor execution. The "sys.monitoring" namespace provides means
to receive callbacks when events of interest occur.

La API de monitoreo consta de tres componentes:

* Tool identifiers

* Events

* Callbacks

## Identificadores de herramientas

A tool identifier is an integer and the associated name. Tool
identifiers are used to discourage tools from interfering with each
other and to allow multiple tools to operate at the same time.
Currently tools are completely independent and cannot be used to
monitor each other. This restriction may be lifted in the future.

Before registering or activating events, a tool should choose an
identifier. Identifiers are integers in the range 0 to 5 inclusive.

### Registro y uso de herramientas

sys.monitoring.use_tool_id(tool_id: int, name: str, /) -> None

   Must be called before *tool_id* can be used. *tool_id* must be in
   the range 0 to 5 inclusive. Raises a "ValueError" if *tool_id* is
   in use.

sys.monitoring.clear_tool_id(tool_id: int, /) -> None

   Unregister all events and callback functions associated with
   *tool_id*.

sys.monitoring.free_tool_id(tool_id: int, /) -> None

   Should be called once a tool no longer requires *tool_id*. Will
   call "clear_tool_id()" before releasing *tool_id*.

sys.monitoring.get_tool(tool_id: int, /) -> str | None

   Returns the name of the tool if *tool_id* is in use, otherwise it
   returns "None". *tool_id* must be in the range 0 to 5 inclusive.

La máquina virtual trata todos los ID de la misma manera con respecto
a los eventos, pero los siguientes ID están predefinidos para
facilitar la cooperación de las herramientas:

   sys.monitoring.DEBUGGER_ID = 0
   sys.monitoring.COVERAGE_ID = 1
   sys.monitoring.PROFILER_ID = 2
   sys.monitoring.OPTIMIZER_ID = 5

## Eventos

Son aceptados los siguientes eventos:

sys.monitoring.events.BRANCH_LEFT

   A conditional branch goes left.

   It is up to the tool to determine how to present "left" and "right"
   branches. There is no guarantee which branch is "left" and which is
   "right", except that it will be consistent for the duration of the
   program.

sys.monitoring.events.BRANCH_RIGHT

   A conditional branch goes right.

sys.monitoring.events.CALL

   Una llamada en código Python (el evento ocurre antes de la
   llamada).

sys.monitoring.events.C_RAISE

   An exception raised from any callable, except for Python functions
   (event occurs after the exit).

sys.monitoring.events.C_RETURN

   Return from any callable, except for Python functions (event occurs
   after the return).

sys.monitoring.events.EXCEPTION_HANDLED

   Se maneja una excepción.

sys.monitoring.events.INSTRUCTION

   Está a punto de ejecutarse una instrucción de VM.

sys.monitoring.events.JUMP

   Se realiza un salto incondicional en el gráfico de flujo de
   control.

sys.monitoring.events.LINE

   Está a punto de ejecutarse una instrucción que tiene un número de
   línea diferente al de la instrucción anterior.

sys.monitoring.events.PY_RESUME

   Resumption of a Python function (for generator and coroutine
   functions), except for "throw()" calls.

sys.monitoring.events.PY_RETURN

   Retorna de una función Python (ocurre inmediatamente antes del
   retorno, el marco del destinatario estará en la pila).

sys.monitoring.events.PY_START

   Inicio de una función Python (ocurre inmediatamente después de la
   llamada, el marco del destinatario estará en la pila)

sys.monitoring.events.PY_THROW

   A Python function is resumed by a "throw()" call.

sys.monitoring.events.PY_UNWIND

   Exit from a Python function during exception unwinding. This
   includes exceptions raised directly within the function and that
   are allowed to continue to propagate.

sys.monitoring.events.PY_YIELD

   Rinde (*yield*) desde una función Python (ocurre inmediatamente
   antes del rendimiento, el marco del destinatario estará en la
   pila).

sys.monitoring.events.RAISE

   An exception is raised, except those that cause a "STOP_ITERATION"
   event.

sys.monitoring.events.RERAISE

   An exception is re-raised, for example at the end of a "finally"
   block.

sys.monitoring.events.STOP_ITERATION

   An artificial "StopIteration" is raised; see the STOP_ITERATION
   event.

Es posible que se agreguen más eventos en el futuro.

These events are attributes of the "sys.monitoring.events" namespace.
Each event is represented as a power-of-2 integer constant. To define
a set of events, simply bitwise OR the individual events together. For
example, to specify both "PY_RETURN" and "PY_START" events, use the
expression "PY_RETURN | PY_START".

sys.monitoring.events.NO_EVENTS

   An alias for "0" so users can do explicit comparisons like:

      if get_events(DEBUGGER_ID) == NO_EVENTS:
          ...

   Setting this event deactivates all events.

### Eventos locales

Los eventos locales están asociados con la ejecución normal del
programa y ocurren en lugares claramente definidos. Todos los eventos
locales se pueden desactivar. Los eventos locales son:

* "PY_START"

* "PY_RESUME"

* "PY_RETURN"

* "PY_YIELD"

* "CALL"

* "LINE"

* "INSTRUCTION"

* "JUMP"

* "BRANCH_LEFT"

* "BRANCH_RIGHT"

* "STOP_ITERATION"

### Deprecated event

* "BRANCH"

The "BRANCH" event is deprecated in 3.14. Using "BRANCH_LEFT" and
"BRANCH_RIGHT" events will give much better performance as they can be
disabled independently.

### Eventos auxiliares

Los eventos auxiliares se pueden monitorear como otros eventos, pero
están controlados por otros eventos:

* "C_RAISE"

* "C_RETURN"

The "C_RETURN" and "C_RAISE" events are controlled by the "CALL"
event. "C_RETURN" and "C_RAISE" events will only be seen if the
corresponding "CALL" event is being monitored.

### Otros eventos

Other events are not necessarily tied to a specific location in the
program and cannot be individually disabled via "DISABLE".

Los otros eventos que se pueden monitorear son:

* "PY_THROW"

* "PY_UNWIND"

* "RAISE"

* "EXCEPTION_HANDLED"

### El evento STOP_ITERATION

**PEP 380** specifies that a "StopIteration" exception is raised when
returning a value from a generator or coroutine. However, this is a
very inefficient way to return a value, so some Python
implementations, notably CPython 3.12+, do not raise an exception
unless it would be visible to other code.

To allow tools to monitor for real exceptions without slowing down
generators and coroutines, the "STOP_ITERATION" event is provided.
"STOP_ITERATION" can be locally disabled, unlike "RAISE".

Note that the "STOP_ITERATION" event and the "RAISE" event for a
"StopIteration" exception are equivalent, and are treated as
interchangeable when generating events. Implementations will favor
"STOP_ITERATION" for performance reasons, but may generate a "RAISE"
event with a "StopIteration".

## Activar y desactivar eventos

In order to monitor an event, it must be turned on and a corresponding
callback must be registered. Events can be turned on or off by setting
the events either globally and/or for a particular code object. An
event will trigger only once, even if it is turned on both globally
and locally.

### Configuración de eventos globalmente

Los eventos se pueden controlar globalmente modificando el conjunto de
eventos que están siendo monitoreados.

sys.monitoring.get_events(tool_id: int, /) -> int

   Retorna el "int" que representa todos los eventos activos.

sys.monitoring.set_events(tool_id: int, event_set: int, /) -> None

   Activates all events which are set in *event_set*. Raises a
   "ValueError" if *tool_id* is not in use.

No hay eventos activos de forma predeterminada.

### Eventos por objeto de código

Events can also be controlled on a per code object basis. The
functions defined below which accept a "types.CodeType" should be
prepared to accept a look-alike object from functions which are not
defined in Python (see Monitoring C API).

sys.monitoring.get_local_events(tool_id: int, code: CodeType, /) -> int

   Returns all the local events for *code*

sys.monitoring.set_local_events(tool_id: int, code: CodeType, event_set: int, /) -> None

   Activates all the local events for *code* which are set in
   *event_set*. Raises a "ValueError" if *tool_id* is not in use.

### Deshabilitando eventos

sys.monitoring.DISABLE

   A special value that can be returned from a callback function to
   disable events for the current code location.

Local events can be disabled for a specific code location by returning
"sys.monitoring.DISABLE" from a callback function. This does not
change which events are set, or any other code locations for the same
event.

Deshabilitar eventos para ubicaciones específicas es muy importante
para el monitoreo de alto rendimiento. Por ejemplo, un programa se
puede ejecutar con un depurador sin gastos adicionales si el depurador
desactiva toda la supervisión excepto algunos puntos de interrupción.

If "DISABLE" is returned by a callback for a global event,
"ValueError" will be raised by the interpreter in a non-specific
location (that is, no traceback will be provided).

sys.monitoring.restart_events() -> None

   Enable all the events that were disabled by
   "sys.monitoring.DISABLE" for all tools.

## Registrando funciones de retrollamada

sys.monitoring.register_callback(tool_id: int, event: int, func: Callable | None, /) -> Callable | None

   Registers the callable *func* for the *event* with the given
   *tool_id*

   If another callback was registered for the given *tool_id* and
   *event*, it is unregistered and returned. Otherwise
   "register_callback()" returns "None".

   Raises an auditing event "sys.monitoring.register_callback" with
   argument "func".

Funciones pueden ser canceladas llamando
"sys.monitoring.register_callback(tool_id, event, None)".

Las funciones de retrollamada se pueden registrar y cancelar en
cualquier momento.

Callbacks are called only once regardless if the event is turned on
both globally and locally. As such, if an event could be turned on for
both global and local events by your code then the callback needs to
be written to handle either trigger.

### Argumentos de la función de retrollamada

sys.monitoring.MISSING

   A special value that is passed to a callback function to indicate
   that there are no arguments to the call.

When an active event occurs, the registered callback function is
called. Callback functions returning an object other than "DISABLE"
will have no effect. Different events will provide the callback
function with different arguments, as follows:

* "PY_START" and "PY_RESUME":

     func(code: CodeType, instruction_offset: int) -> object

* "PY_RETURN" and "PY_YIELD":

     func(code: CodeType, instruction_offset: int, retval: object) -> object

* "CALL", "C_RAISE" and "C_RETURN" (*arg0* can be "MISSING"
  specifically):

     func(code: CodeType, instruction_offset: int, callable: object, arg0: object) -> object

  *code* represents the code object where the call is being made,
  while *callable* is the object that is about to be called (and thus
  triggered the event). If there are no arguments, *arg0* is set to
  "sys.monitoring.MISSING".

  For instance methods, *callable* will be the function object as
  found on the class with *arg0* set to the instance (i.e. the "self"
  argument to the method).

* "RAISE", "RERAISE", "EXCEPTION_HANDLED", "PY_UNWIND", "PY_THROW" and
  "STOP_ITERATION":

     func(code: CodeType, instruction_offset: int, exception: BaseException) -> object

* "LINE":

     func(code: CodeType, line_number: int) -> object

* "BRANCH_LEFT", "BRANCH_RIGHT" and "JUMP":

     func(code: CodeType, instruction_offset: int, destination_offset: int) -> object

  Note that the *destination_offset* is where the code will next
  execute.

* "INSTRUCTION":

     func(code: CodeType, instruction_offset: int) -> object
