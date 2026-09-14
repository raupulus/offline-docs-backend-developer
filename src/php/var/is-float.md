---
title: is_float
description: Determina si una variable es de tipo float
source_url: https://www.php.net/manual/es/function.is-float.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-float.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: f044a792f
order: 100600
---

is_float

Determina si una variable es de tipo float

## Descripción

```php
is_float(mixed $value): bool
```php

Determina si la variable dada es de tipo float.

> [!NOTE]
> Para comprobar si una variable es un número o una cadena numérica (como las entradas de formulario, que siempre son strings), se debe utilizar la función `is_numeric`.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Retorna `true` si `value` es un `float`, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_float`

```
<?php

var_dump(is_float(27.25));
var_dump(is_float('abc'));
var_dump(is_float(23));
var_dump(is_float(23.5));
var_dump(is_float(1e7));  //Notación científica
var_dump(is_float(true));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(false)
    bool(true)
    bool(true)
    bool(false)

## Véase también

`is_bool`, `is_int`, `is_numeric`, `is_string`, `is_array`, `is_object`
