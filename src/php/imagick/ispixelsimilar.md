---
title: ImagickPixel::isPixelSimilar
description: Verifica la distancia entre este color y otro
source_url: https://www.php.net/manual/es/imagickpixel.ispixelsimilar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/ispixelsimilar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: fa0c88f1e
order: 37610
---

ImagickPixel::isPixelSimilar

Verifica la distancia entre este color y otro

## Descripción

```php
public ImagickPixel::isPixelSimilar(ImagickPixel $color, float $fuzz): bool
```php

Verifica la distancia entre el color descrito por este objeto ImagickPixel y el del objeto proporcionado. Si la distancia entre los dos puntos es inferior al valor del argumento fuzz proporcionado, el color es similar. Este método reemplaza al método [ImagickPixel::isSimilar()](#imagickpixel.issimilar) y normaliza correctamente el valor fuzz de ImageMagick QuantumRange.

## Parámetros

`color`  
El objeto ImagickPixel a utilizar para la comparación.

`fuzz`  
La distancia máxima para la cual se consideran los colores como similares. El valor máximo teórico para este argumento es la raíz cuadrada de tres (1.732).

## Valores devueltos

Devuelve `true` en caso de éxito.
