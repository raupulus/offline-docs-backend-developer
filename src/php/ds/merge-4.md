---
title: Ds\Set::merge
description: Devuelve el resultado de la adición de todos los valores de la secuencia
source_url: https://www.php.net/manual/es/ds-set.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15940
---

Ds\Set::merge

Devuelve el resultado de la adición de todos los valores de la secuencia

## Descripción

```php
public Ds\Set::merge(mixed $values): Ds\Set
```php

Devuelve el resultado de la adición de todos los valores de la secuencia.

## Parámetros

`values`  
Un objeto `traversable` o un `array`.

## Valores devueltos

El resultado de la adición de todos los valores dados a la secuencia, efectivamente el mismo que añadir los valores a una copia, y luego devolver esta copia.

> [!NOTE]
> La instancia actual no será afectada.

## Ejemplos

Ejemplo de `Ds\Set::merge`

```
<?php
$set = new \Ds\Set([1, 2, 3]);

var_dump($set->merge([3, 4, 5]));
var_dump($set);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#2 (6) {
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
    }
    object(Ds\Set)#1 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
