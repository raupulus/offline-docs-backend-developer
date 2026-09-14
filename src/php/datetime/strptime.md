---
title: strptime
description: Analiza una fecha/hora generada con strftime
source_url: https://www.php.net/manual/es/function.strptime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/strptime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 11330
---

strptime

Analiza una fecha/hora generada con

strftime

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] strptime(string $timestamp, string $format): array
```php

`strptime` devuelve un array con la fecha `timestamp` analizada, o `false` si se produjo un error.

Los nombres del mes y del día de la semana y otras cadenas dependientes del lenguaje están subordinados a la configuración regional local establecida con `setlocale` (`LC_TIME`).

## Parámetros

`timestamp` (`string`)  
La cadena a analizar (p.ej. devuelta por `strftime`).

`format` (`string`)  
El formato usado en `timestamp` (p.ej. el mismo que el usado en `strftime`). Observe que algunas de las opciones de formato disponibles en `strftime` pueden no tener ningún efecto en `strptime`; el subconjunto exacto que está soportado variará según el sistema operativo y a la biblioteca de C que esté en uso.

Para más información sobre las opciones de formato, lea la página de `strftime`.

## Valores devueltos

Devuelve un array o `false` si ocurre un error.

| parámetros | Descripción |
|----|----|
| `"tm_sec"` | Segundos después del minuto (0-61) |
| `"tm_min"` | Minutos después de la hora (0-59) |
| `"tm_hour"` | Hora desde la medianoche (0-23) |
| `"tm_mday"` | Día del mes (1-31) |
| `"tm_mon"` | Meses desde Enero (0-11) |
| `"tm_year"` | Años desde 1900 |
| `"tm_wday"` | Días desde el Domingo (0-6) |
| `"tm_yday"` | Días desde el 1 de Enero (0-365) |
| `"unparsed"` | la parte de `timestamp` que no fue reconocida usando el formato `format` especificado |

Los siguientes parámetros son devueltos en el array

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Esta función ha sido marcada como obsoleta. Use `date_parse_from_format` en su lugar (para análisis independiente de la localización), o IntlDateFormatter::parse (para análisis dependiente de la localización) |

## Ejemplos

Ejemplo de `strptime`

```
<?php
$format = '%d/%m/%Y %H:%M:%S';
$strf = strftime($format);

echo "$strf\n";

print_r(strptime($strf, $format));

    
```php

Resultado del ejemplo anterior es similar a:

    03/10/2004 15:54:19

    Array
    (
        [tm_sec] => 19
        [tm_min] => 54
        [tm_hour] => 15
        [tm_mday] => 3
        [tm_mon] => 9
        [tm_year] => 104
        [tm_wday] => 0
        [tm_yday] => 276
        [unparsed] =>
    )

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.

> [!NOTE]
> Internamente, esta función llama a la función `strptime()` proporcionada por la biblioteca C del sistema. Esta función puede presentar diferencias notables de comportamiento en diferentes sistemas operativos. Se recomienda el uso de `date_parse_from_format`, a la cuál no le afectan estas cosas.

> [!NOTE]
> `"tm_sec"` incluye segundos intercalares (actualmente hasta 2 por año). Para más información acerca de los segundos intercalares, vea el [artículo de Wikipedia sobre segundos intercalares](http://en.wikipedia.org/wiki/Leap_second).

## Véase también

IntlDateFormatter::parse, DateTime::createFromFormat, `checkdate`, `strftime`, `date_parse_from_format`
