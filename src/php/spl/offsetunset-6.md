---
title: SplObjectStorage::offsetUnset
description: Quita un objeto de el almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/offsetunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85170
---

SplObjectStorage::offsetUnset

Quita un objeto de el almacenamiento

## Descripción

```php
public SplObjectStorage::offsetUnset(object $object): void
```php

Quitar un `object` de el almacenamiento.

> [!NOTE]
> SplObjectStorage::offsetUnset es un alias de SplObjectStorage::detach.

## Parámetros

`object`  
El `object` a ser removido.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `SplObjectStorage::offsetUnset`

```
<?php
$o = new stdClass;
$s = new SplObjectStorage();
$s->attach($o);
var_dump(count($s));
$s->offsetUnset($o); // Similar a unset($s[$o])
var_dump(count($s));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(1)
    int(0)

## Véase también

SplObjectStorage::offsetGet, SplObjectStorage::offsetSet, SplObjectStorage::offsetExists
