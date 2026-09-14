---
title: ZMQSocket::bind
description: Vincular el socket
source_url: https://www.php.net/manual/es/zmqsocket.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqsocket/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: b8758b060
order: 109340
---

ZMQSocket::bind

Vincular el socket

## Descripción

```php
public ZMQSocket::bind(string $dsn, [bool $force]): ZMQSocket
```php

Vincula el socket a un extremo. El extremo está definido en formato `transporte://dirección` donde transporte es uno de los siguientes: inproc, ipc, tcp, pgm o epgm.

## Parámetros

`dsn`  
El DSN del vículo, por ejemplo `transporte://dirección`.

`force`  
Intenta el vínculo incluso si elm socket ya ha sido vinculado al extremo dado.

## Valores devueltos

Devuelve el objeto actual. Lanza una ZMQSocketException en caso de error.
