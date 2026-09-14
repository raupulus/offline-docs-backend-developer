---
title: Imagick::montageImage
description: Crea una imagen compuesta
source_url: https://www.php.net/manual/es/imagick.montageimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/montageimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 6ce32bdcf
order: 34500
---

Imagick::montageImage

Crea una imagen compuesta

## Descripción

```php
public Imagick::montageImage(ImagickDraw $draw, string $tile_geometry, string $thumbnail_geometry, int $mode, string $frame): Imagick
```php

Crea una imagen compuesta combinando varias imágenes. Las imágenes se utilizan como baldosas en la imagen compuesta, con su nombre opcionalmente debajo.

## Parámetros

`draw`  
El nombre de la fuente, el tamaño y el color se solicitan a este objeto.

`tile_geometry`  
El número de baldosas por filas y por página (ej. `6x4+0+0`).

`thumbnail_geometry`  
El tamaño solicitado para la imagen y su borde para cada miniatura (ej. 120x120+4+3).

`mode`  
El modo de encuadre de las miniaturas. Consulte la lista de [constantes de modo de montaje](#imagick.constants.montagemode).

`frame`  
Encuadra la imagen con un borde decorativo (ej. 15x15+3+3). La color del borde es el color mate de la miniatura.

## Valores devueltos

Crea una imagen compuesta y la devuelve como un nuevo objeto `Imagick`.
