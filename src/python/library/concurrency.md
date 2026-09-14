---
title: Ejecución concurrente
source_url: https://docs.python.org/es/3
source_path: library/concurrency.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2060
---

# Ejecución concurrente

Los módulos descritos en este capítulo proveen soporte para la
ejecución concurrente de código. La elección de qué herramienta
utilizar depende de la tarea a ejecutar (vinculada a CPU o vinculada a
E/S) y del estilo preferido de desarrollo (multi-tarea cooperativa o
multi-tarea apropiativa). A continuación se muestra un resumen:

* "threading" --- Thread-based parallelism

  * Introduction

  * GIL and performance considerations

  * Reference

    * Thread-local data

    * Thread objects

    * Lock objects

    * RLock objects

    * Condition objects

    * Semaphore objects

    * "Semaphore" example

    * Event objects

    * Timer objects

    * Barrier objects

  * Uso de *locks*, condiciones y semáforos en la declaración "with"

* "multiprocessing" --- Process-based parallelism

  * Introducción

    * La clase "Process"

    * Contextos y métodos de inicio

    * Intercambiando objetos entre procesos

    * Sincronización entre procesos

    * Compartiendo estado entre procesos

    * Usando una piscina de trabajadores (*pool of workers*)

  * Referencia

    * Global start method

    * "Process" y excepciones

    * Tuberías (*Pipes*) y Colas (*Queues*)

    * Miscelánea

    * Objetos de conexión *Connection Objects*

    * Primitivas de sincronización (*Synchronization primitives*)

    * Objetos compartidos "ctypes"

      * The "multiprocessing.sharedctypes" module

    * Administradores (*Managers*)

      * Administradores customizables (*Customized managers*)

      * Utilizando un administrador remoto

    * Objetos Proxy (*Proxy Objects*)

      * Limpieza (*Cleanup*)

    * Piscinas de procesos (*Process Pools*)

    * Oyentes y clientes (*Listeners and Clients*)

      * Formatos de dirección (*Address formats*)

    * Llaves de autentificación

    * *Logging*

    * The "multiprocessing.dummy" module

  * Pautas de programación

    * Todos los métodos de inicio

    * Los métodos de inicio *spawn* y *forkserver*

  * Ejemplos

* "multiprocessing.shared_memory" --- Shared memory for direct access
  across processes

* El paquete "concurrent"

* "concurrent.futures" --- Launching parallel tasks

  * Objetos ejecutores

  * ThreadPoolExecutor

    * Ejemplo de ThreadPoolExecutor

  * InterpreterPoolExecutor

  * ProcessPoolExecutor

    * Ejemplo de *ProcessPoolExecutor*

  * Objetos futuro

  * Funciones del módulo

  * Clases de Excepciones

* "concurrent.interpreters" --- Multiple interpreters in the same
  process

  * Key details

  * Introduction

    * Multiple Interpreters and Isolation

    * Running in an Interpreter

    * Concurrency and Parallelism

    * Communication Between Interpreters

    * "Sharing" Objects

  * Reference

    * Interpreter objects

    * Exceptions

    * Communicating Between Interpreters

  * Basic usage

* "subprocess" --- Subprocess management

  * Using the "subprocess" Module

    * Argumentos frecuentemente empleados

    * El constructor de Popen

    * Excepciones

  * Consideraciones sobre seguridad

  * Objetos Popen

  * Elementos auxiliares de Popen en Windows

    * Constantes de Windows

  * Antigua API de alto nivel

  * Replacing Older Functions with the "subprocess" Module

    * Cómo reemplazar la sustitución de órdenes de **/bin/sh**

    * Cómo remplazar los flujos de la shell

    * Cómo reemplazar "os.system()"

    * Cómo reemplazar la familia "os.spawn"

    * Replacing "os.popen()"

  * Funciones de llamada a la shell de retrocompatibilidad

  * Notas

    * Timeout Behavior

    * Cómo convertir una secuencia de argumentos a una cadena en
      Windows

    * Disable use of "posix_spawn()"

* "sched" --- Event scheduler

  * Objetos de "Scheduler"

* "queue" --- A synchronized queue class

  * Objetos de la cola

    * Waiting for task completion

    * Terminating queues

  * Objetos de cola simple

* "contextvars" --- Context Variables

  * variables de contexto

  * Gestión de contexto manual

  * Soporte asyncio

He aquí módulos de apoyo para algunos de los servicios mencionados:

* "_thread" --- Low-level threading API
