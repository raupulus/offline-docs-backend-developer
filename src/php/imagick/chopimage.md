---
title: Imagick::chopImage
description: Borra una región de una imagen y la recorta
source_url: https://www.php.net/manual/es/imagick.chopimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/chopimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32780
---

Imagick::chopImage

Borra una región de una imagen y la recorta

## Descripción

```php
public Imagick::chopImage(int $width, int $height, int $x, int $y): bool
```php

Borra una región de una imagen y colapsa la imagen para ocupar la porción borrada.

## Parámetros

`width`  
Ancho del área cortada

`height`  
Alto del área cortada

`x`  
El punto de referencia X del área cortada

`y`  
El punto de referencia Y del área cortada

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::chopImage`:

Ejemplo de uso de Imagick::chopImage

```
<?php
/* Crear algunos objetos */
$imagen = new Imagick();
$píxel = new ImagickPixel( 'gray' );

/* Nueva imagen */
$imagen->newImage(400, 200, $píxel);

/* Cortar imagen */
$imagen->chopImage(200, 200, 0, 0);

/* Dar un formato a la imagen */
$imagen->setImageFormat('png');

/* Imprimir la imagen con cabeceras */
header('Content-type: image/png');
echo $imagen;

?>

    
```php

## Véase también

`Imagick::cropImage`
