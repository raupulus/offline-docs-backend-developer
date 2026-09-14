---
title: ZMQSocket::sendmulti
description: Enviar un mensaje multiparte
source_url: https://www.php.net/manual/es/zmqsocket.sendmulti.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/sendmulti.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109460
---

ZMQSocket::sendmulti

Enviar un mensaje multiparte

## Descripción

```php
public ZMQSocket::sendmulti(array $message, [int $mode]): ZMQSocket
```php

Envía un mensaje multiparte mediante el socket. La operación puede quedar en espera, a menos que se emplee `ZMQ::MODE_NOBLOCK`.

## Parámetros

`message`  
El mensaje a enviar - un array de cadenas

`mode`  
Proporcional flags de modo para recibir mensajes multiparte o hacer que la operación no quede en espera. Véanse las constantes `ZMQ::MODE_*`.

## Valores devueltos

Devuelve el objeto actual. Lanza una ZMQSocketException en caso de error. Si se emplea `ZMQ::MODE_NOBLOCK` y la operación debería quedar en espera, se devolverá el `bool` false.
