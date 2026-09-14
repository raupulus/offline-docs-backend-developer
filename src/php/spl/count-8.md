---
title: SplObjectStorage::count
description: Devuelve el número de objetos en el almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85070
---

SplObjectStorage::count

Devuelve el número de objetos en el almacenamiento

## Descripción

```php
public SplObjectStorage::count([int $mode]): int
```php

Cuenta el número de objetos en el almacenamiento.

## Parámetros

`mode`  
Si el parámetro opcional `mode` se establece en `COUNT_RECURSIVE` (o 1), `SplObjectStorage::count` contará recursivamente el número de objetos en el almacenamiento.

## Valores devueltos

El número de objetos en el almacenamiento.

## Ejemplos

Ejemplo con `SplObjectStorage::count`

```
<?php
$s = new SplObjectStorage();
$o1 = new stdClass;
$o2 = new stdClass;

$s->attach($o1);
$s->attach($o2);
$s->attach($o1);
var_dump($s->count());
var_dump(count($s));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(2)
    int(2)

## Véase también

SplObjectStorage::attach, SplObjectStorage::detach
