---
title: imagesetthickness
description: Modifica el grosor de una línea
source_url: https://www.php.net/manual/es/function.imagesetthickness.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesetthickness.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: d56953fc8
order: 32370
---

imagesetthickness

Modifica el grosor de una línea

## Descripción

```php
imagesetthickness(GdImage $image, int $thickness): true
```php

`imagesetthickness` modifica el grosor de las líneas en la imagen `image`. Este grosor se aplica en los dibujos de polígonos, círculos, rectángulos, etc. `thickness` se expresa en píxeles.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`thickness`  
El grosor, en píxeles.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagesetthickness`

```
<?php

// Creación de una imagen de 200x100
$im = imagecreatetruecolor(200, 100);
$white = imagecolorallocate($im, 0xFF, 0xFF, 0xFF);
$black = imagecolorallocate($im, 0x00, 0x00, 0x00);

// Establece el fondo en blanco
imagefilledrectangle($im, 0, 0, 199, 99, $white);

// Establece el grosor de la línea a 5
imagesetthickness($im, 5);

// Dibuja el rectángulo
imagerectangle($im, 14, 14, 185, 85, $black);

// Muestra la imagen en el navegador
header('Content-Type: image/png');

imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagesetthickness()](en/reference/image/figures/imagesetthickness.png)
