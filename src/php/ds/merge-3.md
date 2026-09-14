---
title: Ds\Sequence::merge
description: Devuelve el resultado de la adición de todos los valores de la secuencia
source_url: https://www.php.net/manual/es/ds-sequence.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15610
---

Ds\Sequence::merge

Devuelve el resultado de la adición de todos los valores de la secuencia

## Descripción

```php
abstract public Ds\Sequence::merge(mixed $values): Ds\Sequence
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

Ejemplo de `Ds\Sequence::merge`

```
<?php
$sequence = new \Ds\Vector([1, 2, 3]);

var_dump($sequence->merge([4, 5, 6]));
var_dump($sequence);
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
