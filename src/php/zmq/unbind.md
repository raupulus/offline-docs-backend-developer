---
title: ZMQSocket::unbind
description: Desvincular el socket
source_url: https://www.php.net/manual/es/zmqsocket.unbind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/unbind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: ab5614596
order: 109480
---

ZMQSocket::unbind

Desvincular el socket

## Descripción

```php
public ZMQSocket::unbind(string $dsn): ZMQSocket
```php

Desvincula el socket de un extremo. El extremo está definido con el formato `transporte://dirección`, donde transporte es uno de los siguientes: inproc, ipc, tcp, pgm o epgm.

## Parámetros

`dsn`  
El DSN vinculado previamente, por ejemplo `transporte://dirección`.

## Valores devueltos

Devuelve el objeto actual. Lanaza una ZMQSocketException en caso de error.
