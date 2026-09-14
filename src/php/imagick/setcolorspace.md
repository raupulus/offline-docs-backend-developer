---
title: Imagick::setColorspace
description: Establecer el espacio de color
source_url: https://www.php.net/manual/es/imagick.setcolorspace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setcolorspace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35070
---

Imagick::setColorspace

Establecer el espacio de color

## Descripción

```php
public Imagick::setColorspace(int $COLORSPACE): bool
```php

Establece el valor del espacio de color global para el objeto. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.5.7 o superior.

## Parámetros

`COLORSPACE`  
Una de las [constantes COLORSPACE](#imagick.constants.colorspace)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
