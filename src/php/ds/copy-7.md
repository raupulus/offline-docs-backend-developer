---
title: Ds\Set::copy
description: Devuelve una copia superficial de la secuencia
source_url: https://www.php.net/manual/es/ds-set.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15820
---

Ds\Set::copy

Devuelve una copia superficial de la secuencia

## Descripción

```php
public Ds\Set::copy(): Ds\Set
```php

Devuelve una copia superficial de la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial de la secuencia.

## Ejemplos

Ejemplo de `Ds\Set::copy`

```
<?php
$a = new \Ds\Set([1, 2, 3]);
$b = $a->copy();

// Cambiar la copia no afecta al original
$b->add(4);

print_r($a);
print_r($b);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Set Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
    )
    Ds\Set Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
        [3] => 4
    )
