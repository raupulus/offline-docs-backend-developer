---
title: SplObjectStorage::current
description: Devuelve el objeto actual
source_url: https://www.php.net/manual/es/splobjectstorage.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85080
---

SplObjectStorage::current

Devuelve el objeto actual

## Descripción

```php
public SplObjectStorage::current(): object
```php

Devuelve el objeto actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El `object` en la posición actual del iterador.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `SplObjectStorage::current` ahora lanza una excepción `Error` si la posición actual es inválida. Anteriormente, `false` era devuelto. |

## Ejemplos

Ejemplo con `SplObjectStorage::current`

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
    $object = $s->current(); // similar to current($s)
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

SplObjectStorage::rewind, SplObjectStorage::key, SplObjectStorage::next, SplObjectStorage::valid, SplObjectStorage::getInfo
