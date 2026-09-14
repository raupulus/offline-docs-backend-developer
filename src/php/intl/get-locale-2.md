---
title: IntlDateFormatter::getLocale
description: Lee la configuración local utilizada por el formateador
source_url: https://www.php.net/manual/es/intldateformatter.getlocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/get-locale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39610
---

IntlDateFormatter::getLocale

datefmt_get_locale

Lee la configuración local utilizada por el formateador

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getLocale([int $type]): string
```php

Estilo procedimental

```php
datefmt_get_locale(IntlDateFormatter $formatter, [int $type]): string
```

Lee la configuración local utilizada por el formateador.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

`type`  
Puede elegirse entre un valor válido o un valor literal de la configuración local (mediante las constantes `Locale::VALID_LOCALE` y `Locale::ACTUAL_LOCALE`, respectivamente). El valor por omisión es el valor literal.

## Valores devueltos

La configuración local de este formateador, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `datefmt_get_locale`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'La configuración local del formateador es : ' . datefmt_get_locale($fmt);
echo 'El primer formato utilizado es ' . datefmt_format($fmt, 0);

$fmt = datefmt_create(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'La configuración local del formateador es : ' . datefmt_get_locale($fmt);
echo 'El segundo formato utilizado es ' . datefmt_format($fmt, 0);

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
echo 'La configuración local del formateador es : ' . $fmt->getLocale();
echo 'El primer formato utilizado es ' . $fmt->format(0);

$fmt = new IntlDateFormatter(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'La configuración local del formateador es : ' . $fmt->getLocale();
echo 'El segundo formato utilizado es ' . $fmt->format(0);

?>

   
```

El ejemplo anterior mostrará:

    La configuración local del formateador es : en
    El primer formato utilizado es Wednesday, December 31, 1969 4:00:00 PM PT
    La configuración local del formateador es : de
    El segundo formato utilizado es Mittwoch, 31. Dezember 1969 16:00 Uhr GMT-08:00

      

## Véase también

`datefmt_create`
