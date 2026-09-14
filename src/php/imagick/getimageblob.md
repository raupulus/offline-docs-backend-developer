---
title: Imagick::getImageBlob
description: Devuelve la secuencia de imágenes como un blob
source_url: https://www.php.net/manual/es/imagick.getimageblob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageblob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33490
---

Imagick::getImageBlob

Devuelve la secuencia de imágenes como un blob

## Descripción

```php
public Imagick::getImageBlob(): string
```php

Implementa un formato directo en memoria. Devuelve la secuencia de imágenes en forma de string. El formato de la imagen determina el formato del BLOB devuelto (GIF, JPEG, PNG, etc.). Para devolver un formato diferente, utilice la función `Imagick::setImageFormat`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string que contiene las imágenes.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
