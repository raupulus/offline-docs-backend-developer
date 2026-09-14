---
title: imagetypes
description: Devuelve los tipos de imágenes soportados por la versión actual de PHP
source_url: https://www.php.net/manual/es/function.imagetypes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagetypes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 928f05132
order: 32460
---

imagetypes

Devuelve los tipos de imágenes soportados por la versión actual de PHP

## Descripción

```php
imagetypes(): int
```php

Devuelve un campo de octetos correspondiente a los formatos de imágenes soportados por la versión de PHP utilizada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un campo de octetos correspondiente a los formatos de imágenes soportados por la versión de GD utilizada. Los valores siguientes son posibles: `IMG_AVIF` \| `IMG_BMP` \| `IMG_GIF` \| `IMG_JPG` \| `IMG_PNG` \| `IMG_WBMP` \| `IMG_XPM` \| `IMG_WEBP`.

## Historial de cambios

| Versión | Descripción                      |
|---------|----------------------------------|
| 8.1.0   | Añadida la constante `IMG_AVIF`. |
| 7.2.0   | Añadida la constante `IMG_BMP`.  |
| 7.0.10  | Añadida la constante `IMG_WEBP`. |

## Ejemplos

Ejemplo con `imagetypes`

```
<?php
if (imagetypes() & IMG_PNG) {
    echo "El tipo PNG es soportado";
}
?>

    
```php

## Véase también

gd_info
