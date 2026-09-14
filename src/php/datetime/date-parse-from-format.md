---
title: date_parse_from_format
description: Recupera las informaciones de una fecha dada siguiendo un formato específico
source_url: https://www.php.net/manual/es/function.date-parse-from-format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-parse-from-format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11110
---

date_parse_from_format

Recupera las informaciones de una fecha dada siguiendo un formato específico

## Descripción

```php
date_parse_from_format(string $format, string $datetime): array
```php

Devuelve un array asociativo que contiene informaciones detalladas sobre una fecha/hora dada.

## Parámetros

`format`  
Documentación sobre el uso del `format`, por favor referirse a la documentación de `DateTimeImmutable::createFromFormat`. Las mismas reglas se aplican.

`datetime`  
Cadena que representa la fecha/hora.

## Valores devueltos

Devuelve un array asociativo con informaciones detalladas sobre la fecha/hora dada.

El array devuelto tiene claves para `year`, `month`, `day`, `hour`, `minute`, `second`, `fraction`, y `is_localtime`.

Si `is_localtime` está presente, entonces `zone_type` indica el tipo de zona horaria. Para el tipo `1` (desplazamiento UTC) se añaden los campos `zone` y `is_dst`. Para el tipo `2` (abreviatura) se añaden los campos `tz_abbr` y `is_dst`. Para el tipo `3` (identificador de zona horaria) se añaden los campos `tz_abbr` y `tz_id`.

El array incluye los campos `warning_count` y `warnings`. El primero indica el número de advertencias. Las claves del array `warnings` indican la posición en el parámetro `datetime` donde ocurrió la advertencia, con el valor de cadena que describe la advertencia misma. Un ejemplo a continuación muestra tal advertencia.

El array incluye también los campos `error_count` y `errors`. El primero indica el número de errores. Las claves del array `errors` indican la posición en el parámetro `datetime` donde ocurrió el error, con el valor de cadena que describe la advertencia misma. Un ejemplo a continuación muestra tal advertencia.

> [!WARNING]
> El número de elementos de array en los arrays `warnings` y `errors` puede ser inferior a `warning_count` o `error_count` si ocurrieron en la misma posición.

## Errores/Excepciones

Esta función lanza una ValueError cuando el `datetime` contiene bytes NULL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.21, 8.1.8, 8.2.0 | Ahora lanza una ValueError cuando se pasan bytes NULL en `datetime`, lo cual antes era ignorado silenciosamente. |
| 7.2.0 | El elemento `zone` del array devuelto representa segundos en lugar de minutos ahora, y su signo es invertido. Por ejemplo `-120` ahora es igual a `7200`. |

## Ejemplos

Ejemplo con `date_parse_from_format`

```
<?php
$date = "6.1.2009 13:00+01:00";
print_r(date_parse_from_format("j.n.Y H:iP", $date));

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [year] => 2009
        [month] => 1
        [day] => 6
        [hour] => 13
        [minute] => 0
        [second] => 0
        [fraction] => 0
        [warning_count] => 0
        [warnings] => Array
            (
            )

        [error_count] => 0
        [errors] => Array
            (
            )

        [is_localtime] => 1
        [zone_type] => 1
        [zone] => 3600
        [is_dst] =>
    )

Ejemplo de `date_parse_from_format` con advertencias

```
<?php
$date = "26 August 2022 22:30 pm";
$parsed = date_parse_from_format("j F Y G:i a", $date);

echo "Número de advertencias: ", $parsed['warning_count'], "\n";
foreach ($parsed['warnings'] as $position => $message) {
    echo "\tEn la posición {$position}: {$message}\n";
}

    
```php

El ejemplo anterior mostrará:

    Número de advertencias: 1
        En la posición 23: The parsed time was invalid

Ejemplo de `date_parse_from_format` con errores

```
<?php
$date = "26 August 2022 CEST";
$parsed = date_parse_from_format("j F Y H:i", $date);

echo "Número de errores: ", $parsed['error_count'], "\n";
foreach ($parsed['errors'] as $position => $message) {
    echo "\tEn la posición {$position}: {$message}\n";
}

    
```php

El ejemplo anterior mostrará:

    Número de errores: 3
        En la posición 15: A two digit hour could not be found
        En la posición 19: Not enough data available to satisfy format

## Véase también

`DateTimeImmutable::createFromFormat`, `checkdate`
