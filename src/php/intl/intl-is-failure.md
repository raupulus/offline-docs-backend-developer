---
title: intl_is_failure
description: Verifica si un código de error indica un fallo
source_url: https://www.php.net/manual/es/function.intl-is-failure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/functions/intl-is-failure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 16152718a
order: 39810
---

intl_is_failure

Verifica si un código de error indica un fallo

## Descripción

```php
intl_is_failure(int $errorCode): bool
```php

## Parámetros

`errorCode`  
un valor devuelto por una de las funciones `intl_get_error_code`, `collator_get_error_code`.

## Valores devueltos

`true` si el código indica un fallo, y `false` en caso de éxito o advertencia.

## Ejemplos

Ejemplo con `intl_is_failure`

```
<?php
function check( $err_code )
{
    var_export( intl_is_failure( $err_code ) );
    echo "\n";
}

check( U_ZERO_ERROR );
check( U_USING_FALLBACK_WARNING );
check( U_ILLEGAL_ARGUMENT_ERROR );
?>

    
```php

Resultado del ejemplo anterior es similar a:

    false
    false
    true

## Véase también

`intl_get_error_code`, `collator_get_error_code`, `Collator-getErrorCode`
