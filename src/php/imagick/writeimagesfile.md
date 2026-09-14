---
title: Imagick::writeImagesFile
description: Escribe los frames en un descriptor de ficheros
source_url: https://www.php.net/manual/es/imagick.writeimagesfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/writeimagesfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 20ddc39b6
order: 36120
---

Imagick::writeImagesFile

Escribe los frames en un descriptor de ficheros

## Descripción

```php
public Imagick::writeImagesFile(resource $filehandle, [string $format]): bool
```php

Escribe todas las frames de una imagen en un descriptor de fichero. Este método puede ser utilizado para escribir gifs animados u otras imágenes compuestas por múltiples frames en un descriptor de fichero abierto. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`filehandle`  
Descriptor de fichero en el que se escribirán las frames.

`format`  
El formato de la imagen. La lista de especificadores de formato válidos depende del conjunto de características compiladas de ImageMagick, y puede ser consultada en tiempo de ejecución mediante Imagick::queryFormats.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

Imagick::queryFormats
