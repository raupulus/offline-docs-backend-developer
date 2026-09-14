---
title: LuaSandbox::getCPUUsage
description: Recupera el uso actual del tiempo de CPU del entorno Lua
source_url: https://www.php.net/manual/es/luasandbox.getcpuusage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/getcpuusage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43940
---

LuaSandbox::getCPUUsage

Recupera el uso actual del tiempo de CPU del entorno Lua

## Descripción

```php
public LuaSandbox::getCPUUsage(): float
```php

Recupera el uso actual del tiempo de CPU del entorno Lua.

Esto incluye el tiempo pasado en las funciones de retrollamada PHP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el uso actual del tiempo de CPU en segundos.

> [!NOTE]
> En Windows, esta función siempre devuelve cero. En los sistemas operativos que no soportan `CLOCK_THREAD_CPUTIME_ID`, como FreeBSD y Mac OS X, esta función devolverá el tiempo transcurrido en el reloj, no el tiempo de CPU.

## Véase también

LuaSandbox::getMemoryUsage

LuaSandbox::getPeakMemoryUsage

LuaSandbox::setCPULimit
