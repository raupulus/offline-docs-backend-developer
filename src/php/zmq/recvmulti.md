---
title: ZMQSocket::recvMulti
description: Recibir un mensaje multiparte
source_url: https://www.php.net/manual/es/zmqsocket.recvmulti.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/recvmulti.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109440
---

ZMQSocket::recvMulti

Recibir un mensaje multiparte

## Descripción

```php
public ZMQSocket::recvMulti([int $mode]): array
```php

Recibe un array con el mensaje multiparte de un socket. Por defecto, la recepción quedará en espera hasta que haya disponible un mensaje, a menos que se emplee el flag `ZMQ::MODE_*`.

## Parámetros

`mode`  
Proporcionar banderas de modo para recibir mensajes multiparte o hacer que la operación no quede en espera. Véanse las constantes `ZMQ::MODE_*`.

## Valores devueltos

Devuelve el array con las partes del mensaje. Lanza una ZMQSocketException en caso de error. Si se emplea `ZMQ::MODE_NOBLOCK` y la operación debería quedar en espera, se devolverá el `bool` false.
