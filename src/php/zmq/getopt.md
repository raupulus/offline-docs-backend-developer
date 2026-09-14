---
title: ZMQContext::getOpt
description: Obtener la opción de contexto
source_url: https://www.php.net/manual/es/zmqcontext.getopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqcontext/getopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 109090
---

ZMQContext::getOpt

Obtener la opción de contexto

## Descripción

```php
public ZMQContext::getOpt(string $key): mixed
```php

Devuelve el valor de una opción de contexto.

## Parámetros

`key`  
Un entero que representa la opción. Véanse las constantes `ZMQ::CTXOPT_*`.

## Valores devueltos

Devuelve un `string` o un `int`, dependiendo de `key`. Lanza una ZMQContextException en caso de error.
