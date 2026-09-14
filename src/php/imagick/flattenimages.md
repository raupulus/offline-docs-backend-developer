---
title: Imagick::flattenImages
description: Fusiona una secuencia de imágenes
source_url: https://www.php.net/manual/es/imagick.flattenimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/flattenimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33250
---

Imagick::flattenImages

Fusiona una secuencia de imágenes

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::flattenImages(): Imagick
```php

Fusiona una secuencia de imágenes. Esto es práctico para combinar una serie de capas de Photoshop en una sola imagen.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
