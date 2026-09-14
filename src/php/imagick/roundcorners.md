---
title: Imagick::roundCorners
description: Redondea las esquinas de una imagen
source_url: https://www.php.net/manual/es/imagick.roundcorners.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/roundcorners.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 34990
---

Imagick::roundCorners

Redondea las esquinas de una imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::roundCorners(float $x_rounding, float $y_rounding, [float $stroke_width], [float $displace], [float $size_correction]): bool
```php

Redondea las esquinas de una imagen. Los dos primeros argumentos controlan el nivel de redondeo, y el tercero puede ser utilizado para afinar este proceso. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior. Este método no está disponible si Imagick ha sido compilado con ImageMagick versión 7.0.0 o superior.

## Parámetros

`x_rounding`  
Redondeo en x

`y_rounding`  
Redondeo en y

`stroke_width`  
Ancho del trazo

`displace`  
Desplazamiento de la imagen

`size_correction`  
Corrección de tamaño

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::roundCorners`:

Redondea las esquinas de una imagen.

```
<?php

$image = new Imagick();
$image->newPseudoImage(100, 100, "magick:rose");
$image->setImageFormat("png");

$image->roundCorners(5,3);
$image->writeImage("rounded.png");
?>

    
```php
