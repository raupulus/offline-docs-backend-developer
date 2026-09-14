---
title: Imagick::__toString
description: Devuelve la imagen como un string
source_url: https://www.php.net/manual/es/imagick.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/toString.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 35960
---

Imagick::\_\_toString

Devuelve la imagen como un string

## Descripción

```php
public Imagick::__toString(): string
```php

Devuelve la imagen actual como un string. Solamente devolverá una única imagen; no debería usarse con objetos Imagick que contengan varias imágenges, p.ej., un GIF animado o un PDF con varias páginas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del string en caso de éxito o un string vacío en caso de fallo.

## Véase también

Imagick::getImageBlob

Imagick::getImagesBlob
