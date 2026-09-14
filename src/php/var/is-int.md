---
title: is_int
description: Determina si una variable es de tipo integer
source_url: https://www.php.net/manual/es/function.is-int.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-int.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 100610
---

is_int

Determina si una variable es de tipo integer

## Descripción

```php
is_int(mixed $value): bool
```php

Determina si la variable dada es de tipo integer.

> [!NOTE]
> Para comprobar si una variable es un número o una cadena numérica (como las entradas de formulario, que siempre son strings), se debe utilizar la función `is_numeric`.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Retorna `true` si `value` es un `int`, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_int`

```
<?php
$values = array(23, "23", 23.5, "23.5", null, true, false);
foreach ($values as $value) {
    echo "is_int(";
    var_export($value);
    echo ") = ";
    var_dump(is_int($value));
}
?>

    
```php

El ejemplo anterior mostrará:

    is_int(23) = bool(true)
    is_int('23') = bool(false)
    is_int(23.5) = bool(false)
    is_int('23.5') = bool(false)
    is_int(NULL) = bool(false)
    is_int(true) = bool(false)
    is_int(false) = bool(false)

## Véase también

`is_bool`, `is_float`, `is_numeric`, `is_string`, `is_array`, `is_object`
