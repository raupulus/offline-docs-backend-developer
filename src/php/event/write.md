---
title: EventBuffer::write
description: Escribe el contenido del buffer en un fichero o en un socket
source_url: https://www.php.net/manual/es/eventbuffer.write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 19360
---

EventBuffer::write

Escribe el contenido del buffer en un fichero o en un socket

## Descripción

```php
public EventBuffer::write(mixed $fd, [int $howmuch]): int
```php

Escribe el contenido del buffer en un descriptor de fichero. El buffer será vaciado después de la escritura exitosa de los últimos octetos.

## Parámetros

`fd`  
Recurso de socket, flujo, o un descriptor numérico de fichero asociado con un socket.

`howmuch`  
El número máximo de octetos a escribir.

## Valores devueltos

Devuelve el número de octetos escritos, o `false` en caso de error.

## Véase también

EventBuffer::read
