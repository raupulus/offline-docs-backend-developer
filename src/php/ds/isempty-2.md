---
title: Ds\Deque::isEmpty
description: Indica si la deque está vacía
source_url: https://www.php.net/manual/es/ds-deque.isempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/isempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e924f5b8
order: 14580
---

Ds\Deque::isEmpty

Indica si la deque está vacía

## Descripción

```php
public Ds\Deque::isEmpty(): bool
```php

Indica si la deque está vacía.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la deque está vacía, `false` en caso contrario.

## Ejemplos

Ejemplo de `Ds\Deque::isEmpty`

```
<?php
$a = new \Ds\Deque([1, 2, 3]);
$b = new \Ds\Deque();

var_dump($a->isEmpty());
var_dump($b->isEmpty());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
