---
title: gmstrftime
description: Formatea una fecha/hora GMT/TUC según la configuración local
source_url: https://www.php.net/manual/es/function.gmstrftime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/gmstrftime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 6c27f7044
order: 11270
---

gmstrftime

Formatea una fecha/hora GMT/TUC según la configuración local

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Se recomienda evitar su uso.

Las alternativas a esta función incluyen:

gmdate

IntlDateFormatter::format

## Descripción

```php
#[\Deprecated] gmstrftime(string $format, [int $timestamp]): string
```php

Se comporta igual que `strftime` excepto que la hora devuelta es la hora del meridiano de Greenwich (GMT). Por ejemplo, cuando se ejecuta en la hora estándar del este (GMT -0500), la primera línea a continuación imprime "Dec 31 1998 20:00:00", mientras que la segunda imprime "Jan 01 1999 01:00:00".

> [!WARNING]
> Esta función depende de la información local del sistema operativo, que puede ser inconsistente o no estar disponible. Se recomienda utilizar el método IntlDateFormatter::format.

## Parámetros

`format`  
Ver la descripción de la función `strftime`.

`timestamp`  
El parámetro opcional `timestamp` es un `int` timestamp Unix que por defecto es la hora local actual si `timestamp` se omite o es `null`. En otras palabras, por defecto toma el valor de `time`.

## Valores devueltos

Devuelve un `string` formateado según el formato dado utilizando el argumento `timestamp` o la hora local actual si no se proporciona ningún timestamp. Los nombres de los meses, días de la semana y otras cadenas dependientes de una localización dada, respetan la localización actual definida por la función `setlocale`. En caso de error, se devuelve `false`.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `timestamp` ahora es nullable. |

## Ejemplos

Ejemplo con `gmstrftime`

```
<?php

setlocale(LC_TIME, 'es_ES.UTF-8');
date_default_timezone_set('EST');

echo strftime("%B %d %Y %H:%M:%S",   mktime(20, 0, 0, 12, 31, 98)) . "\n";
echo gmstrftime("%B %d %Y %H:%M:%S", mktime(20, 0, 0, 12, 31, 98));

   
```php

El ejemplo anterior mostrará:

    Deprecated: Function strftime() is deprecated since 8.1, use IntlDateFormatter::format() instead in script on line 6
    diciembre 31 1998 20:00:00

    Deprecated: Function gmstrftime() is deprecated since 8.1, use IntlDateFormatter::format() instead in script on line 7
    enero 01 1999 01:00:00

## Véase también

IntlDateFormatter::format, DateTimeInterface::format, `strftime`
