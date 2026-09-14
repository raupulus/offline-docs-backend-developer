---
title: Imagick::getImageRegion
description: Extrae una región de la imagen
source_url: https://www.php.net/manual/es/imagick.getimageregion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageregion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33960
---

Imagick::getImageRegion

Extrae una región de la imagen

## Descripción

```php
public Imagick::getImageRegion(int $width, int $height, int $x, int $y): Imagick
```php

Extrae una región de la imagen y la devuelve como un nuevo objeto Imagick.

## Parámetros

`width`  
El ancho de la región extraída.

`height`  
El alto de la región extraída.

`x`  
Coordenada X de la esquina superior izquierda de la región extraída.

`y`  
Coordenada Y de la esquina superior izquierda de la región extraída.

## Valores devueltos

Extrae una región de la imagen y la devuleve como una nueva varita mágica.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
