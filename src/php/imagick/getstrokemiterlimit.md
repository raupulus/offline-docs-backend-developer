---
title: ImagickDraw::getStrokeMiterLimit
description: Devuelve el valor de 'miterLimit'
source_url: https://www.php.net/manual/es/imagickdraw.getstrokemiterlimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/getstrokemiterlimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 36460
---

ImagickDraw::getStrokeMiterLimit

Devuelve el valor de 'miterLimit'

## Descripción

```php
public ImagickDraw::getStrokeMiterLimit(): int
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Devuelve el valor de 'miterLimit'. Cuando dos segmentos se encuentran en ángulo agudo y se ha especificado que las uniones miter para `'lineJoin'`, es posible que el miter exceda el grosor del trazo del camino. La 'miterLimit' establece un límite al ratio entre la longitud del miter y `'lineWidth'`.

## Valores devueltos

Devuelve un entero que describe el valor de 'miterLimit', y 0 si la 'miterLimit' no está configurada.
