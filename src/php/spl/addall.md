---
title: SplObjectStorage::addAll
description: Agrega todos los objetos de otro almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.addall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/addall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 85040
---

SplObjectStorage::addAll

Agrega todos los objetos de otro almacenamiento

## Descripción

```php
public SplObjectStorage::addAll(SplObjectStorage $storage): int
```php

Agrega todos los pares de objetos de datos de un diferente almacenamiento en el almacenamiento actual.

## Parámetros

`storage`  
El almacenamiento que se quiere importar.

## Valores devueltos

El número de objetos en el almacén.

## Ejemplos

Ejemplo de `SplObjectStorage::addAll`

```
<?php
$o = new stdClass;
$a = new SplObjectStorage();
$a[$o] = "hola";

$b = new SplObjectStorage();
$b->addAll($a);
echo $b[$o]."\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    hola

## Véase también

SplObjectStorage::removeAll
