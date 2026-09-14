---
title: ArrayObject::offsetUnset
description: Elimina el valor en el índice especificado
source_url: https://www.php.net/manual/es/arrayobject.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/offsetunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81500
---

ArrayObject::offsetUnset

Elimina el valor en el índice especificado

## Descripción

```php
public ArrayObject::offsetUnset(mixed $key): void
```php

Elimina el valor en el índice especificado.

## Parámetros

`key`  
El índice a eliminar.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con ArrayObject::offsetUnset

```
<?php
$arrayobj = new ArrayObject(array(0=>'zero',2=>'two'));
$arrayobj->offsetUnset(2);
var_dump($arrayobj);
?>

    
```php

El ejemplo anterior mostrará:

    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(1) {
        [0]=>
        string(4) "zero"
      }
    }
