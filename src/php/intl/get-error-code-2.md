---
title: IntlDateFormatter::getErrorCode
description: Lee el código de error de la última operación
source_url: https://www.php.net/manual/es/intldateformatter.geterrorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/get-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: a4e79bc8e
order: 39590
---

IntlDateFormatter::getErrorCode

datefmt_get_error_code

Lee el código de error de la última operación

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getErrorCode(): int
```php

Estilo procedimental

```php
datefmt_get_error_code(IntlDateFormatter $formatter): int
```

Devuelve el código de error de la última operación de formato.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

## Valores devueltos

El código de error, uno de los valores UErrorCode. El valor inicial es U_ZERO_ERROR.

## Ejemplos

Ejemplo con `datefmt_get_error_code`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
$str = datefmt_format($fmt);

printf(
    "Error : %s (%d)\n",
    datefmt_get_error_message($fmt),
    datefmt_get_error_code($fmt)
);
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
$str = $fmt->format(0);

printf(
    "Error : %s (%d)\n",
    $fmt->getErrorMessage(),
    $fmt->getErrorCode()
);
?>

   
```

El ejemplo anterior mostrará:

    Error : U_ZERO_ERROR (0)

      

## Véase también

`datefmt_get_error_message`, `intl_get_error_code`, `intl_is_failure`
