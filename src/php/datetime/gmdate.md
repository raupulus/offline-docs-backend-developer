---
title: gmdate
description: Formatea una fecha/hora GMT/TUC
source_url: https://www.php.net/manual/es/function.gmdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/gmdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11250
---

gmdate

Formatea una fecha/hora GMT/TUC

## Descripción

```php
gmdate(string $format, [int $timestamp]): string
```php

Idéntico a la función `date`, excepto que el tiempo devuelto es Greenwich Mean Time (GMT).

## Parámetros

`format`  
El formato de la fecha de salida en forma de `string`. Ver las opciones de formato para la función `date`.

`timestamp`  
El parámetro opcional `timestamp` es un `int` timestamp Unix que por defecto es la hora local actual si `timestamp` se omite o es `null`. En otras palabras, por defecto toma el valor de `time`.

## Valores devueltos

Devuelve una fecha formateada.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `timestamp` ahora es nullable. |

## Ejemplos

Ejemplo con `gmdate`

```
<?php
date_default_timezone_set("Europe/Helsinki");

echo date("M d Y H:i:s e", mktime(0, 0, 0, 1, 1, 1998)) . "\n";
echo gmdate("M d Y H:i:s e", mktime(0, 0, 0, 1, 1, 1998));

    
```php

El ejemplo anterior mostrará:

    Jan 01 1998 00:00:00 Europe/Helsinki
    Dec 31 1997 22:00:00 UTC

## Véase también

DateTimeImmutable::\_\_construct, DateTimeInterface::format, `date`, `mktime`, `gmmktime`, IntlDateFormatter::format
