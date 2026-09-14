---
title: Imagick::setImageBackgroundColor
description: Establece el color de fondo de la imagen
source_url: https://www.php.net/manual/es/imagick.setimagebackgroundcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagebackgroundcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35190
---

Imagick::setImageBackgroundColor

Establece el color de fondo de la imagen

## Descripción

```php
public Imagick::setImageBackgroundColor(mixed $background): bool
```php

Establece el color de fondo de la imagen.

## Parámetros

`background`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que un string represente el color como un parámetro. Versiones anteriores sólo permitían un objeto ImagickPixel. |
