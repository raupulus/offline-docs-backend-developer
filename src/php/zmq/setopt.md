---
title: ZMQContext::setOpt
description: Establecer una opción de socket
source_url: https://www.php.net/manual/es/zmqcontext.setopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqcontext/setopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109120
---

ZMQContext::setOpt

Establecer una opción de socket

## Descripción

```php
public ZMQContext::setOpt(int $key, mixed $value): ZMQContext
```php

Establece una opción de contexto de ZMQ. El tipo del valor `value` depende de `key`. Véanse los [Tipos de constantes de ZMQ](#zmq.constants) para más información.

## Parámetros

`key`  
Una de las constantes `ZMQ::CTXOPT_*`.

`value`  
El valor del parámetro.

## Valores devueltos

Devuelve el objeto actual. Lanza una ZMQContextException en caso de error.
