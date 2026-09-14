---
title: Imagick::animateImages
description: Anima una imagen o imágenes
source_url: https://www.php.net/manual/es/imagick.animateimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/animateimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32670
---

Imagick::animateImages

Anima una imagen o imágenes

## Descripción

```php
public Imagick::animateImages(string $x_server): bool
```php

Este método anima la imagen en un servidor X local o remoto. Este método no está disponible en Windows. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`x_server`  
La dirección del servidor X

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

`Imagick::displayImage`
