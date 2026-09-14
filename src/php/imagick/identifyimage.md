---
title: Imagick::identifyImage
description: Identifica una imagen y obtiene sus atributos
source_url: https://www.php.net/manual/es/imagick.identifyimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/identifyimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 10a34d49b
order: 34340
---

Imagick::identifyImage

Identifica una imagen y obtiene sus atributos

## Descripción

```php
public Imagick::identifyImage([bool $appendRawOutput]): array
```php

Identifica una imagen y devuelve los atributos. Los atributos incluyen el ancho, alto, tamaño de la imagen, entre otros.

## Parámetros

`appendRawOutput`  
Si es `true`, la salida bruta se agrega al array.

## Valores devueltos

Identifica una imagen y devuelve los atributos. Los atributos incluyen el ancho, alto, tamaño de la imagen, entre otros.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo de formato resultante

    Array
    (
        [imageName] => /some/path/image.jpg
        [format] => JPEG (Joint Photographic Experts Group JFIF format)
        [geometry] => Array
            (
                [width] => 90
                [height] => 90
            )

        [type] => TrueColor
        [colorSpace] => RGB
        [resolution] => Array
            (
                [x] => 300
                [y] => 300
            )

        [units] => PixelsPerInch
        [fileSize] => 1.88672kb
        [compression] => JPEG
        [signature] => 9a6dc8f604f97d0d691c0286176ddf992e188f0bebba98494b2146ee2d7118da
    )
