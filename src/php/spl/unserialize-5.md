---
title: SplObjectStorage::unserialize
description: Deserializa un almacenamiento desde su representación string
source_url: https://www.php.net/manual/es/splobjectstorage.unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85240
---

SplObjectStorage::unserialize

Deserializa un almacenamiento desde su representación string

## Descripción

```php
public SplObjectStorage::unserialize(string $data): void
```php

Deserializa las entradas del almacenamiento y los añade al almacenamiento actual.

## Parámetros

`data`  
La representación serializada del almacenamiento.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `SplObjectStorage::unserialize`

```
<?php
$s1 = new SplObjectStorage;
$s2 = new SplObjectStorage;
$o = new stdClass;
$s1[$o] = "datos";

$s2->unserialize($s1->serialize());

var_dump(count($s2));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(1)

## Véase también

SplObjectStorage::serialize
