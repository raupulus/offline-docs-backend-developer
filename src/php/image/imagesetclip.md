---
title: imagesetclip
description: Establece el rectángulo de recorte
source_url: https://www.php.net/manual/es/function.imagesetclip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesetclip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: fcd921429
order: 32330
---

imagesetclip

Establece el rectángulo de recorte

## Descripción

```php
imagesetclip(GdImage $image, int $x1, int $y1, int $x2, int $y2): true
```php

`imagesetclip` establece el rectángulo de recorte actual, es decir, el área más allá de la cual ningún píxel será dibujado.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x1`  
La coordenada x de la esquina superior izquierda.

`y1`  
La coordenada y de la esquina superior izquierda.

`x2`  
La coordenada x de la esquina inferior derecha.

`y2`  
La coordenada y de la esquina inferior derecha.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Véase también

imagegetclip
