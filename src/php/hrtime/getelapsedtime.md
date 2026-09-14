---
title: HRTime\StopWatch::getElapsedTime
description: Obtiene el tiempo transcurrido para todos los intervalos
source_url: https://www.php.net/manual/es/hrtime-stopwatch.getelapsedtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hrtime/hrtime-stopwatch/getelapsedtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hrtime
translation_status: ready
translation_reviewed: true
translation_revision: 3e7e14916
order: 29500
---

HRTime\StopWatch::getElapsedTime

Obtiene el tiempo transcurrido para todos los intervalos

## Descripción

```php
public HRTime\StopWatch::getElapsedTime([int $unit]): float
```php

Obtiene el tiempo transcurrido para todos los intervalos anteriores cerrados.

## Parámetros

`unit`  
Unidad de tiempo representada por una constante HRTime\Unit. Por omisión vale HRTime\Unit::SECOND.

## Valores devueltos

Devuelve un `float` que indica el tiempo transcurrido.
