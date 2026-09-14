---
title: SplObjectStorage::offsetSet
description: Asocia datos a un objeto en el almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85160
---

SplObjectStorage::offsetSet

Asocia datos a un objeto en el almacenamiento

## Descripción

```php
public SplObjectStorage::offsetSet(object $object, [mixed $info]): void
```php

Asocia datos a un `object` en el almacenamiento.

> [!NOTE]
> SplObjectStorage::offsetSet es un alias de SplObjectStorage::attach.

## Parámetros

`object`  
El `object` al que se le van a asociar datos.

`info`  
Los datos asociados con el `object`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `SplObjectStorage::offsetSet`

```
<?php
$s = new SplObjectStorage;

$o1 = new stdClass;

$s->offsetSet($o1, "hola"); // Similar a $s[$o1] = "hola";

var_dump($s[$o1]);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(4) "hola"

## Véase también

SplObjectStorage::attach, SplObjectStorage::offsetGet, SplObjectStorage::offsetExists, SplObjectStorage::offsetUnset
