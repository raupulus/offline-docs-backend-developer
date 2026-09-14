---
title: Imagick::setSizeOffset
description: Establece el tamaño y el índice del objeto Imagick
source_url: https://www.php.net/manual/es/imagick.setsizeoffset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setsizeoffset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35720
---

Imagick::setSizeOffset

Establece el tamaño y el índice del objeto Imagick

## Descripción

```php
public Imagick::setSizeOffset(int $columns, int $rows, int $offset): bool
```php

Establece el tamaño y el índice del objeto Imagick. Se debe establecer antes de leer un formato de imagen en bruto como RGB, GRAY, o CMYK. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`columns`  
El ancho en píxeles.

`rows`  
El alto en píxeles.

`offset`  
El índice de la imagen.

## Valores devueltos

Devuelve `true` en caso de éxito.
