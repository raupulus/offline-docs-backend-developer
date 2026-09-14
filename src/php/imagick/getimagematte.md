---
title: Imagick::getImageMatte
description: Indica si la imagen tiene un canal mat
source_url: https://www.php.net/manual/es/imagick.getimagematte.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagematte.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33850
---

Imagick::getImageMatte

Indica si la imagen tiene un canal mat

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::getImageMatte(): bool
```php

Devuelve `true` si la imagen tiene un canal mat, y `false` en caso contrario. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.
