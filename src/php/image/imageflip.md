---
title: imageflip
description: Devuelve una imagen utilizando el modo proporcionado
source_url: https://www.php.net/manual/es/function.imageflip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageflip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: fcd921429
order: 32030
---

imageflip

Devuelve una imagen utilizando el modo proporcionado

## Descripción

```php
imageflip(GdImage $image, int $mode): true
```php

Devuelve la imagen `image` utilizando el `mode` proporcionado.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`mode`  
Modo de volteo; puede ser una de las constantes `IMG_FLIP_*`:

| Constante | Significado |
|----|----|
| `IMG_FLIP_HORIZONTAL` | Voltea la imagen horizontalmente. |
| `IMG_FLIP_VERTICAL` | Voltea la imagen verticalmente. |
| `IMG_FLIP_BOTH` | Voltea la imagen tanto horizontal como verticalmente. |

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Voltear una imagen verticalmente

Este ejemplo utiliza la constante `IMG_FLIP_VERTICAL`.

```
<?php
// Archivo
$filename = 'phplogo.png';

// Tipo de contenido
header('Content-type: image/png');

// Carga
$im = imagecreatefrompng($filename);

// Volteo vertical
imageflip($im, IMG_FLIP_VERTICAL);

// Mostrar
imagejpeg($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo: Imagen volteada verticalmente](en/reference/image/figures/imageflipvertical.png)

Voltear una imagen horizontalmente

Este ejemplo utiliza la constante `IMG_FLIP_HORIZONTAL`.

```
<?php
// Archivo
$filename = 'phplogo.png';

// Tipo de contenido
header('Content-type: image/png');

// Carga
$im = imagecreatefrompng($filename);

// Volteo horizontal
imageflip($im, IMG_FLIP_HORIZONTAL);

// Mostrar
imagejpeg($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo: Imagen volteada horizontalmente](en/reference/image/figures/imagefliphorizontal.png)
