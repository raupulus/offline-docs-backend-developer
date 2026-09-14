---
title: is_bool
description: Determina si una variable es un bool
source_url: https://www.php.net/manual/es/function.is-bool.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-bool.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: d816a0fad
order: 100560
---

is_bool

Determina si una variable es un bool

## Descripción

```php
is_bool(mixed $value): bool
```php

`is_bool` determina si la variable dada es un bool.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Retorna `true` si `value` es un `bool`, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_bool`

```
<?php
$a = false;
$b = 0;

// Si $a es un bool, is_bool retornará true
if (is_bool($a) === true) {
    echo "Sí, es un bool.\n";
}

// Si $b no es un bool, is_bool retornará false
if (is_bool($b) === false) {
    echo "No, no es un bool.\n";
}
?>

    
```php

## Véase también

`is_float`, `is_int`, `is_string`, `is_object`, `is_array`
