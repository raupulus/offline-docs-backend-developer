---
title: Ds\Vector::merge
description: Devuelve el resultado de la adición de todos los valores dados al vector
source_url: https://www.php.net/manual/es/ds-vector.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16360
---

Ds\Vector::merge

Devuelve el resultado de la adición de todos los valores dados al vector

## Descripción

```php
public Ds\Vector::merge(mixed $values): Ds\Vector
```php

Devuelve el resultado de la adición de todos los valores dados al vector.

## Parámetros

`values`  
Un objeto `traversable` o un `array`.

## Valores devueltos

El resultado de la adición de todos los valores dados al vector, efectivamente el mismo que añadir los valores a una copia, y luego devolver esta copia.

> [!NOTE]
> La instancia actual no será afectada.

## Ejemplos

Ejemplo de `Ds\Vector::merge`

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);

var_dump($vector->merge([4, 5, 6]));
var_dump($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Vector)#2 (6) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
      [3]=>
      int(4)
      [4]=>
      int(5)
      [5]=>
      int(6)
    }
    object(Ds\Vector)#1 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
