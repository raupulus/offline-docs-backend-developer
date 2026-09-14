---
title: NoRewindIterator::rewind
description: Evita la operación de rebobinado en el iterador interno
source_url: https://www.php.net/manual/es/norewinditerator.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/norewinditerator/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82790
---

NoRewindIterator::rewind

Evita la operación de rebobinado en el iterador interno

## Descripción

```php
public NoRewindIterator::rewind(): void
```php

Evita la operación de rebobinado en el iterador interno.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `NoRewindIterator::rewind`

Este ejemplo demuestra que, si se llama a rewind en un objeto NoRewindIterator no tiene ningún efecto.

```
<?php
$fruits = array("limon", "naranja", "manzana", "pera");

$noRewindIterator = new NoRewindIterator(new ArrayIterator($fruits));

echo $noRewindIterator->current() . "\n";
$noRewindIterator->next();
// ahora rebobine el iterador (nada debería suceder)
$noRewindIterator->rewind();
echo $noRewindIterator->current() . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    limon
    naranja
