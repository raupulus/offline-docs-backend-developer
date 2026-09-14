---
title: La clase EventBase
source_url: https://www.php.net/manual/es/class.eventbase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19140
---

## Introducción

La clase `EventBase` representa la estructura base de un evento libevent. Contiene un conjunto de eventos y puede verificar cuáles son los eventos activos.

Cada evento base tiene un *método* o un *backend* utilizado para determinar cuáles son los eventos listos. Estos métodos son : `select`, `poll`, `epoll`, `kqueue`, `devpoll`, `evport` y `win32`.

Para configurar un evento base a utilizar, o evitar un backend específico, la clase `EventConfig` puede ser utilizada.

> [!WARNING]
> No *destruya* el objeto `EventBase` hasta que los recursos asociados a los objetos `Event` no sean liberados. De lo contrario, esto llevará a resultados totalmente indefinidos.

## Sinopsis de la clase

EventBase

final

EventBase

Constantes

const

int

EventBase::LOOP_ONCE

1

const

int

EventBase::LOOP_NONBLOCK

2

const

int

EventBase::NOLOCK

1

const

int

EventBase::STARTUP_IOCP

4

const

int

EventBase::NO_CACHE_TIME

8

const

int

EventBase::EPOLL_USE_CHANGELIST

16

Métodos

## Constantes predefinidas

`EventBase::LOOP_ONCE`  
Flag utilizado con el método EventBase::loop que significa: "bloqueo mientras libevent tiene un evento activo, luego, salida una vez que todos los eventos activos han ejecutado sus funciones de retrollamada".

`EventBase::LOOP_NONBLOCK`  
Flag utilizado con el método EventBase::loop que significa: "no bloquear: ver qué eventos están listos actualmente, ejecutar sus funciones de retrollamada con una prioridad alta, luego, salir".

`EventBase::NOLOCK`  
Flag de configuración. No bloquear la base del evento, incluso si un bloqueo había sido puesto en su lugar.

`EventBase::STARTUP_IOCP`  
Flag de configuración específico de Windows. Activa el repartidor IOCP al inicio.

`EventBase::NO_CACHE_TIME`  
Flag de configuración. En lugar de verificar el tiempo actual cada vez que el bucle de eventos está listo para ejecutar la función de retrollamada, el tiempo será verificado cada vez que el tiempo máximo de espera para la función de retrollamada sea alcanzado.

`EventBase::EPOLL_USE_CHANGELIST`  
Si se utiliza el backend `epoll`, este flag significa que es seguro utilizar el código interno de modificación de lista interna a Libevent para agrupar los añadidos y las supresiones con el fin de intentar minimizar el número de llamadas al sistema.

El hecho de definir este flag hace que el código sea más rápido, pero puede enfrentarse a un bug de Linux: no es seguro utilizar este flag en presencia de fds clonados por dup() o una de sus variantes. Esto produciría un comportamiento extraño y muy difícil de diagnosticar.

Este flag también puede ser activado definiendo la variable de entorno `EVENT_EPOLL_USE_CHANGELIST`.

Este flag no tiene ningún efecto si se utiliza con un backend diferente a `epoll`.
