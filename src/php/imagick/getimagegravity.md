---
title: Imagick::getImageGravity
description: Obtiene la gravedad de la imagen
source_url: https://www.php.net/manual/es/imagick.getimagegravity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagegravity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33760
---

Imagick::getImageGravity

Obtiene la gravedad de la imagen

## Descripción

```php
public Imagick::getImageGravity(): int
```php

Obtiene el valor de la gravedad actual de la imagen. A diferencia del método `Imagick::getGravity`, este método devuelve la gravedad definida para la secuencia actual de la imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la propiedad de gravedad de la imagen. Consúltese la lista de [constantes de gravedad](#imagick.constants.gravity).
