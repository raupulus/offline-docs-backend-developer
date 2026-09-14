---
title: Gmagick::newimage
description: Crea una nueva imagen
source_url: https://www.php.net/manual/es/gmagick.newimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/newimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27230
---

Gmagick::newimage

Crea una nueva imagen

## Descripción

```php
public Gmagick::newimage(int $width, int $height, string $background, [string $format]): Gmagick
```php

Crea una nueva imagen con el color de fondo especificado.

## Parámetros

`width`  
Ancho de la nueva imagen.

`height`  
Alto de la nueva imagen.

`background`  
El color de fondo a utilizar para la imagen (en forma de número de punto flotante).

`format`  
El formato de la imagen.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
