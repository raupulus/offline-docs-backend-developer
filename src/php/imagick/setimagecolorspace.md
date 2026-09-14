---
title: Imagick::setImageColorspace
description: Establece el espacio de color de una imagen
source_url: https://www.php.net/manual/es/imagick.setimagecolorspace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagecolorspace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35270
---

Imagick::setImageColorspace

Establece el espacio de color de una imagen

## Descripción

```php
public Imagick::setImageColorspace(int $colorspace): bool
```php

Establece el espacio de color de una imagen. Este método debería emplearse al crear imágenes nuevas. Para cambiar el espacio de color de una imagen existente se debería utilizar Imagick::transformImageColorspace.

## Parámetros

`colorspace`  
Una de las [constantes COLORSPACE](#imagick.constants.colorspace)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
