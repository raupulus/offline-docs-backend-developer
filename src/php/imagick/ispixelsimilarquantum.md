---
title: ImagickPixel::isPixelSimilarQuantum
description: Indica si dos colores difieren en menos de la distancia especificada
source_url: https://www.php.net/manual/es/imagickpixel.ispixelsimilarquantum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/ispixelsimilarquantum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1534707f6
order: 37620
---

ImagickPixel::isPixelSimilarQuantum

Indica si dos colores difieren en menos de la distancia especificada

## Descripción

```php
public ImagickPixel::isPixelSimilarQuantum(string $color, [string $fuzz]): bool
```php

Indica si dos colores difieren en menos de la distancia especificada. El valor de flou debe estar comprendido entre 0 y QuantumRange. El valor máximo representa la distancia más larga posible en el espacio colorimétrico. Por ejemplo, de RGB(0, 0, 0) a RGB(255, 255, 255) para el espacio colorimétrico RGB

## Parámetros

`color`  

`fuzz`  

## Valores devueltos
