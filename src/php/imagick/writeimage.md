---
title: Imagick::writeImage
description: Escribe una imagen al nombre de fichero especificado
source_url: https://www.php.net/manual/es/imagick.writeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/writeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 36090
---

Imagick::writeImage

Escribe una imagen al nombre de fichero especificado

## Descripción

```php
public Imagick::writeImage([string $filename]): bool
```php

Escribe una imagen al nombre de fichero especificado. Si el parámetro 'filename' es NULL, la imagen se escribe en el nombre de fichero establecido por Imagick::readImage() o Imagick::setImageFilename().

## Parámetros

`filename`  
Nombre del fichero donde escribir la imagen. La extensión del nombre de fichero define el tipo del fichero. El formato puede ser forzado independientemente del formato que use la extensión del fichero: usando un prefijo, por ejemplo "jpg:test.png".

## Valores devueltos

Devuelve `true` en caso de éxito.
