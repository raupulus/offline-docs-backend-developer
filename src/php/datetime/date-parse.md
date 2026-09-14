---
title: date_parse
description: Retorna un array asociativo con información detallada sobre una fecha/hora
  dada
source_url: https://www.php.net/manual/es/function.date-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: ee1ce6a0e
order: 11120
---

date_parse

Retorna un array asociativo con información detallada sobre una fecha/hora dada

## Descripción

```php
date_parse(string $datetime): array
```php

`date_parse` analiza la cadena `datetime` dada según las mismas reglas `strtotime` y `DateTimeImmutable::__construct`. En lugar de devolver un timestamp Unix (con `strtotime`) o un objeto `DateTimeImmutable` (con `DateTimeImmutable::__construct`), devuelve un array asociativo con la información que podría detectar en la cadena `datetime` dada.

Si no se puede encontrar información sobre un cierto grupo de elementos, estos elementos del array serán definidos como `false` o estarán ausentes. Si es necesario para construir un timestamp o un objeto `DateTimeImmutable` a partir de la misma cadena `datetime`, varios campos pueden ser definidos con un valor no-`false`. Ver los ejemplos a continuación para los casos en que esto ocurre.

## Parámetros

`datetime`  
Fecha/hora en un formato aceptado por `DateTimeImmutable::__construct`.

## Valores devueltos

Retorna un `array` que contiene información sobre la fecha/hora analizada.

El array retornado tiene claves para `year`, `month`, `day`, `hour`, `minute`, `second`, `fraction`, y `is_localtime`.

Si `is_localtime` está presente, entonces `zone_type` indica el tipo de zona horaria. Para el tipo `1` (desplazamiento UTC) los campos `zone` y `is_dst` son añadidos. Para el tipo `2` (abreviatura) los campos `tz_abbr` y `is_dst` son añadidos. Para el tipo `3` (identificador de zona horaria) los campos `tz_abbr` y `tz_id` son añadidos.

Si elementos de tiempo relativo están presentes en la cadena `datetime`, como `+3 days`, el array retornado incluye un array anidado con la clave `relative`. Este array contiene entonces las claves `year`, `month`, `day`, `hour`, `minute`, `second`, y si es necesario `weekday`, y `weekdays`, dependiendo de la cadena pasada.

El array incluye los campos `warning_count` y `warnings`. El primero indica el número de advertencias. Las claves del array `warnings` indican la posición en el parámetro `datetime` donde ocurrió la advertencia, con el valor de cadena describiendo la advertencia misma. Un ejemplo a continuación muestra tal advertencia.

El array incluye también los campos `error_count` y `errors`. El primero indica el número de errores. Las claves del array `errors` indican la posición en el parámetro `datetime` donde ocurrió el error, con el valor de cadena describiendo la advertencia misma. Un ejemplo a continuación muestra tal advertencia.

> [!WARNING]
> El número de elementos de array en los arrays `warnings` y `errors` puede ser inferior a `warning_count` o `error_count` si ocurrieron en la misma posición.

## Errores/Excepciones

En el caso de que la función retorne un error, el elemento `"errors"` contendrá los mensajes de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El elemento `zone` del array retornado ahora representa segundos en lugar de minutos, y su signo es invertido. Por ejemplo, `-120` ahora es `7200`. |

## Ejemplos

`date_parse` con una cadena `datetime` completa

```
<?php
var_dump(date_parse("2006-12-12 10:00:00.5"));

    
```php

El ejemplo anterior mostrará:

    array(12) {
      ["year"]=>
      int(2006)
      ["month"]=>
      int(12)
      ["day"]=>
      int(12)
      ["hour"]=>
      int(10)
      ["minute"]=>
      int(0)
      ["second"]=>
      int(0)
      ["fraction"]=>
      float(0.5)
      ["warning_count"]=>
      int(0)
      ["warnings"]=>
      array(0) {
      }
      ["error_count"]=>
      int(0)
      ["errors"]=>
      array(0) {
      }
      ["is_localtime"]=>
      bool(false)
    }

Los elementos de zona horaria solo aparecen si están incluidos en la cadena `datetime` dada. En este caso, siempre habrá un elemento `zone_type` y algunos otros dependiendo de su valor.

`date_parse` con información abreviada sobre la zona horaria

```
<?php
var_dump(date_parse("June 2nd, 2022, 10:28:17 BST"));

    
```php

El ejemplo anterior mostrará:

    array(16) {
      ["year"]=>
      int(2022)
      ["month"]=>
      int(6)
      ["day"]=>
      int(2)
      ["hour"]=>
      int(10)
      ["minute"]=>
      int(28)
      ["second"]=>
      int(17)
      ["fraction"]=>
      float(0)
      ["warning_count"]=>
      int(0)
      ["warnings"]=>
      array(0) {
      }
      ["error_count"]=>
      int(0)
      ["errors"]=>
      array(0) {
      }
      ["is_localtime"]=>
      bool(true)
      ["zone_type"]=>
      int(2)
      ["zone"]=>
      int(0)
      ["is_dst"]=>
      bool(true)
      ["tz_abbr"]=>
      string(3) "BST"
    }

