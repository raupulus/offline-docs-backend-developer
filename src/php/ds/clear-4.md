---
title: Ds\Pair::clear
description: Elimina todos los valores
source_url: https://www.php.net/manual/es/ds-pair.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/pair/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 15190
---

Ds\Pair::clear

Elimina todos los valores

## Descripción

```php
public Ds\Pair::clear(): void
```php

Elimina todos los valores del par.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Pair::clear`

```
<?php
$pair = new \Ds\Pair("a", 1);
print_r($pair);

$pair->clear();
print_r($pair);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Pair Object
    (
        [key] => a
        [value] => 1
    )
    Ds\Pair Object
    (
    )
