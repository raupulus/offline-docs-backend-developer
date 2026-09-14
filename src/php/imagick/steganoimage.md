---
title: Imagick::steganoImage
description: Oculta una marca de agua digital dentro de la imagen
source_url: https://www.php.net/manual/es/imagick.steganoimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/steganoimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35870
---

Imagick::steganoImage

Oculta una marca de agua digital dentro de la imagen

## Descripción

```php
public Imagick::steganoImage(Imagick $watermark_wand, int $offset): Imagick
```php

Oculta una marca de agua digital dentro de la imagen. Recupere la marca de agua oculta después para demostrar la autenticidad de la imagen. El parámetro offset define la posición inicial dentro de la imagen para ocultar la marca de agua.

## Parámetros

`watermark_wand`  

`offset`  

## Valores devueltos

Devuelve `true` en caso de éxito.
