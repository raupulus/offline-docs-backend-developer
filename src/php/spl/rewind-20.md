---
title: SplObjectStorage::rewind
description: Rebobina el iterador a el primer elemento de el almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 85200
---

SplObjectStorage::rewind

Rebobina el iterador a el primer elemento de el almacenamiento

## Descripción

```php
public SplObjectStorage::rewind(): void
```php

Rebobina el iterador al primer elemento del almacenamiento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `SplObjectStorage::rewind`

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

SplObjectStorage::next
