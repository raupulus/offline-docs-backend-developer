---
title: idate
description: Formatea una parte de la hora/fecha local como un entero
source_url: https://www.php.net/manual/es/function.idate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/idate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11280
---

idate

Formatea una parte de la hora/fecha local como un entero

## Descripción

```php
idate(string $format, [int $timestamp]): int
```php

Devuelve un número formateado según el formato `format` dado con el timestamp entero dado `timestamp` o la hora actual si no se da un timestamp. En otras palabras, `timestamp` es opcional y el valor por omisión es el valor devuelto por `time`.

A diferencia de la función `date`, `idate` acepta solo un carácter como parámetro `format`.

## Parámetros

`format`  
| Caracteres de `format` | Descripción |
|----|----|
| `B` | Tiempo Internet Swatch Beat |
| `d` | El día del mes |
| `h` | Hora (formato 12 horas) |
| `H` | Hora (formato 24 horas) |
| `i` | Minutos |
| `I`(i, en mayúscula) | Devuelve `1` si el horario de verano está activado, `0` en caso contrario |
| `L`(l, en mayúscula) | Devuelve `1` para un año bisiesto, `0` en caso contrario |
| `m` | Número del mes |
| `N` | Día de la semana ISO-8601 (`1` para el lunes a `7` para el domingo) |
| `o` | Año ISO-8601 (4 dígitos) |
| `s` | Segundos |
| `t` | Día del mes actual |
| `U` | Segundos desde la época Unix - 1 de Enero de 1970 00:00:00 UTC - esto es lo mismo que la función `time` |
| `w` | Día de la semana (`0` para Domingo) |
| `W` | El número de semana del año; según ISO-8601, las semanas comienzan el Lunes |
| `y` | Año en 1 o 2 dígitos, ver la nota más abajo |
| `Y` | Año en 4 dígitos |
| `z` | Día del año |
| `Z` | Desplazamiento horario, en segundos |

Los siguientes caracteres son reconocidos en el string del parámetro `format`

`timestamp`  
El parámetro opcional `timestamp` es un `int` timestamp Unix que por defecto es la hora local actual si `timestamp` se omite o es `null`. En otras palabras, por defecto toma el valor de `time`.

## Valores devueltos

Devuelve un `int` en caso de éxito, o `false` si ocurre un error.

Dado que `idate` siempre devuelve un `int` y no puede comenzar con `0`, `idate` puede devolver menos dígitos de los que se podrían esperar. Ver el ejemplo a continuación.

## Errores/Excepciones

Cada llamada a una función de fecha/hora generará un diagnóstico de tipo `E_WARNING` si la zona horaria no es válida. Ver también `date_default_timezone_set`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Añade los caracteres de formato `N` (día de la semana ISO-8601) y `o` (año ISO-8601). |
| 8.0.0 | `timestamp` ahora es nullable. |

## Ejemplos

Ejemplo con `idate`

```
<?php
$timestamp = strtotime('1st January 2004'); // 1072915200

// esto muestra el año en dos dígitos
// sin embargo, dado que este dígito comenzará con "0",
// solo "4" será mostrado
echo idate('y', $timestamp) . "\n";

$timestamp = strtotime('1st January 2024'); // 1704067200
echo idate('y', $timestamp);

    
```php

El ejemplo anterior mostrará:

    4
    24

## Véase también

DateTimeInterface::format, `date`, `getdate`, `time`
