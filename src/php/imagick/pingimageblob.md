---
title: Imagick::pingImageBlob
description: Traer los atributos rápidamente
source_url: https://www.php.net/manual/es/imagick.pingimageblob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/pingimageblob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34680
---

Imagick::pingImageBlob

Traer los atributos rápidamente

## Descripción

```php
public Imagick::pingImageBlob(string $image): bool
```php

Este método se puede usar para preguntar por el ancho, alto, tamaño y formato de la imagen sin leer toda la imagen de la memoria. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`image`  
Un string que contiene la imagen.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Usar `Imagick::pingImageBlob`

Hacer ping a una imagen desde un string

```
<?php
/* leer el contenido de la imagen */
$imagen = file_get_contents("prueba.jpg");

/* crear un nuevo objeto imagick */
$im = new Imagick();

/* pasar el string al objeto imagick */
$im->pingImageBlob($imagen);

/* imprimir el ancho y alto de la image */
echo $im->getImageWidth() . 'x' . $im->getImageHeight();
?>

    
```php

## Véase también

`Imagick::pingImage`, `Imagick::pingImageFile`, `Imagick::readImage`, `Imagick::readImageBlob`, `Imagick::readImageFile`
