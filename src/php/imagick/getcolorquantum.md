---
title: ImagickPixel::getColorQuantum
description: Devuelve el color del píxel en un array como valores cuánticos
source_url: https://www.php.net/manual/es/imagickpixel.getcolorquantum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/getcolorquantum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 37560
---

ImagickPixel::getColorQuantum

Devuelve el color del píxel en un array como valores cuánticos

## Descripción

```php
public ImagickPixel::getColorQuantum(): array
```php

Devuelve el color del píxel en un array como valores cuánticos. Si ImageMagick ha sido compilado como HDRI, estos valores serán floats, de lo contrario serán integers.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con las claves `"r"`, `"g"`, `"b"`, `"a"`.
