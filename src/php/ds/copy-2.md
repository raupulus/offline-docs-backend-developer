---
title: Ds\Deque::copy
description: Devuelve una copia superficial de la deque
source_url: https://www.php.net/manual/es/ds-deque.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14510
---

Ds\Deque::copy

Devuelve una copia superficial de la deque

## Descripción

```php
public Ds\Deque::copy(): Ds\Deque
```php

Devuelve una copia superficial de la deque.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia superficial de la deque.

## Ejemplos

Ejemplo de `Ds\Deque::copy`

```
<?php
$a = new \Ds\Deque([1, 2, 3]);
$b = $a->copy();

$b->push(4);

print_r($a);
print_r($b);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
    )
    Ds\Deque Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
        [3] => 4
    )
