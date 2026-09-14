---
title: ZMQSocket::getSocketType
description: Obtener el tipo de socket
source_url: https://www.php.net/manual/es/zmqsocket.getsockettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/getsockettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109400
---

ZMQSocket::getSocketType

Obtener el tipo de socket

## Descripción

```php
public ZMQSocket::getSocketType(): int
```php

Obtiene el tipo de socket.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un número entero que representa el tipo de socket. El número entero puede ser comparado con las constantes `ZMQ::SOCKET_*`
