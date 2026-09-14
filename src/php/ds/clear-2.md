---
title: Ds\Deque::clear
description: Elimina todos los valores del deque
source_url: https://www.php.net/manual/es/ds-deque.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14480
---

Ds\Deque::clear

Elimina todos los valores del deque

## Descripción

```php
public Ds\Deque::clear(): void
```php

Elimina todos los valores del deque.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Deque::clear`

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);
print_r($deque);

$deque->clear();
print_r($deque);
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
    )
