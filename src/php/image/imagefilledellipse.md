---
title: imagefilledellipse
description: Dibuja una elipse llena
source_url: https://www.php.net/manual/es/function.imagefilledellipse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefilledellipse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31980
---

imagefilledellipse

Dibuja una elipse llena

## Descripción

```php
imagefilledellipse(GdImage $image, int $center_x, int $center_y, int $width, int $height, int $color): true
```php

Dibuja una elipse centrada en las coordenadas especificadas sobre la imagen proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`center_x`  
X: coordenada del centro.

`center_y`  
Y: coordenada del centro.

`width`  
El ancho de la elipse.

`height`  
La altura de la elipse.

`color`  
El color de relleno. Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagefilledellipse`

```
<?php

// Nueva imagen
$image = imagecreatetruecolor(400, 300);

// Color de fondo
$bg = imagecolorallocate($image, 0, 0, 0);

// Color de relleno de la elipse
$col_ellipse = imagecolorallocate($image, 255, 255, 255);

// Se dibuja la elipse blanca
imagefilledellipse($image, 200, 150, 300, 200, $col_ellipse);

// Se muestra la imagen
header("Content-type: image/png");
imagepng($image);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagefilledellipse()](en/reference/image/figures/imagefilledellipse.png)

## Notas

> [!NOTE]
> `imagefilledellipse` ignora `imagesetthickness`.

## Véase también

imageellipse

imagefilledarc
