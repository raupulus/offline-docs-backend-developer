---
title: Imagick::setResolution
description: Establece la resolución de la imagen
source_url: https://www.php.net/manual/es/imagick.setresolution.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setresolution.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35680
---

Imagick::setResolution

Establece la resolución de la imagen

## Descripción

```php
public Imagick::setResolution(float $x_resolution, float $y_resolution): bool
```php

Establece la resolución de la imagen.

## Parámetros

`x_resolution`  
La resolución horizontal.

`y_resolution`  
La resolución vertical.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Notas

Imagick::setResolution se debe invocar antes de cargar o crear una imagen.

## Véase también

Imagick::setImageResolution

Imagick::getImageResolution
