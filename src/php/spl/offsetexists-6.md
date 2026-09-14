---
title: SplObjectStorage::offsetExists
description: Comprueba si un objeto existe en el almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/offsetexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85140
---

SplObjectStorage::offsetExists

Comprueba si un objeto existe en el almacenamiento

## Descripción

```php
public SplObjectStorage::offsetExists(object $object): bool
```php

Comprueba si un `object` existe en el almacenamiento.

> [!NOTE]
> SplObjectStorage::offsetExists es un alias de SplObjectStorage::contains.

## Parámetros

`object`  
El `object` a ser comprobado.

## Valores devueltos

Devuelve `true` si el `object` existe en el almacenamiento, y `false` en caso contrario.

## Ejemplos

Ejemplo de `SplObjectStorage::offsetExists`

```
<?php
$s = new SplObjectStorage;
$o1 = new stdClass;
$o2 = new stdClass;

$s->attach($o1);

var_dump($s->offsetExists($o1)); // Similar a isset($s[$o1])
var_dump($s->offsetExists($o2)); // Similar a isset($s[$o2])
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)

## Véase también

SplObjectStorage::offsetSet, SplObjectStorage::offsetGet, SplObjectStorage::offsetUnset
