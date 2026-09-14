---
title: ps_close_image
description: Cierra la imagen y libera la memoria
source_url: https://www.php.net/manual/es/function.ps-close-image.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-close-image.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 65670
---

ps_close_image

Cierra la imagen y libera la memoria

## Descripción

```php
ps_close_image(resource $psdoc, int $imageid): void
```php

Cierra una imagen y libera sus recursos. Una vez cerrada la imagen, ya no puede ser utilizada.

## Parámetros

`psdoc`  
Identificador de un fichero postscript devuelto por `ps_new`.

`imageid`  
Identificador de una imagen devuelto por `ps_open_image` o `ps_open_image_file`.

## Valores devueltos

Devuelve `null` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_open_image`, `ps_open_image_file`
