---
title: EvLoop::__construct
description: Construye un objeto de bucle de eventos
source_url: https://www.php.net/manual/es/evloop.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18190
---

EvLoop::\_\_construct

Construye un objeto de bucle de eventos

## Descripción

```php
public EvLoop::__construct([int $flags], [mixed $data], [float $io_interval], [float $timeout_interval])
```php

Construye el objeto de bucle de eventos.

## Parámetros

`flags`  
Uno de los [flags de bucle de eventos](#ev.constants.loop-flags)

`data`  
Datos personalizados para asociar con el bucle.

`io_interval`  
Ver la función [io_interval](#evloop.props.io-interval)

`timeout_interval`  
Ver la función [timeout_interval](#evloop.props.timeout-interval)

## Véase también

EvLoop::defaultLoop
