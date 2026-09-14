---
title: imagecreatefromtga
description: Crear una nueva imagen a partir de un fichero o una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromtga.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromtga.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 7c2251296
order: 31850
---

imagecreatefromtga

Crear una nueva imagen a partir de un fichero o una URL

## Descripción

```php
imagecreatefromtga(string $filename): GdImage
```php

`imagecreatefromtga` devuelve un objeto imagen que representa la imagen obtenida a partir del nombre de fichero proporcionado.

## Parámetros

`filename`  
Ruta de acceso a la imagen TGA Truevision.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia `GDImage`; anteriormente, se devolvía un `resource`. |
