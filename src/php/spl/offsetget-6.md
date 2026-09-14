---
title: SplObjectStorage::offsetGet
description: Devuelve los datos asociados con un object
source_url: https://www.php.net/manual/es/splobjectstorage.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85150
---

SplObjectStorage::offsetGet

Devuelve los datos asociados con un

object

## Descripción

```php
public SplObjectStorage::offsetGet(object $object): mixed
```php

Devuelve los datos asociados con un `object` en el almacenamiento.

## Parámetros

`object`  
El `object` a ser comprobado.

## Valores devueltos

Los datos previamente asociados con el `object` en el almacenamiento.

## Errores/Excepciones

Lanza una excepción de tipo `UnexpectedValueException` cuando no se pudo encontrar `object`.

## Ejemplos

Ejemplo de `SplObjectStorage::offsetGet`

```
<?php
$s = new SplObjectStorage;

$o1 = new stdClass;
$o2 = new stdClass;

$s[$o1] = "hola";
$s->attach($o2);

var_dump($s->offsetGet($o1)); // Similar a $s[$o1]
var_dump($s->offsetGet($o2)); // Similar a $s[$o2]
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(4) "hola"
    NULL

## Véase también

SplObjectStorage::offsetSet, SplObjectStorage::offsetExists, SplObjectStorage::offsetUnset
