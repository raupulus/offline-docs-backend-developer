---
title: is_null
description: Indica si una variable es null
source_url: https://www.php.net/manual/es/function.is-null.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-null.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: d816a0fad
order: 100650
---

is_null

Indica si una variable es

null

## Descripción

```php
is_null(mixed $value): bool
```php

Indica si la variable dada es `null`.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Devuelve `true` si `value` es `null`, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_null`

```
<?php

error_reporting(E_ALL);

$foo = NULL;
var_dump(is_null($inexistent), is_null($foo));

?>

    
```php

## Véase también

El tipo [`null`](#language.types.null.syntax), `isset`, `is_bool`, `is_numeric`, `is_float`, `is_int`, `is_string`, `is_object`, `is_array`
