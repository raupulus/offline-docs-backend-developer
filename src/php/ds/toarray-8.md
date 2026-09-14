---
title: Ds\Stack::toArray
description: Convierte la pila en un array
source_url: https://www.php.net/manual/es/ds-stack.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/stack/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16170
---

Ds\Stack::toArray

Convierte la pila en un

array

## Descripción

```php
public Ds\Stack::toArray(): array
```php

Convierte la pila en un `array`.

> [!NOTE]
> La conversión en `array` no está aún soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todos los valores en el mismo orden que la pila.

## Ejemplos

Ejemplo de `Ds\Stack::toArray`

```
<?php
$stack = new \Ds\Stack([1, 2, 3]);

var_dump($stack->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      int(3)
      [1]=>
      int(2)
      [2]=>
      int(1)
    }
