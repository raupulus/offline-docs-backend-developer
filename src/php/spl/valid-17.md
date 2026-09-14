---
title: SplObjectStorage::valid
description: Comprobar si la entrada actual del iterador es válida
source_url: https://www.php.net/manual/es/splobjectstorage.valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85250
---

SplObjectStorage::valid

Comprobar si la entrada actual del iterador es válida

## Descripción

```php
public SplObjectStorage::valid(): bool
```php

Devuelve si la entrada actual del iterador es válida.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la entrada actual del iterador es válida, en caso contrario `false`.

## Ejemplos

Ejemplo de `SplObjectStorage::valid`

```
<?php
$s = new SplObjectStorage();

$o1 = new stdClass;
$o2 = new stdClass;

$s->attach($o1, "d1");
$s->attach($o2, "d2");

$s->rewind();
while($s->valid()) {
    echo $s->key()."\n";
    $s->next();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    0
    1

## Véase también

SplObjectStorage::current, SplObjectStorage::getInfo
