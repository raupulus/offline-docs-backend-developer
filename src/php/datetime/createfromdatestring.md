---
title: DateInterval::createFromDateString
description: Establece un objeto DateInterval desde las partes relativas de una cadena
source_url: https://www.php.net/manual/es/dateinterval.createfromdatestring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateinterval/createfromdatestring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 10230
---

DateInterval::createFromDateString

Establece un objeto DateInterval desde las partes relativas de una cadena

## Descripción

Estilo orientado a objetos

```php
public static DateInterval::createFromDateString(string $datetime): DateInterval
```php

Estilo procedimental

```php
date_interval_create_from_date_string(string $datetime): DateInterval
```

Usas los analizadores de fecha/hora como los usados en el constructor de `DateTimeImmutable` para crear un `DateInterval` desde las partes relativas de la cadena analizada.

## Parámetros

`datetime`  
Una fecha con partes relativas. Específicamente, los [formatos relativos](#datetime.formats.relative) admitidos por el analizador utilizados por `DateTimeImmutable`, `DateTime`, y `strtotime` serán los empleados para construir el objeto DateInterval

Para usar un string con formato ISO-8601 como `P7D`, debes usar DateInterval::\_\_construct.

## Valores devueltos

Devuelve `DateInterval` en caso de éxito. Estilo procedimental retorna `false` en caso de error.

## Errores/Excepciones

Solo en la API Orientada a Objetos: Si se pasa una cadena de fecha/hora inválida, se lanza DateMalformedIntervalStringException.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora tiene un tipo de retorno tentativo de `DateInterval`. Anteriormente era `DateIntervalfalse`. |
| 8.3.0 | DateInterval::createFromDateString ahora lanza DateMalformedIntervalStringException si se pasa una cadena inválida. Anteriormente, devolvía `false`, y emitía una advertencia. `date_interval_create_from_date_string` no ha cambiado. |
| 8.2.0 | Las propiedades `from_string` y `date_string` solo serán visibles cuando se crea un `DateInterval` con este método. |

## Ejemplos

Analizando intervalos de fechas válidos

```php
<?php
// Cada conjunto de intervalos es equivalente.
$i = new DateInterval('P1D');
$i = DateInterval::createFromDateString('1 day');

$i = new DateInterval('P2W');
$i = DateInterval::createFromDateString('2 weeks');

$i = new DateInterval('P3M');
$i = DateInterval::createFromDateString('3 months');

$i = new DateInterval('P4Y');
$i = DateInterval::createFromDateString('4 years');

$i = new DateInterval('P1Y1D');
$i = DateInterval::createFromDateString('1 year + 1 day');

$i = new DateInterval('P1DT12H');
$i = DateInterval::createFromDateString('1 day + 12 hours');

$i = new DateInterval('PT3600S');
$i = DateInterval::createFromDateString('3600 seconds');

    
```

Analizando combinaciones e intervalos negativos

```php
<?php
$i = DateInterval::createFromDateString('62 weeks + 1 day + 2 weeks + 2 hours + 70 minutes');
echo $i->format('%d %h %i'), "\n";

$i = DateInterval::createFromDateString('1 year - 10 days');
echo $i->format('%y %d'), "\n";

    
```

El ejemplo anterior mostrará:

    449 2 70
    1 -10

Analizando intervalos de fechas relativas especiales

```php
<?php
$i = DateInterval::createFromDateString('last day of next month');
var_dump($i);

$i = DateInterval::createFromDateString('last weekday');
var_dump($i);

    
```

Resultado del ejemplo anterior en PHP 8.2:

```php
object(DateInterval)#1 (2) {
  ["from_string"]=>
  bool(true)
  ["date_string"]=>
  string(22) "last day of next month"
}
object(DateInterval)#2 (2) {
  ["from_string"]=>
  bool(true)
  ["date_string"]=>
  string(12) "last weekday"
}

    
```

Resultado del ejemplo anterior en PHP 8 es similar a:

```php
object(DateInterval)#1 (16) {
  ["y"]=>
  int(0)
  ["m"]=>
  int(1)
  ["d"]=>
  int(0)
  ["h"]=>
  int(0)
  ["i"]=>
  int(0)
  ["s"]=>
  int(0)
  ["f"]=>
  float(0)
  ["weekday"]=>
  int(0)
  ["weekday_behavior"]=>
  int(0)
  ["first_last_day_of"]=>
  int(2)
  ["invert"]=>
  int(0)
  ["days"]=>
  bool(false)
  ["special_type"]=>
  int(0)
  ["special_amount"]=>
  int(0)
  ["have_weekday_relative"]=>
  int(0)
  ["have_special_relative"]=>
  int(0)
}
object(DateInterval)#2 (16) {
  ["y"]=>
  int(0)
  ["m"]=>
  int(0)
  ["d"]=>
  int(0)
  ["h"]=>
  int(0)
  ["i"]=>
  int(0)
  ["s"]=>
  int(0)
  ["f"]=>
  float(0)
  ["weekday"]=>
  int(0)
  ["weekday_behavior"]=>
  int(0)
  ["first_last_day_of"]=>
  int(0)
  ["invert"]=>
  int(0)
  ["days"]=>
  bool(false)
  ["special_type"]=>
  int(1)
  ["special_amount"]=>
  int(-1)
  ["have_weekday_relative"]=>
  int(0)
  ["have_special_relative"]=>
  int(1)
}

    
```
