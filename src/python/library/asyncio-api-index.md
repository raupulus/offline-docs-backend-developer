---
title: Índice de API de alto nivel
source_url: https://docs.python.org/es/3
source_path: library/asyncio-api-index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1580
---

# Índice de API de alto nivel

Esta página lista todas las APIs async/await habilitadas de alto
nivel.

## Tareas

Utilidades para ejecutar programas asyncio, crear Tareas, y esperar en
múltiples cosas con tiempos de espera.

+----------------------------------------------------+----------------------------------------------------+
| "run()"                                            | Crea un loop de eventos, ejecuta una corrutina,    |
## |                                                    | cierra el loop.                                    |

| "Runner"                                           | Un administrador de contexto que simplifica        |
## |                                                    | múltiples llamadas a funciones asíncronas.         |

## | "Task"                                             | Objeto tarea.                                      |

| "TaskGroup"                                        | Un administrador de contexto que contiene un grupo |
|                                                    | de tareas. Proporciona una forma conveniente y     |
|                                                    | confiable de esperar a que finalicen todas las     |
## |                                                    | tareas del grupo.                                  |

## | "create_task()"                                    | Inicia una tarea asyncio, luego la retorna.        |

## | "current_task()"                                   | Retorna la tarea actual.                           |

| "all_tasks()"                                      | Retorna todas las tareas que aún no han terminado  |
## |                                                    | para un bucle de eventos.                          |

## | "await" "sleep()"                                  | Duerme por un número de segundos.                  |

## | "await" "gather()"                                 | Programa y espera por cosas concurrentemente.      |

## | "await" "wait_for()"                               | Ejecuta con un tiempo de espera.                   |

## | "await" "shield()"                                 | Protege de la cancelación.                         |

## | "await" "wait()"                                   | Monitorea la completitud.                          |

| "timeout()"                                        | Ejecuta con un tiempo de espera. Útil en los casos |
## |                                                    | en que "wait_for" no es adecuado.                  |

| "to_thread()"                                      | Ejecute de forma asincrónica una función en un     |
## |                                                    | subproceso del sistema operativo independiente.    |

| "run_coroutine_threadsafe()"                       | Programa una corrutina de desde otro hilo del      |
## |                                                    | sistema operativo.                                 |

## | "for in" "as_completed()"                          | Monitorea por completitud con un loop "for".       |

-[ Ejemplos ]-

* Usando asyncio.gather() para ejecutar cosas en paralelo.

* Usando asyncio.wait_for() para forzar un tiempo de expiración.

* Cancelación.

* Usando asyncio.sleep().

* Ver también la página principal de documentación de Tareas.

## Colas

Las colas deberían ser usadas para distribuir trabajo entre múltiples
Tareas asyncio, implementar pools de conexiones y patrones pub/sub.

# | "Queue"                                            | Una cola FIFO.                                     |

## | "PriorityQueue"                                    | Una cola de prioridad.                             |

## | "LifoQueue"                                        | Una cola LIFO.                                     |

-[ Ejemplos ]-

* Usando asyncio.Queue para distribuir carga de trabajo entre varias
  Tareas.

* Ver también la página de documentación de Colas.

## Subprocesos

Utilidades para generar subprocesos y ejecutar comandos de consola.

# | "await" "create_subprocess_exec()"                 | Crea un subproceso.                                |

## | "await" "create_subprocess_shell()"                | Ejecuta un comando de consola.                     |

-[ Ejemplos ]-

* Ejecutando un comando de consola.

* Ver también la documentación de las APIs de subprocesos.

## Flujos

APIs de alto nivel para trabajar con IO de red.

# | "await" "open_connection()"                        | Establece una conexión TCP.                        |

## | "await" "open_unix_connection()"                   | Establece una conexión de un socket Unix.          |

## | "await" "start_server()"                           | Lanza un servidor TCP.                             |

## | "await" "start_unix_server()"                      | Lanza un servidor de sockets Unix.                 |

| "StreamReader"                                     | Objeto de alto nivel async/await para recibir      |
## |                                                    | datos de red.                                      |

| "StreamWriter"                                     | Objeto de alto nivel async/await para enviar datos |
## |                                                    | de red.                                            |

-[ Ejemplos ]-

* Cliente TCP de ejemplo.

* Ver también la documentación de APIs de flujos.

## Sincronización

Primitivas de sincronización al estilo hilos que pueden ser usadas en
Tareas.

# | "Lock"                                             | Un bloqueo mutex.                                  |

## | "Event"                                            | Un objeto de evento.                               |

## | "Condition"                                        | Un objeto de condición.                            |

## | "Semaphore"                                        | Un semáforo.                                       |

## | "BoundedSemaphore"                                 | Un semáforo acotado.                               |

## | "Barrier"                                          | Un objeto barrera.                                 |

-[ Ejemplos ]-

* Usando asyncio.Event.

* Usando asyncio.Barrier.

* Ver también la documentación de las primitivas de sincronización de
  asyncio.

## Excepciones

+----------------------------------------------------+----------------------------------------------------+
| "asyncio.CancelledError"                           | Lanzada cuando una Tarea es cancelada. Ver también |
## |                                                    | "Task.cancel()".                                   |

| "asyncio.BrokenBarrierError"                       | Lanzada cuando se rompe una barrera. Véase también |
## |                                                    | "Barrier.wait()".                                  |

-[ Ejemplos ]-

* Gestionando CancelledError para ejecutar código en petición de
  cancelación.

* Ver también la lista completa de excepciones específicas de asyncio.
