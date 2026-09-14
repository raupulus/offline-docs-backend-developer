---
title: Imagick::addImage
description: Añade una nueva imagen a la lista de imágenes del objeto Imagick
source_url: https://www.php.net/manual/es/imagick.addimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/addimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32640
---

Imagick::addImage

Añade una nueva imagen a la lista de imágenes del objeto Imagick

## Descripción

```php
public Imagick::addImage(Imagick $source): bool
```php

Añade una nueva imagen al objeto Imagick desde la posición actual del objeto de origen. Después de la operación la posición del iterador se mueve al final de la lista.

## Parámetros

`source`  
El objeto Imagick de origen

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
