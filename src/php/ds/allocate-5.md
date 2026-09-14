---
title: Ds\Sequence::allocate
description: Asigna suficiente memoria para una capacidad requerida
source_url: https://www.php.net/manual/es/ds-sequence.allocate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/allocate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 15490
---

Ds\Sequence::allocate

Asigna suficiente memoria para una capacidad requerida

## Descripción

```php
abstract public Ds\Sequence::allocate(int $capacity): void
```php

Asegura que se asigne suficiente memoria para una capacidad requerida. Esto elimina la necesidad de reasignar el búfer interno a medida que se añaden valores.

## Parámetros

`capacity`  
El número de valores para los cuales se debe asignar la capacidad.

> [!NOTE]
> La capacidad permanecerá igual si este valor es inferior o igual a la capacidad actual.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Sequence::allocate`

```
<?php
$sequence = new \Ds\Vector();
var_dump($sequence->capacity());

$vector->allocate(100);
var_dump($sequence->capacity());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(10)
    int(100)
