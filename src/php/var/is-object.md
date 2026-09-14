---
title: is_object
description: Determina si una variable es de tipo objeto
source_url: https://www.php.net/manual/es/function.is-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: ccc438a27
order: 100670
---

is_object

Determina si una variable es de tipo objeto

## Descripción

```php
is_object(mixed $value): bool
```php

Determina si la variable dada es de tipo objeto.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Retorna `true` si `value` es un `object`, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | `is_object` retorna ahora `true` para un objeto deserializado sin una definición de clase (clase de `__PHP_Incomplete_Class`). Anteriormente se retornaba `false`. |

## Ejemplos

Ejemplo con `is_object`

```
<?php
// Declara una función simple para retornar un array
// de nuestro objeto
function get_students($obj)
{
    if (!is_object($obj)) {
        return false;
    }

    return $obj->students;
}

// Declara una nueva instancia y
// la rellena
$obj = new stdClass();
$obj->students = array('Kalle', 'Ross', 'Felipe');

var_dump(get_students(null));
var_dump(get_students($obj));
?>

    
```php

## Véase también

`is_bool`, `is_int`, `is_float`, `is_string`, `is_array`
