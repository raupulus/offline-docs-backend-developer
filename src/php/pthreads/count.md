---
title: Threaded::count
description: Manipulación
source_url: https://www.php.net/manual/es/threaded.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66790
---

Threaded::count

Manipulación

## Descripción

```php
public Threaded::count(): int
```php

Devuelve el número de propiedades para este objeto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Cuenta las propiedades de un objeto

```
<?php
$safe = new Threaded();

while (count($safe) < 10) {
    $safe[] = count($safe);
}

var_dump(count($safe));
?>

   
```php

El ejemplo anterior mostrará:

    int(10)
