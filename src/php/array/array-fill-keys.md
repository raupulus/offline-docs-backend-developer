---
title: array_fill_keys
description: Rellena un array con valores, especificando las claves
source_url: https://www.php.net/manual/es/function.array-fill-keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-fill-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 96c9d88ba
order: 5260
---

array_fill_keys

Rellena un array con valores, especificando las claves

## Descripción

```php
array_fill_keys(array $keys, mixed $value): array
```php

Rellena un array con el valor del argumento `value`, y utilizando los valores del array `keys` como claves.

## Parámetros

`keys`  
Array de valores que será utilizado como claves. Los valores ilegales para las claves serán convertidos en `string`.

`value`  
Valor a utilizar para rellenar el array.

## Valores devueltos

Devuelve el array relleno.

## Ejemplos

Ejemplo con `array_fill_keys`

```
<?php
$keys = array('foo', 5, 10, 'bar');
$a = array_fill_keys($keys, 'banana');
print_r($a);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [foo] => banana
        [5] => banana
        [10] => banana
        [bar] => banana
    )

## Véase también

`array_fill`, `array_combine`
