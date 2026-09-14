---
title: Imagick::transformImage
description: Método conveniente para establecer el tamaño del recorte y la geometría
  de la imagen
source_url: https://www.php.net/manual/es/imagick.transformimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/transformimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35970
---

Imagick::transformImage

Método conveniente para establecer el tamaño del recorte y la geometría de la imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::transformImage(string $crop, string $geometry): Imagick
```php

Método conveniente para establecer el tamaño del recorte y la geometría de la imagen desde cadenas. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`crop`  
Un string de geometría de recorte. Esta geometría define una sub-región de la imagen a recortar.

`geometry`  
Un string de geometría de imagen. Esta geometría define el tamaño final de la imagen.

## Valores devueltos

Devuelve un objeto Imagick que contiene la imagen transformada.

## Ejemplos

Usar `Imagick::transformImage`:

El ejemplo crea una imagen negra de 100x100 black.

```
<?php
$imagen = new Imagick();
$imagen->newImage(300, 200, "black");
$imagen_nueva = $imagen->transformImage("100x100", "100x100");
$imagen_nueva->writeImage('test_out.jpg');
?>

    
```php

## Véase también

`Imagick::cropImage`, `Imagick::resizeImage`, `Imagick::thumbnailImage`
