---
title: ZMQSocket::setSockOpt
description: Establecer una opción de socket
source_url: https://www.php.net/manual/es/zmqsocket.setsockopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/setsockopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109470
---

ZMQSocket::setSockOpt

Establecer una opción de socket

## Descripción

```php
public ZMQSocket::setSockOpt(int $key, mixed $value): ZMQSocket
```php

Establece una opción de socket de ZMQ. El tipo del valor `value` depende de la clave `key`. Véanse los [Tipos de constantes de ZMQ](#zmq.constants) para más información.

## Parámetros

`key`  
Una de las constantes `ZMQ::SOCKOPT_*`.

`value`  
El valor del parámetro.

## Valores devueltos

Devuelve el objeto actual. Lanaza una ZMQSocketException en caso de error.
