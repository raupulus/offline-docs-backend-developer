---
title: array_reverse
description: Invierte el orden de los elementos de un array
source_url: https://www.php.net/manual/es/function.array-reverse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-reverse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: b8758b060
order: 5560
---

array_reverse

Invierte el orden de los elementos de un array

## Descripción

```php
array_reverse(array $array, [bool $preserve_keys]): array
```php

`array_reverse` devuelve un nuevo array que contiene los mismos elementos que `array`, pero en orden inverso.

## Parámetros

`array`  
El array de entrada.

`preserve_keys`  
Si se establece en `true`, las claves numéricas serán preservadas. Las claves no numéricas no se verán afectadas por esta configuración y siempre serán preservadas.

## Valores devueltos

Devuelve el array en orden inverso.

## Ejemplos

Ejemplo con `array_reverse`

```
<?php
$input  = array("php", 4.0, array("green", "red"));
$reversed = array_reverse($input);
$preserved = array_reverse($input, true);

print_r($input);
print_r($reversed);
print_r($preserved);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => php
    [1] => 4
    [2] => Array
        (
            [0] => green
            [1] => red
        )

)
Array
(
    [0] => Array
        (
            [0] => green
            [1] => red
        )

    [1] => 4
    [2] => php
)
Array
(
    [2] => Array
        (
            [0] => green
            [1] => red
        )

    [1] => 4
    [0] => php
)

    
```php

## Véase también

`array_flip`
