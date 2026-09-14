---
title: Ds\Sequence::reversed
description: Devuelve una copia invertida
source_url: https://www.php.net/manual/es/ds-sequence.reversed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/reversed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15670
---

Ds\Sequence::reversed

Devuelve una copia invertida

## Descripción

```php
abstract public Ds\Sequence::reversed(): Ds\Sequence
```php

Devuelve una copia invertida de la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia invertida de la secuencia.

> [!NOTE]
> La instancia actual no se ve afectada.

## Ejemplos

Ejemplo de `Ds\Sequence::reversed`

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c"]);

print_r($sequence->reversed());
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
    Ds\Vector Object
    (
        [0] => a
        [1] => b
        [2] => c
    )
