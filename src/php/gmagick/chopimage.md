---
title: Gmagick::chopimage
description: Elimina una región de una imagen y la recorta
source_url: https://www.php.net/manual/es/gmagick.chopimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/chopimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26510
---

Gmagick::chopimage

Elimina una región de una imagen y la recorta

## Descripción

```php
public Gmagick::chopimage(int $width, int $height, int $x, int $y): Gmagick
```php

Elimina una región de una imagen y colapsa la imagen para ocupar la porción eliminada.

## Parámetros

`width`  
Ancho del área recortada.

`height`  
Alto del área recortada.

`x`  
Origen X del área recortada.

`y`  
Origen Y del área recortada.

## Valores devueltos

El objeto `Gmagick` recortado.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
