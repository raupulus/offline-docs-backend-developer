---
title: Ds\Sequence::push
description: Añade valores al final de la secuencia
source_url: https://www.php.net/manual/es/ds-sequence.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 15630
---

Ds\Sequence::push

Añade valores al final de la secuencia

## Descripción

```php
abstract public Ds\Sequence::push(mixed ...$values): void
```php

Añade valores al final de la secuencia.

## Parámetros

`values`  
Los valores a añadir.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Sequence::push`

```
<?php
$sequence = new \Ds\Vector();

$sequence->push("a");
$sequence->push("b");
$sequence->push("c", "d");
$sequence->push(...["e", "f"]);

print_r($sequence);
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
