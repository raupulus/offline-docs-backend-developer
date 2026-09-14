---
title: ArrayObject::offsetSet
description: Define $newval como valor en el $index especificado
source_url: https://www.php.net/manual/es/arrayobject.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81490
---

ArrayObject::offsetSet

Define \$newval como valor en el \$index especificado

## Descripción

```php
public ArrayObject::offsetSet(mixed $key, mixed $value): void
```php

Define `value` como valor en el índice `key` especificado.

## Parámetros

`key`  
El índice a definir.

`value`  
El nuevo valor del índice `key`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con ArrayObject::offsetSet

```
<?php
class Example {
    public $property = 'prop:public';
}
$arrayobj = new ArrayObject(new Example());
$arrayobj->offsetSet(4, 'four');
$arrayobj->offsetSet('group', array('g1', 'g2'));
var_dump($arrayobj);

$arrayobj = new ArrayObject(array('zero','one'));
$arrayobj->offsetSet(null, 'last');
var_dump($arrayobj);
?>

    
```php

El ejemplo anterior mostrará:

    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      object(Example)#2 (3) {
        ["property"]=>
        string(11) "prop:public"
        ["4"]=>
        string(4) "four"
        ["group"]=>
        array(2) {
          [0]=>
          string(2) "g1"
          [1]=>
          string(2) "g2"
        }
      }
    }
    object(ArrayObject)#3 (1) {
      ["storage":"ArrayObject":private]=>
      array(3) {
         [0]=>
         string(4) "zero"
         [1]=>
         string(3) "one"
         [2]=>
         string(4) "last"
      }
    }

## Véase también

ArrayObject::append
