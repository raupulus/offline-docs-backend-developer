---
title: jdtounix
description: Convierte un día Juliano en un timestamp UNIX
source_url: https://www.php.net/manual/es/function.jdtounix.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jdtounix.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 789af8343
order: 6670
---

jdtounix

Convierte un día Juliano en un timestamp UNIX

## Descripción

```php
jdtounix(int $julian_day): int
```php

Esta función devuelve un timestamp UNIX correspondiente al día Juliano dado en `julian_day`. El tiempo devuelto es UTC.

## Parámetros

`julian_day`  
El número de días Julianos, comprendido entre `2440588` y `106751993607888` en sistemas de 64 bits, o comprendido entre `2440588` y `2465443` en sistemas de 32 bits.

## Valores devueltos

El timestamp UNIX para el inicio (medianoche, no mediodía) del día Juliano dado.

## Errores/Excepciones

Si `julian_day` está fuera del intervalo permitido, se lanza una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ya no devuelve `false` en caso de error, sino que lanza una `ValueError` en su lugar. |
| 7.3.24, 7.4.12 | El límite superior del parámetro `julian_day` ha sido extendido. Antes, era de `2465342` según la arquitectura. |

## Véase también

`unixtojd`
