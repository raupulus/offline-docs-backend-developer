---
title: Ds\Vector::push
description: Añade valores al final del vector
source_url: https://www.php.net/manual/es/ds-vector.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 16380
---

Ds\Vector::push

Añade valores al final del vector

## Descripción

```php
public Ds\Vector::push(mixed ...$values): void
```php

Añade valores al final del vector.

## Parámetros

`values`  
Los valores a añadir.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Vector::push`

```
<?php
$vector = new \Ds\Vector();

$vector->push("a");
$vector->push("b");
$vector->push("c", "d");
$vector->push(...["e", "f"]);

print_r($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => a
        [1] => b
        [2] => c
        [3] => d
        [4] => e
        [5] => f
    )
