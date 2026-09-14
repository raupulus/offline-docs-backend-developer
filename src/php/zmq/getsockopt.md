---
title: ZMQSocket::getSockOpt
description: Obtener la opción de un socket
source_url: https://www.php.net/manual/es/zmqsocket.getsockopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/getsockopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109410
---

ZMQSocket::getSockOpt

Obtener la opción de un socket

## Descripción

```php
public ZMQSocket::getSockOpt(string $key): mixed
```php

Devuelve el valor de la opción de un socket.

## Parámetros

`key`  
Un número entero que representa la opción. Véanse las constantes `ZMQ::SOCKOPT_*`.

## Valores devueltos

Devuelve un `string` o un `int` dependiendo de `key`. Lanza una ZMQSocketException en caso de error.
