---
title: ArrayObject::serialize
description: Serializa un ArrayObject
source_url: https://www.php.net/manual/es/arrayobject.serialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/serialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81510
---

ArrayObject::serialize

Serializa un ArrayObject

## Descripción

```php
public ArrayObject::serialize(): string
```php

Serializa un `ArrayObject`.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La representación serializada de un objeto `ArrayObject`.

## Ejemplos

Ejemplo con ArrayObject::serialize

```
<?php
$o = new ArrayObject();

$s1 = serialize($o);
$s2 = $o->serialize();

var_dump($s1);
var_dump($s2);
?>

    
```php

El ejemplo anterior mostrará:

    string(45) "C:11:"ArrayObject":21:{x:i:0;a:0:{};m:a:0:{}}"
    string(21) "x:i:0;a:0:{};m:a:0:{}"

## Véase también

ArrayObject::unserialize, `serialize`, [Serialización de objetos](#language.oop5.serialization)
