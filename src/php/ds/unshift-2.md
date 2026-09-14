---
title: Ds\Sequence::unshift
description: Añade valores al inicio de la secuencia
source_url: https://www.php.net/manual/es/ds-sequence.unshift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/unshift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15750
---

Ds\Sequence::unshift

Añade valores al inicio de la secuencia

## Descripción

```php
abstract public Ds\Sequence::unshift([mixed $values]): void
```php

Añade valores al inicio de la secuencia, desplazando todos los valores actuales hacia adelante para hacer espacio para los nuevos valores.

## Parámetros

`values`  
Los valores a añadir al inicio de la secuencia.

> [!NOTE]
> Varios valores serán añadidos en el mismo orden en que son pasados.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Sequence::unshift`

```
<?php
$sequence = new \Ds\Vector([1, 2, 3]);

$sequence->unshift("a");
$sequence->unshift("b", "c");

print_r($sequence);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => b
        [1] => c
        [2] => a
        [3] => 1
        [4] => 2
        [5] => 3
    )
