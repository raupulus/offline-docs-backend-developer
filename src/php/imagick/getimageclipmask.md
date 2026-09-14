---
title: Imagick::getImageClipMask
description: Obtiene la máscara de recorte de la imagen
source_url: https://www.php.net/manual/es/imagick.getimageclipmask.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimageclipmask.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33600
---

Imagick::getImageClipMask

Obtiene la máscara de recorte de la imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::getImageClipMask(): Imagick
```php

Devuelve la máscara de recorte de la imagen. La máscara de recorte es un objeto Imagick que contiene la máscara de recorte. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto Imagick que contiene la máscara de recorte.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
