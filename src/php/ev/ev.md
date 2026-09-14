---
title: La clase Ev
source_url: https://www.php.net/manual/es/class.ev.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 17930
---

## Introducción

La clase Ev es una clase estática que proporciona acceso al bucle por defecto así como a algunas operaciones comunes.

## Sinopsis de la clase

Ev

final

Ev

Constantes

const

int

Ev::FLAG_AUTO

0

const

int

Ev::FLAG_NOENV

16777216

const

int

Ev::FLAG_FORKCHECK

33554432

const

int

Ev::FLAG_NOINOTIFY

1048576

const

int

Ev::FLAG_SIGNALFD

2097152

const

int

Ev::FLAG_NOSIGMASK

4194304

const

int

Ev::RUN_NOWAIT

1

const

int

Ev::RUN_ONCE

2

const

int

Ev::BREAK_CANCEL

0

const

int

Ev::BREAK_ONE

1

const

int

Ev::BREAK_ALL

2

const

int

Ev::MINPRI

-2

const

int

Ev::MAXPRI

2

const

int

Ev::READ

1

const

int

Ev::WRITE

2

const

int

Ev::TIMER

256

const

int

Ev::PERIODIC

512

const

int

Ev::SIGNAL

1024

const

int

Ev::CHILD

2048

const

int

Ev::STAT

4096

const

int

Ev::IDLE

8192

const

int

Ev::PREPARE

16384

const

int

Ev::CHECK

32768

const

int

Ev::EMBED

65536

const

int

Ev::CUSTOM

16777216

const

int

Ev::ERROR

2147483648

const

int

Ev::BACKEND_SELECT

1

const

int

Ev::BACKEND_POLL

2

const

int

Ev::BACKEND_EPOLL

4

const

int

Ev::BACKEND_KQUEUE

8

const

int

Ev::BACKEND_DEVPOLL

16

const

int

Ev::BACKEND_PORT

32

const

int

Ev::BACKEND_ALL

63

const

int

Ev::BACKEND_MASK

65535

Métodos

## Constantes predefinidas

Flags pasados para crear un bucle:

`Ev::FLAG_AUTO`  
El valor por defecto de los flags.

`Ev::FLAG_NOENV`  
Si este flag se utiliza (o si el programa ejecuta setuid o setgid), `libev` no va a mirar la variable de entorno `LIBEV_FLAGS`. De lo contrario (comportamiento por defecto), `LIBEV_FLAGS` va a sobrescribir completamente el flag si se encuentra. Útil para pruebas de rendimiento y para la búsqueda de bugs.

`Ev::FLAG_FORKCHECK`  
Hace que libev verifique si existe un fork en cada iteración, en lugar de llamar manualmente al método EvLoop::fork. Este mecanismo funciona llamando a `getpid()` en cada iteración de la bucle, y así, va a ralentizar el bucle de eventos que poseen muchas iteraciones, pero habitualmente, este ralentizamiento no es notable. La configuración de este flag no puede ser sobrescrita o especificada en la variable de entorno `LIBEV_FLAGS`.

`Ev::FLAG_NOINOTIFY`  
Cuando este flag está especificado, `libev` no va a intentar utilizar la API `inotify` para estos watchers [ev_stat](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_stat_code_did_the_file_attri). Este flag puede ser útil para conservar los descriptores de ficheros inotify, sabiendo que de lo contrario, cada bucle utilizando los watchers `ev_stat` va a consumir un manejador `inotify`.

`Ev::FLAG_SIGNALFD`  
Cuando este flag está especificado, `libev` va a intentar utilizar la API `signalfd` para estos watchers [ev_signal](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_signal_code_signal_me_when_a) (y [ev_child](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_child_code_watch_out_for_pro)). Esta API entrega las señales de forma asíncrona, lo que la hace más rápida, y puede permitir la recuperación de datos de señales en espera. También puede simplificar la gestión de señales con hilos, sabiendo que las señales son propiedades bloqueadas en los hilos. `Signalfd` no será utilizado por defecto.

`Ev::FLAG_NOSIGMASK`  
Cuando este flag está especificado, `libev` no va a modificar la máscara de señal. Esto significa que se debe asegurar que las señales están desbloqueadas antes de recibirlas.

Este comportamiento es útil para la gestión personalizada de señales, o la gestión de señales únicamente en hilos específicos.

Flags a pasar a Ev::run, o a EvLoop::run

`Ev::RUN_NOWAIT`  
Significa que el bucle de eventos va a mirar si hay nuevos eventos presentes, va a gestionar estos nuevos eventos, y todos los eventos especiales, pero no va a esperar y bloquear el proceso en el caso de que no haya eventos, y va a retornar después de una iteración del bucle. A veces es útil poner en cola y gestionar los nuevos eventos durante cálculos largos, y esto, para mantener el programa activo.

`Ev::RUN_ONCE`  
Significa que el bucle de eventos va a mirar si hay nuevos eventos presentes (y esperar, si es necesario), y va a gestionarlos, ellos y los especiales. Va a bloquear el proceso hasta que al menos un evento llegue (que puede ser un evento interno de libev, también, no está garantizado que una función de callback registrada por el usuario sea llamada), y va a retornar después de una iteración del bucle.

