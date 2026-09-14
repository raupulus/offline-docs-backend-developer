---
title: imagescale
description: Redimensiona una imagen utilizando una altura y una anchura proporcionadas
source_url: https://www.php.net/manual/es/function.imagescale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagescale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: ccd3e68e1
order: 32310
---

imagescale

Redimensiona una imagen utilizando una altura y una anchura proporcionadas

## Descripción

```php
imagescale(GdImage $image, int $width, [int $height], [int $mode]): GdImage
```php

`imagescale` redimensiona una imagen utilizando el algoritmo de interpolación dado.

> [!NOTE]
> A diferencia de muchas otras funciones de imagen, `imagescale` no modifica la `image` proporcionada; en su lugar, se devuelve una *nueva* imagen.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`width`  
La anchura a utilizar para el redimensionamiento de la imagen.

`height`  
La altura a utilizar para el redimensionamiento de la imagen. Si se omite o es negativa, se preservará la relación de aspecto de la imagen.

`mode`  
Una de las constantes `IMG_NEAREST_NEIGHBOUR`, `IMG_BILINEAR_FIXED`, `IMG_BICUBIC`, `IMG_BICUBIC_FIXED` o cualquier otra (utilizará dos pasadas).

> [!NOTE]
> `IMG_WEIGHTED4` aún no está soportado.

## Valores devueltos

Devuelve el objeto de la imagen redimensionada en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Genera una `ValueError` si `width` o `height` provoca un desbordamiento o un subdesbordamiento.

Genera una `ValueError` si `mode` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora genera una `ValueError` si `width` o `height` provoca un desbordamiento o un subdesbordamiento. |
| 8.4.0 | Ahora genera una `ValueError` si `mode` es inválido. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage`; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Véase también

imagecopyresized

imagecopyresampled
