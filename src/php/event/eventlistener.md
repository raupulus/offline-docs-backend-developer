---
title: La clase EventListener
source_url: https://www.php.net/manual/es/class.eventlistener.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventlistener.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 20400
---

## Introducción

Representa una escucha de conexión.

## Sinopsis de la clase

EventListener

final

EventListener

Constantes

const

int

EventListener::OPT_LEAVE_SOCKETS_BLOCKING

1

const

int

EventListener::OPT_CLOSE_ON_FREE

2

const

int

EventListener::OPT_CLOSE_ON_EXEC

4

const

int

EventListener::OPT_REUSEABLE

8

const

int

EventListener::OPT_THREADSAFE

16

Propiedades

public

readonly

int

fd

Métodos

## Propiedades

`fd`  
Descriptor de fichero numérico del socket subyacente (Añadido en `event-1.6.0`).

## Constantes predefinidas

`EventListener::OPT_LEAVE_SOCKETS_BLOCKING`  
Por omisión, Libevent pone en modo no bloqueante los descriptores de ficheros o sockets subyacentes. Este flag indica a Libevent que los deje en modo bloqueante.

`EventListener::OPT_CLOSE_ON_FREE`  
Si esta opción está definida, la escucha de la conexión cierra su socket subyacente cuando el objeto `EventListener` es liberado.

`EventListener::OPT_CLOSE_ON_EXEC`  
Si esta opción está definida, la escucha de la conexión define el flag de cierre a la ejecución en el socket de escucha subyacente. Ver la documentación de la plataforma para más información sobre `fcntl` y `FD_CLOEXEC`.

`EventListener::OPT_REUSEABLE`  
Por omisión en algunas plataformas, una vez que un socket de escucha es cerrado, ningún otro socket puede ser ligado al mismo puerto hasta que cierto tiempo no haya pasado. El hecho de definir esta opción hace que Libevent marque este socket como reutilizable, así, una vez cerrado, otro socket puede ser abierto para escuchar el mismo puerto.

`EventListener::OPT_THREADSAFE`  
Bloqueo de la asignación para el escuchador; así, es seguro utilizarlo desde múltiples threads.