Flags pasados a Ev::stop, o a EvLoop::stop

`Ev::BREAK_CANCEL`  
Cancela la operación de cancelación.

`Ev::BREAK_ONE`  
Retorna la llamada más profunda a Ev::run (o EvLoop::run).

`Ev::BREAK_ALL`  
Retorna la llamada más cercana a Ev::run (o EvLoop::run).

Prioridades de Watcher:

`Ev::MINPRI`  
Prioridad mínima permitida para un watcher.

`Ev::MAXPRI`  
Prioridad máxima permitida para un watcher.

Máscaras de bytes de eventos (recibidos):

`Ev::READ`  
El descriptor de fichero en el watcher `EvIo` se ha vuelto accesible en lectura.

`Ev::WRITE`  
El descriptor de fichero en el watcher `EvIo` se ha vuelto accesible en escritura.

`Ev::TIMER`  
El watcher `EvTimer` ha alcanzado su tiempo máximo de espera.

`Ev::PERIODIC`  
El watcher `EvPeriodic` ha alcanzado su tiempo máximo de espera.

`Ev::SIGNAL`  
Una señal especificada en EvSignal::\_\_construct ha sido recibida.

`Ev::CHILD`  
El `pid` especificado en EvChild::\_\_construct ha recibido una modificación de estado.

`Ev::STAT`  
La ruta especificada en el watcher `EvStat` ha modificado sus atributos.

`Ev::IDLE`  
El watcher `EvIdle` funciona cuando no tiene ninguna otra tarea que hacer con los otros watchers.

`Ev::PREPARE`  
Todos los watchers `EvPrepare` son llamados justo antes del inicio de Ev::run. Así, los watchers `EvPrepare` son los últimos watchers en ser llamados antes del reposo del bucle de eventos, o la puesta en cola de los nuevos eventos.

`Ev::CHECK`  
Todos los watchers `EvCheck` son puestos en cola justo después de que Ev::run haya recuperado los nuevos eventos, pero antes, todas las funciones de callback de todos los eventos recibidos son puestas en cola. Así, los watchers `EvCheck` serán llamados antes que cualquier otro watcher de misma prioridad o de prioridad más baja en una iteración del bucle de eventos.

`Ev::EMBED`  
El bucle de eventos embebido especificado en el watcher `EvEmbed` necesita toda la atención.

`Ev::CUSTOM`  
Aún no enviado (o utilizado) por `libev`, pero puede ser libremente utilizado por los usuarios `libev` para señalar los watchers (i.e. vía el método EvWatcher::feed).

`Ev::ERROR`  
Ha ocurrido un error desconocido, el watcher se ha detenido. Esto puede ocurrir porque el watcher no ha podido ser iniciado correctamente porque `libev` ha excedido la memoria asignada, un descriptor de fichero ha sido cerrado, u otro problema. `Libev` considera esto como bugs de la aplicación. Ver también [la anatomía de un watcher](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#ANATOMY_OF_A_WATCHER_CONTENT)

Flags de Backend:

`Ev::BACKEND_SELECT`  
`select(2) backend`

`Ev::BACKEND_POLL`  
`poll(2) backend`

`Ev::BACKEND_EPOLL`  
Backend `epoll(7)` específico de Linux para, a la vez, los kernels antes y después de 2.6.9.

`Ev::BACKEND_KQUEUE`  
Backend `kqueue` utilizado en la mayoría de los sistemas BSD. El watcher `EvEmbed` puede ser utilizado para embeber un bucle (con el backend kqueue) en otro. Actualmente, un bucle puede intentar crear un bucle de eventos con el backend `kqueue` y utilizarlo únicamente para los sockets.

`Ev::BACKEND_DEVPOLL`  
Backend Solaris 8. Actualmente no implementado.

`Ev::BACKEND_PORT`  
Mecanismo de puerto de eventos Solaris con buen rendimiento.

`Ev::BACKEND_ALL`  
Prueba todos los backends (incluyendo los corruptos). No se recomienda utilizarlo explícitamente. Los operadores de bits deberían ser aplicados aquí (i.e. `Ev::BACKEND_ALL` & ~ `Ev::BACKEND_KQUEUE`). Utilice el método Ev::recommendedBackends o no especifique ningún backend.

`Ev::BACKEND_MASK`  
No es un backend, sino una máscara para seleccionar todos los bits de un backend desde el valor de `flags` para representar en una máscara cualquier backend (i.e. al modificar la variable de entorno `LIBEV_FLAGS`).

> [!NOTE]
> Para el bucle por defecto, durante la fase de inicialización del módulo, `Ev` registra llamadas a [ev_loop_fork](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#FUNCTIONS_CONTROLLING_EVENT_LOOPS_CO) vía `pthread_atfork` (si está disponible).

> [!NOTE]
> Hay métodos que proporcionan acceso a la *bucle de eventos por defecto* en la clase `Ev` (i.e. Ev::iteration, Ev::depth, etc.) Para los *bucles personalizados* (creados con EvLoop::\_\_construct), estos valores pueden ser accesibles vía las propiedades y los métodos correspondientes de la clase `EvLoop`.
>
> La instancia del bucle de eventos por defecto puede ser recuperada vía el método EvLoop::defaultLoop.
