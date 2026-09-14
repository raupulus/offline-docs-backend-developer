---
title: Gmagick::readimageblob
description: Lee una imagen desde una cadena binaria
source_url: https://www.php.net/manual/es/gmagick.readimageblob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/readimageblob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27380
---

Gmagick::readimageblob

Lee una imagen desde una cadena binaria

## Descripción

```php
public Gmagick::readimageblob(string $imageContents, [string $filename]): Gmagick
```php

Lee una imagen desde una cadena binaria.

## Parámetros

`imageContents`  
Contenido de la imagen.

`filename`  
El nombre del fichero de imagen.

## Valores devueltos

Un objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
