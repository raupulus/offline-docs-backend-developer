---
title: Ds\Deque::reverse
description: Invierte el deque en su lugar
source_url: https://www.php.net/manual/es/ds-deque.reverse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/reverse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14680
---

Ds\Deque::reverse

Invierte el deque en su lugar

## Descripción

```php
public Ds\Deque::reverse(): void
```php

Invierte el deque en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Deque::reverse`

```
<?php
$deque = new \Ds\Deque(["a", "b", "c"]);
$deque->reverse();

print_r($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => c
        [1] => b
        [2] => a
    )
