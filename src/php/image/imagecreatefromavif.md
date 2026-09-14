---
title: imagecreatefromavif
description: Crear una nueva imagen a partir de un fichero o una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromavif.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromavif.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_revision: 4e04068f2
order: 31760
---

imagecreatefromavif

Crear una nueva imagen a partir de un fichero o una URL

## Descripción

```php
imagecreatefromavif(string $filename): GdImage
```php

`imagecreatefromavif` devuelve un objeto imagen obtenido a partir del fichero `filename`.

## Parámetros

`filename`  
Ruta de acceso a la imagen AVIF.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.
