---
title: SplFixedArray::getSize
description: Obtiene el tamaño de el array
source_url: https://www.php.net/manual/es/splfixedarray.getsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/getsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84700
---

SplFixedArray::getSize

Obtiene el tamaño de el array

## Descripción

```php
public SplFixedArray::getSize(): int
```php

Obtener el tamaño del array.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tamaño del array, como un `int`.

## Ejemplos

Ejemplo de SplFixedArray::getSize

```
<?php
$array = new SplFixedArray(5);
echo $array->getSize()."\n";
$array->setSize(10);
echo $array->getSize()."\n";
?>

    
```php

El ejemplo anterior mostrará:

    5
    10

## Notas

> [!NOTE]
> Este método es funcionalmente equivalente al método SplFixedArray::count

## Véase también

SplFixedArray::count
