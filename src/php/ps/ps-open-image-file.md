---
title: ps_open_image_file
description: Abre una imagen desde un fichero
source_url: https://www.php.net/manual/es/function.ps-open-image-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-open-image-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65900
---

ps_open_image_file

Abre una imagen desde un fichero

## Descripción

```php
ps_open_image_file(resource $psdoc, string $type, string $filename, [string $stringparam], [int $intparam]): int
```php

Carga una imagen para su uso posterior.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`type`  
El tipo de la imagen. Los posibles valores son `png`, `jpeg`, o `eps`.

`filename`  
El nombre del fichero que contiene la información de la imagen.

`stringparam`  
No se utiliza.

`intparam`  
No se utiliza.

## Valores devueltos

Devuelve el identificador de la imagen, o cero en caso de error. El identificador es un número positivo mayor que 0.

## Véase también

`ps_open_image`, `ps_place_image`, `ps_close_image`
