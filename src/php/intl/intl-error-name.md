---
title: intl_error_name
description: Lee el nombre simbólico de un código de error dado
source_url: https://www.php.net/manual/es/function.intl-error-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/functions/intl-error-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 16152718a
order: 39780
---

intl_error_name

Lee el nombre simbólico de un código de error dado

## Descripción

```php
intl_error_name(int $errorCode): string
```php

Devuelve el nombre del código de error ICU.

## Parámetros

`errorCode`  
El código de error ICU.

## Valores devueltos

La cadena devuelta será la del nombre de la constante equivalente.

## Ejemplos

Ejemplo con `intl_error_name`

```
<?php
$coll     = collator_create( 'en_RU' );
$err_code = collator_get_error_code( $coll );

printf( "El nombre simbólico de %d es %s\n.", $err_code, intl_error_name( $err_code ) );
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Symbolic name for -128 is U_USING_FALLBACK_WARNING.

## Véase también

`intl_is_failure`, `intl_get_error_code`, `intl_get_error_message`
