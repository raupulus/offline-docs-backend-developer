---
title: gettype
description: Devuelve el tipo de la variable
source_url: https://www.php.net/manual/es/function.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 51aee00be
order: 100530
---

gettype

Devuelve el tipo de la variable

## Descripción

```php
gettype(mixed $value): string
```php

Devuelve el tipo de la variable `value`. Para verificar el tipo de la variable, se pueden utilizar las funciones `is_*`.

## Parámetros

`value`  
La variable a analizar.

## Valores devueltos

Las cadenas de caracteres que puede devolver la función son las siguientes: `"boolean"`, `"integer"`, `"double"` (por razones históricas, `"double"` es devuelto cuando un valor de tipo `float` es proporcionado, y no `"float"`), `"string"`, `"array"`, `"object"`, `"resource"`, `"resource (closed)"` a partir de PHP 7.2.0, `"NULL"`, `"unknown type"`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | Los recursos cerrados son ahora reportados como `'resource (closed)'`. Anteriormente, el valor devuelto para recursos cerrados era `'unknown type'`. |

## Ejemplos

Ejemplo con `gettype`

```
<?php

$data = array(1, 1., NULL, new stdClass, 'foo');

foreach ($data as $value) {
    echo gettype($value), "\n";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    integer
    double
    NULL
    object
    string

## Véase también

`get_debug_type`, `settype`, `get_class`, `is_array`, `is_bool`, `is_callable`, `is_float`, `is_int`, `is_null`, `is_numeric`, `is_object`, `is_resource`, `is_scalar`, `is_string`, `function_exists`, `method_exists`
