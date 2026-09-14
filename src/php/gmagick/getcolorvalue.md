---
title: GmagickPixel::getcolorvalue
description: Obtiene el valor normalizado del canal de color proporcionado
source_url: https://www.php.net/manual/es/gmagickpixel.getcolorvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagickpixel/getcolorvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 28260
---

GmagickPixel::getcolorvalue

Obtiene el valor normalizado del canal de color proporcionado

## Descripción

```php
public GmagickPixel::getcolorvalue(int $color): float
```php

Obtiene el valor normalizado del canal de color proporcionado, en forma de número de punto flotante comprendido entre 0 y 1.

## Parámetros

`color`  
El canal a verificar, especificado en forma de una de las constantes de canal Gmagick.

## Valores devueltos

El valor del canal, en forma de número de punto flotante normalizado, y emite una excepción `GmagickPixelException` en caso de error.
