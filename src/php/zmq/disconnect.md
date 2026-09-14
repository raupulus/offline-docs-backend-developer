---
title: ZMQSocket::disconnect
description: Desconectar un socket
source_url: https://www.php.net/manual/es/zmqsocket.disconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/disconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 6b766fe97
order: 109370
---

ZMQSocket::disconnect

Desconectar un socket

## Descripción

```php
public ZMQSocket::disconnect(string $dsn): ZMQSocket
```php

Desconectar el socket de un extremo remoto conectado previamente. El extremo está definido con el formato `transporte://dirección`, donde transporte es uno de los siguientes: inproc, ipc, tcp, pgm o epgm.

## Parámetros

`dsn`  
El DSN de conexión, por ejemplo `transporte://dirección`.

## Valores devueltos

Devuelve el objeto actual. Lanza una ZMQSocketException en caso de error.
