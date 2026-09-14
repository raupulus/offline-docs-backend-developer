---
title: IntlDateFormatter::localtime
description: Analiza una cadena y la convierte en tiempo
source_url: https://www.php.net/manual/es/intldateformatter.localtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/localtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 8ddf539e5
order: 39680
---

IntlDateFormatter::localtime

datefmt_localtime

Analiza una cadena y la convierte en tiempo

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::localtime(string $string, [int $offset]): array
```php

Estilo procedimental

```php
datefmt_localtime(IntlDateFormatter $formatter, string $string, [int $offset]): array
```

Convierte la cadena \$value en una fecha descompuesta (un `array` de campos), comenzando en la posición \$parse_pos y consumiendo tantos caracteres como sea posible.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

`string`  
La cadena a convertir.

`offset`  
La posición desde la cual comenzar el análisis en el valor \$value. Las posiciones comienzan en 0. Si no ocurre ningún error durante el análisis de \$value, \$parse_pos contendrá -1, y de lo contrario, contendrá la posición en la cual terminó el análisis (y ocurrió el error). Esta variable contendrá la posición de fin si el análisis falla. Si \$parse_pos \> strlen(\$value), el análisis falla inmediatamente.

## Valores devueltos

Un array de enteros compatible con localtime: contiene la hora en formato de 24 horas en el campo tm_hour, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `datefmt_localtime`

```php
<?php

$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
$arr = datefmt_localtime($fmt, 'Wednesday, December 31, 1969 at 4:00:00 PM Pacific Standard Time', $offset);
echo 'Resultado del análisis ';
if ($arr) {
    foreach ($arr as $key => $value) {
        echo "$key : $value , ";
    }
}

?>

   
```

Ejemplo orientado a objetos

```php
<?php
$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
$arr = $fmt->localtime('Wednesday, December 31, 1969 at 4:00:00 PM Pacific Standard Time', $offset);
echo 'Resultado del análisis ';
if ($arr) {
    foreach ($arr as $key => $value) {
        echo "$key : $value , ";
    }
}

?>

   
```

El ejemplo anterior mostrará:

    Resultado del análisis tm_sec : 0 , tm_min : 0 , tm_hour : 16 , tm_year : 69 ,
    tm_mday : 31 , tm_wday : 3 , tm_yday : 365 , tm_mon : 11 , tm_isdst : 0 ,

      

## Véase también

`datefmt_create`, `datefmt_format`, `datefmt_parse`, `datefmt_get_error_code`, `datefmt_get_error_message`
