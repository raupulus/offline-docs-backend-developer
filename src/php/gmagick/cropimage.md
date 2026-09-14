---
title: Gmagick::cropimage
description: Extrae una región de la imagen
source_url: https://www.php.net/manual/es/gmagick.cropimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/cropimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26560
---

Gmagick::cropimage

Extrae una región de la imagen

## Descripción

```php
public Gmagick::cropimage(int $width, int $height, int $x, int $y): Gmagick
```php

Extrae una región de la imagen.

## Parámetros

`width`  
El ancho del recorte.

`height`  
El alto del recorte.

`x`  
La coordenada X de la esquina superior izquierda de la región recortada.

`y`  
La coordenada Y de la esquina superior izquierda de la región recortada.

## Valores devueltos

El objeto `Gmagick` recortado

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
