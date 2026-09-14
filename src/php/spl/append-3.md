---
title: ArrayObject::append
description: Añade el valor al final de un array
source_url: https://www.php.net/manual/es/arrayobject.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81350
---

ArrayObject::append

Añade el valor al final de un array

## Descripción

```php
public ArrayObject::append(mixed $value): void
```php

Añade un elemento al final del array.

> [!NOTE]
> Este método no puede ser llamado cuando el objeto `ArrayObject` ha sido construido a partir de otro objeto. En ese caso, utilice el método ArrayObject::offsetSet.

## Parámetros

`value`  
El valor añadido.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con ArrayObject::append

```
<?php
$arrayobj = new ArrayObject(array('first','second','third'));
$arrayobj->append('fourth');
$arrayobj->append(array('five', 'six'));
var_dump($arrayobj);
?>

    
```php

El ejemplo anterior mostrará:

    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(5) {
        [0]=>
        string(5) "first"
        [1]=>
        string(6) "second"
        [2]=>
        string(5) "third"
        [3]=>
        string(6) "fourth"
        [4]=>
        array(2) {
          [0]=>
          string(4) "five"
          [1]=>
          string(3) "six"
        }
      }
    }

## Véase también

ArrayObject::offsetSet
