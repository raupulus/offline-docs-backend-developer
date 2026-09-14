---
title: Ds\Set::reverse
description: Invierte el conjunto en su lugar
source_url: https://www.php.net/manual/es/ds-set.reverse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/reverse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15970
---

Ds\Set::reverse

Invierte el conjunto en su lugar

## Descripción

```php
public Ds\Set::reverse(): void
```php

Invierte el conjunto en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Set::reverse`

```
<?php
$set = new \Ds\Set(["a", "b", "c"]);
$set->reverse();

print_r($set);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Set Object
    (
        [0] => c
        [1] => b
        [2] => a
    )
