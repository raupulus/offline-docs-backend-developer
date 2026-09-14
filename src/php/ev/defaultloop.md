---
title: EvLoop::defaultLoop
description: Devuelve o crea el bucle de eventos por omisión
source_url: https://www.php.net/manual/es/evloop.defaultloop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/defaultloop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18200
---

EvLoop::defaultLoop

Devuelve o crea el bucle de eventos por omisión

## Descripción

```php
public static EvLoop::defaultLoop([int $flags], [mixed $data], [float $io_interval], [float $timeout_interval]): EvLoop
```php

Si el bucle de eventos por omisión no está creado, el método EvLoop::defaultLoop lo crea con los parámetros especificados. De lo contrario, devolverá la instancia del objeto correspondiente previamente creado ignorando todos los parámetros.

## Parámetros

`flags`  
Uno de los [flags de bucle de eventos](#ev.constants.loop-flags)

`data`  
Datos personalizados para asociar con el bucle.

`io_collect_interval`  
Ver la función [io_interval](#evloop.props.io-interval)

`timeout_collect_interval`  
Ver la función [timeout_interval](#evloop.props.timeout-interval)

## Valores devueltos

Devuelve el objeto EvLoop en caso de éxito.

## Véase también

EvLoop::\_\_construct
