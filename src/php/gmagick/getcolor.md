---
title: GmagickPixel::getcolor
description: Devuelve el color
source_url: https://www.php.net/manual/es/gmagickpixel.getcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagickpixel/getcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 28240
---

GmagickPixel::getcolor

Devuelve el color

## Descripción

```php
public GmagickPixel::getcolor([bool $as_array], [bool $normalize_array]): mixed
```php

Devuelve el color descrito por el objeto `GmagickPixel`, en forma de `string` o un `array`. Si el color tiene un canal de opacidad definido, este será especificado como cuarto valor de la lista.

## Parámetros

`as_array`  
`true` para indicar que el valor devuelto debe ser un `array` en lugar de una `string`.

`normalize_array`  
`true` para normalizar los valores de color.

## Valores devueltos

Una `string` o un `array` de valores de canales, cada uno normalizado si `true` es proporcionado para `normalize_array`. Emite una excepción `GmagickPixelException` en caso de error.
