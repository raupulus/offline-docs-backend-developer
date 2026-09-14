---
title: imagegetinterpolation
description: Obtiene el método de interpolación
source_url: https://www.php.net/manual/es/function.imagegetinterpolation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegetinterpolation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 593ea510e
order: 32120
---

imagegetinterpolation

Obtiene el método de interpolación

## Descripción

```php
imagegetinterpolation(GdImage $image): int
```php

Obtiene el método de interpolación actualmente definido para la `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

Devuelve el método de interpolación.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Véase también

imagesetinterpolation
