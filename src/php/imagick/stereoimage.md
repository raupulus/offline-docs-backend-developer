---
title: Imagick::stereoImage
description: Compone dos imágenes
source_url: https://www.php.net/manual/es/imagick.stereoimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/stereoimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35880
---

Imagick::stereoImage

Compone dos imágenes

## Descripción

```php
public Imagick::stereoImage(Imagick $offset_wand): bool
```php

Compone dos imágenes y produce una sóla imagen que es la composición de una imagen izquierda y derecha de una pareja estéreo.

## Parámetros

`offset_wand`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
