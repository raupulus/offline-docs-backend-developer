---
title: is_array
description: Determina si una variable es un array
source_url: https://www.php.net/manual/es/function.is-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 0e9db3836
order: 100550
---

is_array

Determina si una variable es un array

## Descripción

```php
is_array(mixed $value): bool
```php

`is_array` determina si la variable dada es un array.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Devuelve `true` si `value` es un `array`, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_array`

```
<?php
$yes = array('esto', 'es', 'un array');

echo is_array($yes) ? 'Array' : 'no es un array';
echo "\n";

$no = 'esto es un string';

echo is_array($no) ? 'Array' : 'no es un array';
?>

    
```php

El ejemplo anterior mostrará:

    Array
    no es un array

## Véase también

`array_is_list`, `is_float`, `is_int`, `is_string`, `is_object`
