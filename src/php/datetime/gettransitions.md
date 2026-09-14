---
title: DateTimeZone::getTransitions
description: Devuelve todas las transiciones de una zona horaria
source_url: https://www.php.net/manual/es/datetimezone.gettransitions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimezone/gettransitions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 77fca2416
order: 10880
---

DateTimeZone::getTransitions

timezone_transitions_get

Devuelve todas las transiciones de una zona horaria

## Descripción

Estilo orientado a objetos

```php
public DateTimeZone::getTransitions([int $timestampBegin], [int $timestampEnd]): array
```php

Estilo procedimental

```php
timezone_transitions_get(DateTimeZone $object, [int $timestampBegin], [int $timestampEnd]): array
```

## Parámetros

`object`  
Solo en estilo procedimental: un objeto `DateTimeZone` retornado por `timezone_open`

`timestampBegin`  
Inicio del timestamp.

`timestampEnd`  
Fin del timestamp.

## Valores devueltos

Devuelve un array indexado numéricamente de arrays de transición en caso de éxito, o `false` si ocurre un error. Los objetos DateTimeZone que envuelven zonas horarias de tipo 1 (desplazamiento UTC) y tipo 2 (abreviaturas) no contienen transiciones y llamar a este método sobre ellos devolverá `false`.

Si `timestampBegin` es proporcionado, la primera entrada en el array devuelto contendrá un elemento de transición al tiempo de `timestampBegin`.

| Clave | Tipo | Descripción |
|----|----|----|
| `ts` | `int` | timestamp Unix |
| `time` | `string` | Cadena de tiempo `DateTimeInterface::ISO8601_EXPANDED` (PHP 8.2 y superior), o `DateTimeInterface::ISO8601` (PHP 8.1 e inferior) |
| `offset` | `int` | Desplazamiento horario hacia UTC en segundos |
| `isdst` | `bool` | Si la hora de verano está activada |
| `abbr` | `string` | Abreviatura de la zona horaria |

Estructura de los arrays de transición

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El valor predeterminado de `timestampEnd` se ha cambiado a 2147483647. Anteriormente, era `PHP_INT_MAX`. |

## Ejemplos

Ejemplo con `timezone_transitions_get`

```php
<?php
$timezone = new DateTimeZone("Europe/London");
$transitions = $timezone->getTransitions();
print_r(array_slice($transitions, 0, 3));
?>

    
```

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [ts] => -2147483648
                [time] => 1901-12-13T20:45:52+00:00
                [offset] => -75
                [isdst] =>
                [abbr] => LMT
            )

        [1] => Array
            (
                [ts] => 442304971
                [time] => 1847-12-01T00:01:15+00:00
                [offset] => 0
                [isdst] =>
                [abbr] => GMT
            )

        [2] => Array
            (
                [ts] => -1691964000
                [time] => 1916-05-21T02:00:00+00:00
                [offset] => 3600
                [isdst] => 1
                [abbr] => BST
            )

    )

Un ejemplo de `timezone_transitions_get` con `timestampBegin` definido

```php
<?php
$timezone = new DateTimeZone("Europe/London");
$transitions = $timezone->getTransitions(time());
print_r(array_slice($transitions, 0, 3));
?>

    
```

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [ts] => 1759058251
                [time] => 2025-09-28T11:17:31+00:00
                [offset] => 3600
                [isdst] => 1
                [abbr] => BST
            )

        [1] => Array
            (
                [ts] => 1761440400
                [time] => 2025-10-26T01:00:00+00:00
                [offset] => 0
                [isdst] =>
                [abbr] => GMT
            )

        [2] => Array
            (
                [ts] => 1774746000
                [time] => 2026-03-29T01:00:00+00:00
                [offset] => 3600
                [isdst] => 1
                [abbr] => BST
            )

    )
