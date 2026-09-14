---
title: IntlDateFormatter::parseToCalendar
description: Analiza una cadena hacia un timestamp, actualizando un calendario abierto
source_url: https://www.php.net/manual/es/intldateformatter.parsetocalendar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/parsetocalendar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: 20687bf9c
order: 39700
---

IntlDateFormatter::parseToCalendar

Analiza una cadena hacia un timestamp, actualizando un calendario abierto

## Descripción

```php
public IntlDateFormatter::parseToCalendar(string $string, [int $offset]): int
```php

Convierte `string` en un valor de tiempo incremental, comenzando en `offset` y leyendo tantos caracteres del valor de entrada como sea posible.

Este método se comporta como IntlDateFormatter::parse, salvo que la zona horaria del formateador se actualiza según la información de zona horaria contenida en la cadena `string` analizada.

## Parámetros

`string`  
La cadena a convertir en un tiempo.

`offset`  
Posición en la que comenzar el análisis en `string` (basada en cero). Si no ocurre ningún error antes de que `string` sea consumida, `offset` contendrá -1; de lo contrario contendrá la posición en la que el análisis terminó (y se produjo el error). Esta variable contendrá la posición final si el análisis falla. Si `offset` \> `strlen($string)`, el análisis falla inmediatamente.

## Valores devueltos

El timestamp del valor analizado, o `false` si el valor no se puede analizar.

## Ejemplos

Ejemplo de IntlDateFormatter::parseToCalendar

```
<?php
$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo $fmt->parseToCalendar('Wednesday, December 20, 1989 at 4:00:00 PM Pacific Standard Time');
?>

   
```php

El ejemplo anterior mostrará:

    630201600

## Véase también

IntlDateFormatter::parse

IntlDateFormatter::format

IntlDateFormatter::getErrorCode

IntlDateFormatter::getErrorMessage
