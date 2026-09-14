---
title: Ds\Deque::contains
description: Determina si el deque contiene valores dados
source_url: https://www.php.net/manual/es/ds-deque.contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 14500
---

Ds\Deque::contains

Determina si el deque contiene valores dados

## Descripción

```php
public Ds\Deque::contains(mixed ...$values): bool
```php

Determina si el deque contiene todos los valores.

## Parámetros

`values`  
Los valores a verificar.

## Valores devueltos

`false` si uno de los `valores` proporcionados no está en el deque, `true` en caso contrario.

## Ejemplos

Ejemplo de `Ds\Deque::contains`

```
<?php
$deque = new \Ds\Deque(['a', 'b', 'c', 1, 2, 3]);

var_dump($deque->contains('a'));                // true
var_dump($deque->contains('a', 'b'));           // true
var_dump($deque->contains('c', 'd'));           // false

var_dump($deque->contains(...['c', 'b', 'a'])); // true

// Siempre estricto
var_dump($deque->contains(1));                  // true
var_dump($deque->contains('1'));                // false

var_dump($deque->contains(...[]));               // true
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    bool(false)
    bool(true)
    bool(true)
    bool(false)
    bool(true)
