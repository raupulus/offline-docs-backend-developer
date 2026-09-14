---
title: SplObjectStorage::setInfo
description: Establece los datos asociados con el iterador de la entrada actual
source_url: https://www.php.net/manual/es/splobjectstorage.setinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/setinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85230
---

SplObjectStorage::setInfo

Establece los datos asociados con el iterador de la entrada actual

## Descripción

```php
public SplObjectStorage::setInfo(mixed $info): void
```php

Asocia datos o información, con el objeto actualmente señalado por el iterador.

## Parámetros

`info`  
Los datos a ser asociados con la entrada del iterador actual.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `SplObjectStorage::setInfo`

```
<?php
$s = new SplObjectStorage();

$o1 = new stdClass;
$o2 = new stdClass;

$s->attach($o1, "d1");
$s->attach($o2, "d2");

$s->rewind();
while($s->valid()) {
    $s->setInfo("new");
    $s->next();
}
var_dump($s[$o1]);
var_dump($s[$o2]);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(3) "new"
    string(3) "new"

## Véase también

SplObjectStorage::current, SplObjectStorage::rewind, SplObjectStorage::key, SplObjectStorage::next, SplObjectStorage::valid, SplObjectStorage::getInfo
