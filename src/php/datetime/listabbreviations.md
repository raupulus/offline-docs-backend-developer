---
title: DateTimeZone::listAbbreviations
description: Devuelve un array asociativo que describe una zona horaria
source_url: https://www.php.net/manual/es/datetimezone.listabbreviations.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimezone/listabbreviations.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10890
---

DateTimeZone::listAbbreviations

timezone_abbreviations_list

Devuelve un array asociativo que describe una zona horaria

## Descripción

Estilo orientado a objetos

```php
public static DateTimeZone::listAbbreviations(): array
```php

Estilo procedimental

```php
timezone_abbreviations_list(): array
```

La lista de abreviaturas devuelta contiene todos los usos históricos de las abreviaturas, lo que puede dar lugar a entradas correctas, pero confusas. Asimismo, existen conflictos, ya que `PST` se utiliza tanto en Estados Unidos como en Filipinas.

La lista que devuelve esta función no es adecuada para construir un menú de opciones que presente una selección de zonas horarias a los usuarios.

> [!NOTE]
> Los datos para esta función están precompilados por razones de rendimiento y no se actualizan al utilizar una [timezonedb](https://pecl.php.net/package/timezonedb) más reciente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el `array` de abreviaturas de zonas horarias.

## Ejemplos

Ejemplo con `timezone_abbreviations_list`

```php
<?php
$timezone_abbreviations = DateTimeZone::listAbbreviations();
print_r($timezone_abbreviations["acst"]);

    
```

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [dst] =>
                [offset] => 34200
                [timezone_id] => Australia/Adelaide
            )

        [1] => Array
            (
                [dst] =>
                [offset] => 34200
                [timezone_id] => Australia/Broken_Hill
            )

        [2] => Array
            (
                [dst] =>
                [offset] => 34200
                [timezone_id] => Australia/Darwin
            )

        [3] => Array
            (
                [dst] =>
                [offset] => 34200
                [timezone_id] => Australia/North
            )

        [4] => Array
            (
                [dst] =>
                [offset] => 34200
                [timezone_id] => Australia/South
            )

        [5] => Array
            (
                [dst] =>
                [offset] => 34200
                [timezone_id] => Australia/Yancowinna
            )

    )

## Véase también

`timezone_identifiers_list`
