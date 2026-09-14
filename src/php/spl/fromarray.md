---
title: SplFixedArray::fromArray
description: Importa un array PHP en una instancia SplFixedArray
source_url: https://www.php.net/manual/es/splfixedarray.fromarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/fromarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84680
---

SplFixedArray::fromArray

Importa un array PHP en una instancia

SplFixedArray

## Descripción

```php
public static SplFixedArray::fromArray(array $array, [bool $preserveKeys]): SplFixedArray
```php

Importa un `array` PHP en una nueva instancia `SplFixedArray`.

## Parámetros

`array`  
El array a importar.

`preserveKeys`  
Intenta guardar los índices numéricos usados en el array original.

## Valores devueltos

Devuelve una instancia de `SplFixedArray` conteniendo el contenido de el array.

## Ejemplos

Ejemplo de `SplFixedArray::fromArray`

```
<?php
$fa = SplFixedArray::fromArray(array(1 => 1, 0 => 2, 3 => 3));

var_dump($fa);

$fa = SplFixedArray::fromArray(array(1 => 1, 0 => 2, 3 => 3), false);

var_dump($fa);
?>

    
```php

El ejemplo anterior mostrará:

    object(SplFixedArray)#1 (4) {
      [0]=>
      int(2)
      [1]=>
      int(1)
      [2]=>
      NULL
      [3]=>
      int(3)
    }
    object(SplFixedArray)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
