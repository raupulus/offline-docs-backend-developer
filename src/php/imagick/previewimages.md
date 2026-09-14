---
title: Imagick::previewImages
description: Precisa rápidamente los parámetros apropiados para el procesamiento de
  la imagen
source_url: https://www.php.net/manual/es/imagick.previewimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/previewimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34720
---

Imagick::previewImages

Precisa rápidamente los parámetros apropiados para el procesamiento de la imagen

## Descripción

```php
public Imagick::previewImages(int $preview): bool
```php

Crea un mosaico de 9 miniaturas de la imagen especificada con la operación de proceso de imágenes aplicada en varias intensidades. Esto es de útil para precisar rápidamente un parámetro apropiado para una operación de proceso de imágenes.

## Parámetros

`preview`  
Tipo de previsualización. Véase [constantes de tipos de previsualización](#imagick.constants.preview)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
