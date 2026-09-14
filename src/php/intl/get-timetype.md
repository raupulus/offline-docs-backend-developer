---
title: IntlDateFormatter::getTimeType
description: Lee el tipo de tiempo para IntlDateFormatter
source_url: https://www.php.net/manual/es/intldateformatter.gettimetype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/get-timetype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39630
---

IntlDateFormatter::getTimeType

datefmt_get_timetype

Lee el tipo de tiempo para IntlDateFormatter

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getTimeType(): int
```php

Estilo procedimental

```php
datefmt_get_timetype(IntlDateFormatter $formatter): int
```

Devuelve el tipo de tiempo utilizado por el formateador.

## Parámetros

`formatter`  
El recurso del formateador `IntlDateFormatter`.

## Valores devueltos

El valor actual de [tipo de fecha](#intl.intldateformatter-constants) utilizado por el formateador, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `datefmt_get_timetype`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El tipo de tiempo del formateador es : ' . datefmt_get_timetype($fmt);
echo 'El primer resultado con timetype es ' . datefmt_format($fmt, 0);

$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::SHORT,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'Ahora, el timetype del formateador es : ' . datefmt_get_timetype($fmt);
echo 'El segundo resultado con timetype es ' . datefmt_format($fmt, 0);

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
echo 'El tipo de tiempo del formateador es : ' . $fmt->getTimeType();
echo 'El primer resultado con timetype es ' . $fmt->format(0);

$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::SHORT,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'Ahora, el timetype del formateador es : ' . $fmt->getTimeType();
echo 'El segundo resultado con timetype es ' . $fmt->format(0);

?>

   
```

El ejemplo anterior mostrará:

    El tipo de tiempo del formateador es : 0
    El primer resultado con timetype es Wednesday, December 31, 1969 4:00:00 PM PT
    Ahora, el timetype del formateador es : 3
    El segundo resultado con timetype es Wednesday, December 31, 1969 4:00 PM

      

## Véase también

`datefmt_get_datetype`, `datefmt_create`
