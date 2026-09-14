---
title: Swoole\Atomic::__construct
description: Construye un nuevo objeto atómico Swoole.
source_url: https://www.php.net/manual/es/swoole-atomic.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/atomic/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 90770
---

Swoole\Atomic::\_\_construct

Construye un nuevo objeto atómico Swoole.

## Descripción

```php
public Swoole\Atomic::__construct([int $value])
```php

Un objeto atómico Swoole es una variable entera que permite a cualquier procesador probar y modificar de manera atómica. Se implementa sobre la base de las instrucciones atómicas del procesador. Las variables atómicas Swoole deben definirse antes de que se llame a swoole_server-\>start.

Compare-and-swap (CAS) es una instrucción atómica utilizada en el multithreading para realizar la sincronización. Compara el contenido de una ubicación de memoria con un valor dado y, solo si son idénticos, modifica el contenido de esa ubicación de memoria a un nuevo valor dado.

## Parámetros

`value`  
El valor del objeto atómico.
