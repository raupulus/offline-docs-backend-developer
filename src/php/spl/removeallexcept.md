---
title: SplObjectStorage::removeAllExcept
description: Remover objetos excepto los contenidos en otro almacenamiento del almacenamiento
  actual
source_url: https://www.php.net/manual/es/splobjectstorage.removeallexcept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/removeallexcept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85190
---

SplObjectStorage::removeAllExcept

Remover objetos excepto los contenidos en otro almacenamiento del almacenamiento actual

## Descripción

```php
public SplObjectStorage::removeAllExcept(SplObjectStorage $storage): int
```php

Remover todos los objetos excepto los contenidos en otro almacenamiento del almacenamiento actual.

## Parámetros

`storage`  
El almacenamiento que contiene los elementos a mantener en el almacenamiento actual.

## Valores devueltos

Devuelve el número de objetos restantes.

## Ejemplos

Ejemplo de `SplObjectStorage::removeAllExcept`

```
<?php
$a = (object) 'a';
$b = (object) 'b';
$c = (object) 'c';

$foo = new SplObjectStorage;
$foo->attach($a);
$foo->attach($b);

$bar = new SplObjectStorage;
$bar->attach($b);
$bar->attach($c);

$foo->removeAllExcept($bar);
var_dump($foo->contains($a));
var_dump($foo->contains($b));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
