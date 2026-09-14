---
title: intl_get_error_code
description: Lee el último código de error
source_url: https://www.php.net/manual/es/function.intl-get-error-code.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/functions/intl-get-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: fed368268
order: 39790
---

intl_get_error_code

Lee el último código de error

## Descripción

```php
intl_get_error_code(): int
```php

Útil para gestionar los errores que ocurren en los métodos estáticos cuando no hay un objeto del cual obtener el mensaje de error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El código de error devuelto por la última llamada a la API.

## Ejemplos

Ejemplo con `intl_get_error_code`

```
<?php
$coll = collator_create( '<bad_param>' );
if( !$coll ) {
    handle_error( intl_get_error_code() );
}
?>

    
```php

## Véase también

`intl_is_failure`, `intl_error_name`, `intl_get_error_message`, `collator_get_error_code`, `numfmt_get_error_code`
