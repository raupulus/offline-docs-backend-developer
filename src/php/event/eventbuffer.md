---
title: La clase EventBuffer
source_url: https://www.php.net/manual/es/class.eventbuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19370
---

## Introducción

La clase `EventBuffer` representa "evbuffer" de Libevent, una utilidad para las I/O bufferizadas.

Los buffers de eventos son generalmente útiles para realizar la parte buffer de una red I/O bufferizada.

## Sinopsis de la clase

EventBuffer

EventBuffer

Constantes

const

int

EventBuffer::EOL_ANY

0

const

int

EventBuffer::EOL_CRLF

1

const

int

EventBuffer::EOL_CRLF_STRICT

2

const

int

EventBuffer::EOL_LF

3

const

int

EventBuffer::PTR_SET

0

const

int

EventBuffer::PTR_ADD

1

Propiedades

public

readonly

int

length

public

readonly

int

contiguous_space

Métodos

## Propiedades

`length`  
El número de bytes almacenados en un buffer de eventos.

`contiguous_space`  
El número de bytes almacenados de manera contigua al inicio del buffer. Los bytes en un buffer pueden estar almacenados en varias partes separadas de la memoria; esta propiedad devuelve el número de bytes actualmente almacenados en la primera parte.

## Constantes predefinidas

`EventBuffer::EOL_ANY`  
El fin de línea es una secuencia de números que representan un retorno de carro y una nueva línea. Este formato no es muy útil; existe solo por razones de compatibilidad ascendente.

`EventBuffer::EOL_CRLF`  
El fin de línea es un retorno de carro opcional, seguido de una nueva línea. (En otras palabras, es `"\r\n"` o `"\n"`). Este formato es útil para analizar los protocolos de Internet basados en texto; el estándar requiere `"\r\n"` pero algunos clientes proporcionan solo `"\n"`.

`EventBuffer::EOL_CRLF_STRICT`  
El fin de línea es un simple retorno de carro, seguido de una simple nueva línea (también conocido como `"\r\n"`. Los valores ASCII son `0x0D` `0x0A`).

`EventBuffer::EOL_LF`  
El fin de línea es un simple carácter de nueva línea (también conocido como `"\n"`. El valor ASCII es `0x0A`).

`EventBuffer::PTR_SET`  
Flag utilizado como argumento del método EventBuffer::setPosition. Si este flag es especificado, la posición del puntero es movida a una posición absoluta del buffer.

`EventBuffer::PTR_ADD`  
Idéntico a `EventBuffer::PTR_SET`, excepto que este flag hace que el método EventBuffer::setPosition se mueva a una posición hacia atrás en relación con el número de bytes especificado (en lugar de definir una posición absoluta).
