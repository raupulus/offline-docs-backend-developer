---
title: Ds\Vector::insert
description: Inserta valores en un índice dado
source_url: https://www.php.net/manual/es/ds-vector.insert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/insert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 16300
---

Ds\Vector::insert

Inserta valores en un índice dado

## Descripción

```php
public Ds\Vector::insert(int $index, mixed ...$values): void
```php

Inserta valores en el vector en un índice dado.

## Parámetros

`index`  
El índice en el cual insertar. `0 <= index <= count`

> [!NOTE]
> Es posible insertar en el índice igual al número de valores.

`values`  
El o los valores a insertar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

`OutOfRangeException` si el índice no es válido.

## Ejemplos

Ejemplo de `Ds\Vector::insert`

```
<?php
$vector = new \Ds\Vector();

$vector->insert(0, "e");             // [e]
$vector->insert(1, "f");             // [e, f]
$vector->insert(2, "g");             // [e, f, g]
$vector->insert(0, "a", "b");        // [a, b, e, f, g]
$vector->insert(2, ...["c", "d"]);   // [a, b, c, d, e, f, g]

var_dump($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Vector)#1 (7) {
      [0]=>
      string(1) "a"
      [1]=>
      string(1) "b"
      [2]=>
      string(1) "c"
      [3]=>
      string(1) "d"
      [4]=>
      string(1) "e"
      [5]=>
      string(1) "f"
      [6]=>
      string(1) "g"
    }
