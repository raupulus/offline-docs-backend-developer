---
title: Imagick::setImageMatte
description: Establece el canal mate de la imagen
source_url: https://www.php.net/manual/es/imagick.setimagematte.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagematte.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35440
---

Imagick::setImageMatte

Establece el canal mate de la imagen

## Descripción

```php
public Imagick::setImageMatte(bool $matte): bool
```php

Establece el canal mate de la imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`matte`  
Si es true activa el canal mate y si es false lo deshabilita.

## Valores devueltos

Devuelve `true` en caso de éxito.
