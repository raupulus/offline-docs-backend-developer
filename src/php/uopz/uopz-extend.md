---
title: uopz_extend
description: Extiende una clase en tiempo de ejecución
source_url: https://www.php.net/manual/es/function.uopz-extend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-extend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 330a38c4d
order: 99240
---

uopz_extend

Extiende una clase en tiempo de ejecución

## Descripción

```php
uopz_extend(string $class, string $parent): bool
```php

Extiende la clase `class` utilizando la clase `parent`.

## Parámetros

`class`  
El nombre de la clase a extender

`parent`  
El nombre de la clase padre

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

A partir de PHP 7.4.0, `uopz_extend` emite una `RuntimeException`, si [OPcache](#book.opcache) está activado, y la entrada de clase de `class` o `parent` (si en un trait) es inmutable.

## Ejemplos

Ejemplo con `uopz_extend`

```
<?php
class A {}
class B {}

uopz_extend(A::class, B::class);

var_dump(class_parents(A::class));
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      ["B"]=>
      string(1) "B"
    }
