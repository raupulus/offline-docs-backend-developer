---
title: pcntl_async_signals
description: Activa/desactiva la gestión asíncrona de las señales o devuelve el antiguo
  parámetro
source_url: https://www.php.net/manual/es/function.pcntl-async-signals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-async-signals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: b890f28c0
order: 61190
---

pcntl_async_signals

Activa/desactiva la gestión asíncrona de las señales o devuelve el antiguo parámetro

## Descripción

```php
pcntl_async_signals([bool $enable]): bool
```php

Si el argumento `enable` es `null`, `pcntl_async_signals` devuelve si la gestión asíncrona de las señales está activada. De lo contrario, la gestión asíncrona de las señales se activa o desactiva.

## Parámetros

`enable`  
Si la gestión asíncrona de las señales debe ser activada.

## Valores devueltos

Cuando se utiliza como getter (`enable` es `null`), devuelve si la gestión asíncrona de las señales está activada. Cuando se utiliza como setter (`enable` no es `null`), devuelve si la gestión asíncrona de las señales estaba activada *antes* de la llamada a la función.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `enable` es ahora nullable. |

## Véase también

declare
