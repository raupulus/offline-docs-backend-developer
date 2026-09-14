---
title: SplObjectStorage::removeAll
description: Remover objetos contenidos en otro almacenamiento de el almacenamiento
  actual
source_url: https://www.php.net/manual/es/splobjectstorage.removeall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/removeall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85180
---

SplObjectStorage::removeAll

Remover objetos contenidos en otro almacenamiento de el almacenamiento actual

## Descripción

```php
public SplObjectStorage::removeAll(SplObjectStorage $storage): int
```php

Remover objetos contenidos en otro almacenamiento de el almacenamiento actual.

## Parámetros

`storage`  
El almacenamiento que contiene los elementos a remover.

## Valores devueltos

Devuelve el número de objetos restantes.

## Ejemplos

Ejemplo de `SplObjectStorage::removeAll`

```
<?php
$o1 = new stdClass;
$o2 = new stdClass;
$a = new SplObjectStorage();
$a[$o1] = "foo";

$b = new SplObjectStorage();
$b[$o1] = "bar";
$b[$o2] = "gee";

var_dump(count($b));
$b->removeAll($a);
var_dump(count($b));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(2)
    int(1)

## Véase también

SplObjectStorage::addAll
