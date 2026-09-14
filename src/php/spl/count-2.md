---
title: ArrayObject::count
description: Retorna el número de propiedades públicas en el objeto ArrayObject
source_url: https://www.php.net/manual/es/arrayobject.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81380
---

ArrayObject::count

Retorna el número de propiedades públicas en el objeto

ArrayObject

## Descripción

```php
public ArrayObject::count(): int
```php

Lee el número de propiedades públicas en el objeto `ArrayObject`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna el número de propiedades públicas en el objeto `ArrayObject`.

> [!NOTE]
> Cuando el objeto `ArrayObject` es construido a partir de un `array`, todas las propiedades son públicas.

## Ejemplos

Ejemplo con ArrayObject::count

```
<?php
class Example {
    public $public = 'prop:public';
    private $prv   = 'prop:private';
    protected $prt = 'prop:protected';
}

$arrayobj = new ArrayObject(new Example());
var_dump($arrayobj->count());

$arrayobj = new ArrayObject(array('first','second','third'));
var_dump($arrayobj->count());
?>

    
```php

El ejemplo anterior mostrará:

    int(1)
    int(3)
