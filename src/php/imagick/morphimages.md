---
title: Imagick::morphImages
description: Metamorfosea un conjunto de imágenes
source_url: https://www.php.net/manual/es/imagick.morphimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/morphimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34510
---

Imagick::morphImages

Metamorfosea un conjunto de imágenes

## Descripción

```php
public Imagick::morphImages(int $number_frames): Imagick
```php

Metamorfosea un conjunto de imágenes. Los píxeles de la imagen y el tamaño son interpolados linealmente para dar la apariencia de una metamorfosis desde una imagen a la siguiente.

## Parámetros

`number_frames`  
El número de imágenes intermedias a generar.

## Valores devueltos

Este método devuelve un nuevo objeto Imagick si se tuvo éxito. Emite una excepción `ImagickException` en caso de fallo.
