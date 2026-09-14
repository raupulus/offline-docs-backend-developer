---
title: Gmagick::writeimage
description: Escribe una imagen en un archivo
source_url: https://www.php.net/manual/es/gmagick.writeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/writeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27850
---

Gmagick::writeimage

Escribe una imagen en un archivo

## Descripción

```php
public Gmagick::writeimage(string $filename, [bool $all_frames]): Gmagick
```php

Escribe una imagen en un archivo específico. Si el argumento `filename` es `null`, la imagen será escrita en el archivo definido por el método Gmagick::readimage o el método Gmagick::setimagefilename.

## Parámetros

`filename`  
El nombre del archivo.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