`date_parse` con información abreviada sobre la zona horaria

```
<?php
var_dump(date_parse("June 2nd, 2022, 10:28:17 Europe/London"));

    
```php

El ejemplo anterior mostrará:

    array(14) {
      ["year"]=>
      int(2022)
      ["month"]=>
      int(6)
      ["day"]=>
      int(2)
      ["hour"]=>
      int(10)
      ["minute"]=>
      int(28)
      ["second"]=>
      int(17)
      ["fraction"]=>
      float(0)
      ["warning_count"]=>
      int(0)
      ["warnings"]=>
      array(0) {
      }
      ["error_count"]=>
      int(0)
      ["errors"]=>
      array(0) {
      }
      ["is_localtime"]=>
      bool(true)
      ["zone_type"]=>
      int(3)
      ["tz_id"]=>
      string(13) "Europe/London"
    }

Si se analiza una cadena `datetime` más mínima, hay menos información disponible. En este ejemplo, todas las partes temporales son retornadas como `false`.

`date_parse` con una cadena mínima

```
<?php
var_dump(date_parse("June 2nd, 2022"));

    
```php

El ejemplo anterior mostrará:

    array(12) {
      ["year"]=>
      int(2022)
      ["month"]=>
      int(6)
      ["day"]=>
      int(2)
      ["hour"]=>
      bool(false)
      ["minute"]=>
      bool(false)
      ["second"]=>
      bool(false)
      ["fraction"]=>
      bool(false)
      ["warning_count"]=>
      int(0)
      ["warnings"]=>
      array(0) {
      }
      ["error_count"]=>
      int(0)
      ["errors"]=>
      array(0) {
      }
      ["is_localtime"]=>
      bool(false)
    }

[Los formatos relativos](#datetime.formats.relative) no influyen en los valores analizados desde formatos absolutos, pero son analizados en el elemento "relativo".

Ejemplo con `date_parse` y formatos relativos

```
<?php
var_dump(date_parse("2006-12-12 10:00:00.5 +1 week +1 hour"));

    
```php

El ejemplo anterior mostrará:

    array(13) {
      ["year"]=>
      int(2006)
      ["month"]=>
      int(12)
      ["day"]=>
      int(12)
      ["hour"]=>
      int(10)
      ["minute"]=>
      int(0)
      ["second"]=>
      int(0)
      ["fraction"]=>
      float(0.5)
      ["warning_count"]=>
      int(0)
      ["warnings"]=>
      array(0) {
      }
      ["error_count"]=>
      int(0)
      ["errors"]=>
      array(0) {
      }
      ["is_localtime"]=>
      bool(false)
      ["relative"]=>
      array(6) {
        ["year"]=>
        int(0)
        ["month"]=>
        int(0)
        ["day"]=>
        int(7)
        ["hour"]=>
        int(1)
        ["minute"]=>
        int(0)
        ["second"]=>
        int(0)
      }
    }

Algunas estrofas, tales como `Thursday` (jueves) definirán la parte hora de la cadena como `0`. Si `Thursday` (jueves) se pasa a `DateTimeImmutable::__construct` la hora, el minuto, el segundo y la fracción también serán definidos como `0`. En el ejemplo a continuación, el elemento año sin embargo es dejado como `false`.

`date_parse` con efectos secundarios

```
<?php
var_dump(date_parse("Thursday, June 2nd"));

    
```php

El ejemplo anterior mostrará:

    array(13) {
      ["year"]=>
      bool(false)
      ["month"]=>
      int(6)
      ["day"]=>
      int(2)
      ["hour"]=>
      int(0)
      ["minute"]=>
      int(0)
      ["second"]=>
      int(0)
      ["fraction"]=>
      float(0)
      ["warning_count"]=>
      int(0)
      ["warnings"]=>
      array(0) {
      }
      ["error_count"]=>
      int(0)
      ["errors"]=>
      array(0) {
      }
      ["is_localtime"]=>
      bool(false)
      ["relative"]=>
      array(7) {
        ["year"]=>
        int(0)
        ["month"]=>
        int(0)
        ["day"]=>
        int(0)
        ["hour"]=>
        int(0)
        ["minute"]=>
        int(0)
        ["second"]=>
        int(0)
        ["weekday"]=>
        int(4)
      }
    }

## Véase también

`date_parse_from_format` para analizar el parámetro `datetime` con un formato específico, `checkdate` para una validación de fecha Gregoriana, `getdate`
