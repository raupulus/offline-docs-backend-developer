---
title: Ds\Collection::toArray
description: Convierte la colección en un array
source_url: https://www.php.net/manual/es/ds-collection.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/collection/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 6bd5455a1
order: 14440
---

Ds\Collection::toArray

Convierte la colección en un

array

## Descripción

```php
public Ds\Collection::toArray(): array
```php

Convierte la colección en un `array`.

> [!NOTE]
> La conversión a un `array` aún no es soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todos los valores en el mismo orden que la colección.

## Ejemplos

`Ds\Collection::toArray` ejemplo

```
<?php
$collection = new \Ds\Vector([1, 2, 3]);

var_dump($collection->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
