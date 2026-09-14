---
title: Ds\Deque::reversed
description: Devuelve una copia invertida
source_url: https://www.php.net/manual/es/ds-deque.reversed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/reversed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14690
---

Ds\Deque::reversed

Devuelve una copia invertida

## Descripción

```php
public Ds\Deque::reversed(): Ds\Deque
```php

Devuelve una copia invertida del deque.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia invertida del deque.

> [!NOTE]
> La instancia actual no se ve afectada.

## Ejemplos

Ejemplo de `Ds\Deque::reversed`

```
<?php
$deque = new \Ds\Deque(["a", "b", "c"]);

print_r($deque->reversed());
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
    Ds\Deque Object
    (
        [0] => a
        [1] => b
        [2] => c
    )
