---
title: ArrayObject::offsetExists
description: Verifica si un índice existe
source_url: https://www.php.net/manual/es/arrayobject.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/offsetexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81470
---

ArrayObject::offsetExists

Verifica si un índice existe

## Descripción

```php
public ArrayObject::offsetExists(mixed $key): bool
```php

## Parámetros

`key`  
El índice a verificar.

## Valores devueltos

`true` si el índice solicitado existe, de lo contrario `false`

## Ejemplos

Ejemplo con ArrayObject::offsetExists

```
<?php
$arrayobj = new ArrayObject(array('zero', 'one', 'example'=>'e.g.'));
var_dump($arrayobj->offsetExists(1));
var_dump($arrayobj->offsetExists('example'));
var_dump($arrayobj->offsetExists('notfound'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(true)
    bool(false)
