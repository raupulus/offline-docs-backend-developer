---
title: Collator::getErrorCode
description: Lee el último error del collator
source_url: https://www.php.net/manual/es/collator.geterrorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/get-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39410
---

Collator::getErrorCode

collator_get_error_code

Lee el último error del collator

## Descripción

Estilo orientado a objetos

```php
public Collator::getErrorCode(): int
```php

Estilo procedimental

```php
collator_get_error_code(Collator $object): int
```

## Parámetros

`object`  
Objeto `Collator`.

## Valores devueltos

El código de error devuelto por la última llamada a un objeto de la API `Collator`, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `collator_get_error_code`

```php
<?php
$coll = collator_create( 'en_US' );
if( collator_get_attribute( $coll, Collator::FRENCH_COLLATION ) === false )
        handle_error( collator_get_error_code() );
?>

    
```

## Véase también

`collator_get_error_message`
