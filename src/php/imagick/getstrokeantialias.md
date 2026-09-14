---
title: ImagickDraw::getStrokeAntialias
description: Devuelve la configuración de antialias de contorno actual
source_url: https://www.php.net/manual/es/imagickdraw.getstrokeantialias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/getstrokeantialias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0f49e97ee
order: 36400
---

ImagickDraw::getStrokeAntialias

Devuelve la configuración de antialias de contorno actual

## Descripción

```php
public ImagickDraw::getStrokeAntialias(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Devuelve la configuración antialias de contorno actual. Los perfiles contorneados tienen antialias por defecto. Cuando se deshabilita el antialias, los píxeles contorneados son puestos en el umbral para determinar si se debería usar el color de contorno o el color del lienzo subyacente.

## Valores devueltos

Devuelve `true` si el antialias está on y `false` si está off.
