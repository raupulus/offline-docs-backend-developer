---
title: Imagick::cropThumbnailImage
description: Crea una miniatura recortada
source_url: https://www.php.net/manual/es/imagick.cropthumbnailimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/cropthumbnailimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33020
---

Imagick::cropThumbnailImage

Crea una miniatura recortada

## Descripción

```php
public Imagick::cropThumbnailImage(int $width, int $height, [bool $legacy]): bool
```php

Crea una miniatura de tamaño fijo ampliando o reduciendo de escala la imagen y recortando un área específica desde el centro.

## Parámetros

`width`  
El ancho de la miniatura

`height`  
El alto de la miniatura

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
