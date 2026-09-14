---
title: ps_place_image
description: Colocar una imágen en la página
source_url: https://www.php.net/manual/es/function.ps-place-image.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-place-image.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65930
---

ps_place_image

Colocar una imágen en la página

## Descripción

```php
ps_place_image(resource $psdoc, int $imageid, float $x, float $y, float $scale): bool
```php

Coloca una imagen cargada anteriormente en la página. La imagen puede ser redimensionada. Si la imagen también debe rotarse, se ha de rotar antes el sistema de coordenadas con la función `ps_rotate`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`imageid`  
El identificador de recursos de la imagen, como el devuelto por las funciones `ps_open_image` o `ps_open_image_file`.

`x`  
La coordenada x de la esquina inferior izquierda de la imagen.

`y`  
La coordenada y de la esquina inferior izquierda de la imagen.

`scale`  
El factor de escala de la imagen. Una escala de 1.0 resultará en una resolución de 72 dpi, ya que cada píxel es equivalente a 1 punto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_open_image`, `ps_open_image_file`
