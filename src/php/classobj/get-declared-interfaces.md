---
title: get_declared_interfaces
description: Devuelve un array con todas las interfaces declaradas
source_url: https://www.php.net/manual/es/function.get-declared-interfaces.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-declared-interfaces.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 6846ebb4e
order: 6820
---

get_declared_interfaces

Devuelve un array con todas las interfaces declaradas

## Descripción

```php
get_declared_interfaces(): array
```php

Devuelve un array con todas las interfaces declaradas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene los nombres de las interfaces declaradas en el script actual.

## Ejemplos

Ejemplo con `get_declared_interfaces`

```
<?php
print_r(get_declared_interfaces());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Traversable
        [1] => IteratorAggregate
        [2] => Iterator
        [3] => ArrayAccess
        [4] => reflector
        [5] => RecursiveIterator
        [6] => SeekableIterator
    )

## Véase también

`interface_exists`, `get_declared_classes`, `class_implements`
