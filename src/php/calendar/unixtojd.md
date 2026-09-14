---
title: unixtojd
description: Convierte un timestamp UNIX en un día Juliano
source_url: https://www.php.net/manual/es/function.unixtojd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/unixtojd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 789af8343
order: 6700
---

unixtojd

Convierte un timestamp UNIX en un día Juliano

## Descripción

```php
unixtojd([int $timestamp]): int
```php

Devuelve el día Juliano del timestamp UNIX `timestamp` (número de segundos desde el 1/1/1970), o para el día actual si `timestamp` es omitido. En cualquier caso, la hora es considerada como la hora local (no UTC).

## Parámetros

`timestamp`  
Un timestamp UNIX a convertir.

## Valores devueltos

Un número de días Julianos, en forma de `int`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `timestamp` ahora es nullable. |

## Véase también

`jdtounix`
