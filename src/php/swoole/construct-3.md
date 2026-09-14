---
title: Swoole\Channel::__construct
description: Construye un canal Swoole
source_url: https://www.php.net/manual/es/swoole-channel.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/channel/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 322606e4f
order: 90910
---

Swoole\Channel::\_\_construct

Construye un canal Swoole

## Descripción

```php
public Swoole\Channel::__construct(string $size)
```php

Un canal Swoole es una estructura de datos en memoria que funciona como Chan en Golang, implementada sobre la base de memoria compartida y cerrojos mutex. Puede ser utilizado como una cola de mensajes de alto rendimiento en memoria. Construye un canal swoole con un tamaño fijo. El tamaño mínimo de un canal swoole es de 64 Ko. Se lanzarán excepciones si no hay suficiente memoria.

## Parámetros

`size`  
El tamaño del canal Swoole.
