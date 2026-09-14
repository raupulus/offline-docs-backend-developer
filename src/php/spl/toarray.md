---
title: SplFixedArray::toArray
description: Devuelve un array PHP de un array fijo
source_url: https://www.php.net/manual/es/splfixedarray.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84810
---

SplFixedArray::toArray

Devuelve un array PHP de un array fijo

## Descripción

```php
public SplFixedArray::toArray(): array
```php

Devuelve un array PHP de un array fijo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` PHP, similar al array fijo.

## Ejemplos

Ejemplo de `SplFixedArray::toArray`

```
<?php
$fa = new SplFixedArray(3);
$fa[0] = 0;
$fa[2] = 2;
var_dump($fa->toArray());
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      int(0)
      [1]=>
      NULL
      [2]=>
      int(2)
    }
