---
title: Threaded::shift
description: Manipulación
source_url: https://www.php.net/manual/es/threaded.shift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/shift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66880
---

Threaded::shift

Manipulación

## Descripción

```php
public Threaded::shift(): bool
```php

Se elimina el primer elemento de la tabla de propiedades del objeto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El primer elemento de la tabla de propiedades del objeto.

## Ejemplos

Eliminación del primer elemento de la tabla de propiedades del objeto threadado

```
<?php
$safe = new Threaded();

while (count($safe) < 10)
    $safe[] = count($safe);

var_dump($safe->shift());
?>

   
```php

El ejemplo anterior mostrará:

    int(0)
