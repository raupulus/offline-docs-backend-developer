---
title: Ds\Vector::toArray
description: Convierte el vector en array
source_url: https://www.php.net/manual/es/ds-vector.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16500
---

Ds\Vector::toArray

Convierte el vector en

array

## Descripción

```php
public Ds\Vector::toArray(): array
```php

Convierte el vector en un `array`.

> [!NOTE]
> La conversión en `array` aún no es soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todos los valores en el mismo orden que el vector.

## Ejemplos

Ejemplo de `Ds\Vector::toArray`

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);

var_dump($vector->toArray());
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
