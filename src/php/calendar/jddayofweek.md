---
title: jddayofweek
description: Devuelve el número del día de la semana
source_url: https://www.php.net/manual/es/function.jddayofweek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jddayofweek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 789af8343
order: 6610
---

jddayofweek

Devuelve el número del día de la semana

## Descripción

```php
jddayofweek(int $julian_day, [int $mode]): int
```php

Devuelve el número del día de la semana. Puede devolver una cadena o un entero, dependiendo del modo.

## Parámetros

`julian_day`  
El número del día juliano, en forma de `int`.

`mode`  
| Modo | Significado |
|----|----|
| 0 (por omisión) | Devuelve el número del día como un entero (0=domingo, 1=lunes, etc.) |
| 1 | Devuelve una cadena que contiene el nombre del día (inglés gregoriano) |
| 2 | Devuelve una cadena que contiene el nombre abreviado del día de la semana (inglés gregoriano) |

Modos para la semana del calendario

## Valores devueltos

El día de la semana gregoriano, en forma de `int` o de `string`.
