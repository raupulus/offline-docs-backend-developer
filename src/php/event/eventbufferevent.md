---
title: La clase EventBufferEvent
source_url: https://www.php.net/manual/es/class.eventbufferevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19670
---

## Introducción

Representa un buffer de eventos Libevent.

Normalmente, una aplicación desea poner en buffer datos además de simplemente responder a eventos. Cuando se desea escribir datos, por ejemplo, el mecanismo habitual se asemeja a:

1.  Se decide que se desea escribir datos en una conexión; coloque estos datos en un buffer.

2.  Se espera a que la conexión se vuelva accesible en escritura.

3.  Se escribe la mayor cantidad de datos posible.

4.  Se recuerda la cantidad escrita, y si aún hay más datos para escribir, se espera a que la conexión vuelva a ser accesible en escritura.

Este mecanismo de bufferización de E/S es lo suficientemente común como para que Libevent proporcione un mecanismo genérico para ello. Un buffer de eventos consta de un transporte subyacente (como un socket), un buffer de lectura y un buffer de escritura. En lugar de un evento clásico, que proporciona funciones de retrollamada cuando el transporte subyacente está listo para ser leído o escrito, un buffer de eventos llama a sus funciones de retrollamada proporcionadas por el usuario cuando ha leído o escrito suficientes datos.

## Sinopsis de la clase

EventBufferEvent

final

EventBufferEvent

Constantes

const

int

EventBufferEvent::READING

1

const

int

EventBufferEvent::WRITING

2

const

int

EventBufferEvent::EOF

16

const

int

EventBufferEvent::ERROR

32

const

int

EventBufferEvent::TIMEOUT

64

const

int

EventBufferEvent::CONNECTED

128

const

int

EventBufferEvent::OPT_CLOSE_ON_FREE

1

const

int

EventBufferEvent::OPT_THREADSAFE

2

const

int

EventBufferEvent::OPT_DEFER_CALLBACKS

4

const

int

EventBufferEvent::OPT_UNLOCK_CALLBACKS

8

const

int

EventBufferEvent::SSL_OPEN

0

const

int

EventBufferEvent::SSL_CONNECTING

1

const

int

EventBufferEvent::SSL_ACCEPTING

2

Propiedades

public

int

fd

public

int

priority

public

readonly

EventBuffer

input

public

readonly

EventBuffer

output

Métodos

## Propiedades

`fd`  
Descriptor de fichero numérico asociado con el buffer de eventos. Normalmente, representa un socket enlazado. Vale `null` si no hay ningún descriptor de fichero (socket) asociado con el buffer de eventos.

`priority`  
La prioridad del evento, utilizada para implementar el buffer de eventos.

`input`  
Objeto de buffer de entrada subyacente (`EventBuffer`)

`output`  
Objeto de buffer de salida subyacente (`EventBuffer`)

## Constantes predefinidas

`EventBufferEvent::READING`  
Un evento ocurre durante la operación de lectura en el bufferevent. Ver otros flags para conocer el tipo de evento.

`EventBufferEvent::WRITING`  
Un evento ocurre durante una operación de escritura en el bufferevent. Ver otros flags para conocer el tipo de evento.

`EventBufferEvent::EOF`  
Se recibe una indicación de fin de fichero en el buffer de eventos.

`EventBufferEvent::ERROR`  
Un error ocurre durante una operación bufferevent. Para más información sobre el error, llame al método EventUtil::getLastSocketErrno y/o EventUtil::getLastSocketError.

`EventBufferEvent::TIMEOUT`  

`EventBufferEvent::CONNECTED`  
Termina una conexión solicitada en el bufferevent.

`EventBufferEvent::OPT_CLOSE_ON_FREE`  
Cuando el buffer de eventos es liberado, cierra el transporte subyacente. Esto cerrará el socket subyacente, liberará el buffer de eventos subyacente, etc.

`EventBufferEvent::OPT_THREADSAFE`  
Asigna automáticamente bloqueos para el bufferevent, para hacer segura la utilización de múltiples threads.

`EventBufferEvent::OPT_DEFER_CALLBACKS`  
Cuando este flag está definido, el bufferevent pospone todas sus funciones de retrollamada. Ver [la documentación sobre la programación de red rápida, portable, no bloqueante con Libevent, el posponer de las funciones de retrollamada](http://www.wangafu.net/~nickm/libevent-book/Ref6_bufferevent.html#_deferred_callbacks).

`EventBufferEvent::OPT_UNLOCK_CALLBACKS`  
Por omisión, cuando el bufferevent está definido para ser seguro al nivel de los threads, el bloqueo del buffer de eventos es mantenido, incluso si una función de retrollamada de usuario es llamada. La definición de esta opción permite a Libevent liberar el bloqueo del buffer de eventos cuando la función de retrollamada es llamada.

`EventBufferEvent::SSL_OPEN`  
La negociación SSL se realiza.

`EventBufferEvent::SSL_CONNECTING`  
SSL realiza actualmente la negociación como cliente.

`EventBufferEvent::SSL_ACCEPTING`  
SSL realiza actualmente la negociación como servidor.
