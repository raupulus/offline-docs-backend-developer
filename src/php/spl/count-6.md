---
title: SplFixedArray::count
description: Devuelve el tamaño del array
source_url: https://www.php.net/manual/es/splfixedarray.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84660
---

SplFixedArray::count

Devuelve el tamaño del array

## Descripción

```php
public SplFixedArray::count(): int
```php

Devuelve el tamaño del array.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tamaño del array.

## Ejemplos

Ejemplo de SplFixedArray::count

```
<?php
$array = new SplFixedArray(5);
echo $array->count() . "\n";
echo count($array) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    5
    5

## Notas

> [!NOTE]
> Este método es funcionalmente equivalente al método SplFixedArray::getSize.

> [!NOTE]
> El cómputo de elementos es siempre igual al tamaño del conjunto ya que todos los valores son inicialmente inicializados con `null`.

## Véase también

SplFixedArray::getSize
