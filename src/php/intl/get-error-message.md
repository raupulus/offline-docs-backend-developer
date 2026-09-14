---
title: Collator::getErrorMessage
description: Lee el último mensaje de error del collator
source_url: https://www.php.net/manual/es/collator.geterrormessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/get-error-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39420
---

Collator::getErrorMessage

collator_get_error_message

Lee el último mensaje de error del collator

## Descripción

Estilo orientado a objetos

```php
public Collator::getErrorMessage(): string
```php

Estilo procedimental

```php
collator_get_error_message(Collator $object): string
```

Lee el último mensaje de error.

## Parámetros

`object`  
Objeto `Collator`.

## Valores devueltos

La descripción de un error ocurrido durante la última llamada a un método de la API `Collator`, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `collator_get_error_message`

```php
<?php
$coll = collator_create( 'lt' );
if( collator_compare( $coll, 'y', 'k' ) === false ) {
    echo collator_get_error_message( $coll );
}
?>

    
```

## Véase también

`collator_get_error_code`
