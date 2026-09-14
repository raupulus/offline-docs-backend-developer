---
title: is_scalar
description: Indica si una variable es un escalar
source_url: https://www.php.net/manual/es/function.is-scalar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-scalar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: d816a0fad
order: 100700
---

is_scalar

Indica si una variable es un escalar

## Descripción

```php
is_scalar(mixed $value): bool
```php

Indica si una [expresión](#language.expressions) es evaluada como un valor escalar.

Consulte [tipos escalares](#language.types.type-system.atomic.scalar) para más información.

> [!NOTE]
> `is_scalar` no considera los valores de tipo `resource` como escalares, dado que los recursos son tipos abstractos, basados en enteros. Esto es susceptible de cambiar.

> [!NOTE]
> La función `is_scalar` no considera el valor NULL como un escalar.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Devuelve `true` si `value` es un escalar, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_scalar`

```
<?php
function show_var($var)
{
    if (is_scalar($var)) {
        echo $var, PHP_EOL;
    } else {
        var_dump($var);
    }
}

$pi = 3.1416;
$proteines = array("hemoglobina", "citocromo c oxidasa", "ferredoxina");

show_var($pi);

show_var($proteines);
?>

    
```php

El ejemplo anterior mostrará:

    3.1416
    array(3) {
      [0]=>
      string(11) "hemoglobina"
      [1]=>
      string(20) "citocromo c oxidasa"
      [2]=>
      string(11) "ferredoxina"
    }

## Véase también

`is_float`, `is_int`, `is_numeric`, `is_real`, `is_string`, `is_bool`, `is_object`, `is_array`
