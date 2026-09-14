---
title: Ds\Set::clear
description: Elimina todos los valores
source_url: https://www.php.net/manual/es/ds-set.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15790
---

Ds\Set::clear

Elimina todos los valores

## Descripción

```php
public Ds\Set::clear(): void
```php

Elimina todos los valores de la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Set::clear`

```
<?php
$set = new \Ds\Set([1, 2, 3]);
print_r($set);

$set->clear();
print_r($set);
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
    )
