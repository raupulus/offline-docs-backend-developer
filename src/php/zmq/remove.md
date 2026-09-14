---
title: ZMQPoll::remove
description: Eliminar un elemento del conjunto de sondeo
source_url: https://www.php.net/manual/es/zmqpoll.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqpoll/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 331fbfeac
order: 109310
---

ZMQPoll::remove

Eliminar un elemento del conjunto de sondeo

## Descripción

```php
public ZMQPoll::remove(mixed $item): bool
```php

Elimina un elemento del conjunto de sondeo. El parámetro `item` puede ser un objeto ZMQSocket, un recurso de flujo o el ID devuelto por el método `ZMQPoll::add`.

## Parámetros

`item`  
El objeto ZMQSocket, flujo de PHP o `string` con el ID del elemento.

## Valores devueltos

Devuelve true si el objeto se eliminó y false si el objeto con el ID dado no existe en el conjunto de sondeo.
