---
title: Ds\Sequence::reverse
description: Invierte la secuencia en el lugar
source_url: https://www.php.net/manual/es/ds-sequence.reverse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/reverse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15660
---

Ds\Sequence::reverse

Invierte la secuencia en el lugar

## Descripción

```php
abstract public Ds\Sequence::reverse(): void
```php

Invierte la secuencia en el lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Sequence::reverse`

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c"]);
$sequence->reverse();

print_r($sequence);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => c
        [1] => b
        [2] => a
    )
