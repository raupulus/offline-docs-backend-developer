---
title: La clase EvIo
source_url: https://www.php.net/manual/es/class.evio.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evio.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 18150
---

## Introducción

Los observadores `EvIo` verifican si un descriptor de fichero (o un socket, o un flujo que pueda ser convertido en descriptor de fichero numérico) está disponible para lectura o escritura en cada iteración del bucle de eventos, o, más precisamente, cuando la lectura no va a bloquear el proceso, y cuando la escritura va a permitir escribir datos. Este comportamiento se denomina *nivel de activación* porque los eventos se mantienen mientras persista la condición. Para detener la recepción de eventos, simplemente se debe detener el observador.

El número de eventos de lectura/escritura de los observadores por `fd` es ilimitado. Establecer todos los descriptores de ficheros en modo no bloqueante es generalmente una buena idea (aunque no es obligatorio).

Otra cosa a tener en cuenta es que es muy fácil recibir notificaciones falsas de sistema listo para lectura, es decir, la función de retrollamada puede ser llamada con `Ev::READ` pero una subsiguiente *read()* puede bloquearse debido a que no hay datos. Es muy simple encontrarse en esta situación. Por lo tanto, se recomienda siempre utilizar I/O no bloqueante: una *read()* adicional que devuelva `EAGAIN` (o similar) es preferible a un programa que espera la llegada de datos.

Si por alguna razón no es posible ejecutar el `fd` en modo no bloqueante, entonces, por separado, se debe volver a verificar si el descriptor de fichero está realmente listo. Algunos usuarios utilizan además `SIGALRM` y un temporizador de intervalo, solo para asegurarse de que no haya bloqueos infinitos.

Se recomienda siempre utilizar el modo no bloqueante.

## Sinopsis de la clase

EvIo

EvIo

extends

EvWatcher

Propiedades

public

fd

public

events

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`fd`  

`events`
