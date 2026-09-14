---
title: Ds\Vector::contains
description: Determina si el vector contiene valores dados
source_url: https://www.php.net/manual/es/ds-vector.contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 16230
---

Ds\Vector::contains

Determina si el vector contiene valores dados

## Descripción

```php
public Ds\Vector::contains(mixed ...$values): bool
```php

Determina si el vector contiene todos los valores.

## Parámetros

`values`  
Los valores a verificar.

## Valores devueltos

`false` si uno de los `valores` proporcionados no está en el vector, de lo contrario `true`.

## Ejemplos

Ejemplo de `Ds\Vector::contains`

```
<?php
$vector = new \Ds\Vector(['a', 'b', 'c', 1, 2, 3]);

var_dump($vector->contains('a'));                // true
var_dump($vector->contains('a', 'b'));           // true
var_dump($vector->contains('c', 'd'));           // false

var_dump($vector->contains(...['c', 'b', 'a'])); // true

// Siempre estricto
var_dump($vector->contains(1));                  // true
var_dump($vector->contains('1'));                // false

var_dump($vector->contains(...[]));               // true
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
