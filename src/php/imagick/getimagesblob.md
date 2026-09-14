---
title: Imagick::getImagesBlob
description: Devuelve todas las imágenes de la secuencia en un BLOB
source_url: https://www.php.net/manual/es/imagick.getimagesblob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagesblob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33990
---

Imagick::getImagesBlob

Devuelve todas las imágenes de la secuencia en un BLOB

## Descripción

```php
public Imagick::getImagesBlob(): string
```php

Implementa el formato directo en memoria. Devuelve todas las imágenes de la secuencia en forma de cadena. El formato de la imagen determina el formato del BLOB devuelto (GIF, JPEG, PNG, etc.). Para devolver un formato de imagen diferente, utilice `Imagick::setImageFormat`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una cadena que contiene todas las imágenes. Emite una excepción `ImagickException` en caso de fallo.
