---
title: localtime
description: Obtiene la hora local
source_url: https://www.php.net/manual/es/function.localtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/localtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11290
---

localtime

Obtiene la hora local

## Descripción

```php
localtime([int $timestamp], [bool $associative]): array
```php

`localtime` devuelve un array idéntico a la estructura devuelta por la función C localtime.

## Parámetros

`timestamp`  
El parámetro opcional `timestamp` es un `int` timestamp Unix que por defecto es la hora local actual si `timestamp` se omite o es `null`. En otras palabras, por defecto toma el valor de `time`.

`associative`  
Determina si la función debe devolver un array regular, indexado numéricamente, o un array asociativo.

## Valores devueltos

Si `associative` está definido como `false` o no se proporciona, entonces el array se devuelve como un array indexado numéricamente estándar. Si `associative` está definido como `true` entonces `localtime` devuelve un array asociativo que contiene los elementos de la estructura devuelta por la llamada a la función localtime de C Las claves del array asociativo son las siguientes:

- "tm_sec" : segundos, de `0` a `59`

- "tm_min" : minutos, de `0` a `59`

- "tm_hour" : hora, de `0` a `23`

- "tm_mday" : día del mes, de `1` a `31`

- "tm_mon" : mes del año, de `0` (Ene) a `11` (Dic)

- "tm_year" : Año desde 1900

- "tm_wday" : Día de la semana, de `0` (Dom) a `6` (Sáb)

- "tm_yday" : Día del año, de `0` a `365`

- "tm_isdst" : ¿Está en vigor el horario de verano?

  Valor positivo si es así, `0` en caso contrario, valor negativo si el resultado no ha podido determinarse.

## Errores/Excepciones

Cada llamada a una función de fecha/hora generará un diagnóstico de tipo `E_WARNING` si la zona horaria no es válida. Ver también `date_default_timezone_set`

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `timestamp` ahora es nullable. |

## Ejemplos

Ejemplo con `localtime`

```
<?php
$localtime = localtime();
$localtime_assoc = localtime(time(), true);
print_r($localtime);
print_r($localtime_assoc);

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 24
        [1] => 3
        [2] => 19
        [3] => 3
        [4] => 3
        [5] => 105
        [6] => 0
        [7] => 92
        [8] => 1
    )

    Array
    (
        [tm_sec] => 24
        [tm_min] => 3
        [tm_hour] => 19
        [tm_mday] => 3
        [tm_mon] => 3
        [tm_year] => 105
        [tm_wday] => 0
        [tm_yday] => 92
        [tm_isdst] => 1
    )

## Véase también

`getdate`
