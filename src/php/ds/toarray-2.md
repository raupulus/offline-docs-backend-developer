---
title: Ds\Deque::toArray
description: Convierte el deque en un array
source_url: https://www.php.net/manual/es/ds-deque.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14770
---

Ds\Deque::toArray

Convierte el deque en un

array

## Descripción

```php
public Ds\Deque::toArray(): array
```php

Convierte el deque en un `array`.

> [!NOTE]
> La conversión en un `array` aún no es soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todas las valores en el mismo orden que el deque.

## Ejemplos

Ejemplo de `Ds\Deque::toArray`

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);

var_dump($deque->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
