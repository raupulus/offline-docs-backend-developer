---
title: Imagick::getImageType
description: Obtiene el tipo posible de imagen
source_url: https://www.php.net/manual/es/imagick.getimagetype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagetype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 34050
---

Imagick::getImageType

Obtiene el tipo posible de imagen

## Descripción

```php
public Imagick::getImageType(): int
```php

Devuelve el tipo posible de imagen.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Obtiene el tipo posible de imagen.

- `imagick::IMGTYPE_UNDEFINED`

- `imagick::IMGTYPE_BILEVEL`

- `imagick::IMGTYPE_GRAYSCALE`

- `imagick::IMGTYPE_GRAYSCALEMATTE`

- `imagick::IMGTYPE_PALETTE`

- `imagick::IMGTYPE_PALETTEMATTE`

- `imagick::IMGTYPE_TRUECOLOR`

- `imagick::IMGTYPE_TRUECOLORMATTE`

- `imagick::IMGTYPE_COLORSEPARATION`

- `imagick::IMGTYPE_COLORSEPARATIONMATTE`

- `imagick::IMGTYPE_OPTIMIZE`

## Errores/Excepciones

Lanza una ImagickException en caso de error.
