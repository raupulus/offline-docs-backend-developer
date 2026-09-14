---
title: Imagick::setImageCompose
description: Establece el operador de composción de una imagen
source_url: https://www.php.net/manual/es/imagick.setimagecompose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagecompose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35280
---

Imagick::setImageCompose

Establece el operador de composción de una imagen

## Descripción

```php
public Imagick::setImageCompose(int $compose): bool
```php

Establece el operador de composción de una imagen, útil para especificar cómo componer la miniatura de la imagen cuando se usa el método Imagick::montageImage().

## Parámetros

`compose`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
