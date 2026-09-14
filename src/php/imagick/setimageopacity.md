---
title: Imagick::setImageOpacity
description: Establece el nivel de opacidad de la imagen
source_url: https://www.php.net/manual/es/imagick.setimageopacity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageopacity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35460
---

Imagick::setImageOpacity

Establece el nivel de opacidad de la imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::setImageOpacity(float $opacity): bool
```php

Establece el nivel de opacidad de la imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.1 o superior. Este método opera en todos los canales, lo que significa que, por ejemplo, un valor de la opacidad de 0.5 establecerá todas las áreas transparentes a parcialmente opacas. Para añadir transparencia a áreas que no lo son ya, use [Imagick::evaluateImage()](#imagick.evaluateimage)

## Parámetros

`opacity`  
El nivel de transpariencia: 1.0 es completamente opaco y 0.0 es completamente transparente.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Un ejemplo de `Imagick::setImageOpacity`

Un ejemplo usando Imagick::setImageOpacity()

```
<?php
/* Crear el objeto */
$imagen = new Imagick('origen.png');

/* Establecer la opacidad */
$imagen->setImageOpacity(0.7);

/* Mostrar la imagen */
header('Content-type: image/png');
echo $imagen;

?>

    
```php
