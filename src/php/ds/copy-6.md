---
title: Ds\Queue::copy
description: Devuelve una copia superficial de la cola
source_url: https://www.php.net/manual/es/ds-queue.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/queue/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15410
---

Ds\Queue::copy

Devuelve una copia superficial de la cola

## Descripción

```php
public Ds\Queue::copy(): Ds\Queue
```php

Devuelve una copia superficial de la cola.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial de la cola.

## Ejemplos

Ejemplo de `Ds\Queue::copy`

```
<?php
$a = new \Ds\Queue([1, 2, 3]);
$b = $a->copy();

// Cambiar la copia no afecta al original
$b->push(4);

print_r($a);
print_r($b);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Queue Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
    )
    Ds\Queue Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
        [3] => 4
    )
