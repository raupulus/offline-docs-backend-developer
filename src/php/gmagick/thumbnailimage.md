---
title: Gmagick::thumbnailimage
description: Modifica el tamaño de una imagen
source_url: https://www.php.net/manual/es/gmagick.thumbnailimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/thumbnailimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27820
---

Gmagick::thumbnailimage

Modifica el tamaño de una imagen

## Descripción

```php
public Gmagick::thumbnailimage(int $width, int $height, [bool $fit]): Gmagick
```php

Modifica el tamaño de una imagen a las dimensiones dadas y elimina los perfiles asociados. El objetivo es producir una imagen en miniatura, menos pesada, con fines de visualización en la Web. Si `true` se proporciona como valor del 3er argumento, entonces los argumentos `width` y `height` se utilizan como valores máximos para cada lado. Ambos lados serán escalados durante la operación.

## Parámetros

`width`  
Ancho de la imagen.

`height`  
Altura de la imagen.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
