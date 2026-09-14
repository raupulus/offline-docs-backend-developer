---
title: intl_get_error_message
description: Lee la descripción del último error
source_url: https://www.php.net/manual/es/function.intl-get-error-message.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/functions/intl-get-error-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: fed368268
order: 39800
---

intl_get_error_message

Lee la descripción del último error

## Descripción

```php
intl_get_error_message(): string
```php

Lee el mensaje de error de la última función de internacionalización llamada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La descripción del error que ocurrió durante la última llamada a la API.

## Ejemplos

Ejemplo con `intl_get_error_message`

```
<?php
if( Collator::getAvailableLocales() === false ) {
    show_error( intl_get_error_message() );
}
?>

    
```php

## Véase también

`intl_error_name`, `intl_get_error_code`, `intl_is_failure`, `collator_get_error_message`, `numfmt_get_error_message`
