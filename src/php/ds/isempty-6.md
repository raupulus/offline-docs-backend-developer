---
title: Ds\Queue::isEmpty
description: Indica si la cola está vacía
source_url: https://www.php.net/manual/es/ds-queue.isempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/queue/isempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e924f5b8
order: 15430
---

Ds\Queue::isEmpty

Indica si la cola está vacía

## Descripción

```php
public Ds\Queue::isEmpty(): bool
```php

Indica si la cola está vacía.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la cola está vacía, de lo contrario `false`.

## Ejemplos

Ejemplo de `Ds\Queue::isEmpty`

```
<?php
$a = new \Ds\Queue([1, 2, 3]);
$b = new \Ds\Queue();

var_dump($a->isEmpty());
var_dump($b->isEmpty());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
