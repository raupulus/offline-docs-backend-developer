---
title: Imagick::mapImage
description: Reemplaza los colores de una imagen con el color más cercano de una imagen
  de referencia
source_url: https://www.php.net/manual/es/imagick.mapimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/mapimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34440
---

Imagick::mapImage

Reemplaza los colores de una imagen con el color más cercano de una imagen de referencia

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::mapImage(Imagick $map, bool $dither): bool
```php

## Parámetros

`map`  

`dither`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
