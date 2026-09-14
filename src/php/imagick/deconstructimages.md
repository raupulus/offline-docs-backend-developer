---
title: Imagick::deconstructImages
description: Devuelve las diferencias de ciertos píxeles entre dos imágenes
source_url: https://www.php.net/manual/es/imagick.deconstructimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/deconstructimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33060
---

Imagick::deconstructImages

Devuelve las diferencias de ciertos píxeles entre dos imágenes

## Descripción

```php
public Imagick::deconstructImages(): Imagick
```php

Compara cada imagen con la siguiente en la secuencia, y devuelve la región máxima de encuadre de los píxeles diferentes que descubre.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un nuevo objeto Imagick en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
