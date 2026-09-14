---
title: ImagickPixelIterator::newPixelRegionIterator
description: Devuelve un nuevo iterador de píxeles
source_url: https://www.php.net/manual/es/imagickpixeliterator.newpixelregioniterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixeliterator/newpixelregioniterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37800
---

ImagickPixelIterator::newPixelRegionIterator

Devuelve un nuevo iterador de píxeles

## Descripción

```php
public ImagickPixelIterator::newPixelRegionIterator(Imagick $wand, int $x, int $y, int $columns, int $rows): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Devuelve un nuevo iterador de píxeles.

## Parámetros

`wand`  

`x`  

`y`  

`columns`  

`rows`  

## Valores devueltos

Devuelve un nuevo `ImagickPixelIterator` en caso de éxito o lanza una excepción `ImagickPixelIteratorException` si ocurre un error.
