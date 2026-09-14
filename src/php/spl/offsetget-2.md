---
title: ArrayObject::offsetGet
description: Devuelve el valor del índice especificado
source_url: https://www.php.net/manual/es/arrayobject.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81480
---

ArrayObject::offsetGet

Devuelve el valor del índice especificado

## Descripción

```php
public ArrayObject::offsetGet(mixed $key): mixed
```php

## Parámetros

`key`  
El índice solicitado.

## Valores devueltos

El valor en el índice o `null`.

## Errores/Excepciones

Genera una advertencia de nivel `E_NOTICE` cuando el índice especificado no existe.

## Ejemplos

Ejemplo con ArrayObject::offsetGet

```
<?php
$arrayobj = new ArrayObject(array('zero', 7, 'example'=>'e.g.'));
var_dump($arrayobj->offsetGet(1));
var_dump($arrayobj->offsetGet('example'));
var_dump($arrayobj->offsetExists('notfound'));
?>

    
```php

El ejemplo anterior mostrará:

    int(7)
    string(4) "e.g."
    bool(false)
