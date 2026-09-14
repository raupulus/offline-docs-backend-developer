---
title: getdate
description: Devuelve la fecha/hora
source_url: https://www.php.net/manual/es/function.getdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/getdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11230
---

getdate

Devuelve la fecha/hora

## Descripción

```php
getdate([int $timestamp]): array
```php

Devuelve un `array` asociativo que contiene las informaciones de fecha y hora del `timestamp`, o la fecha/hora actual local si `timestamp` es omitido o `null`.

## Parámetros

`timestamp`  
El parámetro opcional `timestamp` es un `int` timestamp Unix que por defecto es la hora local actual si `timestamp` se omite o es `null`. En otras palabras, por defecto toma el valor de `time`.

## Valores devueltos

Devuelve un `array` asociativo que contiene las informaciones de fecha y hora del timestamp `timestamp`. Los elementos del array asociativo devuelto son los siguientes:

| Clave | Descripción | Ejemplo de valor devuelto |
|----|----|----|
| `"seconds"` | Representación numérica de los segundos | `0` a `59` |
| `"minutes"` | Representación numérica de los minutos | `0` a `59` |
| `"hours"` | Representación numérica de las horas | `0` a `23` |
| `"mday"` | Representación numérica del día del mes actual | `1` a `31` |
| `"wday"` | Representación numérica del día de la semana actual | `0` (para Domingo) a `6` (para Sábado) |
| `"mon"` | Representación numérica del mes | `1` a `12` |
| `"year"` | Año, con 4 dígitos | Ejemplos: `1999` o `2003` |
| `"yday"` | Representación numérica del día del año | `0` a `365` |
| `"weekday"` | Versión en texto del día de la semana | `Sunday` a `Saturday` |
| `"month"` | Versión en texto del mes, como `January` o `March` | `January` a `December` |
| `0` | Número de segundos desde la época Unix, similar al valor devuelto por la función `time` y utilizado por `date`. | Depende del sistema, típicamente de `-2147483648` a `2147483647`. |

Nombres de las claves del array asociativo devuelto

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `timestamp` ahora es nullable. |

## Ejemplos

Ejemplo con `getdate`

```
<?php
$today = getdate();
print_r($today);

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [seconds] => 40
        [minutes] => 58
        [hours] => 21
        [mday] => 17
        [wday] => 2
        [mon] => 6
        [year] => 2003
        [yday] => 167
        [weekday] => Tuesday
        [month] => June
        [0] => 1055901520
    )

## Véase también

`date`, `idate`, `localtime`, `time`, `setlocale`
