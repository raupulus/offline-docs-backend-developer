---
title: '"asyncio" --- Asynchronous I/O'
source_url: https://docs.python.org/es/3
source_path: library/asyncio.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1770
---

# "asyncio" --- Asynchronous I/O

======================================================================

##### ¡Hola Mundo!

   import asyncio

   async def main():
       print('Hello ...')
       await asyncio.sleep(1)
       print('... World!')

   asyncio.run(main())

asyncio es una biblioteca para escribir código **concurrente**
utilizando la sintaxis **async/await**.

asyncio es utilizado como base en múltiples *frameworks* asíncronos de
Python y provee un alto rendimiento en redes y servidores web,
bibliotecas de conexión de base de datos, colas de tareas
distribuidas, etc.

asyncio suele encajar perfectamente para operaciones con límite de E/S
y código de red **estructurado** de alto nivel.

Ver también:

  A Conceptual Overview of asyncio
     Explanation of the fundamentals of asyncio.

asyncio provee un conjunto de *APIs* de **alto nivel** para:

* ejecutar corutinas de Python de manera concurrente y tener control
  total sobre su ejecución;

* realizar redes E/S y comunicación entre procesos(IPC);

* controlar subprocesos;

* distribuir tareas a través de colas;

* sincronizar código concurrente;

For **introspection**, asyncio provides APIs and tools for:

* inspecting the async call graph of tasks and futures;

* inspecting tasks in another running Python process with command-line
  tools;

Adicionalmente, existen *APIs* de **bajo nivel** para *desarrolladores
de bibliotecas y frameworks* para:

* create and manage event loops, which provide asynchronous APIs for
  networking, running subprocesses, handling OS signals, etc;

* implementar protocolos eficientes utilizando transportes;

* Bibliotecas puente basadas en retrollamadas y código con sintaxis
  *async/wait*.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

-[ asyncio REPL ]-

You can experiment with an "asyncio" concurrent context in the *REPL*:

   $ python -m asyncio
   asyncio REPL ...
   Use "await" directly instead of "asyncio.run()".
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import asyncio
   >>> await asyncio.sleep(10, result='hello')
   'hello'

This REPL provides limited compatibility with "PYTHON_BASIC_REPL". It
is recommended that the default REPL is used for full functionality
and the latest features.

Raises an auditing event "cpython.run_stdin" with no arguments.

Distinto en la versión 3.12.5: (also 3.11.10, 3.10.15, 3.9.20, and
3.8.20) Emits audit events.

Distinto en la versión 3.13: Uses PyREPL if possible, in which case
"PYTHONSTARTUP" is also executed. Emits audit events.

-[ Referencias ]-

##### *APIs* de alto nivel

* Runners

* Coroutines and tasks

* Streams

* Primitivas de sincronización

* Sub-procesos

* Colas

* Excepciones

##### Introspection APIs

* Call graph introspection

* Command-line introspection tools

##### *APIs* de bajo nivel

* Event loop

* Futures

* Transportes y protocolos

* Políticas

* Soporte de plataforma

* Extensión

##### Guías y tutoriales

* Índice de API de alto nivel

* Índice de API de bajo nivel

* Desarrollando con asyncio

* asyncio and free-threaded Python

Nota:

  El código fuente para asyncio puede encontrarse en Lib/asyncio/.
