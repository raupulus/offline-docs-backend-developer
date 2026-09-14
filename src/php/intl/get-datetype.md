---
title: IntlDateFormatter::getDateType
description: Lee el tipo de fecha utilizado por IntlDateFormatter
source_url: https://www.php.net/manual/es/intldateformatter.getdatetype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/get-datetype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39580
---

IntlDateFormatter::getDateType

datefmt_get_datetype

Lee el tipo de fecha utilizado por IntlDateFormatter

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getDateType(): int
```php

Estilo procedimental

```php
datefmt_get_datetype(IntlDateFormatter $formatter): int
```

Devuelve el tipo de fecha utilizado por el formateador `IntlDateFormatter`.

## Parámetros

`formatter`  
El recurso del formateador `IntlDateFormatter`.

## Valores devueltos

El [tipo de fecha](#intl.intldateformatter-constants) actual del formateador, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `datefmt_get_datetype`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El tipo de fecha del formateador es : ' . datefmt_get_datetype($fmt);
echo 'La visualización con el primer tipo de fecha es ' . datefmt_format($fmt, 0);

$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::SHORT,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'Ahora, el tipo de fecha del formateador es : ' . datefmt_get_datetype($fmt);
echo 'La visualización con el segundo tipo de fecha es ' . datefmt_format($fmt, 0);

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
echo 'El tipo de fecha del formateador es : ' . $fmt->getDateType();
echo 'La visualización con el primer tipo de fecha es ' . $fmt->format(0);
$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::SHORT,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'Ahora, el tipo de fecha del formateador es : ' . $fmt->getDateType();
echo 'La visualización con el segundo tipo de fecha es ' . $fmt->format(0);

?>

   
```

El ejemplo anterior mostrará:

    El tipo de fecha del formateador es : 0
    La visualización con el primer tipo de fecha es Wednesday, December 31, 1969 4:00:00 PM PT
    Ahora, el tipo de fecha del formateador es : 2
    La visualización con el primer tipo de fecha es 12/31/69 4:00:00 PM PT

      

## Véase también

`datefmt_get_timetype`, `datefmt_create`
