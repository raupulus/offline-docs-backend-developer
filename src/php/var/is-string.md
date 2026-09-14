---
title: is_string
description: Determina si una variable es de tipo string
source_url: https://www.php.net/manual/es/function.is-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 100710
---

is_string

Determina si una variable es de tipo string

## Descripción

```php
is_string(mixed $value): bool
```php

Determina si la variable dada es de tipo string.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Devuelve `true` si `value` es un `string`, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_string`

```
<?php
$values = array(false, true, null, 'abc', '23', 23, '23.5', 23.5, '', ' ', '0', 0);
foreach ($values as $value) {
    echo "is_string(";
    var_export($value);
    echo ") = ";
    echo var_dump(is_string($value));
}
?>

    
```php

El ejemplo anterior mostrará:

    is_string(false) = bool(false)
    is_string(true) = bool(false)
    is_string(NULL) = bool(false)
    is_string('abc') = bool(true)
    is_string('23') = bool(true)
    is_string(23) = bool(false)
    is_string('23.5') = bool(true)
    is_string(23.5) = bool(false)
    is_string('') = bool(true)
    is_string(' ') = bool(true)
    is_string('0') = bool(true)
    is_string(0) = bool(false)

## Véase también

`is_float`, `is_int`, `is_bool`, `is_object`, `is_array`
