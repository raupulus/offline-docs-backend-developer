---
title: Ds\Sequence::contains
description: Determina si la secuencia contiene valores dados
source_url: https://www.php.net/manual/es/ds-sequence.contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 15520
---

Ds\Sequence::contains

Determina si la secuencia contiene valores dados

## Descripción

```php
abstract public Ds\Sequence::contains(mixed ...$values): bool
```php

Determina si la secuencia contiene todos los valores.

## Parámetros

`values`  
Los valores a verificar.

## Valores devueltos

`false` si uno de los `values` proporcionados no está en la secuencia, `true` en caso contrario.

## Ejemplos

Ejemplo de `Ds\Sequence::contains`

```
<?php
$sequence = new \Ds\Vector(['a', 'b', 'c', 1, 2, 3]);

var_dump($sequence->contains('a'));                // true
var_dump($sequence->contains('a', 'b'));           // true
var_dump($sequence->contains('c', 'd'));           // false

var_dump($sequence->contains(...['c', 'b', 'a'])); // true

// Siempre estricto
var_dump($sequence->contains(1));                  // true
var_dump($sequence->contains('1'));                // false

var_dump($sequence->contains(...[]));               // true
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
