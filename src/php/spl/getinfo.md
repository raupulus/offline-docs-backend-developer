---
title: SplObjectStorage::getInfo
description: Devuelve los datos asociados con la entrada del iterador actual
source_url: https://www.php.net/manual/es/splobjectstorage.getinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/getinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85110
---

SplObjectStorage::getInfo

Devuelve los datos asociados con la entrada del iterador actual

## Descripción

```php
public SplObjectStorage::getInfo(): mixed
```php

Devuelve los datos o información, asociada al objeto señalado por la posición actual del iterador.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Los datos asociados con la posición actual del iterador.

## Ejemplos

Ejemplo de `SplObjectStorage::getInfo`

```
<?php
$s = new SplObjectStorage();

$o1 = new stdClass;
$o2 = new stdClass;

$s->attach($o1, "d1");
$s->attach($o2, "d2");

$s->rewind();
while($s->valid()) {
    $index  = $s->key();
    $object = $s->current(); // similar a current($s)
    $data   = $s->getInfo();

    var_dump($object);
    var_dump($data);
    $s->next();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (0) {
    }
    string(2) "d1"
    object(stdClass)#3 (0) {
    }
    string(2) "d2"

## Véase también

SplObjectStorage::current, SplObjectStorage::rewind, SplObjectStorage::key, SplObjectStorage::next, SplObjectStorage::valid, SplObjectStorage::setInfo
