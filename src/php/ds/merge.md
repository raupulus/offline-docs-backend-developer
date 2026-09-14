---
title: Ds\Deque::merge
description: Devuelve el resultado de la adición de todos los valores dados al deque
source_url: https://www.php.net/manual/es/ds-deque.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14630
---

Ds\Deque::merge

Devuelve el resultado de la adición de todos los valores dados al deque

## Descripción

```php
public Ds\Deque::merge(mixed $values): Ds\Deque
```php

Devuelve el resultado de la adición de todos los valores dados al deque.

## Parámetros

`values`  
Un objeto `traversable` o un `array`.

## Valores devueltos

El resultado de la adición de todos los valores dados al deque, efectivamente el mismo que añadir los valores a una copia, y luego devolver esta copia.

> [!NOTE]
> La instancia actual no será afectada.

## Ejemplos

Ejemplo de `Ds\Deque::merge`

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);

var_dump($deque->merge([4, 5, 6]));
var_dump($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Deque)#2 (6) {
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
    object(Ds\Deque)#1 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
