---
title: SplObjectStorage::serialize
description: Serializa el almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.serialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/serialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85220
---

SplObjectStorage::serialize

Serializa el almacenamiento

## Descripción

```php
public SplObjectStorage::serialize(): string
```php

Devuelve un string que representa el almacenamiento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un string que representa el almacenamiento.

## Ejemplos

Ejemplo de `SplObjectStorage::serialize`

```
<?php
$s = new SplObjectStorage;
$o = new stdClass;
$s[$o] = "datos";

echo $s->serialize()."\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    x:i:1;O:8:"stdClass":0:{},s:4:"datos";;m:a:0:{}

## Véase también

SplObjectStorage::unserialize
