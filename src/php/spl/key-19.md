---
title: SplObjectStorage::key
description: Devuelve el índice en el que se encuentra el iterador actualmente
source_url: https://www.php.net/manual/es/splobjectstorage.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85120
---

SplObjectStorage::key

Devuelve el índice en el que se encuentra el iterador actualmente

## Descripción

```php
public SplObjectStorage::key(): int
```php

Devuelve el índice en el que se encuentra el iterador actualmente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El índice correspondiente a la posición del iterador.

## Ejemplos

Ejemplo de `SplObjectStorage::key`

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

    var_dump($index);
    var_dump($object);
    $s->next();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(0)
    object(stdClass)#2 (0) {
    }
    int(1)
    object(stdClass)#3 (0) {
    }

## Véase también

SplObjectStorage::rewind, SplObjectStorage::current, SplObjectStorage::next, SplObjectStorage::valid
