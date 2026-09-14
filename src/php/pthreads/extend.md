---
title: Threaded::extend
description: Manipulación durante la ejecución
source_url: https://www.php.net/manual/es/threaded.extend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/extend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66800
---

Threaded::extend

Manipulación durante la ejecución

## Descripción

```php
public Threaded::extend(string $class): bool
```php

Hace que la clase estándar sea segura a nivel de thread durante la ejecución.

## Parámetros

`class`  
La clase a extender.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Herencia durante la ejecución

```
<?php
class My {}

Threaded::extend(My::class);

$my = new My();

var_dump($my instanceof Threaded);
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
