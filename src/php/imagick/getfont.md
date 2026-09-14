---
title: Imagick::getFont
description: Obtiene la fuente de caracteres
source_url: https://www.php.net/manual/es/imagick.getfont.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getfont.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33400
---

Imagick::getFont

Obtiene la fuente de caracteres

## Descripción

```php
public Imagick::getFont(): string
```php

Devuelve la propiedad de la fuente de caracteres del objeto. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.7 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` que contiene el nombre de la fuente de caracteres o `false` si la fuente no está definida.

## Véase también

`Imagick::setFont`, `ImagickDraw::setFont`, `ImagickDraw::getFont`
