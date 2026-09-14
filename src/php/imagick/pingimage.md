---
title: Imagick::pingImage
description: Trae los atributos básicos de una imagen
source_url: https://www.php.net/manual/es/imagick.pingimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/pingimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34670
---

Imagick::pingImage

Trae los atributos básicos de una imagen

## Descripción

```php
public Imagick::pingImage(string $filename): bool
```php

Este método se puede usar para preguntar por el ancho, alto, tamaño y formato de la imagen sin leer toda la imagen de la memoria.

## Parámetros

`filename`  
El nombre de fichero de donde se va a leer la información.

## Valores devueltos

Devuelve `true` en caso de éxito.
