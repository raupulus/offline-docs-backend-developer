---
title: gd_info
description: Devuelve información sobre la biblioteca GD instalada
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/gd-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 8a28a068f
order: 31370
---

gd_info

Devuelve información sobre la biblioteca GD instalada

## Descripción

```php
gd_info(): array
```php

Devuelve información sobre la biblioteca GD instalada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array asociativo.

| Atributo | Significado |
|----|----|
| GD Version | `string` que describe la versión de `libgd` que está instalada. |
| FreeType Support | `bool`. `true` si el soporte FreeType está instalado. |
| FreeType Linkage | `string` que describe la forma en la que FreeType ha sido vinculado. Los valores esperados son: '`with freetype`', '`with TTF library`' y '`with unknown library`'. Este elemento solo estará definido si `FreeType Support` es evaluado `true`. |
| GIF Read Support | `bool`. `true` si el soporte para la *lectura* de imágenes `GIF` está incluido. |
| GIF Create Support | `bool`. `true` si el soporte para la *creación* de imágenes `GIF` está incluido. |
| JPEG Support | `bool`. `true` si el soporte de `JPEG` está incluido. |
| PNG Support | `bool`. `true` si el soporte de `PNG` está incluido. |
| WBMP Support | `bool`. `true` si el soporte de `WBMP` está incluido. |
| XBM Support | `bool`. `true` si el soporte de `XBM` está incluido. |
| WebP Support | Valor de tipo `bool`. `true` si el soporte `WebP` está incluido. |
| AVIF Support | Valor de tipo `bool`. `true` si el soporte `AVIF` está incluido. Disponible a partir de PHP 8.1.0. |

Elementos del array devueltos por `gd_info`

## Ejemplos

Ejemplo con `gd_info`

```
<?php
var_dump(gd_info());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(9) {
      ["GD Version"]=>
      string(24) "bundled (2.1.0 compatible)"
      ["FreeType Support"]=>
      bool(false)
      ["GIF Read Support"]=>
      bool(true)
      ["GIF Create Support"]=>
      bool(false)
      ["JPEG Support"]=>
      bool(false)
      ["PNG Support"]=>
      bool(true)
      ["WBMP Support"]=>
      bool(true)
      ["XBM Support"]=>
      bool(false)
      ["WebP Support"]=>
      bool(false)
      ["AVIF Support"]=>
      bool(false)
    }

## Véase también

imagepng

imagejpeg

imagegif

imagewbmp

imagewebp

imageavif

imagetypes
