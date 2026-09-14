---
title: ZMQPoll::add
description: Añadir un elemento al conjunto de sondeo
source_url: https://www.php.net/manual/es/zmqpoll.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqpoll/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 109260
---

ZMQPoll::add

Añadir un elemento al conjunto de sondeo

## Descripción

```php
public ZMQPoll::add(mixed $entry, int $type): string
```php

Añade un nuevo elemento al conjunto de sondeo y devuelve el ID interno de dicho elemento. El elemento puede ser eliminado del conjunto de sondeo utilizando el ID devuelto.

## Parámetros

`entry`  
Un objeto ZMQSocket o un recursode de flujo de PHP

`type`  
Defina la actidad para la que es sondeado el socket Véanse las constantes `ZMQ::POLL_IN` y `ZMQ::POLL_OUT`.

## Valores devueltos

Devuelve el ID del elemento añadido, el cual puede ser empleado más adelante para eliminar el elemento. Lanza una ZMQPollException en caso de error.
